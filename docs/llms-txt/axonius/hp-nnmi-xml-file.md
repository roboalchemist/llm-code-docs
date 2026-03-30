# Source: https://docs.axonius.com/docs/hp-nnmi-xml-file.md

# HP NNMi XML File

HP Network Node Manager i (NNMi) is a network health and performance monitoring software with scalability and device support.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **File name** *(required)* - Specify a unique NNMi XML file name for the adapter connection.

2. **Upload file** *(optional)* - Click **Choose file** to manually upload the XML file.

3. **Path to resource (SMB/URL)** *(optional, default: empty)* - Specify the path to the resource. Specify an SMB share path, a HTTP(S) URL or an FTP URL where a file can be fetched for this connection.

   * This path must include the file name.

   * If an SMB share path is supplied:

   * The path must start with double-backslashes ("\\").

   * If **Suppress NetBIOS name lookup** is enabled, the path must include the server's full NetBIOS name (in the following format: \\

   *\path\to\file.ext)*.

   * If a HTTP(S) URL is supplied:
   * The endpoint must support the HTTP GET method.
   * All URLs must start with HTTP:// or with HTTPS://.
   * If an FTP URL is supplied, all URLs must start with FTP:// or with SFTP:// or with FTPS://
     * The default port for each method is as follows:
       * FTP: 21
       * SFTP: 22
       * FTPS: 990
     * A custom port can be specified in the supplied path, for example: *ftps\://my.host.in.axonius.com:21/path/to/file.ext*

4. **User name for online resource (Share/URL)** *(required, default: empty)* - The credentials for a user account that has the required permissions to fetch assets.

5. **Password for online resource (Share/URL)** *(required, default: empty)* - The user's password. The password must not include ";".

6. **Azure Storage Container Name** *(optional)* - Specify the name of the Azure storage container that you want to fetch. If no name is specified, all Azure storage containers are fetched.

7. **Azure Connection String** *(optional)* - Specify the name of the Azure connection.

8. **Azure Blob Name** *(optional, default: empty)* - Specify the URI of the Azure blob.

9. **Amazon S3 bucket name** *(optional, default: empty)* - Specify the name of the S3 bucket to fetch the file.

10. **Amazon S3 object location (key)** *(optional, default: empty)* - Specify the location to pull a file from Amazon.

11. **Amazon S3 Use EC2 Attached Instance Profile** *(optional, default: false)* -
    * If selected, Axonius will use the EC2 instance (Axonius installed on) attached IAM role / instance profile.
    * If cleared, Axonius will use the supplied account details in the **AWS Access Key ID** and **AWS Access Key Secret**.

12. **Amazon S3 Access Key ID** *(optional)* - Specify the access key ID to access the file provided in the Amazon S3 object location, if it is access-controlled.

13. **Amazon S3 Secret Access Key** *(optional)* - Specify the Amazon S3 secret access key. To obtain a secret access key, see [Security Access Key](https://aws.amazon.com/blogs/security/wheres-my-secret-access-key/).

14. **Encoding** *(optional, default: utf-8)* - Specify a specific file encoding or let Axonius encode it.
    * If supplied, Axonius will attempt to encode the CSV file based on the specified the file encoding type (for example, utf-8) for this connection.
    * If not supplied, Axonius will attempt to encode the CSV file based on common file encoding types for this connection.

15. **Ignore illegal characters** *(optional, default: false)* - Select whether to ignore illegal characters during the data import. An illegal character is any character that cannot be translated in the specified file encoding.
    * If selected, Axonius will ignore illegal characters and will omit those from the imported data.

    * If cleared, if an illegal character is found, the entire data import will fail.

16. **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

17. **HTTP Proxy** *(optional, default: empty)* - Connect the adapter to a HTTP proxy instead of directly connecting it to the domain.

18. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a HTTPS proxy instead of directly connecting it to the domain.

19. **Additional HTTP headers** *(optional)* - Add HTTP headers for the GET request associated with the **Path to IPs XML resource (SMB/URL)**, if a URL is specified.

20. **Suppress NetBIOS name lookup** *(optional, default: false)* - Select to suppress the NetBIOS name lookup.

21. **Upload IPs XML file** *(optional)* - Select an IPs XML file to upload by clicking **Choose file**.

22. **Path to IPs XML resource (SMB/URL)** *(optional)* - Specify the path to the IPs XML resource.

23. **Upload subnets XML file** *(optional)* - Select a subnets XML file to upload by clicking **Choose file**.

24. **Path to interfaces XML resource (SMB/URL)** *(optional)* - Specify the path to the interfaces XML resource.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="HP_NNMi_XML_File2" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HP_NNMi_XML_File2.png" />

## Required Permissions

The value supplied in [User Name](#parameters) must have permissions to fetch assets.

The value supplied in [API Key](#parameters) must be associated with credentials that have permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5