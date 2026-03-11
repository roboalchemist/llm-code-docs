---
id: SignalFX
title: SignalFX
---
SignalFx is a real-time cloud monitoring platform for infrastructure, microservices, and applications. The platform discovers and collects metrics across every component in your cloud environment, replacing traditional point tools and providing real-time predictive analytics. To integrate SignalFX with Zenduty, complete the following steps:

## In Zenduty

1. To add a new SignalFX integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "SignalFX" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In SignalFX

1. Log in to your SignalFX account. Click on the "Integrations" tab and scroll down to the "Notification Services" section.

![](/img/Integrations/SignalFX/1.png)

1. Click on "Webhook" and then click on the "New Integration" button. Paste the webhooks url you copied earlier.

![](/img/Integrations/SignalFX/2.png)

Click Save to create the new webhook.

1. Once the new webhook has been created, stay on the Integrations page. Follow the given instructions to integrate a service of your choice with SignalFX.
As an example, SignalFX SmartAgent is integrated here.

![](/img/Integrations/SignalFX/3.png)

1. Once a service has been integrated, navigate to the "Alerts" page by clicking the tab at the top of the page. Then, click on the "New Detector" button to add a new alert for the integrated service.

![](/img/Integrations/SignalFX/4.png)

1. Now, we will setup the conditions for the alerts.

 * Add the Signal Source. This is the service you just integrated.

 ![](/img/Integrations/SignalFX/5.png)

 * Set the Alert Conditions, Settings and Message as per your need.

 * Click on the "Alert Recipients" tab and add the newly created webhook.

 ![](/img/Integrations/SignalFX/6.png)

2. Once the alert is activated, we should see notifications pop-up on the Zenduty Incidents page.
