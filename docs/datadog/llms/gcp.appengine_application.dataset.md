# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.appengine_application.dataset.md

---
title: App Engine Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > App Engine Application
---

# App Engine Application

App Engine Application is a fully managed platform on Google Cloud for building and running web applications. It automatically handles infrastructure concerns such as scaling, load balancing, and monitoring. Developers can deploy code in multiple languages and frameworks without managing servers. It supports both standard and flexible environments, allowing for quick development and easy integration with other Google Cloud services.

```
gcp.appengine_application
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                        | Description |
| ------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| ancestors                 | core | array<string> |
| auth_domain               | core | string        | Google Apps authentication domain that controls which users can access this application.Defaults to open access for any Google Account.                                                                                                                                                                          |
| code_bucket               | core | string        | Output only. Google Cloud Storage bucket that can be used for storing files associated with this application. This bucket is associated with the application and can be used by the gcloud deployment commands.@OutputOnly                                                                                       |
| database_type             | core | string        | The type of the Cloud Firestore or Cloud Datastore database associated with this application.                                                                                                                                                                                                                    |
| datadog_display_name      | core | string        |
| default_bucket            | core | string        | Output only. Google Cloud Storage bucket that can be used by this application to store content.@OutputOnly                                                                                                                                                                                                       |
| default_cookie_expiration | core | string        | Cookie expiration policy for this application.                                                                                                                                                                                                                                                                   |
| default_hostname          | core | string        | Output only. Hostname used to reach this application, as resolved by App Engine.@OutputOnly                                                                                                                                                                                                                      |
| dispatch_rules            | core | json          | HTTP path dispatch rules for requests to the application that do not explicitly target a service or version. Rules are order-dependent. Up to 20 dispatch rules can be supported.                                                                                                                                |
| feature_settings          | core | json          | The feature specific settings to be used in the application.                                                                                                                                                                                                                                                     |
| gcr_domain                | core | string        | Output only. The Google Container Registry domain used for storing managed build docker images for this application.                                                                                                                                                                                             |
| iap                       | core | json          |
| id                        | core | string        | Identifier of the Application resource. This identifier is equivalent to the project ID of the Google Cloud Platform project where you want to deploy your application. Example: myapp.                                                                                                                          |
| labels                    | core | array<string> |
| location_id               | core | string        | Location from which this application runs. Application instances run out of the data centers in the specified location, which is also where all of the application's end user content is stored.Defaults to us-central.View the list of supported locations (https://cloud.google.com/appengine/docs/locations). |
| name                      | core | string        | Output only. Full path to the Application resource in the API. Example: apps/myapp.@OutputOnly                                                                                                                                                                                                                   |
| organization_id           | core | string        |
| parent                    | core | string        |
| project_id                | core | string        |
| project_number            | core | string        |
| region_id                 | core | string        |
| resource_name             | core | string        |
| service_account           | core | string        | The service account associated with the application. This is the app-level default identity. If no identity provided during create version, Admin API will fallback to this one.                                                                                                                                 |
| serving_status            | core | string        | Serving status of this application.                                                                                                                                                                                                                                                                              |
| ssl_policy                | core | string        | The SSL policy that will be applied to the application. If set to Modern it will restrict traffic with TLS < 1.2 and allow only Modern Ciphers suite                                                                                                                                                             |
| tags                      | core | hstore_csv    |
| zone_id                   | core | string        |
