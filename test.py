from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load the tokenizer and model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("andrijdavid/MeanGirl")
model = AutoModelForCausalLM.from_pretrained("andrijdavid/MeanGirl")

# Initialize the text-generation pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_text(prompt, max_length=50, num_return_sequences=1):
    """
    Generate text based on a given prompt using the model.
    """
    response = pipe(
        prompt,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        temperature=0.7,  # Adjust for creativity (higher = more creative)
        top_p=0.9,        # Nucleus sampling for diversity
        do_sample=True    # Enable sampling for more randomness
    )
    return [result["generated_text"] for result in response]

# Example: Generate a response from the Mean Girl model
prompt = "You're not even that pretty."
generated_text = generate_text(prompt, max_length=100, num_return_sequences=1)

# Print the generated response
print("Generated Text:")
for idx, text in enumerate(generated_text, 1):
    print(f"{idx}. {text}")
