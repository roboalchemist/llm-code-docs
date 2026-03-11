---
id: Freshdesk
title: Freshdesk
---
Freshdesk is an online cloud-based customer service software providing helpdesk support with all smart automations to get things done faster. To integrate Freshdesk with Zenduty, complete the following steps:

## On the Zenduty Dashboard

1. To add a new Freshdesk integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Freshdesk" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Freshdesk

1. Log into Freshdesk. Click on the "Admin" button and select "Automations" under "Helpdesk Productivity Settings".

![](/img/Integrations/Freshdesk/1.png)

1. Click on the "Create the first rule" button.

![](/img/Integrations/Freshdesk/2.png)

1. Select "New Rule" and pick "Rule Name" and "Description". Set Conditions as:
 
 **Type Is Incident**

![](/img/Integrations/Freshdesk/3.png)

1. Select "Trigger Webhook" from the Actions"  dropdown, and set "Request Type" to "POST".

 Under the "URL", paste the webhook url you copied earlier.

 Set the "Encoding" as "JSON" and content as "Simple".
 
 Under "Content", select the following fields- Ticket ID, Subject, Description, Status, Ticket URL.

This is shown in the screenshot below:

![](/img/Integrations/Freshdesk/4.png)

1. Save.

2. From the same window, move to "Ticket Updates" sections and click on "New Rule" button.

![](/img/Integrations/Freshdesk/5.png)

1. Select "New Rule" and pick a "Rule Name" and "Description".

 Set "Action Performed By" to "Agent" and an "Event". For example, here we have picked:"Status is Changed" from "Any Status" to "Any Status" and so on depending upon the requirements.

![](/img/Integrations/Freshdesk/6.png)

![](/img/Integrations/Freshdesk/7.png)

1. In the "On tickets with these properties" section, set condition as "Type Is" and "Incident".

![](/img/Integrations/Freshdesk/8.png)

1. Select "Trigger Webhook" from the "Actions" dropdown and set the "Request Type" to "POST".
 
 In the URL textbox, paste the webhook link you copied earlier.
 
 Set the Encoding to "JSON" and Content to "Simple".
 
 Under Content, Select all the fields under Content, including and especially Ticket ID, Subject, Description, Status and Ticket URL.

This is shown in the screenshot below:

![](/img/Integrations/Freshdesk/9.png)

1. Save.

Freshdesk is now integrated to your Zenduty account.
