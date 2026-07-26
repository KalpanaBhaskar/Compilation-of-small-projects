import os
from groq import Groq

# 1. Initialize the client
# Make sure you ran: export GROQ_API_KEY="your_api_key_here"
# client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
client = Groq(api_key="your-grok-api")

# 2. Send a chat completion request
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  
    messages=[
        {
            "role": "user",
            "content": "Explain LLMs vs AI agents. and if LLM basically uses probability to find the next best word, what makes a reasoning model different?"
        }
    ],
    temperature=0.7,
    max_tokens=1000,
)

# 3. Print the response
print(completion.choices[0].message.content)
