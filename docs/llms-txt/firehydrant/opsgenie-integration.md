# Source: https://docs.firehydrant.com/docs/opsgenie-integration.md

# Opsgenie

FireHydrant's Opsgenie integration enables various capabilities within the platform:

* Automatically create FireHydrant incidents from Opsgenie alerts
* Notify different channels based on incoming alert content
* Page out to teams and services in Opsgenie from FireHydrant
* Automatically pull in on-call responders from Opsgenie escalation policies to incident channels
* Importing services from Opsgenie to FireHydrant's Service Catalog
* ...and more!

## Installation

### Prerequisites

* Ensure the Opsgenie account authorizing the integration has [API access](https://docs.opsgenie.com/docs/service-api#create-service).

### Connecting Opsgenie to FireHydrant

First, you need an Opsgenie API key.

1. Go to the Opsgenie Integrations page **Settings> Integrations** and click **Add integration**.
2. Search for and select **API**. Provide a name for this API integration and click **Continue**.
3. On the API settings page click **Edit**.  By default, all permissions will be selected, and you will want to ensure that "Allow Read Access", "Allow Create and Update Access" and "Allow Configuration Access" are selected.

<Image alt="Creating an API key in Opsgenie" align="center" width="579px" src="https://files.readme.io/568ac35-Screenshot_2024-02-20_at_12.38.45_PM.png">
  Creating an API key in Opsgenie
</Image>

3. Copy the API Key that is generated for you and press **Save**. Review the "Incoming Rules" and press **Turn on integration** to finalize API set up.

Now, take that API key and connect Opsgenie to FireHydrant.

1. Go to **Settings> Integrations list** and click on the Opsgenie integration.
2. On the Opsgenie page, click **Setup Opsgenie** and enter the API key you copied.

Once finished, you should be back on the Opsgenie integration page and a webhook URL will be generated. Make a note of it for the next section.

### Setup Outgoing Webhook

After configuring the connection, you will need to configure an outgoing webhook from Opsgenie so FireHydrant can correctly sync incident states.

<Image alt="Copy this webhook URL after connecting Opsgenie" align="center" width="650px" src="https://files.readme.io/7fc701a-Screenshot_2024-01-03_at_6.44.40_PM.png">
  Copy this webhook URL after connecting Opsgenie
</Image>

1. In the Opsgenie integration settings page on FireHydrant, copy the webhook address provided by FireHydrant.
2. In the Opsgenie app, go to **Settings> Integrations** and click "+ Add Integration."
3. Search for the **Webhook integration** and click on it.
4. Check the **Add alert description to payload** and **Add alert details to payload** boxes on the configuration page. You may choose to edit what events you want to trigger an alert to FireHydrant by modifying the triggers, but we recommend leaving this as the default.
5. Paste the copied webhook into the Webhook URL field and hit **Save**.

<Image alt="Default settings for Opsgenie outgoing webhook" align="center" width="650px" src="https://files.readme.io/b2902e9-opsgenie-outgoing-webhook.png">
  Default settings for Opsgenie outgoing webhook
</Image>

Now, you should be all set! You can create an incident or alert in Opsgenie to test this outgoing webhook. By default, an event should be registered under the "Alert Log" tab of the Opsgenie integration setting page on FireHydrant.

<Image alt="Example alert after configuring outgoing webhook" align="center" width="400px" src="https://files.readme.io/6363309-image.png">
  Example alert after configuring outgoing webhook
</Image>

## Opsgenie Alert Routing

Once your Opsgenie instance is configured, you can set up Alert Routes to take action on your alerts based on the data included in the alert. You can automatically open new incidents, send alerts to any Slack channel, log an alert in FireHydrant, or simply ignore it. To learn more about routing, see [Alert Routing](https://docs.firehydrant.com/docs/alert-routing). Below you'll find the list of parameter mappings for Opsgenie.

### Opsgenie Caveat and Noise

For Opsgenie, if you create an **Incident** in Opsgenie with Responders, you'll get multiple alerts: one "associated alert" that notifies nobody and another alert that pages Responders. This [seems to have been a deliberate decision](https://community.atlassian.com/t5/Opsgenie-questions/2-alerts-are-created-automatically-when-creating-an-Incident/qaq-p/2081425) by the Atlassian team, but this can cause a lot of noise on FireHydrant.

We don't currently have a way we can tell apart between the two alerts, so if you are using FireHydrant Alert Routing in conjunction with Opsgenie, we recommend only creating **Alerts** and not **Incidents** on Opsgenie when possible to avoid duplicate notifications/actions on FireHydrant.

### Parameter Mappings

Here is the table of routable parameters on FireHydrant and the corresponding key/value from the inbound Opsgenie webhook(s). The `$` refers to the webhook body content as a JSON object.

An explanation of Opsgenie's Webhook content can be found [in their docs here](https://support.atlassian.com/opsgenie/docs/opsgenie-edge-connector-alert-action-data/).

| Parameter Name              | Opsgenie Webhook Body               | Notes                                                                                                                                                       |
| --------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Opsgenie: Action            | *$.action*                          | The action taken that triggered this Webhook                                                                                                                |
| Opsgenie: Impacted Services | *$.alert.details.impacted-services* | The services marked impacted on the alert from Opsgenie side                                                                                                |
| Opsgenie: Created At        | *$.alert.createdAt*                 | When the alert was created                                                                                                                                  |
| Opsgenie: Description       | *$.alert.description*               | Description of the alert or incident                                                                                                                        |
| Opsgenie: Priority          | *$.alert.priority*                  | The Opsgenie alert's priority                                                                                                                               |
| Opsgenie: Alert ID          | *$.alert.alertId*                   | ID of the alert in Opsgenie                                                                                                                                 |
| Opsgenie: Message           | *$.alert.message*                   | Alert message or the Incident Summary if it's an incident                                                                                                   |
| Opsgenie: Web URL           | *$.alert.links.web*                 | Not all alerts have this parameter. If this parameter doesn't exist, FireHydrant reconstructs the URL for you and makes it available via Liquid templating. |

The following table shows our overall Alert Routing mapping object - these parameters are standard across all Alerting/Monitoring integrations.

| Parameter Name                  | Opsgenie Webhook Body | Notes                                                                                                                                                                                   |
| ------------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alert Summary                   | *$.alert.message*     | The same as **Opsgenie: Message** above                                                                                                                                                 |
| Alert Description               | *$.alert.description* | The same as **Opsgenie: Description** above                                                                                                                                             |
| Alert Priority                  | *$.alert.priority*    | The same as **Opsgenie: Priority** above                                                                                                                                                |
| Alert Status                    | *$.alert.action*      | The same as **Opsgenie: Action** above                                                                                                                                                  |
| Alert Associated Infrastructure | *N/A*                 | The associated Service/Functionality in FireHydrant. For us to detect this, you [must have linked](https://docs.firehydrant.com/docs/import-and-link-components) a Service or Functionality to a service in Opsgenie. |

## Next Steps

Now that you've configured the Opsgenie integration, you can take the following steps to get the full power of FireHydrant + Opsgenie:

* [Import and Link Components](https://docs.firehydrant.com/docs/import-and-link-components) into your Service Catalog from Opsgenie
* See how you can [page and lookup on-call personnel in Opsgenie](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)
* Automatically create Opsgenie incidents via [Runbook step](https://docs.firehydrant.com/docs/runbook-step-create-opsgenie-incident)
* Configure teams to [pull personnel from on-call schedules](https://docs.firehydrant.com/docs/linking-on-call-schedules-to-teams)