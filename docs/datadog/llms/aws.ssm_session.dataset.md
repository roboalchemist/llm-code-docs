# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_session.dataset.md

---
title: Systems Manager Session
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Systems Manager Session
---

# Systems Manager Session

AWS Systems Manager Session provides a secure, interactive shell or remote desktop connection to your Amazon EC2 instances or on-premises servers without requiring inbound ports, bastion hosts, or SSH keys. It enables administrators to manage and troubleshoot systems directly through the AWS Management Console, CLI, or SDKs, improving security and simplifying access management.

```
aws.ssm_session
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                                | Description |
| -------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| access_type          | core | string     | Standard access type is the default for Session Manager sessions. JustInTime is the access type for Just-in-time node access.                            |
| account_id           | core | string     |
| details              | core | string     | Reserved for future use.                                                                                                                                 |
| document_name        | core | string     | The name of the Session Manager SSM document used to define the parameters and plugin settings for the session. For example, SSM-SessionManagerRunShell. |
| end_date             | core | timestamp  | The date and time, in ISO-8601 Extended format, when the session was terminated.                                                                         |
| max_session_duration | core | string     | The maximum duration of a session before it terminates.                                                                                                  |
| output_url           | core | json       | Reserved for future use.                                                                                                                                 |
| owner                | core | string     | The ID of the Amazon Web Services user that started the session.                                                                                         |
| reason               | core | string     | The reason for connecting to the instance.                                                                                                               |
| session_id           | core | string     | The ID of the session.                                                                                                                                   |
| start_date           | core | timestamp  | The date and time, in ISO-8601 Extended format, when the session began.                                                                                  |
| status               | core | string     | The status of the session. For example, "Connected" or "Terminated".                                                                                     |
| tags                 | core | hstore_csv |
| target               | core | string     | The managed node that the Session Manager session connected to.                                                                                          |
