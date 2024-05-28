import streamlit as st
from PIL import Image
from Controller import chat_router  # Ensure these functions are correctly imported
from fastapi import FastAPI

app = FastAPI()
app.include_router(chat_router)
