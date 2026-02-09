# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_location_smb.dataset.md

---
title: DataSync SMB Location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataSync SMB Location
---

# DataSync SMB Location

DataSync SMB Location in AWS represents a configured connection point to an SMB (Server Message Block) file system. It is used by AWS DataSync to transfer data between on-premises SMB shares or self-managed file servers and AWS storage services. This resource stores details such as the server hostname, share name, authentication information, and mount options, enabling secure and efficient data movement for migration, backup, or replication tasks.

```
aws.datasync_location_smb
```

## Fields

| Title               | ID   | Type          | Data Type                                                                                                                                                         | Description |
| ------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| agent_arns          | core | array<string> | The ARNs of the DataSync agents that can connect with your SMB file server.                                                                                       |
| authentication_type | core | string        | The authentication protocol that DataSync uses to connect to your SMB file server.                                                                                |
| creation_time       | core | timestamp     | The time that the SMB location was created.                                                                                                                       |
| dns_ip_addresses    | core | array<string> | The IPv4 or IPv6 addresses for the DNS servers that your SMB file server belongs to. This element applies only if AuthenticationType is set to KERBEROS.          |
| domain              | core | string        | The name of the Windows domain that the SMB file server belongs to. This element applies only if AuthenticationType is set to NTLM.                               |
| kerberos_principal  | core | string        | The Kerberos principal that has permission to access the files, folders, and file metadata in your SMB file server.                                               |
| location_arn        | core | string        | The ARN of the SMB location.                                                                                                                                      |
| location_uri        | core | string        | The URI of the SMB location.                                                                                                                                      |
| mount_options       | core | json          | The SMB protocol version that DataSync uses to access your SMB file server.                                                                                       |
| tags                | core | hstore_csv    |
| user                | core | string        | The user that can mount and access the files, folders, and file metadata in your SMB file server. This element applies only if AuthenticationType is set to NTLM. |
