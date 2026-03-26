# Source: https://checklyhq.com/docs/integrations/alerts/gitlab_alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating GitLab Alerts

> Configure GitLab Alerts integration to receive failure, degradation, and recovery messages from Checkly

Checkly integrates with [GitLab Alerts](https://docs.gitlab.com/ee/operations/incident_management/alerts.html) and can deliver failure, degradation, and recovery messages to any project in your GitLab installation. More specifically, Checkly will:

* Open new alerts when a check fails.
* Close alerts automatically when a failing check recovers.
* Alert when SSL certificates are about to expire.

1. First, create an **HTTP Endpoint**. Log in to GitLab, select a project workspace and go to "Settings" > "Monitor" and expand the "Alerts" tab and click the "add new integration" button. Then select "HTTP Endpoint" as the integration type.
2. **Choose a name** for your integration like "Checkly".

   <img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/gitlab/gitlab_step2.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=2a990cd769331d0caf36995824df84d7" alt="setup checkly gitlab integration step 2" width="1109" height="829" data-path="images/docs/images/integrations/gitlab/gitlab_step2.png" />
3. Save the integration **copy the displayed Webhook URL and Authorization Key**. It should start with something like `https://gitlab.com/...`

   <img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/gitlab/gitlab_step3.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=8f4d5a4b5efadd9b03f1b63fb9d60a24" alt="setup checkly gitlab integration step 3" width="1109" height="829" data-path="images/docs/images/integrations/gitlab/gitlab_step3.png" />
4. Log in to Checkly and navigate to [Alert Settings](https://app.checklyhq.com/alert-settings/). Click the "Add more channels" button, find GitLab Alerts on the list, and click "Add channel".

   <img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/gitlab/gitlab_step4.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=82fc3e054d9b33fb46b54630af07698f" alt="setup checkly gitlab_integration step 5" width="1085" height="728" data-path="images/docs/images/integrations/gitlab/gitlab_step4.png" />
5. Give the alert channel a name and **paste the Webhook URL and Authorization Key** in their respective input fields. You can now also tweak which alerts you want to be notified of and which checks or check groups should be subscribed to this channel.

   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/gitlab/gitlab_step5.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=920b682d7294f4edb288b32e71e0e578" alt="setup checkly gitlab integration step 5" width="1035" height="700" data-path="images/docs/images/integrations/gitlab/gitlab_step5.png" />

   > Note that we provide a preconfigured message payload but you are free to edit the payload and add more or different variables. Just click the "Edit payload" button and reference the "Help & variables tab".

Congratulations! You have successfully integrated Checkly with GitLab Alerts!


Built with [Mintlify](https://mintlify.com).