# Python SDK
Source: https://docs.dappier.com/integrations/python-sdk



The Dappier Python SDK provides a simple and efficient way to integrate Dappier's real-time data capabilities into your Python applications. With this SDK, you can easily access Dappier's AI models and data models to enhance your applications with live search, financial insights, and domain-specific content.

**GitHub Repository:** [Dappier Python SDK](https://github.com/DappierAI/dappier-py-sdk)

## Available Models

Dappier offers two categories of models that can be used within bolt.new applications:

* **Real-Time Search (AI Models)**: Perform live web and financial queries using natural language.
* **AI Recommendations (Data Models)**: Retrieve curated, vertical-specific content for domains like pets, lifestyle, and news.

All models are rights-cleared, production-ready, and accessible via the Dappier API.

***

### 🔎 Real-Time Search (AI Models)

| Model Name            | Description                                                                                | ai\_model\_id                   | Pricing         |
| --------------------- | ------------------------------------------------------------------------------------------ | ------------------------------- | --------------- |
| **Dappier Search**    | Real-time web search across the latest news, weather, travel, events, and more.            | `am_01j06ytn18ejftedz6dyhz2b15` | **Free**        |
| **Stock Market Data** | Live stock prices, earnings reports, financial news, and sentiment-tagged market insights. | `am_01j749h8pbf7ns8r1bq9s2evrh` | \$0.007 / query |

***

### 🤖 AI Recommendations (Data Models)

| Model Name         | Description                                                                                   | data\_model\_id                 | Pricing        |
| ------------------ | --------------------------------------------------------------------------------------------- | ------------------------------- | -------------- |
| **Sports News**    | Real-time sports headlines from Sportsnaut, LAFB Network, Ringside Intel, and more.           | `dm_01j0pb465keqmatq9k83dthx34` | \$0.50 / query |
| **Lifestyle News** | Pop culture, wellness, and trend articles from The Mix, Snipdaily, Nerdable, and Familyproof. | `dm_01j0q82s4bfjmsqkhs3ywm3x6y` | \$0.50 / query |
| **iHeartDogs AI**  | Dog training, grooming, health, and lifestyle content from iHeartDogs.                        | `dm_01j1sz8t3qe6v9g8ad102kvmqn` | \$0.01 / query |
| **iHeartCats AI**  | Cat care articles on behavior, health, and daily enrichment from iHeartCats.                  | `dm_01j1sza0h7ekhaecys2p3y0vmj` | \$0.01 / query |
| **GreenMonster**   | Sustainable living tips and eco-conscious guides from One Green Planet.                       | `dm_01j5xy9w5sf49bm6b1prm80m27` | \$0.01 / query |
| **WISH-TV AI**     | Local news, politics, multicultural content, and entertainment from the WISH-TV newsroom.     | `dm_01jagy9nqaeer9hxx8z1sk1jx6` | \$0.01 / query |

***

👉 To learn more about how these models work and how to query them, visit the official API reference:\
[https://docs.dappier.com/api-reference](https://docs.dappier.com/api-reference)

***

## Installation

Install the SDK using pip:

```bash  theme={null}
pip install dappier
```

***

## Initialization

Set up your API key and initialize the SDK:

```python Python theme={null}
import os
from dappier import Dappier