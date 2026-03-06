import google.generativeai as genai
import re

# configure Gemini
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro")


# -----------------------------
# Detect trip request
# -----------------------------
def detect_trip_request(text):

    match = re.search(r"(\d+)\s*day", text.lower())

    if match:
        return int(match.group(1))

    return None


# -----------------------------
# Detect greetings
# -----------------------------
def detect_greeting(text):

    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    text = text.lower()

    return any(greet in text for greet in greetings)


# -----------------------------
# Main travel chatbot
# -----------------------------
def travel_chatbot(user_input):

    # greeting response
    if detect_greeting(user_input):

        return (
            "Hello! 👋 I'm your AI Travel Assistant.\n\n"
            "I can help you:\n"
            "• Plan travel itineraries\n"
            "• Discover destinations\n"
            "• Learn about tourist sites\n"
            "• Get travel recommendations\n\n"
            "Try asking something like:\n"
            "“Plan a 5 day trip in Greece.”"
        )

    # general travel prompt
    prompt = f"""
    You are an AI travel assistant for a tourism platform.

    Answer the user's question in a helpful and concise way.

    User question:
    {user_input}
    """

    response = model.generate_content(prompt)

    return response.text