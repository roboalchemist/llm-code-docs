# Source: https://docs.axonius.com/docs/bind-dns-adapter.md

# BIND

BIND is a DNS server software that provides domain name resolution and management services.

The BIND adapter enables Axonius to fetch and catalog DNS records, providing visibility into hostname resolution and network infrastructure.

## Asset Types Fetched

* Devices

## Before You Begin

### Required Permissions

* DNS Zone Transfer must be allowed in your environment.
* You must have SSH:OS file permissions to the Zone file.
* In Remote File connection, you must have permission to access the relevant file.

### Supported from Version

Supported from Axonius version 6.1.53.

## Connecting the Adapter in Axonius

1. **Connection Type** *(required)* - Select between:
   * **DNS Zone Transfer** - DNS Settings are displayed.
   * **Retrieve Zone File** - Remote File Settings are displayed.
   * **Remote File Records-Only Settings** - Remote File Settings are displayed.

### DNS Settings

2. **Domain Name** *(required)* - Enter the hostname or IP address of the BIND server that Axonius can communicate with.
3. **Name Server IP Address** *(optional)* - Enter the specific IP address of the DNS server you want to query.

<Image align="center" alt="Bind DNS options" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/BIND_Name_Server_IP_Address.png" className="border" />

*DNS Settings in DNS Zone Transfer*

### Remote File/Remote File Records-Only Settings

3. **File name** *(required)* - Specify a unique remote file name for the adapter connection.
4. **Select file source** *(required)* - The BIND adapter supports upload of files from a variety of file sources (like in the CSV adapter). The parameters you need to enter change according to the file source that you select. The default is **Upload File**. Refer to [File Sources](/docs/csv#file-sources) for full details.

<Callout icon="📘" theme="info">
  Note about Amazon S3 Bucket

  When selecting Amazon S3 Bucket as the File Source, the parameters are the same as those detailed in [File Sources](/docs/csv#file-sources), in addition to the following parameters:

  * **Contains place-holder** *(default: disabled)* - Enable this if the above Amazon S3 bucket field contains a place holder (pattern) you'd like to replace with one of the available calculated values. When enabled, the following parameters need to be provided:

  * **Place-holder** - Specify the pattern you want to replace. The value can be any valid regular expression.

  * **Replacement options** -  Select which calculated value you'd like to replace your specified pattern with. Currently the only option is **Today's Date**. When this option is selected, the following parameter needs to be provided:

  * **Date format string** - Specify the date format you'd like to use. See more details under [Format Codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).
</Callout>

5. **Upload file** *(required)* - Click **Upload File** to manually upload the remote file.
6. **Encoding** *(optional)* - Specify a specific file encoding or let Axonius encode it.
7. **Ignore illegal characters** - Select this option to ignore illegal characters during the data import. An illegal character is any character that cannot be translated in the specified file encoding. If you do not select this option, and an illegal character is found, the entire data import fails.
8. **PGP Decryption** - *(optional, default: disabled)* - Enable this option to decrypt a PGP-encrypted CSV file. When enabled, you need to provide your PGP credentials: **PGP Private Key** (required) and **PGP Private key passphrase** (optional).
9. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
10. **HTTP Proxy** *(optional)* - Enter an HTTP proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.
11. **HTTPS Proxy** *(optional)* - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Bind_Remote" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-TB88HLE3.png" className="border" />

*Remote File Settings in Retrieve Zone File*

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

* **Global Endpoints Config** -
  * **Record Types to ingest as Devices** - Select the specific DNS record types (such as `A, AAAA,` or `CNAME`; default: `A, AAAA,`) that you want Axonius to ingest as device assets. It is then recommended to exclude record types such as `TXT`, `NS`, `PTR`, and `DNAME`, as these typically do not represent valid device assets.