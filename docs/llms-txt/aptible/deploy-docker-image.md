# Source: https://www.aptible.com/docs/how-to-guides/app-guides/deploy-docker-image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to deploy via Docker Image

> Learn how to deploy your code to Aptible from a Docker Image

## Overview

Aptible lets you [deploying via Docker image](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy). Additionally, [Aptible's Terraform Provider](/reference/terraform) currently only supports this deployment method.

This guide will cover the process for deploying via Docker image to Aptible via the CLI, Terraform, or CI/CD.

## Deploying via the CLI

> ⚠️ Prerequisites: Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview)

### 01: Create an app

Use the `aptible apps:create` to create an [app](/core-concepts/apps/overview). Note the handle you give to the app. We'll refer to it as `$APP_HANDLE`.

### 02: Deploy a Docker image to your app

Use the `aptible deploy` command to deploy a public Docker image to your app like so:

```js  theme={null}
aptible deploy --app "$APP_HANDLE" \
        --docker-image httpd:alpine
```

After you've deployed using [aptible deploy](/reference/aptible-cli/cli-commands/cli-deploy), if you update your image or would like to deploy a different image, use [aptible deploy](/reference/aptible-cli/cli-commands/cli-deploy) again (if your Docker image's name hasn't changed, you don't even need to pass the --docker-image argument again).

> 📘 If you are migrating from [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git), you should also add the --git-detach flag to this command the first time you deploy. See [Migrating from Dockerfile Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) for more information.

## Deploying via Terraform

> ⚠️ Prerequisites: Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview) and the Terraform CLI

### 01: Create an app

[Apps](/core-concepts/apps/overview) can be created using the **terraform** **`aptible_app`** resource.

```js  theme={null}
resource "aptible_app" "APP" {
    env_id = ENVIRONMENT_ID
    handle = "APP_HANDLE"
}
```

### Step 2: Deploy a Docker Image

Set your Docker repo with the registry username and registry password as the configuration variables: `APTIBLE_DOCKER_IMAGE`, `APTIBLE_PRIVATE_REGISTRY_USERNAME`, and `APTIBLE_PRIVATE_REGISTRY_PASSWORD`.

```lua  theme={null}
resource "aptible_app" "APP" {
    env_id = ENVIRONMENT_ID
    handle = "APP_HANDLE"
    config = {
        "KEY" = "value"
        "APTIBLE_DOCKER_IMAGE" = "quay.io/aptible/deploy-demo-app"
        "APTIBLE_PRIVATE_REGISTRY_USERNAME" = "registry_username"
        "APTIBLE_PRIVATE_REGISTRY_PASSWORD" = "registry_password"
    }
}
```

> 📘 Please ensure you have the correct image, username, and password set every time you run. `terraform apply` See [Terraform's refresh Terraform configuration documentation](https://developer.hashicorp.com/terraform/cli/commands/refresh) for more infromation

## Deploying via CI/CD

See related guide: [How to deploy to Aptible with CI/CD](/how-to-guides/app-guides/how-to-deploy-aptible-ci-cd#deploying-with-docker)
