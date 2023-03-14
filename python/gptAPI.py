import openai
import os

# set up your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# prompt text to generate completion
prompt = "what is food receipe for calcium deficiency ?"

# parameters for the API request
params = {
    "engine": "text-davinci-002",
    "prompt": prompt,
    "max_tokens": 50,
    "temperature": 0.5
}

# send the API request
response = openai.Completion.create(**params)

# print the generated text
print(response.choices[0].text.strip())
