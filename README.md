# RSS Feed Monitor and Message Dispatcher

This repository contains three Python scripts: `monitor_rss.py`, `get_user_id.py`, and `push_dingding.py`. 

`monitor_rss.py` is a script that monitors specified RSS feeds for new entries and sends updates to a specified Telegram user through a bot. 

`get_user_id.py` is a script that helps you retrieve the user ID of a Telegram user, which is necessary for `monitor_rss.py` to send updates to the correct person.

`push_dingding.py` is a script that can send messages to DingTalk (also known as DINGDING) by using DingTalk's outgoing webhooks feature.

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

3. If you want to send messages to DingTalk as well, import the `send_to_dd` function from `push_dingding.py` and call it in the `send_message` function.

4. Run `monitor_rss.py`. It will check the RSS feeds every 5 minutes and send a Telegram message (and a DingTalk message if configured) for each new entry.

```bash
python monitor_rss.py
```

### `push_dingding.py`

1. Replace `secret` and `access_token` with your DingTalk webhook's secret and access token.

```python
secret = "your-secret"
access_token = "your-access-token"
```

2. Call `send_to_dd(msg)` function, where `msg` is the message you want to send.

```python
send_to_dd("Hello, DingTalk!")
```

### Tutorials

1. [Monitor Twitter RSS and send message to TG] (https://twitter.com/eth_believer_ho/status/1657035019586609153).


### Contributions

1. The push_dingding.py script was originally written by [鲁初雪](https://twitter.com/PNajgaGihn4ALWm). [Ho Sir](https://github.com/hosir-web3) has modified the script to better fit into this project's structure and to improve compatibility with the existing monitor_rss.py script.
