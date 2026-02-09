# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.serverlessrepo_applications.dataset.md

---
title: Serverlessrepo Applications
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Serverlessrepo Applications
---

# Serverlessrepo Applications

This table represents the serverlessrepo_applications resource from Amazon Web Services.

```
aws.serverlessrepo_applications
```

## Fields

| Title               | ID   | Type          | Data Type                                                                                                                                                                                                                                                                   | Description |
| ------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| application_id      | core | string        | The application Amazon Resource Name (ARN).                                                                                                                                                                                                                                 |
| author              | core | string        | The name of the author publishing the app.Minimum length=1. Maximum length=127.Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";                                                                                                                                           |
| creation_time       | core | string        | The date and time this resource was created.                                                                                                                                                                                                                                |
| description         | core | string        | The description of the application.Minimum length=1. Maximum length=256                                                                                                                                                                                                     |
| home_page_url       | core | string        | A URL with more information about the application, for example the location of your GitHub repository for the application.                                                                                                                                                  |
| is_verified_author  | core | bool          | Whether the author of this application has been verified. This means means that AWS has made a good faith review, as a reasonable and prudent service provider, of the information provided by the requester and has confirmed that the requester's identity is as claimed. |
| labels              | core | array<string> | Labels to improve discovery of apps in search results.Minimum length=1. Maximum length=127. Maximum number of labels: 10Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";                                                                                                                |
| license_url         | core | string        | A link to a license file of the app that matches the spdxLicenseID value of your application.Maximum size 5 MB                                                                                                                                                              |
| name                | core | string        | The name of the application.Minimum length=1. Maximum length=140Pattern: "[a-zA-Z0-9\\-]+";                                                                                                                                                                                 |
| readme_url          | core | string        | A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.Maximum size 5 MB                                                                                                                              |
| spdx_license_id     | core | string        | A valid identifier from https://spdx.org/licenses/.                                                                                                                                                                                                                         |
| tags                | core | hstore_csv    |
| verified_author_url | core | string        | The URL to the public profile of a verified author. This URL is submitted by the author.                                                                                                                                                                                    |
| version             | core | json          | Version information about the application.                                                                                                                                                                                                                                  |
