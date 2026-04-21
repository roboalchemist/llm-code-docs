# Architecture - SSH and Remote Access

Documentation on how Namespace Compute provides remote access capabilities for debugging and interactive sessions across different operating systems.

## Remote Display Options

### VNC for macOS

Access Mac runners through visual remote display:

- Via dashboard
- Via CLI: `nsc vnc <instance-id>`

### RDP for Windows

Interactive visual access to Windows runners:

- Via CLI: `nsc rdp <instance-id>`
- Credentials provided via CLI

### SSH Access

The platform supports command-line debugging through multiple methods:

**Browser-based access:**

- Web SSH interface for terminal access directly in dashboard

**CLI-based access:**

- `nsc ssh <instance-id>`

**Native SSH connections:**

- Provide a public key during instance creation: `nsc create --ssh_key ~/.ssh/id_ed25519.pub`
- Connect directly: `ssh <instance-id>@ssh.<region>.namespace.so`

SSH is available for Linux and macOS, with Windows support noted as coming soon.

## Technical Details - ComputeService API

For programmatic access, the **ComputeService** API's `GetSSHConfig` RPC provides:

- Short-lived SSH private keys with instance-specific access restrictions
- Connection username and endpoint details
- Optional container-specific SSH sessions via the `target_container` parameter

## Connection Methods Summary

| OS | SSH | VNC | RDP |
|---|---|---|---|
| Linux | Yes | No | No |
| macOS | Yes | Yes | No |
| Windows | Coming Soon | No | Yes |

## Security

All connections are:

- Tunneled securely through the Namespace API
- End-to-end encrypted
- No public IP addresses exposed
