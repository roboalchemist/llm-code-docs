# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.s3_access_grant.dataset.md

---
title: S3 Access Grant
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > S3 Access Grant
---

# S3 Access Grant

This table represents the S3 Access Grant resource from Amazon Web Services.

```
aws.s3_access_grant
```

## Fields

| Title                                | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                    | Description |
| ------------------------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string     |
| access_grant_arn                     | core | string     | The Amazon Resource Name (ARN) of the access grant.                                                                                                                                                                                                                                                                                          |
| access_grant_id                      | core | string     | The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access grant.                                                                                                                                                                                                                                        |
| access_grants_location_configuration | core | json       | The configuration options of the grant location. The grant location is the S3 path to the data to which you are granting access.                                                                                                                                                                                                             |
| access_grants_location_id            | core | string     | The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register.                                  |
| account_id                           | core | string     |
| application_arn                      | core | string     | The Amazon Resource Name (ARN) of an Amazon Web Services IAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application.                                                                                          |
| created_at                           | core | timestamp  | The date and time when you created the S3 Access Grants instance.                                                                                                                                                                                                                                                                            |
| grant_scope                          | core | string     | The S3 path of the data to which you are granting access. It is the result of appending the <code>Subprefix</code> to the location scope.                                                                                                                                                                                                    |
| grantee                              | core | json       | The user, group, or role to which you are granting access. You can grant access to an IAM user or role. If you have added your corporate directory to Amazon Web Services IAM Identity Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee can also be a corporate directory user or group. |
| permission                           | core | string     | The type of access granted to your S3 data, which can be set to one of the following values: <ul> <li> <code>READ</code> â Grant read-only access to the S3 data. </li> <li> <code>WRITE</code> â Grant write-only access to the S3 data. </li> <li> <code>READWRITE</code> â Grant both read and write access to the S3 data. </li> </ul>   |
| tags                                 | core | hstore_csv |
