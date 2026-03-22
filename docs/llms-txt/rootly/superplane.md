# Source: https://docs.rootly.com/integrations/superplane.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Superplane

> Connect Rootly with Superplane to automate incident management workflows with triggers and actions.

## Why

**Superplane** Integration allows you to:

* Trigger automated workflows when incidents occur in Rootly
* Create, update, and retrieve incidents programmatically
* Add timeline events and annotations to incidents
* Build complex automation flows with dynamic expressions

## Triggers

### On Incident

Activates workflows when specific incident events occur in Rootly:

* Incident created
* Incident updated
* Incident mitigated
* Incident resolved
* Incident cancelled
* Incident deleted

The trigger automatically establishes a webhook endpoint managed by Superplane.

## Actions

### Create Incident

Generate new incidents programmatically with the following parameters:

* **Title** (required) - The incident title
* **Summary** (optional) - Description of the incident
* **Severity** (optional) - Severity level classification

### Get Incident

Retrieve comprehensive incident details including:

* Associated services and groups
* Action items
* Complete event histories

### Update Incident

Modify existing incident properties:

* Title and summary content
* Status and sub-status values
* Severity classification
* Associated services and teams
* Key-value label assignments

Returns confirmation data including the incident UUID, sequential ID, and modification timestamp.

### Create Event

Add timeline annotations and notes to incidents with visibility controls:

* **Internal** - Visible only to responders
* **External** - Visible on public status pages

## Installation

Visit [Superplane's Rootly component documentation](https://docs.superplane.com/components/rootly/) to configure the integration.

## Configuration

All configuration fields support dynamic expressions, enabling flexible automation based on incident data and external inputs.


Built with [Mintlify](https://mintlify.com).