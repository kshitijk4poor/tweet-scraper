import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter Scraper API credentials
APIFY_TOKEN = os.getenv("APIFY_TOKEN")

# List of Twitter handles to scrape
TWITTER_HANDLES = ["@elonmusk", "@JeffBezos", "@BarackObama", "@BillGates"]

# Output file name
OUTPUT_FILE = "tweet_data.json"