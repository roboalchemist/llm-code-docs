<!-- Source: https://namespace.so/docs/reference/cli/instance-upload -->

# nsc instance upload

Upload a file to an instance.

`instance upload` copies a file from your local machine to a Namespace instance.

## Usage

```
nsc instance upload [instance-id] <local-path> <remote-path>
```

### Example

Upload a configuration file to an instance:

```
$ nsc instance upload 85a32emcg99ii ./config.yaml /etc/app/config.yaml
Uploaded config.yaml (12 KiB) to /etc/app/config.yaml. Took 1.2s.
```

## Options

### --container\_name, -c <name>

Target a container by name.

### --mkdir

Create parent directories on the remote if they don't exist.

Last updated February 13, 2026
