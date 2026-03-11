# Source: https://docs.base44.com/developers/references/monitoring-api/get-started/authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> How to authenticate with the Enterprise Monitoring API

All Monitoring API endpoints require authentication, except for the health check endpoint (`GET /health`).

## Required role

You must have **admin** or **owner** role in the workspace to access the Monitoring API. Regular workspace members cannot access these endpoints.

Requests without the proper role return a `401 Unauthorized` error.

To learn about workspace roles, see [Managing your workspace members](/Account-and-billing/Managing-your-workspaces#managing-your-workspace-members).

## API key

Include your API key in a header with all requests:

```bash  theme={null}
api_key: YOUR_API_KEY
```

### Example request

```curl  theme={null}
curl --request GET \
  --url http://localhost:3000/api/v1/monitoring/analytics/{workspace_id} \
  --header 'api_key: <api_key>'
```

### Get your API key

To get your API key:

1. Click your profile icon at the top right of your account.
2. Click **Settings**.
3. Select the **Account** tab.
4. Scroll down to the **API Key** section.

<Warning>
  Your API key provides access to your workspace. Do not share it with others.
  Only use it in a secure environment.
</Warning>


Built with [Mintlify](https://mintlify.com).