# Key Expiry in Tailscale

**Source:** https://tailscale.com/kb/1028/key-expiry

---

## Overview

Tailscale implements periodic reauthentication as a security measure. The default expiration period is 180 days for newly created domains. When keys expire, connections from that endpoint stop functioning.

## Managing Key Expiry

### Disabling Expiry

Users can disable key expiration on specific devices through the admin console's Machines page by selecting the menu and choosing **Disable Key Expiry**. This option suits trusted servers, subnet routers, and remote devices that are difficult to access.

### Enabling Expiry

To re-enable expiration, users follow the same process in the admin console and select **Enable Key Expiry**.

## Renewing Expired Keys

For devices with the Tailscale CLI, running `tailscale up --force-reauth` renews expired keys. However, this command may temporarily disconnect the device—a concern for remote systems accessed via SSH or RDP.

When a device becomes inaccessible due to key expiration, administrators can temporarily extend the key's lifetime by 30 minutes through the admin console. This window allows the device owner to reauthenticate or disable key expiry entirely.

## Custom Settings

Administrators can configure custom authentication periods between 1 and 180 days via the Device Management settings. Changes apply to newly logged-in devices; existing sessions remain unaffected until the next login.

## Tagged Devices Note

Tagged devices have key expiry disabled by default upon initial authentication.
