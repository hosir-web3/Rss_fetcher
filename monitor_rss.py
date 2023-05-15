import time
import telebot
import feedparser
from bs4 import BeautifulSoup

# uncomment the next line if you will use dingding
# from push_dingding import send_to_dd

# Initialize bot with your token
bot_token = ''
bot = telebot.TeleBot(bot_token)

# Telegram user ID to send messages to
user_id = ''

# List of RSS feed urls
rss_urls = ['https://rsshub.app/twitter/user/elonmusk/exclude_rts_replies', 'https://rsshub.app/twitter/user/eth_believer_ho/exclude_rts_replies']

# Dictionary to store latest entry for each feed
latest_entries = {}

# Function to send message to user
def send_message(link, description):
    # Extract username from link
    username = link.split('/')[3]
    
    # Parse the description to extract the text content
    soup = BeautifulSoup(description, 'html.parser')
    for br in soup.find_all("br"):
        br.replace_with("\n")
    description_text = soup.text

    # Format and send the message
    message = f"{username} has tweeted a post. \n{description_text}"
    bot.send_message(user_id, message)
    
    # uncomment the next line if you will use dingding
    # send_to_dd(message)

# Function to parse feed
def parse_feed(url):
    feed = feedparser.parse(url)
    if url not in latest_entries:
        # If this is a new feed, store the first entry and send a message
        latest_entries[url] = feed.entries[0].published
        send_message(feed.entries[0].link, feed.entries[0].description)
    else:
        # If this feed has been parsed before, only send new entries
        for entry in feed.entries:
            if entry.published > latest_entries[url]:
                latest_entries[url] = entry.published
                send_message(entry.link, entry.description)

# Main loop to parse each feed every 5 minutes
while True:
    for url in rss_urls:
        parse_feed(url)
    time.sleep(300)  # Wait for 5 minutes
