# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.gamelift_build.dataset.md

---
title: GameLift Build
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GameLift Build
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.gamelift_build.dataset/index.html
---

# GameLift Build

GameLift Build in AWS represents a set of game server binaries and related files that you upload to Amazon GameLift for deployment. It is the packaged version of your game server that GameLift uses to create fleets and host multiplayer game sessions. A build includes the executable and any supporting assets required to run your game server in the cloud.

```
aws.gamelift_build
```

## Fields

| Title              | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| ------------------ | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string    |
| account_id         | core | string    |
| build_arn          | core | string    | The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift Servers build resource and uniquely identifies it. ARNs are unique across all Regions. Format is arn:aws:gamelift:<region>::build/build-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912. In a GameLift build ARN, the resource ID matches the BuildId value.                                                                                                                                                                               |
| build_id           | core | string    | A unique identifier for the build.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| creation_time      | core | timestamp | A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").                                                                                                                                                                                                                                                                                                                                                 |
| name               | core | string    | A descriptive label that is associated with a build. Build names do not need to be unique. It can be set using CreateBuild or UpdateBuild.                                                                                                                                                                                                                                                                                                                                                           |
| operating_system   | core | string    | Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the Amazon Linux 2 FAQs. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See Migrate to server SDK version 5. |
| server_sdk_version | core | string    | The Amazon GameLift Servers Server SDK version used to develop your game server.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| size_on_disk       | core | int64     | File size of the uploaded game build, expressed in bytes. When the build status is INITIALIZED or when using a custom Amazon S3 storage location, this value is 0.                                                                                                                                                                                                                                                                                                                                   |
| status             | core | string    | Current status of the build. Possible build statuses include the following: INITIALIZED -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value. READY -- The game build has been successfully uploaded. You can now create new fleets for this build. FAILED -- The game build upload failed. You cannot create new fleets for this build.       |
| tags               | core | hstore    |
| version            | core | string    | Version information that is associated with a build or script. Version strings do not need to be unique.                                                                                                                                                                                                                                                                                                                                                                                             |
