# Source: https://www.aptible.com/docs/core-concepts/apps/deploying-apps/image/deploying-with-git/build.md

# Docker Build

# Build context

When Aptible builds your Docker image using [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git), the build context contains the git repository you pushed and a [`.aptible.env`](/how-to-guides/app-guides/access-config-vars-during-docker-build#aptible-env) file injected by Aptible at the root of your repository.

Here are a few caveats you should be mindful of:

* **Git clone is a shallow clone**
  * When Aptible ships your git repository to a build instance, it uses a git shallow clone.
  * This has no impact on the code being cloned, but you should be mindful that using e.g. `git log` within your container will yield a single commit: the one you deployed from.
* **File timestamps are all set to January 1st, 2000**
  * Git does not preserve timestamps on files. This means that when Aptible clones a git repository, the timestamps on your files represent when the files were cloned, as opposed to when you last modified them.
  * However, Docker caching relies on timestamps (i.e., a different timestamp will break the Docker build cache), so timestamps that reflect the clone time would break Docker caching.
  * To optimize your build times, Aptible sets all the timestamps on all files in your repository to an arbitrary timestamp: January 1st, 2000, at 00:00 UTC.
* **`.dockerignore` is not used**
  * The `.dockerignore` file is read by the Docker CLI client, not by the Docker server.
  * However, Aptible does not use the Docker CLI client and does not currently use the `.dockerignore` file.

# Multi-stage builds

Although Aptible supports [multi-stage builds](https://docs.docker.com/build/building/multi-stage/), there are a few points to keep in mind:

* You cannot specify a target stage to be built within Aptible. This means the final stage is always used as the target.
* Aptible always builds all stages regardless of dependencies or lack thereof in the final stage.
