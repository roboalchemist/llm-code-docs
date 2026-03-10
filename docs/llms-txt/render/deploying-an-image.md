# Source: https://render.com/docs/deploying-an-image.md

# Deploy a Prebuilt Docker Image — Pull images from Docker Hub, GitHub, and more.

You can deploy a prebuilt Docker image to any of the following Render service types (if the image meets the [necessary requirements](#image-requirements)):

- Web services
- Private services
- Background workers
- Cron jobs

You can deploy public images from any registry Render can reach, and you can deploy _private_ images from the following registries:

- Docker Hub
- GitHub Container Registry
- GitLab Container Registry
- Google Artifact Registry
- AWS Elastic Container Registry (ECR)

A Render service that deploys a prebuilt Docker image is an *image-backed service*, as opposed to a *Git-backed service* that [deploys commits from your Git repository](/deploying-a-commit).

## Setup

1. In the [Render Dashboard](https://dashboard.render.com/), click *+ New* and select a service type to deploy. The service creation form appears.

2. Under *Source Code*, click *Existing Image*:

   [image: Deploying a Docker image in the Render Dashboard]

3. Provide the image's URL, along with any required credentials for accessing the image if it's private.

   - Learn more about [private image credentials](#credentials-for-private-images).

   - The *Image URL* field uses default values for an image's host (`docker.io`), namespace (`library`), and tag (`latest`) if you don't provide them. The following values all resolve to the same URL:

     - `docker.io/library/alpine:latest`
     - `docker.io/library/alpine`
     - `library/alpine`
     - `alpine`

   - You can specify an image _digest_ instead of a tag, such as:

     ```
     docker.io/library/alpine@sha256:c0669ef34cdc14332c0f1ab0c2c01acb91d96014b172f1a76f3a39e63d1f0bda
     ```

4. Render verifies that it can access the image using any credentials you provide. After this succeeds, click the now-enabled *Connect* button.

   The remainder of the service creation form becomes active.

5. Configure your service's details (name, region, instance type, and so on).

   You can click *Advanced* for additional configuration options, such as specifying a custom Docker `CMD` for the service.

6. Click the *Deploy* button.

You're all set! Render pulls the image from the registry and kicks off the service's initial deploy.

## Credentials for private images

To deploy a private Docker image on Render, you need to provide a valid credential to pull that image. Render can pull private images from the following container registries:

- Docker Hub
- GitHub Container Registry
- GitLab Container Registry
- Google Artifact Registry
- AWS Elastic Container Registry (ECR)

You specify your image's credential as part of [creating your new service](#setup):

[image: Choose a credential]

The *Credential* dropdown includes any _existing_ credentials you've already added to your workspace. You can reuse the same credential across multiple services.

If you click *Add credential*, the following dialog appears:

[image: Docker credential dialog in the Render Dashboard]

Provide the following details:

| Field | Description |
| --- | --- |
| *Name* | An identifying name for the credential. This value is for reference only. |
| *Registry* | The container registry to pull from. |
| *Username* | The username of the container registry account to use when authenticating. |
| *Personal Access Token* | The registry-generated token that grants permission to access the image. [Learn how to generate a personal access token.](#generating-a-personal-access-token) For Docker Hub only, you can provide your password instead of a personal access token. |

### Generating a personal access token

To generate a personal access token for Render to access your private Docker image, see the instructions for your container registry:

#### Docker Hub

Your personal access token requires access permissions that allow reading private images.

- [Token creation page](https://hub.docker.com/settings/security?generateToken=true)
- [Docker Hub documentation](https://docs.docker.com/docker-hub/access-tokens/)

#### GitHub

Your personal access token requires the `read:packages` permission to pull private images.

- [Token creation page](https://github.com/settings/tokens/new?description=&scopes=read%3Apackages)
- [GitHub documentation](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry)

#### GitLab

Your personal access token requires the `read_registry` permission to pull private images.

- [Token creation page](https://gitlab.com/-/profile/personal_access_tokens?scopes=read_registry)
- [GitLab documentation](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)

#### Google Artifact Registry

Your service account requires the `roles/artifactregistry.reader` permission to pull private images.

- [Service account creation page](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?walkthrough_id=iam--create-service-account#step_index=1)
- [Google documentation](https://cloud.google.com/artifact-registry/docs/docker/authentication#json-key)

#### AWS ECR

- For your *Username*, provide the AWS Account ID for the account that owns the AWS ECR repository.
- For your *Personal Access Token*, provide the password generated by the command `aws ecr get-login-password`.

> *ECR passwords expire after 12 hours.*
>
> To maintain a valid ECR credential, you need to generate a new password and apply it to the credential every 12 hours. You can update your credential programmatically using the Render API's [Update Registry Credential endpoint](https://api-docs.render.com/reference/update-registry-credential).

- [Find your AWS Account ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId)
- [AWS ECR authorization token instructions](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html#registry-auth-token)

### Managing credentials

You can manage your registry credentials from the *Container Registry Credentials* section of your Workspace Settings page:

[image: Container Registry Credentials]

From this section, you can:

- Add a new credential
- Remove a credential if it isn't used by any service

> *You can't remove a credential if at least one service uses it.*
>
> First, create a _new_ credential and apply it to any services that currently use the credential you want to remove.

## Triggering a deploy

Image-backed services do _not_ automatically redeploy whenever a new image is associated with their assigned tag (e.g., `latest`). Instead, you can redeploy using any of the following methods:

### Deploy from the Render Dashboard

In the [Render Dashboard](https://dashboard.render.com/), select your image-backed service and then click *Manual Deploy > Deploy latest reference*:

[image: Deploy latest reference]

This kicks off a deploy that pulls the image that's currently associated with the service's assigned tag.

### Deploy via webhook

Each Render service has a [deploy hook](/deploy-hooks) URL you can use to trigger a deploy via a `GET` or `POST` request. Your service's deploy hook URL is available from its Settings page in the [Render Dashboard](https://dashboard.render.com/):

[image: A service's deploy hook URL in the Render Dashboard]

When you deploy an image-backed service this way, you can optionally specify a tag or digest by appending an `imgURL` query parameter to the deploy hook URL:

```bash
# Append a string with this format to your deploy hook URL.
# This example deploys the image `nginx:1.26` from Docker Hub.
# Note the URL-encoding.
&imgURL=docker.io%2Flibrary%2Fnginx%401.26
```

If you do, Render pulls and deploys the image for the specified tag or digest, _instead of_ using the tag or digest in your service's settings. Note that for _future_ deploys, your service continues to use the tag or digest in its settings.

> All components of `imgURL` _besides_ the tag or digest must match your service's default image URL. Otherwise, Render rejects the deploy request.

Here's an example deploy hook URL that sets its `imgURL` to `docker.io/library/nginx:1.26` (note the required URL encoding):

```
https://api.render.com/deploy/srv-XXYYZZ?key=AABBCC&imgURL=docker.io%2Flibrary%2Fnginx%401.26
```

If request successfully kicks off a deploy, Render returns a `200` response. If you provide an invalid `imgURL`, Render returns a `404` response.

### Running pre-deploy tasks

To run tasks like database migrations or asset uploads before each deploy of your prebuilt image, you can set a [pre-deploy command](/deploys#deploy-steps) for your service.

## Image requirements

Before you deploy a particular Docker image to a Render service, note the following requirements:

#### `linux/amd64` platform

The Docker image must be built for the `linux/amd64` platform. To ensure this, do one of the following:

- Add a [`FROM` instruction](https://docs.docker.com/engine/reference/builder/#from) to your `Dockerfile`:
  ```Dockerfile
  FROM --platform=linux/amd64 <image>
  ```
- Specify the platform as a CLI flag when building the image:
  ```shell
  docker build --platform=linux/amd64
  ```

#### Image size

The Docker image's compressed size cannot exceed 10 GB.

#### Rollback support

To successfully [roll back a deploy](rollbacks) of an image-backed service, the image and digest used for the deploy you roll back to must be available in the container registry. Otherwise, the rollback deploy fails.

## Pulling images

*Render does not store previously pulled Docker images.* Instead, Render pulls your service's associated image from your container registry for _every deploy_. In the case of cron jobs, Render pulls the associated image every time the cron job runs.

In addition to pulling on every deploy, Render needs to pull an image in cases like the following:

- You restart your service, and it's scheduled on a machine that doesn't have a locally cached copy of the image.
- You create additional instances of your service via manual or automatic [scaling](scaling).
- Your service's underlying hardware is retired or experiences a failure, and your service needs to be rescheduled on a new machine.

Because Render relies on your container registry in all of these cases, make sure the images you use are always available in your registry!

### Image pull failures

If Render fails to pull an image from your registry, an `Image Pull Failed` service event appears on the Render Dashboard. Additionally, Render sends a deploy failure notification if you've [enabled notifications](notifications) for the service.

An image pull might fail for any of the following reasons:

- The image no longer exists in the registry.
- Your service uses a private image, and the [credential you've provided](#credentials-for-private-images) is no longer valid.
- The registry is down or experiencing issues.

When you encounter an image pull failure, first go to your service's Settings page on the [Render Dashboard](https://dashboard.render.com/). Under the *Deploy* section, verify the service's image URL and credential. If you need additional assistance, reach out to support@render.com.