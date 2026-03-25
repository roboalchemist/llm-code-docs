# Source: https://docs.rootly.com/incidents/creating-incidents/creating-incidents-via-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Incidents via API

> A step-by-step guide to creating incidents programmatically using the Rootly API, including supported fields, common automation patterns, validation behavior, and best practices.

### Overview

The Rootly API allows you to create incidents automatically from monitoring tools, CI/CD pipelines, internal services, or any external automation system. This is the preferred method when you need:

* Deterministic and repeatable incident creation
* Automated declarations from alerting or detection systems
* Consistent metadata applied across incidents
* The ability to create sub-incidents within orchestrated workflows
* Fully headless incident creation with no human intervention

API-based creation ensures incidents follow the same lifecycle rules, validations, and workflows as incidents created through Slack or the Web UI.

More details is available in the [API documentation](/api-reference/).

### Before You Begin

Before creating incidents via API, ensure you have:

* **A Rootly API token** with permissions to create incidents
* Knowledge of any **required fields** (severity, type, environments, etc.)
* IDs for any contextual fields you intend to populate:
  * Services
  * Functionalities
  * Environments
  * Groups
  * Incident types
  * Custom form fields
* The **Create Incident** endpoint reference:

  `POST /api/v1/incidents`

<Tip>
  To avoid validation failures, review which fields are required under **Configuration → Forms** and **Configuration → Required Fields.**
</Tip>

### Creating an Incident via API

<Steps>
  <Step title="Send a POST request to the Create Incident endpoint">
    Requests must include:

    ```
    POST /api/v1/incidents
    Authorization: Bearer <API_TOKEN>
    Content-Type: application/json

    ```

    Any HTTP client or automation system (Python, curl, Terraform, GitHub Actions, etc.) will work.
  </Step>

  <Step title="Include the required and optional fields">
    Below are the commonly used fields.

    **Core fields**

    * `title`
    * `summary`
    * `severity_id`
    * `incident_type_ids`
    * `private` (boolean)
    * `notify_emails` (array — used by workflows, not auto-emailed by default)

    **Contextual fields**

    * `service_ids`
    * `functionality_ids`
    * `environment_ids`
    * `group_ids`

    **Custom form fields**

    Use `form_field_selections_attributes` to populate custom data.

    Supports all field types: text, dropdowns, multi-select, relations, user selectors, catalog entities, etc.

    **Optional advanced fields**

    * `parent_incident_id` — creates a **sub-incident**
    * `create_test_incident` — only works if the **Test Incidents** feature is enabled
    * `mitigation_message`, `resolution_message`, `cancellation_message`
    * Lifecycle timestamps (advanced):
      * `in_triage_at`, `started_at`, `mitigated_at`, `resolved_at`, `closed_at`

    <Info>
      To create sub-incidents programmatically, provide `parent_incident_id`. Rootly automatically links the child to the parent.
    </Info>
  </Step>

  <Step title="Review the API response">
    A successful response includes:

    * The incident ID
    * Lifecycle status
    * Timestamps
    * A URL to open the incident in the web app
    * Slack channel details (if Slack is integrated + auto-create enabled)

    You can use these details to perform follow-up actions like:

    * Posting timeline entries
    * Updating lifecycle status
    * Attaching alerts
    * Triggering or monitoring workflows
  </Step>
</Steps>

### Example Request Payloads

**Basic example**

```
{
  "title": "API-declared service outage",
  "summary": "Automated alert from internal monitoring.",
  "severity_id": 1,
  "incident_type_ids": [3],
  "private": false
}
```

**With custom fields**

```
{
  "title": "Database latency above threshold",
  "summary": "DB p95 latency exceeded SLO for 10 minutes.",
  "severity_id": 0,
  "service_ids": [12],
  "environment_ids": [4],
  "form_field_selections_attributes": [
    {
      "form_field_id": 45,
      "value": "us-east-1"
    },
    {
      "form_field_id": 46,
      "selected_option_ids": [102]
    }
  ]
}
```

**Creating a sub-incident**

```
{
  "title": "Sub-incident: Cache layer investigation",
  "summary": "Investigating cache cluster behavior.",
  "severity_id": 2,
  "parent_incident_id": 1234,
  "service_ids": [18]
}
```

### Validation & Error Handling

Rootly returns standard error responses for debugging and automation safety.

**401 Unauthorized**

```
{
  "error": "unauthorized",
  "message": "Invalid or missing API token."
}
```

**403 Forbidden**

```
{
  "error": "forbidden",
  "message": "You do not have permission to create incidents."
}
```

**422 Validation Errors**

```
{
  "error": "unprocessable_entity",
  "message": "Validation failed.",
  "details": {
    "severity_id": ["can't be blank"],
    "title": ["can't be blank"]
  }
}
```

**Idempotency (Recommended)**

To prevent duplicate incidents during retries:

```
Idempotency-Key: <unique-key>
```

### Troubleshooting

<AccordionGroup>
  <Accordion title="“Missing required fields”">
    Ensure required fields in **Forms** or **Required Fields** are included.
  </Accordion>

  <Accordion title="“Workflows didn’t run”">
    Check that workflow conditions (severity, type, service, etc.) match the payload.
  </Accordion>

  <Accordion title="“Slack channel not created”">
    Verify:

    * Slack is connected
    * Auto-create channels is enabled
    * Incident is not private (depending on settings)
  </Accordion>

  <Accordion title="“Sub-incident didn’t link”">
    Make sure `parent_incident_id` is passed correctly.
  </Accordion>
</AccordionGroup>

### Best Practices

* Pre-fill key metadata to streamline response
* Use structured fields (services, environments, types) for better analytics
* Use private incidents for security-sensitive or customer-specific events
* Follow consistent naming conventions across automated incidents
* Use idempotency keys to prevent duplication
* Automate creation of sub-incidents for multi-team or multi-domain issues
* Avoid manually setting lifecycle timestamps unless necessary


Built with [Mintlify](https://mintlify.com).