# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/setting-up-alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=51713016017242050dcaa42b96f64b84" alt="" data-og-width="801" width="801" data-og-height="221" height="221" data-path="images/observe-alerts-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=08021604250ffd180e7ff8ad623f8c55 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=5bc1e072fa0b8020aa27f93882c5648e 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=edf7fa76ae3611e9ddf22b87d3db158a 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b8ae60b20c4e11367b5c18536ecd77dd 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=bcab1342af7cb273175abf122fdb4625 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ba78fbbe8906907afe940e2c9944d1e4 2500w" />

#### Slack Alerts

To get Alerts via Slack, you'll need to configure your workspace to receive slack messages via webhook URLs. You'll first need to follow [Slack's instructions to generate a webhook URL](https://api.slack.com/messaging/webhooks):

1. [Create a Slack app](https://api.slack.com/apps/new). This application will be used to send your notifications to your Slack workspace.

2. Pick a name like "Galileo Alerts" that will help identify where these messages are coming from.

3. Enable 'incoming webhooks'.

4. Create an 'incoming webhook' and choose the Slack channel you'd like Galileo's Alerts to go to.

Once you've followed the instructions above, grab the webhook URL from your Slack application and paste it into your Galileo Console. We recommend adding the name of the channel that's getting notificed in the "Notes" section:

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-webhook.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=6f7bc47f70a9c8a8f100706f6f5135ee" alt="" data-og-width="852" width="852" data-og-height="274" height="274" data-path="images/observe-alerts-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-webhook.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=dec1aa412f1f3e766ca7d9c1c2d6f6ef 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-webhook.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b79b48e61e8cfd1114b43aa6724fb210 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-webhook.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=0da87eec0941347a0f0b7cd3a84a83bf 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-webhook.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d4845f9c8b18ed8fd61022de97aa35ce 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-webhook.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=6225b0560b4eec0b6cf2b4044ce9caba 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-webhook.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=1f30c55670ad580878ab397d438dd56d 2500w" />

#### Configuring Alerts

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-configure.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=5e31b4ee8063dfd7283ecda9b044b6bf" alt="" data-og-width="2138" width="2138" data-og-height="670" height="670" data-path="images/observe-alerts-configure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-configure.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ec7f065eb19337c77af0863418c45455 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-configure.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b8befbe52b3b1318c5bb70bf7d367bb6 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-configure.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b54462670aecf7db1f564915a2281201 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-configure.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=0d1f3a5e6c702dbce1d831a97184eedb 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-configure.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=52a0b86e64011db159218dc894d56a59 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-configure.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=1b08d59c102503f1b16ee878046dece5 2500w" />

Each alert is composed of a Metric (e.g. Correctness, Cost, Toxicity), an Aggregation Function (e.g. Min, Max, Average, Total), a threshold (e.g. greater than 0.5), and a time window (e.g. hourly).

**Example Alerts:**

* Exceeding costs: If you want to get alerted with an uptick in cost (above \$10/day, you select `Sum Value` of `Cost` is `more than or equal to` your `10` in the `last day`.

* Hallucinations: If you want to get alerted any time you have a hallucination, select `Min Value` of `Correctness` or `Context Adherence` is `equal to` `0`.

* Hallucination Rate: If you're comfortable with a certain level of hallucinations (e.g. 5%), you can select `Average value` of `Correctness` or `Context Adherence` is `less than or equal` to `0.05`.

**Triggering Alerts**

Once your Alerts are configured, we periodically run jobs to check whether your Alerts have been triggered. Once they do, you should receive an email letting you know which alert has triggered and what the value of the alert is.

From your email, you can click on the "Open Project" link to open your dashboard and find the problematic requests.

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email-example.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=a5c19e309ea3ddf904c019151ec5c781" alt="" data-og-width="2016" width="2016" data-og-height="888" height="888" data-path="images/observe-alerts-email-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email-example.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=3f3c7efba380f24a255f9f4d0ad4eaf2 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email-example.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ad917867dd13b21806c357306b05ae12 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email-example.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ec6144d273f3d73ef526fb8bdaa19444 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email-example.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=7b874f30ac5bfc9786aaf50d92c614bf 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email-example.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=738ae6613c4b7f80de2235ff00840fc0 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/observe-alerts-email-example.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=cec1e941b90ef2854a3a8f7e01506630 2500w" />
