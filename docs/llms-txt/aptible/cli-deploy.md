# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-deploy.md

# aptible deploy

This command is used to deploy an App. This can be used for [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) and/or for [Synchronizing Configuration and code changes](/how-to-guides/app-guides/synchronize-config-code-changes).

Docker image names are only supported in image:tag; sha256 format is not supported.

# Synopsis

```
Usage:
  aptible deploy [OPTIONS] [VAR1=VAL1] [VAR2=VAL2] [...]

Options:
      [--git-commitish=GIT_COMMITISH]                                  # Deploy a specific git commit or branch: the commitish must have been pushed to Aptible beforehand
      [--git-detach], [--no-git-detach]                                # Detach this app from its git repository: its Procfile, Dockerfile, and .aptible.yml will be ignored until you deploy again with git
      [--docker-image=APTIBLE_DOCKER_IMAGE]                            # Shorthand for APTIBLE_DOCKER_IMAGE=...
      [--private-registry-email=APTIBLE_PRIVATE_REGISTRY_EMAIL]        # Shorthand for APTIBLE_PRIVATE_REGISTRY_EMAIL=...
      [--private-registry-username=APTIBLE_PRIVATE_REGISTRY_USERNAME]  # Shorthand for APTIBLE_PRIVATE_REGISTRY_USERNAME=...
      [--private-registry-password=APTIBLE_PRIVATE_REGISTRY_PASSWORD]  # Shorthand for APTIBLE_PRIVATE_REGISTRY_PASSWORD=...
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
```
