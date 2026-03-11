# Source: https://docs.axonius.com/docs/keeper.md

# Keeper Secrets Manager

Keeper Secrets Manager is a secrets management solution that provides zero-knowledge security and automated credential rotation across DevOps, infrastructure, and CI/CD environments.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [Keeper Secrets Manager SDK](https://docs.keeper.io/enterprise-guide/developer-tools).

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 5.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Keeper Secrets Manager server.

2. **User Name** and **Password** - The credentials for a user account that is able to fetch assets.

![Keeper](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Keeper.png)

### Optional Parameters

1. **2FA Secret Key** - The secret generated in Keeper for setting up two-factor authentication for the adapter user. Even though your 2FA might not be mandatory for your own configuration, when connecting the Keeper Secrets Manager adapter 2FA is required.  Refer to [Keeper Two-Factor Authentication](https://docs.keeper.io/en/secrets-manager/secrets-manager/about/one-time-token) for information on how to set up two-factor authentication for the Axonius user.

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

### Related Enforcement Actions

* [Keeper Secrets Manager - Delete User](/docs/keeper-delete-user)