<!-- Source: https://namespace.so/docs/reference/cli/instance-download -->

# nsc instance download

Download a file from an instance.

`instance download` copies a file from a Namespace instance to your local machine.

## Usage

```
nsc instance download [instance-id] <remote-path> [local-path]
```

### Example

Download a file from an instance:

```
$ nsc instance download 85a32emcg99ii /var/log/app.log ./app.log
Downloaded /var/log/app.log (342 KiB). Took 2.3s.
```

## Options

### --container\_name, -c <name>

Target a container by name.

### --mkdir

Create parent directories locally if they don't exist.

Last updated February 13, 2026
