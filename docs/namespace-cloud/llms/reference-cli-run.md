<!-- Source: https://namespace.so/docs/reference/cli/run -->

# nsc run

Quickly run containers in an ephemeral environment.

`run` starts containers in an ephemeral environment. When given an image, an
optional name, and set of ports to expose, a new ephemeral environment is
started with the specified containers. For example:

## Usage

```
nsc run [--on <id>] --image <reference> [-p <ports>] [--ingress <rules>] [--name <name>] [--] [args]
```

### Example

The following example starts a new ephemeral environment, running nginx. The `nginx`
container image has nginx, an http reverse proxy, listening on port 80. We
export that port to a public endpoint, using `-p 80`.

Exported endpoints are Internet-facing but require authentication. Whoever has access to the
workspace where the ephemeral environment was created in, will also have access to the
endpoint.

```
$ nsc run --image nginx -p 80
  Created new ephemeral environment! (id: 85a32emcg99ii).
  More at: https://cloud.namespace.so/01gr490qvbntkjn9jwypnd4g04/instance/85a32emcg99ii
  Running "nginx-t082s"
    Exported 80/tcp as https://4bi2reg-85a32emcg99ii.fra1.namespaced.app
```

## Arguments

Arguments passed to the command will be passed as arguments to the running container.
If you want to specify flags as container arguments, specify them after `--`.
For example: `nsc run --image nginx -- nginx -t`

## Options

### --image <reference>

Specifying an image is required. OCI compatible image registries are supported,
but images must be public, unless you're using `nscr.io`, nsc's own Private
[Container Registry](/docs/architecture/storage/container-registry).

### --on <id>

Rather than creating a new ephemeral environment, start the containers in an
existing environment (identified by its id).

Containers started in the same environment share networking, they can reach each
other on the local private network.

### --name <name>

Container names show up in observability, like logs. If no name is provided, a
name is generated based on the container image name.

### -p <ports>

Exports the specified ports (separated by commas) as public ingresses.

A nsc-based ingress does automatic TLS termination, but only HTTP backend
traffic is supported at the moment. In other words, the container exporting the
port must export an HTTP service.

Ports can also be exported after a container has started, using `nsc expose`.

### --enable\_docker

Enable the use of Docker from within the container.

### --volume <volume>

Attach a volume to the instance. It follows the format
`{cache|persistent}:{tag}:{mountpoint}:{size}`.

For example, `--volume cache:mytag:/cache:50gb` will result in a [Cache Volume](/docs/architecture/storage/cache-volumes)
with the tag `mytag` mounted at `/cache`. There will be 50 GB of space available.

### -o <type>

Specifying `run` command output format. Supported options are `json` and
`plain`. By default `plain` output format is used.

### --wait

Wait until the containers have started.

Note: This waits until the container runtime has started the necessary
processes, and does not check for readiness.

### --duration

Specify how long an ephemeral environment should live for. E.g. `--duration 10m`.

### --ingress <rules>

Specify additional rules per ingress. The following effects can be set per
route:

- `noauth`: Disables authentication on the route.

Rules are defined by mapping one or more rules to a port: `--ingress <port>=<rule>`
with the special case of `*` acting as a wildcard to any port.

Rules are defined by specifying method, path regex, using one of the following schemes:

- `<effect>`: Applies effect to any method or path.
- `<path_regex>:<effect>`: Applies effect to paths that match `path_regex` (the full path without the query is using for matching.).
- `<method>[,<method>,...]:<path_regex>:<effect>`: In addition to matching path, also matches against the HTTP method used.

Last updated July 21, 2025
