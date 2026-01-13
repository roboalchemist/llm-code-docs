# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_location_hdfs.dataset.md

---
title: DataSync HDFS Location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataSync HDFS Location
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.datasync_location_hdfs.dataset/index.html
---

# DataSync HDFS Location

DataSync HDFS Location in AWS represents a connection point to a Hadoop Distributed File System (HDFS) cluster. It allows AWS DataSync to transfer data between HDFS and AWS storage services such as Amazon S3, Amazon EFS, or Amazon FSx. The resource stores configuration details like the HDFS NameNode addresses, authentication type, and security settings, enabling secure and efficient data migration or synchronization from on-premises or self-managed Hadoop environments into AWS.

```
aws.datasync_location_hdfs
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| account_id           | core | string        |
| agent_arns           | core | array<string> | The ARNs of the DataSync agents that can connect with your HDFS cluster.                                                                                             |
| authentication_type  | core | string        | The type of authentication used to determine the identity of the user.                                                                                               |
| block_size           | core | int64         | The size of the data blocks to write into the HDFS cluster.                                                                                                          |
| creation_time        | core | timestamp     | The time that the HDFS location was created.                                                                                                                         |
| kerberos_principal   | core | string        | The Kerberos principal with access to the files and folders on the HDFS cluster. This parameter is used if the AuthenticationType is defined as KERBEROS.            |
| kms_key_provider_uri | core | string        | The URI of the HDFS cluster's Key Management Server (KMS).                                                                                                           |
| location_arn         | core | string        | The ARN of the HDFS location.                                                                                                                                        |
| location_uri         | core | string        | The URI of the HDFS location.                                                                                                                                        |
| name_nodes           | core | json          | The NameNode that manages the HDFS namespace.                                                                                                                        |
| qop_configuration    | core | json          | The Quality of Protection (QOP) configuration, which specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the HDFS cluster. |
| replication_factor   | core | int64         | The number of DataNodes to replicate the data to when writing to the HDFS cluster.                                                                                   |
| simple_user          | core | string        | The user name to identify the client on the host operating system. This parameter is used if the AuthenticationType is defined as SIMPLE.                            |
| tags                 | core | hstore        |
