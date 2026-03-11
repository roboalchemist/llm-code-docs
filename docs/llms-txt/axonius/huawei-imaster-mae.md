# Source: https://docs.axonius.com/docs/huawei-imaster-mae.md

# Huawei iMaster MAE

Huawei iMaster MAE is a platform that provides automated operations and maintenance, monitoring, and optimization for 5G and mobile broadband networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **File name** - Provide a unique name for the adapter connection. The value supplied here is populated in the **File name** field for the data supplied by a specific adapter connection. It is **not** required to be the actual imported file name. This field is an identifier to be used in the Query Wizard.

2. **Select file source** - The Huawei iMaster MAE adapter supports upload of files from a variety of file sources. The parameters you need to enter change according to the file source that you select. Refer to the [CSV File Sources section](/docs/csv#file-sources) for a detailed explanation on each source.

3. **Encoding** *(optional)* - Specify a specific file encoding or let Axonius decode it. When you enter an encoding type Axonius tries to decode the XML file based on the specified file encoding type (for example, utf-8) for this connection. Otherwise Axonius tries to decode the XML file based on common file encoding types for this connection.

<Callout icon="📘" theme="info">
  Note

  Base64 encoding type is also supported for this adapter.
</Callout>

3. **XML File List** *(required)* - Select XML file names from the list to parse from a destination folder. This is relevant to remote file options but not to a single local file upload.

4. **Ignore illegal characters** - Select this option to ignore illegal characters  during the data import. An illegal character is any character that cannot be translated in the specified file encoding. If you do not select this option, and an illegal character is found, the entire data import fails.

5. **PGP Decryption** *(optional, default: disabled)* - Enable this option to decrypt a PGP-encrypted file. When enabled, you need to provide your PGP credentials: PGP Private Key and PGP Private key passphrase (optional).

6. **IS GZIP** - Mark whether this file is a compressed GZIP file or not. If it's GZIP, the adapter will unzip the file before parsing it.

7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

8. **HTTP Proxy** and **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![huawei](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-ROQJ1D4H.png)

## Supported From Version

Supported from Axonius version 6.1.32.1