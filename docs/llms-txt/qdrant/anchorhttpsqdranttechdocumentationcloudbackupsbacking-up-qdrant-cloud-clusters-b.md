# [Anchor](https://qdrant.tech/documentation/cloud/backups/\#backing-up-qdrant-cloud-clusters) Backing up Qdrant Cloud Clusters

Qdrant organizes cloud instances as clusters. On occasion, you may need to
restore your cluster because of application or system failure.

You may already have a source of truth for your data in a regular database. If you
have a problem, you could reindex the data into your Qdrant vector search cluster.
However, this process can take time. For high availability critical projects we
recommend replication. It guarantees the proper cluster functionality as long as
at least one replica is running.

For other use-cases such as disaster recovery, you can set up automatic or
self-service backups.

## [Anchor](https://qdrant.tech/documentation/cloud/backups/\#prerequisites) Prerequisites

You can back up your Qdrant clusters though the Qdrant Cloud
Dashboard at [https://cloud.qdrant.io](https://cloud.qdrant.io/). This section assumes that you’ve already
set up your cluster, as described in the following sections:

- [Create a cluster](https://qdrant.tech/documentation/cloud/create-cluster/)
- Set up [Authentication](https://qdrant.tech/documentation/cloud/authentication/)
- Configure one or more [Collections](https://qdrant.tech/documentation/concepts/collections/)

## [Anchor](https://qdrant.tech/documentation/cloud/backups/\#automatic-backups) Automatic Backups

You can set up automatic backups of your clusters with our Cloud UI. With the
procedures listed in this page, you can set up
snapshots on a daily/weekly/monthly basis. You can keep as many snapshots as you
need. You can restore a cluster from the snapshot of your choice.

> Note: When you restore a snapshot, consider the following:
>
> - The affected cluster is not available while a snapshot is being restored.
> - If you changed the cluster setup after the copy was created, the cluster
>   resets to the previous configuration.
> - The previous configuration includes:
>   - CPU
>   - Memory
>   - Node count
>   - Qdrant version

### [Anchor](https://qdrant.tech/documentation/cloud/backups/\#configure-a-backup) Configure a Backup

After you have taken the prerequisite steps, you can configure a backup with the
[Qdrant Cloud Dashboard](https://cloud.qdrant.io/). To do so, take these steps:

1. On the **Cluster Detail Page** and select the **Backups** tab.
2. Now you can set up a backup schedule.
The **Days of Retention** is the number of days after a backup snapshot is
deleted.
3. Alternatively, you can select **Backup now** to take an immediate snapshot.

![Configure a cluster backup](https://qdrant.tech/documentation/cloud/backup-schedule.png)

### [Anchor](https://qdrant.tech/documentation/cloud/backups/\#restore-a-backup) Restore a Backup

If you have a backup, it appears in the list of **Available Backups**. You can
choose to restore or delete the backups of your choice.

![Restore or delete a cluster backup](https://qdrant.tech/documentation/cloud/restore-delete.png)

## [Anchor](https://qdrant.tech/documentation/cloud/backups/\#backups-with-a-snapshot) Backups With a Snapshot

Qdrant also offers a snapshot API which allows you to create a snapshot
of a specific collection or your entire cluster. For more information, see our
[snapshot documentation](https://qdrant.tech/documentation/concepts/snapshots/).

Here is how you can take a snapshot and recover a collection:

1. Take a snapshot:
   - For a single node cluster, call the snapshot endpoint on the exposed URL.
   - For a multi node cluster call a snapshot on each node of the collection.
     Specifically, prepend `node-{num}-` to your cluster URL.
     Then call the [snapshot endpoint](https://qdrant.tech/documentation/concepts/snapshots/#create-snapshot) on the individual hosts. Start with node 0.
   - In the response, you’ll see the name of the snapshot.
2. Delete and recreate the collection.
3. Recover the snapshot:
   - Call the [recover endpoint](https://qdrant.tech/documentation/concepts/snapshots/#recover-in-cluster-deployment). Set a location which points to the snapshot file ( `file:///qdrant/snapshots/{collection_name}/{snapshot_file_name}`) for each host.

## [Anchor](https://qdrant.tech/documentation/cloud/backups/\#backup-considerations) Backup Considerations

Backups are incremental for AWS and GCP clusters. For example, if you have two backups, backup number 2
contains only the data that changed since backup number 1. This reduces the
total cost of your backups.

For Azure clusters, backups are based on total disk usage. The cost is calculated
as half of the disk usage when the backup was taken.

You can create multiple backup schedules.

When you restore a snapshot, any changes made after the date of the snapshot
are lost.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/backups.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/backups.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-84-lllmstxt|>
## qdrant-1.3.x
- [Articles](https://qdrant.tech/articles/)
- Introducing Qdrant 1.3.0

[Back to Qdrant Articles](https://qdrant.tech/articles/)