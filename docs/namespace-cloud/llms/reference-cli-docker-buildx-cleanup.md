<!-- Source: https://namespace.so/docs/reference/cli/docker-buildx-cleanup -->

# nsc docker buildx cleanup

Unregister Namespace Remote Builders from buildx.

`docker buildx cleanup` stops the Namespace Remote Builders context and unconfigures them from local `buildx`.

## Usage

```
nsc docker buildx cleanup [--state <path>]
```

## Options

### --state <path>

Specify the directory path where the remote builder context configuration is stored.

Last updated July 4, 2025
