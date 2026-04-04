# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotsitewise_portal.dataset.md

---
title: IoT SiteWise Portal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT SiteWise Portal
---

# IoT SiteWise Portal

AWS IoT SiteWise Portal is a managed web application that provides a user-friendly interface for visualizing and monitoring industrial data collected through IoT SiteWise. It allows organizations to create portals where users can securely access dashboards, analyze equipment performance, and gain insights into operational data without needing to build custom applications.

```
aws.iotsitewise_portal
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                                                                                                                                                                                                   | Description |
| -------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| alarms                     | core | json       | Contains the configuration information of an alarm created in an IoT SiteWise Monitor portal.                                                                                                                                                                               |
| notification_sender_email  | core | string     | The email address that sends alarm notifications.                                                                                                                                                                                                                           |
| portal_arn                 | core | string     | The ARN of the portal, which has the following format. arn:${Partition}:iotsitewise:${Region}:${Account}:portal/${PortalId}                                                                                                                                                 |
| portal_auth_mode           | core | string     | The service to use to authenticate users to the portal.                                                                                                                                                                                                                     |
| portal_client_id           | core | string     | The IAM Identity Center application generated client ID (used with IAM Identity Center API operations). IoT SiteWise includes portalClientId for only portals that use IAM Identity Center to authenticate users.                                                           |
| portal_contact_email       | core | string     | The Amazon Web Services administrator's contact email address.                                                                                                                                                                                                              |
| portal_creation_date       | core | timestamp  | The date the portal was created, in Unix epoch time.                                                                                                                                                                                                                        |
| portal_description         | core | string     | The portal's description.                                                                                                                                                                                                                                                   |
| portal_id                  | core | string     | The ID of the portal.                                                                                                                                                                                                                                                       |
| portal_last_update_date    | core | timestamp  | The date the portal was last updated, in Unix epoch time.                                                                                                                                                                                                                   |
| portal_logo_image_location | core | json       | The portal's logo image, which is available at a URL.                                                                                                                                                                                                                       |
| portal_name                | core | string     | The name of the portal.                                                                                                                                                                                                                                                     |
| portal_start_url           | core | string     | The URL for the IoT SiteWise Monitor portal. You can use this URL to access portals that use IAM Identity Center for authentication. For portals that use IAM for authentication, you must use the IoT SiteWise console to get a URL that you can use to access the portal. |
| portal_status              | core | json       | The current status of the portal, which contains a state and any error message.                                                                                                                                                                                             |
| portal_type                | core | string     | Define the type of portal. The value for IoT SiteWise Monitor (Classic) is SITEWISE_PORTAL_V1. The value for IoT SiteWise Monitor (AI-aware) is SITEWISE_PORTAL_V2.                                                                                                         |
| portal_type_configuration  | core | string     | The configuration entry associated with the specific portal type. The value for IoT SiteWise Monitor (Classic) is SITEWISE_PORTAL_V1. The value for IoT SiteWise Monitor (AI-aware) is SITEWISE_PORTAL_V2.                                                                  |
| role_arn                   | core | string     | The ARN of the service role that allows the portal's users to access your IoT SiteWise resources on your behalf. For more information, see Using service roles for IoT SiteWise Monitor in the IoT SiteWise User Guide.                                                     |
| tags                       | core | hstore_csv |
