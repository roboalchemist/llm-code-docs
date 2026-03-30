# Source: https://render.com/docs/deploy-minio.md

# Deploy MinIO

[MinIO](https://min.io/) provides S3-compatible object storage for the hybrid cloud and is great for users looking for a performant and scalable object store to use on Render.

## One-Click Deploy

Click the *Deploy to Render* button below to deploy MinIO to Render.

<deploy-to-render repo="https://github.com/render-examples/minio">
</deploy-to-render>

This deployment will create a Starter Web Service running the latest [Docker Image of MinIO](https://hub.docker.com/r/minio/minio/). Your objects are then stored on a 10GB [Render SSD Disk](disks) so your data is saved across deploys and automatically backed up with daily snapshots.

### After Deployment

1. Navigate to your Services and click on `minio` and find your `*.onrender.com` URL.

2. Go to the Settings tab to configure your desired instance type if additional RAM and CPU are required beyond the default.

3. Go to the Disks tab to configure the amount of Disk storage required. You can always increase the size later, but you cannot decrease it. Pick the lowest value that works for your app.

4. Find your automatically generated `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD` in the Environment tab to use to log in.

5. Learn more about MinIO from the [Quickstart Guide](https://docs.min.io/).

## Manual Deploy

1. Fork our MinIO [example repo](https://github.com/render-examples/minio) from GitHub.

2. Make any required changes such as changing the `region`, `plan` or `disk size` in the provided `render.yaml file.

3. Go to `https://dashboard.render.com/blueprints` for your Render workspace and create a `New Blueprint Instance` using your forked repo.