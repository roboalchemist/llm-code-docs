# Step 5: Call ChatGPT API
openai.api_key = '<YOUR_OPENAI_API_KEY>'

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt_template,
    max_tokens=150
)

chatgpt_response = response.choices[0].text.strip()