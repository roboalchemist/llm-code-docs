# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.qbusiness_web_experience.dataset.md

---
title: Q Business Web Experience
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Q Business Web Experience
---

# Q Business Web Experience

Q Business Web Experience in AWS provides a way to access and interact with Q Business applications through a web-based interface. It enables users to manage, view, and engage with business data and workflows directly from a browser without requiring additional client software. This resource is part of the Q Business service, designed to simplify user access and improve productivity by delivering a streamlined web experience.

```
aws.qbusiness_web_experience
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                                                                                                                                  | Description |
| ------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string        |
| account_id                      | core | string        |
| application_id                  | core | string        | The identifier of the Amazon Q Business application linked to the web experience.                                                                                                                                                                          |
| authentication_configuration    | core | json          | The authentication configuration information for your Amazon Q Business web experience.                                                                                                                                                                    |
| browser_extension_configuration | core | json          | The browser extension configuration for an Amazon Q Business web experience.                                                                                                                                                                               |
| created_at                      | core | timestamp     | The Unix timestamp when the Amazon Q Business web experience was last created.                                                                                                                                                                             |
| customization_configuration     | core | json          | Gets the custom logo, favicon, font, and color used in the Amazon Q web experience.                                                                                                                                                                        |
| default_endpoint                | core | string        | The endpoint of your Amazon Q Business web experience.                                                                                                                                                                                                     |
| error                           | core | json          | When the Status field value is FAILED, the ErrorMessage field contains a description of the error that caused the data source connector to fail.                                                                                                           |
| identity_provider_configuration | core | json          | Information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.                                                                                                                                       |
| origins                         | core | array<string> | Gets the website domain origins that are allowed to embed the Amazon Q Business web experience. The domain origin refers to the base URL for accessing a website including the protocol (http/https), the domain name, and the port number (if specified). |
| role_arn                        | core | string        | The Amazon Resource Name (ARN) of the service role attached to your web experience.                                                                                                                                                                        |
| sample_prompts_control_mode     | core | string        | Determines whether sample prompts are enabled in the web experience for an end user.                                                                                                                                                                       |
| status                          | core | string        | The current status of the Amazon Q Business web experience. When the Status field value is FAILED, the ErrorMessage field contains a description of the error that caused the data source connector to fail.                                               |
| subtitle                        | core | string        | The subtitle for your Amazon Q Business web experience.                                                                                                                                                                                                    |
| tags                            | core | hstore_csv    |
| title                           | core | string        | The title for your Amazon Q Business web experience.                                                                                                                                                                                                       |
| updated_at                      | core | timestamp     | The Unix timestamp when the Amazon Q Business web experience was last updated.                                                                                                                                                                             |
| web_experience_arn              | core | string        | The Amazon Resource Name (ARN) of the role with the permission to access the Amazon Q Business web experience and required resources.                                                                                                                      |
| web_experience_id               | core | string        | The identifier of the Amazon Q Business web experience.                                                                                                                                                                                                    |
| welcome_message                 | core | string        | The customized welcome message for end users of an Amazon Q Business web experience.                                                                                                                                                                       |
