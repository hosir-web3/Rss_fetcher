# Rss_fetcher

This repository contains two Python scripts: `monitor_rss.py` and `get_user_id.py`. 

`monitor_rss.py` is a script that monitors specified RSS feeds for new entries and sends updates to a specified Telegram user through a bot. 

`get_user_id.py` is a script that helps you retrieve the user ID of a Telegram user, which is necessary for `monitor_rss.py` to send updates to the correct person.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have installed the following Python packages:

* `telebot`
* `feedparser`
* `beautifulsoup4`

If not, you can install them using pip:
```
pip install pyTelegramBotAPI feedparser beautifulsoup4
```

### Installing

Clone this repository to your local machine:

```
git clone https://github.com/yourusername/rss-feed-monitor.git
```

## Usage

### `get_user_id.py`

Before running `monitor_rss.py`, you need to get the user ID of the Telegram user to whom the bot should send updates. 

1. Replace `bot_token` in `get_user_id.py` with your Telegram bot token.

```python
bot_token = 'your-telegram-bot-token'
```

2. Run `get_user_id.py`. It will print the user ID and the message text of every message your bot has received. 

```bash
python get_user_id.py
```

### `monitor_rss.py`

1. Replace `bot_token` and `user_id` in `monitor_rss.py` with your Telegram bot token and the user ID you got from `get_user_id.py`, respectively.

```python
bot_token = 'your-telegram-bot-token'
user_id = 'your-user-id'
```

2. Replace `rss_urls` with the list of RSS feeds you want to monitor.

```python
rss_urls = ['rss-feed-1', 'rss-feed-2', '...']
```

3. Run `monitor_rss.py`. It will check the RSS feeds every 5 minutes and send a Telegram message for each new entry.

```bash
python monitor_rss.py
```

* Hat tip to anyone whose code was used
* Inspiration
* etc
