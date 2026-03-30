# Source: https://docs.axonius.com/docs/run-windows-shell-command.md

# Axonius - Deploy Files and Run Shell Command on Windows Assets

**Axonius - Deploy Files and Run Shell Command on Windows Assets** deploys an optional list of selected files and runs a command line on each of the Windows devices which are the results of the query.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Active Directory adapter** - Select this option to use the first connected Microsoft Active Directory (AD) adapter credentials.

## Required Fields

These fields are required to run the Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  Even if you just want to deploy a file, you need to fill in the **Command** and **Command name** fields.
</Callout>

* **Command** - Specify the command you want to run on the Windows device. Add a condition to the command to print the result into the **Command Name** field. For example, *"wmic computersystem get name"* or just *"echo"*.

* **Command name** - Specify the field name to be added to the device. If you set the **Command** field, then you must add a value to this field. This new field will be populated if a condition has been added in the command field.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **User name** and **Password** - Provide credentials to connect and to execute the command on the Windows device: user name and password.
</Callout>

* **DNS Servers** - Specify a comma-separated list of DNS servers to be used to resolve the hostnames in the saved query supplied as a trigger (or devices that have been selected in the asset table).
  * If supplied, Axonius will use the specified DNS server to resolve the devices' hostnames. For each asset, the first response will be the one to be used.
  * If not supplied or if no response has been received from any of the specified DNS servers, the default DNS server will be used.
* **Use NBNS** - Use the NetBIOS Name Service protocol.
* **Max timeout for the created process** - Set the maximum time (in seconds) for the created shell process to run before it is terminated.
* **Reset timer for each request in seconds** - Set the maximum time for each WQL query to return a response.
* **Files to deploy** - To deploy files on the device, use the following controls to upload one or more files:
  * *Choose file* - to choose a file to upload.
  * *+* - to upload an additional file.
  * *x* - to remove an uploaded file.

<Callout icon="📘" theme="info">
  Note:

  The uploaded files are deployed to the *`c:\windows\axonius`* folder. When uploaded, if a file with the same name already exists, it is overridden by the new uploaded file. Uploaded files are not automatically deleted.
</Callout>

* **Path to Remote Files** - Enter the path to the remote files to deploy. Remote services can be: FTP, SFTP, SMB, or URL.
* **Suppress NetBIOS name lookup** - Do not use the NetBIOS name lookup.
* **Additional HTTP headers** - Enter any additional HTTP headers.
* **HTTP proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **Replace command variables with Axonius fields** - You can use Axonius fields as values in command parameters in place of variables. For example, by creating a mapped field named "MY\_FIELD", you can insert it into the command by adding the string `{AXONIUS_ATTRIBUTE:MY_FIELD}`, using the keyword *AXONIUS\_ATTRIBUTE*, where you want this value to be inserted. Each field must be enclosed in curly brackets to mark the beginning and end of the field name.

  For example, the field *TOKEN* is used in the following command:

```

CsUninstallTool.exe MAINTENANCE_TOKEN={AXONIUS_ATTRIBUTE:TOKEN} /quiet

```

See [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping) for more information.

<Image alt="REplaceCommandWithAxoniusField.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/REplaceCommandWithAxoniusField.png" />

* **Files Directory** - Specify the directory to which the files uploaded by the Enforcement Action will be deployed.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Ports

The following ports should be opened:

* 135 RPC
* 445 SMB
* Random port in the range: 1024–65535

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).