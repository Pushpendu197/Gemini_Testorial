### Health Management APP — Recipe Generator

from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

# IMPORT STATEMENT......................................................................
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure Gemini API............................................................................
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini 1.5 Flash and get recipe response......................................
def get_gemini_response(image_parts, dish_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([
        dish_prompt,
        image_parts[0]
    ])
    return response.text

# Convert uploaded image to Gemini-compatible format..............................................................................
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit UI......................................................................................................................
# st.set_page_config(page_title="Gemini Dish-to-Recipe App")
st.header("🍽️ Gemini Dish-to-Recipe App")
st.write("Upload an image of a dish, and AI will try to generate a possible recipe for it!")

uploaded_file = st.file_uploader("Upload a dish image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Dish", use_column_width=True)



# Gemini Prompt to generate recipe..................................................................................................
dish_prompt = """
You are a professional chef. Analyze the uploaded dish image and generate a recipe including:

1. Name of the dish (if known).
2. Estimated list of ingredients.
3. Step-by-step cooking instructions.
4. Optional: serving suggestions or cultural background.

Be descriptive and helpful. If the dish is unclear, suggest a plausible recipe based on the ingredients you can identify visually.
"""

#SUBMIT GENERATE THE RECEIPE.......................................................................................................
submit = st.button("Generate Recipe")

if submit:
    if uploaded_file is None:
        st.error("Please upload an image first.")
    else:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(image_data, dish_prompt)
        st.subheader("🍳 Suggested Recipe")
        st.write(response)
