# Source: https://docs.rootly.com/managing-users/user-permissions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage User Permissions

> User permissions in Rootly are controlled by team-scoped roles for Incident Response and On-Call, allowing precise control over who can access, manage, and act on data.

## Overview

Permissions in Rootly are managed through **roles**, which determine what actions a user can perform within a team. Roles are intentionally **team-scoped** and **product-specific**, giving organizations fine-grained control over access.

Each team membership assigns **two roles** to a user:

* An **Incident Response role**, which governs incident creation, management, configuration, and analytics.
* An **On-Call role**, which governs alerting, paging, schedules, escalation policies, and responder workflows.

This separation allows teams to model real-world responsibilities. For example, a user may participate in incidents without being on-call, or be on-call without having permission to administer incident configuration.

When a user is added to a team, Rootly automatically assigns the team’s default roles for both Incident Response and On-Call. These defaults can be adjusted by administrators at any time.

<Note>
  Permissions are evaluated per team. A user may have different access levels across different teams within the same Rootly workspace.
</Note>

***

### Default Roles

Rootly ships with system-defined roles for both Incident Response and On-Call. These roles are created automatically for every team and cannot be deleted. Some roles are editable, while others are intentionally fixed.

#### Incident Response Roles

Incident Response includes the following default roles:

* Owner
* Admin
* User
* Observer
* No Access

<AccordionGroup>
  <Accordion title="Owner" icon="crown">
    Owners have full access to Incident Response. They can configure incident settings, manage workflows and integrations, access all incident data (including private incidents), and administer platform-level features such as billing.

    This role is typically reserved for platform owners or the core incident management team.
  </Accordion>

  <Accordion title="Admin" icon="shield-check">
    Admins can configure and manage most Incident Response features, including incident properties, workflows, retrospectives, and integrations.

    This role is ideal for teams responsible for maintaining and improving incident processes.
  </Accordion>

  <Accordion title="User" icon="user">
    Users are standard incident participants. They can respond to incidents, update incident details, assign roles, and collaborate during active incidents without having broad administrative permissions.
  </Accordion>

  <Accordion title="Observer" icon="eye">
    Observers primarily have read access but can still create incidents. This makes the role suitable for cross-functional teams such as support, operations, or customer success who need visibility into incidents.
  </Accordion>

  <Accordion title="No Access" icon="ban">
    No Access removes Incident Response permissions entirely for the team. This is useful when a user only needs On-Call access or should not interact with incidents in a given team.
  </Accordion>
</AccordionGroup>

***

#### On-Call Roles

On-Call includes a separate set of default roles:

* Admin
* User
* Observer
* No Access

In addition, On-Call supports **Custom roles** for more granular control.

<AccordionGroup>
  <Accordion title="Admin" icon="shield-check">
    On-Call Admins can manage schedules, escalation policies, routing rules, alert sources, and advanced features such as Live Call Routing and Heartbeats.

    They can also perform bulk actions on alerts, including changing alert status, marking alerts as noise, or deleting alerts.
  </Accordion>

  <Accordion title="User" icon="bell">
    On-Call Users are standard responders. They receive alerts, acknowledge them, resolve incidents, and participate in on-call rotations.
  </Accordion>

  <Accordion title="Observer" icon="eye">
    On-Call Observers have limited access but can typically initiate paging. This role is commonly used for teams that need to trigger alerts without managing on-call configuration.
  </Accordion>

  <Accordion title="No Access" icon="ban">
    No Access removes all On-Call permissions for the team. Users with this role will not receive alerts or interact with paging features.
  </Accordion>

  <Accordion title="Custom Roles" icon="sliders">
    Custom roles allow teams to define precise On-Call access, such as allowing alert acknowledgement without permission to edit schedules or escalation policies.
  </Accordion>
</AccordionGroup>

<Callout icon="info">
  On-Call does not include an **Owner** role. Administrative control is handled through **Admin** and **Custom roles**.
</Callout>

***

## Permission Sets

Permission sets define **what actions a role can perform on a specific entity**. Each permission set typically includes some combination of:

* Create
* Read
* Update
* Delete

Not all entities support all actions. Some include specialized actions beyond standard CRUD behavior.

### Incident Response Permission Sets

| Entity            | Description                                                                                                                                     | Links & Examples                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Alerts            | View and create alert events sent to Rootly from external sources. Alerts cannot be deleted. Status updates are handled by On-Call permissions. | [https://rootly.com/account/alerts](https://rootly.com/account/alerts)                                           |
| API Keys          | Manage API tokens used to authenticate with Rootly APIs.                                                                                        |                                                                                                                  |
| Audits            | View the audit log of configuration and permission changes.                                                                                     | [https://rootly.com/account/audits](https://rootly.com/account/audits)                                           |
| Causes            | Manage incident cause classifications used for analysis and reporting.                                                                          | [https://rootly.com/account/causes](https://rootly.com/account/causes)                                           |
| Custom Fields     | Manage custom incident fields used to capture additional metadata.                                                                              | [https://rootly.com/account/form-fields](https://rootly.com/account/form-fields)                                 |
| Environments      | Manage environment labels used to categorize incidents.                                                                                         | [https://rootly.com/account/environments](https://rootly.com/account/environments)                               |
| Functionalities   | Manage functionality labels representing impacted features or systems.                                                                          | [https://rootly.com/account/functionalities](https://rootly.com/account/functionalities)                         |
| Incident Feedback | Manage feedback collected during or after incident resolution.                                                                                  |                                                                                                                  |
| Incident Roles    | Define roles assigned to responders during incidents.                                                                                           | [https://rootly.com/account/incident-roles](https://rootly.com/account/incident-roles)                           |
| Incident Types    | Manage categories used to classify incidents.                                                                                                   | [https://rootly.com/account/incident-types](https://rootly.com/account/incident-types)                           |
| Incidents         | Manage public incident records, including status, severity, roles, and impacted services.                                                       | [https://rootly.com/account/incidents](https://rootly.com/account/incidents)                                     |
| Integrations      | Manage native integrations with external systems.                                                                                               | [https://rootly.com/account/integrations](https://rootly.com/account/integrations)                               |
| Invitations       | Invite users to join your Rootly workspace.                                                                                                     | [https://rootly.com/account/invitations](https://rootly.com/account/invitations)                                 |
| Playbooks         | Manage playbooks used during incidents.                                                                                                         | [https://rootly.com/account/playbooks](https://rootly.com/account/playbooks)                                     |
| Private Incidents | Manage private incidents with restricted visibility.                                                                                            |                                                                                                                  |
| Pulses            | Manage CI/CD and deployment events sent to Rootly.                                                                                              | [https://rootly.com/account/pulses](https://rootly.com/account/pulses)                                           |
| Retrospective     | Manage retrospective processes and templates.                                                                                                   | [https://rootly.com/account/retrospective-processes](https://rootly.com/account/retrospective-processes)         |
| Roles             | Manage Incident Response roles and permissions.                                                                                                 | [https://rootly.com/account/roles](https://rootly.com/account/roles)                                             |
| Teams             | Manage teams participating in incidents.                                                                                                        | [https://rootly.com/account/teams](https://rootly.com/account/teams)                                             |
| Secrets           | Manage secrets used securely in workflows.                                                                                                      | [https://rootly.com/account/secrets](https://rootly.com/account/secrets)                                         |
| Services          | Manage services associated with incidents.                                                                                                      | [https://rootly.com/account/services](https://rootly.com/account/services)                                       |
| Severities        | Manage severity levels used to classify incidents.                                                                                              | [https://rootly.com/account/severities](https://rootly.com/account/severities)                                   |
| Status Pages      | Manage Rootly-hosted status pages.                                                                                                              | [https://rootly.com/account/status-pages](https://rootly.com/account/status-pages)                               |
| Webhooks          | Manage outbound webhooks for incident and alert events.                                                                                         | [https://rootly.com/account/webhooks/outgoing/endpoints](https://rootly.com/account/webhooks/outgoing/endpoints) |
| Workflows         | Manage automation workflows triggered by incident events.                                                                                       | [https://rootly.com/account/workflows](https://rootly.com/account/workflows)                                     |

### On-Call Permission Sets

On-Call permission sets control **paging, alert handling, and responder operations**.\
These permissions determine how alerts are created, routed, escalated, acknowledged, and resolved, as well as who can configure the systems that support on-call coverage.

Unlike Incident Response permissions, On-Call permissions are focused on **real-time operational behavior** and responder availability.

| Entity                    | Description                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Alerts                    | Create, view, acknowledge, resolve, and re-trigger alerts. Controls the alert lifecycle once paging has begun. |
| Alert Groups              | Manage alert grouping rules used to reduce noise and consolidate related alerts.                               |
| Alert Sources             | Configure inbound alert sources and define how external alerts enter Rootly.                                   |
| Alert Routing Rules       | Define routing logic that determines which team, service, or escalation policy an alert is sent to.            |
| Alert Urgencies           | Manage urgency levels that control escalation behavior and notification intensity.                             |
| Schedules                 | Manage on-call schedules and rotations that determine who is on duty at any given time.                        |
| Schedule Overrides        | Create temporary overrides to adjust on-call coverage outside of normal rotations.                             |
| Escalation Policies       | Configure escalation paths, levels, repeat behavior, and working-hours logic for paging.                       |
| Live Call Routing         | Manage inbound phone numbers, IVR calling trees, voicemail behavior, and live call escalation.                 |
| Heartbeats                | Configure heartbeat monitors used to detect when systems stop checking in.                                     |
| On-Call Roles             | Manage On-Call roles and permission assignments for team members.                                              |
| On-Call Readiness Reports | View and manage reports that assess coverage, responsiveness, and on-call health.                              |
| Services                  | Manage services used for alert routing and ownership in on-call workflows.                                     |
| Teams                     | Manage teams used as alert routing targets and on-call ownership groups.                                       |
| Integrations              | Manage alerting and paging integrations (monitoring tools, incident systems, etc.).                            |
| Webhooks                  | Manage outbound webhooks that emit alert and on-call events.                                                   |
| API Keys                  | Manage API tokens used for on-call and alerting integrations.                                                  |

<Info>
  On-Call permissions govern **who gets paged and how alerts behave**.\
  They are evaluated independently from Incident Response permissions, which control incident records, workflows, and retrospectives.
</Info>

***

## Best Practices

* Assign the minimum permissions required for each role.
* Use Observers to provide visibility without administrative access.
* Separate Incident Response administration from On-Call ownership where possible.
* Restrict Private Incident access to a small, trusted group.
* Clearly document Custom On-Call roles so future administrators understand their intent.

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="A user can view alerts but cannot acknowledge or resolve them" icon="alert-triangle">
    This usually indicates missing On-Call permissions. Confirm the user’s On-Call role includes alert update access for the relevant team.
  </Accordion>

  <Accordion title="A user can page but cannot edit schedules or escalation policies" icon="calendar">
    Paging and configuration permissions are separate by design. Assign an On-Call role that includes schedule and escalation policy management if needed.
  </Accordion>

  <Accordion title="A user can see public incidents but not private incidents" icon="lock">
    Private incidents are controlled separately. Ensure the user’s Incident Response role includes **Private Incident** access for the team.
  </Accordion>

  <Accordion title="Role changes fail or revert unexpectedly" icon="refresh-cw">
    This may occur when seat limits are reached or when role assignments are managed through external identity systems such as SCIM.
  </Accordion>

  <Accordion title="A user has the correct role but still cannot perform an action" icon="help-circle">
    Confirm the user is operating in the correct team and that the permission applies to the correct product (Incident Response vs On-Call).
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).