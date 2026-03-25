# Source: https://docs.axonius.com/docs/nexthink.md

# Nexthink

Nexthink is an IT solution that provides insights into activity across devices, operating systems, and workplace locations to improve IT experiences for employees.

<Callout icon="📘" theme="info">
  Note

  This API is deprecated by Nexthink. To connect to Nexthink, use only the [Nexthink Query Language (NQL)](/docs/nexthink-infinity-nql) adapter.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* -
   * For an on-premises instance:
     Specify the hostname or IP address of the on-premises Nexthink server.
   * For a cloud-based instance:
     You need to query the Nexthink Cloud engine to obtain the host name.

     To query the Nexthink Cloud engine:

     * Use a Web API request with the format:

```
https://-engine-X..nexthink.cloud/2/query?platform=windows&platform=mac_os&query=(select%20(device_uid%20name)%20(from device))&format=csv
```

The Engine returns the list of unique identifiers and names of all Windows and Mac OS devices in CSV format.
For more information about setting the names of the engines, see [Setting the Names of the Engines](https://doc.nexthink.com/Documentation/Nexthink/V6.29/InstallationAndConfiguration/SettingthenamesoftheEngines).

2. **Port** *(required, default: 1671)* - The port in which Axonius is able to communicate.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
4. **Limit Fetched Data to Last x Days** *(required, default: 3)* - Specify how many days Axonius should fetch data from the connection of this adapter.
5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Nexthink" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nexthink.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Fetch local users** *(optional, default: true)* - Clear the option to exclude members of local user groups from a fetch.

2. **Fetch domain users** *(optional, default: true)* - Clear the option to exclude members of domain user groups from a fetch.

3. **Fetch system users** *(optional, default: true)* - Clear the option to exclude members of system user groups from a fetch.

4. **Fetch unknown users** *(optional, default: true)* - Clear the option to exclude unknown users from a fetch.

5. **Fetch installed software for devices** *(optional, default: false)* - Select whether to include installed software in the fetch.

6. **Drop DWM/UMFD accounts** - Select this option to ignore DWM/UMFD accounts

7. **Fetch highest local privilege reached** - Select this option to fetch the field called ‘Highest Local Privilege Reached’.  This information can help determine whether a user is an admin user.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Nexthink Web API V2](https://doc.nexthink.com/Documentation/Nexthink/latest/APIAndIntegrations/Overview).

## Required Permissions

* The value supplied in [User Name](#parameters) must have read access to devices.

* Any account with **Data Privacy** set to none (full access) and the option **Finder access** enabled can make use of the Web API. Otherwise, the Web API will reject the credentials of the account. Moreover, only those users with the right to edit categories can perform updates through NXQL queries.

* User credentials are verified with basic HTTP authentication. For a given user, the visibility and info levels are identical to those defined in their profile in the Portal.

* The access account requires admin rights to access the installed software data from Nexthink.

<Callout icon="📘" theme="info">
  Note

  Note that any change that you make in the Portal to an account is not immediately propagated to the Engine. The synchronization between Engine and Portal can take up to five minutes.

  In practice, that means that you can have some temporary inconsistencies regarding the permissions of the accounts in Nexthink. For instance, if you remove Finder access from an account by changing its profile to prevent it from accessing the Web API, that account might still be able to query an Engine via the Web API for a few minutes before synchronization takes place and its credentials are invalidated.
</Callout>

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                  | Supported | Notes |
| ------------------------ | --------- | ----- |
| Nexthink V6.0 and higher | Yes       |       |