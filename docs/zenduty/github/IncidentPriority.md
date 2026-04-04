---
id: IncidentPriority
title: Incident Priorities
---
Incident priority is the sequence in which an Incident or Problem needs to be resolved, based on Impact and Urgency. Priority also defines response and resolution targets associated with Service Level Agreements. Each team in Zenduty can define their own priorities like P0/P1/P2/P3 or L0/L4/L16 etc.

To setup incident priorities, go to your **Teams** page, click on "configure" next to your team. Go to the "Priorities" Tab and click on **Create Priority**. Select a priority name, description and color and click on "OK".

![](/img/Priority.png)

Once you've defined your priorities, go to **Services** tab under your team and for each service, go to the **Settings** tab and edit the **Default Incident Priority** for your service.

![](/img/Priority1.png)

![](/img/Priority2.png)

Once an incident is triggered, you can alter the priority from the Zenduty application or the Slack or iOS/Android apps as well.

![](/img/Priority3.png)

# Using incident priorities with alert rules

You can dynamically assign incident priorities to incoming incidents using Alert Rules. Go to your integrations page, click on the **Alert Rules** tab and create an alert rule. Set your conditions and in the **Actions** section, select **Assign Priority** and select the desired priority value to assign to your incident.

![](/img/Priority4.png)
