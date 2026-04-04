# Source: https://www.courier.com/docs/platform/sending/digest-send.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send a Message Digest

Digest Send allows you to automatically aggregate multiple individual notifications into a single scheduled digest message. Instead of sending users multiple separate notifications throughout the day, Courier can collect these messages and deliver them as a summarized digest at user-preferred times.

## Key Concepts

### How Digest Send Works

1. **Individual sends**: Your application sends notifications normally using the Send API
2. **Automatic aggregation**: Messages are collected instead of sent immediately when users have digest preferences
3. **Scheduled delivery**: Collected messages are sent as a single digest template at the scheduled time
4. **User control**: Users can choose between instant delivery or digest schedules through preference centers

### When to Use Digest Send

* **High-frequency notifications**: System alerts, activity updates, task assignments
* **Regular updates**: Daily summaries, weekly reports, performance metrics
* **User preference compliance**: Let users control notification frequency
* **Reduced notification fatigue**: Consolidate related messages

<Info>
  **Digest Send vs. Automations**: Use Digest Send for simple aggregation scenarios. For complex logic, conditional routing, or dynamic data fetching, consider [Automation Digests](/platform/automations/digest) instead.
</Info>

## Configuration

### Step 1: Set Up Subscription Topic

Configure digest settings in the [Preferences Editor](https://app.courier.com/settings/preferences):

1. Create a new subscription topic or edit an existing one
2. This topic will group related notifications that can be digested together

### Step 2: Link Individual Templates

Connect the individual notification templates that should be aggregated:

* **Example**: For project updates, link templates for "task-assigned", "comment-added", "status-changed"
* **Purpose**: These templates represent individual notifications that will be collected
* **Behavior**: When users have digest preferences, these individual sends are aggregated instead of sent immediately

### Step 3: Create Digest Template

Design a template that displays the aggregated notifications:

* **Template content**: Should handle multiple events (tasks, comments, status updates, etc.)
* **Data structure**: Receives categorized events with counts and individual items
* **Design considerations**: Show summaries, recent examples, and aggregate counts

### Step 4: Link Digest Template

In the Subscription Topic's Digest Settings:

1. Select your digest template as the "Linked Digest Template"
2. This enables the digest functionality for this topic
3. Users with digest schedules will receive this template instead of individual notifications

<Info>
  **Template Behavior**: Removing the Linked Digest Template disables digest sending. Individual messages will be sent immediately to users who selected digest preferences until a new digest template is linked.
</Info>

### Step 5: Configure Schedules

Set up when digests should be delivered to users:

* **Required**: At least one schedule must be configured
* **Recommendation**: Include an "Instant" schedule as default to allow opt-out from digests
* **User choice**: Multiple schedules appear as options in preference centers
* **Timezone**: Schedules use local timezone for both configuration and user display

<Frame caption="Digest Schedules">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digest-schedules.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=57f4542eb127423fe8a997edfe4093cd" alt="Digest Schedules" width="2114" height="1348" data-path="assets/platform/automations/digest-schedules.png" />
</Frame>

**Common schedule examples:**

* Instant (immediate delivery)
* Daily at 9:00 AM
* Weekly on Monday at 8:00 AM
* Monthly on the 1st at 10:00 AM

### Step 6: Set Up Categories (Optional)

Categories organize different types of events within the same digest:

<Frame caption="Digest Categories">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digest-categories.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=bf111749846a4a90280e459bca85e231" alt="Digest Categories" width="2118" height="1350" data-path="assets/platform/automations/digest-categories.png" />
</Frame>

**Category Configuration:**

* **Purpose**: Separate different event types (tasks vs. comments vs. status updates)
* **Retain settings**: Control which events are included in the final digest
* **Sort options**: Order events by custom data attributes

**Retain Options:**

* **First 10**: First events received during the digest period
* **Last 10**: Most recent events received
* **10 Highest**: Top events sorted by a data attribute (requires `sort_key`)
* **10 Lowest**: Bottom events sorted by a data attribute (requires `sort_key`)

**Data Structure**: Each category appears in the digest template as:

```json  theme={null}
{
  "category_name": {
    "count": 25,
    "items": [
      // Up to 10 individual events based on retain setting
    ]
  }
}
```

### Step 7: Configure Settings

Optional settings for digest behavior:

<Frame caption="Digest Settings">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digest-settings.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=06ef8cef51baef8e53acf79a535e4688" alt="Digest Settings" width="2114" height="1344" data-path="assets/platform/automations/digest-settings.png" />
</Frame>

**Send Empty Digests**: Toggle to send digests even when no events occurred during the schedule window. Useful for:

* Consistent digest delivery schedules
* Including external data fetched in automation templates
* Maintaining user engagement with regular touchpoints

## Implementation

### Example Setup

This example demonstrates setting up digests for project notifications with templates `task-assigned`, `comment-added`, and `project_digest`:

### Send Individual Notifications

Continue sending individual notifications normally. Courier automatically handles aggregation based on user preferences:

**Task assignment notification:**

```json  theme={null}
{
  "message": {
    "to": { "user_id": "user1" },
    "template": "task-assigned",
    "data": {
      "project_name": "Q4 Marketing Campaign",
      "task_title": "Review landing page copy",
      "assignee_name": "Jane Smith"
    }
  }
}
```

**Comment notification:**

```json  theme={null}
{
  "message": {
    "to": { "user_id": "user1" },
    "template": "comment-added", 
    "data": {
      "project_name": "Q4 Marketing Campaign",
      "commenter_name": "Bob Johnson",
      "comment_text": "Looks great, ready for review"
    }
  }
}
```

### Testing Digest Behavior

1. **Set up templates**: Link `task-assigned` and `comment-added` templates to your subscription topic
2. **Configure digest**: Set `project_digest` as the linked digest template
3. **Create schedules**: Add "Instant" (default) and "Daily at 9 AM" options
4. **Test instant delivery**: Send notifications and verify immediate delivery in logs
5. **Switch to digest**: Change user preference from "Instant" to "Daily at 9 AM"
6. **Verify aggregation**: Send notifications and see `DIGESTED` status in logs
7. **Confirm delivery**: Wait for scheduled time and verify digest template delivery

## Digest Send vs. Automations

**Digest Send** is ideal for straightforward aggregation scenarios where you want to collect similar notifications and deliver them on user-preferred schedules. It requires minimal configuration and works automatically with your existing Send API calls.

**[Automation Digests](/platform/automations/digest)** provide additional capabilities when you need dynamic data fetching, complex conditional logic, or custom data processing. For example, if you need to fetch up-to-date profile information at digest delivery time or route to different templates based on the aggregated content, automations are the better choice.

Most digest use cases can be handled effectively with Digest Send, particularly for project updates, system alerts, and performance reports where the goal is simple aggregation and user preference control.

## Monitoring

### Message Status

The **`DIGESTED`** status appears in message logs when:

* User has a non-instant schedule selected for the subscription topic
* Linked Digest Template is configured
* Individual notification is aggregated instead of sent immediately

### Digest Delivery Logs

When digests are sent according to schedule:

* New message log entry shows the Linked Digest Template
* Log includes all collected items associated with the digest
* Individual aggregated messages maintain `DIGESTED` status for tracking

## Related Resources

<CardGroup cols={2}>
  <Card title="Automation Digests" href="/platform/automations/digest" icon="robot">
    Extended digest creation with custom logic and data fetching
  </Card>

  <Card title="Preferences Overview" href="/platform/preferences/preferences-overview" icon="user-gear">
    Learn how users control their notification preferences
  </Card>

  <Card title="Message Logs" href="/platform/analytics/message-logs" icon="chart-line">
    Monitor digest aggregation and delivery in your logs
  </Card>

  <Card title="Subscription Topics" href="/platform/preferences/preferences-overview" icon="tags">
    Understand how to organize notifications with subscription topics
  </Card>
</CardGroup>
