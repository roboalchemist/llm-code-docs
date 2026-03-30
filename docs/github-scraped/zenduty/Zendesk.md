---
id: Zendesk
title: Zendesk
---
Zendesk is a customer service software and support ticketing system. To integrate Zendesk with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Zendesk integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Zendesk" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Zendesk

1. Log in to Zendesk. Go to Settings-> Extensions.

![](/img/Integrations/Zendesk/Webhook1.png)

1. Click on "Add Target" and select HTTP target. Fill in the form as shown below. In the url field, paste the webhooks url you copied earlier.
 Make sure to change the method to POST.

![](/img/Integrations/Zendesk/Webhook2.png)

1. Go to Zendesk -> Settings -> Business Rules -> Triggers

2. Click on "Add Trigger". Give the trigger name as "Zenduty trigger".

![](/img/Integrations/Zendesk/4.png)

1. Under "Meet ALL of the conditions", choose "Type" is "Incident" or some other value according to your requirements.

2. Under "Meet ANY of the following conditions", add two conditions - "Ticket is Created" and "Ticket is Updated"

3. Under Actions, select "Notify target", and select the target created in step 6.

4. In JSON body, paste the JSON below:

```

{"title":"{{ticket.title}}", "description":"{{ticket.description}}","url":"{{ticket.url}}", "id":"{{ticket.id}}", "status":"{{ticket.status}}"}

```

1. Click on "Save". Your Zendesk account is integrated. Zenduty will now create an incident for every new ticket created on Zendesk.
