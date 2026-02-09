# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workmail_organization.dataset.md

---
title: WorkMail Organization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > WorkMail Organization
---

# WorkMail Organization

WorkMail Organization in AWS represents a managed email and calendaring service for businesses. It provides secure, enterprise-grade email hosting with integration to existing corporate directories and support for common email clients. The organization resource contains details about the WorkMail setup, such as domain, directory, and status, enabling administrators to manage and monitor their organization's email environment.

```
aws.workmail_organization
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                        | Description |
| ------------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| alias                    | core | string     | The alias for an organization.                                                                                   |
| arn                      | core | string     | The Amazon Resource Name (ARN) of the organization.                                                              |
| completed_date           | core | timestamp  | The date at which the organization became usable in the WorkMail context, in UNIX epoch time format.             |
| default_mail_domain      | core | string     | The default mail domain associated with the organization.                                                        |
| directory_id             | core | string     | The identifier for the directory associated with an WorkMail organization.                                       |
| directory_type           | core | string     | The type of directory associated with the WorkMail organization.                                                 |
| error_message            | core | string     | (Optional) The error message indicating if unexpected behavior was encountered with regards to the organization. |
| interoperability_enabled | core | bool       | Indicates if interoperability is enabled for this organization.                                                  |
| migration_admin          | core | string     | The user ID of the migration admin if migration is enabled for the organization.                                 |
| organization_id          | core | string     | The identifier of an organization.                                                                               |
| state                    | core | string     | The state of an organization.                                                                                    |
| tags                     | core | hstore_csv |
