---
id: Loggly
title: Loggly
---
Loggly provides log analysis and monitoring in the cloud. To integrate Loggly with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Loggly integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Loggly" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Loggly

1. Log in to Loggly, and navigate to the "Alerts" tab at the top of the page.

![](/img/Integrations/Loggly/1.png)

1. Then go to Alert Endpoints -> Create Endpoint.

![](/img/Integrations/Loggly/2.png)

1. In the "Endpoint" dropdown list, choose "HTTP/S" Endpoint. Enter the Zenduty URL you copied earlier in the URL section.

2. Choose the POST method. Once the webhook is created, goto the "List" option near the top of the page.

3. Then click on "Add New". Select the "Send to Endpoint" option, and select the newly created webhook from the dropdown.

![](/img/Integrations/Loggly/3.png)

1. Fill the "Saved Search" form according to your application's requirements.

2. Zenduty will now send you alerts from Loggly.
