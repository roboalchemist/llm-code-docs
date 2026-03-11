---
id: StatusCake
title: StatusCake
---

StatusCake offers powerful monitoring tools that are quick-and-easy to set up. To integrate StatusCake with Zenduty, complete the following steps:

## In Zenduty

1. To add a new StatusCake integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "StatusCake" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In StatusCake

1. Log in to StatusCake, and go to Alerting -> Contact Groups -> New Contact Group.

2. Enter the Zenduty URL in the "Webhook URL" field and save the contact.

![](/img/Integrations/StatusCake/1.png)

1. Once the webhook is created, we can generate an alert by first going to Uptime Monitoring -> New Basic HTTP/S Test.

2. Enter the URL to be monitored and a contact group with a valid webhook and save the test.

![](/img/Integrations/StatusCake/2.png)

1. StatusCake is now integrated.
