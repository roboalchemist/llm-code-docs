# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lightsail_static_ip.dataset.md

---
title: Lightsail Static IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lightsail Static IP
---

# Lightsail Static IP

Lightsail Static IP is a fixed, public IPv4 address in Amazon Lightsail that you can attach to an instance. Unlike a dynamic IP, it does not change if you stop and start the instance, making it useful for hosting websites, applications, or services that require a consistent endpoint.

```
aws.lightsail_static_ip
```

## Fields

| Title         | ID   | Type       | Data Type                                                                                                                                                                                                                      | Description |
| ------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| arn           | core | string     | The Amazon Resource Name (ARN) of the static IP (arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE).                                                                                      |
| attached_to   | core | string     | The instance where the static IP is attached (Amazon_Linux-1GB-Ohio-1).                                                                                                                                                        |
| created_at    | core | timestamp  | The timestamp when the static IP was created (1479735304.222).                                                                                                                                                                 |
| ip_address    | core | string     | The static IP address.                                                                                                                                                                                                         |
| is_attached   | core | bool       | A Boolean value indicating whether the static IP is attached.                                                                                                                                                                  |
| location      | core | json       | The region and Availability Zone where the static IP was created.                                                                                                                                                              |
| name          | core | string     | The name of the static IP (StaticIP-Ohio-EXAMPLE).                                                                                                                                                                             |
| resource_type | core | string     | The resource type (usually StaticIp).                                                                                                                                                                                          |
| support_code  | core | string     | The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily. |
| tags          | core | hstore_csv |
