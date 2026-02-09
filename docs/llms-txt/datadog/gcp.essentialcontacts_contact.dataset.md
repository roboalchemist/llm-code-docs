# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.essentialcontacts_contact.dataset.md

---
title: Essential Contacts Contact
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Essential Contacts Contact
---

# Essential Contacts Contact

Essential Contacts Contact in Google Cloud Platform is a resource that defines contact information for important notifications about a project or organization. It allows administrators to specify email addresses that receive alerts related to security, billing, and other critical updates. This ensures that the right people are informed about essential events and issues in a timely manner.

```
gcp.essentialcontacts_contact
```

## Fields

| Title                               | ID   | Type          | Data Type                                                                                                                                                                                                                                         | Description |
| ----------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string        |
| ancestors                           | core | array<string> |
| datadog_display_name                | core | string        |
| email                               | core | string        | Required. The email address to send notifications to. The email address does not need to be a Google Account.                                                                                                                                     |
| labels                              | core | array<string> |
| language_tag                        | core | string        | Required. The preferred language for notifications, as a ISO 639-1 language code. See [Supported languages](https://cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages) for a list of supported languages. |
| name                                | core | string        | Output only. The identifier for the contact. Format: {resource_type}/{resource_id}/contacts/{contact_id}                                                                                                                                          |
| notification_category_subscriptions | core | array<string> | Required. The categories of notifications that the contact will receive communications for.                                                                                                                                                       |
| organization_id                     | core | string        |
| parent                              | core | string        |
| project_id                          | core | string        |
| project_number                      | core | string        |
| region_id                           | core | string        |
| resource_name                       | core | string        |
| tags                                | core | hstore_csv    |
| validate_time                       | core | timestamp     | Output only. The last time the validation_state was updated, either manually or automatically. A contact is considered stale if its validation state was updated more than 1 year ago.                                                            |
| validation_state                    | core | string        | Output only. The validity of the contact. A contact is considered valid if it is the correct recipient for notifications for a particular resource.                                                                                               |
| zone_id                             | core | string        |
