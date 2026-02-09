# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-deploy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible deploy

This command is used to deploy an App. This can be used for [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) and/or for [Synchronizing Configuration and code changes](/how-to-guides/app-guides/synchronize-config-code-changes).

Docker image names are only supported in image:tag; sha256 format is not supported.

# Synopsis

```
Usage:
  aptible deploy [--app APP] [OPTIONS] [VAR1=VAL1] [VAR2=VAL2] [...]

Options:
      [--git-commitish=GIT_COMMITISH]                                  # Deploy a specific git commit or branch: the commitish must have been pushed to Aptible beforehand
      [--git-detach], [--no-git-detach]                                # Detach this app from its git repository: its Procfile, Dockerfile, and .aptible.yml will be ignored until you deploy again with git
      [--docker-image=DOCKER_IMAGE]                                    # The docker image to deploy. If none specified, the currently deployed image will be pulled again
      [--private-registry-username=USERNAME]                           # Username for Docker images located in a private repository
      [--private-registry-password=PASSWORD]                           # Password for Docker images located in a private repository
      [--private-registry-email=EMAIL]                                 # This parameter is deprecated
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
```
