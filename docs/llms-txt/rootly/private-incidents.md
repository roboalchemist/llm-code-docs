# Source: https://docs.rootly.com/incidents/private-incidents/private-incidents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Private Incidents Overview

> Learn how private incidents work in Rootly, how access is granted beyond RBAC using incident-level permissions, and how to manage access through both the Web UI and Slack.

### What Are Private Incidents?

Private incidents allow sensitive operational, customer, or security-related information to be restricted to a limited group of responders.\
Unlike standard incidents—where visibility is governed solely by workspace-wide RBAC—**private incidents add a second layer of access control**.

In Rootly, users may gain access to a private incident in two ways:

1. **RBAC permissions**\
   A user whose role grants *private incident read access* can view all private incidents.

2. **Incident-level invitation (subscriber-level access)**\
   Even if a user does *not* have role-based permission, they can still be added as a responder through the **Manage Access** dialog (Web or Slack).\
   This provides **incident-specific access on top of RBAC**.

<Info>
  Private incident access is additive.\
  A user either needs (A) role-based private-incident permissions **or** (B) to be explicitly added as a subscriber to the incident.
</Info>

Rootly exposes simple controls for managing access through both the Web interface and Slack. These tools allow incident commanders to invite additional responders quickly while maintaining strict visibility boundaries.

***

### When to Use Private Incidents

Private incidents are commonly used for:

* Security or privacy-related investigations
* Customer-impacting issues involving sensitive data
* Vendor or partner escalations
* Production outages requiring access to confidential systems or dashboards
* Internal-only discussions during high-severity events

Because access is tightly controlled, private incidents ensure the right responders are looped in without exposing sensitive information to the entire organization.

***

### How to Manage Access

Rootly provides dedicated access-management flows in **both the Web UI** and **Slack**, ensuring responders can add or remove users without breaking focus.

<CardGroup cols={2}>
  <Card title="Manage Access via Web" icon="globe" href="/incidents/private-incidents/manage-via-web">
    Use the Web interface to add or remove subscribers, bulk-edit access, and review current authorized users.
  </Card>

  <Card title="Manage Access via Slack" icon="slack" href="/incidents/private-incidents/manage-via-slack">
    Update access directly from the incident channel using `/rootly manage`, `/rootly access`, or the Manage Access button.
  </Card>
</CardGroup>

***

### How Access Updates Work Behind the Scenes

Rootly performs several automated steps when you update access:

#### Adding a User

* They are added as an **authorized subscriber** to the private incident.
* If Slack is integrated, Rootly automatically attempts to **invite them to the incident channel**.
* They immediately gain permission to view private incident details in the Web UI and API.

#### Removing a User

* They are removed from the incident’s subscriber list.
* If Slack permissions allow it, they are **removed from the incident’s Slack channel**.
* They lose access to incident details, timeline, roles, and integrations.

<Warning>
  Slack workspace restrictions may prevent Rootly from removing users from channels.\
  In those cases, Rootly removes incident access but Slack may reject channel removal.
</Warning>

#### “Remove Unauthenticated Users”

If selected in Slack or the Web UI, Rootly will:

* Remove anyone who **does not have private-incident read permissions**,\
  *even if they were manually added previously*.

This is typically used to quickly sanitize membership during sensitive investigations.

***

### Best Practices for Private Incidents

* **Limit access to essential responders only**\
  Fewer participants reduce noise and risk when working with sensitive information.

* **Grant subscriber access proactively**\
  When involving teams like Legal, Security, or Support, add them early via the Manage Access dialog.

* **Use Slack for quick changes, Web UI for structured updates**\
  Slack is ideal for rapid response.\
  The Web UI is better for reviewing and bulk-editing access.

* **Regularly audit access during long-running incidents**\
  Make sure only the necessary responders continue to have access.

* **Use workflows for automatic access control**\
  Add on-call engineers, service owners, or leadership automatically for critical severities.

***

### FAQ

<AccordionGroup>
  <Accordion title="Do private incidents override RBAC?">
    No. Private incidents **add** incident-level permissions on top of RBAC.\
    Users with the correct role can see all private incidents. Others must be explicitly added.
  </Accordion>

  <Accordion title="Can someone without private-incident permissions join a private incident?">
    Yes—if they are added as a subscriber through the Manage Access dialog (Web or Slack).
  </Accordion>

  <Accordion title="Will Slack notify a user after they’re removed?">
    Slack may send a notification, but this depends on workspace settings.\
    Rootly attempts removal, but Slack may reject the action if workspace policies prevent it.
  </Accordion>

  <Accordion title="Why do some users appear or disappear from the Slack access modal?">
    The modal shows all current subscribers and allows searching for any workspace user.\
    Users may disappear automatically if “Remove Unauthenticated Users” was selected.
  </Accordion>

  <Accordion title="What happens if Slack cannot remove a user from the channel?">
    Rootly removes their incident access, but Slack may block channel removal based on workspace permissions.
  </Accordion>

  <Accordion title="Does access sync to sub-incidents?">
    If your workspace enables parent–child syncing, access changes (invites and removals) may propagate to linked sub-incidents.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).