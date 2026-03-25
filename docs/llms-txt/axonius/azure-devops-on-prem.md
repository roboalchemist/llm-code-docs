# Source: https://docs.axonius.com/docs/azure-devops-on-prem.md

# Azure DevOps (On-Prem)

Azure DevOps (On-Prem) is a Microsoft product that provides version control, reporting, requirements management, project management, automated builds, testing and release management capabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Groups

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Azure DevOps server.
2. **Port** *(optional)* - If not supplied, Axonius will use TCP port 443.
3. **API Version** - Select the API version. The default is 7.0-preview.
4. **Organization** *(required)* - The organization name defined in the customer’s DevOps account.
5. **Token Name** *(required)* - The name of the token you want to use.
6. **Personal Access Token** *(required)* - The personal access token to access the Azure Devops. Refer to [Use personal access tokens](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=preview-page).
7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
8. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the value supplied in **Organization**.
9. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Organization** via the value supplied in **HTTPS Proxy**.
10. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Organization** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Azure DevOps On-Prem](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Azure%20DevOps%20On-Prem.png)

## APIs

Axonius uses the [Azure DevOps Server 2022 API](https://learn.microsoft.com/en-us/rest/api/azure/devops/core/teams/get-team-members-with-extended-properties?view=azure-devops-server-rest-7.0\&tabs=HTTP).

## Required Permissions

The value supplied in [Personal Access Token](#parameters) must be associated with credentials that have read permissions (for Code) in order to fetch assets.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                      | Supported | Notes |
| ---------------------------- | --------- | ----- |
| Azure DevOps Server 2022 API | Yes       |       |