# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_identity.dataset.md

---
title: SES Identity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Identity
---

# SES Identity

SES Identity in AWS represents an email address or domain that you verify to use with Amazon Simple Email Service. It includes attributes for DKIM configuration, custom MAIL FROM domain settings, and verification status. These attributes help ensure email authenticity, improve deliverability, and comply with sending requirements.

```
aws.ses_identity
```

## Fields

| Title                       | ID   | Type       | Data Type                                                      | Description |
| --------------------------- | ---- | ---------- | -------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| dkim_attributes             | core | string     | The DKIM attributes for an email address or a domain.          |
| identity                    | core | string     |
| mail_from_domain_attributes | core | string     | A map of identities to custom MAIL FROM attributes.            |
| tags                        | core | hstore_csv |
| verification_attributes     | core | string     | A map of Identities to IdentityVerificationAttributes objects. |
