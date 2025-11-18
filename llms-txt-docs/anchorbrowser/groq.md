# Source: https://docs.anchorbrowser.io/integrations/groq.md

# Groq GPT-OSS

> Blazing Fast, Accurate Browser Agents

# Anchor Browser + Groq: Blazing, Accurate Fast Browser Agents

[Groq](https://groq.com/) is the fast inference paltform, providing llm APIs with low time-to-first-token and time-to-response

## Python Quickstart (2 minutes to hello world)

<img className="hidden dark:block mx-auto" src="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/groq-anchor-playground.png?fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=7a628c94f9a80d560c7664e965fdc451" alt="AI Form Filling with Groq on Anchor Browser" width="560" data-og-width="1336" data-og-height="969" data-path="images/groq-anchor-playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/groq-anchor-playground.png?w=280&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=003e9557182c3dd79e0c22e0cb76bed3 280w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/groq-anchor-playground.png?w=560&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=813eb1eaef7450e1a03505b5c7c5e194 560w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/groq-anchor-playground.png?w=840&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=5e08519c0ab54aaed7edddcf45fb4df8 840w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/groq-anchor-playground.png?w=1100&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=45cc91d6dee32c0356971f291713a4d8 1100w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/groq-anchor-playground.png?w=1650&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=0ff2e7f7531242a396b342d381bd7569 1650w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/groq-anchor-playground.png?w=2500&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=4bedd82f2a614b424e741666b92ceabc 2500w" />

### Prerequisites

* Python 3.8 or higher installed.

### Setup

1. **Get your API keys:**
   * Go to [Anchor Browser API Key](https://app.anchorbrowser.io/api-keys?utm_source=groq)

2. **Install dependencies:**
   Install the [Anchor Browser Python SDK](https://docs.anchorbrowser.io/quickstart/use-via-sdk?utm_source=groq). ([Typescript SDK](https://docs.anchorbrowser.io/quickstart/use-via-sdk?utm_source=groq) is also available).

```bash  theme={null}
pip install anchorbrowser pydantic
```

## Quick Example: Extract Latest AI News

```python python theme={null}
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

## Advanced Session Configuration

Create a session using advanced configuration (see Anchor [API reference](https://docs.anchorbrowser.io/api-reference/browser-sessions/start-browser-session?utm_source=groq)).

```python python theme={null}
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

## Next Steps

* Explore the [API Reference](https://docs.anchorbrowser.io/api-reference?utm_source=groq) for detailed documentation
* Learn about [Authentication and Identity management](https://docs.anchorbrowser.io/essentials/authentication-and-identity?utm_source=groq)
* Check out [Advanced Proxy Configuration](https://docs.anchorbrowser.io/advanced/proxy?utm_source=groq) for location-specific browsing
* Use more [Agentic tools](https://docs.anchorbrowser.io/agentic-browser-control?utm_source=groq)
