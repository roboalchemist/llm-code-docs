# Source: https://www.courier.com/docs/platform/content/template-settings/general-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# General Settings

> Manage a template's ID, brand, subscription topic, event mapping, conditions, message tags, notes, and publish history.

Each template has a settings panel where you configure its identity, behavior, and publishing. To open it, click the gear icon next to the publish button in the designer.

## General

<Frame caption="General Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/YsQFnOhW0NtR5Dv2/assets/platform/content/notification-settings-general.png?fit=max&auto=format&n=YsQFnOhW0NtR5Dv2&q=85&s=4a025e805c2f01a29c814adeb4d44395" alt="General Settings" width="2068" height="1300" data-path="assets/platform/content/notification-settings-general.png" />
</Frame>

### Notification ID

Every template gets a unique Notification ID assigned by Courier. You can use this ID in the `template` field of your [Send API](/api-reference/send/send-a-message) request, or map a human-readable event alias instead (see [Event Mapping](#event-mapping) below).

### Brand Config

Brands are enabled by default, so every new email template uses your [Default Brand](/platform/content/brands/brands-overview#customizing-brands). You can disable branding per template or assign a [Custom Brand](/platform/content/brands/brands-overview#sending-a-branded-email).

### Subscription Topic

Assign a subscription topic to group templates under a single preference. This lets end users opt in or out of a category of notifications at once rather than one template at a time.

### Message Tags

<Info>
  Message tags are behind a feature flag. Contact [Courier Support](mailto:support@courier.com) or your account team to enable them.
</Info>

Add a comma-separated list of tags to a template. These tags are automatically included in `metadata.tags` on every message sent from that template, so you can filter by tag in an [Inbox](/platform/inbox/inbox-overview) view or query them through the [Messages API](/api-reference/sent-messages/list-messages).

<Frame caption="Message Tags in Template Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/A5Xe4OlKFUkTRiqy/assets/inbox/designer-settings-message-tags.png?fit=max&auto=format&n=A5Xe4OlKFUkTRiqy&q=85&s=c328d65853b609a5f2375e0d4ca8f21a" alt="Message Tags in Template Settings" width="1908" height="1234" data-path="assets/inbox/designer-settings-message-tags.png" />
</Frame>

## Event Mapping

Map an event name to a template so you can reference it by a readable alias instead of the Notification ID. This decouples your code from specific template IDs; you can swap the underlying template without redeploying your application.

<Frame caption="Event Mapping Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/notification-settings-events.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=5480538bec3cc284947f1bd8da1a2774" alt="Event Mapping Settings" width="1912" height="1260" data-path="assets/platform/content/notification-settings-events.png" />
</Frame>

Once mapped, use the event name in the `template` field of your send request:

```json  theme={null}
{
  "message": {
    "template": "order-confirmation",
    "to": { "user_id": "user_123" },
    "data": {
      "order_id": "ORD-12345"
    }
  }
}
```

## Conditions

Use conditions to prevent a template from sending when specific criteria are met. You can reference properties from the `data` or `profile` objects provided in the [Send API](/api-reference/send/send-a-message) call or [User Profile](/api-reference/user-profiles/get-a-profile). See [Send Conditions](/platform/content/template-settings/send-conditions) for details.

## Notes

Notes let you attach internal context to a template. Once added, a note icon appears in the template list; clicking it opens a read-only preview without entering the designer.

<Frame caption="Template Notes">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/notification-settings-notes.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=f3aae7909d67b8236e60d9fcc25dec65" alt="Template Notes" width="998" height="649" data-path="assets/platform/content/notification-settings-notes.png" />
</Frame>

## Publishing & Versioning

Templates follow a publish workflow so you can iterate safely before going live:

* **Draft**: Save changes without affecting live notifications
* **Publish**: Make changes active for all new sends
* **Rollback**: Revert to any previously published version

For API-based templates using Elemental, publishing is handled through your deployment process; new versions become active when you deploy updated code.

You can view the full publish history to see who published each version and when.

<Warning>
  Rolling back overwrites any unpublished draft changes.
</Warning>

<Frame caption="Publish History">
  <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/notification-settings-history.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=f39806d9130591063088f6479c7c149a" alt="Publish History" width="953" height="677" data-path="assets/platform/content/notification-settings-history.png" />
</Frame>
