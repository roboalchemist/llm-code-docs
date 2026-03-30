# Source: https://www.courier.com/docs/tutorials/sending/how-to-manage-user-profiles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Manage User Profiles

> Create, update, and use user profiles to store contact details, custom attributes, and channel tokens for personalized notification delivery.

User profiles store the contact details and attributes Courier needs to deliver notifications. Instead of passing an email address or phone number with every send call, you create a profile once and send to the user by ID.

This tutorial covers creating profiles, updating them with new data, storing push tokens, and using profile data in your notifications.

## Prerequisites

* A [Courier account](https://app.courier.com/) with at least one configured provider
* Your Courier API key (found in [Settings > API Keys](https://app.courier.com/settings/api-keys))

## Create a User Profile

The Profiles API uses `POST /profiles/:user_id` to create or merge data into a profile. If the profile already exists, the supplied values are merged with the existing profile.

<Steps>
  <Step title="Create a profile with contact details">
    <CodeGroup>
      ```bash cURL icon="terminal" wrap theme={null}
      curl -X POST https://api.courier.com/profiles/user_123 \
        -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "profile": {
            "email": "jane@example.com",
            "phone_number": "+15551234567",
            "name": "Jane Doe",
            "locale": "en_US",
            "custom": {
              "company": "Acme Corp",
              "role": "admin",
              "plan": "premium"
            }
          }
        }'
      ```

      ```javascript Node.js icon="node-js" theme={null}
      import Courier from "@trycourier/courier";

      const client = new Courier({ apiKey: "your_api_key" });

      await client.profiles.create("user_123", {
        profile: {
          email: "jane@example.com",
          phone_number: "+15551234567",
          name: "Jane Doe",
          locale: "en_US",
          custom: {
            company: "Acme Corp",
            role: "admin",
            plan: "premium",
          },
        },
      });
      ```

      ```python Python icon="python" theme={null}
      from courier import Courier

      client = Courier(api_key="your_api_key")

      client.profiles.create(
          "user_123",
          profile={
              "email": "jane@example.com",
              "phone_number": "+15551234567",
              "name": "Jane Doe",
              "locale": "en_US",
              "custom": {
                  "company": "Acme Corp",
                  "role": "admin",
                  "plan": "premium",
              },
          },
      )
      ```
    </CodeGroup>

    The `user_id` in the URL path (`user_123`) is the unique identifier you'll use to send notifications to this user. You choose this ID; it can be any string.
  </Step>

  <Step title="Verify the profile">
    <CodeGroup>
      ```bash cURL icon="terminal" wrap theme={null}
      curl https://api.courier.com/profiles/user_123 \
        -H "Authorization: Bearer $COURIER_AUTH_TOKEN"
      ```

      ```javascript Node.js icon="node-js" theme={null}
      const { profile } = await client.profiles.retrieve("user_123");
      console.log(profile);
      ```

      ```python Python icon="python" theme={null}
      response = client.profiles.retrieve("user_123")
      print(response.profile)
      ```
    </CodeGroup>

    You can also view the profile in the [Users](https://app.courier.com/users) section of the Courier dashboard.
  </Step>
</Steps>

## Update a Profile

There are two update strategies depending on whether you want to merge or fully replace the profile data.

### Merge Update (POST)

`POST /profiles/:user_id` merges the supplied values into the existing profile. Existing fields that aren't included in the request are preserved.

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X POST https://api.courier.com/profiles/user_123 \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "profile": {
        "custom": {
          "plan": "enterprise"
        }
      }
    }'
  ```

  ```javascript Node.js icon="node-js" theme={null}
  await client.profiles.create("user_123", {
    profile: {
      custom: { plan: "enterprise" },
    },
  });
  ```

  ```python Python icon="python" theme={null}
  client.profiles.create(
      "user_123",
      profile={"custom": {"plan": "enterprise"}},
  )
  ```
</CodeGroup>

After this call, `email`, `phone_number`, `name`, and other existing fields are unchanged; only `custom.plan` is updated.

### Full Replace (PUT)

`PUT /profiles/:user_id` replaces the entire profile. Any fields not included in the request are removed.

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X PUT https://api.courier.com/profiles/user_123 \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "profile": {
        "email": "jane.doe@newcompany.com",
        "name": "Jane Doe"
      }
    }'
  ```

  ```javascript Node.js icon="node-js" theme={null}
  await client.profiles.replace("user_123", {
    profile: {
      email: "jane.doe@newcompany.com",
      name: "Jane Doe",
    },
  });
  ```

  ```python Python icon="python" theme={null}
  client.profiles.replace(
      "user_123",
      profile={
          "email": "jane.doe@newcompany.com",
          "name": "Jane Doe",
      },
  )
  ```
</CodeGroup>

<Warning>
  A `PUT` replaces the entire profile. After this call, `phone_number`, `locale`, `custom`, and any other fields from the original profile are gone. Use `POST` for partial updates.
</Warning>

## Send to a Profile

Once a profile exists, send notifications by user ID instead of specifying contact details inline.

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X POST https://api.courier.com/send \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "message": {
        "to": {
          "user_id": "user_123"
        },
        "template": "WELCOME_EMAIL",
        "data": {
          "login_url": "https://app.example.com/login"
        }
      }
    }'
  ```

  ```javascript Node.js icon="node-js" theme={null}
  await client.send.message({
    message: {
      to: { user_id: "user_123" },
      template: "WELCOME_EMAIL",
      data: { login_url: "https://app.example.com/login" },
    },
  });
  ```

  ```python Python icon="python" theme={null}
  client.send.message(
      message={
          "to": {"user_id": "user_123"},
          "template": "WELCOME_EMAIL",
          "data": {"login_url": "https://app.example.com/login"},
      },
  )
  ```
</CodeGroup>

Courier looks up the user's profile, resolves their contact details (email, phone, push tokens), and routes the notification based on channel configuration and user preferences.

### Inline Profile Overrides

You can override or supplement profile data at send time. The inline values are merged with the stored profile for that specific send without modifying the stored profile.

```json  theme={null}
{
  "message": {
    "to": {
      "user_id": "user_123",
      "email": "temporary-override@example.com"
    },
    "template": "WELCOME_EMAIL"
  }
}
```

## Store Channel Tokens

Push notification providers (FCM, APNS) require device tokens to deliver messages. Store tokens using the [Device Tokens API](/api-reference/device-tokens/add-single-token-to-user) or let [Courier SDKs](/sdk-libraries/sdks-overview) handle it automatically.

### Via API

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X PUT https://api.courier.com/users/user_123/tokens/device_abc \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "token": "fcm_device_token_here",
      "provider_key": "firebase-fcm",
      "device": {
        "app_id": "com.example.myapp",
        "platform": "android"
      }
    }'
  ```

  ```javascript Node.js icon="node-js" theme={null}
  await client.users.tokens.addSingle("device_abc", {
    user_id: "user_123",
    body_token: "fcm_device_token_here",
    provider_key: "firebase-fcm",
    device: {
      app_id: "com.example.myapp",
      platform: "android",
    },
  });
  ```

  ```python Python icon="python" theme={null}
  client.users.tokens.add_single(
      "device_abc",
      user_id="user_123",
      body_token="fcm_device_token_here",
      provider_key="firebase-fcm",
      device={
          "app_id": "com.example.myapp",
          "platform": "android",
      },
  )
  ```
</CodeGroup>

### Via SDK (Recommended)

Courier's mobile SDKs handle token registration, refresh, and cleanup automatically:

```javascript  theme={null}
// React Native
import { Courier } from "@courier/react-native";

await Courier.setUserId("user_123");
// SDK automatically registers device tokens
```

For details, see the [iOS SDK](/platform/inbox/mobile/ios-sdk), [Android SDK](/platform/inbox/mobile/android-sdk), or [React Native SDK](/sdk-libraries/react-native).

## Use Profile Data in Templates

Any field stored in a user's profile is available as a template variable. In your notification templates, reference profile fields with the `profile` prefix.

For example, if a profile has:

```json  theme={null}
{
  "name": "Jane Doe",
  "custom": {
    "company": "Acme Corp"
  }
}
```

You can use `{{profile.name}}` and `{{profile.custom.company}}` in your template content. You can also use `{{name}}` as a shorthand for top-level profile fields.

<Tip>
  Custom attributes stored under the `custom` key are great for personalization: user roles, subscription tiers, company names, or any data your templates need.
</Tip>

## Delete a Profile

<CodeGroup>
  ```bash cURL icon="terminal" wrap theme={null}
  curl -X DELETE https://api.courier.com/profiles/user_123 \
    -H "Authorization: Bearer $COURIER_AUTH_TOKEN"
  ```

  ```javascript Node.js icon="node-js" theme={null}
  await client.profiles.delete("user_123");
  ```

  ```python Python icon="python" theme={null}
  client.profiles.delete("user_123")
  ```
</CodeGroup>

Deleting a profile removes all stored data. Notifications sent to this user ID will fail until a new profile is created.

## What's Next

<CardGroup cols={2}>
  <Card title="User Management" icon="users" href="/platform/users/users">
    Platform reference for user profiles, CSV import, and push tokens
  </Card>

  <Card title="Profiles API Reference" icon="user" href="/api-reference/user-profiles/get-a-profile">
    Full API documentation for profile CRUD operations
  </Card>

  <Card title="Send Your First Message" icon="paper-plane" href="/tutorials/sending/how-to-send-your-first-message">
    Get started with the Courier Send API
  </Card>

  <Card title="Configure Preferences" icon="list" href="/tutorials/preferences/how-to-configure-user-preferences">
    Let users control which notifications they receive
  </Card>
</CardGroup>
