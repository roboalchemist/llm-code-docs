---
id: Kayako
title: Kayako
---

Kayako builds customer service and help desk software which businesses use to talk to and support their customers. To integrate Kayako with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Kayako integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Kayako" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Kayako

1. Log in to Kayako, click on the "Admin" button and select "Endpoints" under "Integration".

![](/img/Integrations/Kayako/1.png)

1. Click on "New Endpoint" and select Webhook(HTTP Request).

![](/img/Integrations/Kayako/2.png)

1. Set the Request method as “POST” and request content type as “JSON”. Save.

2. Enter the "Endpoint Title" and paste the url you copied earlier under "Request URL".

![](/img/Integrations/Kayako/3.png)

1. Select "Triggers" under "Automation" from the "Admin" menu.

![](/img/Integrations/Kayako/4.png)

1. Click "New Trigger". Enter the "Rule Title" and set the condition as "Conversations: Type equal to Incident".

![](/img/Integrations/Kayako/5.png)

![](/img/Integrations/Kayako/6.png)

1. Select the zenduty endpoint from "Performance Actions" and select "Simple" under request payload. Save.

![](/img/Integrations/Kayako/7.png)

1. Click on New on the top left your screen and select Conversation.

 * If the Conversation is ‘New’ or ‘Open’,it triggers an event in the Zenduty.

 * If the Conversation is ‘Pending’,it is acknowledged.

 * If the Conversation is ‘Completed’,it is resolved.

2. Kayako is now integrated.
