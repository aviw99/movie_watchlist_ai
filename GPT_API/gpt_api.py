import openai

openai.api_key = ' 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'

response = openai.Completion.create(
    engine='text-davinci-003',  # Specify the model
    prompt='intelij free and paid',
    max_tokens=100  # Set the maximum number of tokens for the completion
)

# Retrieve the generated text
generated_text = response.choices[0].text.strip()
print(generated_text)
