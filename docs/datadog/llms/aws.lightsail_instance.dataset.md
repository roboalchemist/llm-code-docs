# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lightsail_instance.dataset.md

---
title: Lightsail Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lightsail Instance
---

# Lightsail Instance

An AWS Lightsail Instance is a virtual private server designed for simplicity and cost-effectiveness. It provides preconfigured compute, storage, and networking resources, making it easy to deploy applications, websites, or development environments without managing complex infrastructure. Lightsail instances are ideal for small to medium workloads, offering predictable pricing and straightforward scaling.

```
aws.lightsail_instance
```

## Fields

| Title              | ID   | Type          | Data Type                                                                                                                                                                                                                      | Description |
| ------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key               | core | string        |
| account_id         | core | string        |
| add_ons            | core | json          | An array of objects representing the add-ons enabled on the instance.                                                                                                                                                          |
| arn                | core | string        | The Amazon Resource Name (ARN) of the instance (arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE).                                                                                       |
| blueprint_id       | core | string        | The blueprint ID (amazon_linux_2023).                                                                                                                                                                                          |
| blueprint_name     | core | string        | The friendly name of the blueprint (Amazon Linux 2023).                                                                                                                                                                        |
| bundle_id          | core | string        | The bundle for the instance (micro_x_x).                                                                                                                                                                                       |
| created_at         | core | timestamp     | The timestamp when the instance was created (1479734909.17) in Unix time format.                                                                                                                                               |
| hardware           | core | json          | The size of the vCPU and the amount of RAM for the instance.                                                                                                                                                                   |
| ip_address_type    | core | string        | The IP address type of the instance. The possible values are ipv4 for IPv4 only, ipv6 for IPv6 only, and dualstack for IPv4 and IPv6.                                                                                          |
| ipv6_addresses     | core | array<string> | The IPv6 addresses of the instance.                                                                                                                                                                                            |
| is_static_ip       | core | bool          | A Boolean value indicating whether this instance has a static IP assigned to it.                                                                                                                                               |
| location           | core | json          | The region name and Availability Zone where the instance is located.                                                                                                                                                           |
| metadata_options   | core | json          | The metadata options for the Amazon Lightsail instance.                                                                                                                                                                        |
| name               | core | string        | The name the user gave the instance (Amazon_Linux_2023-1).                                                                                                                                                                     |
| networking         | core | json          | Information about the public ports and monthly data transfer rates for the instance.                                                                                                                                           |
| port_states        | core | json          | An array of objects that describe the firewall port states for the specified instance.                                                                                                                                         |
| private_ip_address | core | string        | The private IP address of the instance.                                                                                                                                                                                        |
| public_ip_address  | core | string        | The public IP address of the instance.                                                                                                                                                                                         |
| resource_type      | core | string        | The type of resource (usually Instance).                                                                                                                                                                                       |
| ssh_key_name       | core | string        | The name of the SSH key being used to connect to the instance (LightsailDefaultKeyPair).                                                                                                                                       |
| state              | core | json          | The status code and the state (running) for the instance.                                                                                                                                                                      |
| support_code       | core | string        | The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily. |
| tags               | core | hstore_csv    |
| username           | core | string        | The user name for connecting to the instance (ec2-user).                                                                                                                                                                       |
