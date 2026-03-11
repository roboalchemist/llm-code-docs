# Source: https://docs.axonius.com/docs/bloodhound.md

# BloodHound

BloodHound is used to find relationships within an Active Directory (AD) domain to discover attack paths.

The BloodHound adapter enables Axonius to fetch and catalog users and devices, providing visibility into identity relationships and potential attack paths.

## Asset Types Fetched

* Devices
* Users
* Groups

## Before You Begin

### Required Ports

* TCP port 80/443

### Authentication Methods

* User Name/Password for Cloud
* Token Key/Token ID for on-premises

### Required Permissions

The BloodHound adapter requires a **User** or **API Token** with permissions to access the BloodHound API and graph database.

The account must have the ability to:

* **Read Graph Data** - Retrieve details for Users, Devices, and Domains.
* **Execute Cypher Queries** - Run custom queries to identify privileged users and attack paths.
* **Access API Endpoints** - Specifically, access to endpoints for retrieving available domains and user admin rights.

### APIs

Axonius uses the [BloodHound API (v2)](https://support.bloodhoundenterprise.io/hc/en-us/articles/11311053342619-Working-with-the-BloodHound-API) to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 4.6.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the RoboShadow server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Username** and **Password** - Enter the credentials for a user account that has permissions to fetch assets.
3. **Token Key** and **Token ID** - The API Tokens associated with a user account that has permissions to fetch assets. For information on how to create a Token Key/ID pair, see <Anchor label="Working with the BloodHound API" target="_blank" href="https://support.bloodhoundenterprise.io/hc/en-us/articles/11311053342619-Working-with-the-BloodHound-API">Working with the BloodHound API</Anchor>.

<Callout icon="📘" theme="info">
  Note

  * When **User Name** and **Password** are not supplied, **Token Key** and **Token ID** are required.
  * When **Token Key** and **Token ID** are not supplied, **User Name** and **Password** are required.
</Callout>

<Image align="center" alt="Bloodhound adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/BloodHound_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

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

1. **Fetch Assets by Attack Path** - Select this option to discover assets based on BloodHound attack paths. When enabled, the adapter retrieves assets identified within potential attack vectors.
2. **Fetch Tier Zero Devices (Asset Groups Collections)** - Select this option to fetch devices identified as high-value Tier Zero assets within the BloodHound database.
3. **Fetch Computers Admin Users** - Select this option to fetch users who possess administrative rights on computers.
4. **Fetch Computers RDP Users** - Select this option to fetch users who have Remote Desktop Protocol (RDP) access rights on computers.
5. **Domain IDs to exclude from fetch** (*optional*) - Enter a list of domain IDs to exclude from the fetch process. Use this setting to filter out specific domains from data ingestion.
6. **Discover Privileged Users** - Toggle this option to identify and fetch users who hold administrative or privileged access rights within the environment.
7. **Include Associated Devices** - Select this option to enrich the fetched privileged users with their associated devices. This setting retrieves the devices where the user has admin rights and adds them to the user record. This option is available only when **Discover Privileged Users** is enabled.
8. **Fetch only enabled users** - Select this option to only fetch enabled users.