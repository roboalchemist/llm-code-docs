# Source: https://docs.embedchain.ai/examples/whatsapp_bot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 💬 WhatsApp Bot

### 🚀 Getting started

1. Install embedchain python package:

```bash  theme={null}
pip install --upgrade embedchain
```

2. Launch your WhatsApp bot:

<Tabs>
  <Tab title="docker">
    ```bash  theme={null}
    docker run --name whatsapp-bot -e OPENAI_API_KEY=sk-xxx -p 8000:8000 embedchain/whatsapp-bot
    ```
  </Tab>

  <Tab title="python">
    ```bash  theme={null}
    python -m embedchain.bots.whatsapp --port 5000
    ```
  </Tab>
</Tabs>

If your bot needs to be accessible online, use your machine's public IP or DNS. Otherwise, employ a proxy server like [ngrok](https://ngrok.com/) to make your local bot accessible.

3. Create a free account on [Twilio](https://www.twilio.com/try-twilio)
   * Set up a WhatsApp Sandbox in your Twilio dashboard. Access it via the left sidebar: `Messaging > Try it out > Send a WhatsApp Message`.
   * Follow on-screen instructions to link a phone number for chatting with your bot
   * Copy your bot's public URL, add /chat at the end, and paste it in Twilio's WhatsApp Sandbox settings under "When a message comes in". Save the settings.

* Copy your bot's public url, append `/chat` at the end and paste it under `When a message comes in` under the `Sandbox settings` for Whatsapp in Twilio. Save your settings.

### 💬 How to use

* To connect a new number or reconnect an old one in the Sandbox, follow Twilio's instructions.
* To include data sources, use this command:

```text  theme={null}
add <url_or_text>
```

* To ask the bot questions, just type your query:

```text  theme={null}
<your-question-here>
```

### Example

Here is an example of Elon Musk WhatsApp Bot that we created:

<img src="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/whatsapp.jpg?fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=ae4c8f9920e2e5e9c7a4020b099d915a" data-og-width="290" width="290" data-og-height="600" height="600" data-path="images/whatsapp.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/whatsapp.jpg?w=280&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=4052fa84a8c16c3577f242c461aae22b 280w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/whatsapp.jpg?w=560&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=98f9c7bf982450fcc5a2d61a5ea3f44b 560w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/whatsapp.jpg?w=840&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=67898fc6c1527fc83c25fe0c6766b304 840w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/whatsapp.jpg?w=1100&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=6e461032728b1df4751d8d3d89cafa06 1100w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/whatsapp.jpg?w=1650&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=7f5596c4a5471c649cbf0dc80daa3522 1650w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/whatsapp.jpg?w=2500&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=66e1c111aae4bb96fda28ef25a4df02a 2500w" />
