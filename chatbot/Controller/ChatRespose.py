import google.generativeai as genai
import os
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
chat_router = APIRouter(prefix='/api/chatbot/v1')

genai.configure(api_key=os.getenv('GEMINI_API'))

# Set up the model generation configuration
generation_config = {
    "temperature": 0.3,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 256,
}

@chat_router.post('/chat')
def get_model_response(question: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                                      generation_config=generation_config)
        convo = model.start_chat()
        response = convo.send_message(f'you are AI Farmer please answer this Quistion: {question}')
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


