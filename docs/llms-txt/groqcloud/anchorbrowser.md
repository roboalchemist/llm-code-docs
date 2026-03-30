# Source: https://console.groq.com/docs/anchorbrowser

---
description: Learn how to use Anchor Browser with Groq to automate workflows for web applications that lack APIs or have limited API coverage.
title: Anchor Browser + Groq: Blazing Fast Browser Agents - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Anchor Browser + Groq: Blazing Fast Browser Agents](#anchor-browser--groq-blazing-fast-browser-agents)

[Anchor Browser](https://anchorbrowser.io?utm%5Fsource=groq) is the platform for AI Agentic browser automation, which solves the challenge of automating workflows for web applications that lack APIs or have limited API coverage. It simplifies the creation, deployment, and management of browser-based automations, transforming complex web interactions into simple API endpoints.

### [Python Quickstart (2 minutes to hello world)](#python-quickstart-2-minutes-to-hello-world)

[Anchor Browser](https://anchorbrowser.io?utm%5Fsource=groq) enables AI-powered browser automation using Groq's fast inference. This quickstart shows you how to use AI to automate web interactions like data collection.

![AI Form Filling with Groq on Anchor Browser](https://console.groq.com/groq-anchor-playground.png) 

### [Prerequisites](#prerequisites)

* Python 3.8 or higher installed.

### [Setup](#setup)

1. **Get your API keys:**  
   * Go to [Anchor Browser API Key](https://app.anchorbrowser.io/api-keys?utm%5Fsource=groq)
2. **Install dependencies:**Install the [Anchor Browser Python SDK](https://docs.anchorbrowser.io/quickstart/use-via-sdk?utm%5Fsource=groq). ([Typescript SDK](https://docs.anchorbrowser.io/quickstart/use-via-sdk?utm%5Fsource=groq) is also available).

curl

```
pip install anchorbrowser pydantic
```

## [Quick Example: Extract Latest AI News](#quick-example-extract-latest-ai-news)

Python

```
import os
from anchorbrowser import Anchorbrowser

# Initialize the Anchor Browser Client
client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

# Collect the newest from AI News website
task_result = client.agent.task(
    "Extract the latest news title from this AI News website",
    task_options={
        "url": "https://www.artificialintelligence-news.com/",
        "provider": "groq",
        "model": "openai/gpt-oss-120b",
    }
)

print("Latest news title:", task_result)
```

## [Advanced Session Configuration](#advanced-session-configuration)

Create a session using advanced configuration (see Anchor [API reference](https://docs.anchorbrowser.io/api-reference/sessions/create-session?utm%5Fsource=groq)).

Python

```
import os
from anchorbrowser import Anchorbrowser

# configuration example, can be ommited for default values.
session_config = {
    "session": {
        "recording": False,  # Disable session recording
        "proxy": {
            "active": True,
            "type": "anchor_residential",
            "country_code": "us"
        },
        "max_duration": 5,  # 5 minutes
        "idle_timeout": 1    # 1 minute
    }
}

client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
configured_session = client.sessions.create(browser=session_config)

# Get the session_id to run automation workflows to the same running session.
session_id = configured_session.data.id

# Get the live view url to browse the browser in action (it's interactive!).
live_view_url = configured_session.data.live_view_url

print('session_id:', session_id, '\nlive_view_url:', live_view_url)
```

## [Next Steps](#next-steps)

* Explore the [API Reference](https://docs.anchorbrowser.io/api-reference?utm%5Fsource=groq) for detailed documentation
* Learn about [Authentication and Identity management](https://docs.anchorbrowser.io/api-reference/authentication?utm%5Fsource=groq)
* Check out [Advanced Proxy Configuration](https://docs.anchorbrowser.io/api-reference/proxies?utm%5Fsource=groq) for location-specific browsing
* Use more [Agentic tools](https://docs.anchorbrowser.io/agentic-browser-control?utm%5Fsource=groq)