# Source: https://docs.axonius.com/docs/custom-files.md

# Custom Files

The **Custom Files** adapter imports CSV, JSON, TXT and XML files with inventory information from the asset types listed.

## Asset Types Fetched

* Devices, Aggregated Security Findings, Users, Software, Application Extensions, Admin Managed Extensions, User Initiated Extensions, Application Add-Ons, Application Extension Instances, Admin Managed Extension Instances, User Initiated Extension Instances, Application Add-On Instances, Application Keys, SaaS Applications, Networks, Containers, Alerts/Incidents, Databases, Network Services, Certificates

See the list of [fields imported with a custom file](https://docs.axonius.com/axonius-help-docs/docs/asset-fields-imported-in-file-based-adapters) for each asset type.

## Example Files

**CSV file**

[Software\_Test.csv](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Files/software_test.csv)

**JSON file**

[Test.json](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Files/test.json)

**TXT file**

```
hostname=server01 ip=192.168.1.10 os="Windows Server 2019" status=active mac=00:1A:2B:3C:4D:5E serial=SRV001
hostname=server02 ip=192.168.1.11 os="Ubuntu 22.04 LTS" status=active mac=00:1A:2B:3C:4D:5F serial=SRV002
hostname=workstation01 ip=192.168.1.50 os="Windows 11 Pro" status=active mac=00:1A:2B:3C:4D:60 serial=WKS001
hostname=laptop01 ip=192.168.1.100 os="macOS Ventura" status=inactive mac=00:1A:2B:3C:4D:61 serial=LPT001
hostname=db-primary ip=10.0.0.5 os="Red Hat Enterprise Linux 9" status=active mac=00:1A:2B:3C:4D:62 serial=DB001
hostname=web-proxy ip=10.0.0.10 os="Debian 12" status=active mac=00:1A:2B:3C:4D:63 serial=PRX001
```

## Connection Parameters

1. **File Type** *(required)* - Select CSV, JSON, XML, or TXT.
   1. When selecting TXT, a field titled **Field Separator** appears. This field defines the character that separates the `key=value` pairs in each line of the TXT file.\
      **Explanation about the TXT file format:** This file type parses files containing `key=value` pairs. Each line in the file represents one asset, with multiple fields separated by a delimiter defined in **Field Separator**.  Values containing spaces must be wrapped in double quotes
      `key1=value1<separator>key2=value2<separator>key3="value with spaces"`
2. **File Contents** *(required)* - Select the file contents according to the required Asset Type. If you select Devices, a **File Contains Software info** checkbox appears. Select this option to import an installed software list instead of devices. See [Which fields are imported with a software applications file?](/docs/custom-files#which-fields-are-imported-with-a-software-applications-file) for more information.
3. **File Identifier** *(required)* - Provide a unique name for the adapter connection. The value supplied here is populated in the File Name field for the data supplied by a specific adapter connection.
4. **Select file source** - The Custom Files adapter supports upload of files from a variety of file sources. The parameters you need to enter change according to the file source that you select. The default is **Upload File**. See [File Sources](/docs/custom-files#file-sources) for more information.
5. **Encoding** - Specify a specific file encoding or let Axonius decode it. When you enter an encoding type Axonius tries to decode the CSV file based on the specified file encoding type (for example, utf-8) for this connection. Otherwise Axonius tries to decode the CSV file based on common file encoding types for this connection.
6. **Ignore illegal characters** - Select this option to ignore illegal characters during the data import. An illegal character is any character that cannot be translated in the specified file encoding. If you do not select this option, and an illegal character is found, the entire data import fails.
7. **Is GZIP** - Mark whether this file is a compressed GZIP file or not. If it's GZIP, the adapter will unzip the file before parsing it.
8. **Enable PGP Decryption** *(optional, default: disabled)* - Enable this option to decrypt a PGP-encrypted CSV file. When enabled, you need to provide your PGP credentials: **PGP Private Key** and **PGP Private key passphrase** (optional).
9. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
10. **HTTP Proxy** - A proxy to use when connecting to an HTTP(S) URL specified in Select file source.
11. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![](https://files.readme.io/00a6f63830f3ee8cbe18a2667a6f042c973435c90768e20a16da240ac257f517-image.png)

### File Sources

The CSV adapter supports upload of files from a variety of file sources. See [File Sources](https://docs.axonius.com/axonius-help-docs/docs/file-sources) for a detailed list.

![](https://files.readme.io/5a8c999891c31f6cc80a14a8bcfa7f659885f446d902d70f592a0bee5784c65c-image.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. See [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Parse entity fields dynamically** - Selected by default. When selected, the adapter will parse all fields in the file and add a custom prefix.
2. **Set Time Zone** - Set the time zone of date fields fetched with this adapter. Default is UTC.
3. **Custom Parsing** - See [Adapter Custom Parsing](/docs/adapter-custom-parsing).

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Supported From Version

Supported from Axonius version 6.1.

<br />