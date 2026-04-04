# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediaconnect_flow.dataset.md

---
title: Elemental MediaConnect Flow
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaConnect Flow
---

# Elemental MediaConnect Flow

Elemental MediaConnect Flow in AWS is a managed service resource that enables the transport of live video streams with high reliability and security. It allows you to ingest, distribute, and share live video content across partners, regions, or workflows without needing to build custom video transport infrastructure. This resource represents the configuration and state of a live video flow, including its sources, outputs, and entitlements.

```
aws.mediaconnect_flow
```

## Fields

| Title      | ID   | Type       | Data Type                                                                                                                      | Description |
| ---------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| flow       | core | json       | The flow that you requested a description of.                                                                                  |
| messages   | core | json       | Any errors that apply currently to the flow. If there are no errors, MediaConnect will not include this field in the response. |
| tags       | core | hstore_csv |
