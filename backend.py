import openai
import os

API_key = os.getenv("OPENAIKEY")

class Chatbot:
    def __init__(self):
        openai.api_key = API_key

    def get_response(self, user_input):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=50,
            n=1)
        return response

if __name__ == "__main__":
    bot=Chatbot()
    user_input = "hi, what is a prime number?"
    output = bot.get_response(user_input)
    print(output)
