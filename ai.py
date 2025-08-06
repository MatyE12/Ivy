import os

from mistralai import Mistral
askme = (input("What would you like to ask Mistral?") + "extra extra short, human-like answer, do not mention it in the response")
run = True
api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model = model,

    messages = [
        {

            "role": "user",
            "content": askme,

        },

    ]
)

print(chat_response.choices[0].message.content)

