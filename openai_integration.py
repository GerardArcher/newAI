import openai

# Set up your OpenAI API key
openai.api_key = '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'

# Generate text using OpenAI
response = openai.Completion.create(
  engine="davinci",
  prompt="Once upon a time",
  max_tokens=50
)

print(response.choices[0].text.strip())
