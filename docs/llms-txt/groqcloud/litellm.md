# Source: https://console.groq.com/docs/litellm

---
description: Learn how to use LiteLLM with Groq to deploy production-ready LLM applications with robust observability, cost tracking, and smart caching.
title: LiteLLM + Groq: Production LLM Deployments - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [🚅 LiteLLM + Groq for Production Deployments](#-litellm--groq-for-production-deployments)

[LiteLLM](https://docs.litellm.ai/docs/) provides a simple framework with features to help productionize your application infrastructure, including:

* **Cost Management:** Track spending, set budgets, and implement rate limiting for optimal resource utilization
* **Smart Caching:** Cache frequent responses to reduce API calls while maintaining Groq's speed advantage
* **Spend Tracking:** Track spend for individual API keys, users, and teams

### [Quick Start (2 minutes to hello world)](#quick-start-2-minutes-to-hello-world)

#### [1\. Install the package:](#1-install-the-package)

curl

```
pip install litellm
```

#### [2\. Set up your API key:](#2-set-up-your-api-key)

curl

```
export GROQ_API_KEY="your-groq-api-key"
```

#### [3\. Send your first request:](#3-send-your-first-request)

Python

```
import os
import litellm

api_key = os.environ.get('GROQ_API_KEY')


response = litellm.completion(
    model="groq/llama-3.3-70b-versatile", 
    messages=[
       {"role": "user", "content": "hello from litellm"}
   ],
)
print(response)
```

### [Next Steps](#next-steps)

For detailed setup of advanced features:

* [Configuration of Spend Tracking for Keys, Users, and Teams](https://docs.litellm.ai/docs/proxy/cost%5Ftracking)
* [Configuration for Budgets and Rate Limits](https://docs.litellm.ai/docs/proxy/users)

For more information on building production-ready applications with LiteLLM and Groq, see:

* [Official Documentation: LiteLLM](https://docs.litellm.ai/docs/providers/groq)
* [Tutorial: Groq API Cookbook](https://github.com/groq/groq-api-cookbook/tree/main/tutorials/litellm-proxy-groq)