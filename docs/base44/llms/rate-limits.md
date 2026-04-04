# Source: https://docs.base44.com/developers/references/monitoring-api/get-started/rate-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limits

> Enterprise Monitoring API rate limits and throttling behavior

Rate limits are applied per authenticated user using a token-bucket algorithm.

## Limits by endpoint

| Endpoint                                                   | Limit      |
| ---------------------------------------------------------- | ---------- |
| [Get analytics](/api-reference/analytics/get-analytics)    | 50 req/min |
| [List users](/api-reference/users/list-users)              | 50 req/min |
| [Get user](/api-reference/users/get-user)                  | 75 req/min |
| [List user apps](/api-reference/users/list-user-apps)      | 50 req/min |
| [Get app analytics](/api-reference/apps/get-app-analytics) | 50 req/min |

<Info>Enterprise users have doubled rate limits across all endpoints.</Info>

## Exceeding rate limits

If you exceed the rate limit, you'll receive a `429 Too Many Requests` response. Wait before retrying.


Built with [Mintlify](https://mintlify.com).