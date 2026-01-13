# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_location_nfs.dataset.md

---
title: DataSync NFS Location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataSync NFS Location
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.datasync_location_nfs.dataset/index.html
---

# DataSync NFS Location

DataSync NFS Location in AWS represents a Network File System (NFS) endpoint that DataSync can use as a source or destination for data transfers. It defines the NFS server, mount path, and related configuration details, enabling secure and efficient movement of files between on-premises storage, other NFS servers, and AWS storage services.

```
aws.datasync_location_nfs
```

## Fields

| Title          | ID   | Type      | Data Type                                                                           | Description |
| -------------- | ---- | --------- | ----------------------------------------------------------------------------------- | ----------- |
| _key           | core | string    |
| account_id     | core | string    |
| creation_time  | core | timestamp | The time when the NFS location was created.                                         |
| location_arn   | core | string    | The ARN of the NFS location.                                                        |
| location_uri   | core | string    | The URI of the NFS location.                                                        |
| mount_options  | core | json      | The mount options that DataSync uses to mount your NFS file server.                 |
| on_prem_config | core | json      | The DataSync agents that can connect to your Network File System (NFS) file server. |
| tags           | core | hstore    |
