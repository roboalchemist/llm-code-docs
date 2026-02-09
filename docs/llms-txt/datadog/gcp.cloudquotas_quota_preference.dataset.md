# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudquotas_quota_preference.dataset.md

---
title: Quota Preference
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Quota Preference
---

# Quota Preference

Quota Preference in Google Cloud Platform allows users to define and manage preferences for quota usage and allocation across projects or services. It helps control resource consumption by setting limits or preferences for specific APIs or resource types, ensuring efficient usage and preventing unexpected quota exhaustion.

```
gcp.cloudquotas_quota_preference
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| contact_email        | core | string        | Input only. An email address that can be used to contact the user, in case Google Cloud needs more information to make a decision before additional quota can be granted. When requesting a quota increase, the email address is required. When requesting a quota decrease, the email address is optional. For example, the email address is optional when the `QuotaConfig.preferred_value` is smaller than the `QuotaDetails.reset_value`. |
| create_time          | core | timestamp     | Output only. Create time stamp                                                                                                                                                                                                                                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| etag                 | core | string        | Optional. The current etag of the quota preference. If an etag is provided on update and does not match the current server's etag of the quota preference, the request will be blocked and an ABORTED error will be returned. See https://google.aip.dev/134#etags for more details on etags.                                                                                                                                                 |
| justification        | core | string        | The reason / justification for this quota preference.                                                                                                                                                                                                                                                                                                                                                                                         |
| labels               | core | array<string> |
| name                 | core | string        | Required except in the CREATE requests. The resource name of the quota preference. The path that follows `/locations` must be `/global`. For example: `projects/123/locations/global/quotaPreferences/my-config-for-us-east1`                                                                                                                                                                                                                 |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| quota_config         | core | json          | Required. Preferred quota configuration.                                                                                                                                                                                                                                                                                                                                                                                                      |
| quota_id             | core | string        | Required. The id of the quota to which the quota preference is applied. A quota name is unique in the service. For example, `CpusPerProjectPerRegion`                                                                                                                                                                                                                                                                                         |
| reconciling          | core | bool          | Output only. Is the quota preference pending Google Cloud approval and fulfillment.                                                                                                                                                                                                                                                                                                                                                           |
| region_id            | core | string        |
| resource_name        | core | string        |
| service              | core | string        | Required. The name of the service to which the quota preference is applied.                                                                                                                                                                                                                                                                                                                                                                   |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Update time stamp                                                                                                                                                                                                                                                                                                                                                                                                                |
| zone_id              | core | string        |
