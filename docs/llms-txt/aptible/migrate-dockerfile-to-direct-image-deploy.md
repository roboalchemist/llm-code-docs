# Source: https://www.aptible.com/docs/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to migrate from Dockerfile Deploy to Direct Docker Image Deploy

If you are currently using [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git) and would like to migrate to a Direct Docker Image Deploy, use the following instructions:

1. If you have a `Procfile` or `.aptible.yml` file in your repository, you must embed it in your Docker image. To do so, follow the instructions at [Procfiles and `.aptible.yml` with Direct Docker Image Deploy](/core-concepts/apps/deploying-apps/image/deploying-with-docker-image/procfile-aptible-yml-direct-docker-deploy).

2. If you modified your image to add the `Procfile` or `.aptible.yml`, rebuild your image and push it again.

3. Deploy using `aptible deploy` as documented in [Using `aptible deploy`](/reference/aptible-cli/cli-commands/cli-deploy), with one exception: the first time you deploy (you don't need to do it again), add the `--git-detach` flag to this command.
