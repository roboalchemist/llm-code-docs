<!-- Source: https://namespace.so/docs/reference/cli/docker-remote -->

# nsc docker remote

Run docker on the target instance.

`docker remote` forwards Docker commands to a Namespace instance. All arguments after `remote` are passed directly to the Docker CLI on the remote instance.

## Usage

```
nsc docker remote [instance-id] -- <docker-args...>
```

### Example

List containers running on the remote instance:

```
$ nsc docker remote 85a32emcg99ii -- ps
CONTAINER ID   IMAGE          COMMAND   CREATED        STATUS       NAMES
abc12345def    myapp:latest   "run..."  3 minutes ago  Up 3 min     myapp
```

## Options

All flags are passed through to the Docker CLI on the remote instance.

Last updated February 13, 2026
