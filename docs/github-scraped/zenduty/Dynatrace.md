---
id: Dynatrace
title: Dynatrace
---
Dynatrace provides application performance management, artificial intelligence for operations, cloud infrastructure monitoring, and digital experience management. To integrate Dynatrace with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Dynatrace integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Dynatrace" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Dynatrace

1. Login to Dynatrace. Go to Settings -> Integration -> Problem notifications. Click on the "Set Up Notifications" tab at the top of the page.

![](/img/Integrations/Dynatrace/1.png)

1. Next, paste this payload into the "Custom Payload" field:

 ```
 {
 "State":"{State}",
 "ProblemID":"{ProblemID}",
 "ProblemTitle":"{ProblemTitle}",
 "ProblemDetails":"{ProblemDetailsText}",
 "ProblemURL":"{ProblemURL}"
 }
 ```

2. Paste the url you copied earlier.

![](/img/Integrations/Dynatrace/2.png)

1. Click "Save" and Dynatrace is integrated.
