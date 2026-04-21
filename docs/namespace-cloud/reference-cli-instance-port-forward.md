<!-- Source: https://namespace.so/docs/reference/cli/instance-port-forward -->

# nsc instance port-forward

Opens a local port which connects to the instance.

`instance port-forward` creates a tunnel from a local port to a port on a Namespace instance. This is useful for accessing services running inside an instance without exposing them publicly.

## Usage

```
nsc instance port-forward [instance-id] --target_port <port>
```

### Example

Forward local port 8080 to port 80 on the instance:

```
$ nsc instance port-forward 85a32emcg99ii --target_port 80
Listening on 127.0.0.1:8080
```

## Options

### --target\_port <port>

Which port to forward to on the remote instance.

Last updated February 13, 2026
