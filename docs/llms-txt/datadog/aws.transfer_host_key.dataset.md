# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transfer_host_key.dataset.md

---
title: Transfer Family Host Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transfer Family Host Key
---

# Transfer Family Host Key

Transfer Family Host Key in AWS is a resource used to manage SSH host keys for AWS Transfer Family servers. It allows secure identification of the server to clients during SFTP, FTPS, or FTP connections. By using host keys, clients can verify they are connecting to the correct server, ensuring trust and preventing man-in-the-middle attacks.

```
aws.transfer_host_key
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                                                                                     | Description |
| -------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| arn                  | core | string     | The unique Amazon Resource Name (ARN) for the host key.                                                                                                                                                       |
| date_imported        | core | timestamp  | The date on which the host key was added to the server.                                                                                                                                                       |
| description          | core | string     | The text description for this host key.                                                                                                                                                                       |
| host_key_fingerprint | core | string     | The public key fingerprint, which is a short sequence of bytes used to identify the longer public key.                                                                                                        |
| host_key_id          | core | string     | A unique identifier for the host key.                                                                                                                                                                         |
| tags                 | core | hstore_csv |
| type                 | core | string     | The encryption algorithm that is used for the host key. The Type parameter is specified by using one of the following values: ssh-rsa ssh-ed25519 ecdsa-sha2-nistp256 ecdsa-sha2-nistp384 ecdsa-sha2-nistp521 |
