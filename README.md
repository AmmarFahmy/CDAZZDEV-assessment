# Dual LLM Chat Application

This is a Streamlit application that allows you to chat with two different LLaMA 2 models side by side using a single input field:
- meta-llama/Llama-2-7b-chat-hf
- AmmarFahmy/llama-2-7b-social-media-ad-generation

## Running the App Locally

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Deploying to Hugging Face Spaces

1. Create a new Space on Hugging Face
2. Connect your GitHub repository or upload the files directly
3. Make sure to add your Hugging Face token as a secret

## Usage

- Type your message in the input field at the bottom
- Hit Enter to send the message to both models
- The responses will appear in their respective chat windows on the left and right sides