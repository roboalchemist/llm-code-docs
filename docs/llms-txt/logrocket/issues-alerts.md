# Source: https://docs.logrocket.com/docs/issues-alerts.md

# Issues Alerts (Beta)

Issues Alerts deliver notifications of impactful issues flagged by Galileo AI directly to your team via Slack and webhooks.

<Callout icon="🧪" theme="default">
  Issue Alerts is currently in **open beta**
</Callout>

Issues Alerts notifies teams of new issues affecting users flagged as severe by [Galileo AI](https://docs.logrocket.com/docs/galileo). These alerts are configurable and delivered to your preferred channel, reducing the need for constant monitoring within LogRocket. You can configure on the Issues tab or within Settings > Issues Settings.

<Image align="center" border={true} width="300px" src="https://files.readme.io/72a80e055cac9413f0b01a825f1d71fb431249609838f6af2a76fa67693d770d-Screenshot_2025-09-03_at_10.52.18_AM.png" className="border" />

<Image align="center" border={true} caption="Click &#x22;Configure Alerts&#x22; -> &#x22;Alerts&#x22; to get started" src="https://files.readme.io/95a87eb56f2cab368c0b06b3d47fe77282f7df9f1428e0c43d9d04270cc2d594-Screenshot_2025-09-03_at_11.14.17_AM.png" width="500px" />

## Configuring Alerts

Issues Alerts can be configured with the following conditions:

* **Page Definitions** - Alerts can be scoped to focus just on certain Visited URL [Definitions](https://docs.logrocket.com/docs/definitions), or feature areas of a site or app. [Page Definitions can also be used to filter issues on the Issues tab](https://docs.logrocket.com/docs/issues#definitions-feature-areas-filter).
* **Platform** - This provides the option to limit the alerts to issues that have occurred on the chosen platform (Web/Android/iOS).
* **Alert Threshold** - the number of users an issue must affect before it is alerted on.

<br />

<Image align="center" src="https://files.readme.io/89b93aef2e89ea2ca87a5d3f6ff5c387aa42d0803080fd8a88563366647b95b2-Screenshot_2025-09-03_at_11.31.29_AM.png" />

NOTE: your permissions will need to include access to General Settings to configure an Issues alert

## Alert Destinations

Alerts can be configured to send to Slack or webhooks. When creating an alert configuration, select the "Send to:" destination:

<Image align="center" border={true} caption="Issues Alerts destinations" src="https://files.readme.io/85a32c6fa6538b56b4bc7a32cb16dfff481d6b6a1f4838a336cbb00b59e33325-Screenshot_2025-09-03_at_11.46.41_AM.png" />

### Alerts via Slack

<Image align="center" border={true} caption="Issues Alert via **Slack**" src="https://files.readme.io/97f0c586bbbabaddb6ebdc782a28e998689bc7dd2240b245470d12fefee1abd4-Screenshot_2025-09-03_at_12.13.02_PM.png" />

When creating an Issues Alert, select "Slack" in the "Send to" field. Click the "Connect Slack" button to be directed to Slack's authentication and setup flow.

![](https://files.readme.io/bf54194-Screenshot_2023-07-19_at_1.16.43_PM.png)

Completing the Slack flow completes the Slack integration.

### Alerts via Webhook

When creating an Issues Alert Configuration, select "Webhook" in the "Send to" field. In the "Webhook URL" field, provide the endpoint URL from your chosen destination that provides the webhook.

#### Example webhook payload

```json json
{
  type: 'IssuesAlert',
  appID: 'apphub/logrocket',
  title: 'New Severe Issues',
  issue: {
    issueType: 'EXCEPTION',
    url: 'https://app.logrocket.com/issues/',
    firstSeen: 1746809383, // epoch ms
    sessionCount: 10,
    sessionRate: '1.2', // occurrences per minute
    label: 'Error • TypeError: Cannot read properties of undefined (reading "title")',
    issueDescription: 'Users get an error and are logged out',
    screenshotUrl: 'https://storage.googleapis.com/logrocket-assets/logrocket-logo-slack.png'
  }
}
```

<br />

<br />