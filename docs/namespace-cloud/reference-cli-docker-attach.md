<!-- Source: https://namespace.so/docs/reference/cli/docker-attach -->

# nsc docker attach-context

Attach your local Docker to an ephemeral environment.

`docker attach-context` configures a Docker context that uses an ephemeral environment.

## Usage

```
nsc docker attach-context {--new | --to <instance-id>} [--name <name>] [-state <path>] [--machine_type <cpu>x<mem>] [--background] [--use]
```

### Example

Create an ephemeral instance:

```
$ nsc create
  Created new ephemeral environment! ID: me4ev9pm8qk8o
```

Attach your local Docker to the new environment:

```
$ nsc docker attach-context --to me4ev9pm8qk8o --name my-remote-docker --background --use
  Attached Docker Context: my-remote-docker
```

Run Docker commands as usual and use the newly created context:

```
$ docker compose up
```

### Example with Cache Volumes

Create bare instance with Cache Volume:

```
$ nsc create --bare --volume cache:tagname:/mountpoint:50gb
  Created new ephemeral environment! ID: me4ev9pm8qk8o
```

Attach your local Docker context to the remote instance:

```
$ nsc docker attach-context --to me4ev9pm8qk8o --background --use
```

Finally, run a container and bind mount the cache volume directory into it:

```
$ docker run --rm -it -v /mountpoint:/cache ubuntu
```

Your container can access the cache context at `/cache` path. Check how [cache volumes](/docs/architecture/storage/cache-volumes) work.

## Options

### --new

Create a new ephemeral environment. Either `--new` or `--to <instance-id>` must be set.

### --to <instance-id>

Rather than creating a new ephemeral environment, attach to Docker in an existing environment (identified by its id).
Either `--new` or `--to <instance-id>` must be set.

### --name <name>

The name of the Docker context that is created; by default it will be `nsc-{instance-id}`.

### --state <path>

Specify a custom directory where the command stores the Docker context configuration.

### --machine\_type <cpu>x<mem>

Specifying the machine shape when creating a new environment. The following are the supported machine shapes:

- `2x2`: 2 CPU 2 GB memory.
- `2x4`: 2 CPU 4 GB memory.
- `4x4`: 4 CPU 4 GB memory.
- `4x8`: 4 CPU 8 GB memory.
- `4x16`: 4 CPU 16 GB memory.
- `16x32`: 16 CPU 32 GB memory.

### --background

If set, attach to the Docker context in the background. So, `nsc docker attach-context` does not block the caller.

### --use

If set, it configures local Docker to use the newly configured Docker context.

Last updated July 4, 2025
