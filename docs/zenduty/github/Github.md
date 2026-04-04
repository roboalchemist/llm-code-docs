---
id: Github
title: Github
---
GitHub brings together the world's largest community of developers to discover, share, and build better software.

With the Zenduty integration, you will be able to receive context notifications about new code pushes, pull requests, issues and issue comments. New issues will trigger a new incident.

To integrate Github with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Github integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Github" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Github

1. Log in to Github and navigate to the project from which you wish to receive alerts.

2. On the top bar, click on the project Settings (you will need admin rights for this).

3. From the left panel, click on Webhooks. Click on Add Webhook.

4. In the "Payload URL" input box, paste the Integration URL you copied earlier.

5. Choose "Content Type" as application/json

6. Under "Which events would you like to trigger this webhook?", click on "Let me select individual events".

7. Select the events which you want to track in Zenduty. Events supported are "Pushes", "Issues", "Pull Requests" and "Releases"

![](/img/Integrations/Github/1.png)

1. Click on Add Webhook to save.
