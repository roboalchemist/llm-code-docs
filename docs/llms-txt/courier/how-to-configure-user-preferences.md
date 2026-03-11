# Source: https://www.courier.com/docs/tutorials/preferences/how-to-configure-user-preferences.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How To Configure Preferences via API

> Use the Preferences API to read and update user notification preferences programmatically, including opt-in/out status and channel routing for Enterprise customers.

Use the [User Preferences API](/api-reference/user-preferences/get-users-preferences) to manage notification preferences from your backend. This tutorial covers reading and updating preferences programmatically; for setting up subscription topics and surfacing preferences to users, see:

* [How To Set Up a Hosted Preference Center](/tutorials/preferences/how-to-set-up-hosted-preference-center) for a turnkey hosted page
* [How To Embed Preferences in React](/tutorials/preferences/how-to-embed-preferences-in-react) for in-app components

## Prerequisites

* Subscription topics configured in the [Preferences Editor](https://app.courier.com/settings/preferences)
* Templates mapped to topics
* Your Courier API key (from [Settings > API Keys](https://app.courier.com/settings/api-keys))

## Required Parameters

Every preference update needs two identifiers:

* **`user_id`** - The recipient's unique ID (same ID used in send requests)
* **`topic_id`** - The subscription topic ID, found in the [Preferences Editor](/platform/preferences/preferences-editor)

## Read a User's Preferences

Fetch all preferences for a user to see their current opt-in/out status across all topics:

<CodeGroup>
  ```bash curl theme={null}
  curl -X GET https://api.courier.com/users/{user_id}/preferences \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN"
  ```

  ```typescript Node theme={null}
  import Courier from "@trycourier/courier";

  const client = new Courier({ apiKey: "your_api_key" });

  const { items } = await client.users.preferences.retrieve("user_123");

  for (const topic of items) {
    console.log(`${topic.topic_name}: ${topic.status}`);
    // e.g. "Product Updates: OPTED_IN"
  }
  ```

  ```python Python theme={null}
  from courier import Courier

  client = Courier(api_key="your_api_key")

  response = client.users.preferences.retrieve("user_123")

  for topic in response.items:
      print(f"{topic.topic_name}: {topic.status}")
  ```
</CodeGroup>

## Update a Topic Preference

Set a user's opt-in status for a specific topic. The `topic` object requires a `status` field with one of these values:

| Status      | Behavior                                                                  |
| ----------- | ------------------------------------------------------------------------- |
| `OPTED_IN`  | User receives notifications for this topic                                |
| `OPTED_OUT` | User does not receive notifications for this topic                        |
| `REQUIRED`  | User cannot opt out (use for critical notifications like security alerts) |

<CodeGroup>
  ```bash curl theme={null}
  curl -X PUT https://api.courier.com/users/{user_id}/preferences/{topic_id} \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "topic": {
        "status": "OPTED_IN"
      }
    }'
  ```

  ```typescript Node theme={null}
  import Courier from "@trycourier/courier";

  const client = new Courier({ apiKey: "your_api_key" });

  await client.users.preferences.updateOrCreateTopic("TOPIC_ID", {
    user_id: "user_123",
    topic: {
      status: "OPTED_IN",
    },
  });
  ```

  ```python Python theme={null}
  from courier import Courier

  client = Courier(api_key="your_api_key")

  client.users.preferences.update_or_create_topic(
      "TOPIC_ID",
      user_id="user_123",
      topic={"status": "OPTED_IN"},
  )
  ```
</CodeGroup>

## Custom Routing (Enterprise)

Enterprise customers can set channel delivery preferences per topic. For example, if a notification template has email, SMS, and push channels, you can let a user receive only email:

<CodeGroup>
  ```bash curl theme={null}
  curl -X PUT https://api.courier.com/users/{user_id}/preferences/{topic_id} \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "topic": {
        "status": "OPTED_IN",
        "has_custom_routing": true,
        "custom_routing": ["email"]
      }
    }'
  ```

  ```typescript Node theme={null}
  import Courier from "@trycourier/courier";

  const client = new Courier({ apiKey: "your_api_key" });

  await client.users.preferences.updateOrCreateTopic("TOPIC_ID", {
    user_id: "user_123",
    topic: {
      status: "OPTED_IN",
      has_custom_routing: true,
      custom_routing: ["email"],
    },
  });
  ```

  ```python Python theme={null}
  from courier import Courier

  client = Courier(api_key="your_api_key")

  client.users.preferences.update_or_create_topic(
      "TOPIC_ID",
      user_id="user_123",
      topic={
          "status": "OPTED_IN",
          "has_custom_routing": True,
          "custom_routing": ["email"],
      },
  )
  ```
</CodeGroup>

<Note>
  Custom routing requires an Enterprise plan. The notification template must have multiple delivery channels configured and be linked to a subscription topic.
</Note>

## Tenant-Scoped Preferences

If your app uses [tenants](/platform/tenants/tenants-overview), pass a `tenant_id` to read or write preferences scoped to a specific tenant:

<CodeGroup>
  ```bash curl theme={null}
  curl -X GET "https://api.courier.com/users/{user_id}/preferences?tenant_id=tenant_abc" \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN"
  ```

  ```typescript Node theme={null}
  const { items } = await client.users.preferences.retrieve("user_123", {
    tenant_id: "tenant_abc",
  });
  ```

  ```python Python theme={null}
  response = client.users.preferences.retrieve("user_123", tenant_id="tenant_abc")
  ```
</CodeGroup>

## What's Next

<CardGroup cols={2}>
  <Card title="Set Up Hosted Preferences" href="/tutorials/preferences/how-to-set-up-hosted-preference-center" icon="globe">
    Deploy a hosted preference page for your users
  </Card>

  <Card title="Embed Preferences in React" href="/tutorials/preferences/how-to-embed-preferences-in-react" icon="react">
    Build an in-app preference center with React components
  </Card>

  <Card title="Preferences Editor" href="/platform/preferences/preferences-editor" icon="gear">
    Configure topics, sections, and channel options
  </Card>

  <Card title="User Preferences API" href="/api-reference/user-preferences/get-users-preferences" icon="code">
    Full API reference
  </Card>
</CardGroup>
