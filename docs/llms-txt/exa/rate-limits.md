# Source: https://docs.exa.ai/reference/rate-limits.md

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


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt