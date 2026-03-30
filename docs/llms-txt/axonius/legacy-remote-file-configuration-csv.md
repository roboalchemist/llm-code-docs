# Source: https://docs.axonius.com/docs/legacy-remote-file-configuration-csv.md

# CSV Legacy Remote File Configuration

This adapter configuration page details the configuration of the following CSV based adapters, using the Legacy CSV Remote File Configuration.
For full details about configuration of the CSV and JSON adapters refer to the [CSV](/docs/csv) adapter.

<Callout icon="📘" theme="info">
  Note

  * It is possible to configure the **CSV** based adapters to fetch files from various storage places including: Microsoft OneDrive, Azure, and Amazon S3.

  * The **CSV** adapter parameters and functionality are common to all adapters that import files.:

  * [**CSV - Applications**](/docs/applications-csv)

  * [**CSV - DNS Records**](/docs/dns-records-csv)

  * [**CSV-Expenses**](/docs/expenses-csv)

  * [**CSV-Licenses**](/docs/licenses-csv)

  * **[CSV - Networks](https://docs.axonius.com/axonius-help-docs/docs/networks-csv)**

  * **[CSV - Networks Services](https://docs.axonius.com/axonius-help-docs/docs/csv-networks-services)**

  * **[CSV - Software Inventory](https://docs.axonius.com/axonius-help-docs/docs/software-inventory-csv)**

  * **[CSV - URLs](https://docs.axonius.com/axonius-help-docs/docs/urls-csv)**

  * **[F-Secure Policy Manager](/docs/f-secure-policy-manager)** - imports .csv files.

  * [**Forcepoint Web Security Endpoint CSV File**](/docs/forcepoint-web-security-endpoint) - imports .csv files.

  * **[L0phtCrack 7](/docs/l0phtcrack-7)** - imports .csv files.

  * **[Masscan](/docs/masscan)** - imports .json files.

  * **[Nmap Security Scanner](/docs/nmap-security-scanner)** - imports .xml files.

  * [**SQLite**](/docs/sqlite) - imports device information from an SQLite database.

  * **[Tenable Nessus CSV File](/docs/tenable-nessus-csv-file)** - imports .csv files.

  * [**Varonis CSV**](/docs/varonis-csv) - imports .csv files.
</Callout>

## Parameters

1. **File contains users information**
   * Selecting this option imports the file as a list of users instead of devices.
   * See the [below section](/docs/csv#which-fields-will-be-imported-with-a-users-file) for fields required in a **Users Information File**.
2. **File contains installed software information**
   * Selecting this option imports an installed software list instead of devices.
   * See the [below section](/docs/csv#which-fields-will-be-imported-with-a-software-applications-file) for fields required in a **Software Applications File**.
3. **File name** *(required)* - A unique name for the adapter connection. The value supplied here is populated in the **File name** field for the data supplied by a specific adapter connection.

<Callout icon="📘" theme="info">
  Note

  The specified File Name is not required to be the actual imported file name. This field is an identifier for use in the Query Wizard.
</Callout>

4. **Upload file** *(optional)* - Select a local CSV file to import.

<Callout icon="📘" theme="info">
  Note

  * When using this option, the data imported from the CSV will never be fetched again, as the file is static.

  * Each adapter that imports files supports a different file type: CSV, JSON, or XML.
</Callout>

10. **Path to resource (SMB/URL/Folder path)** *(optional)* - Specify an SMB share path, HTTP(S) URL, FTP URL, or folder path where a file can be fetched for this connection.

<Callout icon="📘" theme="info">
  **Note**

  If you are uploading a file from an online storage location and want to use it **only** for custom enrichment, you must disable the **Active connection** setting on the [CSV adapter](https://docs.axonius.com/docs/csv) connection. In this case, the CSV adapter connection will not fetch new assets.

  <Image align="center" border={false} width="350px" src="https://files.readme.io/fb89e658cca2134a3bc2dc3a06c3345edd1d31b16022652271c7c9fdefcbadf8-DisableActiveConnection-cut.png" />
</Callout>

* This path must include the file name.
* If an SMB share path is supplied:
  * The path must start with double-backslashes (`\\`).
  * If **Suppress NetBIOS name lookup** is enabled,  the path must include the server's full NetBIOS name in the following format:
    *`\<full_server_NetBIOS_name>\path\to\file.ext`*
  * Wildcards are supported in file names.
  * **Suppress NetBIOS name lookup** must be enabled.
  * The asterisk \* wildcard matches any sequence of characters (0 or more, including NULL characters).
  * The **?** wildcard matches a single character (or a NULL at the end of a file name).
  * The matching file names are sorted by file creation time.
  * If multiple files match the wildcard search, the most recently created file is selected.
* If an HTTP(S) URL is supplied:
  * The endpoint must support the HTTP GET method.
  * All URLs must start with HTTP:// or with HTTPS://
* If an FTP URL is supplied, all URLs must start with FTP:// or with SFTP:// or with FTPS://
  * The default port for each method is as follows:
    * FTP: 21
    * SFTP: 22
    * FTPS: 990
  * A custom port can be specified in the supplied path, for example: *ftps\://my.host.in.axonius.com:21/path/to/file.ext*
* If a folder path is supplied:
  * The remaining necessary parameters for Microsoft OneDrive must be provided.
  * The path must be separated by forward slashes.
  * For personal files on Microsoft OneDrive, use the path relative to 'My files'. For example, the folder path for "My files `>` Documents `>` Axonius `>` file.csv" should be Documents/Axonius/file.csv).
  * Use the URL of the file when opened in the browser (recommended). Alternatively, use the Copy Link from the file (this method will work, but, the link will expire and will need to be regularly updated)

6. **Username for online resource (Share/URL)** and **Password for online resource (Share/URL)** *(optional)* - Username and password for the SMB share, URL, or folder path. These settings may be required if the "ubuntu" user on the Axonius system does not have access to the SMB share / URL / folder path.
   * If supplied for an SMB or folder path, the username and password are used for authentication of this connection.
   * If supplied for a URL, the username and password are used for BASIC authentication of this connection.

<Callout icon="📘" theme="info">
  Note

  When you configure the CSV adapter to fetch CSV files from Microsoft OneDrive,  you are required to supply **File name**, **Path to resource (SMB/URL/Folder path)**, **Username for online resource (Share/URL)**, and **Password for online resource (Share/URL)**, as well as the following three fields **Microsoft OneDrive Tenant ID**, **Microsoft OneDrive Client ID**, and **Azure Cloud Environment**. When  multi-factor authentication is used in the Azure/Microsoft Office account  **Username for online resource (Share/URL)**, and **Password for online resource (Share/URL)** may not be used.
</Callout>

7. **Microsoft OneDrive Tenant ID** *(optional)*  - Microsoft Entra ID (Azure AD) ID. Used to authenticate Microsoft OneDrive through Microsoft Entra ID (Azure AD) and use the Graph API.
8. **Microsoft OneDrive Client ID** *(optional)*  - The Application ID of the Axonius application.
9. **Azure Cloud Environment** *(optional)*  - Select your Microsoft Azure or Microsoft Entra ID (Azure AD) cloud environment type.

<Callout icon="📘" theme="info">
  Note

  When you configure the CSV adapter to fetch a file from Azure,  you are required to supply **File name**, as well as the following three fields **Azure Storage Container Name**, **Azure Connection String**, and **Azure Blob Name**.
</Callout>

10. **Azure Storage Container Name** *(optional)*  - The name of the container on Azure where the CSV file is located.

11. **Azure Connection String** *(optional)*  - The connection string that includes the authorization information required to access data in the Azure Storage account. You can find the connection string in the Azure portal under Storage Accounts -> \[Account Name] -> Access Keys, where \[Account Name] is the specific storage account that contains the CSV files to be ingested into Axonius. Copy the entire connection string and paste it into this  field.

12. **Azure Blob Name** *(optional)* - The Azure Blob Name.

13. **Amazon S3 bucket name** *(optional)* - The name of the S3 bucket to fetch the file.

14. **Amazon S3 object location** *(optional)* - The location within the S3 bucket where the file can be fetched.

15. **Amazon S3 Use EC2 Attached Instance Profile**
    * If enabled, Axonius uses the EC2 instance (Axonius installed on) attached IAM role / instance profile.
    * If disabled, Axonius uses the supplied account details in the **AWS Access Key ID** and **AWS Access Key Secret**.

16. **Amazon S3 Access Key ID** and **Amazon S3 Secret Access Key** *(optional)* - The credentials used to access the S3 object.

17. **External Role ARN** *(optional; for Axonius-Hosted users only, and for both CloudFormation/Organizations connections)* - Enter your External Role ARN using the following format: `arn:aws:iam::[AWSLaunchAccountID]:role/[AccessName]`.

18. **Entry Point External ID** *(optional; for Axonius-Hosted users only, and for both CloudFormation/Organizations connections)* - Copy your Customer ID from your Axonius Instance. To find your Customer ID, log into your Axonius instance and navigate to **System Settings** → **About**.

19. **Box Platform private key configuration file** *(optional)* - The private key configuration file that provides the Required Permissions to fetch assets. This JSON authentication file must have permission to read/download the specified File ID.  In order to fetch files from Box Platform both of these settings must be configured.

20. **Box File ID**  *(optional)*  - The ID of the Box file. The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL https\://\*.app.box.com/files/123 the file\_id is 123. Refer to [Box Platform documentation](https://developer.box.com/reference/get-files-id/#path-parameters) for more information

21. **Encoding** *(optional)*  - Specify a specific file encoding or let Axonius encode it.
    * If supplied, Axonius tries to encode the CSV file based on the specified file encoding type (for example, utf-8) for this connection.
    * If not supplied, Axonius tries to encode the CSV file based on common file encoding types for this connection.

22. **Ignore illegal characters** - Select whether illegal characters are ignored during the data import. An illegal character is any character that cannot be translated in the specified file encoding.
    * If enabled, Axonius ignores illegal characters and omits those from the imported data.
    * If disabled, if an illegal character is found, the entire data import fails.

23. **Verify SSL** - If an HTTP(S) URL is specified, verify the SSL certificate offered by the host supplied in the **Path to Resource (SMB/URL/Folder path)** field. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#/ssl-trust--ca-settings) .

24. **HTTP proxy** *(optional)* - A proxy to use when connecting to the HTTP(S) URL specified in **Path to Resource (SMB/URL/Folder path)**.

25. **HTTPS proxy** *(optional)* - A proxy to use when connecting to the HTTP(S) URL specified in **Path to Resource (SMB/URL/Folder path)**.

26. **Additional HTTP headers** *(optional)* - Specify additional information to pass with the HTTP request.
    * If supplied, Axonius passes additional information with the HTTP request (for example, `{"Accept": "text/csv"}`) for this connection.
    * If not supplied, Axonius does not pass additional information with the HTTP request for this connection.

27. **Suppress NetBIOS name lookup**  - Applicable only for files fetched from SMB share.
    * If enabled and the file is fetched from SMB share, Axonius does not verify the server's name via NetBios for this connection. This option must be enabled in order to use wildcards in SMB file names.
    * If disabled and if  the file is fetched from SMB share, Axonius verifies the server's name via NetBios for this connection.

28. **Custom prefix for dynamic fields** *(optional)* - Specify a prefix to be added for dynamic fields. A dynamic field refers to any field that is not part of an asset default field.
    * If supplied, Axonius adds the specified prefix for any dynamic field. This can assist you in identifying such fields.
    * If not supplied, Axonius does not add any prefix for any dynamic field.

29. **Multi-value fields delimiter** *(optional)* - Specify a delimiter to separate between values within the same field in the imported CSV file.
    * If supplied, Axonius considers fields that contain the specified delimiter as multi-value fields. For example, ';'.
    * If not supplied, Axonius considers all imported fields as single-value fields.

30. **File Type** - Select the type of file uploaded, either CSV, or Excel Spreadsheet. When you select "Excel Spreadsheet", the adapter supports .xls , and.xlsx files, and pulls in the entirety of the first Worksheet as if it were a CSV table. Functionality for tables uploaded from Excel is the same as for CSV files.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CSV adapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CSV%20adapter.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Set Time Zone** - Set the time zone of date fields fetched with this adapter. Default is **UTC**.
* **Use fetch time for Last Seen** - Select this option to set that all entities (devices and users) fetched by this adapter have their Last Seen set to the time the entity was fetched (fetch\_time).

## APIs

When uploading files from Microsoft OneDrive, Axonius uses the [List FIles Shared With Me - OneDrive API - OneDrive dev center](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/api/drive_sharedwithme?view=odsp-graph-online).

## Required Permissions

When uploading files from Microsoft OneDrive, and using OAuth authentication the value supplied in [Microsoft OneDrive Client ID](#parameters) must have Files.Read.All delegated permissions in the Azure application in order to to fetch files.

When uploading files from Microsoft OneDrive, the value supplied in [Username for online resource (Share/URL)](#parameters) must have Files.Read.All permissions to fetch files.

## If multiple file options are added to a 'file-based' adapter, what file is imported?

If multiple import file import types are provided in the CSV adapter (or for other file-based adapter), they are imported in the following order:

1. Path to resource (SMB/URL/Folder path)
2. Amazon S3 Bucket
3. Uploaded file

The file content is determined based on the following order:

1. User assets - If **File contains users information** is selected
2. Installed software list - If **File contains installed software information** field is enabled.
3. Device assets - If none of the options above is selected, the CSV is assumed to be a device CSV.  If a device exists more than once in a CSV file, only the first device found is used.

## Which fields are required for each Import Type?

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Import Type
      </th>

      <th>
        \*KEY fields
      </th>

      <th>
        Optional fields
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        From a File
      </td>

      <td>
        * File name
        * Upload file
      </td>

      <td>
        * File contains users information
        * File contains installed software information
        * Encoding
        * Ignore illegal characters
        * Custom prefix for dynamic fields
        * Multi-value fields delimiter
        * Connection Label
      </td>
    </tr>

    <tr>
      <td>
        From an HTTP(S) URL
      </td>

      <td>
        * File name
        * Path to resource (SMB/URL/Folder path)
        * Verify SSL
        * Choose Instance (on multi-node Axonius environment)
      </td>

      <td>
        * File contains users information
        * File contains installed software information
        * Username for online resource (Share/URL)
        * Password for online resource (Share/URL)
        * Encoding - HTTP proxy - HTTP proxy
        * HTTPS proxy
        * Additional HTTP headers
        * Ignore illegal characters
        * Custom prefix for dynamic fields
        * Multi-value fields delimiter
        * Connection Label
      </td>
    </tr>

    <tr>
      <td>
        From an FTP URL
      </td>

      <td>
        * File name
        * Path to resource (SMB/URL/Folder path)
        * Choose Instance (on multi-node Axonius environment)
      </td>

      <td>
        * File contains users information
        * File contains installed software information
        * Username for online resource (Share/URL)
        * Password for online resource (Share/URL)
        * Encoding
        * Ignore illegal characters
        * Custom prefix for dynamic fields
        * Multi-value fields delimiter
        * Connection Label
      </td>
    </tr>

    <tr>
      <td>
        From a file share
      </td>

      <td>
        * File name
        * Path to resource (SMB/URL/Folder path)
        * Choose Instance (on multi-node Axonius environment)
        * Suppress NetBIOS name lookup
      </td>

      <td>
        * File contains users information
        * File contains installed software information
        * Username for online resource (Share/URL)
        * Password for online resource (Share/URL)
        * Encoding- Ignore illegal characters
        * Custom prefix for dynamic fields
        * Multi-value fields delimiter
        * Connection Label
      </td>
    </tr>

    <tr>
      <td>
        From Microsoft OneDrive
      </td>

      <td>
        * File name
        * Path to resource (SMB/URL/Folder path)
        * Choose Instance (on multi-node Axonius environment)
      </td>

      <td>
        * File contains users information
        * File contains installed software information
        * Username for online resource (Share/URL)
        * Password for online resource (Share/URL)
        * Microsoft OneDrive Tenant ID
        * Microsoft OneDrive Client ID
        * Azure Cloud Environment
        * Encoding- Ignore illegal characters
        * Custom prefix for dynamic fields
        * Multi-value fields delimiter
        * Connection Label
      </td>
    </tr>

    <tr>
      <td>
        From an Amazon S3 Bucket
      </td>

      <td>
        * File name
        * Amazon S3 bucket name
        * Amazon S3 object location (key)
      </td>

      <td>
        * File contains users information
        * File contains installed software information
        * Amazon S3 Access Key ID
        * Amazon S3 Secret Access Key
        * Encoding- Ignore illegal characters
        * Custom prefix for dynamic fields
        * Multi-value fields delimiter
        * Connection Label
      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="📘" theme="info">
  Note

  Based on the order of operations, any fields that are specified and not applicable to the import type are ignored. For example, filling in the **Amazon S3 bucket name** field while the **Path to resource (SMB/URL/Folder path)** is populated causes the **Path to resource (SMB/URL/Folder path)** property to be ignored *but not removed.*
</Callout>

## Which fields are imported with a devices file?

The following data is imported as common data fields while any other data in the CSV/JSON/XML is exclusively be Adapter Specific data.

<Callout icon="📘" theme="info">
  Note

  Fields marked as \***KEY** indicate that you need to include at least one of these fields as part of the imported CSV file.  More \***KEY** fields available in the CSV file help provide stronger correlation.
</Callout>

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        UI Field Name
      </th>

      <th>
        Accepted CSV Field Name(s)
      </th>

      <th>
        Notes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Architecture
      </td>

      <td>
        architecture
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Asset Name
      </td>

      <td>
        name\
        vmname\
        displayname\
        assetname\
        machinename\
        instancename\
        samaccountname\
        endpointname
      </td>

      <td>
        If no hostname is configured, the Asset Name value is used for the Host Name.
      </td>
    </tr>

    <tr>
      <td>
        Device Manufacturer Serial
      </td>

      <td>
        serial\
        serialnumber\
        sn\
        hostserialnumber\
        deviceserialnumber\
        serial#\
        endpointserialnumber
      </td>

      <td>
        \***KEY**
      </td>
    </tr>

    <tr>
      <td>
        Device Manufacturer
      </td>

      <td>
        manufacturer\
        devicemanufacturer
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Device Model
      </td>

      <td>
        model\
        modelid\
        endpointmodel
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Domain
      </td>

      <td>
        domain\
        domainname\
        endpointdomain
      </td>

      <td>
        If this value is not specified AND the device is specified in DOMAIN\Name format, Axonius replaces the Domain value with the parsed out DOMAIN.
      </td>
    </tr>

    <tr>
      <td>
        Host Name
      </td>

      <td>
        hostname\
        host\
        fqdn\
        fullyqualifieddomainname\
        compname\
        computername\
        servername\
        dnsname\
        hosthostname\
        endpointfqdn
      </td>

      <td>
        \***KEY** -  If the device is specified in DOMAIN\Name, Axonius parses the DOMAIN value out. If the CSV field is set to "unknown", Axonius sets the Host Name to blank.
      </td>
    </tr>

    <tr>
      <td>
        ID
      </td>

      <td>
        id\
        identifier\
        serialnumber\
        assetid\
        resourceid
      </td>

      <td>
        \***KEY** - The ID field is a combination of the "CSV File Name" value and the specified field names.
      </td>
    </tr>

    <tr>
      <td>
        IPs
      </td>

      <td>
        ipaddresstext\
        ip\
        ipaddress\
        ipaddresses,\
        ips\
        primaryip\
        endpointipaddress\
        ipaddresstext\
        registerip\
        sourceip\
        managementip\
        privateip\
        allips\
        lastip\
        address\
        ipaddresslist\
        ipaddri\
        ipaddrs\
        ipaddr\
        localip\
        privateipaddresses
      </td>

      <td>
        This field accepts a comma separated set of IP addresses.
      </td>
    </tr>

    <tr>
      <td>
        Last Seen
      </td>

      <td>
        lastmessagetime\
        lastdiscoveredtime\
        lastseen
      </td>

      <td>
        If this value is not specified, enter the time that the CSV was last imported.
      </td>
    </tr>

    <tr>
      <td>
        Last Used Users
      </td>

      <td>
        username
      </td>

      <td>
        This appends to the existing Last Used Users list if the device already exists.
      </td>
    </tr>

    <tr>
      <td>
        MAC
      </td>

      <td>
        mac\
        macaddress\
        macaddresses\
        macs
      </td>

      <td>
        \***KEY** - This field accepts a comma separated set of MAC addresses.
      </td>
    </tr>

    <tr>
      <td>
        Network Interfaces
      </td>

      <td>
        networkinterfaces
      </td>

      <td>
        Axonius attempts to parse IP address(es), MAC address(es), and network interface cards from this field.
      </td>
    </tr>

    <tr>
      <td>
        OS (see Notes)
      </td>

      <td>
        os\
        osname\
        osversion\
        operatingsystem\
        osmode\
        uname\
        endpointos
      </td>

      <td>
        This field is parsed out into multiple properties within the OS field. Not all OSes are parsed properly. Please reach out to Axonius if an OS is not parsing as expected.
      </td>
    </tr>

    <tr>
      <td>
        OS: Kernel Version
      </td>

      <td>
        kernel\
        kernelversion
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Software Name
      </td>

      <td>
        packages
      </td>

      <td>
        This is delimited by spaces.
      </td>
    </tr>
  </tbody>
</Table>

## Which fields are imported with a users file?

The following data is imported as common data fields while any other data in the CSV/JSON is exclusively Adapter Specific data.

<Callout icon="📘" theme="info">
  Note

  Fields marked as \***KEY** indicate that you need to include at least one of these fields as part of the imported CSV file.  More \***KEY** fields available in the CSV file help provide stronger correlation.
</Callout>

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        UI Field Name
      </th>

      <th>
        Accepted CSV Field Name(s)
      </th>

      <th>
        Notes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Domain
      </td>

      <td>
        domain\
        domainname\
        endpointdomain
      </td>

      <td />
    </tr>

    <tr>
      <td>
        First Name
      </td>

      <td>
        firstname\
        givenname
      </td>

      <td />
    </tr>

    <tr>
      <td>
        ID
      </td>

      <td>
        id\
        identifier\
        serialnumber\
        assetid\
        resourceid
      </td>

      <td>
        \***KEY** - The ID field is a combination of the "CSV File Name" value and the specified field names.
      </td>
    </tr>

    <tr>
      <td>
        Last Name
      </td>

      <td>
        lastname\
        surname\
        sn
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Mail
      </td>

      <td>
        mail\
        email\
        usermail\
        mailaddress\
        email address\
        emailprimarywork
      </td>

      <td>
        \***KEY**
      </td>
    </tr>

    <tr>
      <td>
        Name
      </td>

      <td>
        name\
        vmname\
        displayname\
        assetname\
        machinename\
        instancename\
        samaccountname\
        endpointname
      </td>

      <td>
        \***KEY**
      </td>
    </tr>

    <tr>
      <td>
        User Name
      </td>

      <td>
        username
      </td>

      <td>
        \***KEY**
      </td>
    </tr>
  </tbody>
</Table>

## Which fields are imported with a software applications file?

The following data is imported as common data fields while any other data in the CSV/JSON is exclusively Adapter Specific data.
In order for vulnerabilities (Aggregated Security Findings) to be parsed from the CSV adapter, the MINIMUM requirements are:

* The adapter is configured with "File contains installed software"
* The file has at least the following headers:
  * Hostname (or any of the headers supported as hostname)
  * Software Name (header must be present, though may be empty on a row)
  * CVE ID

The other headers (or data in a row for those headers) are optional for the purposes of parsing vulnerabilities

<Callout icon="📘" theme="info">
  Note

  Fields marked as \***KEY** indicate that you need to include at least one of these fields as part of the imported CSV file.  More \***KEY** fields available in the CSV file help provide stronger correlation.
</Callout>

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        UI Field Name
      </th>

      <th>
        Accepted CSV Field Name(s)
      </th>

      <th>
        Notes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Host Name
      </td>

      <td>
        hostname\
        host\
        fqdn\
        fullyqualifieddomainname\
        compname\
        computername\
        servername\
        dnsname\
        hosthostname\
        endpointfqdn
      </td>

      <td>
        \***KEY** - This field is required as the software list is imported to each individual device.

        If a file contains installed software information, the adapter will also add data to the **Security Finding Instances** table, for rows that contain a CVE ID column, in addition to parsing the installed software.
      </td>
    </tr>

    <tr>
      <td>
        Software Name
      </td>

      <td>
        softwarename\
        swname
      </td>

      <td>
        \***KEY** this field is required in order to parse installed software.  This field may be left empty on a row with CVE ID.
      </td>
    </tr>

    <tr>
      <td>
        Software Path
      </td>

      <td>
        softwarepath\
        swpath
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Software Vendor
      </td>

      <td>
        softwarevendor\
        swvendor
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Software Version
      </td>

      <td>
        softwareversion\
        swversion
      </td>

      <td />
    </tr>

    <tr>
      <td>
        CVE ID
      </td>

      <td>
        cve\
        cveid\
        cvelist\
        grypecve
      </td>

      <td>
        If present, a row featuring a CVE ID is parsed as Security Finding Instances in addition to installed software.
      </td>
    </tr>

    <tr>
      <td>
        CVE Description
      </td>

      <td>
        cvedescription
      </td>

      <td>
        This field will be ignored if CVE ID is empty or not present.
      </td>
    </tr>

    <tr>
      <td>
        CVE Severity
      </td>

      <td>
        cveseverity
      </td>

      <td>
        CVE Severity needs to be one of the values listed here. An invalid CVE Severity value is ignored.   This field will be ignored if CVE ID is empty or not present. 'NONE', 'LOW', 'MEDIUM', 'MODERATE', 'SEVERE', 'SERIOUS', 'HIGH', 'CRITICAL', 'URGENT', 'INFO', 'UNTRIAGED', 'NEGLIGIBLE'
      </td>
    </tr>

    <tr>
      <td>
        CVE Status
      </td>

      <td>
        cvestatus
      </td>

      <td>
        CVE Status needs to be one of the values listed here. An invalid CVE Status value is ignored.   This field will be ignored if CVE ID is empty or not present. 'open', 'closed', 'reopen', 'expired', 'done', 'valid', 'obsolete', 'pending'
      </td>
    </tr>
  </tbody>
</Table>

## Example CSV File

For an example of a CSV file, download the following zipped csv:

([https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CSVExamples.zip](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CSVExamples.zip))