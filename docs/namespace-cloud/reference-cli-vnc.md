<!-- Source: https://namespace.so/docs/reference/cli/vnc -->

# nsc vnc

Start a VNC session.

`vnc` connects to a previously created instance via VNC, allowing you to access [graphical environments
on remote instances](/docs/architecture/compute/ssh-remote-display#vnc-remote-display).

VNC support is currently available for [macOS instances](/docs/architecture/compute/macos). Support for other platforms is in development.

## Usage

```
nsc vnc [instance-id]
```

### Example

Start a VNC session to a running instance, or omit the instance id to get a list of your instances.

```
$ nsc vnc 85a32emcg99ii
Connected to instance.
Opening VNC client...
```

Alternatively, you can also access VNC directly from the Namespace [dashboard](https://cloud.namespace.so/workspace/instances).

![Tahoe Remote Display](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftahoeremotedisplay.b8f208ef.png&w=1200&q=75)

## Options

`nsc vnc` has no options.

Last updated February 13, 2026
