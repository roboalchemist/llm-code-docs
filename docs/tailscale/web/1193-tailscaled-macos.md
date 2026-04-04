# Tailscale SSH Documentation

**Source:** https://tailscale.com/kb/1193/tailscaled-macos

---

## Overview

Tailscale SSH enables centralized authentication and authorization for SSH connections within your tailnet. Rather than managing individual SSH keys, Tailscale leverages its existing WireGuard infrastructure and identity system.

## Key Capabilities

### Authentication & Encryption

- Tailscale manages authentication using node keys distributed across your network
- Connections receive dual encryption: WireGuard at the network layer plus SSH protocol encryption
- "SSH as normal" workflow—no new binaries or configurations required

### Access Control

Tailscale enforces SSH policies through its access control system, allowing administrators to:
- Restrict SSH access by user, group, or device tags
- Require periodic re-authentication via check mode
- Revoke access instantly by updating policies

### Session Management

- Optional check mode requires users to re-authenticate for high-risk connections
- Default check period is 12 hours; customizable down to 1 minute
- Sessions terminate if access policies are modified

## Configuration Steps

### Prerequisites

Server support is limited to:
- Linux systems
- macOS (open source `tailscaled` variant only)

Clients may run any Tailscale-supported platform.

### Setup Process

1. **Enable SSH on destination host:**
   ```
   tailscale set --ssh
   ```
   This generates cryptographic material and configures port 22 interception.

2. **Configure access policies** via the admin console's Access Controls section to define:
   - Network connectivity rules (any connections between source and destination)
   - SSH-specific rules (users and destinations permitted for SSH)

3. **Connect via hostname:**
   ```
   ssh user@device.tailnet-name.ts.net
   ```
   Or using Tailscale IP addresses (format: 100.x.x.x)

## Policy Structure

SSH access rules require:
- **Source:** User, group, tag, or autogroup originating the connection
- **Destination:** Tagged device or autogroup receiving the connection
- **Users:** Host-level usernames allowed (e.g., `autogroup:nonroot`)
- **Action:** Either `accept` or `check` (with optional `checkPeriod`)

Rules are evaluated by restrictiveness—check policies override accept policies for the same connection.

## Important Limitations

- Tailscale SSH only works on Tailscale-connected devices; subnet router devices cannot participate
- SSH port cannot be customized from port 22
- Restarting the Tailscale daemon terminates active sessions
- Incompatible with Synology and QNAP devices
- Any OS user on the client can initiate connections (lacks traditional SSH key file restrictions)

## Disabling Tailscale SSH

To disable on a single device:
```
tailscale set --ssh=false
```

To disable network-wide, remove SSH rules from access control policies and disable SSH on all hosts.
