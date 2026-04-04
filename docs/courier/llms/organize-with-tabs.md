# Source: https://www.courier.com/docs/platform/inbox/organize-with-tabs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organize Messages with Tabs

> Create tabbed views so users can quickly find the messages that matter.

In **Courier Inbox**, **tabs** are the primary way to organize and filter **in-app notifications**.

<Frame caption="CourierInbox with many tabs">
    <img src="https://mintcdn.com/courier-4f1f25dc/gpcirRSrjdoqq8DR/platform/inbox/assets/courier-react-tabs-cropped.png?fit=max&auto=format&n=gpcirRSrjdoqq8DR&q=85&s=a26a485893e3eb2d8361e6f748e56819" alt="Preview of CourierInbox with tabs" width="1320" height="515" data-path="platform/inbox/assets/courier-react-tabs-cropped.png" />
</Frame>

A **tab** is a filtered view of notifications. Tabs apply a `filter` object to determine which notifications appear in the list.

Each tab can filter notifications using a `filter` object. You can use one or more of the following filters:

* `tags` to show specific notification types. These are defined by you.

* `status` to filter by read/unread

* `archived` to include archived notifications

* A **feed** is a top-level container in the inbox header that groups related tabs together.

Most apps only need **one feed** (so the feed selector is hidden), but you can define **multiple feeds** if you want separate top-level categories of notifications.

You can learn more about tabs and feeds in our [Inbox documentation](/sdk-libraries/courier-react-web#tabs-and-feeds).

## Example

Define tabs inside a `feeds` array. Each tab has a `datasetId` (unique identifier), `title` (display name), and `filter` object.

<CodeGroup>
  ```jsx React theme={null}
  <CourierInbox
    feeds={[
      {
        feedId: "notifications",
        title: "Notifications",
        tabs: [
          { datasetId: "all", title: "All", filter: {} },
          { datasetId: "unread", title: "Unread", filter: { status: "unread" } },
          { datasetId: "orders", title: "Orders", filter: { tags: ["order"] } },
          { datasetId: "alerts", title: "Alerts", filter: { tags: ["alert"] } },
        ],
      },
    ]}
  />
  ```

  ```html Web Components theme={null}
  <courier-inbox id="inbox"></courier-inbox>

  <script type="module">
    const inbox = document.getElementById("inbox");
    inbox.setFeeds([
      {
        feedId: "notifications",
        title: "Notifications",
        tabs: [
          { datasetId: "all", title: "All", filter: {} },
          { datasetId: "unread", title: "Unread", filter: { status: "unread" } },
          { datasetId: "orders", title: "Orders", filter: { tags: ["order"] } },
          { datasetId: "alerts", title: "Alerts", filter: { tags: ["alert"] } },
        ],
      },
    ]);
  </script>
  ```
</CodeGroup>

Tags are set when you send a message using `metadata.tags`:

```json  theme={null}
{
  "message": {
    "to": { "user_id": "user_123" },
    "template": "order-shipped",
    "metadata": {
      "tags": ["order"]
    }
  }
}
```

## Related Resources

<CardGroup cols={2}>
  <Card title="Get Started with Inbox" href="/platform/inbox/inbox-overview" icon="inbox">
    Set up Courier Inbox in your app
  </Card>

  <Card title="React SDK" href="/sdk-libraries/courier-react-web" icon="react">
    Full tabs and feeds reference for React
  </Card>
</CardGroup>
