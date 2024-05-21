import openai
import os
import dotenv
import gradio as gr
from PIL import Image
import pytesseract

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def check_image_for_beef(image):
    # Save the image temporarily
    image_path = "temp_image.jpg"
    image.save(image_path)

    try:

        extracted_text = pytesseract.image_to_string(image)
        print(extracted_text)
        if 'beef' in extracted_text.lower():
            answer = "YES"
        else:
            answer = "NO"
    except ImportError:
        answer = "OCR library not installed. Please install pytesseract."

    return answer

# Create the Gradio interface
iface = gr.Interface(
    fn=check_image_for_beef,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=gr.Textbox(label="Result"),
    title="Beef Detector",
    description="Upload an image to check if the word 'beef' is present in the image."
)

if __name__ == "__main__":
    iface.launch()
