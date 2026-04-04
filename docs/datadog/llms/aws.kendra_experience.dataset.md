# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kendra_experience.dataset.md

---
title: Amazon Kendra Experience
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amazon Kendra Experience
---

# Amazon Kendra Experience

Amazon Kendra Experience is a feature that allows users to create and manage customized search experiences powered by Amazon Kendra. It defines how end users interact with search results, including user interfaces, access controls, and personalization settings. This resource provides details about an existing experience, such as its configuration, status, and associated data sources.

```
aws.kendra_experience
```

## Fields

| Title         | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                           | Description |
| ------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| configuration | core | json       | Shows the configuration information for your Amazon Kendra experience. This includes ContentSourceConfiguration, which specifies the data source IDs and/or FAQ IDs, and UserIdentityConfiguration, which specifies the user or group information to grant access to your Amazon Kendra experience. |
| created_at    | core | timestamp  | The Unix timestamp when your Amazon Kendra experience was created.                                                                                                                                                                                                                                  |
| description   | core | string     | Shows the description for your Amazon Kendra experience.                                                                                                                                                                                                                                            |
| endpoints     | core | json       | Shows the endpoint URLs for your Amazon Kendra experiences. The URLs are unique and fully hosted by Amazon Web Services.                                                                                                                                                                            |
| error_message | core | string     | The reason your Amazon Kendra experience could not properly process.                                                                                                                                                                                                                                |
| id            | core | string     | Shows the identifier of your Amazon Kendra experience.                                                                                                                                                                                                                                              |
| index_id      | core | string     | Shows the identifier of the index for your Amazon Kendra experience.                                                                                                                                                                                                                                |
| name          | core | string     | Shows the name of your Amazon Kendra experience.                                                                                                                                                                                                                                                    |
| role_arn      | core | string     | The Amazon Resource Name (ARN) of the IAM role with permission to access the Query API, QuerySuggestions API, SubmitFeedback API, and IAM Identity Center that stores your users and groups information.                                                                                            |
| status        | core | string     | The current processing status of your Amazon Kendra experience. When the status is ACTIVE, your Amazon Kendra experience is ready to use. When the status is FAILED, the ErrorMessage field contains the reason that this failed.                                                                   |
| tags          | core | hstore_csv |
| updated_at    | core | timestamp  | The Unix timestamp when your Amazon Kendra experience was last updated.                                                                                                                                                                                                                             |
