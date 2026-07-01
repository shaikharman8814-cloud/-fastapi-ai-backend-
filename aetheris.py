from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
app=FastAPI()
client=genai.Client(api_key="Your api key here")
class chat(BaseModel):
    message:str
@app.post("/chat")
def chat(data:chat):
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=data.message
    )
    
    return{
        "reply":response.text
    }