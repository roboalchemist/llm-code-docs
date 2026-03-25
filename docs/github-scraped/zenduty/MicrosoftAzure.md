---
id: MicrosoftAzure
title: Microsoft Azure Alerts
---
Microsoft Azure alerts helps you monitor applications, infrastructure, and servers for various metrics. For an alert rule on a metric value, when the value of a specified metric crosses a threshold assigned, the alert rule becomes active and sends a notification to Zenduty. For an alert rule on events, a rule can send a notification on every event, or, only when a certain number of events happen. To integrate Azure Monitor with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Microsoft Azure integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button correspoding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Microsoft Azure" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Microsoft Azure

1. Open the Azure portal and click on Alerts. Search on the search bar if not directly visible.

 ![](/img/Integrations/MicrosoftAzure/11.jpg)

1. Create a new alert rule.

![](/img/Integrations/MicrosoftAzure/12.jpg)

1. Select the resource which you want to monitor. Here we shall monitor a Virtual Machine.  
   
![](/img/Integrations/MicrosoftAzure/13.jpg)

![](/img/Integrations/MicrosoftAzure/14.png)

1. Select the condition based on which the alert is to be triggered. Here we create an alert which is triggered when the CPU utilization of a Virtual Machine crosses 50%.

![](/img/Integrations/MicrosoftAzure/15.jpg)

![](/img/Integrations/MicrosoftAzure/16.png)

![](/img/Integrations/MicrosoftAzure/17.png)

1. Create an Action Group (or use a previously created action group)

![](/img/Integrations/MicrosoftAzure/18.jpg)

1. Enter the Action group name and short name:

![](/img/Integrations/MicrosoftAzure/19.png)

1. Enter an action name and select Webhook under Action Type. A dialog box appears in the side.

![](/img/Integrations/MicrosoftAzure/20.png)

1. Enter the URL copied from Step 4 above.

![](/img/Integrations/MicrosoftAzure/21.png)

1. Enable the common alert schema by toggling the button to yes and then click on OK.

![](/img/Integrations/MicrosoftAzure/22.jpg)

1. Click on OK to add the action group.

![](/img/Integrations/MicrosoftAzure/23.png)

The action group has now been created. It should visible under the section of Action Groups

![](/img/Integrations/MicrosoftAzure/24.jpg)

1. Fill in the alert details appropriately. The alert rule name along with the severity will appear as the alert message and the alert description will appear as the summary in Zenduty

 ![](/img/Integrations/MicrosoftAzure/25.jpg)

1. Click on create alert rule. You have now successfully added Azure as an integration!
