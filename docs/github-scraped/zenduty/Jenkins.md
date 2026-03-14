---
id: Jenkins
title: Jenkins
---
Jenkins is a self-contained Java-based program, ready to run out-of-the-box, with packages for Windows, Mac OS X and other Unix-like operating systems

With the Zenduty integration, you will be able to receive context notifications about new builds. Failed builds will trigger new incidents.

To integrate Jenkins with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Jenkins integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Jenkins" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Jenkins

1. Log in to your Jenkins instance.

2. Install the Jenkins Notifications plugin from the Jenkins marketplace.

3. Navigate the the job from which you wish to receive alerts.

4. From the left panel, click on Configure

5. Click on the "Job notifications" tab on the top. Click on "Add Endpoint".

6. Under format, select JSON. Under protocol, select HTTPS. Under event, select "All Events".

7. Under URL source, select "Plain text". In the URL field, paste the integration URL you copied earlier.

![](/img/Integrations/Jenkins/1.png)

1. Click on Save to apply the settings.
