# Vehicle Number Plate Recognition and Notification System

This project implements a **Vehicle Number Plate Recognition System** using image processing and machine learning techniques. The system detects vehicle number plates from images, performs Optical Character Recognition (OCR) to extract the license plate numbers, and sends notifications to vehicle owners based on their license number. The application utilizes **OpenCV**, **Tesseract OCR**, and **Twilio API** for deployment.

### Key Features:
- **Vehicle Number Plate Detection** from images.
- **OCR (Optical Character Recognition)** to extract license plate numbers.
- **Send SMS Notifications** to vehicle owners using **Twilio API**.
- User-friendly interface built with **Streamlit**.
- Ability to **retrieve vehicle owner details** from a CSV file.

### Technology Stack

- **Python**: Main programming language for developing the system.
- **OpenCV**: Used for image processing and number plate detection.
- **Tesseract OCR**: For extracting text from the detected vehicle number plate.
- **Twilio API**: For sending SMS notifications to vehicle owners.
- **Streamlit**: Framework for building the interactive web application.
- **CSV**: For storing vehicle owner details (car owner, vehicle, phone).

## Installation & Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/vehicle-number-plate-recognition.git
    cd vehicle-number-plate-recognition
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

    The required libraries include:
    - `opencv-python` for image processing.
    - `pytesseract` for Optical Character Recognition.
    - `twilio` for SMS functionality.
    - `streamlit` for creating the web app.
    - `pandas` for handling CSV files.

3. **Prepare Data**:
    - The project uses `drivers.csv` to store vehicle owner details (name, vehicle, phone number). Ensure this file is present in the project directory.

4. **Run the application locally**:
    ```bash
    streamlit run app.py
    ```

    The Streamlit app will start and open in your browser at `http://localhost:8501`.

## How It Works

1. **Upload an Image**:
   - Upload an image of a vehicle number plate via the Streamlit web interface.

2. **Number Plate Detection**:
   - The system processes the image and detects the number plate using image processing techniques such as edge detection, contour finding, and Gaussian blur.

3. **OCR Extraction**:
   - Once the number plate is detected, the system uses **Tesseract OCR** to extract the license plate number.

4. **Lookup Vehicle Owner Details**:
   - The extracted license plate number is compared with records in the `drivers.csv` file to find the corresponding vehicle owner details.

5. **Send SMS Notification**:
   - Once a matching vehicle owner is found, an SMS notification is sent to the registered phone number using the **Twilio API**. The message informs the user about a speeding violation or similar traffic-related issue.

## Deployment

The application is deployed and can be accessed locally through the Streamlit framework.

1. **Launch the app**:
   - Once the app is running, users can upload an image of a vehicle.
   - The app detects the vehicle’s license plate, extracts the number, looks up the owner’s details, and sends a notification.

## Image Processing & License Plate Detection

- **Preprocessing**: The input image undergoes several preprocessing steps, including converting to grayscale, thresholding, blurring, and edge detection to highlight the number plate.
- **Contour Detection**: The contours of the image are analyzed to identify potential number plates based on the shape and size.
- **Plate Extraction**: A bounding box is drawn around the detected plate region, and the plate is cropped from the image for OCR.

## Vehicle Owner Lookup

- **CSV File**: The vehicle owner information (name, vehicle, and phone number) is stored in a CSV file called `drivers.csv`. Each record contains a vehicle's license number and the corresponding owner details.
- **Lookup Function**: The extracted license plate number is compared against the entries in the `drivers.csv` file to find a matching vehicle owner.

## SMS Notification

- **Twilio API**: Once the vehicle owner’s details are found, an SMS notification is sent using the **Twilio API**. The message contains details about the vehicle, the violation, and a fine amount.

## Enhancements & Future Work

- **Accuracy Improvement**: Improve the accuracy of license plate detection using advanced techniques such as deep learning-based object detection.
- **Multiple Plate Detection**: Extend the system to handle multiple vehicles and license plates in a single image.
- **Integration with Payment Systems**: Allow vehicle owners to view and pay fines directly through the application.

## Conclusion

This project demonstrates how to integrate computer vision, OCR, and SMS notification technologies to automate the process of vehicle number plate recognition and notification. The application provides an intuitive interface for users to upload images and receive real-time alerts related to traffic violations.
