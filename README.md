# Build Alert Bot
 
Build Alert Bot is a little script that will send messages to a Discord server when an Unreal lighting build starts and finishes.
Whether you want to reliably time exactly how long your builds take or just walk away from your computer without having to worry about
checking if your build is done, this bot is your friend.
 
# Installation

1. Install [Python](https://www.python.org/downloads/), then use [pip](https://pip.pypa.io/en/stable/) to install the bot's dependencies:

```bash
pip install time
pip install datetime
pip install os
pip install requests
```
 
2. Click on the Server you want the bot to message and navigate to Server Settings > Webhooks > Create Webhook. Name it whatever you like (or just Build Alert Bot is fine.)

3. Copy the webhook URL and paste it into `discord_endpoint.py` and you're done!

# Usage

To run the bot, open a Terminal window and navigate to its folder, then run:
```bash
python3 ./BuildAlertBot.py
```

As long as the bot is running, it will let you know when any lighting build starts and finishes.

# License
[MIT](https://choosealicense.com/licenses/mit/)
