---
id: StatusPage2
title: StatusPage (2-Way)
---
StatusPage.io is the best way for web infrastructure, developer API, and SaaS companies to get set up with their very own status page in minutes. To integrate Zenduty with StatusPage, complete the following steps:

## In Zenduty

1. To add a new StatusPage integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Outgoing Integrations" and then "Add New Integration". Give it a name and select the application "StatusPage(2-Way)" from the dropdown menu.

4. Go to "Configure" under your StatusPage (2-Way) Integration.

5. Here, you have to input your StatusPage API, which can be found by :

    1. Logging in to your account at https://manage.statuspage.io/login
    2. Click on the User Profile icon at the top-right.
    3. Click the "Manage Account" link under the menu which appears.
    4. Click on the "API" tab and copy the API key.

6. Paste the API key in Zenduty and Proceed by clicking "Authenticate StatusPage".

7. If the API is authenticated, Select the Page & then one Component of that Page.

8. Then, write the description of the incident (Which will be common to all incidents incited by this integration.)

![](/img/Integrations/Statuspage/7.png)

1. Copy the Webhook URL (For 2-Way integration) and Save the integration.

## In StatusPage

1. Login. Go to Notifications -> Subscribers. Click on "Add Subscriber".

![](/img/Integrations/Statuspage/1.png)

![](/img/Integrations/Statuspage/2.png)

1. Under "Subscriber Type" select "Webhook", enter the Webhook URL and a valid email address.

Now, we can monitor the incidents that are made by Zenduty, and the changes are reflected in the StatusPage incident is reflected in the Zenduty incident.

1. StatusPage is now integrated.
