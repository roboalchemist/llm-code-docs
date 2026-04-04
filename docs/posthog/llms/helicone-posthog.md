# Source: https://posthog.com/docs/llm-analytics/integrations/helicone-posthog.md

# Integrating with Helicone - Docs

You can integrate with [Helicone](https://www.helicone.ai/) and bring data into PostHog for analysis. Additionally, we offer a dashboard template to help you quickly get insights into your LLM product.

## How to install the integration

1.  Sign up for [Helicone](https://www.helicone.ai/) and add it to your app.
2.  Similar to how you set `Helicone-Auth` [header](https://docs.helicone.ai/helicone-headers/header-directory#supported-headers) when configuring your LLM client, add two new headers `Helicone-Posthog-Key` and `Helicone-Posthog-Host` with your PostHog host and API key (you can find these in your [PostHog project settings](https://us.posthog.com/settings/project)):

PostHog AI

### Python

```python
client = OpenAI(
  api_key="your-api-key-here",  # Replace with your OpenAI API key
  base_url="https://oai.hconeai.com/v1",  # Set the API endpoint
  default_headers= {
    "Helicone-Auth": f"Bearer {HELICONE_API_KEY}",
    "Helicone-Posthog-Key": "<ph_project_token>",
    "Helicone-Posthog-Host": "https://us.i.posthog.com",
  }
)
```

### Node.js

```javascript
import { Configuration, OpenAIApi } from "openai";
const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
    basePath: "https://oai.hconeai.com/v1",
    baseOptions: {
      headers: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
          "Helicone-Posthog-Key": "<ph_project_token>",
          "Helicone-Posthog-Host": "https://us.i.posthog.com",
      },
    },
});
const openai = new OpenAIApi(configuration);
```

### Terminal

```bash
curl --request POST \
     --url https://oai.hconeai.com/v1/chat/completions \
     --header 'Authorization: Bearer <<YOUR_OPENAI_API_KEY>> \
     --header 'Content-Type: application/json' \
     --header 'Helicone-Posthog-Key: Bearer <ph_project_token> \
     --header 'Helicone-Posthog-Host: Bearer https://us.i.posthog.com \
     --header 'Helicone-Auth: Bearer <<YOUR_HELICONE_API_KEY>> \
     --data '{
         "model": "gpt-3.5-turbo",
         "messages": [
             {
                 "role": "system",
                 "content": "Say Hello!"
             }
         ],
         "temperature": 1,
         "max_tokens": 10
 }'
```

Helicone events will now be exported into PostHog as soon as they're available.

## Using the Helicone dashboard template

Once you've installed the integration, [dashboard templates](/docs/product-analytics/dashboards.md) help you quickly set up relevant insights. You can see an example [Helicone dashboard here](https://us.posthog.com/shared/6_Qa74au0RhxERZ3wW9g87oxWlFxNA).

To create your own dashboard from a template:

1.  Go the [dashboard tab](https://us.posthog.com/dashboard) in PostHog.
2.  Click the **New dashboard** button in the top right.
3.  Select **LLM metrics – Helicone** from the list of templates.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better