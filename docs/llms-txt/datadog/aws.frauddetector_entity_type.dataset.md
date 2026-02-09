# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_entity_type.dataset.md

---
title: Fraud Detector Entity Type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector Entity Type
---

# Fraud Detector Entity Type

Fraud Detector Entity Type in AWS defines the type of entity, such as a customer or account, that you want to evaluate for potential fraudulent activity. It helps structure fraud detection models by categorizing the subjects involved in transactions or events, enabling more accurate risk assessments and tailored detection logic.

```
aws.frauddetector_entity_type
```

## Fields

| Title             | ID   | Type       | Data Type                                           | Description |
| ----------------- | ---- | ---------- | --------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| arn               | core | string     | The entity type ARN.                                |
| created_time      | core | string     | Timestamp of when the entity type was created.      |
| description       | core | string     | The entity type description.                        |
| last_updated_time | core | string     | Timestamp of when the entity type was last updated. |
| name              | core | string     | The entity type name.                               |
| tags              | core | hstore_csv |
