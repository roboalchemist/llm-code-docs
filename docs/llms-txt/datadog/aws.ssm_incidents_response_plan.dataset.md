# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_incidents_response_plan.dataset.md

---
title: Systems Manager Incidents Response Plan
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Systems Manager Incidents Response
  Plan
---

# Systems Manager Incidents Response Plan

This table represents the Systems Manager Incidents Response Plan resource from Amazon Web Services.

```
aws.ssm_incidents_response_plan
```

## Fields

| Title             | ID   | Type          | Data Type                                                                                                               | Description |
| ----------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string        |
| account_id        | core | string        |
| actions           | core | json          | The actions that this response plan takes at the beginning of the incident.                                             |
| arn               | core | string        | The ARN of the response plan.                                                                                           |
| chat_channel      | core | json          | The Chatbot chat channel used for collaboration during an incident.                                                     |
| engagements       | core | array<string> | The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident. |
| incident_template | core | json          | Details used to create the incident when using this response plan.                                                      |
| integrations      | core | json          | Information about third-party services integrated into the Incident Manager response plan.                              |
| name              | core | string        | The short format name of the response plan. The name can't contain spaces.                                              |
| tags              | core | hstore_csv    |
