# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_authorizer.dataset.md

---
title: IoT Authorizer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Authorizer
---

# IoT Authorizer

IoT Authorizer in AWS is a custom authorization component for AWS IoT Core that allows you to define how devices and clients authenticate when connecting to the IoT message broker or Device Gateway. It enables the use of custom authentication logic, such as token-based systems or third-party identity providers, giving flexibility beyond standard AWS IoT authentication methods.

```
aws.iot_authorizer
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                          | Description |
| ------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| authorizer_arn            | core | string     | The authorizer ARN.                                                                                                                                                                                |
| authorizer_function_arn   | core | string     | The authorizer's Lambda function ARN.                                                                                                                                                              |
| authorizer_name           | core | string     | The authorizer name.                                                                                                                                                                               |
| creation_date             | core | timestamp  | The UNIX timestamp of when the authorizer was created.                                                                                                                                             |
| enable_caching_for_http   | core | bool       | When true, the result from the authorizer's Lambda function is cached for the time specified in refreshAfterInSeconds. The cached result is used while the device reuses the same HTTP connection. |
| last_modified_date        | core | timestamp  | The UNIX timestamp of when the authorizer was last updated.                                                                                                                                        |
| signing_disabled          | core | bool       | Specifies whether IoT validates the token signature in an authorization request.                                                                                                                   |
| status                    | core | string     | The status of the authorizer.                                                                                                                                                                      |
| tags                      | core | hstore_csv |
| token_key_name            | core | string     | The key used to extract the token from the HTTP headers.                                                                                                                                           |
| token_signing_public_keys | core | hstore     | The public keys used to validate the token signature returned by your custom authentication service.                                                                                               |
