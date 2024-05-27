import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API'))
# Set up the model

generation_config = {
  "temperature": 0.3,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 256,
}

def get_model_respose(question):
    model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                                generation_config=generation_config)

    convo = model.start_chat()
    

    respose = convo.send_message(question)
    respose = respose.text
    return respose