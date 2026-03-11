# Source: https://www.courier.com/docs/platform/automations/digest.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Automation Digests

> Aggregate user events into scheduled notifications using Courier's digest system. Configure schedules, categories, and retention policies in the Preferences Editor.

Courier Automations can create recurring user digests on configured intervals. This is useful for weekly reports, activity summaries, or any periodic notification where you want to aggregate events.

<Warning>
  Automation digests require **two separate automations**: one to collect events (with an "Add to Digest" node) and one to release the digest (with a "Digest" trigger). Events won't be delivered if either automation is missing. See [Working with Digests in Automations](#working-with-digests-in-automations) for setup details.
</Warning>

<Note>
  For simpler use cases, Courier offers a [digest feature in the Send API](/platform/sending/digest-send) that doesn't require automations.
</Note>

## Configure Digests in the Preferences Editor

Configure a digest with at least one schedule in the [Preferences Editor](https://app.courier.com/settings/preferences). Create a new subscription topic or open an existing one's settings.

### Schedule a Digest

In the digest section, click **Schedules** to define when the digest releases. At least one schedule is required, but you can configure multiple to give users a choice. Multiple schedules appear as options in the hosted preferences page.

<Note>
  The date-time picker uses local timezone. Users viewing hosted preferences or using front-end preference components see times in their local timezone.
</Note>

<Frame caption="Digest Schedules">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digest-schedules.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=57f4542eb127423fe8a997edfe4093cd" alt="Digest Schedules" width="2114" height="1348" data-path="assets/platform/automations/digest-schedules.png" />
</Frame>

### Schedule ID Format

When working with digest APIs, schedule IDs use the format `sch/{uuid}`. You can find the schedule ID in the browser's network panel when viewing the Schedules section of a subscription topic - look for the `pk` field in the response.

<Note>
  The schedule ID includes the `sch/` prefix. When using this ID in API URLs, you must URL-encode the forward slash as `%2F`.
</Note>

**Examples**:

| Raw Schedule ID                            | URL-Encoded for API                          |
| ------------------------------------------ | -------------------------------------------- |
| `sch/a3726ea9-3453-465f-93ad-632061ba8f59` | `sch%2Fa3726ea9-3453-465f-93ad-632061ba8f59` |
| `sch/549ef749-7c87-4eea-b695-2e2d23c025ff` | `sch%2F549ef749-7c87-4eea-b695-2e2d23c025ff` |

### Configure Digest Categories

Categories separate different types of data within the same digest. For example, a weekly blog engagement digest might have separate categories for likes and comments.

<Frame caption="Digest Categories">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digest-categories.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=bf111749846a4a90280e459bca85e231" alt="Digest Categories" width="2118" height="1350" data-path="assets/platform/automations/digest-categories.png" />
</Frame>

Each category has a `retain` setting that controls which events are kept when the digest releases:

| Retain Option  | Description                                |
| -------------- | ------------------------------------------ |
| **First 10**   | The first 10 events received (default)     |
| **Last 10**    | The most recent 10 events                  |
| **10 Highest** | Top 10 sorted by `sort_key` (descending)   |
| **10 Lowest**  | Bottom 10 sorted by `sort_key` (ascending) |

When using **Highest** or **Lowest**, you must specify a `sort_key` (a data attribute in the event used for sorting).

When the digest releases, each category is delivered in this format:

```json  theme={null}
{
  "[category_key]": {
    "count": 15,
    "items": [...]
  }
}
```

* `count`: Total number of events received (may exceed 10)
* `items`: The retained events based on your retain setting (max 10)

### Configure Other Digest Settings

The **Invoke when empty** toggle sends digests to users in an audience even if no events were received during the schedule window. This is useful for fetching custom data in the automation and sending it regardless of event activity.

<Frame caption="Digest Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digest-settings.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=06ef8cef51baef8e53acf79a535e4688" alt="Digest Settings" width="2114" height="1344" data-path="assets/platform/automations/digest-settings.png" />
</Frame>

## Mapping a Template to a Digest

Link a notification template to the digest so all accumulated events trigger through an automation.

From the digest settings in preferences, map the notification template you want to use.

<Frame caption="Template Mapping">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digest-mapping.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=a521298f54fe8ca774b2fbefb6d7ba60" alt="Template Mapping" width="2030" height="1246" data-path="assets/platform/automations/digest-mapping.png" />
</Frame>

Then configure an automation with the appropriate trigger. For example, if digest events come from Segment:

<Frame caption="Automation Digest">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digest-automation.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=b4729bfc4c7cd4053e4e47d730ad360a" alt="Automation Digest" width="2502" height="1524" data-path="assets/platform/automations/digest-automation.png" />
</Frame>

After publishing, digested events appear in the logs until the schedule releases the digest.

<Frame caption="Digest Logs">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digest-logs.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=7c78b0d80d402d627de2ec752e07c93d" alt="Digest Logs" width="1780" height="1306" data-path="assets/platform/automations/digest-logs.png" />
</Frame>

## Working with Digests in Automations

Two automation nodes handle digest events: one to collect events, one to release them.

### Digest Event Collection

Add an **Add to Digest** node to your automation:

1. Right-click the canvas and select "Add to Digest"
2. Choose the subscription topic where you configured the digest
3. Events accumulate per user, identified by `user_id` or `userId` in the event data

<Note>
  Both `user_id` and `userId` are accepted in the event data for user identification.
</Note>

### Digest Release

Create a separate automation to process and send the compiled digest:

1. Select the trigger node and choose **Digest** from the Trigger section
2. Select the same subscription topic used for event collection
3. The automation fires at scheduled intervals, processing each user's accumulated data

<Frame caption="Automation Digest Trigger">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digest-trigger.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=a37deaaa4cbeed15e290d8b4d0bd1d5e" alt="Automation digest trigger" width="2570" height="1710" data-path="assets/platform/automations/digest-trigger.png" />
</Frame>

The digest payload arrives in this structure:

```json  theme={null}
{
  "[category_key]": {
    "count": 15,
    "items": [
      { "event": "data", "from": "first_event" },
      { "event": "data", "from": "second_event" }
    ]
  }
}
```

Use this data in your notification template to render the digest summary.

## Testing Digests

1. **Send test events** by invoking your collection automation (see [Adding Events via API](#adding-events-via-api))
2. **Verify accumulation** by [listing digest instances](#listing-digest-instances); confirm `event_count` increments and `status` is `IN_PROGRESS`
3. **Trigger a release** using the [manual trigger endpoint](#releasing-a-digest-early); check that your template receives the digest payload
4. **Verify the email** contains the expected digest items and category data

<Warning>
  Do not manually invoke digest trigger automations via the `/automations/{id}/invoke` endpoint. This bypasses the digest accumulation system and will result in empty digest data. Always use the `/digests/schedules/{id}/trigger` endpoint or wait for the scheduled release.
</Warning>

## Timing Considerations

### List Subscriptions and Digest Events

If your automation subscribes a user to a list and then immediately sends a digest event, the subscription may not have propagated before the event is processed. This can cause the event to be dropped because the user isn't yet recognized as a subscriber for the topic.

To avoid this race condition:

* Add a short delay (a few seconds) between the subscription call and the first digest event
* Or subscribe users to lists as a separate, earlier step in your workflow rather than inline with digest event submission

### Scheduled vs Instant Delivery

Scheduled digests batch events until the next scheduled release time. If you send a digest event at 9:05 AM and the schedule is "Daily at 9:00 AM," that event won't be delivered until the following day at 9:00 AM. This is expected behavior; the event is accumulating in a new digest instance.

To test digests without waiting for the schedule, use the [manual trigger endpoint](#manually-triggering-a-digest-release) or add a shorter schedule (every 5-15 minutes) during development.

## Managing Digests via API

If the Preferences Editor UI is unavailable or you need programmatic control over digest schedules, you can manage digests through the API.

### Listing Digest Instances

Check which users have accumulated events for a given schedule:

```bash  theme={null}
curl -X GET "https://api.courier.com/digests/schedules/sch%2F{uuid}/instances" \
  -H "Authorization: Bearer $COURIER_AUTH_TOKEN"
```

Each instance in the response includes `event_count`, `status` (`IN_PROGRESS` or `CLOSED`), and the `user_id`.

### Releasing a Digest Early

Trigger an immediate release without waiting for the scheduled time:

```bash  theme={null}
curl -X POST "https://api.courier.com/digests/schedules/sch%2F{uuid}/trigger" \
  -H "Authorization: Bearer $COURIER_AUTH_TOKEN"
```

This closes all `IN_PROGRESS` instances for the schedule and invokes the digest trigger automation for each user.

### Adding Events via API

You can submit digest events by invoking the collection automation directly:

```bash  theme={null}
curl -X POST "https://api.courier.com/automations/{collector-automation-id}/invoke" \
  -H "Authorization: Bearer $COURIER_AUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "user_id": "user-123",
      "title": "New comment on your post",
      "body": "Alice replied to your thread"
    }
  }'
```

<Note>
  Use the collection automation's ID (the one with the "Add to Digest" node), not the trigger automation's ID. Invoking the trigger automation directly bypasses the digest system and produces empty results.
</Note>
