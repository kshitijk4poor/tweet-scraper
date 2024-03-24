import json
import asyncio
from apify_client import ApifyClient

from config import APIFY_TOKEN, TWITTER_HANDLES, OUTPUT_FILE

# Initialize the ApifyClient with your API token
client = ApifyClient(APIFY_TOKEN)

# Function to retrieve tweets for a given Twitter handle
def get_tweets(handle, max_tweets=5):
    # Prepare the Actor input
    run_input = {
        "handles": [handle],
        "tweetsDesired": max_tweets,
        "addUserInfo": True,
        "startUrls": [],
        "proxyConfig": {"useApifyProxy": True},
    }

    # Run the Actor and wait for it to finish
    run = client.actor("u6ppkMWAx2E2MpEuF").call(run_input=run_input)

    # Fetch and return the results from the run's dataset
    return [item for item in client.dataset(run["defaultDatasetId"]).iterate_items()]

async def main():
    # Retrieve tweets for each Twitter handle and store the data in a JSON file
    tweet_data = {}
    for handle in TWITTER_HANDLES:
        tweet_data[handle] = get_tweets(handle)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(tweet_data, f, indent=4)

    print(f"Tweet data saved to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    asyncio.run(main())