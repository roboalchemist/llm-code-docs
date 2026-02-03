# Source: https://exa.ai/docs/reference/rate-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limits

> Default rate limits for Exa API endpoints

***

<Info>
  Need higher rate limits? Contact us at [hello@exa.ai](mailto:hello@exa.ai) to discuss an Enterprise plan.
</Info>

Our API endpoints have default rate limits to ensure reliable performance for all users. Most endpoints are limited by QPS, while the Research API uses concurrent task limits for its long-running operations.

| Endpoint    | Limit               |
| ----------- | ------------------- |
| `/search`   | 5 QPS\*             |
| `/contents` | 50 QPS              |
| `/answer`   | 5 QPS               |
| `/research` | 15 concurrent tasks |

*\*QPS = Queries Per Second*
