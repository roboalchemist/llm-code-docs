# Source: https://docs.airbyte.com/ai-agents/connectors/zendesk-talk/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/zendesk-support/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/zendesk-chat/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/woocommerce/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/typeform/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/twilio/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/tiktok-marketing/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/stripe/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/snapchat-marketing/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/slack/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/shopify/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/sentry/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/sendgrid/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/salesforce/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/pylon/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/pinterest/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/paypal-transaction/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/orb/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/notion/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/monday/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/mailchimp/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/linkedin-ads/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/linear/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/klaviyo/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/jira/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/intercom/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/incident-io/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/hubspot/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/harvest/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/greenhouse/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/granola/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/google-search-console/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/google-drive/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/google-analytics-data-api/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/google-ads/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/gong/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/gmail/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/gitlab/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/github/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/freshdesk/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/facebook-marketing/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/confluence/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/clickup-api/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/chargebee/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/ashby/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/asana/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/amplitude/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/amazon-seller-partner/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/amazon-ads/AUTH.md

# Source: https://docs.airbyte.com/ai-agents/connectors/airtable/AUTH.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-airtable/latest/icon.svg)

# Airtable authentication

Copy Page

This page documents the authentication and configuration options for the Airtable agent connector.

## Authentication[​](#authentication "Direct link to Authentication")

### Open source execution[​](#open-source-execution "Direct link to Open source execution")

In open source mode, you provide API credentials directly to the connector.

#### OAuth[​](#oauth "Direct link to OAuth")

This authentication method isn't available for this connector.

#### Token[​](#token "Direct link to Token")

`credentials` fields you need:

| Field Name              | Type  | Required | Description                                                                                             |
| ----------------------- | ----- | -------- | ------------------------------------------------------------------------------------------------------- |
| `personal_access_token` | `str` | Yes      | Airtable Personal Access Token. See <https://airtable.com/developers/web/guides/personal-access-tokens> |

Example request:

```
from airbyte_agent_airtable import AirtableConnector
from airbyte_agent_airtable.models import AirtableAuthConfig

connector = AirtableConnector(
    auth_config=AirtableAuthConfig(
        personal_access_token="<Airtable Personal Access Token. See https://airtable.com/developers/web/guides/personal-access-tokens>"
    )
)
```

### Hosted execution[​](#hosted-execution "Direct link to Hosted execution")

In hosted mode, you first create a connector via the Airbyte API (providing your OAuth or Token credentials), then execute operations using either the Python SDK or API. If you need a step-by-step guide, see the [hosted execution tutorial](https://docs.airbyte.com/ai-agents/quickstarts/tutorial-hosted).

#### OAuth[​](#oauth-1 "Direct link to OAuth")

This authentication method isn't available for this connector.

#### Bring your own OAuth flow[​](#bring-your-own-oauth-flow "Direct link to Bring your own OAuth flow")

This authentication method isn't available for this connector.

#### Token[​](#token-1 "Direct link to Token")

Create a connector with Token credentials.

`credentials` fields you need:

| Field Name              | Type  | Required | Description                                                                                             |
| ----------------------- | ----- | -------- | ------------------------------------------------------------------------------------------------------- |
| `personal_access_token` | `str` | Yes      | Airtable Personal Access Token. See <https://airtable.com/developers/web/guides/personal-access-tokens> |

Example request:

```
curl -X POST "https://api.airbyte.ai/api/v1/integrations/connectors" \
  -H "Authorization: Bearer <YOUR_BEARER_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "<CUSTOMER_NAME>",
    "connector_type": "Airtable",
    "name": "My Airtable Connector",
    "credentials": {
      "personal_access_token": "<Airtable Personal Access Token. See https://airtable.com/developers/web/guides/personal-access-tokens>"
    }
  }'
```

#### Execution[​](#execution "Direct link to Execution")

After creating the connector, execute operations using either the Python SDK or API. If your Airbyte client can access multiple organizations, include `organization_id` in `AirbyteAuthConfig` and `X-Organization-Id` in raw API calls.

**Python SDK**

```
from airbyte_agent_airtable import AirtableConnector, AirbyteAuthConfig

connector = AirtableConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@AirtableConnector.tool_utils
async def airtable_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

**API**

```
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors/<connector_id>/execute' \
  -H 'Authorization: Bearer <YOUR_BEARER_TOKEN>' \
  -H 'X-Organization-Id: <YOUR_ORGANIZATION_ID>' \
  -H 'Content-Type: application/json' \
  -d '{"entity": "<entity>", "action": "<action>", "params": {}}'
```
