import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from the .env file
load_dotenv()

# Set the environment variable for the API key
# os.environ["GROQ_API_KEY"] = "your_api_key"

# Initialize the Groq client with the API key
client = Groq()

# Streamlit app UI
st.title("Diet Planner App 🎉🎂✨🍰🥳")

st.info("This app helps you plan your diet and track your meals.")
st.sidebar.header("Diet Planner")
st.sidebar.subheader("Select your preferences")
st.sidebar.write("Please select your dietary preferences below:")

# List of diet options
diet_options = [
    "Vegetarian", "Vegan", "Gluten-free", "Keto", "Paleo", "Mediterranean", 
    "Low-carb", "Low-fat", "High-protein", "Diabetic", "Heart-healthy", 
    "DASH", "Flexitarian", "Whole30", "Raw food", "FODMAP", "Anti-inflammatory", 
    "Low-sodium", "Low-cholesterol"
]

# Display diet options in the sidebar
for option in diet_options:
    st.sidebar.write(option)

# Define the robot's role in the conversation
robot_role_message = "You are an expert in diet planning. You will help the user plan their diet based on their preferences."

# User input for dietary preferences
user_message = st.text_input("Enter your dietary preferences (e.g., vegetarian, vegan, gluten-free):")

# Sidebar controls for Groq API parameters
st.sidebar.header("API Settings")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5, 0.05, help="Controls the randomness of the response. Lower values are more focused and deterministic, higher values are more random.")
top_p = st.sidebar.slider("Top-p (nucleus sampling)", 0.0, 1.0, 1.0, 0.05, help="Controls the diversity of the output by sampling from the top-p probability mass.")
max_tokens = st.sidebar.number_input("Max Tokens", 50, 1000, 300, 50, help="Maximum number of tokens in the generated response.")

# Initialize a variable to store the diet plan (it will be None initially)
Diet_Planner = None

# Handle button click and check for user input
if st.button("Generate Diet Plan") and user_message:
    try:
        # Call the Groq API to get a response using the user-defined settings
        response = client.chat.completions.create(
            messages=[{"role": "system", "content": robot_role_message},
                      {"role": "user", "content": user_message}],
            model="llama-3.3-70b-versatile",  # Specify your model
            temperature=temperature,
            max_completion_tokens=max_tokens,
            top_p=top_p,
            stop=None,
            stream=False
        )

        # Extract the content from the response
        Diet_Planner = response.choices[0].message.content

        # Display the generated diet plan
        st.write(Diet_Planner)
    except Exception as e:
        st.error(f"Error generating diet plan: {e}")
else:
    st.write("Please enter your dietary preferences and click the button to generate your diet plan.")
