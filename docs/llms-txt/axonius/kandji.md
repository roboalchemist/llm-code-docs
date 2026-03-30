# Source: https://docs.axonius.com/docs/kandji.md

# Kandji

Kandji is an Apple device management (MDM) solution for macOS, iOS, iPadOS, and tvOS.

The Kandji adapter enables Axonius to fetch and catalog Apple devices, providing visibility into their configuration, installed software, and vulnerability status.

## Asset Types Fetched

* Devices
* Aggregated Security Findings
* Users
* Software
* SaaS Applications

## Before You Begin

### Required Ports

* TCP Port 443 (HTTPS)

### Required Permissions

The Kandji adapter requires an **API Token** with permissions to read the relevant data types.

### Creating a User Account in Kandji

<Callout icon="💡" theme="warn">
  Important

  * While to access SaaS data you need to grant roles and/or permissions that include write capabilities, the adapter only actually reads data from the application.
  * Creating a dedicated service user account ensures the integration remains stable regardless of future staff changes.
</Callout>

1. From the Kandji console, click  **Settings** in the left-hand navigation bar.
2. Select the **Access** tab.
3. Click **New User** on the top right.
4. Fill in the **First Name**, **Last Name**, and **Email Address** fields.
5. Choose an **Admin** access level for the new team member.
6. Click **Submit**.
7. Log in to the supplied email address and open the Kandji invitation. Complete the login process and supply a password.

### Creating an API Token in Kandji

1. Login with an admin user or with the user account you just created.
2. From the Kandji console, click  **Settings** in the left-hand navigation bar.
3. Log in and click on **Settings**.
4. Click the **Access** tab.
5. Click **Add API Token**.
6. Provide a **Name** and a **Description** for your API token.
7. Click **Create**.
8. Copy the generated token.
9. Click **Next.**
10. In Axonius configuration, paste the copied token in the API Token field.
11. Configure the token permissions:
    1. Back in Kandji, Click **Configure**.

    2. In the **Devices** section, select the following options:
       * Device details
       * Device list
       * Device ID
       * Application list
       * Device Parameters

    3. Click **Save**.

### APIs

Axonius uses the <Anchor label="Iru Endpoint Management API" target="_blank" href="https://api.kandji.io/">Iru Endpoint Management API</Anchor> and its <Anchor label="Devices API" target="_blank" href="https://api.kandji.io/#78209960-31a7-4e3b-a2c0-95c7e65bb5f9">Devices API</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 4.5.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the Kandji server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Token** - Enter the API Token associated with a user account that has permissions to fetch assets.
   To generate an API Token, see <Anchor label="Generate an API Token" target="_blank" href="https://support.kandji.io/api">Generate an API Token</Anchor>.

<Image align="center" alt="Kandji adapter - Add Connection" border={true} width="100% " src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Kandji_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Enrich device information** - Select this option to retrieve additional details for each device, including disk encryption status, FileVault information, and other security parameters.
2. **Fetch applications** - Select this option to retrieve the list of installed applications for each device.
3. **Fetch ADE (automated device enrolled) devices** - Select this option to include devices enrolled via Apple's Automated Device Enrollment (ADE) program in the fetch.
4. **Enrich device with detected vulnerabilities** - Select this option to fetch vulnerability data detected on the devices. When enabled, the adapter retrieves CVE details and associates them with the corresponding assets.

### Related Enforcement Actions

* [Kandji - Delete User](/docs/kandji-delete-user)

<br />

<br />