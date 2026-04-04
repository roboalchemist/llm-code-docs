# Tailscale Documentation

This directory contains documentation for Tailscale, a VPN built on WireGuard.

## Quick Navigation

### Installation & Setup
- [Installation on macOS](1017-install-mac.md)
- [macOS Variants (App Store vs Standalone)](1065-macos-variants.md)
- [Running tailscaled CLI on macOS](1193-tailscaled-macos.md)
- [Installation on Linux](1054-install-linux.md)
- [Installation on Windows](1018-install-windows.md)
- [Getting Started](1016-start-using.md)

### CLI & Command Reference
- [CLI Reference](1080-cli-reference.md)
- [Authentication Keys](1085-auth-keys.md)

### Configuration & Advanced
- [Key Expiry and Authentication](1028-key-expiry.md)
- [DNS and MagicDNS](1082-dns.md)
- [Custom DERP Servers](1069-custom-derp.md)

### Self-Hosted Options
- [Headscale - Self-hosted Control Server](1143-headscale.md)

## macOS-Specific Guide

If you're setting up Tailscale on macOS:

1. **Choose your variant** - See [macOS Variants](1065-macos-variants.md) for differences between App Store and Standalone
2. **Install** - Follow [Installation on macOS](1017-install-mac.md)
3. **Use the CLI** - If using Standalone, see [Running tailscaled on macOS](1193-tailscaled-macos.md)
4. **Connect to custom servers** - Use `--login-server` flag in [CLI Reference](1080-cli-reference.md)

## CLI Essentials

Common commands:
- `tailscale up` - Connect to Tailscale
- `tailscale down` - Disconnect
- `tailscale status` - View connections
- `tailscale ip` - Get device's Tailscale IP
- `tailscale login --login-server=<url>` - Connect to custom server (e.g., Headscale)

See [CLI Reference](1080-cli-reference.md) for complete documentation.

## Self-Hosted with Headscale

To connect to a self-hosted Tailscale server (Headscale):

1. Use `--login-server=https://your-headscale-url`
2. Authentication and key management work the same way
3. See [Headscale documentation](1143-headscale.md) for setup

---

**Source:** https://tailscale.com/kb/
**Last Updated:** 2026-02-01
