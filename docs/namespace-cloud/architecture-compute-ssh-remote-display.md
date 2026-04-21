<!-- Source: https://namespace.so/docs/architecture/compute/ssh-remote-display -->

# SSH / Remote Display with Namespace Compute

## Remote Display

Namespace supports visual debug access through multiple options which is invaluable for debugging GUI applications, testing user interfaces, and investigating display-related issues.

### VNC Integration

Access your Mac runners through Remote Display (VNC) directly from the Namespace [dashboard](https://cloud.namespace.so/workspace/instances).

![Tahoe Remote Display](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftahoeremotedisplay.b8f208ef.png&w=1200&q=75)

You can also start a VNC session using our [CLI](/docs/reference/cli/installation):

```
$

```
nsc vnc <instance-id>
```
```

VNC support is currently available for macOS runners. Support for other platforms is in development.

### RDP Access

To gain interactive, visual access to your Windows runners, you can rely on our RDP integration.

![Windows RDP](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fwindows-demo.338ac8f5.png&w=1200&q=75)

You can start an RDP session using our [CLI](/docs/reference/cli/installation).

```
$

```
nsc rdp <instance-id>
```
```

RDP credentials are printed on the CLI and currently need to be entered in the RDP client manually.

## SSH Access

Connect to any running instance via SSH for command-line debugging and investigation.
Perfect for examining file systems, running diagnostic commands, and troubleshooting build environments.
The simplest path to jump into an interactive terminal is through your browser with our web SSH interface.

![Terminal access](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fwebterminal.2c3ff973.png&w=1200&q=75)

Alternatively, you can jump into an SSH session from your command line.
To open an SSH session, you can use our [CLI](/docs/reference/cli/installation):

```
$

```
nsc ssh <instance-id>
```
```

SSH access is available for Linux and macOS runners, with Windows support coming soon.

To use native SSH, supply your public key when creating an instance:

```
$

```
nsc create --ssh_key ~/.ssh/id_ed25519.pub
```
```

and then connect to it using:

```
$

```
ssh <instance-id>@ssh.<region>.namespace.so
```
```

**Note:** If you'd like to use your GitHub SSH key with native SSH instead, reach out to our [support team](mailto:support@namespace.so) to get it enabled.

## API Reference

SSH credentials can be obtained programmatically via the [ComputeService](https://buf.build/namespace/cloud/docs/main:namespace.cloud.compute.v1beta)
`GetSSHConfig` RPC. It returns:

- A short-lived **SSH private key** with access restricted to the specified instance.
- The **username** and **endpoint** to connect to.

You can optionally specify a `target_container` to open an SSH session directly inside a specific
container running on the instance.

Last updated March 23, 2026
