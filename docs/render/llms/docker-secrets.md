# Source: https://render.com/docs/docker-secrets.md

# Using Secrets with Docker

Docker services can access environment variables and secret files like other kinds of services at run time.
However, because of the way that Docker builds work, you won't have access to environment variables and secret files as usual at build time.

## Security

Before going into how to use your environment variables and secret files for Docker builds, you should know that using secrets with Docker can result in your image containing sensitive information.
Although we store your images securely, Docker registries should be treated like code repositories: it's best practice to not store secrets in them.
You should avoid using secrets in your Docker builds to eliminate the chance of accidentally storing sensitive material.

That being said, some build processes _require_ credentials to access private resources, for example.
For these, it's best to use [secret files](#secret-files-in-docker-builds).

## Secret Files in Docker Builds

The best way to use secrets in your Docker build is with secret files.
Unlike build args, secret mounts aren't persisted in your built image.

Secret files in Docker builds make use of secret mounts which are available with Dockerfile syntax v1.2.
At the top of your Dockerfile, add

```dockerfile
# syntax = docker/dockerfile:1.2
```

Then, add `--mount=type=secret,id=FILENAME,dst=/etc/secrets/FILENAME` to your run `RUN` instructions, replacing `FILENAME` with the name of your secret file.
If your filename contains non-alphanumeric characters, replace them with `_` for the `id=` part.
For example, if you have a secret file named `.env`, then using

```dockerfile
RUN --mount=type=secret,id=_env,dst=/etc/secrets/.env cat /etc/secrets/.env
```

will print the content of `.env` in your build.
You can make use of *multiple secret files* by adding more `--mount=type=secret,...`.

> The `--mount=type=secret,...` needs to be included for every instruction that requires the secret file.

Read more about Docker secrets and secret mounts in the [Docker Docs](https://docs.docker.com/develop/develop-images/build_enhancements/#new-docker-build-secret-information).

### Building Images with Secrets Locally

To build images locally with Dockerfiles that make use of secrets, you need to have a recent version of Docker installed.
When you run `docker build`, ensure that BuildKit is enabled with the `DOCKER_BUILDKIT=1` and pass in secrets using the `--secret` argument like so:

```bash
DOCKER_BUILDKIT=1 docker build --secret id=FILENAME,src=LOCAL_FILENAME ...
```

`FILENAME` is the same as the ID from `--mount=type=secret,id=FILENAME,...` in your Dockerfile and `LOCAL_FILENAME` is an appropriate secret file located on your build host.

Read more about Docker secrets and secret mounts in the [Docker Docs](https://docs.docker.com/develop/develop-images/build_enhancements/#new-docker-build-secret-information).

## Accessing Secret Files at Runtime

If you add [secret files](configure-environment-variables#secret-files) to a Docker-based service, those services are available at runtime at `/etc/secrets/<filename>`.

When accessing secret files in Docker services, you might encounter permission errors like the following:

```
cp: cannot open '/etc/secrets/myfile' for reading: Permission denied
```

To resolve this, make sure your application user is in group `1000`. You can set this in your Dockerfile:

```dockerfile
# Alpine-based images do not have usermod by default and must install it:
# RUN apk add shadow

# Add your application user to group 1000
RUN usermod -a -G 1000 your-app-user
```

## Environment Variables in Docker Builds

Docker doesn't provide a way to pass in environment variables to a build.
It does, however, provide build args.
Render injects your service's environment variables as build args with the same keys and values.
You can make use of build args in your Dockerfile using the [`ARG` instruction](https://docs.docker.com/engine/reference/builder/#arg).

> We recommend against using `ARG` instructions for secrets. Consider
>   using <a href="#secret-files-in-docker-builds">secret files</a> instead for
>   build-time secrets.
