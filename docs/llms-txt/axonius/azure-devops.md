# Source: https://docs.axonius.com/docs/azure-devops.md

# Azure DevOps

Azure DevOps is a Microsoft product that provides version control, reporting, requirements management, project management, automated builds, testing and release management capabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Activities
* Application Resources

## Parameters

To connect the adapter, you can either authenticate with a personal access token **or** with a service principal.
Refer to [Required Permissions](/docs/azure-devops#required-permissions) for the permissions relevant to each authentication method.

### Authenticating with a Personal Access Token

The following parameters are required:

1. **Organization** - The organization name defined in the customer’s DevOps account.
2. **Token Name** - The name of the token you want to use.
3. **Personal Access Token** - The personal access token to access the Azure Devops. Refer to [Use personal access tokens](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=preview-page).

### Authenticating with a Service Principal

The following parameters are required.

<Callout icon="📘" theme="info">
  Note

  The following parameters can be configured only in the Azure portal, and not in the Azure DevOps portal. Refer to the [ Microsoft Entra ID adapter documentation](/docs/microsoft-azure-active-directory-ad#create-an-application-key) for a detailed guide on how to configure these.
</Callout>

1. **Organization** - The organization name defined in the customer’s DevOps account.
2. **Azure Client ID** -The Application ID of the Axonius application.
3. **Azure Client Secret** - Specify a non-expired key generated from the new client secret.
4. **Azure Tenant ID** - The ID for Microsoft Entra ID.
5. **Cloud Environment** - Select your Microsoft Azure or Microsoft Entra ID cloud environment type.

For additional information, refer to [Use service principals & managed identities in Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/service-principal-managed-identity?view=azure-devops).

### Additional Parameters

These parameters are optional and can be added to any authentication method.

1. **Domain or IP** - The hostname or IP address of the Azure DevOps server. The default is [https://vssps.dev.azure.com/](https://vssps.dev.azure.com/).
2. **Port** - If not supplied, Axonius will use TCP port 443.
3. **API Version** - Select the API version. The default is 6.1-preview\.1.4.
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the value supplied in **Organization**.
6. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Organization** via the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Organization** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="AzureDevOPsConnection" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-05D4DVBQ.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Groups of Each User** - Select this option to fetch memberships of users in groups.
2. **Fetch Git Repositories** - Select this option to fetch the Git Repositories from the projects in Azure DevOps.
3. **Fetch Git Commits from the last X days** *(optional)* - Use the arrows on the right to set the day count.
4. **Fetch Users Projects** - Select this option to fetch all projects of all users. The results can be viewed under **Assets**`>`**Users**`>` **Projects** field (add it to the table if it is not there). You can also go to a user\`s profile and view the **Projects** field of that specific user.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Azure DevOps Services REST API 6.1](https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/users/list?view=azure-devops-rest-6.1).

## Required Permissions

* The values supplied in [Token Name and Personal Access Token](/docs/azure-devops#authenticating-with-a-personal-access-token) refer to a generated personal access token (PAT) used to authenticate into Azure DevOps that has permission to read, write and manage work items. For details, see [ Azure DevOps - Create a personal access token (PAT)](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=preview-page#create-a-pat).
* The values supplied in [Azure Client ID, Azure Client Secret, Azure Tenant ID and Cloud Environment](/docs/azure-devops#authenticating-with-a-service-principal) must have permission to read, write and manage work items. For details, see [Add a service principal to an Azure DevOps organization](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/service-principal-managed-identity?view=azure-devops).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                             | Supported | Notes |
| ----------------------------------- | --------- | ----- |
| Azure DevOps Services REST API 6.1. | Yes       |       |

### Related Enforcement Actions

* [Microsoft Azure DevOps - Create Task](/docs/create-azure-devops-task)
* [Microsoft Azure DevOps - Update Task](/docs/update-azure-devops-task)