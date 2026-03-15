# Source: https://docs.firehydrant.com/docs/incident-roles.md

# Incident Roles

Incident roles help align responders behind a clear set of tasks, responsibilities, and expectations. They also help responders stay organized during stressful situations where many things need to get done.

> 📘 Note:
>
> This is not to be confused with [FireHydrant user access roles](https://docs.firehydrant.com/docs/role-based-access-controls)

## Default Roles

<Image alt="Example incident roles page" align="center" src="https://files.readme.io/5eb00e2-Screenshot_2023-12-11_at_11.34.15_AM.png">
  Example incident roles page
</Image>

FireHydrant ships with several roles out-of-box, but they can be customized, deleted, or otherwise adjusted per your organization's needs.

* **Commander**
  * Generally, the Incident Commander holds the high-level view of the incident and organizes the response. This may involve pulling in the right stakeholders, facilitating communications, and otherwise ensuring the team stays on track and knows what they need to do.
* **Ops Lead**
  * The Ops Lead is generally a responder who jumps in and handles the technical work of mitigating the incident. This could include restarting servers, browsing and fetching logs, or any other deep technical work. Ops Leads often include SMEs or specific service owners.
* **Communication**
  * The Communications role generally consists of people responsible for following along with the incident, distilling updates, and then facilitating external communications to customers. This could include email, status page, messaging, or other comms as required.
* **Planning**
  * Sometimes, more complex incidents or long-running incidents may require additional help. We think of planners as an additional support role that helps facilitate things like creating Follow-Ups, arranging hand-offs, or other work as required.

## Customize roles

1. Navigate to **Settings> Incidents > Roles**.
2. On the Roles page, click "+ Add role" if creating a new role, or click on the role in question if editing an existing role.
3. Provide/edit the name, summary, and description for the role, then click **Save**.
   * The **Name** and **Summary** fields will be shown to users via a direct message in Slack when assigned during an incident.

<Image alt="Example Slack DM from FireHydrant when assigned a role and/or task list" align="center" src="https://files.readme.io/e6523e6-Screenshot_2023-12-11_at_11.36.48_AM.png">
  Example Slack DM from FireHydrant when assigned a role and/or task list
</Image>

## Next Steps

Once you've customized incident roles to your preferences:

* See how to [assign roles](https://docs.firehydrant.com/docs/adding-responders) during an incident
* You can also designate [default roles](https://docs.firehydrant.com/docs/team-management) for individuals/on-call people on teams
* Assign [lists of pre-defined tasks](https://docs.firehydrant.com/docs/managing-tasks) to specific roles on incidents to further cut down on toil