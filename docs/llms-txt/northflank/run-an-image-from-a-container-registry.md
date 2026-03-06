# Source: https://northflank.com/docs/v1/application/run/run-an-image-from-a-container-registry.md

# Run an image from a container registry

You can run images from container registries in three different ways on Northflank:

- As a continuously running service

- As a regularly scheduled cron job

- As a manually-run job

> [!note] 
> [Click here](https://app.northflank.com/s/project/create/service) to create a deployment service.
You can create a new continuously-running deployment service, a scheduled cron job or a manual job with an external image as the source.
You will need to enter the full image path and, if the image is private, select the [appropriate registry credentials](#verify-image).

![Deploying an image from a container registry in the Northflank application](https://assets.northflank.com/documentation/v1/application/run/run-an-image-from-a-container-registry/deploy-external-image.png)

## Image paths

Image paths include the registry url, username, image, and sometimes version, in the format:

`[registry-url]/[account]/[image]:[version]`

For example:

`docker.io/nginxinc/nginx-unprivileged:latest`

Northflank will automatically detect the registry and relevant credentials.

If you do not include the registry Northflank will default to `Docker Hub`, and if you do not specify an account Northflank will default to `Library`. `nginx:latest` would therefore become `docker.io/library/nginx:latest`

## Verify image

Northflank will attempt to automatically verify the image from the path you have entered. If the path cannot be verified, you will be prompted to either select your credentials or check the image path is correct.

If you do not have the [necessary credentials saved](./save-registry-credentials), select `Add new credential +`.

If entering a path or selecting credentials fail to trigger automatic verification, you can manually verify by clicking the verify button  above the image path field.

## Next steps

- [Set up a pipeline and release flow: Manage your deployments and release your updates in an intuitive pipeline with release flows.](/v1/application/release/create-a-pipeline-and-release-flow)
- [Networking on Northflank: Configure ports and security for your deployments.](/v1/application/network/networking-on-northflank)
- [Scale your services: Increase the resources available to your services, and the number of instances to deploy.](/v1/application/scale/scale-on-northflank)
- [Add databases and persistent storage: Create and use databases and other types of persistent storage in your project's applications and services.](/v1/application/databases-and-persistence/stateful-workloads-on-northflank)
