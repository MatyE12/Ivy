import os
from mistralai import Mistral

def ask_ivy():
    # Get API key from environment variable
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise EnvironmentError("MISTRAL_API_KEY environment variable not set.")

    client = Mistral(api_key=api_key)
    model = "mistral-large-latest"

    while True:
        # Ask the user
        askme = input("Mit szeretnél Ivytől kérdezni? (vagy írj exitet a kilépéshez!): ")
        if askme.strip().lower() in {"exit", "szia", "bye", "tchüss"}:
            print("Viszlát!")
            break

        # Add instruction for short, human-like answer
        prompt = askme + " extra extra short, your name is Ivy, human-like answer, do not mention it in the response."

        # Get response from Mistral
        chat_response = client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )

        # Print the answer
        print("\nIvy:", chat_response.choices[0].message.content, "\n")

# Only run if script is executed directly
if __name__ == "__main__":
    ask_ivy()
