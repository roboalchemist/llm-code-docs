<!-- Source: https://namespace.so/docs/reference/cli/proxy -->

# nsc proxy

Provides proxy support for instance services.

`proxy` opens a local proxy to a service running on a Namespace instance.

## Usage

```
nsc proxy [instance-id] [--service <service>]
```

### Example

Proxy a VNC service from a running instance:

```
$ nsc proxy 85a32emcg99ii --service vnc
VNC:
  Endpoint: 127.0.0.1:54321
  Username: admin
  Password: secret123
```

## Options

### --service, -s <service>

The service to proxy (e.g. `vnc`, `rdp`).

### --output, -o <format>

Output format. One of `plain` or `json`. Default is `plain`.

### --output\_to <path>

If specified, write the JSON configuration to this path.

### --once

If set, stop the proxy after a single connection.

### --websocket

If set, outputs information to connect to the service directly using websockets.

Last updated February 13, 2026
