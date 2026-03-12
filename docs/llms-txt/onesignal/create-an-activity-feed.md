# Source: https://documentation.onesignal.com/docs/en/create-an-activity-feed.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create activity feed

> Learn how to build an in-app activity feed using OneSignal's REST API, Event Streams, or on-device logic to track and display user notification history.

## What is an activity feed?

An activity feed lets users see the history of notifications they've received within your app.

OneSignal focuses on delivering notifications but does not currently store the history of messages sent to each individual user. To build this functionality, you'll need to store notification data yourself—either on your backend server or directly on the user’s device.

<Tabs>
  <Tab title="Option 1">
    ## Saving to server

    **Recommended Approach**

    Rather than relying on background processing in your app, use the [Create notification](/reference/create-message) REST API to send each notification and also store a copy on your server. Then, when the app launches, it can check the server for updates.

    Once the data is stored, you can retrieve and display the user’s notification history at any time.
  </Tab>

  <Tab title="Option 2">
    ## Create an activity feed using OneSignal Event Streams

    OneSignal’s [Event Streams](./event-streams) feature provides a scalable way to stream real-time events from your app to your backend systems or data warehouse. This lets you build a feed that reflects in-app user behavior—like follows, comments, purchases, or notification events—without manually updating the feed within your app.

    ### How it works

    Event Streams exports live event data including:

    * Notification deliveries
    * Email/SMS opens and clicks
    * User-triggered actions

    Destinations include:

    * Webhooks (your HTTP endpoints)
    * Amazon Kinesis
    * Amazon S3
    * Google Cloud Storage
    * BigQuery
    * And more

    Your system receives these events as they occur and can use them to update a feed UI or analytics pipeline.

    ## Steps to set up an Activity Feed with Event Streams

    <Steps>
      <Step title="Enable Event Streams">
        * Go to the **OneSignal Dashboard** > **Settings** > **Event Streams**.
        * Choose a destination such as a Webhook or data pipeline (e.g., Amazon Kinesis).
        * Select the events you want to stream (e.g., `message.sent`, `message.delivered`, `message.clicked`).
      </Step>

      <Step title="Configure your backend to handle event data">
        * Create a webhook or consumer that ingests event data.
        * Parse the event payload to extract relevant fields like:

          * `external_id` (the user ID)
          * `event` type (`message.delivered`, etc.)
          * `timestamp`
          * `contents` (notification message)
          * `additional_data` (any custom metadata)
      </Step>

      <Step title="Store and structure Activity Feed entries">
        * Save these events to your database in a format suitable for querying and rendering.

        ```json  theme={null}
        {
          "message.id": "f3c9cd09-10d7-4f59-b9bc-66e16607f1d5",
          "message.name": "the-name-you-set",
          "message.title": "Claim 50% Off Today", // email subject example
          "message.title": "{'en':'the message title/headings'}", // push title example
          "message.contents": "{'en':'the message content'}",
          "message.template_id": "the-template-uuid-if-set",
          "message.url": "the-message-url",
          "message.app_url": "the-message-app-url",
          "message.web_url": "the-message-web-url"
        }
        ```
      </Step>

      <Step title="Render the feed in your app">
        * Build a frontend component (e.g., React, SwiftUI, or Android View) to query and display recent events for the logged-in user.
        * Optionally include filters or grouping by event type.
      </Step>

      <Step title="Enhance with additional metadata">
        * When sending notifications, include `additional_data` to provide feed context, for example:

          ```json  theme={null}
          {
            "action": "commented",
            "post_id": "xyz123"
          }
          ```

        * This allows you to create rich feed entries such as “Jane commented on your post.”
      </Step>
    </Steps>

    ### Example use cases

    * **E-commerce**: Show order confirmations, shipping updates, and promotions.
    * **Social Apps**: Show likes, comments, follows.
    * **SaaS Platforms**: Track task assignments, mentions, or activity logs.

    ### Benefits

    * Real-time updates via event streaming
    * Fully customizable logic and display
    * Scalable, backend-driven architecture
  </Tab>
</Tabs>

***

Built with [Mintlify](https://mintlify.com).
