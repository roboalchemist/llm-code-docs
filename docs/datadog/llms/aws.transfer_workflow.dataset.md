# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transfer_workflow.dataset.md

---
title: Transfer Family Workflow
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transfer Family Workflow
---

# Transfer Family Workflow

AWS Transfer Family Workflow is a managed resource that defines and automates file transfer processes within AWS Transfer Family. It allows you to create workflows that perform actions such as copying, tagging, or invoking AWS Lambda functions when files are uploaded or downloaded. This helps streamline data processing, enforce compliance, and integrate file transfers with other AWS services.

```
aws.transfer_workflow
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                         | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | Specifies the unique Amazon Resource Name (ARN) for the workflow.                                 |
| description        | core | string     | Specifies the text description for the workflow.                                                  |
| on_exception_steps | core | json       | Specifies the steps (actions) to take if errors are encountered during execution of the workflow. |
| steps              | core | json       | Specifies the details for the steps that are in the specified workflow.                           |
| tags               | core | hstore_csv |
| workflow_id        | core | string     | A unique identifier for the workflow.                                                             |
