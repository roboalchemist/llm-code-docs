# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkservices_gateway.dataset.md

---
title: Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Gateway
---

# Gateway

Gateway in Google Cloud is a managed service that provides a secure entry point for APIs and services. It allows you to deploy, secure, and monitor APIs at scale without managing infrastructure. Gateways handle authentication, traffic management, and policy enforcement, making it easier to expose backend services to clients in a controlled and reliable way.

```
gcp.networkservices_gateway
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                 | Description |
| ----------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string        |
| addresses               | core | array<string> | Optional. Zero or one IPv4 or IPv6 address on which the Gateway will receive the traffic. When no address is provided, an IP from the subnetwork is allocated This field only applies to gateways of type 'SECURE_WEB_GATEWAY'. Gateways of type 'OPEN_MESH' listen on 0.0.0.0 for IPv4 and :: for IPv6.                                                  |
| ancestors               | core | array<string> |
| certificate_urls        | core | array<string> | Optional. A fully-qualified Certificates URL reference. The proxy presents a Certificate (selected based on SNI) when establishing a TLS connection. This feature only applies to gateways of type 'SECURE_WEB_GATEWAY'.                                                                                                                                  |
| create_time             | core | timestamp     | Output only. The timestamp when the resource was created.                                                                                                                                                                                                                                                                                                 |
| datadog_display_name    | core | string        |
| description             | core | string        | Optional. A free-text description of the resource. Max length 1024 characters.                                                                                                                                                                                                                                                                            |
| envoy_headers           | core | string        | Optional. Determines if envoy will insert internal debug headers into upstream requests. Other Envoy headers may still be injected. By default, envoy will not insert any debug headers.                                                                                                                                                                  |
| gateway_security_policy | core | string        | Optional. A fully-qualified GatewaySecurityPolicy URL reference. Defines how a server should apply security policy to inbound (VM to Proxy) initiated connections. For example: `projects/*/locations/*/gatewaySecurityPolicies/swg-policy`. This policy is specific to gateways of type 'SECURE_WEB_GATEWAY'.                                            |
| ip_version              | core | string        | Optional. The IP Version that will be used by this gateway. Valid options are IPV4 or IPV6. Default is IPV4.                                                                                                                                                                                                                                              |
| labels                  | core | array<string> | Optional. Set of label tags associated with the Gateway resource.                                                                                                                                                                                                                                                                                         |
| name                    | core | string        | Identifier. Name of the Gateway resource. It matches pattern `projects/*/locations/*/gateways/`.                                                                                                                                                                                                                                                          |
| network                 | core | string        | Optional. The relative resource name identifying the VPC network that is using this configuration. For example: `projects/*/global/networks/network-1`. Currently, this field is specific to gateways of type 'SECURE_WEB_GATEWAY'.                                                                                                                       |
| organization_id         | core | string        |
| parent                  | core | string        |
| ports                   | core | array<int64>  | Required. One or more port numbers (1-65535), on which the Gateway will receive traffic. The proxy binds to the specified ports. Gateways of type 'SECURE_WEB_GATEWAY' are limited to 5 ports. Gateways of type 'OPEN_MESH' listen on 0.0.0.0 for IPv4 and :: for IPv6 and support multiple ports.                                                        |
| project_id              | core | string        |
| project_number          | core | string        |
| region_id               | core | string        |
| resource_name           | core | string        |
| routing_mode            | core | string        | Optional. The routing mode of the Gateway. This field is configurable only for gateways of type SECURE_WEB_GATEWAY. This field is required for gateways of type SECURE_WEB_GATEWAY.                                                                                                                                                                       |
| scope                   | core | string        | Optional. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single configuration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens. |
| self_link               | core | string        | Output only. Server-defined URL of this resource                                                                                                                                                                                                                                                                                                          |
| server_tls_policy       | core | string        | Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled.                                                                                                                                                                                                                |
| subnetwork              | core | string        | Optional. The relative resource name identifying the subnetwork in which this SWG is allocated. For example: `projects/*/regions/us-central1/subnetworks/network-1` Currently, this field is specific to gateways of type 'SECURE_WEB_GATEWAY".                                                                                                           |
| tags                    | core | hstore_csv    |
| type                    | core | string        | Immutable. The type of the customer managed gateway. This field is required. If unspecified, an error is returned.                                                                                                                                                                                                                                        |
| update_time             | core | timestamp     | Output only. The timestamp when the resource was updated.                                                                                                                                                                                                                                                                                                 |
| zone_id                 | core | string        |
