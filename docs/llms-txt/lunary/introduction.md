# Source: https://docs.lunary.ai/docs/more/security/introduction.md

# Source: https://docs.lunary.ai/docs/api/introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Overview of the Lunary.ai API.

# API Reference

Use the Lunary API to access programmatically access your data.

## Base URL

The base URL for the Lunary Cloud API is:

```bash  theme={null}
https://api.lunary.ai/v1
```

In the case of self-hosting, replace the host with your backend's URL.

## Authentication

You'll need to authenticate your requests to access any of the endpoints in the data API.

To obtain your private API key, visit the [Settings Page](https://app.lunary.ai/settings). Each project has its own private and public API key.

The private API key can be passed in the Authorization header as a Bearer token.

Some endpoints, such as the ingestion endpoint, can be accessed with the public key.

### Sample request

```bash  theme={null}
curl --get 'https://api.lunary.ai/v1/runs' \
  -H "Authorization: Bearer <api_key>" \
  -d "limit=10" \
  -d "page=0" \
  -d "order=asc" \
  -d "type=llm" 
```

## Rate Limiting

The API employs a sliding window rate limiter. The current rate limit for this endpoint is set at 30 requests per second.

## Error Handling

Standard HTTP status codes are used for error handling:

* `429`: Rate limit exceeded.

* `422`: Missing or incorrect parameters.

* `403`: Unauthorized access .

* `50X`: Internal server error.
