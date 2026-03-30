# Source: https://pipedream.com/docs/connect/api-reference/rate-limits.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limits

## Pipedream rate limits

The following rate limits apply to all Connect API endpoints:

| Name                                                                | Endpoint                    | Request Limit       | Scope             |
| ------------------------------------------------------------------- | --------------------------- | ------------------- | ----------------- |
| [Create Connect Token](/connect/api-reference/create-connect-token) | `POST /token`               | 100 per minute      | Per external user |
| [Account Management](/connect/api-reference/list-accounts)          | `GET \| DELETE /accounts/*` | 2,000 per 5 minutes | Per project       |
| [List Tools](/connect/api-reference/list-components)                | `GET /components/*`         | 3,000 per 5 minutes | Per project       |

**Need higher limits?** [Contact our support team](https://pipedream.com/support) to discuss your requirements.

## Custom rate limits

You can set custom rate limits for your users to control their usage of the Connect API and prevent runaway requests or abuse.

### Create rate limit

Create a rate limit by specifying a time window and maximum requests allowed within that window. The API returns a `rate_limit_token` that you include in subsequent Connect API requests.

```http  theme={null}
POST /rate_limits
```

#### Parameters

| Parameter             | Type    | Description                         |
| --------------------- | ------- | ----------------------------------- |
| `window_size_seconds` | integer | Time window duration in seconds     |
| `requests_per_window` | integer | Maximum requests allowed per window |

#### Example request

```bash  theme={null}
# First, obtain an OAuth access token
curl -X POST https://api.pipedream.com/v1/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "client_credentials",
    "client_id": "{oauth_client_id}",
    "client_secret": "{oauth_client_secret}"
  }'

# Create the rate limit
curl -X POST https://api.pipedream.com/v1/connect/rate_limits \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "window_size_seconds": 10,
    "requests_per_window": 1000
  }'
```

#### Response

```json  theme={null}
{
  "token": "CiKpqRdTmNwLfhzSvYxBjAkMnVbXuQrWeZyHgPtJsDcEvFpLnE"
}
```

### Using rate limit tokens

Include the `rate_limit_token` in the `x-pd-rate-limit` header for all Connect API requests:

```bash  theme={null}
curl -X POST "https://api.pipedream.com/v1/connect/{project_id}/actions/run" \
  -H "Authorization: Bearer {access_token}" \
  -H "Content-Type: application/json" \
  -H "x-pd-rate-limit: {rate_limit_token}" \
  -d '{
    "external_user_id": "user123",
    "id": "gitlab-list-commits",
    "configured_props": {
      "gitlab": {
        "authProvisionId": "apn_kVh9AoD"
      },
      "projectId": 45672541,
      "refName": "main"
    }
  }'
```

Built with [Mintlify](https://mintlify.com).
