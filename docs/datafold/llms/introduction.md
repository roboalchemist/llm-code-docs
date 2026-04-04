# Source: https://docs.datafold.com/api-reference/introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

Our REST API allows you to interact with Datafold programmatically. To use it, you'll need an API key. Follow the instructions below to get started.

## Create an API Key

Open the Datafold app, visit Settings > Account, and select **Create API Key**.

<Note>
  Store your API key somewhere safe. If you lose it, you'll need to generate a new one.
</Note>

<img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e01e1d4e974f64bc105d9f84be2832ad" alt="Create an API key" data-og-width="2742" width="2742" data-og-height="1126" height="1126" data-path="images/create-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=097e301bb425134d419f5faa9f02de32 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c8496a16d3e4f24af0c1712d485bfe91 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=60e57f3cc4b71dbf91fe669ff9218fd5 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=fc6b27ac503686211a5846e47156b028 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=12e9e42e7a7b002e41ea4cb78dfc20a1 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/create-api-key.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0b53a6f6a3a1235e43db9f5ae21c9ac5 2500w" />

## Use your API Key

When making requests to the Datafold API, you'll need to include the API key as a header in your HTTP request for authentication. The header should be named `Authorization`, and the value should be in the format:

```
Authorization: Key {API_KEY}
```

For example, if you're using cURL:

```bash  theme={null}
curl https://app.datafold.com/api/v1/... -H "Authorization: Key {API_KEY}"
```

## Datafold SDK

Rather than hit our REST API endpoints directly, we offer a convenient Python SDK for common development and deployment testing workflows. You can find more information about our SDK [here](/api-reference/datafold-sdk).

## Need help?

If you have any questions about how to use our REST API, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
