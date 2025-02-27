import streamlit as st
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json
import os
os.environ["PYTHONWARNINGS"] = "ignore"



# Streamlit UI
st.set_page_config(page_title="AI Travel Planner", layout="wide")
st.title("🌍 AI-Powered Travel Planner")

# User Input
location = st.text_input("📍 Enter your destination:")
days = st.number_input("📆 Number of days:", min_value=1, max_value=30, value=3)
preferences = st.text_area("🎯 Enter your preferences (e.g., adventure, relaxation, culture):")

# LLM Setup
llm = GooglePalm(google_api_key="AIzaSyAHl04QuirH2-qF98iB45NB8r6Tz-AAHOM")  # Ensure to use google_api_key
template = PromptTemplate(
    input_variables=["location", "days", "preferences"],
    template="Provide a structured JSON travel itinerary for {location} for {days} days, considering {preferences}."
)
chain = LLMChain(llm=llm, prompt=template)

# Generate Travel Plan
if st.button("🚀 Generate Itinerary"):
    with st.spinner("Generating your personalized itinerary..."):
        response = chain.run({"location": location, "days": days, "preferences": preferences})
        
        try:
            itinerary = json.loads(response)
            st.subheader("📌 Your AI-Generated Travel Itinerary:")
            st.json(itinerary, expanded=True)
        except json.JSONDecodeError:
            st.error("❌ Error: Unable to parse response. Please try again.")

