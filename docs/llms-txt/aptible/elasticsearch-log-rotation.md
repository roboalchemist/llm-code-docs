# Source: https://www.aptible.com/docs/how-to-guides/observability-guides/elasticsearch-log-rotation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up Elasticsearch Log Rotation

> ❗️ These instructions apply only to Kibana/Elasticsearch versions 7.4 or higher. Earlier versions of Elasticsearch and Kibana did not provide all of the UI features mentioned in this guide. Instead, for version 6.8 or earlier, refer to our [aptible/elasticsearch-logstash-s3-backup](https://github.com/aptible/elasticsearch-logstash-s3-backup) application.

If you're using Elasticsearch to hold log data, you'll almost certainly be creating new indexes periodically - by default, Logstash or Aptible [log drains](/core-concepts/observability/logs/log-drains/overview) will do so daily. New indexes will necessarily mean that as time passes, you'll need more and more disk space, but also, less obviously, more and more RAM. Elasticsearch allocates RAM on a per-index basis, and letting your log retention grow unchecked will almost certainly lead to fatal issues when the database runs out of RAM or disk space.

## Components

We recommend using a combination of Elasticsearch's native features to ensure you do not accumulate too many open indexes by backing up your indexes to S3 in your own AWS account:

* [Index Lifecycle Management](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html) can be configured to delete indexes over a certain age.
* [Snapshot Lifecycle Management](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-lifecycle-management.html) can be configured to back up indexes on a schedule, for example, to S3 using the Elasticsearch [S3 Repository Plugin](https://www.elastic.co/guide/en/elasticsearch/plugins/current/repository-s3.html), which is available by default.

## Configuring a snapshot repository in S3

**Step 1:** Create an S3 bucket. We will use "aptible\_logs" as the bucket name for this example.

**Step 2:** Create a dedicated user to minimize the permissions of the access key, which will be stored in the database. Elasticsearch recommends creating an IAM policy with the minimum access level required. They provide a [recommended policy here](https://www.elastic.co/guide/en/elasticsearch/plugins/current/repository-s3-repository.html#repository-s3-permissions).

**Step 3:** Register the snapshot repository using the [Elasticsearch API](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/put-snapshot-repo-api.html) directly because the Kibana UI does not provide you a way to specify your IAM keypair. In this example, we'll call the repository "s3\_repository" and configure it to use the "aptible\_logs" bucket created above:

```bash  theme={null}
curl -X PUT "https://username:password@localhost:9200/_snapshot/s3_repository?pretty" -H 'Content-Type: application/json' -d'
{
  "type": "s3",
  "settings": {
    "bucket" : "aptible_logs",
    "access_key": "AWS_ACCESS_KEY_ID",
    "secret_key": "AWS_SECRET_ACCESS_KEY",
    "protocol": "https",
    "server_side_encryption": true
  }
}
'
```

Be sure to provide the correct username, password, host, and port needed to connect to your database, likely as provided by the [database tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels), if you're connecting that way.

[The full documentation of available options is here.](https://www.elastic.co/guide/en/elasticsearch/plugins/current/repository-s3-usage.html)

## Backing up your indexes

To backup your indexes, use Elasticsearch's [Snapshot Lifecycle Management](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-lifecycle-management.html) to automate daily backups of your indexes. In Kibana, you'll find these settings under Elasticsearch Management > Snapshot and Restore. Snapshots are incremental, so you can set the schedule as frequently as you like, but at least daily is recommended. You can find the [full documentation for creating a policy here](https://www.elastic.co/guide/en/kibana/7.x/snapshot-repositories.html#kib-snapshot-policy).

## Limiting the live retention

Now that you have a Snapshot Lifecycle policy configured to backup your data to S3, the final step is to ensure you delete indexes after a specific time in Elasticsearch. Deleting indexes will ensure both RAM and disk space requirements are relatively fixed, given a fixed volume of logs. For example, you may keep only 30 days in Elasticsearch, and if you need older indexes, you can retrieve them by restoring the snapshot from S3.

**Step 1:** Create a new policy by navigating to Elasticsearch Management > Index Lifecycle Policies. Under "Hot phase", disable rollover - we're already creating a new index daily, which should be sufficient. Enable the "Delete phase" and set it for 30 days from index creation (or to your desired live retention).

**Step 2:** Specify to Elasticsearch which new indexes you want this policy to apply automatically. In Kibana, go to Elasticsearch Management > Index Management, then click Index Templates. Create a new template using the Index pattern `logstash-*`. You can leave all other settings as default. This template will ensure all new daily indexes get the lifecycle policy applied.

```
{
  "index.lifecycle.name": "rotation"
}
```

**Step 3:** Apply the lifecycle policy to any existing indexes. Under Elasticsearch Management > Index Management, select one by one each `logstash-*` index, click Manage, and then Apply Lifecycle Policy. Choose the policy you created earlier. If you want to apply the policy in bulk, you'll need to use the [update settings API](https://www.elastic.co/guide/en/elasticsearch/reference/master/set-up-lifecycle-policy.html#apply-policy-multiple) directly.

## Snapshot Lifecycle Management as an alternative to Aptible backups

Aptible [database backups](/core-concepts/managed-databases/managing-databases/database-backups) allow for the easy restoration of a backup to an Aptible database using a single [CLI command](/reference/aptible-cli/cli-commands/cli-backup-restore). However, the data retained with [Snapshot Lifecycle Management](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-lifecycle-management.html) is sufficient to restore the Elasticsearch database in the event of corruption, and you can configure Elasticsearch take much more frequent backups.
