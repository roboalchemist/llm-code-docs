---
id: GhostInspector
title: Ghost Inspector
---
Ghost inspector helps you build or record automated website tests in your browser and continuously monitor websites for issues. To integrate Ghost Inspector with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Ghost Inspector integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Ghost Inspector" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Ghost Inspector

1. Log into Ghost Inspector.

![](/img/Integrations/GhostInspector/1.png)

1. Now create a "Test".

![](/img/Integrations/GhostInspector/2.png)

![](/img/Integrations/GhostInspector/3.png)

1. Go to "Notification" -> "Webhook" and create a "Notifier".

![](/img/Integrations/GhostInspector/4.png)

1. Now in the URL field paste the copied link and click on "Add".

![](/img/Integrations/GhostInspector/5.png)

1. Then go to Settings -> Notification -> Email and then select "Condition" and create a "Condition".

2. Ghost Inspector is now integrated.
