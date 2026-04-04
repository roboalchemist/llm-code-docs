# Source: https://northflank.com/docs/v1/application/databases-and-persistence/migrate-data-to-northflank/migrate-your-minio-deployment-to-northflank.md

# Migrate your MinIO® deployment to Northflank

You can migrate your existing MinIO®* deployment or S3-compatible storage to Northflank with different strategies:

- **Site replication:** if you are migrating from another MinIO deployment you can use site replication, which creates a two-way sync between MinIO deployments. Site replication synchronises your existing buckets and objects, as well as IAM, security tokens, access keys, and bucket-level configurations between deployments.

- **Mirror:** if you are migrating from an S3-compatible storage service or do not want to enable two-way sync you can use the mirror command. This will create a one-way sync between your existing buckets and your Northflank addon.

- **Copy:** if you are migrating from S3-compatible storage, another MinIO deployment, or your local/server filesystem and your storage is not actively being used (no new uploads, modifications, or deletions), you can use the copy command to move your bucket contents to Northflank.

## Permissions

The account used to access your source MinIO deployment will require the `EnableRemoteBucketConfiguration` and `EnableReplicationRuleConfiguration` permissions.

You can find the [necessary policy here](https://min.io/docs/minio/linux/administration/bucket-replication/bucket-replication-requirements.html#id1).

## Import using replicate

Site replication allows you to seamlessly migrate your existing MinIO deployment to Northflank. You can only configure site replication between MinIO deployments, if you are migrating from another S3-compatible storage system you can migrate using the [mirror](#import-using-mirror) or [copy](#import-using-copy) methods.

After configuring site replication you can either remove your old MinIO deployment and terminate it to transfer fully over to Northflank, or leave it running with site replication enabled in order to provide redundancy.

You can replicate your entire existing MinIO deployment either in the [MinIO console](https://min.io/), or using the [MinIO client](https://min.io/docs/minio/linux/reference/minio-mc.html).

First [create a Northflank MinIO addon](https://app.northflank.com/s/project/create/addon) to import to, and [connect to it](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-minio-on-northflank#connect-to-minio) with your preferred administration tool.

> [!note] Prerequisites for site replication
> 
- The Northflank MinIO addon you want to import to must be empty of all buckets and objects
- If you are using an external identity provider with your existing MinIO deployment, configure the Northflank MinIO deployment with this before continuing
- The source MinIO site and the Northflank MinIO addon must be [publicly accessible](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-minio-on-northflank#access-minio) during the migration
- [Check the MinIO documentation](https://min.io/docs/minio/linux/operations/install-deploy-manage/multi-site-replication.html#prerequisites) for multi-site replication before beginning.

### Replicate your site using the MinIO console

Navigate to your source MinIO deployment that contains your data and log in using the console endpoint. Open the site replication page and click add sites. Enter the details for your existing MinIO instance, and give it a recognisable name.

Return to your Northflank MinIO addon's connection details page and copy the `EXTERNAL_MINIO_ENDPOINT`, `ACCESS_KEY` and `SECRET_KEY` into the peer sites section of the site replication page, and give it a recognisable name.

Save these details and your MinIO deployments will begin syncing. You can check the progress from the replication status page, which will show you the number of synchronised buckets, users, groups, and policies between the deployments. You can also check the status of individual buckets.

You can now replace your old MinIO deployment's connection details with the new Northflank endpoint and keys in your application/infrastructure. While both deployments are live and site replication is enabled all data will be synchronised between both MinIO instances.

You can delete the site replication configuration from either MinIO deployment's site replication page and terminate your old MinIO deployment when ready.

### Replicate your site using the MinIO client

Add your source MinIO deployment and the Northflank MinIO addon as aliases in your shell, using your relevant connection details:

```shell
mc alias set minio-source <MINIO_SOURCE_ENDPOINT> <ADMIN_USERNAME> <ADMIN_PASSWORD>
mc alias set minio-northflank <EXTERNAL_MINIO_ENDPOINT> <ADMIN_USERNAME> <ADMIN_PASSWORD>
```

Now run the `mc admin replicate add` command to configure site replication. The source MinIO instance must be listed first:

```shell
mc admin replicate add minio-source minio-northflank
```

You should see a success message, and you can check the replication configuration with the command:

```shell
mc admin replicate status minio-source
```

You can check the sync progress with:

```shell
mc admin replicate status minio-northflank
```

You can now replace your old MinIO deployment's connection details with the new Northflank endpoint and keys in your application/infrastructure. While both deployments are live and site replication is enabled all data will be synchronised between both MinIO instances. You can delete the site replication configuration with the following command when ready:

```shell
mc admin replicate rm minio-northflank minio-source --force
```

The two MinIO deployments will now be unlinked, and you can terminate your old MinIO deployment.

## Import using mirror

If you are importing from another S3-compatible storage service you can use the [mirror](https://min.io/docs/minio/linux/reference/minio-mc/mc-mirror.html#continuously-mirror-s3-bucket-to-an-s3-compatible-host) command to synchronise your bucket contents.

Mirror will create a one-way sync between your source storage and your Northflank MinIO addon. This means you can transfer existing buckets and objects as well as keep up-to-date with any new uploads while migrating your applications and infrastructure to use the Northflank addon.

> [!note] Versioning and metadata
> Mirror will not copy any metadata or previous versions of your objects, this data will be lost. If versioning is enabled on a bucket in your Northflank MinIO storage, objects will be versioned from the point that they were transferred to the new bucket.

The mirror command will only copy file paths and objects, you will need to manually create any users, groups, and other MinIO configuration options. You can do this before, or after, transferring your data.

First [create a Northflank MinIO addon](https://app.northflank.com/s/project/create/addon) to import to, and [connect to it](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-minio-on-northflank#connect-to-minio) with your preferred administration tool.

### Configure your buckets

If your existing buckets on your source S3 storage have any policies affecting them, such as versioning, quotas, retention, or object locking you should re-create your buckets and their associated policies in your Northflank MinIO addon before transferring your objects with mirror.

For example, if your source S3 bucket has object locking enabled and has locked objects stored in it, you must create a bucket with object locking enabled otherwise the transfer will fail.

If no bucket with the specified name is present on the target, the mirror command can will a new bucket with no policies. However, you will not be able to configure some policies after bucket has been created, including retention and object locking.

### Copy your storage contents using mirror

Add your source S3 storage deployment and the Northflank MinIO addon as aliases in your shell, using your relevant connection details (you can copy the `EXTERNAL_MINIO_CONNECT_COMMAND` from the Northflank addon's connection details page):

```shell
mc alias set S3-source <S3_SOURCE_ENDPOINT> <ADMIN_USERNAME> <ADMIN_PASSWORD>
mc alias set minio <EXTERNAL_MINIO_ENDPOINT> <ADMIN_USERNAME> <ADMIN_PASSWORD>
```

You can now begin mirroring either all your buckets, or specific buckets from your existing storage to Northflank. You can mirror all buckets from the source by specifying only the source and target aliases, or mirror specific buckets/paths within buckets, by specifying the source and target aliases and buckets/paths.

```shell
## mirror all buckets
mc mirror --watch S3-source minio

## mirror specific bucket/path
mc mirror --watch S3-source/source-bucket minio/target-bucket
```

The `--watch` option means the process will continuously synchronise files from the source to Northflank until you terminate it. It will overwrite objects that exist on the source and on the Northflank addon, which means any changes to objects on the source will be synchronised.

The `--watch` option does not remove objects that exist on the target but not the source, but you can use the `--remove` flag as well if required. This will only remove objects when the command is first run, so you can continue to sync new objects from the source while also uploading new objects to the Northflank MinIO addon.

### Migrate your application/infrastructure

You can now configure your new MinIO deployment with any required users, groups, and policies, if you have not already, and update your application and infrastructure to use the Northflank MinIO addon's connection details.

The Northflank MinIO deployment should now receive uploads from applications with the new connection details, as well as new uploads to your old S3 storage. This will allow you to gracefully migrate to Northflank, and you can terminate the mirror process and your old S3 storage deployment when ready.

## Import using copy

If you are importing from another S3-compatible storage service or your local/server filesystem you can use the [copy](https://min.io/docs/minio/linux/reference/minio-mc/mc-cp.html) command to simply upload objects to your buckets.

This is a one-time operation, so any changes made to the source buckets or local files will not be reflected in your Northflank MinIO addon after the copy has been completed. If you need to migrate storage that is actively in use you should use [mirror](#import-using-mirror) or [replicate the site (MinIO only)](#import-using-replicate) instead.

First [create a Northflank MinIO addon](https://app.northflank.com/s/project/create/addon) to import to, and [connect to it](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-minio-on-northflank#connect-to-minio) with your preferred administration tool.

### Configure your buckets

Using the console or client create your required buckets, configured with or without versioning, quotas, retention, or object locking. You will not be able to configure some policies after a bucket has been created.

### Copy objects from S3-compatible storage

Add your source S3-compatible storage deployment and the Northflank MinIO addon as aliases in your shell, using your relevant connection details (you can copy the `EXTERNAL_MINIO_CONNECT_COMMAND` from the Northflank addon's connection details page):

```shell
mc alias set S3-source <S3_SOURCE_ENDPOINT> <ADMIN_USERNAME> <ADMIN_PASSWORD>
mc alias set minio <EXTERNAL_MINIO_ENDPOINT> <ADMIN_USERNAME> <ADMIN_PASSWORD>
```

You can now copy the contents of existing buckets using the `cp` command with the `--recursive` flag, to copy all the bucket's objects and their paths:

```shell
mc cp --recursive S3-source/source-bucket minio/target-bucket
```

### Copy objects from local filesystem

Add your Northflank MinIO addon as an alias in your shell, using either the `EXTERNAL_MINIO_CONNECT_COMMAND` from the addon's connection details page, or the `MINIO_CONNECT_COMMAND` if you have [forwarded](https://northflank.com/docs/v1/api/forwarding) your addon:

```shell
mc alias set minio <EXTERNAL_MINIO_ENDPOINT> <ADMIN_USERNAME> <ADMIN_PASSWORD>
```

You can now copy the contents of existing buckets using the `cp` command with the `--recursive` flag, to copy all objects and their paths from the specified directory:

```shell
mc cp --recursive local_files/my_objects minio/target-bucket
```

### Migrate your application/infrastructure

Check your Northflank MinIO addon has all the buckets and objects you expect it to using the console or client.

You can now configure your new MinIO deployment with any required users, groups, and policies, if you have not already, and update your application and infrastructure to use the Northflank MinIO addon's connection details.

## Next steps

- [Deploy MinIO® on Northflank: MinIO is a High Performance Object Storage with an Amazon S3 cloud storage service compatible API.](/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-minio-on-northflank)
- [Access a database: Securely access your database locally or make it available online.](/v1/application/databases-and-persistence/access-a-database)
- [Backup, restore, and import your data: Create and import backups of your database, or restore from an existing backup.](/v1/application/databases-and-persistence/backup-restore-and-import-data)
- [Use a database with your applications: Securely access your database in your project's applications and services.](/v1/application/databases-and-persistence/connect-database-secrets-to-workloads)

* MinIO is a registered trademark of the MinIO Corporation.
