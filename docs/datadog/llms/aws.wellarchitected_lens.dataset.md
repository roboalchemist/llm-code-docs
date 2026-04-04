# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.wellarchitected_lens.dataset.md

---
title: AWS Well-Architected Lens
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS Well-Architected Lens
---

# AWS Well-Architected Lens

AWS Well-Architected Lens is a framework component that helps evaluate and improve cloud workloads based on AWS best practices. It provides structured guidance through lenses that focus on specific technology domains or industry scenarios. Each lens includes questions, design principles, and improvement plans to assess architecture alignment with operational excellence, security, reliability, performance efficiency, and cost optimization.

```
aws.wellarchitected_lens
```

## Fields

| Title               | ID   | Type       | Data Type                                              | Description |
| ------------------- | ---- | ---------- | ------------------------------------------------------ | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| description         | core | string     | The description of the lens.                           |
| lens_arn            | core | string     | The ARN of a lens.                                     |
| lens_version        | core | string     | The version of a lens.                                 |
| name                | core | string     | The full name of the lens.                             |
| owner               | core | string     | The Amazon Web Services account ID that owns the lens. |
| share_invitation_id | core | string     | The ID assigned to the share invitation.               |
| tags                | core | hstore_csv |
