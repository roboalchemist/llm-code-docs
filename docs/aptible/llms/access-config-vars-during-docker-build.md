# Source: https://www.aptible.com/docs/how-to-guides/app-guides/access-config-vars-during-docker-build.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to access configuration variables during Docker build

By design (for better or worse), Docker doesn't allow setting arbitrary environment variables during the Docker build process: that is only possible when running [Containers](/core-concepts/architecture/containers/overview) after the [Image](/core-concepts/apps/deploying-apps/image/overview) is built.

The rationale for this is that [Dockerfiles](/core-concepts/apps/deploying-apps/image/deploying-with-git/overview) should be fully portable and not tied to any specific environment.

A direct consequence of this design is that your [Configuration](/core-concepts/apps/deploying-apps/configuration) variables, set via [`aptible config:set`](/reference/aptible-cli/cli-commands/cli-config-set), are not available to commands executed during the Docker build.

It's a good idea to follow Docker best practice and avoid depending on Configuration variables in instructions in your Dockerfile, but if you absolutely need to, Aptible provides a workaround: `.aptible.env`.

## `.aptible.env`

When building your image, Aptible injects a `.aptible.env` file at the root of your repository prior to running the Docker build. The file contains your Configuration variables, and can be sourced by a shell.

Here's an example:

```ruby  theme={null}
RAILS_ENV=production
DATABASE_URL=postgresql://user:password@host:123/db
```

If needed, you can use this file to access environment variables during your build, like this:

```ruby  theme={null}
# Assume that you've already ADDed your repo:
ADD . /app
WORKDIR /app

# The bundle exec rake assets:precompile command
# will run with your configuration
RUN set -a && . /app/.aptible.env && \
        bundle exec rake assets:precompile
```

> ❗️ Do **not** use the `.aptible.env` file outside of Dockerfile instructions. This file is only injected when your image is built, so changes to your configuration will **not** be reflected in the `.aptible.env` file unless you deploy again or rebuild. Outside of your Dockerfile, your configuration variables are accessible in the [Container Environment](/core-concepts/architecture/containers/overview).
