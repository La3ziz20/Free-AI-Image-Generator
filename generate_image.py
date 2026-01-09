import requests
import io
import os
import time
from PIL import Image

def generate_with_hf(prompt, token):
    """
    Generates an image using Hugging Face Inference API (Stable Diffusion XL).
    Requires a valid HF_TOKEN.
    """
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"inputs": prompt}

    print(f"Generating with Hugging Face (Model: Stable Diffusion XL)...")
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
    
    image_bytes = response.content
    image = Image.open(io.BytesIO(image_bytes))
    return image

def generate_with_pollinations(prompt):
    """
    Generates an image using Pollinations.ai (No token required).
    """
    # Pollinations uses a GET request with the prompt in the URL
    # We need to URL encode the prompt
    print(f"Generating with Pollinations.ai...")
    
    # Simple URL encoding
    import urllib.parse
    encoded_prompt = urllib.parse.quote(prompt)
    
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
        
    image_bytes = response.content
    image = Image.open(io.BytesIO(image_bytes))
    return image

def main():
    print("--- Free Python Image Generator ---")
    print("1. Pollinations.ai (No API Key required, Easiest)")
    print("2. Hugging Face (Requires API Key, Higher Quality Control)")
    
    choice = input("Choose a method (1 or 2): ").strip()
    
    prompt = input("Enter your image prompt: ").strip()
    if not prompt:
        print("Prompt cannot be empty.")
        return

    image = None
    if choice == "1":
        image = generate_with_pollinations(prompt)
    elif choice == "2":
        token = os.environ.get("HF_TOKEN")
        if not token:
            print("\nNote: HF_TOKEN environment variable not found.")
            token = input("Please paste your Hugging Face API Token (hidden): ").strip()
        
        if not token:
            print("Token is required for Hugging Face.")
            return
            
        image = generate_with_hf(prompt, token)
    else:
        print("Invalid choice. Using Pollinations by default.")
        image = generate_with_pollinations(prompt)

    if image:
        timestamp = int(time.time())
        filename = f"generated_{timestamp}.png"
        image.save(filename)
        print(f"\nSuccess! Image saved as {filename}")
        try:
            image.show()
        except:
            pass
    else:
        print("\nFailed to generate image.")

if __name__ == "__main__":
    main()
