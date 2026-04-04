# Source: https://docs.embedchain.ai/components/data-sources/discord.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 💬 Discord

To add any Discord channel messages to your app, just add the `channel_id` as the source and set the `data_type` to `discord`.

<Note>
  This loader requires a Discord bot token with read messages access.
  To obtain the token, follow the instructions provided in this tutorial:
  <a href="https://www.writebots.com/discord-bot-token/">How to Get a Discord Bot Token?</a>.
</Note>

```python  theme={null}
import os
from embedchain import App

# add your discord "BOT" token
os.environ["DISCORD_TOKEN"] = "xxx"

app = App()

app.add("1177296711023075338", data_type="discord")

response = app.query("What is Joe saying about Elon Musk?")

print(response)
# Answer: Joe is saying "Elon Musk is a genius".
```
