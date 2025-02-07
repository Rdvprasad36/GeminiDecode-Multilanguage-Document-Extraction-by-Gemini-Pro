GeminiDecode-Multilanguage-Document-Extraction-by-Gemini-Pro.

Document: https://workdrive.zohoexternal.com/writer/open/ln8if366794f7faf0427a93243057f7a32827?authId=%7B%22linkId%22%3A%225k2wApaD3ur-LYmlU%22%7D

GeminiDecode is a state-of-the-art solution designed to extract and process data from documents in multiple languages with unmatched efficiency. By utilizing advanced natural language processing (NLP) and machine learning (ML) algorithms, it seamlessly identifies, extracts, and categorizes information from various document formats, ensuring both accuracy and speed. Ideal for global enterprises, GeminiDecode supports over 50 languages, providing robust data extraction capabilities that streamline workflows, enhance productivity, and improve decision-making processes.

Features
Multilanguage Support: Extracts data from documents in over 50 languages.

Advanced NLP and ML: Employs cutting-edge natural language processing and machine learning algorithms.

Efficiency and Accuracy: Guarantees high precision and speed in data extraction and processing.

Versatile Document Formats: Supports a variety of document formats.

Project Flow
User Interaction: The user interacts with the user interface (UI) to input their data.

Data Transmission: User input is collected from the UI and transmitted to the backend using the Google API key.

Model Processing: The input is sent to the Gemini Pro pre-trained model through an API call.

Result Generation: The Gemini Pro pre-trained model processes the input and generates the output.

Output Display: The results are returned to the frontend for formatting and display.

Requirements
To run this project, you need:

Python 3.x installed on your machine.

A valid Google API key for accessing the Gemini API.

Create a .env file in the project's root directory and add your Google API key:

GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
Install the required libraries:

pip install -r requirements.txt
Usage
Run the Streamlit application:

streamlit run app.py
Open your web browser and navigate to http://localhost:8501.

Upload a PDF document and enter your prompt to extract information.
