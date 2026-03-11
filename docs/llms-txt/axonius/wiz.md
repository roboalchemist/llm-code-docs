# Source: https://docs.axonius.com/docs/wiz.md

# Wiz

<Callout icon="❗️" theme="error">
  Customers using a Custom Wiz Service Account to connect Axonius to Wiz should migrate to using the Wiz Axonius integration Service Account ([see below](#configuring-the-wiz-axonius-integration) ). The integration is vetted by both companies and ensures a proper support and escalation mechanism. Contact Axonius support if you have any question.
</Callout>

Wiz analyzes all layers of the cloud stack to identify high-risk attack vectors to be prioritized and fixed.

## Asset Types Fetched

This adapter fetches the following types of assets:

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Vulnerabilities.svg) Vulnerabilities | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Domains_URLs.svg) Domains & URLs | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Compute_Services.svg) Compute Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Services.svg) Application Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Networks.svg) Networks | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Load_Balancers.svg) Load Balancers | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Databases.svg) Databases | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Containers.svg) Containers | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Object_Storage.svg) Object Storage | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Network_Services.svg) Network Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/File_Systems.svg) File Systems | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Accounts_Tenants.svg) Accounts/Tenants | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Serverless_Functions.svg) Serverless Functions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Disks.svg) Disks | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Compute_Image.svg) Compute Images | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Secrets.svg) Secrets | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Certificates.svg) Certificates | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg) Alerts/Incidents | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Permissions.svg) Permissions

## Before You Begin

### Supported From Version

Supported from Axonius version 4.4

### APIs

Axonius uses the <Anchor label="Wiz API" target="_blank" href="https://docs.wiz.io/docs/wiz-api-introduction">Wiz API</Anchor>.

### Required Ports:

* **TCP port 443**

### Required Permissions

The Wiz Axonius integration is required for this adapter deployment. The appropriate permissions will be set automatically by the integration, which is vetted and tested by both Axonius and Wiz.

<Callout icon="📘" theme="info">
  Note:

  Users are able to see the permissions set in the integration's Service Account prior to creating the integration.
</Callout>

## Configuring the Wiz Axonius Integration

1. In Wiz, go to **Settings** > **Deployments** > **Integration** and click **+ Add Deployment**.
2. Under the required category or by using the search bar, type Axonius.
3. On the **New Axonius Integration** page:

   1. For **Name**, enter a meaningful name, for example: **Axonius Integration**.
   2. For Scope, narrow the scope of this integration to a specific project.
      1. ***IF*** you select a specific project, make sure to gather it's Project ID for later use (**Settings** > **Projects**).
   3. Review the permissions required for the service account that is used for this integration.

   <br />

   <Image align="center" width="400px" src="https://files.readme.io/b36c1a47886b1479f5818319f4e73ab45a448285894784e8c4ba37a1204d7287-Wiz_Integration1.png" />

   <br />
4. Click **Add Integration**.
5. A new service account is created.
   Under **New Service Account Credentials**, *copy and save* the following to a local file or secure location for the next step:

   1. Client ID
   2. Client Secret
   3. API Endpoint URL (Example: `https://api.us48.app.wiz.io/graphql`)
   4. Authentication URL (Example: `https://auth.app.wiz.io/oauth/token`)

   <Image align="center" width="400px" src="https://files.readme.io/d2c5239fb6d0e1eb032075ae3b2d172637b96c09fa6a8a8cc53f7c26f8e86013-Wiz_Integration2.png" />

## Deploying the Wiz Adapter in Axonius

1. Navigate to the Adapters page, search for `Wiz`, and click on the adapter tile.
2. Click **Add Connection**.

### Required Parameters

1. **API Endpoint URL** - The API Endpoint URL of the Wiz server that Axonius can communicate with via the [Required Ports](#required-ports). Use the `API Endpoint URL` that you previously copied.
2. **Authentication URL** - Enter the URL of the Authentication service used for the Wiz application. Use the `Authentication URL` that you previously copied.

<Callout icon="📘" theme="info">
  **Notes**

  * Confirm that the public IP address of your Axonius instance is added to the "Source IP address" configuration within the Wiz application.

  * If you are filtering outbound traffic from your Axonius instance, verify that you have both the API Endpoint URL and the Authentication URL as allowed destinations.
</Callout>

3. **Client Key** and **Client Secret** - Input the Key and Secret from the Axonius Integration Service Account. Use the `Client ID` and `Client Secret` that you previously copied.

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/wiz_parameters.png)

### Optional Parameters

1. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
2. **Project ID Mapping** *(Legacy Only, unavailable for new connections)* - Leave empty if migrating from custom service account to Wiz Axonius integration service account.
3. **Project UUID** - Enter the Project UUID you scoped the Integration Service Account with or use an asterisk `*` to retrieve all projects.
4. **Use legacy connection** *(Legacy Only)* - uncheck if migrating from custom service account to Wiz Axonius integration service account.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

<Accordion title="Expand/Collapse" icon="fa-info-circle">
  1. **Asset types to fetch** *(default:`VIRTUAL_MACHINE`)* - Select one or more types of assets to fetch.

  2. **Do not fetch devices where Power State is Turned Off** - When selected, devices with a power state 'off' are not fetched by Axonius.

  3. **Fetch cloud configuration findings** - Select this option to enrich assets with cloud configuration findings.

  4. **Cloud configuration findings severity to fetch** *(default:`CRITICAL` ,`HIGH`)* - Select one or more severity levels from this drop-down to filter cloud configuration findings.

  5. **Cloud configuration findings status to fetch** *(default:`OPEN` ,`IN PROGRESS`)* - Select one or more status values from this drop-down to filter cloud configuration findings.

  6. **Fetch issues** - Select this option to fetch issues and enrich assets with corresponding data.

  7. **Fetch issues evidence (non-legacy)** - Select this option to fetch issues evidence data. (not available for legacy connections).

  8. **Fetch issue source rules** - Select this option to fetch issue source rules data. This includes data for Controls as well as other sources for Issues, such as Cloud Configuration Rules and Cloud Event Rules.

  9. **Issues severity to fetch** *(default:`CRITICAL`, `HIGH`, `MEDIUM`)* - Select one or more severity levels to filter issues that are fetched.

  10. **Issues status to fetch** *(default:`OPEN`, `IN_PROGRESS`)* - Select one or more statuses to filter issues that are fetched.

  11. **Fetch Installed Software** - Select this option to fetch installed software information and enrich assets with corresponding data.

  12. **Filter installed software older than X days** *(optional, default: 8)* - Select whether to enrich installed software data for installed software older than the provided number of days. If you enter 0, no filtering will occur.

  13. **Fetch vulnerability findings** - Select this option to fetch vulnerability information and enrich assets with corresponding data.

  14. **Vulnerability status to fetch** *(default:`OPEN`, `REJECTED`, `RESOLVED`)*- Select one or more vulnerability statuses to be fetched.

  15. **Ignore rejected and resolved vulnerabilities older than** *(optional, default: 14)* - Set a number of days for  the adapter to ignore rejected and resolved vulnerabilities older than the set number of days.

  16. **Parse vulnerability findings description (warning: heavy field)** - Select this option to parse the vulnerability description field.

  17. **Vulnerability findings detection method to fetch** - Select detection methods to filter vulnerability findings that are fetched. If empty all methods will be fetched.

  18. **Vulnerability findings severity to fetch** *(default:`CRITICAL`, `HIGH`, `MEDIUM`)* - Select one or more severity levels of vulnerability findings to filter findings that are fetched. Select 'NONE' to filter all severity levels.

  19. **Fetch network exposures** - Select this option to fetch network exposures and enrich assets with corresponding data.

  20. **Enrich assets with Stateful set** - Select this option to enrich assets with information on their Kubernetes cluster type.

  21. **Enrich assets with Service Usage Technology** - Select this option to enrich subscriptions with service usage tech information.

  22. **Enrich assets with Authentication Configuration** - Select this option to fetch authentication configuration information and enrich assets with corresponding data.

  23. **Enrich assets with Access Role Binding** - Select this option to fetch access role binding information and enrich assets with corresponding data.

  24. **Enrich assets with Data Findings** - Enable this option to enrich the following assets with data findings: Databases, Database Server, Bucket, Serverless Functions, Virtual Machines, File System Services.
      * **Data Findings severity to fetch** - Select the severities to filter data findings that are fetched. If empty all severities will be fetched.

  25. **Attach volumes to associated VMs** *(default: True)* - Select this option to attach cloud storage volumes to their associated VMs. When not selected, each volume is created as a separate device.

  26. **Attach network interfaces to associated assets** *(default: True)* - This setting attaches network interfaces to their associated assets. When not selected, each network interface is created as a separate device.

  27. **Fetch subscription tags** - Select this option to fetch Subscription Tags. When this setting is selected, the adapter creates dynamic `subscription_tag` fields and parses the tags into the regular `subscription_tags` list.

  28. **List of tags to parse as fields**  - Specify a comma-separated list of tag keys to be parsed as device fields. Each tag is a key-value pair that is part of the **Adapter Tags** complex field.

  29. **Fetch Wiz users** - Select this option to fetch Wiz users (Wiz platform user accounts).

  30. **Fetch cloud user assets** - Select this option to fetch cloud user assets discovered by Wiz.

  31. **Cloud user asset types to fetch** *(default:`SERVICE_ACCOUNT`, `USER_ACCOUNT`)* - Select one or more user types to fetch.

  32. **Parse Wiz vulnerability findings to a separate field** - Wiz vulnerability findings are parsed by default into the Vulnerable Software field. Selecting this option will also parse them into a field named Vulnerability Findings.

  33. **Fetch compute images as devices** - Select this option to parse compute images as both Compute Images and Devices asset types. When this setting is unselected, the SNAPSHOT asset type is only parsed as Compute Images.

  <Callout icon="📘" theme="info">
    Note

    To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
  </Callout>
</Accordion>

## Related Enforcement Actions

[Wiz - Add Tags to Assets](/docs/add-tags-to-assets-in-wiz)

[Wiz - Update Issues](https://docs.axonius.com/axonius-help-docs/docs/update-wiz-issues)