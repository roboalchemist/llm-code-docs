# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_playback_restriction_policy.dataset.md

---
title: IVS Playback Restriction Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IVS Playback Restriction Policy
---

# IVS Playback Restriction Policy

An IVS Playback Restriction Policy in AWS defines rules that control where and how Amazon Interactive Video Service streams can be played. It allows you to restrict playback based on criteria such as specific domains or geographic locations, helping secure content delivery and ensuring streams are only accessible to authorized viewers.

```
aws.ivs_playback_restriction_policy
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                                                                                                                                                                                  | Description |
| -------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                             | core | string        |
| account_id                       | core | string        |
| allowed_countries                | core | array<string> | A list of country codes that control geoblocking restriction. Allowed values are the officially assigned ISO 3166-1 alpha-2 codes. Default: All countries (an empty array).                                                                |
| allowed_origins                  | core | array<string> | A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin. Default: All origins (an empty array). |
| arn                              | core | string        | Playback-restriction-policy ARN                                                                                                                                                                                                            |
| enable_strict_origin_enforcement | core | bool          | Whether channel playback is constrained by origin site. Default: false.                                                                                                                                                                    |
| name                             | core | string        | Playback-restriction-policy name. The value does not need to be unique.                                                                                                                                                                    |
| tags                             | core | hstore_csv    |
