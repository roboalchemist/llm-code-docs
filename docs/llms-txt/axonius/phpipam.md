# Source: https://docs.axonius.com/docs/phpipam.md

# phpIPAM

phpIPAM is an open-source web IP address management application (IPAM).

## Asset Types Fetched

This adapter fetches the following types of assets:

* Devices, Users, Networks

## Before You Begin

## APIs

Axonius uses the [phpIPAM API](https://phpipam.net/api/api_documentation/).

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to devices.
To read users, the supplied [User Name](#parameters) must have rwa permissions.

### Setting Up phpIPAM to Work with Axonius

To gain access to the API:

1. Login to phpIPAM with a user that has admin permissions.

2. Go to **Settings**   and enable the API module.

3. Go to **Settings** →  **API** and click **Create API key** to create a new API App (application). The application should have **Read** permissions.  Set all APP params as desired for your APP.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1048\).png)

4. Use the **App id** in the [Application ID](#parameters) field in the adapter connection configuration dialog.

Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **phpIPAM Host Name** *(required)* - The hostname or IP address of the phpIPAM server.

2. **Application ID** *(required)* - The App id that you received when creating the API App in phpIPAM.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Image alt="phpIPAM adapter" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/phpIPAM.png" />

### &#x20;Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **Fetch Users**  - Select whether to fetch users' data from the phpIPAM server.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1307).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **CIDR exclude list** - Specify a comma-separated list of CIDRs to be excluded.
2. **CIDR include list** - Specify a comma-separated list of CIDRs to be included.
3. **Fetch subnets addresses as devices** - Select whether to fetch all the addresses under all the subnets in phpIPAM and create devices from these addresses
   * API used -  /api/my\_app/subnets/`{id}`/addresses/

<Callout icon="📘" theme="info">
  NOTE

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

<br />