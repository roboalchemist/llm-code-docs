# Source: https://docs.drip.re/developer/authentication.md

# Source: https://docs.drip.re/api-reference/authentication.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> Learn how to authenticate with the DRIP API using API keys and bearer tokens

The DRIP API uses API key authentication. You'll need to include your API key in the Authorization header of every request.

## Getting Your API Key

1. Log into your DRIP dashboard
2. Navigate to **Settings** > **API Keys**
3. Click **Generate New API Key**
4. Copy and securely store your API key

<Warning>
  Keep your API keys secure and never expose them in client-side code. Treat them like passwords.
</Warning>

## Authentication Header

Include your API key in the `Authorization` header using the Bearer token format:

```bash  theme={"dark"}
Authorization: Bearer YOUR_API_KEY_HERE
```

## Example Request

<CodeGroup>
  ```bash cURL theme={"dark"}
  curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID" \
    -H "Authorization: Bearer YOUR_API_KEY_HERE" \
    -H "Content-Type: application/json"
  ```

  ```javascript JavaScript theme={"dark"}
  const response = await fetch('https://api.drip.re/api/v1/realms/YOUR_REALM_ID', {
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY_HERE',
      'Content-Type': 'application/json'
    }
  });
  ```

  ```python Python theme={"dark"}
  import requests

  headers = {
      'Authorization': 'Bearer YOUR_API_KEY_HERE',
      'Content-Type': 'application/json'
  }

  response = requests.get('https://api.drip.re/api/v1/realms/YOUR_REALM_ID', headers=headers)
  ```

</CodeGroup>

## API Key Permissions

API keys inherit the permissions of the user who created them. Ensure your account has the necessary permissions for the operations you want to perform:

* **Read permissions**: View realm data, member information, point balances
* **Write permissions**: Update member balances, create quests, manage store items
* **Admin permissions**: Full realm management capabilities

## Testing Authentication

You can test your authentication by making a simple request to get your realm information:

```bash  theme={"dark"}
curl -X GET "https://api.drip.re/api/v1/realms/YOUR_REALM_ID" \
  -H "Authorization: Bearer YOUR_API_KEY_HERE"
```

A successful response will return your realm data. An authentication error will return a `401 Unauthorized` status.

## Security Best Practices

<CardGroup cols={2}>
  <Card title="Environment Variables" icon="shield-check">
    Store API keys in environment variables, never in your source code
  </Card>

  <Card title="Rotate Keys" icon="arrows-rotate">
    Regularly rotate your API keys and revoke unused ones
  </Card>

  <Card title="Scope Permissions" icon="lock">
    Use accounts with minimal necessary permissions for API operations
  </Card>

  <Card title="Monitor Usage" icon="chart-line">
    Monitor API key usage to detect unauthorized access
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
