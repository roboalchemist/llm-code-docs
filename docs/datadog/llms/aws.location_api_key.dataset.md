# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.location_api_key.dataset.md

---
title: Location API Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Location API Key
---

# Location API Key

This table represents the Location API Key resource from Amazon Web Services.

```
aws.location_api_key
```

## Fields

| Title        | ID   | Type       | Data Type                                                                                                                                                                                                                         | Description |
| ------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key         | core | string     |
| account_id   | core | string     |
| create_time  | core | timestamp  | The timestamp for when the API key resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.                                          |
| description  | core | string     | The optional description for the API key resource.                                                                                                                                                                                |
| expire_time  | core | timestamp  | The timestamp for when the API key resource will expire in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.                                          |
| key          | core | string     | The key value/string of an API key.                                                                                                                                                                                               |
| key_arn      | core | string     | The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all Amazon Web Services. <ul> <li> Format example: <code>arn:aws:geo:region:account-id:key/ExampleKey</code> </li> </ul> |
| key_name     | core | string     | The name of the API key resource.                                                                                                                                                                                                 |
| restrictions | core | json       |
| tags         | core | hstore_csv |
| update_time  | core | timestamp  | The timestamp for when the API key resource was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.                                     |
