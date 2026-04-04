---
id: FreshdeskTwoWay
title: Freshdesk (two-way)
---
Freshdesk is an online cloud-based customer service software providing helpdesk support with all smart automations to get things done faster. To integrate Two-Way Freshdesk with Zenduty, complete the following steps:

## On the Zenduty Dashboard

1. To add a new Freshdesk integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Outgoing Integration". Give it a name and select the application "Freshdesk(two-way)" from the dropdown menu.

![](/img/Integrations/FreshDeskOutgoing/FreshDesk7.png)

1. Go to "Configure" under your integrations to edit it.

2. Opena new tab and to your Freshdesk page and copy your API token from the "My Profile Settings" page.

![](/img/Integrations/FreshDeskOutgoing/FreshDesk1.png)

1. GO back to the Zenduty Freshdesk(two-way) settings tab, and under "Domain name", enter your Freshdesk domain name. For example, if your Freshdesk URL is acme.freshdesk.com, then your domain name is "acme"

![](/img/Integrations/FreshDeskOutgoing/FreshDesk3.png)

1. Click Next to Authenticate your credentials

![](/img/Integrations/FreshDeskOutgoing/FreshDesk2.png)

1. Proceed to map the Incident response from  Zenduty to FreshDesk and from FreskDesk to Zenduty. This  will determine what action will change the ticket status and vice versa with Zenduty incident statuses.

This is shown in the screenshot below:
![](/img/Integrations/FreshDeskOutgoing/FreshDesk4.png)

1. Copy the generated webhook URL to be applied onto FreshDesk.

2. Then click "Save Integration".

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

 Set "When an Action Performed By" to "Agent or Requester".Then set "Involved any of these events" for "Status is Changed" from "Any Status" to "Any Status".

2. In the "On tickets with these properties" section, set condition as "Type Is" and "Incident".

![](/img/Integrations/FreshDeskOutgoing/FreshDesk5.png)

1. Select "Trigger Webhook" from the "Actions" dropdown and set the "Request Type" to "POST".

 In the URL textbox, paste the webhook link you copied earlier.

 Set the Encoding to "JSON" and Content to "Simple".

 Under Content, Select fields - Ticket ID, Subject, Description, Ticket Status and Ticket URL.

This is shown in the screenshot below:

![](/img/Integrations/FreshDeskOutgoing/FreshDesk6.png)

1. Save.

Your Freshdesk(two-way) is now integrated to your Zenduty account.
