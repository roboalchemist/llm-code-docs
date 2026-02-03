# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transfer_profile.dataset.md

---
title: Transfer Family Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transfer Family Profile
---

# Transfer Family Profile

AWS Transfer Family Profile is a resource that defines user-specific settings for secure file transfers over protocols like SFTP, FTPS, and FTP. A profile contains configurations such as role associations, policies, and access details that determine how users interact with Transfer Family servers. It helps centralize and manage permissions, ensuring consistent and secure access control for file transfer operations.

```
aws.transfer_profile
```

## Fields

| Title           | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                   | Description |
| --------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string        |
| account_id      | core | string        |
| arn             | core | string        | The unique Amazon Resource Name (ARN) for the profile.                                                                                                                                                                                                                                                                      |
| as2_id          | core | string        | The As2Id is the AS2-name, as defined in the RFC 4130. For inbound transfers, this is the AS2-From header for the AS2 messages sent from the partner. For outbound connectors, this is the AS2-To header for the AS2 messages sent to the partner using the StartFileTransfer API operation. This ID cannot include spaces. |
| certificate_ids | core | array<string> | An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.                                                                                                                                                                                              |
| profile_id      | core | string        | A unique identifier for the local or partner AS2 profile.                                                                                                                                                                                                                                                                   |
| profile_type    | core | string        | Indicates whether to list only LOCAL type profiles or only PARTNER type profiles. If not supplied in the request, the command lists all types of profiles.                                                                                                                                                                  |
| tags            | core | hstore_csv    |
