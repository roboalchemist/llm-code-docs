# Source: https://docs.axonius.com/docs/box-platform-create-update-user.md

# Box - Create/Update User

**Box - Create/Update User** creates or updates Box Platform users for assets returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **Box Platform private key configuration file** - The private key configuration file that provides the [Required Permissions](#required-permissions) to fetch assets.
* **Action** - Select the action to perform.
* **Use Adapter connection** - Enter the ID of the adapter connection this action should use.
* **Initial Request Body** - Enter the initial request body in JSON format.
* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.
  <br />

## APIs

Axonius uses the following BOX APIs:

* [Create user - API Reference - Box Developer Documentation](https://developer.box.com/reference/post-users/)
* [Update user - API Reference - Box Developer Documentation](https://developer.box.com/reference/put-users-id/)
* [Upload file](https://developer.box.com/reference/post-files-content/) - for file size up to 20MB.
* [Create upload session](https://developer.box.com/reference/post-files-upload-sessions/) - for file size over 20MB.

## Required Permissions

The value supplied in [**Box Platform private key configuration file**](/docs/send-csv-to-box#additional-fields) refers to the generated private key configuration file for your Custom App using JWT authentication:

1. **Set up a Custom App** - Set up a Custom App using JWT authentication. For details, see [Box Guides - Setup with JWT](https://developer.box.com/guides/applications/custom-apps/jwt-setup/).
2. **Create Box Platform private key configuration file** - After a Custom App has been created to use JWT authentication, there is an option available in the Developer Console to have Box create a configuration file. This file will include the keypair as well as a number of other application details that are used during authentication.

   1. Click on the "Configuration" option from the left sidebar in your application and scroll down to the "Add and Manage Public Keys" section.

   <Image align="center" alt="image.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(728).png" />

   2. Click the "Generate a Public/Private Keypair" button to have Box generate a keypair. This will trigger the download of a JSON configuration file that you can move to your application code.
   3. Upload this file as the **Box Platform private key configuration file**.
3. **Application Scopes** - The configured app must have the following application scopes:
   * Read all files and folders stored in Box
   * Read and write all files and folders stored in Box