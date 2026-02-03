# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sso_application.dataset.md

---
title: IAM Identity Center Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM Identity Center Application
---

# IAM Identity Center Application

IAM Identity Center Application in AWS represents an application that can be integrated with AWS IAM Identity Center (formerly AWS SSO) to provide single sign-on access for users. It allows administrators to configure and manage access to external or custom applications, enabling centralized authentication and authorization. This resource helps streamline user access management by connecting applications to the identity center, ensuring secure and consistent sign-in experiences across environments.

```
aws.sso_application
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                                                                                 | Description |
| ------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| application_account      | core | string     | The Amazon Web Services account ID number of the application.                                                                                                                                                             |
| application_arn          | core | string     | The ARN of the application.                                                                                                                                                                                               |
| application_assignments  | core | json       | The list of users assigned to an application.                                                                                                                                                                             |
| application_provider_arn | core | string     | The ARN of the application provider for this application.                                                                                                                                                                 |
| assignment_required      | core | bool       | If AssignmentsRequired is true (default value), users don't have access to the application unless an assignment is created using the CreateApplicationAssignment API. If false, all users have access to the application. |
| created_date             | core | timestamp  | The date and time when the application was originally created.                                                                                                                                                            |
| description              | core | string     | The description of the application.                                                                                                                                                                                       |
| instance_arn             | core | string     | The ARN of the instance of IAM Identity Center that is configured with this application.                                                                                                                                  |
| name                     | core | string     | The name of the application.                                                                                                                                                                                              |
| portal_options           | core | json       | A structure that describes the options for the access portal associated with this application.                                                                                                                            |
| status                   | core | string     | The current status of the application in this instance of IAM Identity Center.                                                                                                                                            |
| tags                     | core | hstore_csv |
