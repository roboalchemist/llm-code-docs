# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/deploys-take-long.md

# Deploys Take Too long

When Aptible builds your App, it must run each of the commands in your Dockerfile. We leverage Docker's built-in caching support, which is described in detail in [Docker's documentation.](https://docs.docker.com/articles/dockerfile_best-practices/#build-cache)

> 📘 [Shared Stacks](/core-concepts/architecture/stacks#shared-stacks) are more likely to miss the build cache than [Dedicated Stacks](/core-concepts/architecture/stacks#dedicated-stacks)

To take full advantage of Docker's build caching, you should organize the instructions in your Dockerfile so that the most time-consuming build steps are more likely to be cached. For many apps, the dependency installation step is the most time-consuming, so you'll want to (a) separate that process from the rest of your Dockerfile instructions and (b) ensure that it happens early in the Dockerfile.

We provide specific instructions and Dockerfile snippets for some package managers in our [How do I use Dockerfile caching to make builds faster?](/how-to-guides/app-guides/make-docker-deploys-faster) tutorials.

You can also switch to [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) for full control over your build process.
