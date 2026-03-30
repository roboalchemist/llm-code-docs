# Source: https://novita.ai/docs/guides/langfuse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Langfuse

> Step-by-step guide to set up Langfuse with Novita AI to develop, monitor, evaluate, and debug AI applications.

With Langfuse, your team can collaboratively debug, analyze, and iterate on their LLM applications built with Novita AI. Its fully integrated features streamline the development workflow, enhancing efficiency and accelerating progress.

This guide shows you how to integrate Novita AI with Langfuse. Novita AI's API endpoints for chat, language and code are fully compatible with OpenAI's API. This allows us to use the Langfuse OpenAI drop-in replacement to trace all parts of your application.

# Prerequisites

Before you begin, make sure you have the following:

* Novita AI LLM API Key:
  * Visit Novita AI’s website to create an account.
  * Log in and go to the Key Management page to generate your API Key, which is essential for integrating Novita AI’s models with Langfuse.

    <Frame>
        <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/langfuse-1.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=d7d5a07696198c38f4d3872678a80e85" alt="" width="3486" height="1004" data-path="images/third-party/langfuse-1.png" />
    </Frame>
* Langfuse Account:
  * Sign up for a Langfuse account on the official [Langfuse](https://langfuse.com)website to start building powerful AI applications.

# Integration Steps

## Step 1: Install Dependencies

Ensure you have installed all the required Python packages:

```shell  theme={"system"}
pip install openai langfuse
```

## Step 2: Set Up Environment Variables

```python  theme={"system"}
import os

# Get keys for your project from the project settings page
# https://cloud.langfuse.com

os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-..." # DOCS EXAMPLE KEYS
os.environ["LANGFUSE_SECRET_KEY"] = "sk-..." # DOCS EXAMPLE KEYS
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com" # 🇪🇺 EU region
# os.environ["LANGFUSE_HOST"] = "https://us.cloud.langfuse.com" # 🇺🇸 US region


# Get your Novita AI API key from the project settings page
os.environ["NOVITA_API_KEY"] = "..."
```

## Step 3: Langfuse OpenAI drop-in Replacement

In this step we use the native [OpenAI drop-in replacement](https://langfuse.com/docs/integrations/openai/python/get-started) by importing `from langfuse.openai import openai`.

To start using Novita AI with OpenAI's client libraries, pass in your Novita AI API key to the `api_key` option, and change the `base_url` to [`https://api.novita.ai/openai:`](https://api.novita.ai/openai)

```python  theme={"system"}
# instead of import openai:
from langfuse.openai import openai

client = openai.OpenAI(
  api_key=os.environ.get("NOVITA_API_KEY"),
  base_url="https://api.novita.ai/openai",
)
```

**Note:** The OpenAI drop-in replacement is fully compatible with the [Langfuse Python SDK](https://langfuse.com/docs/observability/sdk/overview) and [`@observe()` instrumentation](https://langfuse.com/docs/observability/sdk/instrumentation) to trace all parts of your application.

## Step 4: Run An Example

The following code cell shows how to use the traced OpenAI client to call Novita AI's chat model. All API calls will be seamlessly traced by Langfuse.

```python  theme={"system"}
client = openai.OpenAI(
  api_key=os.environ.get("NOVITA_API_KEY"),
  base_url="https://api.novita.ai/openai",
)

response = client.chat.completions.create(
  model="meta-llama/llama-3.1-70b-instruct",
  messages=[
    {"role": "system", "content": "Act like you are a helpful assistant."},
    {"role": "user", "content": "What are the famous attractions in San Francisco?"},
  ]
)

print(response.choices[0].message.content)

San Francisco, one of the most iconic cities in the world, is home to a plethora of famous attractions that cater to all interests and ages. Here are some of the most popular attractions in San Francisco:

1. **Golden Gate Bridge**: An engineering marvel and a symbol of San Francisco, the Golden Gate Bridge is a must-visit attraction. Take a walk or bike ride across the bridge for spectacular views of the city and the Bay.
2. **Alcatraz Island**: Explore the infamous former prison turned national park, which once housed notorious inmates like Al Capone. Take a ferry to the island and enjoy a guided tour of the prison and its surroundings.
3. **Fisherman's Wharf**: A bustling waterfront district, Fisherman's Wharf is famous for its seafood restaurants, street performers, and stunning views of the Bay Bridge and Alcatraz Island. Don't miss the sea lions at Pier 39!
4. **Chinatown**: San Francisco's Chinatown is one of the largest and oldest in the United States. Explore the colorful streets, try some authentic Chinese cuisine, and shop for unique souvenirs.
5. **Golden Gate Park**: A sprawling urban park that's home to several attractions, including the de Young Museum, the California Academy of Sciences, and the Japanese Tea Garden.
6. **Cable Cars**: A classic San Francisco experience, the cable cars offer a fun and historic way to explore the city. Take a ride on the Powell-Mason line to Fisherman's Wharf, or the Powell-Hyde line to Lombard Street.
7. **Lombard Street**: Known as the "crookedest street in the world," Lombard Street is a scenic and winding road that offers stunning views of the city.
8. **Union Square**: A vibrant public square in the heart of the city, Union Square is surrounded by shopping, dining, and entertainment options. Catch a show at the historic Curran Theatre or take a stroll through the square.
9. **The Painted Ladies**: A row of colorful Victorian houses on Alamo Square, the Painted Ladies are a iconic symbol of San Francisco's architecture. Take a photo in front of these stunning homes.
10. **The Exploratorium**: A museum of science, art, and human perception, the Exploratorium is a great place to learn and have fun. With interactive exhibits and stunning views of the Bay, it's a must-visit for families and science enthusiasts.
11. **Pier 39**: A popular shopping and dining destination, Pier 39 offers stunning views of the Bay Bridge, Alcatraz Island, and the sea lions that call the pier home.
12. **The de Young Museum**: A fine arts museum located in Golden Gate Park, the de Young Museum features a diverse collection of art and cultural exhibitions from around the world.

These are just a few of the many famous attractions in San Francisco. Whether you're interested in history, culture, science, or entertainment, San Francisco has something for everyone.
```

## Step 5: See Traces in Langfuse

After running the example model call, you can view the traces in Langfuse. These traces provide detailed information about your Novita AI API calls, including:

* Request parameters (model, messages, temperature, etc.)
* Response content
* Token usage statistics
* Latency metrics

[Public example trace link in Langfuse](https://cloud.langfuse.com/project/cm7ua5l6e05wlad07qr6ce2wn/traces/039cc8b2-dba0-479f-9cd6-63672bc08c71?timestamp=2025-03-06T02%3A15%3A15.184Z).


Built with [Mintlify](https://mintlify.com).