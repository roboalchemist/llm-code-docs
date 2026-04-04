# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.api_management_service_api.dataset.md

---
title: Api Management Service Api
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Api Management Service Api
---

# Api Management Service Api

This table represents the api_management_service_api resource from Microsoft Azure.

```
azure.api_management_service_api
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                                                                                                                                                                                          | Description |
| -------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string        |
| api_revision                     | core | string        | Describes the revision of the API. If no value is provided, default revision 1 is created                                                                                                                                                          |
| api_revision_description         | core | string        | Description of the API Revision.                                                                                                                                                                                                                   |
| api_version                      | core | string        | Indicates the version identifier of the API if the API is versioned                                                                                                                                                                                |
| api_version_description          | core | string        | Description of the API Version.                                                                                                                                                                                                                    |
| api_version_set                  | core | json          | Version set details                                                                                                                                                                                                                                |
| api_version_set_id               | core | string        | A resource identifier for the related ApiVersionSet.                                                                                                                                                                                               |
| authentication_settings          | core | json          | Collection of authentication settings included into this API.                                                                                                                                                                                      |
| contact                          | core | json          | Contact information for the API.                                                                                                                                                                                                                   |
| description                      | core | string        | Description of the API. May include HTML formatting tags.                                                                                                                                                                                          |
| id                               | core | string        | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}                                                          |
| is_current                       | core | bool          | Indicates if API revision is current api revision.                                                                                                                                                                                                 |
| is_online                        | core | bool          | Indicates if API revision is accessible via the gateway.                                                                                                                                                                                           |
| license                          | core | json          | License information for the API.                                                                                                                                                                                                                   |
| location                         | core | string        |
| name                             | core | string        | The name of the resource                                                                                                                                                                                                                           |
| path                             | core | string        | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. |
| protocols                        | core | array<string> | Describes on which protocols the operations in this API can be invoked.                                                                                                                                                                            |
| provisioning_state               | core | string        | The provisioning state                                                                                                                                                                                                                             |
| resource_group                   | core | string        |
| service_url                      | core | string        | Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.                                                                                                                                               |
| source_api_id                    | core | string        | API identifier of the source API.                                                                                                                                                                                                                  |
| subscription_id                  | core | string        |
| subscription_key_parameter_names | core | json          | Protocols over which API is made available.                                                                                                                                                                                                        |
| subscription_name                | core | string        |
| subscription_required            | core | bool          | Specifies whether an API or Product subscription is required for accessing the API.                                                                                                                                                                |
| tags                             | core | hstore_csv    |
| terms_of_service_url             | core | string        | A URL to the Terms of Service for the API. MUST be in the format of a URL.                                                                                                                                                                         |
| type                             | core | string        | Type of API.                                                                                                                                                                                                                                       |
