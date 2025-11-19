# Source: https://www.aptible.com/docs/core-concepts/apps/deploying-apps/linking-apps-to-sources.md

# Linking Apps to Sources

# Overview

Apps can be connected to their [Sources](/core-concepts/observability/sources) to enable the Aptible dashboard to provide details about the code that is deployed in your infrastructure, enabling your team to answer the question "*what's deployed where?*".

When an App is connected to its Source, you'll see details about the currently-deployed revision (the git ref, SHA, commit message, and other information) in the header of the App Details page, as well as a running history of revision information on the Deployments tab.

# Sending Deployment Metadata to Aptible

To get started, you'll need to configure your deployment pipeline to send Source information when your App is deployed.

## Using the Aptible Deploy GitHub Action

> 📘 If you're using **version `v4` or later** of the official [Aptible Deploy GitHub Action](https://github.com/aptible/aptible-deploy-action), Source information is retrieved and sent automatically. No further configuration is required.

To set up a new Source for an App, visit the [Source Setup page](https://app.aptible.com/sources/setup) and follow the instructions. You will be presented with a GitHub Workflow that you can add to your repository.

## Using Another Deployment Strategy

The Sources feature is powered by [App configuration](/core-concepts/apps/deploying-apps/configuration), so if you're using Terraform or your own custom scripts to deploy your app, you'll just need to send the following variables along with your deployment (note that **all of these variables are optional**):

* `APTIBLE_GIT_REPOSITORY_URL`, the browser-accessible URL of the git repository associated with the App.
  * Example: `https://github.com/example-org/example`.
* `APTIBLE_GIT_REF`, the branch name or tag of the revision being deployed.
  * Example: `release-branch-2024-01-01` or `v1.0.1`.
* `APTIBLE_GIT_COMMIT_SHA`, the 40-character git commit SHA.
  * Example: `2fa8cf206417ac18179f36a64b31e6d0556ff20684c1ad8d866569912bbf7235`.
* `APTIBLE_GIT_COMMIT_URL`, the browser-accessible URL of the commit.
  * Example: `https://github.com/example-org/example/commit/2fa8cf`.
* `APTIBLE_GIT_COMMIT_TIMESTAMP`, the ISO8601 timestamp of the git commit.
  * Example: `2024-01-01T12:00:00-04:00`.
* `APTIBLE_GIT_COMMIT_MESSAGE`, the full git commit message.
* (If deploying a Docker image) `APTIBLE_DOCKER_REPOSITORY_URL`, the browser-accessible URL of the Docker registry for the image being deployed.
  * Example: `https://hub.docker.com/repository/docker/example-org/example`

For example, if you're using the Aptible CLI to deploy your app, you might use a command like this:

```shell  theme={null}
$ aptible deploy --app your-app \
    --docker-image=example-org/example:v1.0.1 \
    APTIBLE_GIT_REPOSITORY_URL="https://github.com/example/example" \
    APTIBLE_GIT_REF="$(git symbolic-ref --short -q HEAD || git describe --tags --exact-match 2> /dev/null)" \
    APTIBLE_GIT_COMMIT_SHA="$(git rev-parse HEAD)" \
    APTIBLE_GIT_COMMIT_URL="https://github.com/example/repo/commit/$(git rev-parse HEAD)" \
    APTIBLE_GIT_COMMIT_MESSAGE="$(git log -1 --pretty=%B)" \
    APTIBLE_GIT_COMMIT_TIMESTAMP="$(git log -1 --pretty=%cI)"
```
