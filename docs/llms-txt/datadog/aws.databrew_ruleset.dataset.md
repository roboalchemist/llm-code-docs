# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.databrew_ruleset.dataset.md

---
title: Glue DataBrew Ruleset Item
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Glue DataBrew Ruleset Item
---

# Glue DataBrew Ruleset Item

A Glue DataBrew Ruleset Item represents an individual data quality rule within a ruleset in AWS Glue DataBrew. It defines a specific validation or condition that data must meet, such as value ranges, formats, or uniqueness. These items help automate data profiling and quality checks, ensuring datasets meet required standards before further processing or analysis.

```
aws.databrew_ruleset
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                   | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     | The ID of the Amazon Web Services account that owns the ruleset.                            |
| create_date        | core | timestamp  | The date and time that the ruleset was created.                                             |
| created_by         | core | string     | The Amazon Resource Name (ARN) of the user who created the ruleset.                         |
| description        | core | string     | The description of the ruleset.                                                             |
| last_modified_by   | core | string     | The Amazon Resource Name (ARN) of the user who last modified the ruleset.                   |
| last_modified_date | core | timestamp  | The modification date and time of the ruleset.                                              |
| name               | core | string     | The name of the ruleset.                                                                    |
| resource_arn       | core | string     | The Amazon Resource Name (ARN) for the ruleset.                                             |
| rule_count         | core | int64      | The number of rules that are defined in the ruleset.                                        |
| tags               | core | hstore_csv |
| target_arn         | core | string     | The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with. |
