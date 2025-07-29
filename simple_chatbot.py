
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
# model =  genai.GenerativeModel("gemini-2.5-pro")
# model =  genai.GenerativeModel("gemini-1.5-flash-8b")


# Start the chatbot
print("=== 🤖 Ask Me Anything (Chatbot) ===")
print("😎 Type 'exit' to quit.")

while True:
    question = input("😎 \nYou: ")
    if question.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = model.generate_content(question)
        print("\n 😎Bot:", response.text.strip())
    except Exception as e:
        print("Error:", str(e))
