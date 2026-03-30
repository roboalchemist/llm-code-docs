# Source: https://docs.axonius.com/docs/bitsight-security-ratings.md

# BitSight Security Ratings

BitSight Security Ratings are a data-driven and dynamic measurement of an organization’s cybersecurity performance.

| Attributes                  | Axonius Cyber Assets     | Axonius SaaS Applications |
| --------------------------- | ------------------------ | ------------------------- |
| Service Account Required?   | Yes                      | Yes                       |
| API Key Required            | Yes                      | Yes                       |
| API Key Permission          | Read access to devices   | Admin                     |
| Service Account Permissions | User                     | Admin                     |
| Required Adapter Fields     | BitSight domain, API Key | BitSight domain, API Key  |
| Assets Fetched              | Users                    | SaaS data                 |

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Aggregated Security Findings
* Groups
* SaaS Applications
* Domains & URLs
* Certificates
* Roles

## Parameters

1. **BitSight Domain** *(required, default: `https://api.bitsighttech.com`)* - The hostname or IP address of the BitSight server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Company Name (leave empty to fetch data from parent company)** *(optional, default: empty)* - Specify a company name to only fetch data associated with that company.

4. **CIDR Data CSV File** - Upload the .csv file with your CIDR data. This is a CSV file that allows adding data for a specific IP CIDR range. The CSV file should contain the following columns, "CIDR Block", "Country", "Attributed To", "Source", "AS Number". If an IP address is contained in the CIDR block in the CSV file, the values from the other columns in this file are applied to the device.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="bitsight" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-9D93BBIZ.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Use My Company Only if company name is missing** *(default: true)* - Select whether to automatically use the name of your organization for this adapter if no name has been manually set.
2. **Fetch vulnerabilities and company's findings** - Select this option to fetch vulnerabilities detected in BitSight.
3. **Fetch only findings that affects rating** - Select to fetch only findings that have an impact on the letter grade.
4. **Fetch company assets** - Select this option to fetch company assets.
5. **Fetch infrastructure changes** - Select this option to fetch infrastructure changes.
6. **Fetch company security ratings** - Select to fetch latest company security rating for each company and add it to the device.
7. **Parse Asset Name and Host Name from Domain** - Select to fetch and parse devices' Asset Name and Host Name from the domain.
8. **Fetch devices from X days ago** - Specify a number of last days to fetch devices from.
9. **Parse Domains as Devices** - Select to fetch ULRs or Domains as Devices.

## Required Permissions

* **For accounts with Axonius Cyber Assets** - The value supplied in [API Key](#parameters) must be associated with a user account that has read access to devices.
* **For accounts with Axonius SaaS Applications** - The BitSight user must be associated with the 'Admin' role. For more information see [Creating a User in BitSight](/docs/bitsight-security-ratings#creating-a-user-in-bitsight).

## Setting Up the Integration

### Creating a User in BitSight

1. Log into the BitSight admin panel as Administrator.

2. Navigate to **Settings `>` Manage Users**.

   <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Bitsight_Manage%20Users.png" />

3. Create a new user:
   * If you have Axonius SaaS Applications, from Roles, select **Admin**.
   * Otherwise, the adapter requires the least-privileged type of user, which is the **User** role.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(521\).png)

4. Once added, you should receive an approval email from BitSight to the specified mail address.

5. Click the attached link to set a new password of at least 32 characters.

### Create an API Token

1. Log into the panel Navigate to **settings `>` account**.
2. Scroll down to API Token and click **Generate New Token**.

   <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(522).png" />
3. Copy the generated token.
4. In Axonius, paste the copied token into the **API Key** field.

<br />

### Related Enforcement Actions

* [BitSight - Create User](/docs/bitsight-create-user)
* [BitSight - Assign Role to User](/docs/bitsight-assign-role-to-user)
* [BitSight - Assign Group to User](/docs/bitsight-assign-group-to-user)