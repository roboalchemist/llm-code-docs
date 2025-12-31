# Source: https://docs.agent.ai/builder/secrets.md

# Using Secrets in Agent.ai

Secrets let you securely store sensitive data like API keys or tokens and use them in your agents without hardcoding values directly into your workflow. This is especially useful when using REST actions to call external services.

By using secrets, you can keep credentials safe, reduce duplication across agents, and simplify maintenance if values ever change.

## When to Use Secrets

Use a secret whenever you're working with:

* API keys (e.g. OpenWeather, Slack, Notion)
* Authorization tokens
* Other sensitive config values you don’t want exposed in your agent steps

<img src="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=91ec146116757d831aed47442d2f5a62" alt="Secrets Pn" data-og-width="2734" width="2734" data-og-height="794" height="794" data-path="images/secrets.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=280&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=e8219845fce5443fd4e30766fed32534 280w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=560&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=0c0dd8cc637413305f82b13b1dab345d 560w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=840&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=f16011724a7c46f94db3726016115b05 840w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=1100&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=eca83c1dbf4b6a19907018630d18bcb3 1100w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=1650&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=8b588f2298369a0aef153c78f5bb27d3 1650w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=2500&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=b8b0779f4f161c4dd45ef65f73b71039 2500w" />

## How to Add a Secret

To add a new secret:

1. Go to the [Secrets tab](https://agent.ai/builder/secrets) from the profile navigation menu.
2. Click **Add secret**
3. Enter a **name** (e.g. weather\_api\_key) and the **secret value**
4. Click **Save**

Once saved, your secret will appear in the list as a masked value. You’ll reference it by name in your agents, not by its raw value.

## How to Use a Secret in an Agent

Anywhere you'd normally paste an API key or token in a REST call or prompt, use the secret reference format:

```
{{secrets.weather_api_key}}
```

For example, in your REST action’s header:

```json  theme={null}
{
  "Authorization": "Bearer {{secrets.weather_api_key}}"
}
```

Or directly in your request URL or body:

```json  theme={null}
{
  "url": "https://api.example.com/data?key={{secrets.weather_api_key}}"
}
```

## Best Practices

* Use clear, descriptive names (e.g. `notion_token`, `slack_webhook`)
* Avoid including the actual key in prompt text or test runs
* Rotate or update secrets as needed in the Secrets tab without having to update your agents

Questions about configuring secrets and handling sensitive credentials in Agent.ai? Reach out to our [support team](https://agent.ai/feedback).
