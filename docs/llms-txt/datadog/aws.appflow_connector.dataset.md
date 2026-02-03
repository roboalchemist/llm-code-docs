# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appflow_connector.dataset.md

---
title: Amazon AppFlow Connector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amazon AppFlow Connector
---

# Amazon AppFlow Connector

Amazon AppFlow Connector is a managed integration resource that enables secure data transfer between AWS services and supported SaaS applications. It allows you to configure, manage, and monitor connections to external systems, making it easier to automate data flows without custom code. This resource provides details about a connector's configuration, capabilities, and status, helping you understand how data can be moved and transformed between sources and destinations.

```
aws.appflow_connector
```

## Fields

| Title                                 | ID   | Type          | Data Type                                                                                                      | Description |
| ------------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string        |
| account_id                            | core | string        |
| authentication_config                 | core | json          | The authentication config required for the connector.                                                          |
| can_use_as_destination                | core | bool          | Specifies whether the connector can be used as a destination.                                                  |
| can_use_as_source                     | core | bool          | Specifies whether the connector can be used as a source.                                                       |
| connector_arn                         | core | string        | The Amazon Resource Name (ARN) for the registered connector.                                                   |
| connector_description                 | core | string        | A description about the connector.                                                                             |
| connector_label                       | core | string        | The label used for registering the connector.                                                                  |
| connector_metadata                    | core | json          | Specifies connector-specific metadata such as oAuthScopes, supportedRegions, privateLinkServiceUrl, and so on. |
| connector_modes                       | core | array<string> | The connection modes that the connector supports.                                                              |
| connector_name                        | core | string        | The connector name.                                                                                            |
| connector_owner                       | core | string        | The owner who developed the connector.                                                                         |
| connector_provisioning_config         | core | json          | The configuration required for registering the connector.                                                      |
| connector_provisioning_type           | core | string        | The provisioning type used to register the connector.                                                          |
| connector_runtime_settings            | core | json          | The required connector runtime settings.                                                                       |
| connector_type                        | core | string        | The connector type.                                                                                            |
| connector_version                     | core | string        | The connector version.                                                                                         |
| is_private_link_enabled               | core | bool          | Specifies if PrivateLink is enabled for that connector.                                                        |
| is_private_link_endpoint_url_required | core | bool          | Specifies if a PrivateLink endpoint URL is required.                                                           |
| logo_url                              | core | string        | Logo URL of the connector.                                                                                     |
| registered_at                         | core | timestamp     | The date on which the connector was registered.                                                                |
| registered_by                         | core | string        | Information about who registered the connector.                                                                |
| supported_api_versions                | core | array<string> | A list of API versions that are supported by the connector.                                                    |
| supported_data_transfer_apis          | core | json          | The APIs of the connector application that Amazon AppFlow can use to transfer your data.                       |
| supported_data_transfer_types         | core | array<string> | The data transfer types that the connector supports. RECORD Structured records. FILE Files or binary data.     |
| supported_destination_connectors      | core | array<string> | Lists the connectors that are available for use as destinations.                                               |
| supported_operators                   | core | array<string> | A list of operators supported by the connector.                                                                |
| supported_scheduling_frequencies      | core | array<string> | Specifies the supported flow frequency for that connector.                                                     |
| supported_trigger_types               | core | array<string> | Specifies the supported trigger types for the flow.                                                            |
| supported_write_operations            | core | array<string> | A list of write operations supported by the connector.                                                         |
| tags                                  | core | hstore_csv    |
