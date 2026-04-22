<!-- Source: https://namespace.so/docs/reference/cli/docker-buildx-setup -->

# nsc docker buildx setup

Setup buildx in the current machine, to use Namespace Remote Builders.

`docker buildx setup` configures the local Docker's `buildx` plugin to use the Namespace [Remote Builders](/docs/solutions/docker-builders).
So the following `docker build` commands will use a high-capacity remote builder hosted by Namespace.

The builder machines are created on demand whenever a build is started, triggering a connection to the remote builders.
The architecture of the builder machine (AMD64 or ARM64) is inferred by the build command's platform.

## Usage

```
nsc docker buildx setup [--name <name>] [-state <path>] [--background] [--create_at_startup] [--use]
```

### Example

The following example configures local `buildx` to use Namespace Remote Builders.

```
$ nsc docker buildx setup --background --use
```

Then, following Docker builds will use Remote Builders.

```
$ docker build . -t app:latest
```

## Options

### --name <name>

Specify the name of the `buildx` builder. By default, it is "nsc-remote".

### --state <path>

Specify a custom directory where the command stores the remote builders context configuration.

### --background

If set, runs the proxy in the background. So, `nsc docker buildx setup` does not block the caller.

### --create\_at\_startup

By default, Remote Builders are created on demand, whenever a new build request is issued.
If this flag is set, the Remote Builders are created immediately.

### --use

If set, it configures local Docker context to use the Namespace Remote Builders.
By default, it only configures the builders in `docker buildx`, and it does not change the Docker context.

Last updated July 4, 2025
