import openai

# Set your OpenAI API key
openai.api_key = "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"

# Specify the model to use
model = "davinci"  # You can also use "gpt-3.5-turbo"

# Provide a prompt (text) for which you want to generate embeddings
prompt = "This is a sample text for which I want to generate embeddings."

# Use the model to generate embeddings
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=50  # Adjust this as needed for the desired length
)

# Extract the generated embeddings
embeddings = response.choices[0].text

print("Text Embeddings:")
print(embeddings)
