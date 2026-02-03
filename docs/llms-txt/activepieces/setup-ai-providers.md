# Source: https://www.activepieces.com/docs/admin-guide/guides/setup-ai-providers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setup AI Providers

AI providers are configured by the platform admin to centrally manage credentials and access, making [AI pieces](https://www.activepieces.com/pieces/ai) and their features available to everyone in all projects.

## Supported Providers

* **OpenAI**
* **Anthropic**
* **Gemini**
* **Vercel AI Gateway**
* **Cloudflare AI Gateway**

## How to Setup

Go to **Admin Console** → **AI** page. Add your provider's base URL and API key. These settings apply to all projects.

<img src="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/configure-ai-provider.png?fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=f3d6967212b94b909e89d77917dcacc0" alt="Manage AI Providers" data-og-width="1420" width="1420" data-og-height="800" height="800" data-path="resources/screenshots/configure-ai-provider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/configure-ai-provider.png?w=280&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=5562cf7264f88ea8b817ce9dfb846928 280w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/configure-ai-provider.png?w=560&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=adea1c7aa126c5dd9ff9d9ab6d2adca9 560w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/configure-ai-provider.png?w=840&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=430b9334e37b374c663bdc78830f8823 840w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/configure-ai-provider.png?w=1100&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=e52d82550e028d9d7d9317d2b3a5b050 1100w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/configure-ai-provider.png?w=1650&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=77667efb2e6f71474bfcf81fa85ddd0d 1650w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/configure-ai-provider.png?w=2500&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=9bf447af05f4b1358f88d11a8bd23f94 2500w" />

## Cost Control & Logging

Use an AI gateway like **Vercel AI Gateway** or **Cloudflare AI Gateway** to:

* Set rate limits and budgets
* Log and monitor all AI requests
* Track usage across projects

Just set the gateway URL as your provider's base URL in the Admin Console.
