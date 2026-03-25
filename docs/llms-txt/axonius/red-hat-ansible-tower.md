# Source: https://docs.axonius.com/docs/red-hat-ansible-tower.md

# Red Hat Automation Controller (Ansible Tower)

Red Hat Automation Controller (Ansible Tower) is a web console and REST API for operationalizing Ansible across teams, organizations, and the entire enterprise.

**Related Enforcement Actions**

* [Red Hat Ansible Tower - Run Command](/docs/run-ansible-command)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Ansible Tower Domain** *(required)* - The hostname of the Red Hat Ansible Tower server.
2. **User Name** and **Password** *(optional)* – The user name and password for an Ansible Tower user configured with a **System Auditor** user type. For more details on Ansible Tower users, see [Ansible Tower User Guide - Users](https://docs.ansible.com/ansible-tower/latest/html/userguide/users.html).

<Callout icon="📘" theme="info">
  Note

  When **API Token** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **API Token** *(optional)* - An API Token associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Token** is required.
</Callout>

4. **Verify SSL**  - Select to verify the SSL certificate offered by the value supplied in **Ansible Tower Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Ansible Tower Domain**.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Ansible Tower Domain** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Ansible Tower Domain** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![RedHatAutomationController](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RedHatAutomationController.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Switch hostname** - Toggle on this option to use the value of another field as the hostname value. Available options are displayed.
2. **Parse hostname with description** -   Select this option to use the value of the *Description* field in the *Host Name* field if the description field exists.  This option is only available when  *Switch hostname*  is enabled.
3. **Set Device ID to Name** - Select this option to enable using the device name for the asset ID.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Red Hat Ansible Tower API](https://docs.ansible.com/ansible-tower/latest/html/towerapi/index.html).