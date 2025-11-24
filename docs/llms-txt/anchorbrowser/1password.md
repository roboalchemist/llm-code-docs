# Source: https://docs.anchorbrowser.io/integrations/1password.md

# 1Password

> Securely inject 1Password secrets into your browser sessions

## Overview

The 1Password integration **enables your AI agent to securely authenticate with services** during browser automation by injecting secrets, credentials, and other sensitive data from your 1Password vaults directly into your Anchor Browser sessions. This gives your AI agent the ability to log into websites, access APIs, and perform authenticated actions **without you needing to hardcode credentials** in your automation scripts.

<Info>
  The actual secret values are **never exposed** to the AI agent, logs, API responses, or any other output
</Info>

## Prerequisites

Before you can use the 1Password integration, you need:

1. **1Password Account**: An active 1Password account with access to the secrets you want to use  in a vault different than “Personal”.
2. **Anchor Browser API Key**: Your Anchor Browser API key for authentication

## Getting a 1Password Service Account Token

1. Log in to your [1Password account](https://my.1password.com/)
2. Navigate to **Developer** → **Directory** → **Service Accounts**
3. Click **Create Service Account**
4. Give your service account a descriptive name (e.g., "Anchor Browser Automation")
5. Grant the service account access to the vaults containing the secrets you need
6. Copy the service account token (starts with `ops_`) - you'll need this for the integration setup

<Warning>
  Store your service account token securely. It provides access to your
  1Password secrets and should be treated like a password.
</Warning>

## Creating a 1Password Integration

### Using the API

Create a 1Password integration using the AnchorBrowser API:

```bash  theme={null}
curl -X POST https://api.anchorbrowser.io/v1/integrations \
  -H "anchor-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My 1Password Integration",
    "type": "1PASSWORD",
    "credentials": {
      "type": "serviceAccount",
      "data": {
        "serviceAccount": "ops_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      }
    }
  }'
```

**Response:**

```json  theme={null}
{
  "data": {
    "integration": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "My 1Password Integration",
      "type": "1PASSWORD",
      "path": "integrations/team-id/550e8400-e29b-41d4-a716-446655440000",
      "createdAt": "2024-01-01T00:00:00.000Z"
    }
  }
}
```

Save the `id` from the response - you'll need it to use the integration in browser sessions.

## Using 1Password Integration in Browser Sessions

Once you've created a 1Password integration, you can use it in your browser sessions to automatically load secrets.

### Load All Secrets

Load all secrets from your 1Password vaults:

```bash  theme={null}
curl -X POST https://api.anchorbrowser.io/v1/sessions \
  -H "anchor-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "integrations": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "type": "1PASSWORD",
        "configuration": {
          "load_mode": "all"
        }
      }
    ]
  }'
```

### Load Specific Secrets

Load only specific secrets using 1Password secret references:

```bash  theme={null}
curl -X POST https://api.anchorbrowser.io/v1/sessions \
  -H "anchor-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "integrations": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "type": "1PASSWORD",
        "configuration": {
          "load_mode": "specific",
          "secrets": [
            "op://Production/Database/username",
            "op://Production/Database/password",
            "op://Production/API Keys/stripe_key"
          ]
        }
      }
    ]
  }'
```

## 1Password Secret Reference Format

1Password uses a specific format for secret references:

```
op://[vault]/[item]/[field]
```

* **vault**: The name of your 1Password vault
* **item**: The name of the item in the vault
* **field**: The specific field within the item

### Examples

```
op://Production/AWS Credentials/access_key_id
op://Development/GitHub/personal_access_token
op://Shared/Stripe/api_key
```

## Accessing Secrets in Your Browser Session

Once loaded, secrets are available as environment variables in your browser session. The environment variable name is derived from the secret reference:

* Secret reference: `op://Production/Database/username`
* Environment variable: `OP_PRODUCTION_DATABASE_USERNAME`

The conversion follows these rules:

1. Remove the `op://` prefix
2. Replace `/` with `_`
3. Convert to uppercase
4. Prefix with `OP_`

<Info>
  **AI Agent Security**: When your AI agent accesses these environment variables, it can use them for authentication with external services, but the actual credential values are never visible in the agent's output, logs, or responses. The credentials are used transparently by the browser environment for authentication purposes only.
</Info>

### Example: Using Secrets in Automation

<CodeGroup>
  ```javascript node.js theme={null}
  (async () => {
    // Create a session with 1Password integration
    const response = await fetch('https://api.anchorbrowser.io/v1/sessions', {
      method: 'POST',
      headers: {
        'anchor-api-key': process.env.ANCHOR_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        integrations: [
          {
            id: integrationId,
            type: '1PASSWORD',
            configuration: {
              load_mode: 'specific',
              secrets: [
                'op://Production/Database/username',
                'op://Production/Database/password'
              ]
            }
          }
        ]
      })
    });


    const sessionData = await response.json();
    console.log(sessionData)

    // Access the secrets in your automation code
    // The secrets are automatically available as environment variables
    // OP_PRODUCTION_DATABASE_USERNAME and OP_PRODUCTION_DATABASE_PASSWORD
    // Your AI agent can use these for authentication without exposing the actual values
  })();
  ```

  ```python python theme={null}
  import os
  import requests

  # Create a session with 1Password integration
  response = requests.post(
      "https://api.anchorbrowser.io/v1/sessions",
      headers={
          "anchor-api-key": os.getenv("ANCHOR_API_KEY"),
          "Content-Type": "application/json"
      },
      json={
          "integrations": [
              {
                  "id": integration_id,
                  "type": "1PASSWORD",
                  "configuration": {
                      "load_mode": "specific",
                      "secrets": [
                          "op://Production/Database/username",
                          "op://Production/Database/password"
                      ]
                  }
              }
          ]
      }
  )

  session_data = response.json()
  print(session_data)
  # Access the secrets in your automation code
  # The secrets are automatically available as environment variables
  # OP_PRODUCTION_DATABASE_USERNAME and OP_PRODUCTION_DATABASE_PASSWORD
  # Your AI agent can use these for authentication without exposing the actual values
  ```
</CodeGroup>

## Managing Integrations

### List All Integrations

```bash  theme={null}
curl -X GET https://api.anchorbrowser.io/v1/integrations \
  -H "anchor-api-key: YOUR_API_KEY"
```

**Response:**

```json  theme={null}
{
  "data": {
    "integrations": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "name": "My 1Password Integration",
        "type": "1PASSWORD",
        "createdAt": "2024-01-01T00:00:00.000Z"
      }
    ]
  }
}
```

### Delete an Integration

```bash  theme={null}
curl -X DELETE https://api.anchorbrowser.io/v1/integrations/550e8400-e29b-41d4-a716-446655440000 \
  -H "anchor-api-key: YOUR_API_KEY"
```

**Response:**

```json  theme={null}
{
  "data": {
    "integration": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "deleted": true,
      "path": "integrations/team-id/550e8400-e29b-41d4-a716-446655440000"
    }
  }
}
```

<Warning>
  Deleting an integration will remove the stored service account token. Any
  browser sessions using this integration will fail to load secrets.
</Warning>

## Troubleshooting

### Integration Creation Fails

* **Invalid Service Account Token**: Verify your token starts with `ops_` and is valid
* **Insufficient Permissions**: Ensure the service account has access to the required vaults

### Secrets Not Loading

* **Invalid Secret Reference**: Check the format of your secret references (`op://vault/item/field`)
* **Service Account Access**: Verify the service account has access to the specified vaults and items
* **Item or Field Not Found**: Ensure the vault, item, and field names are correct and exist

### Environment Variables Not Available

* **Check Secret Reference Format**: Ensure your secret references follow the correct format
* **Verify Integration ID**: Make sure you're using the correct integration ID in your session configuration

## Support

For additional help with 1Password integration:

* [1Password Service Accounts Documentation](https://developer.1password.com/docs/service-accounts/)
* Contact Anchor Browser support at [support@anchorbrowser.io](mailto:support@anchorbrowser.io)
