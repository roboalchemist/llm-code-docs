# Source: https://docs.axonius.com/docs/file-sources.md

# File Sources

File-based adapters such as [CSV](https://docs.axonius.com/axonius-help-docs/docs/csv) and [Custom Files](https://docs.axonius.com/axonius-help-docs/docs/custom-files) support upload of files from a variety of sources. The parameters you need to enter change according to the file source that you select. The default is **Upload File**.

<Image align="center" src="https://files.readme.io/ec05648a1af9f9364a414a3118a66f5e86f3259c26718ce9aa326fa6c566cc02-image.png" />

The file content is determined based on the following order:

1. User assets - If the **File contains users information** parameter is selected
2. Installed Software list - If the **File contains installed software information** parameter is selected
3. Device assets - If none of the options above is selected, the CSV is assumed to be a Device CSV. If a device exists more than once in a CSV file, only the first device found is used.

<Accordion title="Upload File" icon="fa-info-circle">
  Use **Upload File** to import a  local CSV, JSON, or XML. file.

  Under **Upload File** , select a local CSV file to import.

  <Callout icon="📘" theme="info">
    Note

    * When using this option, the data imported from the CSV will never be fetched again, as the file is static.

    * Each adapter that imports files supports a different file type: CSV, JSON, TXT or XML.
  </Callout>
</Accordion>

<Accordion title="Microsoft OneDrive" icon="fa-info-circle">
  Upload a file from Microsoft OneDrive.

  **Note**: When uploading files from Microsoft OneDrive, Axonius uses the [List FIles Shared With Me - OneDrive API - OneDrive dev center](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/api/drive_sharedwithme?view=odsp-graph-online).

  1. **Azure Cloud Environment** *(optional)*  - Select your Microsoft Azure or Microsoft Entra ID (Azure AD) cloud environment type.
  2. **Microsoft OneDrive Tenant ID** *(optional)*  - Microsoft Entra ID (Azure AD)​ ID. Used to authenticate Microsoft OneDrive through Microsoft Entra ID (Azure AD) and use the Graph API.
  3. **Microsoft OneDrive Client ID**   - The Application ID of the Axonius application.
  4. **Microsoft OneDrive Client Secret**, **Microsoft OneDrive OAuth Authorization Code**,  **Microsoft OneDrive Redirect URI**    - Enter these parameters when multi-factor authentication is used in the Azure/Microsoft Office account. To use this option an    OAuth Authorization Code must be created. The OAuth Token/Code Procedure will use the following URL

  <Anchor label="https://login.microsoftonline.com/[[TENANT_ID]]/oauth2/v2.0/authorize?client_id=[[CLIENT_ID]]&scope=https://graph.microsoft.com/.default&response_type=code&redirect_uri=[[REDIRECT_URI]]&response_mode=query" target="_blank" href="https://login.microsoftonline.com/[[TENANT_ID]]/oauth2/v2.0/authorize?client_id=[[CLIENT_ID]]&scope=https://graph.microsoft.com/.default&response_type=code&redirect_uri=[[REDIRECT_URI]]&response_mode=query">[https://login.microsoftonline.com/\[\[TENANT\_ID\]\]/oauth2/v2.0/authorize?client\_id=\[\[CLIENT\_ID\]\]\&scope=https://graph.microsoft.com/.default\&response\_type=code\&redirect\_uri=\[\[REDIRECT\_URI\]\]\&response\_mode=query](https://login.microsoftonline.com/\[\[TENANT_ID]]/oauth2/v2.0/authorize?client_id=\[\[CLIENT_ID]]\&scope=https://graph.microsoft.com/.default\&response_type=code\&redirect_uri=\[\[REDIRECT_URI]]\&response_mode=query)</Anchor>

  5. **Path to resource (URL/Folder path)** *(optional)*

  * If a folder path is supplied:
    * The remaining necessary parameters for Microsoft OneDrive must be provided.
    * The path must be separated by forward slashes.
    * For personal files on Microsoft OneDrive, use the path relative to 'My files'. For example, the folder path for "My files `>` Documents `>` Axonius `>` file.csv" should be Documents/Axonius/file.csv).
    * Use the URL of the file when opened in the browser (recommended). Alternatively, use the Copy Link from the file (this method will work, but, the link will expire and will need to be regularly updated).

  6. **Username for remote resource** and **Password for remote resource**  - Username and password for the remote resource.     You cannot use these parameters when multi-factor authentication is used in the Azure/Microsoft Office account.

  When uploading files from Microsoft OneDrive, and using OAuth authentication the value supplied in [Microsoft OneDrive Client ID](#parameters) must have Files.Read.All delegated permissions in the Azure application in order to to fetch files.

  When uploading files from Microsoft OneDrive, the value supplied in [Username for remote resource (Share/URL)](#parameters) must have Files.Read.All permissions to fetch files.
</Accordion>

<Accordion title="Microsoft Azure" icon="fa-info-circle">
  Upload a file from a container on Azure.

  1. **Azure Storage Container Name** *(required)*  - The name of the container on Azure where the CSV file is located.
  2. **Azure Connection String**   *(required)* - The connection string that includes the authorization information required to access data in the Azure Storage account. You can find the connection string in the Azure portal under Storage Accounts -> \[Account Name] -> Access Keys, where \[Account Name] is the specific storage account that contains the CSV files to be ingested into Axonius. Copy the entire connection string and paste it into this  field.
  3. **Azure Blob Name**  *(required)* - The Azure Blob Name.
</Accordion>

<Accordion title="Microsoft SharePoint" icon="fa-info-circle">
  Upload a file from Microsoft SharePoint.

  **Authentication Method** - Select the authentication method: User Credentials, Client Credentials, Client REST Credentials, or Certificate (PFX).

  * **User Credentials**
    * Enter a **user name** and **password**
    * **Tenant** - Microsoft Entra ID (Azure AD)​ ID. Used to authenticate Microsoft SharePoint through Microsoft Entra ID (Azure AD) and use the Graph API.
    * **Client ID** - The Application ID of the Axonius application.

  * **Client Credentials (For SharePoint API Auth)**
    * Enter a **Client ID** and **Secret**
    * **Tenant** - Microsoft Entra ID (Azure AD)​ ID. Used to authenticate Microsoft SharePoint through Microsoft Entra ID (Azure AD) and use the Graph API.
    * **Domain** - The domain

  * **Client REST Credentials (For Microsoft Graph API Auth)**
    * **Host Name or IP Address**  *(default: graph.microsoft.com)*- The hostname or IP address of the SharePoint server.
    * **Tenant** - Microsoft Entra ID (Azure AD)​ ID. Used to authenticate Microsoft SharePoint through Microsoft Entra ID (Azure AD) and use the Graph API.
    * **Client ID** - The Application ID of the Axonius application.
    * **Client Secret** - Specify a non-expired key, generated from the new client secret.

  * **Certificate (PFX)**
    * **Tenant** - Microsoft Entra ID (Azure AD)​ ID. Used to authenticate Microsoft SharePoint through Microsoft Entra ID (Azure AD) and use the Graph API.
    * **Client ID** - The Application ID of the Axonius application.
    * **PFX Certificate File** and **PFX Password** - Upload a password-protected PFX certificate file and provide the passwoed.

  * **SharePoint Host Name** - Domain/Host Name of the SharePoint site, example: `companyname.sharepoint.com`

  * **SharePoint Site Name** - Name of the SharePoint site the file is located in

  * **SharePoint Folder Path** - Relative path to the file from the Documents location, example: `Documents/Path/To/File`

  * **SharePoint File Name** - example: `axonius_devices.csv`

  Permissions required: Note  The Sharepoint account needs the "Sites.Read.All" permission, either assigned to a user or client application through Entra ID.
</Accordion>

<Accordion title="Microsoft SharePoint On-Premise" icon="fa-info-circle">
  Upload a file from Microsoft SharePoint On-Premise.

  1. **Site URL** - URL of the SharePoint site the file is located in.
  2. **File Path** - Path to the CSV file. Must contain the file name as well.
  3. **Username** - Enter the username in the following format: `DOMAIN\\username`
  4. **Password** - The Username's password.
</Accordion>

<Accordion title="GitHub" icon="fa-info-circle">
  Upload a file from GitHub.

  1. Populate the following parameters: **GitHub - Domain**, **GitHub - Repository**, **GitHub - Branch**.
  2. **GitHub - File Path ("/" separated**) - Path to the CSV file. Must contain the file name as well.
  3. Select one of the following authentication methods:
     1. To authenticate with a **User Name** and **Password**, populate these parameters.
     2. To authenticate with an **Authorization Token**, provide the personal access token that has read access.
     3. To authenticate with the GitHub App, provide the following parameters:
        1. Check **GitHub - Authenticate Using GitHub App**.
        2. **GitHub - App ID** - The GitHub app ID can be found under the GitHub app's page.
        3. **GitHub - App Key File (pem)** - Click **Upload File** to upload the GitHub app's .pem key file. You can download this file from the GitHub app's page.
</Accordion>

<Accordion title="SAP Fieldglass" icon="fa-info-circle">
  Upload a file from SAP Fieldglass.

  1. **SAP Fieldglass Environment URL** - For example, `https://www.fieldglass.net`.
  2. **SAP Fieldglass Client ID** - A valid SAP Fieldglass username.
  3. **SAP Fieldglass Client Secret** - Can be your application password **or** a license key generated from the SAP Fieldglass system.
  4. **SAP Fieldglass Connector Name** - Your custom connector name that you are using to fetch data.
</Accordion>

<Accordion title="Amazon S3 Bucket" icon="fa-info-circle">
  Upload a file from an Amazon S3 Bucket.

  1. **Amazon S3 bucket name** *(required)*  - The name of the S3 bucket from which to fetch the file.
  2. **Amazon S3 object location (key)**  *(required)* - The location within the S3 bucket from where the file can be fetched.
  3. **Amazon S3 Use EC2 Attached Instance Profile**
     * If enabled, Axonius uses the EC2 instance (Axonius installed on) attached IAM role / instance profile.
     * If disabled, Axonius uses the supplied account details in the **AWS Access Key ID** and **AWS Access Key Secret**.
  4. **Amazon S3 Access Key ID** and **Amazon S3 Secret Access Key** *(optional)* - The credentials used to access the S3 object.
  5. **Amazon S3 Region** - The Amazon region on which the S3 bucket is located.
  6. **Amazon S3 Interface VPC Endpoint** - Custom VPC endpoint.
  7. **Amazon S3 directory** *(default: false)* - Select this option to show that the object specified in object location is a directory. Note that the adapter always imports all the files found under the specified location.
  8. **External Role ARN** *(optional; for Axonius-Hosted users only, and for both CloudFormation/Organizations connections)* - Enter your External Role ARN using the following format: `arn:aws:iam::[AWSLaunchAccountID]:role/[AccessName]`.
  9. **Entry Point External ID** *(optional; for Axonius-Hosted users only, and for both CloudFormation/Organizations connections)* - Copy your Customer ID from your Axonius Instance. To find your Customer ID, log into your Axonius instance and navigate to **System Settings** → **About**.
</Accordion>

<Accordion title="Box Platform" icon="fa-info-circle">
  Upload a file from Box Platform.

  1. **Box Platform private key configuration file** *(required)*   - The private key configuration file that provides the Required Permissions to fetch assets. This JSON authentication file must have permission to read/download the specified File ID.  In order to fetch files from Box Platform both of these settings must be configured.
  2. **Box File ID**   *(required)*  - The ID of the Box file. The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL https\://\*.app.box.com/files/123 the file\_id is 123. Refer to [Box Platform documentation](https://developer.box.com/reference/get-files-id/#path-parameters) for more information
</Accordion>

<Accordion title="URL/FTP" icon="fa-info-circle">
  Supply a URL or FTP from which to fetch the file.

  1. **Path to resource (URL)** *(required)* -  Specify the path relative to the configured Webroot or Chroot. This path may differ from the absolute path on the local filesystem.
     * Include the filename with the extension and protocol (ftp, https, http, ftp, ftps, sftp)
     * (Optional) Include the port number if it's non-default (see below)
     * User the following formats:
       * `[protocol]://[address][:port]/path/to/filename.csv`
       * `[protocol]://[address][:port]/filename.xslx`
     * Example: `https://mysite.domain.com/directory1/hostedfile.xslx
       http://192.168.1.1:8080/hostedfile.csv`
     * Default ports:
       * HTTP: 80

       * HTTPS: 443

       * FTP: 21

       * SFTP: 22

       * FTPS: 990

  2. **Username for remote resource** and **Password for remote resource**  - Username and password for the URL. These settings may be required if the "ubuntu" user on the Axonius system does not have access to the  URL. The username and password are used for BASIC authentication of this connection.

  3. **Additional HTTP headers**  *(optional)* - Specify additional information to pass with the HTTP request  (for example `{"Accept": "text/csv"}`).

  4. **Content key in JSON (If returned as JSON)** - When fetching the CSV file via URL, if the URL returns the response as a JSON expression, set this field to the JSON key that represents the actual content of the CSV file. For example, if the URL returns the following JSON expression: `{'content': 'column1,column2\na,b', 'name': 'file.csv'}`, set this fields as "content".
</Accordion>

<Accordion title="SMB Share" icon="fa-info-circle">
  Upload a file from an SMB share path.

  1. **Path to resource (SMB)** *(required)* - Specify an SMB share path where a file can be fetched. This path must include the file name and must start with double-backslashes (`\\`).

  2. **Username for remote resource** and **Password for remote resource** *(optional)* - Username and password for the SMB share. These settings may be required if the "ubuntu" user on the Axonius system does not have access to the SMB share.   The username and password are used for authentication of this connection.

  3. **SMB Version** - Select which SMB version to use. The default is V1.

  4. **Get All Files from Path** - Enable this to download all files from a folder.

  5. **Suppress NetBIOS name lookup**  -  Select this option so that  Axonius does not verify the server's name via NetBios. This option must be enabled in order to use wildcards in SMB file names. When this setting is enabled,  the path must include the server's full NetBIOS name in the following format:
     *`\\<full_server_NetBIOS_name>\path\to\file.ext`*

  * Wildcards are supported in file names as follows:
  * **Suppress NetBIOS name lookup** must be enabled.
  * The asterisk \* wildcard matches any sequence of characters (0 or more, including NULL characters).
  * The **?** wildcard matches a single character (or a NULL at the end of a file name).
  * The matching file names are sorted by file creation time.
  * If multiple files match the wildcard search, the most recently created file is selected.
</Accordion>

<Accordion title="Google Sheets" icon="fa-info-circle">
  You can upload a file that was previously fetched by the [Google Sheets](/docs/google-sheets) adapter.

  1. **Service account JSON credentials** *(required)* - A JSON  Key Pair associated with a service account that has the [Required Permissions](#required-permissions) to fetch assets. Click **Upload** to upload a file containing the binary contents of the keypair file (JSON) generated for the service account credentials.
  2. **Spreadsheet ID**  *(required)* - The Spreadsheet ID (gathered from the link to the spreadsheet)
  3. **Data range (A1 or R1C1 notation)**  *(required)* -  A1 or R1C1 notation of the data range to read. Example: 'My Worksheet'!A1:Z99 to pull cells A1 to Z99 from the worksheet “My Worksheet”. Always use single-quotes when specifying a worksheet that contains spaces in the name. A data range and a worksheet range must be specified  as an absolute path.
</Accordion>