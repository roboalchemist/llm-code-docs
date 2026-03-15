# Source: https://docs.firehydrant.com/docs/notify-slack-when-a-new-ai-summary-is-generated.md

# Notify Slack when a new AI Summary is generated

Want to tell a Slack channel when a new AI summary has been generated for your incident? Follow these steps.

First, visit your runbooks page and edit or create a new runbook. We'll use our runbook to then add a step with conditions for posting into Slack when a new summary has become available.

![](https://files.readme.io/3f853d5026bf738a7fb771672266b0feff85585dcd2a6d66e6494e97d2c71a25-CleanShot_2025-07-16_at_09.13.172x.png)

If you're creating a new runbook, click the "Add your first step" button to open the step builder for the runbook.

![](https://files.readme.io/47dfb2cd7d289d6c91071a4c21b0bed87810ddde27e330a21f239d782757f9ac-CleanShot_2025-07-16_at_09.16.072x.png)

In the step builder, you have options! You can choose:

1. If you'd like to send the message with your new AI summary to the *incident* channel (the one FireHydrant creates per incident).
2. Or, if you'd like to send the incident to *a separate channel* (IE: A #support channel).

Or, you can add both steps to your runbook. The choice is yours.

![](https://files.readme.io/19824a3455178de30cccd3bbe27bc2c3a77ab691d80f03abcb26e94367a817f3-CleanShot_2025-07-16_at_09.17.332x.png)

For this guide, we're using the **Notify Slack channels with a custom message** step type. We'll configure it with:

* The `#general` channel (so our entire company sees the update)
* A liquid template for the AI summary
* Some conditions to make sure we only post when a new summary is generated

![](https://files.readme.io/71dba43bb8bfc365082375e7adc9002454debc94fbc0823a6c3afc43a2df49f2-CleanShot_2025-07-16_at_09.21.522x.png)

An example liquid template is:

```liquid Liquid Template
A new incident summary has been posted:
{{ incident.ai_incident_summary }}
```

In some cases, these summaries can be *very* long and you may want to shorten them:

```liquid Liquid Template
A new incident summary has been posted:
{{ incident.ai_incident_summary | truncatewords: 30 }}
```

### Conditions

After you've configured these values, we need to add the magic: **The conditions!**

FireHydrant supports a "AI Summary" attribute that has a few operators on them, including one for when the AI summary changes. Select it, and then select the operator for "changes."

Then, make sure you check the box for "Rerun on every transition" – this is what makes FireHydrant repeat this step each time the condition evaluates to true.

![](https://files.readme.io/1afdee6b2b852299180b1f57697cd2c90a4a93c0becfd2f908c5760f41197c5a-Clipboard-20250716-132949-923.gif)

## Voila!

After that, click "Add Step", **save your runbook**, and give it a shot!