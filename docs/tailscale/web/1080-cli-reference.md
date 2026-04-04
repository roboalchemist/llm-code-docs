# Tailscale CLI Documentation

**Source:** https://tailscale.com/kb/1080/cli

---

## Overview

Tailscale includes a built-in command-line interface for managing devices within a Tailscale network (tailnet). The CLI is available across all pricing plans and supports tab-completion for enhanced usability.

## Getting Started

### Platform-Specific Access

**Linux:** The `tailscale` binary is typically in your `$PATH`:
```shell
tailscale <command>
```

**macOS & Windows:** Access varies by installation method. Refer to platform-specific documentation.

**Mobile:** No CLI support exists for iOS or Android.

### Tab Completion

Enable shell completion with:
```shell
tailscale completion <shell> [--flags] [--descs]
```

Supported shells: Bash, Zsh, Fish, PowerShell

## Essential Commands

### Connection Management

**`tailscale up`** - Connect to Tailscale with optional authentication
```shell
tailscale up [flags]
```
Key flags include `--accept-routes`, `--advertise-exit-node`, `--shields-up`, and `--ssh`

**`tailscale down`** - Disconnect from Tailscale
```shell
tailscale down
```

**`tailscale login`** - Authenticate and join your tailnet
```shell
tailscale login [flags]
```

**`tailscale logout`** - Sign out and invalidate credentials

### Network Diagnostics

**`tailscale status`** - View connection status to network peers
```shell
tailscale status [--json]
```
Returns peer information including IP addresses, machine names, connection types, and traffic metrics.

**`tailscale ping`** - Test connectivity over Tailscale
```shell
tailscale ping <hostname-or-ip>
```

**`tailscale netcheck`** - Report physical network conditions and relay latencies

**`tailscale whois`** - Identify machines and users by Tailscale IP
```shell
tailscale whois ip[:port] [--json]
```

### File & Service Sharing

**`tailscale file`** - Transfer files via Taildrop
```shell
tailscale file cp <files...> <target>:
tailscale file get <target-directory>
```

**`tailscale serve`** - Share local services within the tailnet
```shell
tailscale serve <target>
```

**`tailscale funnel`** - Expose local services to the internet
```shell
tailscale funnel <target>
```

### Advanced Configuration

**`tailscale ssh`** - Establish secure SSH sessions
```shell
tailscale ssh <args>
```

**`tailscale set`** - Modify specific preferences without full reconnection
```shell
tailscale set [flags]
```

**`tailscale cert`** - Generate Let's Encrypt certificates
```shell
tailscale cert hostname.tails-scales.ts.net
```

**`tailscale lock`** - Manage Tailnet Lock security features
```shell
tailscale lock <subcommand>
```

### System Information

**`tailscale version`** - Display Tailscale version details
```shell
tailscale version [flags]
```

**`tailscale ip`** - Retrieve device Tailscale IP address
```shell
tailscale ip [flags] [<hostname>]
```

**`tailscale bugreport`** - Generate diagnostic data for troubleshooting

## Additional Commands

- **`dns`** - Configure Tailscale DNS settings
- **`drive`** - Manage Taildrive shares
- **`configure`** - Set up resources (Kubernetes, VPN, Synology, etc.)
- **`exit-node`** - List and manage exit nodes
- **`metrics`** - Expose client metrics
- **`nc`** - Connect to remote ports
- **`switch`** - Manage multiple accounts
- **`update`** - Update Tailscale client version
- **`web`** - Start web interface server
- **`syspolicy`** - Inspect system policy settings
- **`appc-routes`** - View app connector route status

## Common Flags

All commands accept:
- `--socket=<path>` - Specify tailscaled socket location
- `--help` - Display command documentation
