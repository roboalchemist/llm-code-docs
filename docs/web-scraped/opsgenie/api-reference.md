# OpsGenie REST API Documentation

## Overview

The OpsGenie REST API provides programmatic access to:

- Alert management (create, list, acknowledge, close)
- Incident management (create, update, resolve)
- Team management (create, list members)
- On-call schedules and rotations
- Users and permissions
- Integrations and webhooks

All API endpoints use REST principles and return JSON responses.

## Base URLs

**US Region:**

```text
https://api.opsgenie.com/v2
```

**EU Region:**

```text
https://api.eu.opsgenie.com/v2
```

## Authentication

### API Key Authentication

Include your API key in the `Authorization` header:

```text
Authorization: GenieKey YOUR_API_KEY
```

Get your API key from Settings > API Key Management in the OpsGenie UI.

### User-Level API Keys

Create API keys with specific permissions:

1. Go to Settings > API Key Management
2. Click "Add New API Key"
3. Select permissions (read, create, delete)
4. Save and use the key

## HTTP Methods

| Method | Purpose |
|--------|---------|
| GET | Retrieve data |
| POST | Create resource or perform action |
| PATCH | Update resource |
| PUT | Replace resource |
| DELETE | Delete resource |

## Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized (invalid API key) |
| 403 | Forbidden (insufficient permissions) |
| 404 | Not Found |
| 422 | Unprocessable Entity (validation error) |
| 429 | Too Many Requests (rate limited) |
| 500 | Internal Server Error |

## Rate Limiting

OpsGenie API has the following rate limits:

- **100 requests per minute** for standard API keys
- **1000 requests per minute** for enterprise API keys

Rate limit headers in response:

- `X-Rate-Limit-Limit` - Request limit
- `X-Rate-Limit-Remaining` - Remaining requests
- `X-Rate-Limit-Reset-After` - Reset time in seconds

## Request/Response Format

### Request Example

```bash
curl -X POST https://api.opsgenie.com/v2/alerts \
  -H "Authorization: GenieKey YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "API Test Alert",
    "priority": "P3"
  }'
```

### Response Example

```json
{
  "data": {
    "alertId": "550e8400-e29b-41d4-a716-446655440000",
    "message": "API Test Alert",
    "status": "open"
  },
  "took": 154,
  "requestId": "d7f4e8c1-f3c8-4b0e-8d5f-6c2e7b9a1d3f"
}
```

## Common Response Fields

- `data` - Response payload
- `took` - Response time in milliseconds
- `requestId` - Unique request identifier (for support)

## Error Responses

```json
{
  "took": 12,
  "requestId": "...",
  "errors": [
    {
      "code": 40001,
      "message": "Invalid API key"
    }
  ]
}
```

## Pagination

List endpoints support pagination:

```text
GET /alerts?limit=20&offset=40
```

Query parameters:

- `limit` - Number of results (default: 20, max: 100)
- `offset` - Number of items to skip

Response includes:

```json
{
  "data": [...],
  "paging": {
    "first": "...",
    "last": "...",
    "next": "...",
    "prev": "..."
  }
}
```

## Query Filters

### Alert Query Examples

```bash
# Alerts from a specific team
curl "https://api.opsgenie.com/v2/alerts?query=team%3Dplatform" \
  -H "Authorization: GenieKey YOUR_API_KEY"

# Unacknowledged critical alerts
curl "https://api.opsgenie.com/v2/alerts?query=status%3Dopen%20AND%20priority%3DP1" \
  -H "Authorization: GenieKey YOUR_API_KEY"

# Alerts with specific tag
curl "https://api.opsgenie.com/v2/alerts?query=tag%3Dproduction" \
  -H "Authorization: GenieKey YOUR_API_KEY"
```

## Webhook Events

OpsGenie can send webhook events for:

- `alerts.created` - New alert created
- `alerts.acknowledged` - Alert acknowledged
- `alerts.closed` - Alert closed
- `alerts.escalated` - Alert escalated
- `alerts.note_added` - Note added to alert
- `incidents.created` - New incident
- `incidents.updated` - Incident updated
- `incidents.closed` - Incident resolved

### Webhook Configuration

1. Go to Settings > Webhooks
2. Click "Add Webhook"
3. Enter webhook URL
4. Select event types
5. Configure authentication if needed
6. Test and save

### Example Webhook Payload

```json
{
  "action": "Create",
  "alert": {
    "alertId": "550e8400-e29b-41d4-a716-446655440000",
    "message": "Server CPU High",
    "description": "CPU > 90%",
    "priority": "P2",
    "status": "open",
    "createdAt": "2024-01-15T10:30:00Z"
  },
  "source": "Datadog"
}
```

## SDKs and Libraries

### Official SDKs

- **Java** - opsgenie-sdk-java
- **Go** - opsgenie-go-sdk
- **Python** - opsgenie-sdk-python
- **Node.js** - opsgenie-sdk-js

### Community Libraries

Check GitHub for additional community-maintained SDKs in other languages.

## Code Examples

### Python

```python
from opsgenie.swagger_client import ApiClient
from opsgenie.swagger_client.swagger.apis.alert_api import AlertApi
from opsgenie.swagger_client.swagger.models.create_alert_payload import CreateAlertPayload

client = ApiClient(api_key="YOUR_API_KEY")
alert_api = AlertApi(api_client=client)

payload = CreateAlertPayload(
    message="Alert from Python",
    priority="P3",
    tags=["python", "test"]
)

response = alert_api.create_alert(create_alert_payload=payload)
print(f"Alert created: {response.data.alert_id}")
```

### JavaScript/Node.js

```javascript
const OpsGenieClient = require('opsgenie-sdk').OpsGenieClient;
const AlertApi = require('opsgenie-sdk').AlertApi;

const client = new OpsGenieClient({
  apiKey: 'YOUR_API_KEY'
});

const alertApi = new AlertApi(client);

alertApi.createAlert({
  message: 'Alert from Node.js',
  priority: 'P3'
}).then(response => {
  console.log('Alert created:', response.data.alertId);
}).catch(err => {
  console.error('Error:', err);
});
```

### Java

```java
import com.opsgenie.oas.client.ApiClient;
import com.opsgenie.oas.client.api.AlertApi;
import com.opsgenie.oas.client.model.CreateAlertPayload;

ApiClient client = new ApiClient();
client.setApiKey("YOUR_API_KEY");

AlertApi alertApi = new AlertApi(client);

CreateAlertPayload payload = new CreateAlertPayload();
payload.setMessage("Alert from Java");
payload.setPriority(CreateAlertPayload.PriorityEnum.P3);

alertApi.createAlert(payload);
```

## Troubleshooting

### 401 Unauthorized

- Verify API key is correct
- Check API key has required permissions
- Ensure API key is not expired

### 429 Too Many Requests

- Implement exponential backoff retry logic
- Reduce request rate
- Contact Atlassian for rate limit increase

### 422 Unprocessable Entity

- Check required fields are included
- Verify field values are valid
- Review error message for specific validation errors

## Deprecations

OpsGenie is being discontinued. Consider migrating to Jira Service Management's API.

## Support

- API Status: https://status.opsgenie.com/
- Documentation: https://docs.opsgenie.com/
- Community: https://community.atlassian.com/t5/OpsGenie/ct-p/opsgenie
