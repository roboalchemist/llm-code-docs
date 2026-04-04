# Three Ways to Run Tailscale on macOS

**Source:** https://tailscale.com/kb/1065/macos-variants

---

## Overview

Tailscale requires macOS 12.0 (Monterey) or later. The application offers three installation variants, each with distinct features and trade-offs for different use cases.

## Installation Options

### 1. Standalone Variant (Recommended)

The Standalone variant uses Apple's system extensions framework, introduced in macOS 10.15. This approach provides:

- **No Apple ID required** for installation
- **Faster security updates** without App Store review delays
- **Conflict detection** for third-party VPN tools
- Access to more features than App Store limitations allow
- Direct installation from Tailscale's package server

### 2. Mac App Store Variant

Available through the official Mac App Store, this option features:

- **Easy setup** for users already in the Apple ecosystem
- **Sandboxed operation** for enhanced isolation
- **Apple ID requirement** for installation and updates
- Notable limitation: incompatibility with Screen Time web filter
- Restricted functionality due to App Sandbox constraints

### 3. Open Source CLI Variant (tailscaled)

The command-line only distribution offers:

- **No GUI required** — full management via terminal commands
- **Open source code** available on GitHub
- **Recommended only for experienced administrators** managing unattended installations
- Limited Taildrop support and no exit node usage capability

## Comparison Summary

| Feature | App Store | Standalone | CLI (tailscaled) |
|---------|-----------|-----------|------------------|
| **GUI** | Yes | Yes | No |
| **Apple ID Required** | Yes | No | No |
| **Auto-Updates** | App Store managed | In-app | Manual |
| **Screen Time Compatible** | No | Yes | Yes |
| **MDM Support** | Yes | Yes | No |
| **Open Source** | No | No | Yes |

## Recommendation

Begin with the Standalone variant unless you specifically need App Store deployment. Install the Mac App Store version only if Standalone installation isn't feasible or your deployment strategy requires it.

**Warning:** Never run both Standalone and App Store variants simultaneously on the same machine, as this prevents the extension from launching properly.
