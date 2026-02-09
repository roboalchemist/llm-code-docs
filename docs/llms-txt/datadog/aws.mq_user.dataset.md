# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mq_user.dataset.md

---
title: MQ User
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MQ User
---

# MQ User

An AWS MQ User represents a user account within an Amazon MQ broker. It defines the authentication credentials and permissions that allow clients to connect securely to the broker. Users can be configured with specific access rights, such as read or write permissions, to control how they interact with queues and topics. This helps manage secure communication and message flow between applications using the broker.

```
aws.mq_user
```

## Fields

| Title            | ID   | Type          | Data Type                                                                                                                                                                                                              | Description |
| ---------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string        |
| account_id       | core | string        |
| broker_id        | core | string        | Required. The unique ID that Amazon MQ generates for the broker.                                                                                                                                                       |
| console_access   | core | bool          | Enables access to the the ActiveMQ Web Console for the ActiveMQ user.                                                                                                                                                  |
| groups           | core | array<string> | The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long. |
| mq_user_arn      | core | string        |
| pending          | core | json          | The status of the changes pending for the ActiveMQ user.                                                                                                                                                               |
| replication_user | core | bool          | Describes whether the user is intended for data replication                                                                                                                                                            |
| tags             | core | hstore_csv    |
| username         | core | string        | Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.                        |
