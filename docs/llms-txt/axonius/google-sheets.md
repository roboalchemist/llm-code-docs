# Source: https://docs.axonius.com/docs/google-sheets.md

# Google Sheets

Google Sheets is a spreadsheet application included as part of the free, web-based Google Docs Editors suite offered by Google.
This adapter only connects to and uploads files from Google Sheets as a CSV source.

<Callout icon="💡" theme="warn">
  The dedicated Google Sheets adapter is now  **deprecated**. We have consolidated our Google Sheets capabilities into the **Custom Files** adapter  to provide a more streamlined experience.

  * **Existing Users:** Your current integrations will continue to function.
  * **New Users:** Please use the [Custom Files Adapter](/docs/custom-files) for all Google Sheets integrations.
</Callout>

### Use Cases the Adapter Solves

* **Automating Spreadsheet Ingestion**: Automatically pull asset data stored in Google Sheets into Axonius without manual exports.
* **Consolidating Decentralized Data**: Centralize asset information maintained by different teams in Google Sheets into a single source of truth.
* **Enriching Asset Inventories**: Supplement existing device and user data with custom attributes tracked in specialized spreadsheets.

### Asset Types Fetched

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg" /> Devices | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg" /> Users | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Vulnerabilities.svg" /> Aggregated Security Findings | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg" /> Software | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg" /> SaaS Applications | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Domains_URLs.svg" /> Domains & URLs |

<br />

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Service Account (JSON Key Pair)

### APIs

* Axonius uses the [Google Sheets API](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get?apix_params=%7B%22spreadsheetId%22%3A%221YyTVZaJN9xwdNZQas8BZMeEfxYcen9oHY5WBZj9EG0A%22%2C%22range%22%3A%22Top60%20Adapters%22%7D).

### Permissions

To use this adapter you have to:

* Enable Google Workspace API and/or Google Sheets API.
* Scope granted to service account - at minimum: `https://www.googleapis.com/auth/spreadsheets.readonly`.
* The Spreadsheet must be shared with the service account E-mail, at least with View permissions.

#### Supported From Version

Supported from Axonius version 5.0

### Setting Up Google Sheets to Work with Axonius

1. Create a service account for Google Workspace. Refer to [Service Account Credentials](https://developers.google.com/workspace/guides/create-credentials#service-account). If you have already created a [Service Account for the Google Workspace](/docs/g-suite-by-google#creating-a-service-account) adapter, then the same credentials may be used.
2. Make sure you add the required permissions listed above.
3. It is suggested you follow this guide to set up the [Service Account API](https://developers.google.com/sheets/api/quickstart/python).
4. Share the specific Spreadsheet with the service account E-mail (View permissions).

<br />

### File Structure

Refer to [Which Fields are Required for Each Import Type](/docs/csv#which-fields-are-required-for-each-import-type) in the CSV adapter for information about the structure of the files to import.

<br />

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **Google Sheets**, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **JSON Key pair for the service account** - A  JSON  Key Pair associated with a service account that has the [Required Permissions](#required-permissions) to fetch assets. Click **Upload File** to upload a file containing the binary contents of the keypair file (JSON) generated for the service account credentials.
2. **Spreadsheet ID** - The Spreadsheet ID (gathered from the link to the spreadsheet).
3. **Data Range** - *( A1 or R1C1 notation)* - A1 or R1C1 notation of the data range to read. Example: 'My Worksheet'!A1:Z99 to pull cells A1 to Z99 from the worksheet “My Worksheet”. Always use single-quotes when specifying a worksheet that contains spaces in the name. A data range and a worksheet range must be specified  as an absolute path.
4. **Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters).

<Image align="center" alt="Google Sheets connection screen" border={false} width="500" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GoogleSheets.png" />

### Optional Parameters

1. **Range contains users information** - Select this option to import the file as a list of users instead of devices.
2. **Range contains URLs and domains information** - Select this option to fetch URL and domain assets from a spreadsheet.
3. **Range contains installed software information** - Select this option to import an installed software list instead of devices.
4. **Custom prefix for dynamic fields** - Specify a prefix to be added for dynamic fields Dynamic fields refer to any field that is not part of an asset default fields. This can assist you in identifying such fields.
5. **Multi-value fields delimiter** - Specify a delimiter (e.g., ';') to separate values within the same field in the imported  file.
6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.
7. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
8. **HTTPS Proxy User Name** - The user name for the HTTPS Proxy.
9. **HTTPS Proxy Password** - The password for the HTTPS Proxy.
10. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>