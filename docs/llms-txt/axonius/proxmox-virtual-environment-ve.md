# Source: https://docs.axonius.com/docs/proxmox-virtual-environment-ve.md

# Proxmox Virtual Environment (VE)

Proxmox Virtual Environment (VE) is an open source server virtualization management solution based on QEMU/KVM and LXC.

### Asset Types Fetched

* Devices

## Before You Begin

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [Proxmox REST API v2](https://pve.proxmox.com/pve-docs/api-viewer/index.html).

### Permissions

The value supplied in [User Name](#required-parameters) must have read access to devices - 'PVEAuditor' role. For more details, see [Proxmox VE - Permission Management](https://pve.proxmox.com/wiki/User_Management#pveum_permission_management).

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Proxmox Domain** - The hostname or IP address of the Proxmox VE server.
2. **Port** - Connection port.
3. **User Name** and **Password**  - The credentials for a user account that has the Required Permissions to fetch assets.
   A user is often internally identified by their user name and realm in the form `<userid>@<realm>`

   Examples: <br />
   userid\@realm <br />
   root\@pam

   For more information about Proxmox realms, see [Authentication Realms](https://pve.proxmox.com/pve-docs/chapter-pveum.html#pveum_authentication_realms).

<Image alt="Proxmox Virtual Environment (VE)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Proxmox%20Virtual%20Environment%20(VE).png" />

### Optional Parameters

* **Verify SSL** - Verify the SSL certificate offered by the value supplied in **Proxmox Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Tags to parse as fields** - Enter a comma-separated list of tag keys to be parsed as device fields. Each tag is a key-value pair that is part of the **Adapter Tags** complex field.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>