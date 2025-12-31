# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/operation-restricted-to-availability.md

# Operation Restricted to Availability Zone(s)

## Cause

Since there is varied support for container profiles per availability zone (AZ), [scaling](/core-concepts/scaling/overview) a database to a different [container profile](/core-concepts/scaling/container-profiles) may require moving the database to a different AZ. Moving a database to a different AZ requires a complete backup and restore of the underlying disk, which results in downtime of a few minutes up to even hours, depending on the size of the disk.

To protect your service from unexpected downtime, scaling to a container profile that requires an AZ move will result in an error and no change to your service. The error you see in logs will look something like:

```
ERROR -- : Operation restricted to availability zone(s) us-east-1e where m5 is not available. Disks cannot be moved to a different availability zone without a complete backup and restore.
```

## Resolution

If you still want to scale to a container profile that will result in an availability zone move, you can plan for the backup and restore by first looking at recent database backups and noting the time it took them to complete. You should expect roughly this amount of downtime for the **backup only**. You can speed up the backup portion of the move by creating a manual backup before running the operation since backups are incremental.

When restoring your database from a backup, you may initially experience slower performance. This slowdown occurs because each block on the restored volume is read for the first time from slower, long-term storage. This 'first-time' read is required for each block and affects different databases in various ways:

* For large PostgreSQL databases with busy access patterns and longer-than-default checkpoint periods, you may face delays of several minutes or more. This is due to the need to read WAL files before the database becomes online and starts accepting connections.

* Redis databases with persistence enabled could see delays in startup times as disk-based data must be read back into memory before the database is online and accepting connections.

* Databases executing disk-intensive queries will experience slower initial query performance as the data blocks are first read from the volume.

Depending on the amount of data your database needs to load into memory to start serving connections, this part of the downtime could be significant and might take more than an hour for larger databases. If you're running a large or busy database, we strongly recommend testing this operation on a non-production instance to estimate the total downtime involved.

When you're ready to move, go to the Aptible Dashboard, find your database, go to the settings panel, and select the container profile you wish to migrate to in the "Restart Database with Disk Backup and Restore" panel. After acknowledging the warning about downtime, click the button and your container profile scaling operation will begin.
