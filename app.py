import streamlit as st
import os
from dotenv import load_dotenv
from google.generativeai import configure, GenerativeModel
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract

# Load environment variables
load_dotenv()

# Function to configure Google Generative AI
def configure_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key is None:
        st.error("API key not found. Please check your .env file.")
        return None
    configure(api_key=api_key)
    return GenerativeModel("gemini-1.5-flash")

# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text.strip()

# Function to extract text from images
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text.strip()

# Function to summarize text using Generative AI
def generate_summary(text):
    if not text:
        return "No content to summarize."
    model = configure_gemini()
    # Use a concise prompt for summary generation
    prompt = f"Provide a brief summary of the following text:\n{text}\n\nSummary:"
    response = model.generate_content([prompt])
    return response.text.strip() if response else "Failed to generate summary."

# Streamlit UI with styling
st.markdown(
    """
    <style>
    body {
        background-color: #73EC8B;  /* Background color */
    }
    .title {
        color: #FF6347;  /* Title color */
        font-size: 2.5em;
        text-align: center;
        font-weight: bold;
    }
    .subtitle {
        color: #54C392;  /* Subtitle color */
        font-size: 1.5em;
        margin-top: 20px;
    }
    .summary {
        background-color: #15B392; /* Summary background color */
        color: white; /* Text color for the summary */
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Main title with styling
st.markdown('<div class="title">GeminiDecode: Multilanguage Document Extraction by Gemini Pro : By Shubham Godse</div>', unsafe_allow_html=True)

text="Utilizing Gemini Pro AI,this project effortlessly extracts vital information from diverse multilingual documents, transcending language barriers with \nprecision and efficiency for enchanced productivity and decision-making"
st.markdown(text, unsafe_allow_html=True)

# File uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Choose a PDF or an image...", type=["pdf", "jpg", "jpeg", "png"])

# Initialize a text variable
text = ""

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        # Extract and display text from PDF
        text = extract_text_from_pdf(uploaded_file)
        st.markdown('<div class="subtitle">Uploaded PDF Document:</div>', unsafe_allow_html=True)
        st.write("PDF file uploaded successfully.")
    else:
        # Load image for text extraction and resize it
        image = Image.open(uploaded_file)
        text = extract_text_from_image(image)
        st.markdown('<div class="subtitle">Uploaded Image:</div>', unsafe_allow_html=True)
        st.image(image, caption='Uploaded Image', use_column_width=False, width=300)  # Resized image to 300px width

    if st.button("Tell me about this document:"):
        summary = generate_summary(text)
        st.markdown('<div class="summary"><strong>Summary:</strong><br>{}</div>'.format(summary), unsafe_allow_html=True)