# Source: https://northflank.com/docs/v1/application/build/inject-build-arguments.md

# Inject build arguments

You can set [Build arguments (ARG)](https://docs.docker.com/engine/reference/builder/#arg) to be passed to the Docker container at build-time. You can set build arguments in individual resources, or [create a secret group](https://northflank.com/docs/v1/application/secure/manage-secret-groups) so that multiple resources in a project can inherit the same secrets.

You can also upload [secret files](#add-a-secret-file-to-a-build) to make certificates, configuration files, and other data available in your builds.

![Build arguments editor in the Northflank application](https://assets.northflank.com/documentation/v1/application/build/inject-build-arguments/build-arguments.png)

Although unlikely, some buildpacks may override your build arguments.

You can set build arguments (`ARG`) to be passed to the Docker container at build-time in jobs, build services, and combined services.

Your build arguments will be passed to the Dockerfile on build via the `--build-arg` flag. They do not persist in the built image and are set as key-value pairs.

For example, a variable set as `PACKAGES=npm-cache` can be accessed in the Dockerfile by declaring the ARG. Variables must be declared in the Dockerfile with ARG before being accessed. Arguments will only be in scope for the build section where they are declared.

```dockerfile
FROM alpine as base
ARG PACKAGES
RUN echo "Using: ${PACKAGES}"
# PACKAGES available

FROM base as stage1
RUN echo "Using: ${PACKAGES}"
# PACKAGES not available

FROM base as stage2
ARG PACKAGES
RUN echo "Using: ${PACKAGES}"
# PACKAGES available
```

To set build arguments for a single resource, navigate to the build arguments page in your resource and select an editor mode. You may be prompted to enter your password.

### Persist build arguments in the runtime environment

If you want to access a build argument value in the runtime environment, declare it as an runtime variable (`ENV`) in the Dockerfile with the value of the build argument. You should not pass secrets to your runtime environment in this way, as it will be visible to anyone with the image.

```dockerfile
FROM alpine as production
ARG PACKAGES
ENV PACKAGES=${PACKAGES}
# PACKAGES available in build and runtime
```

![Setting build arguments in the Northflank application](https://assets.northflank.com/documentation/v1/application/secure/inject-secrets/build-arguments.png)

Learn more about build arguments and the [Docker ARG command](https://docs.docker.com/engine/reference/builder/#arg).

## Add a secret file to a build

You can include secret files which can be accessed during the build process. This can be useful to provide certificates, secrets, or configuration files that must be accessed during the build process, but which should not be included in your repository.

To add a secret file, paste or upload the content in the secret file editor on the environment page of a build service, combined service, or a job that builds from a repository. You can also upload secret files to [secret groups](https://northflank.com/docs/v1/application/secure/manage-secret-groups) to make them available to multiple resources in the same project.

Secret files in builds are injected relative to the repository root, unlike secret files in deployed containers which are injected relative to the build root.

Secret files in builds also cannot overwrite files in the repository, for example a repository with `data/config.json` would fail to build if you added a secret file with the path `/data/config.json`.

If you reference a secret file in your Dockerfile it is relative to the build context, not the container root. This also means that the secret file path needs to take the build context into account when you add the file to Northflank.

If you want to access a secret file while using the build context `/frontend` the file path must be set to `/frontend/data/config.json`. You can make the file available under this path by specifying `COPY ./data/config.json .` in the Dockerfile.

The table below gives examples of how a path would be set and accessed in various contexts:

| Secret file mount path | Build context | Secret file relative to build context | Dockerfile COPY example | File location in build after `WORKDIR app; COPY ${file} .` |
| --- | --- | --- | --- | --- |
| `/secrets/my-secret` | `/` | `./secrets/my-secret` | `COPY ./secrets/my-secret .` | `/app/my-secret` |
| `/secrets/my-secret` | `/frontend` | `secret outside of build context` | `secret outside of build context` | `secret outside of build context` |
| `/frontend/secrets/my-secret` | `/frontend` | `./secrets/my-secret` | `COPY ./secrets/my-secret .` | `/app/my-secret` |

## Learn more

- [Inject secrets: Set build arguments and inject runtime variables into running deployments.](/v1/application/secure/inject-secrets)
- [Manage groups of secrets: Create and manage groups of secrets that can be inherited throughout an entire project or by specific services and jobs.](/v1/application/secure/manage-secret-groups)
- [Upload a secret file: Add secret files that will be mounted in your container.](/v1/application/secure/upload-secret-files)
