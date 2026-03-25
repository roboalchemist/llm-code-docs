---
id: Sysdig
title: Sysdig
---
Sysdig is the first unified approach to cloud-native visibility and security with Kubernetes, Prometheus, and Falco support.
To integrate Sysdig with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Sysdig integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Sysdig" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Sysdig

1. Sign into Sysdig.

2. Then Add a new "HOST" as per your requirements.

![](/img/Integrations/Sysdig/1.png)

1. Go to settings and add a "NOTIFICATION CHANNEL".

![](/img/Integrations/Sysdig/2.png)

1. Then paste the copied link in the "URL" field and fill in the other details.

![](/img/Integrations/Sysdig/3.png)

1. Go to "Alerts" and select "Create alert" and add the required alert by filling in the required details.

![](/img/Integrations/Sysdig/4.png)

![](/img/Integrations/Sysdig/5.png)

![](/img/Integrations/Sysdig/6.png)

1. Now monitor the newly added alerts.

2. Sysdig is now integrated.
