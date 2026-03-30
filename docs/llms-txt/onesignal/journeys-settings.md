# Source: https://documentation.onesignal.com/docs/en/journeys-settings.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Journey settings

> Configure your Journey including who enters, exits, re-enters, and when it starts or stops.

Your Journey Settings define how users interact with your Journey.

## Naming and describing your Journey

When you click **Create Journey**, a modal appears (only once per new Journey) prompting you to:

* Enter a **Journey Name** (required)
* Enter a **Description** (optional)

**Validation rules:**

* Journey name is required.
* Name maximum length: **300 characters**
* Description maximum length: **255 characters**

Click **Continue** to save the Journey and open the Settings panel.

If you click **Cancel**, the Journey will be created using the default auto-generated name (for example, `New Journey 2026-02-18`) with an empty description.

<Note>
  The initialization modal does not appear when duplicating a Journey or creating one from a template.
</Note>

### Editing name and description

After creation, the **Journey Name** and **Description** appear at the top of the page and can be edited inline. The description field supports multi-line text.

Start by giving your Journey a name and description that clearly communicates its purpose to your team. Common examples include:

* Abandoned Cart
* Welcome Campaign
* Inactive User Reach Out

<Frame caption="Journey Settings">
  <img src="https://mintcdn.com/onesignal/h5D53ACj6-juR4cp/images/journeys/journeys-settings.png?fit=max&auto=format&n=h5D53ACj6-juR4cp&q=85&s=0fad19d7b60992e5e3fb425f2a833ca1" alt="Journey Settings screen" width="1550" height="822" data-path="images/journeys/journeys-settings.png" />
</Frame>

<Accordion title="Goals (Alpha)" description="Set success metrics for Journeys and supported message steps to measure performance over time.">
  <Note>
    **Alpha feature:** Journey and Message Goals are currently in **alpha**.\
    To become part of the alpha program, contact **[support@onesignal.com](mailto:support@onesignal.com)**.
  </Note>

  Goals help you measure whether your Journey or a specific message inside it is performing the way you expect.

  A goal is a metric threshold like “more than 1 user entered the Journey” or “CTR is greater than 20%”—that OneSignal continuously evaluates as your Journey runs.

  You can configure goals in two places:

* **Journey Goal** (overall Journey performance)
* **Message Goal** (for individual message action steps that support goals)

  Goals are not currently supported for Journey action steps.

### Journey Goal

  A Journey Goal tracks a single success metric for the entire Journey, for example whether users are entering, exit, or complete it.

  <Frame caption="Journey Goal in Journey Settings">
    <img src="https://mintcdn.com/onesignal/xo_UEAi3ihwfgC3h/images/journeys/journeys-goal-settings.png?fit=max&auto=format&n=xo_UEAi3ihwfgC3h&q=85&s=a8ffcba1aebaf857db2e2568c2600523" alt="Journey Settings with a Journey Goal configured" width="1800" height="1288" data-path="images/journeys/journeys-goal-settings.png" />
  </Frame>

  To set a Journey Goal:

  1. Open your Journey and click **Settings**.
  2. Select **Goals**.
  3. Enable **Set a Journey Goal**.
  4. Enter a **Name** (required) and optional **Description**.
  5. Choose a **Metric** and condition, then set the **Value** threshold.
  6. Click **Save**.

  Once configured, your Journey Goal appears at the top of the Journey report with its current value.

  <Frame caption="Journey Goal shown in the Journey report">
    <img src="https://mintcdn.com/onesignal/Z8vWzTvDAwha39jH/images/journeys/journeys-goal-report.png?fit=max&auto=format&n=Z8vWzTvDAwha39jH&q=85&s=95862d0201305e5fbac450bb8b17643b" alt="Journey report showing the Journey Goal and current progress" width="2510" height="1390" data-path="images/journeys/journeys-goal-report.png" />
  </Frame>

#### Journey Goal metrics

  Journey Goals support Journey level engagement metrics such as:

* **Entered Journey** (users who started the Journey)
* **Completed** (users who reached the end)
* **Exited Early** (users who left due to exit rules)

  Use Journey Goals when you want a quick health check like:

* “Did at least 100 users enter this Journey?”
* “Are most users completing it?”
* “Are too many users exiting early?”

  ***

### Message Goals (Push + other supported message steps)

  Message steps support their own **Message Goal**, which measures performance for that specific message. For example, a Push Notification step can track CTR, confirmations, or clicks.

  <Frame caption="Message Goal configuration inside a Push Notification step">
    <img src="https://mintcdn.com/onesignal/xo_UEAi3ihwfgC3h/images/journeys/journeys-message-goal.png?fit=max&auto=format&n=xo_UEAi3ihwfgC3h&q=85&s=2a29219ac096763d12bf7f12ec36c7a7" alt="Push step settings showing Message Goal configuration" width="1866" height="1604" data-path="images/journeys/journeys-message-goal.png" />
  </Frame>

  To set a Message Goal:

  1. Click the message action step in your Journey (for example, **Push Notification**).
  2. In editor, enable **Set a Push Goal** (or equivalent goal toggle).
  3. Enter a **Name** and optional **Description**.
  4. Select a **Metric**, condition, and **Value**.
  5. Click **Save**.

  When the message is sent, the goal appears in the message-level report so you can monitor whether that message is meeting your benchmark.

  <Frame caption="Message goal displayed in the message report">
    <img src="https://mintcdn.com/onesignal/xo_UEAi3ihwfgC3h/images/journeys/journeys-message-goal-report.png?fit=max&auto=format&n=xo_UEAi3ihwfgC3h&q=85&s=2b278a606f917b9105a1b152b4d6719c" alt="Message report showing goal status and delivery metrics" width="2498" height="1660" data-path="images/journeys/journeys-message-goal-report.png" />
  </Frame>

#### Message Goal metrics (Push)

  Push goals support delivery and engagement metrics such as:

* **Sent**
* **Delivered**
* **Confirmed**
* **Clicked**
* **CTR**
* **Failed**
* **Unsubscribed**
* **Capped**

  Some metrics may allow you to track either:

* **Rate** (percentage-based), like CTR
* **Count** (total number), like clicks
</Accordion>

## Entry rules

Entry rules define how users can enter your Journey based on their segment membership or custom events.

* You cannot use both Segments and Custom Events for Journey entry rules. However, you can use Custom Events to continue users through a Journey via the [Wait until step](./journeys-actions#wait-until).
* Once a Journey is set live, you cannot change the entry rules from Segments to Custom Events and vice versa. You will need to stop & archive the Journey, duplicate it, and start a new Journey.

<Frame caption="Entry rules for a Journey">
  <img src="https://mintcdn.com/onesignal/h5D53ACj6-juR4cp/images/journeys/journeys-entry-rules.png?fit=max&auto=format&n=h5D53ACj6-juR4cp&q=85&s=d86f2e5b9089c044511a12a9b4663e72" alt="Segment-based Journey entry rule configuration" width="1782" height="1268" data-path="images/journeys/journeys-entry-rules.png" />
</Frame>

### Audience segment

Use **Include Segment** and **Exclude Segment** to control who qualifies for your Journey.

Segment checks are done at the Subscription-level and consider all of a user's Subscriptions. If a user is qualified to enter the Journey but also fits the [Exit Rules](#exit-rules), they will enter the first step of the Journey before exiting.

If a Journey is active, the segments used in its entry rules cannot be edited. To modify them, archive the Journey or remove the segment from the entry rules first.

#### How inclusion and exclusion logic works

* ✅ If **any Subscription** is in an **Included Segment(s)** → the user enters the Journey.
* ❌ If **any Subscription** is in an **Excluded Segment(s)** → the user is blocked entirely.

<Warning>
  Journeys evaluate audience qualification using all of a user's Subscriptions. To avoid unexpected behavior, always define both **Included** and **Excluded** Segments explicitly.

  **Example:**
  You're targeting users inactive for 60+ hours (`last_session > 60hrs`).

* **Include**: Segment where `last_session > 60hrs`
* **Exclude**: Segment where `last_session ≤ 60hrs`
    This prevents users with one inactive and one active Subscription from mistakenly qualifying.
</Warning>

#### Future additions only

Segments are dynamic and have users entering and exiting them constantly. Checking this option means **any user currently in the included or excluded segment at the time the Journey is set live will never enter the Journey**. Even if the user leaves the segment and enters again, they will never enter the Journey.

This is ideal for one-time onboarding campaigns where users should not re-enter after completing the Journey once.

<Warning>
  Once a Journey with "Future additions only" is set live, the included and excluded segments are locked and cannot be edited. If you need to change the target audience, you must **duplicate the Journey**, edit the included and/or excluded segments, and launch the new Journey.
</Warning>

### Custom events

Define which specific users should enter the Journey based on [Custom Events](./custom-events). Users that satisfy the entry rule requirements can be added to the Journey more than once at the same time.

When a Custom Event name and optional properties match the entry rules, the user enters the Journey and that event is stored. The stored event may be [referenced in Liquid Syntax](./message-personalization#custom-events) and used for [Event Matching](./journeys-actions#event-matching). If you enter the user into the Journey multiple times, each entry can have unique properties based on the data you pass in the Custom Event payload.

* **Custom Event Name:** Enter the Event Name that you plan to send via API.
* **Filter by property:** Add any additional properties that you’d like to reference to filter who enters the Journey.

<Frame caption="Custom event entry rule requires the sign_up event to include the property plan is trial">
  <img src="https://mintcdn.com/onesignal/h5D53ACj6-juR4cp/images/journeys/journeys-custom-event-properties.png?fit=max&auto=format&n=h5D53ACj6-juR4cp&q=85&s=bc6a4296f783fd5714e0e7479ef911e6" alt="Journey custom event property filters" width="1782" height="1014" data-path="images/journeys/journeys-custom-event-properties.png" />
</Frame>

Custom events can also be used for:

* [Exit rules](#exit-when-custom-event-condition-occurs)
* [Wait Until steps](./journeys-actions#wait-until)
* [Personalization](./message-personalization)

***

## Exit rules

Exit rules define when users automatically leave the Journey. They may re-enter later based on your re-entry settings.

<Warning>
  If a user matches the entry rules and exit rules, then they will enter the Journey and complete the first step before exiting. You can prevent this by either:

* Use a **Wait step** as the first step of the Journey.
* Update the Excluded Segments of the Entry rules to specify exactly which users should not enter the Journey. See above [Entry rules > Audience segment](#audience-segment) for more details.
</Warning>

<Frame caption="Journey exit rules">
  <img src="https://mintcdn.com/onesignal/h5D53ACj6-juR4cp/images/journeys/journeys-exit-rules.png?fit=max&auto=format&n=h5D53ACj6-juR4cp&q=85&s=bd78087cb77df60d055fdac31c417aee" width="1780" height="1200" data-path="images/journeys/journeys-exit-rules.png" />
</Frame>

### Exit when user becomes active in your app/website

As soon as the user returns to your app or website with the OneSignal SDK, their "last session" updates making them *active* again. Therefore, they exit the Journey.

Useful for re-engagement or reactivation Journeys.

### Exit when custom event condition occurs

Send a [Custom Event](./custom-events) to exit the user from the Journey immediately.

### Exit when user no longer matches the audience conditions

Automatically remove users if they stop matching the original entry rule audience segments.

### Exit when a user enters a segment

If a user enters a selected segment at any point, they are removed from the Journey and stop receiving messages.

#### Tag users when they exit early

Apply or remove a tag when users exit early.

* Leave the value blank to remove an existing tag.
* If the app is at the tag limit, no tag will be applied.

**Common use cases:**

* **Trigger another Journey:**
  Tag users (e.g. `exited-journey-1:true`), then use that tag to define a segment for your next Journey.

* **Limit concurrent Journeys:**
  Tag users when they enter (`in-journey:true`), and remove the tag when they finish or exit. This allows you to exclude them from other Journeys using that tag.

***

## Re-entry rules

Re-entry rules determine if—and when—users can enter the Journey again after exiting. Re-entry rules can only be configured for Journeys with Audience Segment [entry rules](#entry-rules) because re-entry is always supported for Custom Event entry rules.

<Frame caption="Journey re-entry rules.">
  <img src="https://mintcdn.com/onesignal/h5D53ACj6-juR4cp/images/journeys/journeys-re-entry-rules.png?fit=max&auto=format&n=h5D53ACj6-juR4cp&q=85&s=1a15f0b435259cf4300c8966dc33c9be" alt="Re-entry configuration for a Journey" width="1786" height="748" data-path="images/journeys/journeys-re-entry-rules.png" />
</Frame>

Use this for recurring campaigns e.g. cart abandonment, inactivity-based campaigns, etc.

<Warning>
  When editing a Journey's re-entry rules:

* Re-entry settings only apply to users who exit **after** the rules are updated.
* Earlier exits follow the original re-entry configuration.
</Warning>

***

## Schedule

Set when the Journey should start and end.

* Start the Journey immediately or at some point in the future.
  * The Journey will appear as **Scheduled** in the dashboard until the start time.
  * It automatically becomes **Active** at the configured start time.
* Allow the Journey to run indefinitely until you stop it or set a future end time.
  * If end date set, the Journey will be **Stopped and Archived** automatically once the end time is reached.
  * All messages immediately stop for users currently in the Journey.
  * These users will **not** trigger exit or early exit events.

### Let current users finish the Journey

To stop new users from entering but let current ones finish:

1. Update the Entry Rules Audience Segment to only **include** an empty segment (e.g. a [Test Users](./find-set-test-subscriptions) segment).
2. Update the Exit Rules to **Uncheck** "Exit when a user no longer matches the audience conditions".

This ensures existing users continue through to the end.

<Warning>
  If your account has reached its Journey limit:

* Scheduled Journeys will **not** launch.
* The most recent scheduler will be notified.

  To resolve, archive an active Journey, then try again.
</Warning>

***

Built with [Mintlify](https://mintlify.com).
