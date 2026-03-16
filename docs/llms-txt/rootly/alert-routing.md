# Source: https://docs.rootly.com/alerts/alert-routing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Alert Routing

> Use Alert Routes to determine which teams, services, and escalation policies receive incoming alerts from your monitoring tools.

### Overview

Alert Routing ensures that alerts from your monitoring and observability systems reach the correct responders quickly and reliably. Rootly provides a unified routing layer that works across all alert sources, enabling consistent on-call workflows.

Rootly supports two routing pathways:

1. **Routing inside your monitoring tool** (Datadog, PagerDuty, Opsgenie, etc.)
2. **Routing inside Rootly** using centralized **Alert Routes**

This guide focuses on routing **inside Rootly**.

<Frame>
    <img src="https://mintcdn.com/rootly/QmdIMAh57EozQkVv/images/CleanShot2025-10-14at11.09.36@2x.png?fit=max&auto=format&n=QmdIMAh57EozQkVv&q=85&s=6b93c2b77dd3a4b7bce1b0167b6a8f5f" alt="Alert Routes page" width="2896" height="1794" data-path="images/CleanShot2025-10-14at11.09.36@2x.png" />
</Frame>

***

### What Is an Alert Route?

An **Alert Route** defines *when*, *how*, and *to whom* Rootly should send alerts. It supports evaluation against:

* Alert Sources
* Alert Fields (normalized metadata)
* Raw payload values (JSONPath)
* Teams, services, and escalation policies

<Info>
  **Tip:** Alert Routes work best when combined with **Alert Fields**, which let you write stable routing logic even when payload schemas vary across providers.
</Info>

***

### Creating an Alert Route

Navigate to **Alerts → Routes** and click **New Route**.

Each route requires:

#### Name

A descriptive title that clarifies the route’s purpose.

#### Alert Sources

Select one or more alert sources the route should evaluate.\
Sources can be added or removed at any time.

See all integrations → [Integrations Overview](/integrations/overview)

#### Owning Team

Controls who can edit the route.

<Note>
  **Permissions:**

  * Team Admins may only create routes **for their own team**.
  * Teams can only route alerts **from alert sources they own**.
</Note>

After creating a route, you can begin adding Routing Rules.

***

### Configuring Routing Rules

Routing Rules determine *which alerts should page responders* and *where they should go*.

Click **Add routing rule** to create one.

<Frame>
    <img src="https://mintcdn.com/rootly/nDfhzuVZYgleyNlU/images/CleanShot2025-10-14at11.49.35@2x.png?fit=max&auto=format&n=nDfhzuVZYgleyNlU&q=85&s=9303d54412c3b27741a1a51c65f58c7e" alt="Routing Rule creation" width="2896" height="1796" data-path="images/CleanShot2025-10-14at11.49.35@2x.png" />
</Frame>

***

### Routing Rule Conditions

Conditions define when a rule should trigger.

#### Select a Field

You may reference:

* **Alert Fields** (recommended)
* **Payload values via JSONPath**

<Info>
  Alert Fields ensure your routing logic remains stable even if payload structures change.
</Info>

<Frame>
    <img src="https://mintcdn.com/rootly/nDfhzuVZYgleyNlU/images/CleanShot2025-10-14at11.55.38@2x.png?fit=max&auto=format&n=nDfhzuVZYgleyNlU&q=85&s=100ccae779054b2522b88fd9c39ea01a" alt="Condition builder" width="1194" height="1270" data-path="images/CleanShot2025-10-14at11.55.38@2x.png" />
</Frame>

#### Choose an Operator

Supported operators include:

* *is one of*
* *contains*
* *starts with*
* *matches regex*
* *is empty*
* and more

<Tip>
  Use **regex** when values vary across alert providers and need flexible matching.
</Tip>

#### Add Additional Conditions

Use **AND/OR** groups to define complex routing logic.

#### Live Preview

Rootly shows matching historical alerts to validate your logic.

<Frame>
    <img src="https://mintcdn.com/rootly/nDfhzuVZYgleyNlU/images/CleanShot2025-10-15at09.38.17@2x.png?fit=max&auto=format&n=nDfhzuVZYgleyNlU&q=85&s=5c06eeb894a940fcb38f4645a5ccbfc1" alt="Matching alerts preview" width="2896" height="1800" data-path="images/CleanShot2025-10-15at09.38.17@2x.png" />
</Frame>

***

### Routing Rule Destinations

Each rule must specify **who receives the alert**. You may route alerts to:

* **Teams**
* **Services**
* **Escalation Policies**

Routing to a team or service automatically triggers its configured escalation policy.

<Tip>
  For easier reporting and maintenance, we recommend routing to **teams** or **services**, not directly to escalation policies.
</Tip>

Rules may include **multiple destinations**, all of which will be paged when the rule fires.

***

### Completing the Alert Route

A route may contain any number of rules.\
Rootly evaluates rules **top-to-bottom**, so ordering matters.

Use the rule menu (**… → Reorder rule**) to adjust order.

***

### How Rootly Routes Alerts

Rootly evaluates alerts in two sequential stages.

#### Stage 1 — Payload-Based Routing

If the alert payload contains a **target ID** (team or service), Rootly immediately routes the alert there without evaluating Alert Routes.

#### Stage 2 — Evaluate Alert Routes

If the alert does not specify a target:

#### Evaluate Routes

Rootly evaluates **every Alert Route associated with the alert’s source**.

#### Evaluate Rules

Within each route, rules are evaluated **from top to bottom**.

* The first matching rule triggers paging
* Rootly stops evaluating additional rules in that route
* Other routes referencing the same source will still run

<Warning>
  If no rules match, the alert becomes a **Non-Paging Alert**. Review these in the Alerts dashboard by filtering **Status → Non-Paging**.
</Warning>

<Frame>
    <img src="https://mintcdn.com/rootly/nDfhzuVZYgleyNlU/images/CleanShot2025-10-15at09.47.55@2x.png?fit=max&auto=format&n=nDfhzuVZYgleyNlU&q=85&s=26225a656d1eebfa1da2fce7d350a646" alt="Reordering rules" width="1654" height="934" data-path="images/CleanShot2025-10-15at09.47.55@2x.png" />
</Frame>

<Tip>
  Order rules **most specific → least specific** to avoid unintended matches.
</Tip>

***

### Alert Timeline

Every routed alert includes a timeline event documenting:

* Which **Alert Route** was applied
* Which **Routing Rule** matched
* Which **destinations** were paged

<Frame>
    <img src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/alerts/alert-timeline-routing.webp?fit=max&auto=format&n=R81sNIO9rI160XHL&q=85&s=834498a426b01d058fdbf0b5e36fd6c6" alt="Alert timeline routing" width="990" height="160" data-path="images/alerts/alert-timeline-routing.webp" />
</Frame>

This ensures responders understand *why* they were paged.

***

### Best Practices

* Prefer **Alert Fields** over JSONPath for stability.
* Start with broad routing categories and refine with specific rules.
* Keep rule names action-oriented and descriptive.
* Regularly check **Non-Paging Alerts** for routing gaps.
* Route to **teams/services**, not escalation policies, for better ownership.
* Combine routes thoughtfully when different teams own different tools.

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="My alert is not routing to anyone">
    * Ensure the alert source is included in at least one route.
    * Verify that at least one rule matches the alert.
    * Confirm the alert payload does not contain a `target_id`, which overrides routing.
  </Accordion>

  <Accordion title="The wrong rule is triggering">
    * Check the rule order; a broader rule may be matching first.
    * Validate operators and values used in conditions.
    * Ensure Alert Field mappings are extracting values correctly.
  </Accordion>

  <Accordion title="My alert is routing to too many destinations">
    * All routes referencing the alert source are evaluated.
    * Remove unnecessary alert sources from routes.
    * Tighten condition logic.
  </Accordion>

  <Accordion title="JSONPath conditions aren't matching the alert">
    * Review the alert payload preview (purple pill tokens).
    * Confirm your JSONPath reflects the actual alert structure.
    * Use Alert Fields whenever possible.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).