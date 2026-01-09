import time
from generate_image import generate_with_pollinations

def main():
    print("--- Easy Image Generator (Pollinations.ai) ---")
    
    while True:
        prompt = input("\nEnter your image prompt (or 'q' to quit): ").strip()
        if prompt.lower() == 'q':
            break
        
        if not prompt:
            continue

        image = generate_with_pollinations(prompt)

        if image:
            timestamp = int(time.time())
            filename = f"generated_{timestamp}.png"
            image.save(filename)
            print(f"Success! Saved to {filename}")
            try:
                image.show()
            except:
                pass
        else:
            print("Failed.")

if __name__ == "__main__":
    main()
