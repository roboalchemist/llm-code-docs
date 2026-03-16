# Source: https://docs.rootly.com/incidents/incident-operations/web-creating-a-sub-incident.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Sub-Incidents via Web Interface

> Learn how to create sub-incidents through the Rootly web interface using the incident menu and creation form.

### How It Works

You can create a sub-incident directly from an existing incident in the Rootly web interface.\
This is useful when multiple teams need to investigate different parts of a larger incident while keeping everything linked and coordinated.

***

### Step 1 — Open the Sub-Incident Action

In any parent incident, click the **⋯ (More)** menu next to the incident title or status.\
You will see **Create Sub-Incident** when:

* The incident is **not already a sub-incident**
* The incident is **not a scheduled maintenance incident**
* You have **permission to create incidents**

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/creating-sub-incident/web-1.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=ffc2c1049c0c32617ed3b1af8562380a" alt="Create Sub-Incident from menu" width="902" height="398" data-path="images/creating-sub-incident/web-1.webp" />
</Frame>

***

### Step 2 — Complete the Sub-Incident Form

Selecting **Create Sub-Incident** opens the standard **New Incident** form.\
Rootly automatically injects a hidden `parent_incident_id`, ensuring the new incident is created as a sub-incident.

You can customize:

* Summary
* Severity
* Impacted services & functionalities
* Roles, assignees, and metadata
* Any fields defined in **Configuration → Forms & Fields**

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/creating-sub-incident/web-2.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=ebb0857bef7b558e5ae804f7bae4ffc1" alt="Sub-incident creation form" width="909" height="1242" data-path="images/creating-sub-incident/web-2.webp" />
</Frame>

Click **Create Incident** to finish.

***

### What Happens After Creation

Once saved:

* The new incident becomes a **sub-incident** of the parent
* Its **kind** is automatically derived (e.g., `normal_sub`, `scheduled_sub`)
* The parent incident displays a **Sub-Incidents** panel linking to all sub-incidents

<Info>
  Sub-incidents cannot themselves create further sub-incidents.\
  They represent the lowest level in an incident hierarchy.
</Info>

***

### Optional: Attach an Existing Incident as a Sub-Incident

If you already have an incident you want to convert into a sub-incident:

1. Open the child incident
2. Go to **⋯ → Attach to Parent Incident**
3. Choose a parent incident from the autocomplete search
4. Save

This option appears only when:

* The incident is **not already a sub-incident**
* It has **no sub-incidents of its own**
* You have permission to create incidents

***

### Best Practices

* **Use sub-incidents when multiple teams or domains are involved**\
  Helps isolate workstreams while maintaining a unified parent incident.

* **Keep naming clear and scoped**\
  Example: “Database Failover Sub-Incident (SRE)” or “Authentication Latency (Identity Team)”.

* **Enable workflows**\
  Many teams auto-assign roles, create tasks, or spin up Slack channels for sub-incidents.

* **Avoid unnecessary sub-incidents**\
  If the effort is small or tightly scoped, keep work in the main incident.

* **Review sub-incidents together during retrospectives**\
  They provide excellent insight into how different teams contributed to resolution.

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="I don’t see the 'Create Sub-Incident' option">
    This usually occurs when:

    * The incident is **already a sub-incident**
    * The incident is a **scheduled maintenance incident**
    * You lack **create incident** permissions
    * Your team has feature restrictions
  </Accordion>

  <Accordion title="I can't attach an existing incident to a parent">
    This happens if:

    * The incident **already has a parent**
    * It has its **own sub-incidents** (nested sub-incidents are not allowed)
    * The incident was created as **scheduled maintenance**
    * You don’t have adequate permissions
  </Accordion>

  <Accordion title="The wrong fields were inherited">
    Inheritance varies depending on:

    * Workflow automation
    * Feature flags (e.g., parent/sub synchronization)
    * Privacy rules
    * Origin of creation (Slack vs Web)
  </Accordion>

  <Accordion title="Timeline syncing is not working">
    Timeline sync requires:

    * `enable_parent_and_sub_incident_sync` feature flag
    * `parent_to_sub_incident_sync` enabled on the incident\
      Only **non-internal** timeline events sync across related incidents.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).