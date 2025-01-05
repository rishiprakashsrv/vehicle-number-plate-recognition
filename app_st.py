import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from twilio.rest import Client
import csv
import os

def image_gen(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, bla = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    blur = cv2.bilateralFilter(gray, 25, 105, 110)
    img = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(img, 100, 100)

    cnts, _ = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1000]
    
    plate = None
    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        edges_count = cv2.approxPolyDP(c, 0.02 * perimeter, True)
        if len(edges_count) == 4:
            x, y, w, h = cv2.boundingRect(c)
            plate = image[y:y+h, x:x+w]
            break
    
    if plate is not None:
        cv2.imwrite("data/images/plate.png", plate)
        return plate
    else:
        st.error("License plate could not be detected.")
        return None

def image_plate_no():
    plate_image = cv2.imread("data/images/plate.png")
    text = pytesseract.image_to_string(plate_image, lang="eng")
    return text.replace(" ", "").strip()

import csv
import os

def find_driver_details(license_number):
    csv_file = "data/drivers.csv"  
    
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"{csv_file} not found. Please check the file path.")
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['License_Number'] == license_number:
                return {
                    'Car_Owner': row['Car_Owner'],
                    'Vehicle': row['Vehicle'],
                    'Phone': row['Phone']
                }
    return None


def send_sms(to_phone, body):
    ACCOUNT_SID = 'AC3fabe0f6eddf041146aaf487556xxxxx'
    AUTH_TOKEN = 'b4d3c34de30fefb5086def3d3d0xxxxx'
    TWILIO_PHONE_NUMBER = '+1231625xxxx'
    
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body=body, from_=TWILIO_PHONE_NUMBER, to=to_phone)
    return message

st.title("Vehicle Number Plate Recognition System")

uploaded_file = st.file_uploader("Upload an image of a vehicle", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Process Image"):
        plate = image_gen(image)
        if plate is not None:
            st.image(plate, caption="Detected License Plate", use_column_width=True)
            license_number = image_plate_no()
            st.write(f"Detected License Plate Number: {license_number}")
            
            owner, vehicle, phone = find_driver_details(license_number)
            if owner and phone:
                st.success(f"Owner: {owner}, Vehicle: {vehicle}, Phone: {phone}")
                fine_amount = st.text_input("Enter fine amount:", value="100")
                if st.button("Send SMS"):
                    message_body = f"Dear {owner},\nYou have been charged with a speeding ticket. Fine amount Rs {fine_amount} for vehicle {vehicle}. License Number - {license_number}. Please submit the amount at the nearest traffic stop to avoid further penalty!"
                    response = send_sms(phone, message_body)
                    st.success(f"Message sent to {phone}: {response.sid}")
            else:
                st.error("No matching driver details found.")
