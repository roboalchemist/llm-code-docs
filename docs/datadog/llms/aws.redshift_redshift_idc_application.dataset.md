# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshift_redshift_idc_application.dataset.md

---
title: Redshift Redshift Idc Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift Redshift Idc Application
---

# Redshift Redshift Idc Application

This table represents the Redshift Redshift Idc Application resource from Amazon Web Services.

```
aws.redshift_redshift_idc_application
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                              | Description |
| ----------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| authorized_token_issuer_list  | core | json       | The authorized token issuer list for the Amazon Redshift IAM Identity Center application.                                                              |
| iam_role_arn                  | core | string     | The ARN for the Amazon Redshift IAM Identity Center application. It has the required permissions to be assumed and invoke the IDC Identity Center API. |
| idc_display_name              | core | string     | The display name for the Amazon Redshift IAM Identity Center application. It appears on the console.                                                   |
| idc_instance_arn              | core | string     | The ARN for the IAM Identity Center instance that Redshift integrates with.                                                                            |
| idc_managed_application_arn   | core | string     | The ARN for the Amazon Redshift IAM Identity Center application.                                                                                       |
| idc_onboard_status            | core | string     | The onboarding status for the Amazon Redshift IAM Identity Center application.                                                                         |
| identity_namespace            | core | string     | The identity namespace for the Amazon Redshift IAM Identity Center application. It determines which managed application verifies the connection token. |
| redshift_idc_application_arn  | core | string     | The ARN for the Redshift application that integrates with IAM Identity Center.                                                                         |
| redshift_idc_application_name | core | string     | The name of the Redshift application in IAM Identity Center.                                                                                           |
| service_integrations          | core | json       | A list of service integrations for the Redshift IAM Identity Center application.                                                                       |
| tags                          | core | hstore_csv |
