from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# FUNCTION TO LOAD GEMINI PRO MODEL AND GET RESPONSE 
model= genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    



