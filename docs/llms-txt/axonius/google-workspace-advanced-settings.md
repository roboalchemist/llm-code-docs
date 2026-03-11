# Source: https://docs.axonius.com/docs/google-workspace-advanced-settings.md

# Google Workspace Advanced Settings

## Accessing Advanced Configuration

1. Navigate to **Adapters** and search for `Google Workspace (G Suite)`, then click the adapter tile.
2. In the left menu, select **Advanced Configuration** under **Advanced Settings**.

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

## Google Workspace - Advanced Settings

In Advanced Settings, at the top of the Advanced Configuration, you can choose asset types that are relevant to specific advanced configurations.

1. From the dropdown, select one or more asset types.

<Image align="left" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Advanced%20Settings%20Asset%20Type%20Dropdown(1).png" />

2. The relevant advanced configurations are displayed.
3. Next to certain configurations, you can find a small ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Tooltip%20icon\(1\).png) icon. Hover over the icon to see more information.
4. The Advanced Configuration page is divided into sections, which can be collapsed to make it easier to navigate.

### Data Enrichment

1. **Fetch MDM devices** *(default: true)* – Select this option to fetch mobile devices and Chrome OS devices from Google Workspace. Fetching MDM devices requires additional OAuth scopes. See [Advanced Permissions](/docs/google-workspace-advanced-permissions).
2. **Fetch Applications** - Select this option to fetch application information from Android devices as "Installed Software"
3. **Fetch user groups** - Select this option to fetch user group memberships for each user from Google Workspace. This setting requires additional OAuth scopes and Google Cloud APIs. See [Advanced Permissions](/docs/google-workspace-advanced-permissions).
4. **Enrich Groups Settings** - Select this option to fetch group permissions (capabilities) and enrich them as dynamic group fields. Enriching group settings requires additional OAuth scopes and enabling the required Google Cloud APIs. See [Advanced Permissions](/docs/google-workspace-advanced-permissions).
5. **Fetch user roles** - Select this option to fetch user role assignments from Google Workspace. Fetching user roles requires additional OAuth scopes. See [Advanced Permissions](/docs/google-workspace-advanced-permissions).
6. **Fetch Cloud Identity Device Users** - Fetch users associated with Cloud Identity devices. This is very time consuming and will make minimum two API calls per device.
7. **Fetch Disk Usage -** Select this option to fetch the amount of disk storage space used by each Google account.
   Fetching disk usage requires additional OAuth scopes and enabling the required Google Cloud APIs.
   See [Advanced Permissions](/docs/google-workspace-advanced-permissions).
8. **Fetch extensions** - Select to fetch instances of Google granting access permissions to other SaaS or native applications.
9. **Fetch Licenses -** Select to fetch Google licenses in your organization.
10. **Fetch Settings (Policies)** - Select to fetch settings configured for the Google accounts in your organization.

<Callout icon="📘" theme="info">
  Note:

  Fetching settings requires additional OAuth scopes and enabling the required Google Cloud APIs.
  See [Advanced Permissions](/docs/google-workspace-advanced-permissions).
</Callout>

11. **Fetch User Audit Logs** - Select to fetch Google audit logs from the past 90 days.

<Callout icon="📘" theme="info">
  Note:

  Fetching user audit logs requires additional OAuth scopes.
  See [Advanced Permissions](/docs/google-workspace-advanced-permissions).
</Callout>

### Fetch and Parse

1. **Cloud Identity prefer device with recent last seen if duplicated asset name** - Select this option to save the device with the most recent Last Seen date under that asset name, when multiple instances of the same asset name are fetched from Cloud Identify.
2. **Ignore Cloud Identity devices without serial** - Select this option to ignore devices coming from Cloud Identity without Serial Numbers.
3. **Do not fetch disabled User** - Select this option to exclude disabled user accounts from the fetch.
4. **When Possible - Use Annotation ID as Asset Name** - Populate the asset name with the value of the Annotation ID (when the value exists) instead of using the value in the Name field.
5. **Use Hostname as Asset Name for Cloud Identity Devices** - Select this option to use the host name as the asset name, when the host name exists.

### Advanced Configuration

1. **Enrich User Browser Policies from Groups** - Select this option to fetch groups’ browser policies and parse them to the relevant users and groups.
   Fetching browser policies requires additional OAuth scopes and enabling the required Google Cloud APIs. See [Advanced Permissions](/docs/google-workspace-advanced-permissions).
2. **Enrich Extensions last access days** - Select this option to limit the amount of extensions that the adapter fetches and the amount of parallel requests performed by the adapter to fetch extensions.
3. **Fetch Extensions last access from the past X days** - Enter the number of days to fetch extensions for. For example, if you enter ‘3’ the adapter fetches all extensions accessed in the past three days.
4. **Max workers to get audit logs** - Enter the maximum number of parallel requests (workers) to allow for fetching extensions. Note: Fetching extensions requires adding the following scope to your Google Workspace (G Suite) admin account: For more information, see [Advanced Permissions](/docs/google-workspace-advanced-permissions).
5. **Enrich users last activity from the selected events** - Select the user events to be fetched for the ’Last Access’ field.

## Axonius SaaS Applications Best Practices

* To fetch Axonius SaaS Applications set the following:
  * Enrich Groups settings
  * Fetch user roles
  * Fetch User Audit Logs
* The following will get partial data unless entering username/password :
  * Fetch extensions
  * Fetch Licenses
  * Fetch Settings (Policies)

In addition, in the adapter connection - **Get OAuth Apps** should be turned on.