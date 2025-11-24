# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/setting-up-alerts.md

# Setting Up Alerts

> How to set up Alerts and automatically be alerted when things go wrong

Galileo enables you to get alerted whenever unexpected things happen (e.g. your cost is higher than expected, your model is hallucinating more than you want, users are entering foul language into your app).

**Pre-requisites**

Before setting up alerting, make sure you:

* [Configure your LLM APIs](/galileo/gen-ai-studio-products/galileo-evaluate/integrations/llms)

* [Turn on the Metrics you want to track (Guardrail Metrics or Custom Metrics)](/galileo/gen-ai-studio-products/galileo-observe/how-to/choosing-your-guardrail-metrics)

#### Set-Up

To set up your alerts, you need to define:

1. Who should be alerted and how

2. What they should be alerted on

Your *Alerting Settings* will be under your *Project Settings* page (i.e. the ⚙️ icon near the top-right of your *Monitoring Dashboard)*.

#### Email Alerts

If you want Alerts to be sent via emails, add your recipients' email addresses in the Alerts Recipients section:

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-alerts-email.png)

#### Slack Alerts

To get Alerts via Slack, you'll need to configure your workspace to receive slack messages via webhook URLs. You'll first need to follow [Slack's instructions to generate a webhook URL](https://api.slack.com/messaging/webhooks):

1. [Create a Slack app](https://api.slack.com/apps/new). This application will be used to send your notifications to your Slack workspace.

2. Pick a name like "Galileo Alerts" that will help identify where these messages are coming from.

3. Enable 'incoming webhooks'.

4. Create an 'incoming webhook' and choose the Slack channel you'd like Galileo's Alerts to go to.

Once you've followed the instructions above, grab the webhook URL from your Slack application and paste it into your Galileo Console. We recommend adding the name of the channel that's getting notificed in the "Notes" section:

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-alerts-webhook.png)

#### Configuring Alerts

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-alerts-configure.png)

Each alert is composed of a Metric (e.g. Correctness, Cost, Toxicity), an Aggregation Function (e.g. Min, Max, Average, Total), a threshold (e.g. greater than 0.5), and a time window (e.g. hourly).

**Example Alerts:**

* Exceeding costs: If you want to get alerted with an uptick in cost (above \$10/day, you select `Sum Value` of `Cost` is `more than or equal to` your `10` in the `last day`.

* Hallucinations: If you want to get alerted any time you have a hallucination, select `Min Value` of `Correctness` or `Context Adherence` is `equal to` `0`.

* Hallucination Rate: If you're comfortable with a certain level of hallucinations (e.g. 5%), you can select `Average value` of `Correctness` or `Context Adherence` is `less than or equal` to `0.05`.

**Triggering Alerts**

Once your Alerts are configured, we periodically run jobs to check whether your Alerts have been triggered. Once they do, you should receive an email letting you know which alert has triggered and what the value of the alert is.

From your email, you can click on the "Open Project" link to open your dashboard and find the problematic requests.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/observe-alerts-email-example.png)
