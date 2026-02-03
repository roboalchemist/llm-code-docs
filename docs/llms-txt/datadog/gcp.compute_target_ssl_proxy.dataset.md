# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_target_ssl_proxy.dataset.md

---
title: Target SSL Proxy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Target SSL Proxy
---

# Target SSL Proxy

A Target SSL Proxy in Google Cloud is a regional proxy resource that routes incoming SSL traffic from clients to backend services. It terminates SSL connections at the proxy level, offloading encryption and decryption, and then forwards the unencrypted traffic to the appropriate backend. This allows centralized SSL certificate management, improved performance, and secure client connections for applications running behind load balancers.

```
gcp.compute_target_ssl_proxy
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| certificate_map      | core | string        | URL of a certificate map that identifies a certificate map associated with the given target proxy. This field can only be set for global target proxies. If set, sslCertificates will be ignored. Accepted format is//certificatemanager.googleapis.com/projects/{project}/locations/{location}/certificateMaps/{resourceName}.                                                                                                                     |
| creation_timestamp   | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| id                   | core | string        | [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                                     |
| kind                 | core | string        | Output only. [Output Only] Type of the resource. Alwayscompute#targetSslProxy for target SSL proxies.                                                                                                                                                                                                                                                                                                                                               |
| labels               | core | array<string> |
| name                 | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| proxy_header         | core | string        | Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE.                                                                                                                                                                                                                                                                                                                      |
| region_id            | core | string        |
| resource_name        | core | string        |
| self_link            | core | string        | [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                                  |
| service              | core | string        | URL to the BackendService resource.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ssl_certificates     | core | array<string> | URLs to SslCertificate resources that are used to authenticate connections to Backends. At least one SSL certificate must be specified. Currently, you may specify up to 15 SSL certificates. sslCertificates do not apply when the load balancing scheme is set to INTERNAL_SELF_MANAGED.                                                                                                                                                          |
| ssl_policy           | core | string        | URL of SslPolicy resource that will be associated with the TargetSslProxy resource. If not set, the TargetSslProxy resource will not have any SSL policy configured.                                                                                                                                                                                                                                                                                |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
