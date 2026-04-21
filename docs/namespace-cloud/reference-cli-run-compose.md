<!-- Source: https://namespace.so/docs/reference/cli/run-compose -->

# nsc run-compose

Quickly start a set of containers from your compose project in an ephemeral environment.

`run-compose` starts a set of containers defined in a [compose file](https://docs.docker.com/compose/compose-file/)
in an ephemeral environment. Similar to `docker-compose`, `nsc run-compose`
uses *compose.yaml* (preferable), *compose.yml*, *docker-compose.yaml* or
*docker-compose.yml* file in working directory.

## Usage

```
nsc run-compose [--dir <dir>] [--development] [-o <plain|json>]
```

### Example

In the following example, `nsc` starts containers using compose file in the
current directory:

```
$ nsc run-compose
 
  Created new ephemeral environment! (id: 9f8q34lp1v0v6).
 
  More at: https://cloud.namespace.so/01gr1g2rpb7ahzddy3f227exq9/instance/9f8q34lp1v0v6
```

Then you can SSH into the instance using the instance ID from the output:

```
$ nsc ssh 9f8q34lp1v0v6
```

and explore the created containers with `nerdctl`:

```
$ nerdctl ps
```

Additionally, you can expose any service from the compose file publicly using
[`nsc expose`](/docs/reference/cli/expose) command with the flag `--source containerd`.

## Options

### --dir <dir>

To specify a working directory from where `nsc` loads the compose file.

### --development

Specify to enables development facilities, including making containers optional.

### -o <type>

Specifying `run-compose` command output format. Supported options are `json` and
`plain`. By default `plain` output format is used.

### --wait

Wait for all containers to start running.

Last updated July 4, 2025
