# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.connectors_endpoint_attachment.dataset.md

---
title: Connectors Endpoint Attachment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connectors Endpoint Attachment
---

# Connectors Endpoint Attachment

Connectors Endpoint Attachment in Google Cloud is a resource that allows private connectivity between a Virtual Private Cloud (VPC) network and a Connectors instance. It establishes a secure network path so that services running in a VPC can access connector endpoints without using public internet routes. This helps maintain data privacy and reduces latency for integrations with external systems or APIs.

```
gcp.connectors_endpoint_attachment
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                        | Description |
| ---------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| ancestors              | core | array<string> |
| create_time            | core | timestamp     | Output only. Created time.                                                                                                                                                       |
| datadog_display_name   | core | string        |
| description            | core | string        | Optional. Description of the resource.                                                                                                                                           |
| endpoint_global_access | core | bool          | Optional. The Private Service Connect Connection Endpoint Global Access. https://cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access           |
| endpoint_ip            | core | string        | Output only. The Private Service Connect connection endpoint ip                                                                                                                  |
| labels                 | core | array<string> | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| name                   | core | string        | Output only. Resource name of the Endpoint Attachment. Format: projects/{project}/locations/{location}/endpointAttachments/{endpoint_attachment}                                 |
| organization_id        | core | string        |
| parent                 | core | string        |
| project_id             | core | string        |
| project_number         | core | string        |
| region_id              | core | string        |
| resource_name          | core | string        |
| service_attachment     | core | string        | Required. The path of the service attachment                                                                                                                                     |
| state                  | core | string        | Output only. The Private Service Connect Connection Endpoint State. This value is only available in the Full view.                                                               |
| tags                   | core | hstore_csv    |
| update_time            | core | timestamp     | Output only. Updated time.                                                                                                                                                       |
| zone_id                | core | string        |
