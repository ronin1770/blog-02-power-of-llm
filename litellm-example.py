
import litellm, os

# Set up LiteLLM with your OpenAI API key
openai_api_key = '<YOUR-API-KEY>'
os.environ["OPENAI_API_KEY"] = openai_api_key

# Define a prompt for GPT-4
prompt = "Explain the concept of quantum computing in simple terms."

messages = [{"role" : "user", "content" : prompt }]

# Call the GPT-4 model using litellm's gpt4_completion function
response = litellm.completion(
    messages=messages,
    model="gpt-4",
    max_tokens=150,   # Adjust based on the desired response length
    temperature=0.7   # Control creativity (0.0 - precise, 1.0 - creative)
)

# Print the response from GPT-4
print(response)
