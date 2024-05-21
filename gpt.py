import openai
import os
import dotenv
import gradio as gr
from PIL import Image

dotenv.load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")

def check_image_for_beef(image):
    # Save the image temporarily
    image_path = "temp_image.jpg"
    image.save(image_path)

    # Create the OpenAI request
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an assistant that helps identify text in images."},
            {"role": "user", "content": "Do you see the word beef in this image? Just answer YES OR NO."},
            {"role": "user", "content": f"![image]({os.path.abspath(image_path)})"}
        ],
        max_tokens=10  # Limit tokens since the response is just YES or NO
    )

    # Extract the response
    print(response)
    answer = response.choices[0].message.content
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
