# Source: https://documentation.onesignal.com/docs/en/goals.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Goals

> Define a success metric and target value on any message or Journey, then track progress on the delivery report.

Use Goals to measure the impact of your messages and Journeys against specific targets. Set a metric and threshold before sending, then monitor real-time progress on the delivery report to understand what's working.

<Note>
  Goals are currently in **Beta** and available in early access to all plans. Functionality may change before general availability.
</Note>

## What Goals track

When you set a Goal, you choose a metric (such as clicks or delivered), decide whether to measure it as a **rate** or **count**, and set a target value. After the message sends, the delivery report displays a banner showing real-time progress toward the target.

Goals are available on:

* Push notifications
* Email messages
* SMS messages
* In-app messages
* Journeys

## Set a Goal on a message

You can add a Goal during message creation in the dashboard. The Goal step appears in the message composer after you configure your audience and content.

<Steps>
  <Step title="Enable the Goal">
    Check **Set a Message Goal** to enable the Goal step.
  </Step>

  <Step title="Name your Goal">
    Enter a **Goal name** and optional **description** to identify the Goal on your delivery report.
  </Step>

  <Step title="Choose a metric">
    Select a **metric** to track (for example, Clicked or Delivered).
  </Step>

  <Step title="Select the measurement type">
    Toggle between **Rate** (percentage) or **Count** (absolute number).
  </Step>

  <Step title="Set the target value">
    Enter the **target value** — this is the threshold that defines success.
  </Step>
</Steps>

<Frame caption="Setting a Goal on a push notification in the message composer.">
  <img src="https://mintcdn.com/onesignal/lsATV3cjw65zIoFr/images/goals/goal-setup-push.png?fit=max&auto=format&n=lsATV3cjw65zIoFr&q=85&s=0c28d5e3f840f4fce2f730c61f7d6d44" alt="Message Goal step in the push notification composer showing the goal name Click Through Rate, CTR metric selected, Rate toggle selected, and a target percentage of 7 percent." width="2688" height="1190" data-path="images/goals/goal-setup-push.png" />
</Frame>

<Tip>
  A Goal locks after you send the message. You cannot edit the metric, type, or target value after send.
</Tip>

## Track a Goal on a delivery report

When a message has a Goal, a banner appears at the top of its delivery report showing:

* The Goal name and description
* The selected metric and target value
* Current progress toward the target

<Frame caption="Goal progress banner on an email delivery report.">
  <img src="https://mintcdn.com/onesignal/lsATV3cjw65zIoFr/images/goals/goal-banner-delivery-report.png?fit=max&auto=format&n=lsATV3cjw65zIoFr&q=85&s=83477fb86c4e866d31124165173127f4" alt="Email delivery report with a Goal banner showing an email goal set for more than 50 Unique Opens with current progress at 0." width="2686" height="1200" data-path="images/goals/goal-banner-delivery-report.png" />
</Frame>

## Goals on Journeys

You can also set Goals on Journeys to measure whether a multi-step flow meets your success criteria. Journey Goals work the same way — you define a metric and target, then track progress on the Journey analytics page.

<Card title="Journey Goals" icon="route" href="./journeys-settings">
  Learn how to set and track Goals on Journeys.
</Card>

## Conversion metrics (coming soon)

Support for conversion-based metrics in Goals is on the way. While you wait, learn how conversion metrics work today.

<Card title="Conversion metrics" icon="chart-line" href="./conversion-metrics">
  Track purchases, sign-ups, and other downstream actions.
</Card>

## FAQ

**Can I edit a Goal after sending a message?**
No. Goals lock when the message sends. If you need a different metric or target, create a new message with an updated Goal.

**Why don't I see the Goal banner on my delivery report?**
The Goal banner only appears if a Goal was set before the message was sent. Goals cannot be added retroactively to existing messages.

**Which metrics are available for Goals?**
Available metrics depend on the channel. Common options include Clicked and Delivered. The metric picker in the Goal step shows only metrics supported by the selected channel.

**Do Goals affect message delivery or targeting?**
No. Goals are purely for measurement. They do not change how or to whom a message is delivered.

Built with [Mintlify](https://mintlify.com).
