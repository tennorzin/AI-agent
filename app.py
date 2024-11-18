import streamlit as st
import pandas as pd
import requests
import openai
import time

# Set API keys
API_KEY = "8bb4a150172cae7fc96ea1931c18db9c223dc89a214680f15360630c4b518650"  # SerpAPI key
openai.api_key = "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"  # OpenAI key

# Function to perform web search using SerpAPI


# Function to perform web search using SerpAPI with rate-limiting handling
def search_entity(entity, custom_query):
    SEARCH_URL = "https://serpapi.com/search"
    query = custom_query.format(entity=entity)
    params = {"q": query, "api_key": API_KEY}
    
    while True:  # Retry loop for handling rate limits
        response = requests.get(SEARCH_URL, params=params)
        if response.status_code == 200:
            return response.json().get("organic_results", [])
        elif response.status_code == 429:  # Rate limit hit
            st.warning("Rate limit hit! Retrying after 5 seconds...")
            time.sleep(5)  # Wait before retrying
        else:
            return []  # Return empty if other errors occur



# Streamlit app
st.title("AI Agent Dashboard")
st.markdown("Upload a CSV file, define your query, and retrieve structured information using AI.")

# File upload
uploaded_file = st.file_uploader("Upload a CSV File", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data:")
    st.write(data.head())

    # Column selection (Dropdown)
    column = st.selectbox("Select the column containing entities", data.columns)

    # Prompt input with example replacement
    prompt = st.text_input(
        "Enter your query (use {entity} as placeholder)",
        value="Get me the email address of {entity}."
    )
    # Replace {entity} with an example in the preview
    st.write("Query Example:", prompt.format(entity="Google"))

    if st.button("Perform Search and Extract Information"):
        entities = data[column].dropna().unique()
        results = []
        
        for entity in entities:
            # Perform web search
            search_results = search_entity(entity, prompt)
            st.write("Raw Search Results:", search_results)

            if search_results:
                # Extract information using GPT
                extracted_info = extract_info(entity, search_results, prompt)
            else:
                extracted_info = "No results found."
            
            results.append({"Entity": entity, "Extracted Information": extracted_info})
        
        # Display results
        results_df = pd.DataFrame(results)
        st.write("Extracted Information:")
        st.table(results_df)

        # Download results
        st.download_button(
            "Download Results as CSV",
            results_df.to_csv(index=False),
            "results.csv",
            "text/csv"
        )
