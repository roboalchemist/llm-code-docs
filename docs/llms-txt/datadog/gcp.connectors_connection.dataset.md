# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.connectors_connection.dataset.md

---
title: Connector Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connector Connection
---

# Connector Connection

Connector Connection in Google Cloud represents a network link created through Serverless VPC Access. It allows serverless environments such as Cloud Run, App Engine, or Cloud Functions to securely connect to resources inside a Virtual Private Cloud (VPC) network. This connection provides private IP access to databases, services, or other workloads running in the VPC, enabling secure communication without exposing traffic to the public internet.

```
gcp.connectors_connection
```

## Fields

| Title                          | ID   | Type          | Data Type                                                                                                                                                                                                                                             | Description |
| ------------------------------ | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string        |
| ancestors                      | core | array<string> |
| async_operations_enabled       | core | bool          | Optional. Async operations enabled for the connection. If Async Operations is enabled, Connection allows the customers to initiate async long running operations using the actions API.                                                               |
| auth_config                    | core | json          | Optional. Configuration for establishing the connection's authentication with an external system.                                                                                                                                                     |
| auth_override_enabled          | core | bool          | Optional. Auth override enabled for the connection. If Auth Override is enabled, Connection allows the backend service auth to be overridden in the entities/actions API.                                                                             |
| billing_config                 | core | json          | Output only. Billing config for the connection.                                                                                                                                                                                                       |
| config_variables               | core | json          | Optional. Configuration for configuring the connection with an external system.                                                                                                                                                                       |
| connection_revision            | core | int64         | Output only. Connection revision. This field is only updated when the connection is created or updated by User.                                                                                                                                       |
| connector_version              | core | string        | Required. Connector version on which the connection is created. The format is: projects/*/locations/*/providers/*/connectors/*/versions/* Only global location is supported for ConnectorVersion resource.                                            |
| connector_version_infra_config | core | json          | Output only. Infra configs supported by Connector Version.                                                                                                                                                                                            |
| connector_version_launch_stage | core | string        | Output only. Flag to mark the version indicating the launch stage.                                                                                                                                                                                    |
| create_time                    | core | timestamp     | Output only. Created time.                                                                                                                                                                                                                            |
| datadog_display_name           | core | string        |
| description                    | core | string        | Optional. Description of the resource.                                                                                                                                                                                                                |
| destination_configs            | core | json          | Optional. Configuration of the Connector's destination. Only accepted for Connectors that accepts user defined destination(s).                                                                                                                        |
| envoy_image_location           | core | string        | Output only. GCR location where the envoy image is stored. formatted like: gcr.io/{bucketName}/{imageName}                                                                                                                                            |
| eventing_config                | core | json          | Optional. Eventing config of a connection                                                                                                                                                                                                             |
| eventing_enablement_type       | core | string        | Optional. Eventing enablement type. Will be nil if eventing is not enabled.                                                                                                                                                                           |
| eventing_runtime_data          | core | json          | Output only. Eventing Runtime Data.                                                                                                                                                                                                                   |
| gcp_status                     | core | json          | Output only. Current status of the connection.                                                                                                                                                                                                        |
| host                           | core | string        | Output only. The name of the Hostname of the Service Directory service with TLS.                                                                                                                                                                      |
| image_location                 | core | string        | Output only. GCR location where the runtime image is stored. formatted like: gcr.io/{bucketName}/{imageName}                                                                                                                                          |
| is_trusted_tester              | core | bool          | Output only. Is trusted tester program enabled for the project.                                                                                                                                                                                       |
| labels                         | core | array<string> | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources                                                                      |
| lock_config                    | core | json          | Optional. Configuration that indicates whether or not the Connection can be edited.                                                                                                                                                                   |
| log_config                     | core | json          | Optional. Log configuration for the connection.                                                                                                                                                                                                       |
| name                           | core | string        | Output only. Resource name of the Connection. Format: projects/{project}/locations/{location}/connections/{connection}                                                                                                                                |
| node_config                    | core | json          | Optional. Node configuration for the connection.                                                                                                                                                                                                      |
| organization_id                | core | string        |
| parent                         | core | string        |
| project_id                     | core | string        |
| project_number                 | core | string        |
| region_id                      | core | string        |
| resource_name                  | core | string        |
| service_account                | core | string        | Optional. Service account needed for runtime plane to access Google Cloud resources.                                                                                                                                                                  |
| service_directory              | core | string        | Output only. The name of the Service Directory service name. Used for Private Harpoon to resolve the ILB address. e.g. "projects/cloud-connectors-e2e-testing/locations/us-central1/namespaces/istio-system/services/istio-ingressgateway-connectors" |
| ssl_config                     | core | json          | Optional. Ssl config of a connection                                                                                                                                                                                                                  |
| subscription_type              | core | string        | Output only. This subscription type enum states the subscription type of the project.                                                                                                                                                                 |
| suspended                      | core | bool          | Optional. Suspended indicates if a user has suspended a connection or not.                                                                                                                                                                            |
| tags                           | core | hstore_csv    |
| tls_service_directory          | core | string        | Output only. The name of the Service Directory service with TLS.                                                                                                                                                                                      |
| traffic_shaping_configs        | core | json          | Optional. Traffic shaping configuration for the connection.                                                                                                                                                                                           |
| update_time                    | core | timestamp     | Output only. Updated time.                                                                                                                                                                                                                            |
| zone_id                        | core | string        |
