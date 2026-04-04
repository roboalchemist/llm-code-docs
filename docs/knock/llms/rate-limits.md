# Source: https://docs.knock.app/api-reference/overview/rate-limits.md

# Rate limits

Each endpoint in the Knock API is rate limited. Knock uses a tier system to determine the rate limit scale for each endpoint. When your request has been rate limited, the Knock API will return a `429 Too Many Requests` error in response.

> **Rate limit tiers are assigned per-endpoint.** 

Knock's default behavior scopes rate limits based on the authorizing credential used in your requests. When you use a public or private API key to authorize a request, Knock will scope the rate limit for each endpoint by the [environment](/concepts/environments) associated with the key. If you use a signed user token as your authorizing credential, Knock will scope the rate limit by both the key's environment and the signing user. See our documentation on [enhanced security mode](/in-app-ui/security-and-authentication#authentication-with-enhanced-security) for more details on working with signed user tokens.

If you're concerned about exceeding a Knock rate limit, please [contact us](https://knock.app/contact-sales) and we can help figure out a usage rate that's right for your specific needs.

, "1 request / second"],
    [, "5 requests / second"],
    [, "60 requests / second"],
    [, "200 requests / second"],
    [, "1,000 requests / second"],
  ]}
/>
