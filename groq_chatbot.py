import logging
from groq import Groq

class GroqClient:
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.client = Groq(api_key=api_key)
        self.model = model

    def get_chat_completion(self, messages):
        try:
            response = self.client.chat.completions.create(
                model=self.model, messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"An error occurred during chat completion: {e}")
            raise

class Chatbot:
    def __init__(self, groq_client):
        self.groq_client = groq_client
        self.messages = [{"role": "system", "content": "You are a helpful assistant. Your name is Fournuggets AI, created by FourNuggets."}]

    def get_ai_response(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        bot_message = self.groq_client.get_chat_completion(self.messages)
        self.messages.append({"role": "assistant", "content": bot_message})
        return bot_message

#api key

import pandas as pd
from datetime import datetime

# Assuming your CSV file is named 'random_data_and_timestamps.csv'
filename = 'random_data_and_timestamps.csv'

def get_and_update_oldest_data(filename):
  """
  Reads CSV data, retrieves the oldest data row, updates its time and date,
  and returns the updated DataFrame.
  """
  # Read DataFrame from CSV
  df = pd.read_csv(filename)

  # Convert 'date' column to datetime format for comparison
  df['date'] = pd.to_datetime(df['date'])

  # Find the index of the row with the oldest date
  oldest_index = df['date'].idxmin()

  # Get the oldest data row
  oldest_data = df.iloc[oldest_index]

  # Get current date and time
  now = datetime.now()

  # Update time and date in the oldest data row
  oldest_data['time'] = now.strftime("%H:%M:%S")
  oldest_data['date'] = now.strftime("%Y-%m-%d")

  # Update the DataFrame with the modified row
  df.iloc[oldest_index] = oldest_data

  return df,oldest_data['data']

# Read and update CSV data
# updated_df,api=  get_and_update_oldest_data(filename)
# print(api)
# Optionally, print the updated DataFrame (uncomment if desired)
# print(updated_df)

# Save the updated DataFrame back to the CSV file
# updated_df.to_csv(filename, index=False)

# print(f"Oldest data updated with current time and date. Updated data saved to {filename}")

# Usage
if __name__ == "__main__":
    model = "mixtral-8x7b-32768"
    os.environ["api_key"]= groq_key

    if not api_key:
        logging.error("GROQ API key not found in environment")
        exit(1)

    groq_client = GroqClient(api_key, model)
    chatbot = Chatbot(groq_client)
    print("Start chatting with the bot (type 'quit' to stop)!")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break

        bot_response = chatbot.get_ai_response(user_input)
        print(f"Bot: {bot_response}")
