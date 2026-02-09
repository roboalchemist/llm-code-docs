# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_configuration_set.dataset.md

---
title: SES Configuration Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Configuration Set
---

# SES Configuration Set

An SES Configuration Set in AWS is a set of rules that you can apply to your Amazon Simple Email Service (SES) email sending. It allows you to control and monitor how emails are processed by defining event destinations such as CloudWatch, Kinesis Firehose, or SNS. This helps track metrics like bounces, complaints, and delivery, and enables advanced email sending features like reputation management and event publishing.

```
aws.ses_configuration_set
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                     | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| configuration_set  | core | json       | The configuration set object associated with the specified configuration set.                                 |
| delivery_options   | core | json       | Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). |
| event_destinations | core | json       | A list of event destinations associated with the configuration set.                                           |
| reputation_options | core | json       | An object that represents the reputation settings for the configuration set.                                  |
| tags               | core | hstore_csv |
| tracking_options   | core | json       | The name of the custom open and click tracking domain associated with the configuration set.                  |
