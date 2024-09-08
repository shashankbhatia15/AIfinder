import streamlit as st
import os
import pprint
from groq_chatbot import *
from langchain_community.utilities import GoogleSerperAPIWrapper

# Set API keys
os.environ["SERPER_API_KEY"] = st.secrets["serper_key"]
os.environ["api_key"]=  st.secrets["groq_key"]

# Create Streamlit app
def main():
    st.title("Tanya AI")

    # Get user input
    query = st.text_input("Enter your query (e.g., 'HCOB Eurozone Manufacturing PMI august'):")

    if st.button("Submit"):
        # Perform search using Google Serper API
        search = GoogleSerperAPIWrapper(gl='in')
        results = search.results(query)
        final_answer = search._parse_results(results=results)

        # Display search results


        # st.write(pprint.pformat(results['organic']))

        # Use Groq chatbot to rewrite the answer
        model = "llama-3.1-8b-instant"
        groq_client = GroqClient(api_key, model)
        chatbot = Chatbot(groq_client)
        bot_response = chatbot.get_ai_response(
            f"Rewrite the answer for the question in the proper manner. Don't repeat the question or the answer, simply give the rewritten answer as output. Question: {query} Answer: {final_answer}"
        )

        # Display rewritten answer
        st.subheader("AI Insights:")
        st.write(bot_response)
        st.subheader("Search Results:")
        for x in results['organic']:
            st.write(pprint.pformat(x))

if __name__ == "__main__":
    main()