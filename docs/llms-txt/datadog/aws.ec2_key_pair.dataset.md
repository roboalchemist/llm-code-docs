# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_key_pair.dataset.md

---
title: EC2 Key Pair
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Key Pair
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_key_pair.dataset/index.html
---

# EC2 Key Pair

An EC2 Key Pair in AWS is a set of security credentials used to connect securely to Amazon EC2 instances. It consists of a public key that AWS stores and a private key that you download and keep safe. When you launch an instance, the public key is placed on it, and you use the private key to establish secure SSH or RDP access. Key pairs help ensure that only authorized users can access your instances.

```
aws.ec2_key_pair
```

## Fields

| Title           | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| --------------- | ---- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string    |
| account_id      | core | string    |
| create_time     | core | timestamp | If you used Amazon EC2 to create the key pair, this is the date and time when the key was created, in ISO 8601 date-time format, in the UTC time zone. If you imported an existing key pair to Amazon EC2, this is the date and time the key was imported, in ISO 8601 date-time format, in the UTC time zone.                                                                                                                                                                                                                                                                                                                   |
| key_fingerprint | core | string    | If you used CreateKeyPair to create the key pair: For RSA key pairs, the key fingerprint is the SHA-1 digest of the DER encoded private key. For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with OpenSSH 6.8. If you used ImportKeyPair to provide Amazon Web Services the public key: For RSA key pairs, the key fingerprint is the MD5 public key fingerprint as specified in section 4 of RFC4716. For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with OpenSSH 6.8. |
| key_name        | core | string    | The name of the key pair.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| key_pair_arn    | core | string    |
| key_pair_id     | core | string    | The ID of the key pair.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| key_type        | core | string    | The type of key pair.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| tags            | core | hstore    |
