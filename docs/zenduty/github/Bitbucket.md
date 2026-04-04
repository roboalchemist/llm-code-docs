---
id: Bitbucket
title: Bitbucket
---

Bitbucket is a web-based version control repository hosting service owned by Atlassian, for source code and development projects that use either Mercurial or Git revision control systems.

With the Zenduty integration, you will be able to receive context notifications about new code pushes, pull requests, issues and issue comments. New issues will trigger a new incident.

To integrate Bitbucket with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Bitbucket integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Bitbucket" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Bitbucket

1. Log in to Bitbucket and navigate to the project to which you want to receive alerts from.

2. On the left bar, click on the project Settings (you will need admin rights for this).

3. From the left panel, click on Webhooks. Click on Add Webhook.

4. Give a title, and in the URL input box, paste the Integration URL you copied earlier.

5. In Triggers, click on "Choose from a full list of triggers".

6. Select the events which you want to track in Zenduty.

![](/img/Integrations/Bitbucket/1.png)

1. Click on Save to complete the integration.

![](/img/Integrations/Bitbucket/1.png)
