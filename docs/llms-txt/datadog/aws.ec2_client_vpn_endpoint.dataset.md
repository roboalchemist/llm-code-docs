# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_client_vpn_endpoint.dataset.md

---
title: Client VPN Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Client VPN Endpoint
---

# Client VPN Endpoint

Client VPN Endpoint in AWS is a managed client-based VPN service that enables secure access to AWS resources and on-premises networks. It allows users to connect from any location using OpenVPN-based clients, providing encrypted communication over the internet. This resource supports authentication, authorization, and fine-grained access control, making it easier to extend private network access to remote users.

```
aws.ec2_client_vpn_endpoint
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                                                                                           | Description |
| --------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| account_id                  | core | string        |
| associated_target_networks  | core | json          | Information about the associated target networks. A target network is a subnet in a VPC.                                                                                                            |
| authentication_options      | core | json          | Information about the authentication method used by the Client VPN endpoint.                                                                                                                        |
| client_cidr_block           | core | string        | The IPv4 address range, in CIDR notation, from which client IP addresses are assigned.                                                                                                              |
| client_connect_options      | core | json          | The options for managing connection authorization for new client connections.                                                                                                                       |
| client_login_banner_options | core | json          | Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established.                                                   |
| client_vpn_endpoint_arn     | core | string        |
| client_vpn_endpoint_id      | core | string        | The ID of the Client VPN endpoint.                                                                                                                                                                  |
| connection_log_options      | core | json          | Information about the client connection logging options for the Client VPN endpoint.                                                                                                                |
| creation_time               | core | string        | The date and time the Client VPN endpoint was created.                                                                                                                                              |
| deletion_time               | core | string        | The date and time the Client VPN endpoint was deleted, if applicable.                                                                                                                               |
| description                 | core | string        | A brief description of the endpoint.                                                                                                                                                                |
| dns_name                    | core | string        | The DNS name to be used by clients when connecting to the Client VPN endpoint.                                                                                                                      |
| dns_servers                 | core | array<string> | Information about the DNS servers to be used for DNS resolution.                                                                                                                                    |
| security_group_ids          | core | array<string> | The IDs of the security groups for the target network.                                                                                                                                              |
| self_service_portal_url     | core | string        | The URL of the self-service portal.                                                                                                                                                                 |
| server_certificate_arn      | core | string        | The ARN of the server certificate.                                                                                                                                                                  |
| session_timeout_hours       | core | int64         | The maximum VPN session duration time in hours. Valid values: 8 | 10 | 12 | 24 Default value: 24                                                                                                    |
| split_tunnel                | core | bool          | Indicates whether split-tunnel is enabled in the Client VPN endpoint. For information about split-tunnel VPN endpoints, see Split-Tunnel Client VPN endpoint in the Client VPN Administrator Guide. |
| status                      | core | json          | The current state of the Client VPN endpoint.                                                                                                                                                       |
| tags                        | core | hstore_csv    |
| transport_protocol          | core | string        | The transport protocol used by the Client VPN endpoint.                                                                                                                                             |
| vpc_id                      | core | string        | The ID of the VPC.                                                                                                                                                                                  |
| vpn_port                    | core | int64         | The port number for the Client VPN endpoint.                                                                                                                                                        |
| vpn_protocol                | core | string        | The protocol used by the VPN session.                                                                                                                                                               |
