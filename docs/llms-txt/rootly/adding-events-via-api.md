# Source: https://docs.rootly.com/incidents/incident-timeline/adding-events-via-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Events to Timeline via API

> A detailed guide to adding timeline events programmatically using the Rootly API, including supported fields, common automation patterns, validation behavior, and best practices.

### Overview

The Rootly API allows you to automatically add timeline events from monitoring tools, CI/CD pipelines, automation systems, or any service that needs to record activity during an incident. This is ideal when you want to:

* Ensure key system activity is captured automatically
* Add highly structured or machine-generated data
* Record actions taken outside Slack or the Web UI
* Maintain a complete and auditable incident history
* Integrate internal tools directly into your incident process

API-created timeline events behave exactly the same as those added through Slack, email, or the Web UI. They appear chronologically, support visibility controls, and participate in analytics, retrospective preparation, and exports.

More details are available in the [API documentation](/api-reference/).

***

### Before You Begin

Before adding events through the API, ensure you have:

* A **Rootly API token** with permission to update incidents
* The **incident ID** for the timeline you want to write to
* Any IDs for context you plan to add later (services, functionalities, etc.)
* Awareness of your team’s required fields for timeline events (if applicable)
* The **Incident Events** API endpoint reference:

  `/api/v1/teams/:team_id/incidents/:incident_id/events`

<Tip>
  If you are unsure which fields your team requires, check **Configuration → Required Fields** or the incident’s form configuration.
</Tip>

***

### Adding a Timeline Event via API

<Steps>
  <Step title="Identify the target incident">
    You must know the incident ID, which you can obtain from:

    * The Web UI URL
    * The list-incidents API
    * A previously created incident response
    * A workflow-driven or system-triggered context

    All events you create will attach directly to this incident’s timeline.
  </Step>

  <Step title="Prepare your event fields">
    The API supports several top-level fields for constructing timeline entries:

    **Core fields**

    * Event text (the message shown in the timeline)
    * Visibility (internal-only or external/public)
    * Occurred time (when the event actually happened)
    * Starring (optional highlighting)

    **Impact fields (set after creation)**\
    These can be added after the event exists:

    * Affected services
    * Affected functionalities

    <Info>
      If you do not provide an occurred time, Rootly uses the creation timestamp automatically, ensuring correct chronological ordering.
    </Info>
  </Step>

  <Step title="Submit the API request">
    Any workflow engine, monitoring tool, or automation system can make the call using standard HTTP—CI/CD pipelines, serverless functions, alert processors, or internal services.

    The API will return the full event record, including IDs you can use for follow-up actions.
  </Step>

  <Step title="Attach optional service or functionality impact">
    After the event is created, you may optionally attach:

    * Impacted services
    * Impacted functionalities

    These attributes enrich the incident story and make root-cause and impact analysis clearer.
  </Step>

  <Step title="Verify the event in the timeline">
    Once created, the event appears immediately:

    * In the incident’s timeline UI
    * In Slack (if the incident channel displays timeline messages)
    * In exports and retrospectives
    * In API queries and analytics

    You can edit, star, or delete the event later if needed.
  </Step>
</Steps>

***

### What You Can Include in an API Timeline Event

You can capture a wide range of structured information through API events:

* Deployment summaries
* Automated rollback notices
* Monitoring alerts or anomaly detections
* CI/CD pipeline results
* Runbook or playbook execution steps
* Health check transitions
* Logs or metrics snapshots
* Notifications from internal tooling

<Info>
  API events support both internal-only and externally visible visibility settings, making them suitable for both responder-facing and customer-facing communications.
</Info>

***

### Validation & Error Behavior

Rootly uses consistent validation rules across Slack, email, the Web UI, and the API. When submitting an event programmatically, you may encounter:

**Unauthorized access**\
Occurs when the API token is missing or invalid.

**Forbidden actions**\
Triggered when the token does not have permission to modify the incident.

**Validation errors**\
May occur if required fields are missing, formats are invalid, or the incident cannot accept changes in its current lifecycle state.

**Incorrect incident ID**\
If the incident does not exist or cannot be accessed by your integration.

<Tip>
  Most validation failures can be resolved by verifying that the target incident exists, your API token has the correct permissions, and event text and visibility values match expected formats.
</Tip>

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="The event is not appearing in the timeline">
    Ensure the incident ID is correct and the API token has permission to update the incident.
  </Accordion>

  <Accordion title="The timeline order looks incorrect">
    Provide an explicit occurred time when backfilling or submitting historical events.
  </Accordion>

  <Accordion title="My system needs to attach impacted services">
    These are added after initial creation. First create the event, then attach services or functionalities using their respective endpoints.
  </Accordion>

  <Accordion title="The event does not appear on the external timeline">
    Verify that the visibility is set to external. Internal events are not displayed publicly.
  </Accordion>

  <Accordion title="I can’t delete or update events via API">
    Confirm that your token has update/delete permissions and that the event is editable (some system events are intentionally locked).
  </Accordion>
</AccordionGroup>

***

### Best Practices

* **Keep event messages concise**\
  The timeline should tell a clear, readable story.

* **Attach context after creation**\
  Tagging services and functionalities improves investigative clarity.

* **Automate high-frequency or system-driven updates**\
  Let your monitoring and tooling contribute directly to the timeline.

* **Avoid sending overly verbose machine logs**\
  Link to deeper logs instead of pasting large blocks of text.

* **Use explicit timestamps for backfilled entries**\
  This helps maintain an accurate historical sequence.

* **Maintain consistent formatting**\
  Standard phrasing (e.g., “Deployment started…”, “Alert triggered…”) improves readability in retrospectives.

* **Integrate with workflow-based automations**\
  API-created events can trigger or complement workflows for notifications, assignments, or analytics.


Built with [Mintlify](https://mintlify.com).