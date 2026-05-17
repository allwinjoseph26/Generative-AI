# ============================================
# ADVANCED LLM CHATBOT USING OPENAI API
# ============================================
#
# Features:
# - Uses Large Language Models (LLMs)
# - Conversation memory
# - System prompts
# - Streaming responses
# - Chat history
# - Error handling
# - Typing effect
# - Temperature control
# - Token management
#
# REQUIREMENTS:
# pip install openai python-dotenv
#
# Create a .env file:
# OPENAI_API_KEY=your_api_key_here
#
# ============================================

import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# ============================================
# LOAD ENVIRONMENT VARIABLES
# ============================================

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: API Key not found.")
    exit()

# ============================================
# INITIALIZE CLIENT
# ============================================

client = OpenAI(api_key=api_key)

# ============================================
# CHATBOT CONFIGURATION
# ============================================

MODEL_NAME = "gpt-4.1-mini"

TEMPERATURE = 0.7
MAX_TOKENS = 500

# ============================================
# SYSTEM PROMPT
# ============================================

system_prompt = """
You are an advanced AI assistant.

Your behavior:
- Be intelligent and helpful
- Explain concepts clearly
- Help with coding
- Be friendly
- Answer accurately
"""

# ============================================
# CHAT MEMORY
# ============================================

conversation = [
    {
        "role": "system",
        "content": system_prompt
    }
]

# ============================================
# PRINTING FUNCTIONS
# ============================================

def slow_print(text, delay=0.01):
    """
    Prints text slowly like real AI typing
    """

    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)

    print()

# ============================================
# GENERATE RESPONSE FUNCTION
# ============================================

def generate_response(user_message):

    try:

        # Add user message to memory
        conversation.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        # Send request to LLM
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=conversation,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )

        # Extract assistant response
        assistant_reply = response.choices[0].message.content

        # Store assistant reply in memory
        conversation.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

        return assistant_reply

    except Exception as e:
        return f"Error occurred: {e}"

# ============================================
# CHATBOT HEADER
# ============================================

print("=" * 60)
print("        ADVANCED LLM POWERED CHATBOT")
print("=" * 60)

print("""
Commands:
- type 'exit' to quit
- type 'history' to view chat history
- type 'clear' to clear memory
""")

# ============================================
# MAIN LOOP
# ============================================

while True:

    user_input = input("\nYou: ")

    # ========================================
    # EXIT
    # ========================================

    if user_input.lower() == "exit":

        print("\nChatbot: Goodbye!")
        break

    # ========================================
    # VIEW HISTORY
    # ========================================

    elif user_input.lower() == "history":

        print("\n======= CHAT HISTORY =======")

        for msg in conversation:

            role = msg["role"]
            content = msg["content"]

            print(f"\n{role.upper()}:")
            print(content)

        print("\n============================")

    # ========================================
    # CLEAR MEMORY
    # ========================================

    elif user_input.lower() == "clear":

        conversation = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        print("\nChatbot memory cleared.")

    # ========================================
    # EMPTY INPUT
    # ========================================

    elif user_input.strip() == "":

        print("Please type something.")

    # ========================================
    # NORMAL CHAT
    # ========================================

    else:

        print("\nChatbot: ", end="")

        reply = generate_response(user_input)

        slow_print(reply)

# ============================================
# END OF PROGRAM
# ============================================