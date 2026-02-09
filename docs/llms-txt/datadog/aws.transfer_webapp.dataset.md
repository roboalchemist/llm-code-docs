# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transfer_webapp.dataset.md

---
title: Transfer Family Webapp
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transfer Family Webapp
---

# Transfer Family Webapp

This table represents the Transfer Family Webapp resource from Amazon Web Services.

```
aws.transfer_webapp
```

## Fields

| Title                               | ID   | Type       | Data Type                                                                                                                                                                               | Description |
| ----------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string     |
| access_endpoint                     | core | string     | The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value. |
| account_id                          | core | string     |
| arn                                 | core | string     | The Amazon Resource Name (ARN) of the web app.                                                                                                                                          |
| described_identity_provider_details | core | json       | A structure that contains the details for the identity provider used by the web app.                                                                                                    |
| tags                                | core | hstore_csv |
| web_app_endpoint                    | core | string     | The <code>WebAppEndpoint</code> is the unique URL for your Transfer Family web app. This is the value that you use when you configure <b>Origins</b> on CloudFront.                     |
| web_app_id                          | core | string     | The unique identifier for the web app.                                                                                                                                                  |
| web_app_units                       | core | json       | A union that contains the value for number of concurrent connections or the user sessions on your web app.                                                                              |
