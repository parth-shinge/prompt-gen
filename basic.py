def generate_prompt(content_type, topic, style):
    prompt = (
        f"Create a {style} {content_type} about {topic}. "
        f"Make sure to include relevant visuals, clear text, and a cohesive design."
    )
    return prompt

def main():
    print("Welcome to the Prompt Generator for AI Design Tools!")

    content_type = input("Enter the type of content (e.g. presentation, infographic, poster): ")
    topic = input("Enter the topic: ")
    style = input("Enter the style (e.g. modern, playful, minimalist): ")

    final_prompt = generate_prompt(content_type, topic, style)
    
    print("\nHere’s your prompt:")
    print(final_prompt)

if __name__ == "__main__":
    main()
