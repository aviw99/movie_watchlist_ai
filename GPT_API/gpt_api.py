import openai

openai.api_key = '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'

response = openai.Completion.create(
    engine='text-davinci-003',  # Specify the model
    prompt='Once upon a time',
    max_tokens=10  # Set the maximum number of tokens for the completion
)

# Retrieve the generated text
generated_text = response.choices[0].text.strip()
print(generated_text)
