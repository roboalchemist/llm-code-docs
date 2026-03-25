# Source: https://www.courier.com/docs/platform/analytics/message-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Message Logs

> Courier Message Logs track each message's status—Queued, Sent, Delivered, Opened, Clicked—with filtering by status, provider, recipient, and timeline events. Includes inbox sync, automation logs, and error insights.

The Courier Message Logs provide a timeline and insights into the status of your notifications, recipients, lists, and automations. Each step in the send status has a visual representation.

<Frame caption="Courier Message Logs">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/analytics/logs-navbar.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=3bfe3d51ec5a36f50e32b1b3941d6ca0" alt="Courier Message Logs" width="3010" height="1636" data-path="assets/platform/analytics/logs-navbar.png" />
</Frame>

The message logs display key information in the summary view:

* The **Status** of each message send request
* The **Notification** and **Recipient** associated with each send
* The **Provider** channels for the notification

## Message Statuses

Every message in Courier progresses through a series of statuses. The following statuses are tracked:

### Delivery Statuses

| Status        | Description                                                                                                                                                |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Queued**    | Courier has received a valid Send API request and is processing the notification.                                                                          |
| **Routed**    | Channel routing is complete; the message is ready for delivery.                                                                                            |
| **Sent**      | Courier sent the request to the downstream provider. A `200` response from Courier does not guarantee delivery; the provider may still reject the message. |
| **Delivered** | The provider confirmed the message was accepted. For email, this means it reached the inbox. For SMS, not all providers return delivery confirmation.      |
| **Opened**    | The recipient opened the notification (email with open tracking enabled, or inbox/push via SDK events).                                                    |
| **Clicked**   | The recipient clicked a link in the notification (requires link tracking enabled).                                                                         |

### Processing Statuses

| Status        | Description                                                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Delayed**   | The message is scheduled for future delivery.                                                                                                  |
| **Digested**  | The message was added to a digest queue and will be sent as part of a batched notification.                                                    |
| **Filtered**  | The message was filtered out by routing rules, preferences, or send conditions.                                                                |
| **Throttled** | The message is being rate-limited due to [send limits](/platform/sending/send-limits) or workspace quota.                                      |
| **Simulated** | The message was sent with a [mock key](/platform/workspaces/environments-api-keys), simulating the lifecycle without delivery to the provider. |

### Error Statuses

| Status            | Description                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| **Undeliverable** | The provider rejected the message or delivery failed.                                          |
| **Unmapped**      | The Notification ID does not exist or the Event ID is not mapped to a notification.            |
| **Unroutable**    | No valid delivery route was found (e.g., missing recipient address or no configured channels). |
| **Canceled**      | The message delivery was canceled before being sent.                                           |

<Note>
  **Has Errors** is not a status but a filter indicator showing that the message timeline includes an error response.
</Note>

### Channel-Specific Behavior

| Event         | Email                            | Push (APNS/FCM)                   | Inbox                             | SMS                                      | Chat                       |
| ------------- | -------------------------------- | --------------------------------- | --------------------------------- | ---------------------------------------- | -------------------------- |
| **Delivered** | Provider confirms inbox delivery | Delivery Rate = 100% - Error Rate | Delivery Rate = 100% - Error Rate | Not all providers return delivery status | Provider confirms delivery |
| **Opened**    | Requires open tracking           | Not supported                     | SDK push events                   | n/a                                      | n/a                        |
| **Clicked**   | Requires link tracking           | SDK click events                  | SDK click events                  | n/a                                      | Requires link tracking     |

### Inbox and Channel Sync

Notification event states are synchronized between the [inbox](/platform/inbox/inbox-overview) and other channels within a notification template. For example, if a notification was sent with both `inbox` and `email` channels, opening the email will mark the inbox notification as `read`.

<Note>
  This sync only works one way. Reading an inbox message will not mark an email as `opened`.
</Note>

## Viewing Logs

### Histogram

The logs histogram breaks down delivery metrics for specific days, grouping events in color-coordinated graphs.

<Frame caption="Logs Histogram">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/analytics/logs-histogram.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=51c2dfcfcc1c48c307fcd0aacef19393" alt="Logs Histogram" width="2678" height="896" data-path="assets/platform/analytics/logs-histogram.png" />
</Frame>

You can drag-select within the histogram to filter to a custom date range.

<Frame caption="Drag Select View">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/analytics/logs-histogram.gif?s=c31474a2247b2378b8725fa6b89bd2f8" alt="Drag Select View" width="724" height="480" data-path="assets/platform/analytics/logs-histogram.gif" />
</Frame>

### Log Detail View

Click any notification in the list view to open the log details, which includes:

* **Summary** - Message and Recipient IDs, timestamps for each stage (Enqueued, Sent, First Delivery, etc.)
* **Timeline** - Detailed timeline of every step; click any event to view additional details

<Frame caption="Detailed View">
  <img src="https://mintcdn.com/courier-4f1f25dc/A5Xe4OlKFUkTRiqy/assets/platform/analytics/logs-detailed.png?fit=max&auto=format&n=A5Xe4OlKFUkTRiqy&q=85&s=3a2e54af2ce89afa9cdf9a7290da4be7" alt="Detailed View" width="2232" height="1476" data-path="assets/platform/analytics/logs-detailed.png" />
</Frame>

To investigate errors, click the `Error Encountered` event in the timeline to review the error message.

<Frame caption="Error Tab">
  <img src="https://mintcdn.com/courier-4f1f25dc/A5Xe4OlKFUkTRiqy/assets/platform/analytics/logs-error.png?fit=max&auto=format&n=A5Xe4OlKFUkTRiqy&q=85&s=fb8fb96ee55d1db464ad2e91c42e131d" alt="Error Tab" width="2232" height="1468" data-path="assets/platform/analytics/logs-error.png" />
</Frame>

## Filtering Logs

Filter your message logs to find specific notifications:

* **Date** - Filter by date range (limited by your account's [log retention](#log-retention) period)
* **Recipient** - Filter by email address or Recipient ID
* **Notification** - Filter by specific notification template
* **Status** - Filter by one or more statuses: Queued, Sent, Delivered, Opened, Clicked, Undeliverable, Unmapped
* **Errors** - Show only notifications with errors in their timeline
* **Provider** - Filter by one or more integrated providers

<Note>
  Unmapped means the Event ID does not [map to a notification](https://help.courier.com/en/articles/4189555-send-basics-how-notifications-are-triggered-and-sent-with-courier) or the Notification ID is invalid.
</Note>

## Rendered Content

The Courier [Messages API](/api-reference/sent-messages/get-message-content) lets you retrieve the rendered output of any notification in your send history. This is useful for debugging and verifying what was actually sent to providers.

To fetch the rendered content for a message:

1. **Fetch message history** - Use GET `/messages/:message_id/history` with the message ID from your send response. You can use the history [endpoint](/api-reference/sent-messages/get-message-history) or the `getMessageHistory` SDK function.

2. **Fetch message content** - Use the root-relative URL from the `RENDERED` event in the history response, appended to the Courier API host: `https://api.courier.com`

<Frame caption="Example of a Rendered Event">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/analytics/rendered-sample.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=61b8d667ffb61a8706b3074aa14ea6bc" alt="Example of a Rendered Event" width="1480" height="812" data-path="assets/platform/analytics/rendered-sample.png" />
</Frame>

<Frame caption="Example of a Rendered Push Event">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/analytics/rendered-content.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=bd7263a67594b98d44f17bc7f8cbefba" alt="Example of a Rendered Push Event" width="532" height="160" data-path="assets/platform/analytics/rendered-content.png" />
</Frame>

### Rendered Content for Emails

HTML content is returned with `content-type: text/html` as raw HTML:

```plaintext  theme={null}
content-type: text/html
content-length: 32015
date: Tue, 26 Oct 2021 17:10:10 GMT
x-amzn-requestid: e9d54717-3cb0-4f1e-a47a-b64317738596
access-control-allow-origin: *
strict-transport-security: max-age=31536000;includeSubDomains;preload
```

<Frame caption="Example of an Email Response">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/analytics/rendered-response.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=d64f3e88de6b5a170c7989ffaed4650b" alt="Example of an Email Response" width="619" height="938" data-path="assets/platform/analytics/rendered-response.png" />
</Frame>

## Log Retention

Courier retains message logs for different periods depending on your account type:

* **Free and Pro accounts**: Logs are retained for **30 days**
* **Contracted accounts**: Logs are retained for **1 year**

The Log date filter in the Message Logs interface will only allow you to filter and view logs within your account's retention period. Logs older than the retention period are automatically deleted and cannot be recovered.

<Note>
  **Enterprise Customers**: If you need longer log retention periods, contact [Courier Support](mailto:support@courier.com) to discuss extended retention options.
</Note>

## Troubleshooting Delivery Issues

If a message shows **Sent** but the recipient hasn't received it, use the timeline in the log detail view to identify where the problem is:

1. **Check the provider response.** Click the Sent event to see the raw response. If the provider returned an error, the details will be here.
2. **Check your provider's dashboard.** Cross-reference the message ID with your provider's activity feed (SendGrid Activity, Postmark Activity, SES console, etc.) for bounce, block, or deferral events.
3. **Verify sender authentication.** Confirm that SPF, DKIM, and DMARC records are correctly configured for your sending domain.

If the message shows **Delivered** but the recipient still hasn't received it, the issue is on the recipient's side; their mail server accepted the email, but an internal filter or email security gateway may be quarantining it.

For a full walkthrough, see [How to Debug Email Delivery Issues](/tutorials/monitoring/how-to-debug-delivery-issues).

## Automation Logs

The [Automation](/platform/automations/automations-overview) logs provide detailed insights into the status of an automation run as well as step details.

### Automation Run List

<Frame caption="Automation Logs">
  <img src="https://mintcdn.com/courier-4f1f25dc/A5Xe4OlKFUkTRiqy/assets/platform/analytics/logs-automation.png?fit=max&auto=format&n=A5Xe4OlKFUkTRiqy&q=85&s=100ddba66aee7f2463b81f83afd68440" alt="Automation Logs" width="3022" height="1278" data-path="assets/platform/analytics/logs-automation.png" />
</Frame>

Clicking into one of the automation in log opens the run summary, providing details on each of the steps in the automation.

<Frame caption="Automation Run Summary">
  <img src="https://mintcdn.com/courier-4f1f25dc/A5Xe4OlKFUkTRiqy/assets/platform/analytics/logs-detailed-automation.png?fit=max&auto=format&n=A5Xe4OlKFUkTRiqy&q=85&s=22250349eead568481ae8d31d2ec35ff" alt="Automation Run Summary" width="2088" height="1312" data-path="assets/platform/analytics/logs-detailed-automation.png" />
</Frame>
