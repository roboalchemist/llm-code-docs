# Source: https://docs.pentaho.com/pdc-api-docs/v1/get-started-with-pdc-api-v1.md

# Get started with PDC API

The Data Catalog API enables you to programmatically interact with your catalog environment. You can use it to connect to data sources, run profiling jobs, trigger discovery, manage glossaries, or automate governance tasks without relying on the user interface.

This guide helps you get up and running in minutes. You will:

* Configure the base API URL for your environment (production, staging, or local).
* Authenticate using OAuth2 to obtain a bearer token.
* Make your first API request to verify connectivity.
* Add a data source and trigger a profiling job.
* Poll a job until it completes and view the results.

Perform the following steps to quickly start with PDC API:

{% stepper %}
{% step %}

### Open Swagger UI

Open the Swagger UI for your environment:

```
https://<your-domain>/api/public/v1/swagger/
```

Example:

```
https://10.177.176.228/api/public/v1/swagger/
```

This page lists all available PDC API endpoints grouped by domain.
{% endstep %}

{% step %}

### Get a bearer token

Use the Auth endpoint to authenticate with your PDC username and password.

```bash
curl -X POST "https://<your-domain>/api/public/v1/auth" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=<your-username>" \
  -d "password=<your-password>"
```

Successful response (200):

```json
{
  "message": "OK",
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR..."
  }
}
```

Copy the `accessToken` value.
{% endstep %}

{% step %}

### Authorize in Swagger UI

1. Click **Authorize** in the Swagger UI.
2. Paste the bearer token (without the `Bearer` prefix).
3. Click **Authorize**.

Swagger UI will now include the token automatically in every request.
{% endstep %}

{% step %}

### Call a protected endpoint

Now test an authenticated request — for example, list notifications:

```bash
curl -X GET "https://<your-domain>/api/public/v1/notifications" \
  -H "accept: application/json" \
  -H "Authorization: Bearer <accessToken>"
```

Sample response:

```json
[
  {
    "id": "notif_12345",
    "type": "JOB_COMPLETED",
    "message": "Profiling job finished successfully",
    "timestamp": "2025-09-01T08:30:00Z"
  }
]
```

{% endstep %}
{% endstepper %}
