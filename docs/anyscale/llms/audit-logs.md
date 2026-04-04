# Source: https://docs.anyscale.com/administration/security-and-compliance/audit-logs.md

# Audit logs

[View Markdown](/administration/security-and-compliance/audit-logs.md)

# Audit logs

This page provides an overview of audit logs on Anyscale.

## Enable audit logs[​](#enable-audit-logs "Direct link to Enable audit logs")

Anyscale doesn't enable audit logs by default. Audit logs aren't available on Anyscale-hosted clouds. Contact [Anyscale support](mailto:support@anyscale.com) to enable audit logging.

When you enable audit logging, you configure the following:

| Configuration    | Options                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Export location  | - S3 bucket<br />- Google Cloud Storage bucket<br />- Azure blob storage or ADLS container |
| Upload frequency | - Hourly<br />- Every 15 minutes                                                           |
| File format      | - JSONL (newline-separated JSON)<br />- Parquet                                            |

note

Anyscale supports audit log delivery to Azure storage for organizations enrolled in the Private Preview for Anyscale on Azure. See [Anyscale on AKS](/admin/azure/configure-aks.md).

## Log contents[​](#contents "Direct link to Log contents")

Anyscale uploads one file per entity on the configured frequency schedule. Anyscale outputs files to the following path within the object storage container:

```
/<org_id>/audit_logs/<entity>/<timestamp>.log.<file_format>
```

For example, `/org_123/audit_logs/job/1690300746.log.jsonl`.

Files consist of user action records. Records have the following schema:

```
{
   "timestamp": string,
   "user_id": string,
   "source_ip": string,
   "action": Action (enum), // see "Supported User Actions"
   "entity": Entity (enum), // see "Supported User Actions"
   "metadata": nullable object,
   "user": {
      "name": string,
      "email": string
   }
}
```

The following example record shows a user login:

```
{
   "timestamp": "2023-08-01 01:04:05.073682+00:00",
   "user_id": "usr_123",
   "source_ip": "1.2.3.4",
   "action": "LOGIN",
   "entity": "ACCESS",
   "metadata": null,
   "user": {
      "name": "Jane",
      "email": "jane@company.com"
   }
}
```

## Supported user actions[​](#user-actions "Direct link to Supported user actions")

The following table lists the logged user actions:

| Entity           | Action      | Metadata                                                                                  |
| ---------------- | ----------- | ----------------------------------------------------------------------------------------- |
| `USER`           | `INVITE`    | `invitee_email: string`                                                                   |
| `USER`           | `JOIN`      |                                                                                           |
| `USER`           | `REMOVE`    | `removee_id: string`                                                                      |
| `USER`           | `MODIFY`    | `modifee_id: string`, `old_role: string`, `new_role: string`                              |
| `PAYMENT`        | `ADD`       |                                                                                           |
| `ACCESS`         | `LOGIN`     |                                                                                           |
| `ACCESS`         | `LOGOUT`    |                                                                                           |
| `SUPPORT_ACCESS` | `LOGIN`     |                                                                                           |
| `SUPPORT_ACCESS` | `REQUEST`   | `duration: float` (seconds)                                                               |
| `BUDGET`         | `CREATE`    | `id: string`                                                                              |
| `BUDGET`         | `DELETE`    | `id: string`                                                                              |
| `BUDGET`         | `MODIFY`    | `id: string`, `is_enabled: boolean`, `budget_amount: string`, `evaluation_period: string` |
| `RESOURCE_QUOTA` | `CREATE`    | `id: string`                                                                              |
| `RESOURCE_QUOTA` | `DELETE`    | `id: string`                                                                              |
| `RESOURCE_QUOTA` | `MODIFY`    | `id: string`, `is_enabled: boolean`, `updated_resource_quota: dict`                       |
| `CLUSTER`        | `CREATE`    | `id: string`                                                                              |
| `CLUSTER`        | `START`     | `id: string`                                                                              |
| `CLUSTER`        | `TERMINATE` | `id: string`                                                                              |
| `CLUSTER`        | `ARCHIVE`   | `id: string`                                                                              |
| `CLOUD`          | `CREATE`    | `name: string`                                                                            |
| `CLOUD`          | `DELETE`    | `name: string`                                                                            |
| `CLUSTER_ENV`    | `CREATE`    | `name: string`                                                                            |
| `CLUSTER_ENV`    | `DELETE`    | `name: string`                                                                            |
| `COMPUTE_CONFIG` | `CREATE`    | `name: string`                                                                            |
| `JOB`            | `CREATE`    | `name: string`                                                                            |
| `JOB`            | `TERMINATE` | `name: string`                                                                            |
| `JOB`            | `ARCHIVE`   | `name: string`                                                                            |
| `SERVICE`        | `CREATE`    | `name: string`                                                                            |
| `SERVICE`        | `TERMINATE` | `name: string`                                                                            |
| `WORKSPACE`      | `CREATE`    | `name: string`                                                                            |
| `WORKSPACE`      | `START`     | `name: string`                                                                            |
| `WORKSPACE`      | `TERMINATE` | `name: string`                                                                            |
| `WORKSPACE`      | `DELETE`    | `name: string`                                                                            |
