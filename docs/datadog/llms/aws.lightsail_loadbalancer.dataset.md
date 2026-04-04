# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lightsail_loadbalancer.dataset.md

---
title: Lightsail Load Balancer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lightsail Load Balancer
---

# Lightsail Load Balancer

This table represents the Lightsail Load Balancer resource from Amazon Web Services.

```gdscript3
aws.lightsail_loadbalancer
```

## Fields

| Title                                         | ID   | Type         | Data Type                                                                                                                                                                                                      | Description |
| --------------------------------------------- | ---- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                          | core | string       |
| account_id                                    | core | string       |
| arn                                           | core | string       | The Amazon Resource Name (ARN) of the load balancer.                                                                                                                                                           |
| created_at                                    | core | timestamp    | The date when your load balancer was created.                                                                                                                                                                  |
| dns_name                                      | core | string       | The DNS name of your Lightsail load balancer.                                                                                                                                                                  |
| health_check_path                             | core | string       |
| https_redirection_enabled                     | core | string       |
| instance_health_summary                       | core | json         | An array of InstanceHealthSummary objects describing the health of the load balancer.                                                                                                                          |
| instance_port                                 | core | int64        | The port where the load balancer will direct traffic to your Lightsail instances. For HTTP traffic, it's port 80. For HTTPS traffic, it's port 443.                                                            |
| ip_address_type                               | core | string       | The IP address type of the load balancer. The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.                              |
| location                                      | core | json         | The AWS Region where your load balancer was created (<code>us-east-2a</code>). Lightsail automatically creates your load balancer across Availability Zones.                                                   |
| name                                          | core | string       | The name of the load balancer (<code>my-load-balancer</code>).                                                                                                                                                 |
| protocol                                      | core | string       | The protocol you have enabled for your load balancer. Valid values are below. You can't just have <code>HTTP_HTTPS</code>, but you can have just <code>HTTP</code>.                                            |
| public_ports                                  | core | array<int64> | An array of public port settings for your load balancer. For HTTP, use port 80. For HTTPS, use port 443.                                                                                                       |
| resource_type                                 | core | string       | The resource type (<code>LoadBalancer</code>.                                                                                                                                                                  |
| session_stickiness_enabled                    | core | string       |
| session_stickiness_lb_cookie_duration_seconds | core | string       |
| state                                         | core | string       | The status of your load balancer. Valid values are below.                                                                                                                                                      |
| support_code                                  | core | string       | The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily. |
| tags                                          | core | hstore_csv   |
| tls_certificate_summaries                     | core | json         | An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the SSL/TLS certificates. For example, if <code>true</code>, the certificate is attached to the load balancer. |
| tls_policy_name                               | core | string       |
