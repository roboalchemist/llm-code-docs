# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.resourcegroups_group.dataset.md

---
title: Resource Groups Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Resource Groups Group
---

# Resource Groups Group

Resource Groups Group in AWS represents a collection of AWS resources that are grouped together for easier management and organization. Using this resource, you can define logical groupings based on tags or CloudFormation stacks, making it simpler to apply automation, monitoring, and access control across multiple resources at once. It helps streamline operations by allowing you to manage related resources as a single unit.

```
aws.resourcegroups_group
```

## Fields

| Title           | ID   | Type       | Data Type                                                                                                                                            | Description |
| --------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| application_tag | core | hstore     | A tag that defines the application group membership. This tag is only supported for application groups.                                              |
| criticality     | core | int64      | The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.   |
| description     | core | string     | The description of the resource group.                                                                                                               |
| group_arn       | core | string     | The Amazon resource name (ARN) of the resource group.                                                                                                |
| name            | core | string     | The name of the resource group.                                                                                                                      |
| owner           | core | string     | A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization. |
| tags            | core | hstore_csv |
