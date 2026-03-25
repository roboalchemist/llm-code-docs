# Source: https://docs.firehydrant.com/docs/pagerduty-integration.md

# PagerDuty

Our PagerDuty integration enables various functions to improve the efficiency of your incident management. You can:

* Automatically create FireHydrant incidents from PagerDuty alerts
* Notify different channels based on incoming alert content
* Page out to teams and services in PagerDuty from FireHydrant
* Automatically pull in on-call responders from PagerDuty's escalation policies to incident channels
* Importing services from PagerDuty to FireHydrant's Service Catalog
* ...and more!

## Prerequisites

* You will need <Glossary>Owner</Glossary> permissions to configure integrations in FireHydrant
* You'll need access to PagerDuty's Webhooks and Integrations settings (usually admin).

## Installation

> 🚧 Note
>
> The Default user email for the PagerDuty integration in FireHydrant must also be a user or account in PagerDuty, with matching emails. Failure to do so will result in errors when attempting to page through PagerDuty in Slack using `/fh page`

First, you need a PagerDuty API key.

1. Go to your PagerDuty dashboard and navigate to the page where you can set up API keys. (This will be something like **Integrations>**  **API Access Keys** ).

<Image align="center" alt="API Access Keys menu item in PagerDuty" border={false} caption="API Access Keys menu item in PagerDuty" src="https://files.readme.io/0ab8dac-pagerduty-api-key.png" width="650px" />

2. On the API Access page, click **Create New API Key** and provide a description for the API key.
3. Click **Create Key**.
4. Copy the API Key that PagerDuty generates. Then go to [FireHydrant's integrations page](https://app.firehydrant.io/organizations/integrations).
5. Click on the PagerDuty integration card, then click **Setup PagerDuty**.
6. Enter the PagerDuty API key you copied into the **API Token** field.
7. For **Default User Email**, for this field you must enter the email for an active user within your existing PagerDuty account.
8. For **Domain**, we default to showing `https://api.pagerduty.com`, which is the domain for PagerDuty's US service region. If you are a company based out of the EU and using PagerDuty's EU service region, then you will need to modify that value to `https://api.eu.pagerduty.com`. For more information, visit [PagerDuty's documentation](https://support.pagerduty.com/docs/service-regions).
9. Click **Authorize Application**.

### Setup Outgoing Webhook

> 🚧 Note
>
> If you plan to [import or link services](https://docs.firehydrant.com/docs/import-and-link-components) from PagerDuty, **do not** configure this outgoing webhook and skip this section. When you link or import PagerDuty Services to FireHydrant services, we automatically create service-scoped webhooks in PagerDuty.

After configuring the connection, if you do not plan to import or link services from PagerDuty, you should configure an outgoing webhook from PagerDuty so FireHydrant can both sync incident states and receive webhooks on alerts.

<Image align="center" alt="Webhook URL generated after installing PagerDuty" border={false} caption="Webhook URL generated after installing PagerDuty" src="https://files.readme.io/b978685-Screenshot_2024-01-03_at_7.15.58_PM.png" width="650px" />

1. In the integration settings page for PagerDuty on FireHydrant, copy the webhook address provided.
2. In PagerDuty, Head to **Integrations > Generic Webhooks** and click "+ New Webhook."
3. In **Webhook URL**, paste in the value you copied from FireHydrant.
4. For **Scope Type** choose "Account".
5. For **Event Subscription**, you can uncheck all the `service.*` events, leaving only the incident updates.
6. Click "Add Webhook".

To test this, go ahead and create an incident in FireHydrant. With default rules in FireHydrant, this will log an alert processing message.

<Image align="center" alt="Webhook logged after PagerDuty alert created" border={false} caption="Webhook logged after PagerDuty alert created" src="https://files.readme.io/d8c953f-image.png" width="400px" />

## PagerDuty Alert Routing

<Image align="center" alt="Configuring alert routes in PagerDuty" border={false} caption="Configuring alert routes in PagerDuty" src="https://files.readme.io/b449723-image.png" width="650px" />

Once your PagerDuty instance is configured, you can set up Alert Routes to take action on your alerts based on the data included in the alert. You can automatically open new incidents, send alerts to any Slack channel, log an alert in FireHydrant, or simply ignore it. To learn more, visit [Alert Routing](https://docs.firehydrant.com/docs/alert-routing) documentation. The rest of this page details the parameter mappings for PagerDuty.

### Parameter Mappings

Here is the table of routable parameters on FireHydrant and the corresponding key/value from the inbound PagerDuty webhook(s). The `$` refers to the webhook body content as a JSON object.

An explanation of PagerDuty's Webhook content can be found [in their docs here](https://developer.pagerduty.com/docs/ZG9jOjQ1MTg4ODQ0-overview).

| Parameter Name                   | PagerDuty Webhook Body            | Notes                                                                                                                                    |
| -------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| PagerDuty: Event Type            | *$.event.event\_type*             | The type of event sent by PagerDuty                                                                                                      |
| PagerDuty: Occurred At           | *$.event.occurred\_at*            | The datetime of when the event occurred according to PagerDuty                                                                           |
| PagerDuty: Alert ID              | *$.event.data.id*                 | The ID of the alert in PagerDuty                                                                                                         |
| PagerDuty: Incident ID           | *$.event.data.incident.id*        | The ID of the incident in PagerDuty                                                                                                      |
| PagerDuty: Incident Summary      | *$.event.data.title*              | Short summary of the PagerDuty incident                                                                                                  |
| PagerDuty: Data Type             | *$.event.data.type*               | The type of data, e.g., 'incident' or 'incident\_note', present in this message                                                          |
| PagerDuty: Alert Web URL         | *$.event.data.html\_url*          | URL to alert page in PagerDuty                                                                                                           |
| PagerDuty: Incident Web URL      | *$.event.data.incident.html\_url* | URL to incident page in PagerDuty                                                                                                        |
| PagerDuty: Incident Priority     | *$.event.data.priority.summary*   | Incident priority in PagerDuty. Must [enable priorities](https://support.pagerduty.com/docs/incident-priority) in PagerDuty to use this. |
| PagerDuty: Incident Status       | *$.event.data.status*             | The status of the incident in PagerDuty. Is one of `triggered`, `acknowledged`, and `resolved`.                                          |
| PagerDuty: Incident Note Content | *$.event.data.content*            | The content of a note posted to an incident in PagerDuty. Only shows up for `incident.annotated` events.                                 |
| PagerDuty: Incident Title        | *$.event.data.title*              | Name of the incident. Essentially the same as Incident Summary.                                                                          |

The following table maps our overall Alert Routing mapping object - these parameters are standard across all Alerting/Monitoring integrations.

| Parameter Name                  | PagerDuty Webhook Body          | Notes                                                                                                                                                                               |
| ------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alert Summary                   | *$.event.data.title*            | The same as **PagerDuty: Incident Summary** above.                                                                                                                                  |
| Alert Description               | *N/A*                           | Maps to nothing for PagerDuty. PagerDuty has a **Description** field in their alerts, but oddly they do not surface it in the webhook, so FireHydrant has no way of accessing it.   |
| Alert Priority                  | *$.event.data.priority.summary* | The same as **PagerDuty: Incident Priority** above.                                                                                                                                 |
| Alert Status                    | *$.event.data.status*           | Almost the same as **PagerDuty: Incident Status** above. However, FireHydrant expects `opened` instead of `triggered` to align with internal terminology.                           |
| Alert Associated Infrastructure | *N/A*                           | The associated Service/Functionality in FireHydrant. For us to detect this, you need to [import and/or link](https://docs.firehydrant.com/docs/import-and-link-components) a service in PagerDuty to FireHydrant. |

## Next Steps

Now that you've configured the PagerDuty integration, you can take the following steps to get the full power of FireHydrant + PagerDuty:

* [Import and Link Components](https://docs.firehydrant.com/docs/import-and-link-components) into your Service Catalog from PagerDuty
* See how you can [page and lookup on-call personnel in PagerDuty](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)
* Automatically create PagerDuty incidents via [Runbook step](https://docs.firehydrant.com/docs/runbook-step-create-pagerduty-incident)
* Configure teams to [pull personnel from on-call schedules](https://docs.firehydrant.com/docs/linking-on-call-schedules-to-teams)