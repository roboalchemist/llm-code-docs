# Source: https://herd.laravel.com/docs/macos/herd-pro-services/minio.md

# MinIO

# Set up MinIO

MinIO is an open-source, S3 compatible object storage and works perfectly if you want to use the same APIs locally that you use on your production environment. You can set up MinIO as a Herd service and log into its dashboard to create your first storage bucket with the same credentials that you use as environment variables.

<Frame>
  <img alt="Screenshot of minio settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3f961357945e0f3bfae4d4bca5472bb8" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-minio.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2ff8e42fddedcdcce32c2150df67c058 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d6246dc5c1a2ebb8e44a7580cdb05c4e 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8e8fafe49839a7425f3c8580c188f410 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c3144e8885f8332378bf8ec7371ab5a8 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=eb571ea89f3611c556a598e24351b8fb 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=71a84daba8bfedcb968418d6c393d02e 2500w" />
</Frame>

## Configuration

Before you can connect your application to MinIO, you need to create a first bucket within the dashboard. The easiest way to access the dashboard or view the logs of the service is via the Herd service configuration.

<Frame>
  <img alt="Screenshot of the MinIO configuration" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=69c2f4331f300ac1b610d2db4b985506" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_minio.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=36d8c8b2949f5971ffeb8209487a7080 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=55805e9fead2a2e680bf4c645b9c9de9 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=dfe5b486dcdae16c15bc33430156891f 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=43e5868242cd80bd189383d2f6ce45d8 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2eb93d67a5a94fa36e24f79e52ab725a 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6e4f9d0f7d7b7c4e72b0dcba11fd31f8 2500w" />
</Frame>

## Dashboard

You can access the MinIO dashboard via `http://localhost:PORT` or by using the dashboard button in the services list. Log in with the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to create your first bucket and use the object storage like in your production environment.

<Frame>
  <img alt="Screenshot of the MinIO dashboard" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1bb8feeac9813ec43bab6473fe902332" data-og-width="2666" width="2666" data-og-height="1710" height="1710" data-path="images/docs/setup-minio-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f927fe3d161ee49f7365b33a90bd676a 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4300308ef79e53aa45d8ba815404527e 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=40c267a85137ebbb55530f93b6b9249f 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=bae7e1afa13ed9ef8678ed590d4eca27 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c51fcfc397c31a7db0c5ddf6a4752697 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3ad9cf7b58dccb320e8512a95c86703d 2500w" />
</Frame>

## Configuration

After setting the name, port, and autostart options and starting up the service, please log into the dashboard and create a bucket to be able to upload files.

You can then adjust your `.env` file in order to connect to your local MinIO service.

```env  theme={null}
AWS_BUCKET=herd-bucket # Your bucket name
AWS_ACCESS_KEY_ID=herd
AWS_SECRET_ACCESS_KEY=secretkey
AWS_USE_PATH_STYLE_ENDPOINT=true
AWS_URL=http://localhost:9000/YOUR-BUCKET-NAME
AWS_ENDPOINT=http://localhost:9000
```

You can find additional information about configuring MinIO with Laravel in the [Laravel documentation](https://laravel.com/docs/11.x/filesystem#amazon-s3-compatible-filesystems).

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version            |
| ------- | ------------------ |
| MinIO   | RELEASE.2024-06-29 |
