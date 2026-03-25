# Source: https://docs.axonius.com/docs/qualys-certificate-view-csv.md

# Qualys Certificate View CSV

Qualys Certificate View CSV is a certificate management solution that provides discovery, monitoring, and lifecycle management of digital certificates across distributed environments.

<Callout icon="📘" theme="info">
  Note

  The adapter requires a CSV from Qualys to have the following columns:

  * Name
  * Issuer
  * Issuer Organization
  * Expiration
  * Algorithm
  * Key Size
  * Last Found
  * Instances
  * Assets
  * Extended Validation
  * Sources
  * Type
</Callout>

<br />

### Asset Types Fetched

* Certificates

#### Supported From Version

Supported from Axonius version 7.0.12.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **File Identifier** - Provide a unique name for the adapter connection. The value supplied here is populated in the **File name** field for the data supplied by a specific adapter connection.

<Callout icon="📘" theme="info">
  Note

  The specified File Name is not required to be the actual imported file name. This field is an identifier for use in the Query Wizard.
</Callout>

2. **Select file source** - The Qualys Certificate View CSV adapter supports upload of files from a variety of file sources. The parameters you need to enter change according to the file source that you select. The default is **Upload File**. Refer to [File Sources](/docs/csv#file-sources) for full details.

<Image alt="Qualys Certificate View CSV connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/QualysCertificateViewCSV_AddConnection.png" />

<br />

### Optional Parameters

1. **Encoding** - Specify a specific file encoding or let Axonius decode it. When you enter an encoding type Axonius tries to decode the CSV file based on the specified file encoding type (for example, utf-8) for this connection. Otherwise Axonius tries to decode the CSV file based on common file encoding types for this connection.

   <Callout icon="📘" theme="info">
     Note

     Base64 encoding type is also supported for this adapter.
   </Callout>

2. **Ignore illegal characters** - Select this option to ignore illegal characters  during the data import. An illegal character is any character that cannot be translated in the specified file encoding. If you do not select this option, and an illegal character is found, the entire data import fails.

3. **IS GZIP** - Mark whether this file is a compressed GZIP file or not. If it's GZIP, the adapter will unzip the file before parsing it.

4. **Enable PGP Decryption** *(default: disabled)* - Enable this option to decrypt a PGP-encrypted CSV file. When enabled, you need to provide your PGP credentials: **PGP Private Key** and **PGP Private key passphrase** (optional).

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).