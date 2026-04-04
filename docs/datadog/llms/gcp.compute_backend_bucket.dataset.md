# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_backend_bucket.dataset.md

---
title: Compute Backend Bucket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Compute Backend Bucket
---

# Compute Backend Bucket

A Compute Backend Bucket in Google Cloud is a backend service that uses a Cloud Storage bucket to serve static content for HTTP(S) load balancing. It allows you to host and deliver static assets such as images, videos, or website files directly from Cloud Storage while benefiting from load balancing, caching, and global content delivery through Google's infrastructure.

```
gcp.compute_backend_bucket
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ----------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string        |
| ancestors               | core | array<string> |
| bucket_name             | core | string        | Cloud Storage bucket name.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| cdn_policy              | core | json          | Cloud CDN configuration for this BackendBucket.                                                                                                                                                                                                                                                                                                                                                                                                     |
| compression_mode        | core | string        | Compress text responses using Brotli or gzip compression, based on the client's Accept-Encoding header.                                                                                                                                                                                                                                                                                                                                             |
| creation_timestamp      | core | timestamp     | [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                             |
| custom_response_headers | core | array<string> | Headers that the Application Load Balancer should add to proxied responses.                                                                                                                                                                                                                                                                                                                                                                         |
| datadog_display_name    | core | string        |
| description             | core | string        | An optional textual description of the resource; provided by the client when the resource is created.                                                                                                                                                                                                                                                                                                                                               |
| edge_security_policy    | core | string        | [Output Only] The resource URL for the edge security policy associated with this backend bucket.                                                                                                                                                                                                                                                                                                                                                    |
| enable_cdn              | core | bool          | If true, enable Cloud CDN for this BackendBucket.                                                                                                                                                                                                                                                                                                                                                                                                   |
| id                      | core | string        | [Output Only] Unique identifier for the resource; defined by the server.                                                                                                                                                                                                                                                                                                                                                                            |
| kind                    | core | string        | Output only. Type of the resource.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| labels                  | core | array<string> |
| name                    | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| organization_id         | core | string        |
| parent                  | core | string        |
| project_id              | core | string        |
| project_number          | core | string        |
| region_id               | core | string        |
| resource_name           | core | string        |
| self_link               | core | string        | [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags                    | core | hstore_csv    |
| used_by                 | core | json          | Output only. [Output Only] List of resources referencing that backend bucket.                                                                                                                                                                                                                                                                                                                                                                       |
| zone_id                 | core | string        |
