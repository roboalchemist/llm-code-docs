---
id: Dynamics365
title: Microsoft Dynamics
---
Microsoft Dynamics is a line of enterprise resource planning and customer relationship management software applications. Microsoft markets Dynamics applications through a network of reselling partners who provide specialized services. Microsoft Dynamics forms part of "Microsoft Business Solutions".

The Zenduty-Dynamics integration helps you escalate critical cases/incidents to the right team, proactively alert them about SLA violations and bring in SMEs and stakeholders into high priority cases. To integrate Panopta with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Dynamics integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Dynamics" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Dynamics(you will need Office365-Dynamics Administrator permissions to do the steps below)

We will be using the Dynamics Plugin Registration Tool to create a Webhook action to the webhook URL copied in step 4, for Dynamics "Create" and "Update" actions on the "Incidents" entity in Dynamics.

1. Click [here](https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/download-tools-nuget) and download and install the Dynamics PluginRegistrationTool.

2. Open the PluginRegistration tool. Click on "Create new connection" and login with your administrator account.

3. Inside Plugin Registration tool, click on Register -> Register New Web Hook.

4. Specify any name for the webhook. In the Endpoint URL, paste the URL copied without any query string part. For **Authentication** select WebhookKey and paste the URL copied in step 4 to register the Webhook.

5. Register a new step inside the Webhook. In **Message** select "Create". For Primary Entity, select "Incident". For event handler, select Webhook registered in step 8. For **Event Pipeline stage of execution** select "PostOperation". For **Execution mode** select "Asynchronous". For **Deployment**, select "Server".

6. Register a new step inside the Webhook. In **Message** select "Update". For Primary Entity, select "Incident". For event handler, select Webhook registered in step 8. For **Event Pipeline stage of execution** select "PostOperation". For **Execution mode** select "Asynchronous". For **Deployment**, select "Server".

7. Dynamics 365 is now integrated with Zenduty.
