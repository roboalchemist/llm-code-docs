# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotwireless_destination.dataset.md

---
title: Iotwireless Destination
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iotwireless Destination
---

# Iotwireless Destination

This table represents the iotwireless_destination resource from Amazon Web Services.

```
aws.iotwireless_destination
```

## Fields

| Title           | ID   | Type       | Data Type                                                | Description |
| --------------- | ---- | ---------- | -------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| arn             | core | string     | The Amazon Resource Name of the resource.                |
| description     | core | string     | The description of the resource.                         |
| expression      | core | string     | The rule name or topic rule to send messages to.         |
| expression_type | core | string     | The type of value in <code>Expression</code>.            |
| name            | core | string     | The name of the resource.                                |
| role_arn        | core | string     | The ARN of the IAM Role that authorizes the destination. |
| tags            | core | hstore_csv |
