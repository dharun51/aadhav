import requests
API_KEY = "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"

def chat():
    print("🤖 Welcome to GP AI (GROQ HTTP Version) 🤖")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json=payload
        )

        try:
            print("GP AI:", res.json()["choices"][0]["message"]["content"])
        except Exception as e:
            print("⚠️ API Error:", res.json())

chat()
