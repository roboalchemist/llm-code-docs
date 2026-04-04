# Source: https://docs.datadoghq.com/incident_response/incident_management/incident_settings/property_fields.md

---
title: Property Fields
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Incident Response > Incident Management > Incident Settings > Property
  Fields
---

# Property Fields

## Overview{% #overview %}

Custom property fields enable you to capture important attributes unique to your organization, such as specific product models in the automotive industry or unique codes in a software deployment. These attributes help you efficiently categorize incidents.

You can use custom fields to filter for specific subsets of incidents on the [Incident Management](https://app.datadoghq.com/incidents) page and in [Incident Management Analytics](https://docs.datadoghq.com/incident_response/incident_management/analytics). You can also build conditions around custom fields in [incident notification rules](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules).

## Field sections{% #field-sections %}

Property fields are organized into three tables that correspond to where the fields appear in the [Overview tab](https://docs.datadoghq.com/incident_response/incident_management/investigate#overview-tab) of the Incident Details page:

1. `What Happened`
1. `Why It Happened`
1. `Attributes`

You can move or reorder property fields by dragging them using the drag handle icon.

## Default fields{% #default-fields %}

There are five default fields:

| Fields                    | Description                                                                                                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Detection Method** | Add context on how this incident was declared.                                                                                                                                                         |
| **Summary**               | Provide details on what happened to cause this incident.                                                                                                                                               |
| **Root Cause**       | List possible root causes or areas for investigation.                                                                                                                                                  |
| **Services**              | If you have [Datadog APM](https://docs.datadoghq.com/tracing/) configured, the `Services` property field automatically uses your APM Service names. To add values to `Services`, you can upload a CSV. |
| **Teams**                 | The `Teams` property field automatically populates from the [teams](https://docs.datadoghq.com/account_management/teams/) defined in your organization.                                                |

**Note**: You cannot delete default fields.

### Field types{% #field-types %}

You can define new fields of any of the following field types:

{% dl %}

{% dt %}
**Single Select**
{% /dt %}

{% dd %}
A dropdown that accepts one value. You set the available values when defining the field.
{% /dd %}

{% dt %}
**Multi Select**
{% /dt %}

{% dd %}
A dropdown that accepts multiple values. You set the available values when defining the field.
{% /dd %}

{% dt %}
**Text Array**
{% /dt %}

{% dd %}
A free-form field that accepts multiple values. Incident responders set arbitrary values when setting the field on an incident.
{% /dd %}

{% dt %}
**Text Area**
{% /dt %}

{% dd %}
A free-form text box that accepts a single value. Incident responders set arbitrary values when setting the field on an incident.
{% /dd %}

{% dt %}
**Metric Tag**
{% /dt %}

{% dd %}
A dropdown that accepts multiple values. Incident responders are prompted to select any ingested values of the metric tag you select when defining the field.
{% /dd %}

{% dt %}
**Number**
{% /dt %}

{% dd %}
Accepts any integer or decimal number.
{% /dd %}

{% dt %}
**Datetime**
{% /dt %}

{% dd %}
Accepts any datetime. Values are stored in UTC and are parsed and formatted using the user's local timezone.
{% /dd %}

{% /dl %}

### Field names{% #field-names %}

A field's name is a snake-case identifier used in [search and analytics queries](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/property_fields#custom-fields-in-search-and-analytics), [Workflow automations](https://docs.datadoghq.com/actions/workflows/), and APIs. Its display name is a user-friendly label that determines how the field appears in an [incident's overview page](https://docs.datadoghq.com/incident_response/incident_management/investigate#overview-tab), an [incident's timeline](https://docs.datadoghq.com/incident_response/incident_management/investigate/timeline), and the [incident declaration modal](https://docs.datadoghq.com/incident_response/incident_management/declare).

### Required at declaration{% #required-at-declaration %}

If you mark a field as "Required at Declaration," users are required to enter a value when declaring incidents. This option does not affect Datadog Workflow automations or API requests.

### Prompt user{% #prompt-user %}

Incident Management can be configured to prompt responders to set particular fields when changing the incident's state. To set this behavior for a field, edit the field's "Prompt user" option.

**During declaration**: Users are prompted to enter a value for the field during declaration and at all state changes if the field is empty.

**When the incident is moved to Stable/Resolved/Completed**: Users are prompted to enter a value for the field when moving the incident to the selected state and any later state. For example, if you select "When the incident is moved to Stable," users are prompted to fill out the field when moving incidents to Stable, Resolved, or Completed.

### Custom fields in search and analytics{% #custom-fields-in-search-and-analytics %}

Single-Select, Multi-Select, Text Array, Number, and Datetime fields are searchable facets in the [Incident Homepage](https://app.datadoghq.com/incidents) and [Incident Management Analytics](https://docs.datadoghq.com/incident_response/incident_management/analytics).

In Incident Management Analytics, number fields appear as measures that can be graphed and visualized in [Dashboards](https://docs.datadoghq.com/dashboards/) and [Notebooks](https://docs.datadoghq.com/notebooks/).
