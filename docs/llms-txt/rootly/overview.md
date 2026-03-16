# Source: https://docs.rootly.com/integrations/slack/workflows/overview.md

# Source: https://docs.rootly.com/integrations/overview.md

# Source: https://docs.rootly.com/collaborative-retrospectives/overview.md

# Source: https://docs.rootly.com/api-reference/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> API Authentication and Request Examples

<CardGroup cols={2}>
  <Card title="Download OpenAPI Specification" icon="download" href="https://rootly.com/swagger/v1/swagger.json">
    Download our OpenAPI/Swagger specification to explore our API endpoints or generate client libraries.
  </Card>

  <Card title="Official SDKs" icon="code" href="/api-reference/sdks">
    Use our official Go and Python SDKs to integrate with the Rootly API.
  </Card>
</CardGroup>

# How to generate an API Key?

To generate a new API key, navigate to: **Organization dropdown** > **Organization Settings** > **API Keys > Generate New API Key**.

Rootly supports three scopes of API Keys:

| API Key Type     | Permissions                                                                                                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Global API Key   | Global API Keys are assigned On-Call and Incident Response role when they're generated. The assigned role's permissions control the key's permissions.  Global API Keys are able to interact with all entities within your Rootly instance. |
| Team API Key     | Team API Keys inherit the same permissions of a Team Admin. They have full read and edit access to any Rootly entity that team owns, such as the team's Schedules and Escalation Policies.                                                  |
| Personal API Key | Personal API Keys inherit the permissions of the user who created the API key.                                                                                                                                                              |

# JSON:API Specification

Rootly is using **JSON:API** ([https://jsonapi.org](https://jsonapi.org)) specification:

* JSON:API is a specification for how a client should request that resources be fetched or modified, and how a server should respond to those requests.
* JSON:API is designed to minimize both the number of requests and the amount of data transmitted between clients and servers. This efficiency is achieved without compromising readability, flexibility, or discoverability.
* JSON:API requires use of the JSON:API media type (**application/vnd.api+json**) for exchanging data.

# Authentication and Requests

We use standard HTTP Authentication over HTTPS to authorize your requests.

```bash  theme={null}
curl --request GET \
--header 'Content-Type: application/vnd.api+json' \
--header 'Authorization: Bearer YOUR-TOKEN' \
--url https://api.rootly.com/v1/incidents
```

# Rate limiting

* There is a default limit of **3000** **GET**, **HEAD**, and **OPTIONS** calls **per API key** every minute. The limit is calculated over a **1-minute sliding window** looking back from the current time. While the limit can be configured to support higher thresholds, you must first contact your **Rootly Customer Success Manager** to make any adjustments.
* There is a default limit of **3000** **POST**, **PUT**, **PATCH** or **DELETE** calls **per API key** every minute. Alert creation is limited to 50 per minute per API key. The limit is calculated over a **1-minute sliding window** looking back from the current time. While the limit can be configured to support higher thresholds, you must first contact your **Rootly Customer Success Manager** to make any adjustments.
  * Note: Our default rate limit for Alert Creation is 50 alerts every minute, per API key or alert source.
* When rate limits are exceeded, the API will return a **429 Too Many Requests** HTTP status code with the response: `{"error": "Rate limit exceeded. Try again later."}`
  * We recommend configuring your Alert Sources to handle this response and retry in order to create your Alert in Rootly.
* **X-RateLimit headers** are included in every API response, providing real-time rate limit information:
  * **X-RateLimit-Limit** - The maximum number of requests permitted and the time window (e.g., "3000, 3000;window=60" for 3000 requests per minute)
  * **X-RateLimit-Remaining** - The number of requests remaining in the current rate limit window
  * **X-RateLimit-Used** - The number of requests already made in the current window
  * **X-RateLimit-Reset** - The time at which the current rate limit window resets, in UTC epoch seconds

# Pagination

* Pagination is supported for all endpoints that return a **collection** of items.
* Pagination is controlled by the **page** query parameter

## Example

```bash  theme={null}
curl --request GET \
--header 'Content-Type: application/vnd.api+json' \
--header 'Authorization: Bearer YOUR-TOKEN' \
--url https://api.rootly.com/v1/incidents?page[number]=1&page[size]=10
```


Built with [Mintlify](https://mintlify.com).