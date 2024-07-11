from openai import OpenAI
import os

API_key = os.getenv("OPENAIKEY")
client = OpenAI(api_key=API_key)

class Chatbot:

    def get_response(self, user_input):
        response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=user_input,
        max_tokens=200,
        temperature=0.5,
        n=1).choices[0].text
        return response

if __name__ == "__main__":
    bot=Chatbot()
    user_input = "give me a quick joke"
    output = bot.get_response(user_input)
    print(output)
