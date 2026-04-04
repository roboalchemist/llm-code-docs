# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.security_contact.dataset.md

---
title: Security Contact
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Security Contact
---

# Security Contact

Security Contact in Azure is a resource used to define security-related contact information for an Azure subscription or tenant. It allows administrators to specify email addresses and phone numbers that Microsoft can use to send security alerts, notifications, and important updates. This ensures that the right people are informed quickly about potential threats or incidents, helping organizations respond effectively to security issues.

```
azure.security_contact
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                      | Description |
| --------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| alert_notifications   | core | json       | Defines whether to send email notifications about new security alerts                                                                          |
| emails                | core | string     | List of email addresses which will get notifications from Microsoft Defender for Cloud by the configurations defined in this security contact. |
| id                    | core | string     | Resource Id                                                                                                                                    |
| location              | core | string     |
| name                  | core | string     | Resource name                                                                                                                                  |
| notifications_by_role | core | json       | Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.         |
| phone                 | core | string     | The security contact's phone number                                                                                                            |
| resource_group        | core | string     |
| subscription_id       | core | string     |
| subscription_name     | core | string     |
| tags                  | core | hstore_csv |
| type                  | core | string     | Resource type                                                                                                                                  |
