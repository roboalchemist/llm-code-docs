# Source: https://docs.axonius.com/docs/csv.md

# CSV

The CSV adapter imports .csv files with inventory information including devices and serial numbers, users, and installed software data.

<Callout icon="📘" theme="info">
  **Notes**

  * It is possible to configure the **CSV** adapter to fetch files from various storage places including: Microsoft OneDrive, Azure, Amazon S3, and more. See [File Sources](https://docs.axonius.com/axonius-help-docs/docs/file-sources) for the full list.

  * The **CSV** adapter parameters and functionality are common to all adapters that import files:
    * **[CSV](/docs/csv)** - imports .csv files.
    * **[JSON](/docs/json)** - imports .json files.
    * Custom Files - imports .csv, .json, .txt and .xml files.
    * **[F-Secure Policy Manager](/docs/f-secure-policy-manager)** - imports .csv files.
    * [**Forcepoint Web Security Endpoint CSV File**](/docs/forcepoint-web-security-endpoint) - imports .csv files.
    * **[L0phtCrack 7](/docs/l0phtcrack-7)** - imports .csv files.
    * **[Masscan](/docs/masscan)** - imports .json files.
    * **[Nmap Security Scanner](/docs/nmap-security-scanner)** - imports .xml files.
    * **[Tenable Nessus CSV File](/docs/tenable-nessus-csv-file)** - imports .csv files.
    * [**Varonis CSV**](/docs/varonis-csv) - imports .csv files.
    * [CSV Asset-Specific Adapters](https://docs.axonius.com/axonius-help-docs/docs/csv-specific-adapters) - have the same functionality as the general CSV adapters, but each adapter is dedicated to a specific asset type.
</Callout>

## Asset Types Fetched

This adapter fetches the following types of assets (other asset types are supported in specific CSV adapters):

* Devices, Users, Aggregated Security Findings, Software, SaaS Applications, Databases, Accounts/Tenants, Business Applications

See the list of [fields imported with a CSV file](https://docs.axonius.com/axonius-help-docs/docs/asset-fields-imported-in-file-based-adapters) for each asset type.

### APIs

When uploading files from Microsoft OneDrive, Axonius uses the [List FIles Shared With Me - OneDrive API - OneDrive dev center](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/api/drive_sharedwithme?view=odsp-graph-online).

### Example CSV File

For an example of a CSV file, download the following zipped file:
([https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Files/CSVExamples.zip](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Files/CSVExamples.zip))

## Connection Parameters

1. **File contains users information**  -  Select  this option to imports the file as a list of users instead of devices.  See the [below section](/docs/csv#which-fields-are-imported-with-a-users-file) for fields required in a **Users Information File**.
2. **File contains installed software information** - Select this option to import  an installed software list instead of devices. See the [below section](/docs/csv#which-fields-are-imported-with-a-software-applications-file) for fields required in a **Software Applications File**.
3. **File contains database information** - Select this option to import the file as a list of databases instead of devices. See the [below section](/docs/csv#which-fields-are-imported-with-a-databases-file) for fields required in a **Databases File**.
4. **File contains accounts information** - Select this option to import the file as a list of accounts instead of devices. See the [below section](/docs/csv#which-fields-are-imported-with-an-accounts-file) for fields required in an **Accounts File**.
5. **File Identifier** *(required)* - Provide a unique name for the adapter connection. The value supplied here is populated in the **File name** field for the data supplied by a specific adapter connection.

<Callout icon="📘" theme="info">
  Note

  The specified File Name is not required to be the actual imported file name. This field is an identifier for use in the Query Wizard.
</Callout>

6. **Select file source** - The CSV adapter supports upload of files from a variety of file sources. The parameters you need to enter change according to the file source that you select. The default is **Upload File**. Refer to [File Sources](/docs/csv#file-sources) for full details.
7. **Encoding** *(optional)* - Specify a specific file encoding or let Axonius decode it. When you enter an encoding type Axonius tries to decode the CSV file based on the specified file encoding type (for example, utf-8) for this connection. Otherwise  Axonius tries to decode the CSV file based on common file encoding types for this connection.

<Callout icon="📘" theme="info">
  Note

  Base64 encoding type is also supported for this adapter.
</Callout>

8. **Ignore illegal characters** - Select this option to ignore illegal characters  during the data import. An illegal character is any character that cannot be translated in the specified file encoding. If you do not select this option, and an illegal character is found, the entire data import fails.
9. **IS GZIP** - Mark whether this file is a compressed GZIP file or not. If it's GZIP, the adapter will unzip the file before parsing it.
10. **Enable PGP Decryption** *(optional, default: disabled)* - Enable this option to decrypt a PGP-encrypted CSV file. When enabled, you need to provide your PGP credentials: **PGP Private Key** and **PGP Private key passphrase** (optional).
11. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
12. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
13. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
14. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
15. **Custom prefix for dynamic fields** *(optional)* - Specify a prefix to be added for dynamic fields. A dynamic field refers to any field that is not part of an asset default field. Adding a prefix to such fields can help you identify them, so that the dynamic field format is `{"CSV"}_{"custom prefix"}_{fieldname}`.
16. **Add CSV prefix for dynamic fields** *(optional, default: enabled)* - When enabled, the `CSV` prefix is added to dynamic fields by default, as demonstrated above. Disable this to remove the `CSV` prefix from dynamic fields, so that the dynamic field format is `{"custom prefix"}_{fieldname}`.

<Callout icon="📘" theme="info">
  Note

  If you do not provide any custom prefix to dynamic fields AND **Add CSV prefix for dynamic fields** is disabled, the dynamic field format is simply `{fieldname}`.
</Callout>

17. **Multi-value fields delimiter** *(optional)* - Specify a delimiter to separate between values within the same field in the imported CSV file.  When you specify a delimiter Axonius considers fields that contain the specified delimiter as multi-value fields. For example, ';'.  Otherwise  Axonius considers all imported fields as single-value fields.
18. **File Type** - Select the type of file uploaded, either CSV, or Excel Spreadsheet. When you select "Excel Spreadsheet", the adapter supports .xls , and.xlsx files, and pulls in the entirety of the first Worksheet as if it were a CSV table. Functionality for tables uploaded from Excel is the same as for CSV files.
19. **Allow empty values** - Select this option to allow the system to support assets with empty fields.  If an asset was created with a field that contained a value, when the CSV file subsequently contains an empty field with the same name, the device or user asset will display that field without a value in it.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![](https://files.readme.io/61b966ef27cc90603fb88d95e3110ad1df34d3b60b7050926d37f1c63eb0bd55-image.png)

### File Sources

The CSV adapter supports upload of files from a variety of file sources. See [File Sources](https://docs.axonius.com/axonius-help-docs/docs/file-sources) for the a detailed list.

![](https://files.readme.io/ec05648a1af9f9364a414a3118a66f5e86f3259c26718ce9aa326fa6c566cc02-image.png)

<Callout icon="📘" theme="info">
  **Note**

  If you are uploading a file from an online storage location and want to use it **only** for custom enrichment, you must disable the **Active connection** setting on the [CSV adapter](https://docs.axonius.com/docs/csv) connection. In this case, the CSV adapter connection will not fetch new assets.

  <Image align="center" border={false} width="350px" src="https://files.readme.io/fb89e658cca2134a3bc2dc3a06c3345edd1d31b16022652271c7c9fdefcbadf8-DisableActiveConnection-cut.png" />
</Callout>

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Set Time Zone** - Set the time zone of date fields fetched with this adapter. Default is **UTC**.
2. **Use fetch time for Last Seen** - Select this option to set that all entities (devices and users) fetched by this adapter have their Last Seen set to the time the entity was fetched (fetch\_time). When you choose this option, the system does not look in   the CSV file for a date and only uses the value set here.
3. **Date Format** - Select the format you want the date to be displayed in. You can choose between "Automatically Identify" (the system will automatically set the format), "DD/MM/YYYY", or “MM/DD/YYYY“.
4. **Additional primary keys for software files** - Enter additional primary keys to use when correlating installed software CSV files. By default, only "hostname" is used as a primary key.  Contact Axonius support before you use this option.
5. **Do not add filename to entity IDs** - By default Axonius adds the filename to the ID of the entities created by the CSV file (device ID, etc). Select this option to not add the filename to the entity ID.
6. **Parse double quotes as escaping** - Some CSV formats use double quotes as escaping for a single " sign. Select this option to explicitly parse double quotes as escaping, to prevent errors that might occur by incorrect dynamic parsing of double quotes.
7. **Force fields to be strings** - Select this option to add names of non-string fields dynamically created by the adapter, and force them to be strings instead of their original field type.
8. **Parse entity fields dynamically** - This setting is enabled by default so that the adapter dynamically parses all of the fields of the entity fetched. Unselect to disable this setting.
9. **Custom Parsing** - see [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>