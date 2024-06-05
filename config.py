import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

SYSTEM_INSTRUCTION = "You are a helpful crypto trader assistant. Under the with MACD and RSI indicators, you will find the volume, and below that, the RSI, MACD. \
    Analyze the chart for patterns indicating the potential direction of the price. Keep your analysis short, concise, and to the point. \
    Should I buy or sell?, or stay out of market?"

TARGET_INSTRUCTION = "Perform market analysis and price forecasting based off of this chart. And also provide me the conclusion of the analysis."

global new_image_bool
new_image_bool = False

global gpt_conversation
gpt_conversation = None
