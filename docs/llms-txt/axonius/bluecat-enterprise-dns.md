# Source: https://docs.axonius.com/docs/bluecat-enterprise-dns.md

# BlueCat Enterprise DNS

BlueCat Enterprise DNS connects all disparate DNS and DHCP with centralized management of all clients and critical assets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Networks

## Parameters

1. **Host** *(required)*  - The URL of the BlueCat management server (e.g., `https://bluecat.company.com`).

2. **User Name** and **Password** *(required)*  - Specify valid username and password, that are dependent on the connection option you have chosen:
   * API - Username and password must be created in BlueCat.  The user account must have the “API User” privilege assigned.  Please see details below.
   * Database connection - Username and password with read permissions for the configured database. The best practice is to create a designated user for Axonius usage.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. **Connect to Database** *(required, default: False)* - Choose whether to use an API or database connection to fetch data from BlueCat.

8. **Use BlueCat API v2** - Select whether to use BlueCat API V2.

9. **Database Port** and **Database Name**  *(optional)* - Database port and name are mandatory if you have chosen to use database connection to fetch data from BlueCat.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="BlueCat Enterprise DNS" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BlueCat%20Enterprise%20DNS.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Time in seconds to sleep between each request** *(optional, default: 0)* - Specify sleeping time in seconds between each API request Axonius sends to BlueCat.
2. **Get extra host data** *(required, default: True)*
   * If enabled, all connections for this adapter will fetch devices extended host data.
   * If disabled, all connections for this adapter will not fetch devices extended host data.
3. **Parse Address Name as HostName for DHCP records** - Select this option to use the Address Name as the HostName for DNS records.
4. **Enforce Asset Name Uniqueness** - Select to use address IP to enforce asset name uniqueness.
5. **Drop static/gateway records with no expiry time** *(required, default: True)*
   * If enabled, all connections for this adapter will not fetch static/gateway records without expiry time.
   * If disabled, all connections for this adapter will  fetch static/gateway records without expiry time.
6. **Entities per page** *(required, default: 100)*  - Set the number of results per page received for a given query to BlueCat API, to gain better control on the performance of all connections for this adapter.
7. \*\*Exclude no 'Last Seen`devices** *(required, default: False)* - Select whether to exclude devices that do not have`last seen' indication.
8. **Exclude by Network CIDR or Network Name** - Enter a comma-separated list of strings that represent a network CIDR or network name in BlueCat. If the device is part of these networks then it will be excluded from the fetch.

<Callout icon="📘" theme="info">
  Note

  If a string contains a comma inside it, you must put the string itself into double quotes.
</Callout>

7. **Fetch Tags** - Select this option to fetch tags from BlueCat.
8. **Non-Expiring device states include list**  *(optional, default STATIC, GATEWAY)* - When the expiry\_time is null then enter statuses by which to filter devices. Only devices whose status are in this list will be fetched. Examples include: UNALLOCATED, STATIC, DHCP\_ALLOCATED, DHCP\_FREE, DHCP\_RESERVED,
   DHCP\_LEASED, RESERVED, GATEWAY. Enter 'None' to include devices with a null/None state or assets with no expiry time. Find a list of valid values in [BlueCat Enterprise DNS documentation](https://docs.bluecatnetworks.com/r/Address-Manager-API-Guide/DNS/9.3.0)
9. **Invalid device states exclude list** - Enter statuses that the adapter will not fetch. Networks in these states will not be fetched.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [BlueCat Address Manager RESTful v2 API](https://docs.bluecatnetworks.com/r/en-US/Address-Manager-RESTful-v2-API-Guide/9.5.0).

## Creating User for Axonius in BlueCat

The user account in Step 2 can be created by accessing the “Administration” and “Users and Groups” sections of the BlueCat management UI.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(366).png" />

Please ensure the user account has the “API User” permissions assigned to a read only group.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(367).png" />