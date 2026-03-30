# Source: https://checklyhq.com/docs/communicate/status-pages/incidents.md

# Source: https://checklyhq.com/docs/communicate/dashboards/incidents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Incident & Maintenance messages

Using **Incidents** you can communicate outages and planned maintenance to your audience — customers, co-workers, partners —
or whoever might be lucky enough to visit one of your dashboards. This turns your dashboard into a status page!

Note that incidents are nested under dashboards. This means you can have multiple dashboards for different audiences (with
different custom domains). Use cases are:

1. You run an agency with multiple customers.
2. You have multiple internal teams, managing different services in your stack.
3. You have a staging and production environment you want to keep tabs on.

<Note>
  Incidents are only available on certain plans. For more details, see our [Pricing page](https://www.checklyhq.com/pricing).
</Note>

## Creating incidents

You can quickly create an incident directly from the [dashboard's overview page](https://app.checklyhq.com/dashes) and
publish it to your dashboard in seconds. Things might be on fire. You want to be quick!

<img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/dashboards-v2/create_incident.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=1bfc51aa4ad3487545653ac025e9a526" alt="create an incident" width="2438" height="796" data-path="images/docs/images/dashboards-v2/create_incident.png" />

## Incident types

You can create three types of incidents:

* **Major impact**: use this for breaking outages that have a major impact. Things are on fire.
* **Minor impact**: use this to indicate performance degradation, partial failures, etc.
* **Maintenance**: use this for typical planned maintenance. Nothing on fire, just letting you know.

Each type of incident will render differently on your dashboard, indicating a different level of severity.
Here is an example:

<img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/dashboards-v2/incidents_types.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=aaa98e3fb6fc154e91b252675adbccc4" alt="incident types major, minor, maintenance" width="1079" height="761" data-path="images/docs/images/dashboards-v2/incidents_types.png" />

## Incident updates

For the **major impact** and **minor impact** incidents, you can add updates as you resolve the matter at hand. At each
stage you can add an updated message, which will show up on your dashboard to keep your
audience in the loop.

It's very simple:

1. Pick the status with the slider: **Investigating**, **Identified**, **Monitoring** and **Resolved**.
2. Add some clarifying text in the **Update Message** text field.

You can edit any updates later to correct typos. You can also add more updates within the same category of updates, for
instance, if the "Investigating" phase is taking longer than expected and you want to post an update.

Here's an example of what that would look like while typing out the update messages.

<img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/dashboards-v2/incident_updates.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=884b8cc728cfb4ab914ba95fd87da90a" alt="updating an incident" width="1439" height="1014" data-path="images/docs/images/dashboards-v2/incident_updates.png" />

All incidents and their updates will show up on your dashboard (if you have Incidents enabled for the relevant dashboard)
in a chronological list for later reference.

<img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/dashboards-v2/dashboard_incident_list.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=158c0fa263f15be4625f2658715eb86e" alt="dashboard incident list" width="720" height="507" data-path="images/docs/images/dashboards-v2/dashboard_incident_list.png" />


Built with [Mintlify](https://mintlify.com).