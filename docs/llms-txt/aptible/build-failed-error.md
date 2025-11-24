# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/build-failed-error.md

# Build Failed Error

## Cause

This error is returned when you attempt a [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git), but your [Dockerfile](/core-concepts/apps/deploying-apps/image/deploying-with-git/overview) could not be built successfully.

## Resolution

The logs returned when you hit this error include the full output from the Docker build that failed for your Dockerfile. Review the logs first to try and identify the root cause.

Since Aptible uses [Docker](https://www.docker.com/), you can also attempt to reproduce the issue locally by [installing Docker locally](https://docs.docker.com/installation/) and then running `docker build .` from your app repository.

Once your app builds locally with a given Dockerfile, you can commit all changes to the Dockerfile and push the repo to Aptible, where it should also build successfully.
