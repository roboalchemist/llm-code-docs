# Source: https://docs.rootly.com/incidents/incidents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Understand how Rootly streamlines incident response through automated detection, paging, triage, and response workflows across your entire incident lifecycle.

## How Rootly Works

Rootly provides an end-to-end incident management platform that helps your teams detect issues quickly, coordinate a response, and learn from every incident. This page walks through the main phases of the incident lifecycle in Rootly and points you to where each phase lives in the product and documentation.

### Incident Lifecycle at a Glance

Most teams move through a common flow:

1. Detect a potential issue from alerts.
2. Create an incident (manually or automatically).
3. Triage and understand impact.
4. Coordinate a response across teams.
5. Resolve the incident.
6. Run a retrospective and track follow-ups.
7. Use analytics to improve over time.

Each of these phases maps to specific areas in Rootly, described below.

### Detection & Alerting

Rootly starts working as soon as your monitoring or observability tools notice something is wrong. You can connect sources like Datadog, Grafana, Sentry, cloud provider alerts, or any system capable of sending webhooks.

Once connected, alerts flow into Rootly and can:

* Create incidents automatically based on your rules.
* Attach to existing incidents to provide additional context.
* Drive paging via your escalation policies.

To learn more about setting up detection, look for the [**Alert Sources**](/alerts/alerts) and [**Integrations**](https://docs.rootly.com/integrations/overview) documentation.

<Info>
  Use **Alert Sources** to connect monitoring tools and define which alerts should create or update incidents.
</Info>

### Creating Incidents

Incidents are the core record of “something is wrong” in Rootly. You can create them:

* Manually from the UI (for example when someone reports an issue in Slack or via support).
* Automatically from alerts when certain conditions are met.
* Via automations or external systems (Slack commands, CI/CD pipelines, etc.).

When a new incident is opened, Rootly prompts you for key **incident properties** such as severity, impacted service, type, and any custom fields your team has defined. These properties drive workflows, routing, and reporting later.

For more detail, see the [**Creating Incidents**](/incidents/creating-incidents/creating-incidents-via-web-ui) documentation.

### Triage & Assess

Once an incident exists, the first step is understanding how bad it is and who needs to be involved. On the incident detail page, responders can:

* Update **status** (for example: Open, In Triage, Mitigated, Resolved).
* Adjust **severity** and affected **services** to reflect impact.
* Attach related alerts and signals.
* Assign an **incident commander** and other roles.
* Capture notes, hypotheses, and decisions in one place.

This is also where you will see the evolving **incident timeline**, including changes, assignments, notifications, and actions taken.

Look for the [**Incident Lifecycle**](/incidents/incident-lifecycle) and **Triage Incidents** docs for a deeper dive into statuses, roles, and best practices.

<Info>
  Most lifecycle actions—status changes, severity updates, assignments, and alert attachments—live on the **Incident Detail** page.
</Info>

### Respond & Coordinate

During an active incident, Rootly helps keep everyone aligned and reduces manual coordination work.

Typical activities include:

* Synchronizing updates to Slack or other chat tools.
* Notifying stakeholders and leadership on a predictable cadence.
* Posting updates to status pages.
* Creating and tracking action items or tasks.
* Running automation (for example, calling runbooks or external tools).

This behavior is usually powered by **Workflows** that react to incident events (like “status changed to Mitigated” or “severity is SEV0”) and perform actions for you.

To see what’s possible, explore the [**Workflows**](https://docs.rootly.com/workflows/workflows) and [**Communication & Notifications** ](https://docs.rootly.com/notifications/getting-started)documentation.

<Info>
  Workflows are a powerful way to standardize how your organization responds to incidents, without responders having to remember every step manually.
</Info>

### Resolve the Incident

When the underlying issue has been mitigated or fully fixed, the incident is moved to a **Resolved** state.

At this point, Rootly can:

* Run “on-resolve” workflows (for example, notify stakeholders, close tickets, or clean up temporary channels).
* Enforce required fields, such as root cause, impact summary, or customer communication notes.
* Trigger the creation of a retrospective automatically based on your rules.

If you want to control what must be filled out before resolution, see the **Incident Properties** or **Required Fields** documentation.

<Info>
  Many teams configure a workflow that automatically creates a retrospective when an incident’s status changes to **Resolved**.
</Info>

### Retrospectives

After resolution, the focus shifts to learning. Rootly’s **Retrospectives** provide a structured way to:

* Document what happened and when.
* Capture contributing factors and underlying causes.
* Record customer impact and communication.
* Create and assign follow-up actions.
* Share outcomes with stakeholders.

Retrospectives are linked directly to the incident and use the same properties (like service and severity) so they can be analyzed alongside other incidents.

To learn more about templates, workflows, and best practices, see the [**Retrospectives**](/retrospectives/retrospectives) documentation.

<Info>
  Rootly uses the term **Retrospective** instead of “postmortem,” but you can mirror whatever language your team prefers in templates and forms.
</Info>

### Analytics & Insights

Rootly automatically records every incident, alert, and lifecycle change so you can answer questions like:

* How quickly do we detect and resolve incidents (MTTD, MTTR)?
* Which services or teams are seeing the most incidents?
* Are certain severities increasing over time?
* Are retrospectives being completed and action items followed up?

The **Incident Analytics** documentation explains the available dashboards, filters, and metrics, and how to slice your data by properties such as service, severity, or type.

### Incident Properties

Incident properties are the fields that describe an incident and drive automation. They can be:

* **Built-in fields** like title, severity, status, and impacted services.
* **Custom fields** defined by your organization (for example, customer segment, region, product area, or incident type).

These properties are used to:

* Categorize and filter incidents during triage.
* Power workflow conditions (for example, “page leadership when severity is SEV0”).
* Enforce required information at different lifecycle stages.
* Break down analytics by whichever dimensions matter to you.

You can manage and customize these fields in the **Incident Properties / Form Fields** settings, and you can read more in the dedicated [**Incident Properties** ](/configuration/configuration)documentation.

<Info>
  A common pattern is to start with a simple set of properties (severity, service, type) and expand over time as analytics needs become clearer.
</Info>

### Where to Go Next

If you’re just getting started, here are good follow-up pages to link from here:

* [**Incidents**](/incidents/creating-incidents/creating-incidents-via-web-ui) – how to create, view, and manage incidents.
* [**Alert Sources**](/integrations/datadog/alerts) – how to connect monitoring tools and route alerts.
* [**Workflows**](https://docs.rootly.com/workflows/workflows) – how to automate response and communications.
* [**Retrospectives**](/retrospectives/retrospectives) – how to document and learn from incidents.
* [**Incident Analytics**](/metrics/default-metrics) – how to measure and improve your reliability.
* [**Incident Properties** ](/configuration/configuration)– how to define the fields that structure your incidents.

### FAQ

<AccordionGroup>
  <Accordion title="How do incidents get created in Rootly?" iconType="thin">
    Incidents can be created manually from the UI, automatically from alerts, through workflows, or from external tools like Slack or CI/CD pipelines. See **Incidents** or [**Alert Sources**](/alerts/alerts) to learn more.
  </Accordion>

  <Accordion title="When should I use workflows?">
    Use workflows to automate repetitive tasks—paging responders, posting Slack updates, syncing status pages, creating tickets, assigning roles, or creating retrospectives.
  </Accordion>

  <Accordion title="Do incidents have different severities or types?">
    Yes. Severity, type, impacted service, and other fields are all customizable through **Incident Properties** and can be used to drive workflows or analytics.
  </Accordion>

  <Accordion title="What is the difference between alerts and incidents?">
    Alerts are incoming signals from monitoring tools. Incidents are the structured record Rootly creates to track and manage an issue. Multiple alerts can attach to the same incident.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).