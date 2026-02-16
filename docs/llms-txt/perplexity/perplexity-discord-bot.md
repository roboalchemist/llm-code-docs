# Perplexity Discord Bot

Source: https://docs.perplexity.ai/docs/cookbook/examples/discord-py-bot/README

A simple discord.py bot that integrates Perplexity's Sonar API to bring AI answers to your Discord server.

A simple `discord.py` bot that integrates [Perplexity's Sonar API](https://docs.perplexity.ai/) into your Discord server. Ask questions and get AI-powered answers with web access through slash commands or by mentioning the bot.

<img alt="Discord Bot Demo" />

## ✨ Features

* **🌐 Web-Connected AI**: Uses Perplexity's Sonar API for up-to-date information
* **⚡ Slash Command**: Simple `/ask` command for questions
* **💬 Mention Support**: Ask questions by mentioning the bot
* **🔗 Source Citations**: Automatically formats and links to sources
* **🔒 Secure Setup**: Environment-based configuration for API keys

## 🛠️ Prerequisites

<Steps>
  <Step title="Python Environment">
    **Python 3.8+** installed on your system

    ```bash theme={null}
    python --version  # Should be 3.8 or higher
    ```
  </Step>

  <Step title="Perplexity API Access">
    **Active Perplexity API Key** from [Perplexity AI Settings](https://www.perplexity.ai/settings/api)

    <Note>You'll need a paid Perplexity account to access the API. See the [pricing page](https://www.perplexity.ai/pricing) for current rates.</Note>
  </Step>

  <Step title="Discord Bot Application">
    **Discord Bot Token** from the [Discord Developer Portal](https://discord.com/developers/applications)
  </Step>
</Steps>

## 🚀 Quick Start

### 1. Repository Setup

Clone the repository and navigate to the bot directory:

```bash theme={null}
git clone https://github.com/perplexity-ai/api-cookbook.git
cd api-cookbook/docs/examples/discord-py-bot/
```

### 2. Install Dependencies

```bash theme={null}
