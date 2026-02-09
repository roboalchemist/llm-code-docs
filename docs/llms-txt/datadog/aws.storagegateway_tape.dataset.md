# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.storagegateway_tape.dataset.md

---
title: Storage Gateway Virtual Tape
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Storage Gateway Virtual Tape
---

# Storage Gateway Virtual Tape

AWS Storage Gateway Virtual Tape is a cloud-based storage resource that emulates physical tape libraries, enabling you to back up and archive data to Amazon S3 or Amazon S3 Glacier. It integrates with existing backup applications, allowing organizations to replace or extend on-premises tape infrastructure with scalable, durable, and cost-effective cloud storage.

```
aws.storagegateway_tape
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                      | Description |
| -------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| pool_entry_date      | core | timestamp  | The date that the tape enters a custom tape pool.                                                                                                                                                                                                                                                                                              |
| pool_id              | core | string     | The ID of the pool that contains tapes that will be archived. The tapes in this pool are archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool. |
| progress             | core | float64    | For archiving virtual tapes, indicates how much data remains to be uploaded before archiving is complete. Range: 0 (not started) to 100 (complete).                                                                                                                                                                                            |
| retention_start_date | core | timestamp  | The date that the tape is first archived with tape retention lock enabled.                                                                                                                                                                                                                                                                     |
| tags                 | core | hstore_csv |
| tape_arn             | core | string     | The Amazon Resource Name (ARN) of the virtual tape.                                                                                                                                                                                                                                                                                            |
| tape_barcode         | core | string     | The barcode that identifies a specific virtual tape.                                                                                                                                                                                                                                                                                           |
| tape_created_date    | core | timestamp  | The date the virtual tape was created.                                                                                                                                                                                                                                                                                                         |
| tape_size_in_bytes   | core | int64      | The size, in bytes, of the virtual tape capacity.                                                                                                                                                                                                                                                                                              |
| tape_status          | core | string     | The current state of the virtual tape.                                                                                                                                                                                                                                                                                                         |
| tape_used_in_bytes   | core | int64      | The size, in bytes, of data stored on the virtual tape. This value is not available for tapes created prior to May 13, 2015.                                                                                                                                                                                                                   |
| vtl_device           | core | string     | The virtual tape library (VTL) device that the virtual tape is associated with.                                                                                                                                                                                                                                                                |
| worm                 | core | bool       | If the tape is archived as write-once-read-many (WORM), this value is true.                                                                                                                                                                                                                                                                    |
