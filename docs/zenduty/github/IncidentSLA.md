---
id: IncidentSLA
title: Incident SLAs
---
Incident SLAs let you set acknowledgement and resolution SLAs for your incidents. SLAs allow your teams to prioritize incidents as well as increase transparency amongst incident stakeholders - support, account managers and management.

IMPORTANT: SLA alerts are sent to those notification rules that are set for time zero(immediate) for both high and low urgency incidents. If you'd like to receive SLA alerts on any contact channel, add that contact channel in your notification rule for time t=0(immediate)

To setup incident SLAs, go to your **Teams** page, click on "configure" next to your team. Go to the "SLA" Tab and click on **Create SLA**.

Select a SLA name, description and acknowledgement and resolution SLA times. Set the SLA alerts for when you'd like to receive an alert - before or after an acknowledgment or resolution SLA is about to be or has already been violated.

![](/img/SLA1.png)

![](/img/SLA2.png)

![](/img/SLA3.png)

Once you've defined your SLAs, go to **Services** tab under your team and for each service, go to the **Settings** tab and edit the **SLA Policy** for your service. This SLA policy will be applied by default to all your incidents.

![](/img/SLA4.png)

Once an incident is triggered, you can alter the incident SLA from the Zenduty application or the Slack or iOS/Android apps as well.

![](/img/SLA5.png)

# Assigning incident SLAs dynamically with alert rules

You can dynamically assign incident SLAs to incoming incidents using Alert Rules. Go to your integrations page, click on the **Alert Rules** tab and create an alert rule. Set your conditions and in the **Actions** section, select **Assign SLA** and select the desired SLA value to assign to your incident.

![](/img/SLA6.png)
