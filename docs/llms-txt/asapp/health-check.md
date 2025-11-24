# Source: https://docs.asapp.com/getting-started/developers/health-check.md

# Health Check

> Check the operational status of ASAPP's API platform

ASAPP provides a simple endpoint to check if our API services are operating normally. You can use this to verify the platform's availability or implement automated health monitoring.

## Checking API Health

Send a GET request to the [health check](/apis/health-check/check-asapps-apis-health) endpoint:

```bash  theme={null}
curl https://api.sandbox.asapp.com/v1/health \
  -H "asapp-api-id: YOUR_API_ID" \
  -H "asapp-api-secret: YOUR_API_SECRET"
```

A successful response will return:

```json  theme={null}
{
  "healthCheck": "SUCCESS"
}
```

The status will be either `SUCCESS` when operating normally or `FAILED` if there are service disruptions.
