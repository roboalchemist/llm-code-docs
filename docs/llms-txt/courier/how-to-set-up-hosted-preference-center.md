# Source: https://www.courier.com/docs/tutorials/preferences/how-to-set-up-hosted-preference-center.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How To Set Up a Hosted Preference Center

> Create subscription topics, map them to notification templates, and deploy a Courier-hosted preference page so your users can manage their notification settings.

Give your users a branded page where they control which notifications they receive and how. This tutorial walks through the full setup: creating topics in the Preferences Editor, connecting them to templates, and adding preference links to your notifications.

By the end, your users will be able to visit a hosted page to opt in/out of notification categories and (on Enterprise plans) choose delivery channels.

## Prerequisites

* A [Courier account](https://app.courier.com/) with at least one configured provider (e.g. SendGrid, Twilio)
* At least one published notification template

## Step 1: Create Subscription Topics

Subscription topics are the notification categories your users can control. For example: "Product Updates", "Marketing", "Security Alerts".

<Steps>
  <Step title="Open the Preferences Editor">
    Navigate to [Settings > Preferences Editor](https://app.courier.com/settings/preferences) in the Courier dashboard.

    <Frame caption="Preferences Editor in the Courier dashboard">
      <img src="https://mintcdn.com/courier-4f1f25dc/COhQJbAYr9RT05BN/assets/tutorials/preferences/preferences-editor.png?fit=max&auto=format&n=COhQJbAYr9RT05BN&q=85&s=7edbc81d44ef4f4618eac060f2a128e9" alt="Preferences Editor" width="2988" height="1760" data-path="assets/tutorials/preferences/preferences-editor.png" />
    </Frame>
  </Step>

  <Step title="Create a Subscription Topic">
    Click **Add Topic** and give it a user-facing name (e.g. "Product Updates"). This name is what your users will see on the preference page.

    <Frame caption="Creating a new subscription topic">
      <img src="https://mintcdn.com/courier-4f1f25dc/COhQJbAYr9RT05BN/assets/tutorials/preferences/topic-editor-modal.png?fit=max&auto=format&n=COhQJbAYr9RT05BN&q=85&s=0b15859fc82de0e8ba1cf84a001269da" alt="Topic editor modal" width="2030" height="1260" data-path="assets/tutorials/preferences/topic-editor-modal.png" />
    </Frame>
  </Step>

  <Step title="Set the Default State">
    Choose whether users start opted in, opted out, or are required to receive this topic:

    | Default State | Behavior                                             |
    | ------------- | ---------------------------------------------------- |
    | **On**        | Users receive notifications unless they opt out      |
    | **Off**       | Users must opt in to receive notifications           |
    | **Required**  | Users cannot opt out (e.g. security alerts, billing) |

    For most notification categories, **On** is appropriate. Use **Required** sparingly for critical communications.
  </Step>

  <Step title="Configure Unsubscribe Headers">
    Each topic has an **Unsubscribe Headers** setting that controls whether Courier includes `List-Unsubscribe` headers in emails sent for this topic:

    | Setting | When to use                                                                                        |
    | ------- | -------------------------------------------------------------------------------------------------- |
    | **Off** | Transactional messages (order confirmations, password resets) that users should always receive     |
    | **On**  | Marketing messages (newsletters, promotions) where email clients should show an unsubscribe option |

    When enabled, email clients like Gmail and Apple Mail display a native "Unsubscribe" button in the message header, which helps with deliverability and compliance.
  </Step>

  <Step title="Create a Preference Section (Optional)">
    Click **Add Section** to group related topics together on the preference page. For example, a "Marketing" section might contain "Product Updates", "Newsletter", and "Event Invitations".

    If you don't create sections, all topics appear in a flat list.

    <Frame caption="Preference section grouping related topics">
      <img src="https://mintcdn.com/courier-4f1f25dc/COhQJbAYr9RT05BN/assets/tutorials/preferences/topic-section-example.png?fit=max&auto=format&n=COhQJbAYr9RT05BN&q=85&s=0317b9233c8f91d6626d976a91e13995" alt="Topic section example" width="2496" height="1254" data-path="assets/tutorials/preferences/topic-section-example.png" />
    </Frame>
  </Step>
</Steps>

For full details on topic and section configuration, see the [Preferences Editor](/platform/preferences/preferences-editor) reference.

## Step 2: Map Templates to Topics

Connect your notification templates to subscription topics so Courier automatically respects user preferences when sending.

<Steps>
  <Step title="Open Topic Settings">
    In the Preferences Editor, click the topic you created and look for the **Linked Notifications** section.

    <Frame caption="Linked Notifications in topic settings">
      <img src="https://mintcdn.com/courier-4f1f25dc/COhQJbAYr9RT05BN/assets/tutorials/preferences/linked-notifications.png?fit=max&auto=format&n=COhQJbAYr9RT05BN&q=85&s=df69da0d489cc2f61d904f3ab5bb7201" alt="Linked Notifications in topic settings" width="2222" height="1382" data-path="assets/tutorials/preferences/linked-notifications.png" />
    </Frame>
  </Step>

  <Step title="Link Your Templates">
    Select the notification templates that belong to this topic. When a user opts out of the topic, Courier suppresses all linked templates for that user.

    <Note>
      Each template can only be mapped to one subscription topic at a time.
    </Note>
  </Step>

  <Step title="Publish Your Changes">
    Click the **Publish** button in the Preferences Editor. Changes to topics, sections, and template mappings are saved as a draft until you publish. Your hosted preference page and embedded components will not reflect updates until you publish.
  </Step>
</Steps>

You can also set the topic when creating or editing a template in the [Template Designer](/platform/content/template-designer/template-designer-overview).

## Step 3: Add Preference Links to Notifications

Insert preference center URLs into your notification templates so users can access their settings. Courier generates unique, authenticated URLs per user; no additional auth setup is needed.

### In Content Blocks

If your template uses the visual editor with content blocks (text, markdown, quote, list), use:

```
{$.urls.preferences}
```

### In Handlebars Templates

If your template uses Handlebars syntax (template blocks, email templates, brand templates):

```
{{var "urls.preferences"}}
```

### In Elemental JSON

If you build notification content programmatically with [Elemental](/platform/content/elemental/elemental-overview):

```json  theme={null}
{
  "type": "action",
  "content": "Manage Preferences",
  "href": "{$.urls.preferences}",
  "style": "button"
}
```

### In Brand Footer

To show the preference link on every notification automatically, add it to your brand footer. This requires a **Custom MJML/Handlebars** brand template (the standard template only supports social links in the footer).

1. Open your brand in [Settings > Brands](https://app.courier.com/database/brands)
2. Select **Custom MJML/Handle Bars** as the Template Type
3. In the MJML Footer section, add a preference link using the Handlebars variable:

```xml  theme={null}
<mj-wrapper css-class="footer" background-color="#ffecb8">
  <mj-section background-color="#ffecb8" padding="10px">
    <mj-column>
      <mj-text align="center" color="white">
        <a href="{{var "urls.preferences"}}">Manage Notification Preferences</a>
      </mj-text>
    </mj-column>
  </mj-section>
</mj-wrapper>
```

<Frame caption="Custom MJML brand template with preference link in footer">
  <img src="https://mintcdn.com/courier-4f1f25dc/COhQJbAYr9RT05BN/assets/tutorials/preferences/brand-footer-preferences-link.png?fit=max&auto=format&n=COhQJbAYr9RT05BN&q=85&s=d9a7f2ab6f70fa41522ea23b34b8c51a" alt="Brand footer with preference link in MJML" width="2988" height="1798" data-path="assets/tutorials/preferences/brand-footer-preferences-link.png" />
</Frame>

For details on custom brand templates, see the [Brand Designer](/platform/content/brands/brand-designer) reference.

<Note>
  **Important**: Include `to.user_id` in your send requests for preference links to work. The user ID maps recipients to their preference profiles.
</Note>

## Step 4: Add Unsubscribe Links (Recommended)

Add one-click unsubscribe links so users can quickly opt out of a specific topic. This is important for email compliance.

The variable syntax matches the preference link pattern:

| Context        | Syntax                           |
| -------------- | -------------------------------- |
| Content blocks | `{$.urls.unsubscribe}`           |
| Handlebars     | `{{var "urls.unsubscribe"}}`     |
| Elemental JSON | `"href": "{$.urls.unsubscribe}"` |

When a user clicks an unsubscribe link, Courier shows a confirmation page and opts them out of the topic associated with that notification.

## Step 5: Preview and Test

Before going live, verify everything works end-to-end.

<Steps>
  <Step title="Preview the Preference Page">
    In the [Preferences Editor](https://app.courier.com/settings/preferences), click **Preview** to see how your preference page looks to users. It automatically applies your [brand styling](/platform/content/brands/brands-overview).

    <Frame caption="Hosted preference center preview">
      <img src="https://mintcdn.com/courier-4f1f25dc/COhQJbAYr9RT05BN/assets/tutorials/preferences/preview-preferences.png?fit=max&auto=format&n=COhQJbAYr9RT05BN&q=85&s=54fec69609de450136ce840e1aa59f55" alt="Hosted preference center preview" width="2130" height="1872" data-path="assets/tutorials/preferences/preview-preferences.png" />
    </Frame>
  </Step>

  <Step title="Send a Test Notification">
    Send a test notification to yourself and confirm:

    * The preference link in the notification opens the hosted preference page
    * The unsubscribe link opts you out of the correct topic
    * Opting out actually suppresses future notifications for that topic
  </Step>
</Steps>

## Step 6: Manage Preferences Programmatically (Optional)

You can also read and update user preferences from your backend using the API or SDKs. This is useful for syncing preferences with your own settings UI or importing existing preferences.

### Fetch a User's Preferences

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

### Update a User's Topic Preference

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

### Set Custom Routing (Enterprise)

Let users control which channels they receive notifications on for a given topic:

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
  Custom routing requires an Enterprise plan. The notification template must have multiple delivery channels configured and be linked to a subscription topic for channel preferences to take effect.
</Note>

For full API documentation, see the [User Preferences API reference](/api-reference/user-preferences/get-users-preferences).

## What's Next

<CardGroup cols={2}>
  <Card title="Embed Preferences in React" href="/tutorials/preferences/how-to-embed-preferences-in-react" icon="react">
    Build an in-app preference center with React components
  </Card>

  <Card title="Preferences Editor Reference" href="/platform/preferences/preferences-editor" icon="gear">
    Full reference for topic and section configuration
  </Card>

  <Card title="Hosted Page Reference" href="/platform/preferences/hosted-page" icon="globe">
    Detailed hosted preference center documentation
  </Card>

  <Card title="User Preferences API" href="/api-reference/user-preferences/get-users-preferences" icon="code">
    API reference for managing preferences programmatically
  </Card>
</CardGroup>
