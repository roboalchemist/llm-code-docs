# Source: https://console.groq.com/docs/overview-refresh

---
description: Documentation for Groq products and APIs. Fast LLM inference, OpenAI-compatible. Simple to integrate, easy to scale. Start building in minutes.
title: GroqDocs - Build Fast
image: https://console.groq.com/og_cloudv5.jpg
---

## Welcome

Fast LLM inference, OpenAI-compatible. Simple to integrate, easy to scale. Start building in minutes.

Python

```
import OpenAI from "openai";
const client = new OpenAI({
    apiKey: process.env.GROQ_API_KEY,
    baseURL: "https://api.groq.com/openai/v1",
});

const response = await client.responses.create({
    model: "openai/gpt-oss-20b",
    input: "Explain the importance of fast language models",
});
console.log(response.output_text);
```

```
from openai import OpenAI
import os
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Explain the importance of fast language models",
    model="openai/gpt-oss-20b",
)
print(response.output_text)
```

```
curl -X POST https://api.groq.com/openai/v1/responses \
-H "Authorization: Bearer $GROQ_API_KEY" \
-H "Content-Type: application/json" \
-d '{
    "model": "openai/gpt-oss-20b",
    "input": "Explain the importance of fast language models"
}'
```

[![MCP Logo](https://console.groq.com/_next/image?url=%2Fmcp.png&w=64&q=75)Google Workspace Connectors are now available on GroqConnect your AI agents to Gmail, Google Calendar, and Google Drive with ready-made connectors.Learn More](/docs/tool-use/remote-mcp/connectors) 

![Getting Started video cover](https://console.groq.com/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FlLmPol9YPyI%2Fmaxresdefault.jpg&w=3840&q=75)

## Getting Started

Take a quick video tour on how to get started building your app on Groq.

[Quick StartGet started with the Groq API](https://console.groq.com/docs/quickstart)[ModelsSee all the models Groq offers](https://console.groq.com/docs/models)[API ReferenceExplore all API endpoints](https://console.groq.com/docs/api-reference)[CookbooksSee code examples and tutorials](https://github.com/groq/groq-api-cookbook)[Rate LimitsReference the model rate limits](https://console.groq.com/docs/rate-limits)[IntegrationsConnect to external services](https://console.groq.com/docs/integrations)

### External API Compatibility

OpenAI base URL: 

https://api.groq.com/openai/v1

[Learn about](https://console.groq.com/docs/openai) OpenAI compatibility