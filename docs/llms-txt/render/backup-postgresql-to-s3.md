# Source: https://render.com/docs/backup-postgresql-to-s3.md

# Back Up Render Postgres to Amazon S3

In this guide we'll show you how to back up your Render Postgres instance to Amazon S3.

Render continually backs up all paid Render Postgres instances to provide [point-in-time recovery](postgresql-backups). For additional control, you can create a [cron job](cronjobs) that periodically backs up your data to Amazon S3.

You will need a [Render Postgres database](postgresql) and an [Amazon Web Services](https://aws.amazon.com/) (AWS) account for this guide.

By following this guide, you'll be able to:

1. [Create AWS credentials](#create-aws-credentials) that will enable working with Amazon S3.
2. [Configure and create a backup Cron Job](#configure-and-create-the-backup-cron-job) for your database.
3. [Validate that the backup is working.](#validate-the-cron-job)

## Create AWS Credentials

We will create credentials with AWS IAM to enable working with Amazon S3.

1. Open the AWS console and navigate to the IAM service. Open the Users view and select the `Add Users` button.

   [image: A screenshot of the AWS Dashboard creating a new IAM user]

2. Enter a descriptive username, such as `<database name>-render-postgres-backup-cron`.

3. For `Select AWS credential type*` select `Access key - Programmatic access`.

4. Select the `Next: Permissions` button to move to the `Set Permissions` view.

   [image: A screenshot of the AWS Dashboard selecting the AmazonS3FullAccess policy for new IAM user]

5. In the `Set Permissions` view, select `Attach existing policies directly` and search for `AmazonS3FullAccess`. Check the box to select `AmazonS3FullAccess`.

> It's possible to use finer-grained policies to authorize the Cron Job. We recommend <a href="https://litestream.io/guides/s3/#restrictive-iam-policy">Litestream's guide</a> if you'd like to further lock down permissions.

6. Skip through the next two views with the `Next` buttons to move to the `Review` view. Confirm the details of your user.

7. Select the `Create User` button.

8. Record the access key ID (`AKIAXXXXXXXXXXXXXXXX`) and the secret access key.

## Configure and Create the Backup Cron Job

1. Fork [render-examples/postgres-s3-backups](https://github.com/render-examples/postgres-s3-backups).

2. In the `render.yaml` file, edit the `fromDatabase` name in the Cron Job's `DATABASE_URL` environment variable to be the name of your Render Postgres instance.

> *Do not use PGBouncer as your `DATABASE_URL` when performing a backup.* For details, see [this GitHub issue](https://github.com/pgbouncer/pgbouncer/issues/452).

3. In the `render.yaml` file, edit the Cron Job's `region` to match the region of your database.

4. By default, the Cron Job will run the backup daily at 3 a.m. UTC. You can change the time and frequency by modifying the Cron Job's `schedule` in the `render.yaml` file.

5. Commit and push your changes.

6. On the Render Dashboard, go to [Blueprints](https://dashboard.render.com/blueprints) and click the `New Blueprint Instance` button. Select your repository (after giving Render permission to access it, if you haven’t already). Alternatively, you can click the Deploy To Render button in the Readme of the forked repo.

   [image: A screenshot of the Render Dashboard filling out the new Blueprint form]

7. Enter a descriptive `Service Group Name` such as `Backup <database name> to S3`.

8. Fill in the environment variables:

   | Environment Variable      | Value                                                                                                                                                                                                                                           |
   | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | *AWS_REGION*            | Choose the [AWS region](https://docs.aws.amazon.com/general/latest/gr/s3.html) closest to the region of your database. For example, a Render Postgres instance in the Oregon region would use `us-west-2` for the AWS Region US West (Oregon).  |
   | *S3_BUCKET_NAME*        | Choose a globally unique name for your bucket. For example `<your-username>-<database name>-render-postgres-backups`. The name must follow [Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html). |
   | *AWS_ACCESS_KEY_ID*     | Copy the `Access key ID` (`AKIAXXXXXXXXXXXXXXXX`) we saved when creating the User.                                                                                                                                                              |
   | *AWS_SECRET_ACCESS_KEY* | Copy the secret access key we saved when creating the User.                                                                                                                                                                                     |
   | *POSTGRES_VERSION*      | Enter your database's PostgreSQL version. You can see the version when viewing your instance in the Render Dashboard. For example, `14`.                                                                                                        |

9. Select `Apply` to create the Cron Job.

## Validate the Cron Job

1. View the newly created Cron Job and wait for the first build to finish.

2. Select the `Trigger Run` button and wait for the job to finish with a `Cron job succeeded` event.

3. Verify the backup by inspecting the contents of your S3 bucket.

That's it! Your Cron Job will now periodically back up your Render Postgres instance to Amazon S3.

## Troubleshooting

### Large Databases

The `aws` CLI tool requires additional configuration when uploading large files to S3. If your compressed backup file exceeds 50 GB, add an `--expected-size` flag in the the `upload_to_bucket` function in `backup.sh`.

### Credential Errors

You may have an error with your IAM user if your Cron Job fails and you see an error message similar to:

```
An error occurred (SignatureDoesNotMatch) when calling the CreateBucket operation:
The request signature we calculated does not match the signature you provided.
Check your key and signing method.
```

Check over the [Create AWS Credentials](#create-aws-credentials) instructions.