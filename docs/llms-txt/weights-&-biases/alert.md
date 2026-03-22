# Source: https://docs.wandb.ai/models/runs/alert.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Send alerts, triggered from your Python code, to your Slack or email

# Send an alert

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://wandb.me/alerts-colab" />

Create alerts with Slack or email if your run crashes or with a custom trigger. For example, you can create an alert if the gradient of your training loop starts to blow up (reports NaN) or a step in your ML pipeline completes. Alerts apply to all projects where you initialize runs, including both personal and team projects.

And then see W\&B Alerts messages in Slack (or your email):

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/_OEDykSS2PIumrEw/images/track/send_alerts_slack.png?fit=max&auto=format&n=_OEDykSS2PIumrEw&q=85&s=a3ebc3dccaa85a8c8df635f9eca20101" alt="Slack alert setup" width="567" height="331" data-path="images/track/send_alerts_slack.png" />
</Frame>

<Note>
  W\&B Alerts require you to add `run.alert()` to your code. Without modifying your code, [Automations](/models/automations/) provide another way to notify Slack based on an event in W\&B, such as when an [artifact](/models/artifacts/) artifact version is created or when a [run metric](/models/runs/) meets or changes by a threshold.

  For example, an automation can notify a Slack channel when a new version is created, run an automated testing webhook when the `production` alias is added to an artifact, or start a validation job only when a run's `loss` is within acceptable bounds.

  Read the [Automations overview](/models/automations/) or [create an automation](/models/automations/create-automations/).
</Note>

<Note>
  The following guide only applies to alerts in Multi-tenant Cloud.

  If you're using [W\&B Server](/platform/hosting/) in your Private Cloud or on W\&B Dedicated Cloud, refer to [Configure Slack alerts in W\&B Server](/platform/hosting/monitoring-usage/slack-alerts) to set up Slack alerts.
</Note>

To set up an alert, take these steps, which are detailed in the following sections:

1. Turn on Alerts in your W\&B [User Settings](https://wandb.ai/settings).
2. Add `run.alert()` to your code.
3. Test the configuration.

### 1. Turn on alerts in your W\&B User Settings

In your [User Settings](https://wandb.ai/settings):

* Scroll to the **Alerts** section
* Turn on **Scriptable run alerts** to receive alerts from `run.alert()`
* Use **Connect Slack** to pick a Slack channel to post alerts. We recommend the **Slackbot** channel because it keeps the alerts private.
* **Email** will go to the email address you used when you signed up for W\&B. We recommend setting up a filter in your email so all these alerts go into a folder and don't fill up your inbox.

You will only have to do this the first time you set up W\&B Alerts, or when you'd like to modify how you receive alerts.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/_OEDykSS2PIumrEw/images/track/demo_connect_slack.png?fit=max&auto=format&n=_OEDykSS2PIumrEw&q=85&s=93436de7124ffccc9a07c3af6460b2bc" alt="Alerts settings in W&B User Settings" width="1420" height="900" data-path="images/track/demo_connect_slack.png" />
</Frame>

### 2. Add `run.alert()` to your code

Add `run.alert()` to your code (either in a Notebook or Python script) wherever you'd like it to be triggered

```python  theme={null}
import wandb

with wandb.init() as run:
    run.alert(title="High Loss", text="Loss is increasing rapidly")
```

### 3. Test the configuration

Check your Slack or emails for the alert message. If you didn't receive any, make sure you've got emails or Slack turned on for **Scriptable Alerts** in your [User Settings](https://wandb.ai/settings)

## Example

This simple alert sends a warning when accuracy falls below a threshold. In this example, it only sends alerts at least 5 minutes apart.

```python  theme={null}
import wandb
from wandb import AlertLevel

with wandb.init() as run:

    if acc < threshold:
        run.alert(
            title="Low accuracy",
            text=f"Accuracy {acc} is below the acceptable threshold {threshold}",
            level=AlertLevel.WARN,
            wait_duration=300,
        )
```

## Tag or mention users

Use the at sign `@` followed by the Slack user ID to tag yourself or your colleagues in either the title or the text of the alert. You can find a Slack user ID from their Slack profile page.

```python  theme={null}
run.alert(title="Loss is NaN", text=f"Hey <@U1234ABCD> loss has gone to NaN")
```

## Configure team alerts

Team admins can set up alerts for the team on the team settings page: `wandb.ai/teams/your-team`.

Team alerts apply to everyone on your team. W\&B recommends using the **Slackbot** channel because it keeps alerts private.

## Change Slack channel to send alerts to

To change what channel alerts are sent to, click **Disconnect Slack** and then reconnect. After you reconnect, pick a different Slack channel.
