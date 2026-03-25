# Source: https://docs.axonius.com/docs/endor-labs.md

# Endor Labs

Endor Labs is a platform that provides software supply chain security and management solutions.

### Asset Types Fetched

* Vulnerabilities, SaaS Applications, Application Resources

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key/Secret

### APIs

Axonius uses the following APIs:

* [ListProjects](https://docs.endorlabs.com/api/#tag/ProjectService/operation/ProjectService_ListProjects)
* [GetFinding](https://docs.endorlabs.com/api/#tag/FindingService/operation/FindingService_GetFinding)

### Permissions

To fetch findings from the Endor Labs API, the API token used must belong to a service account or user with the appropriate access scopes.

**Required Permissions**:

| Permission/Role                 | Description                                                                                          |
| ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `FINDING_VIEWER`                | Grants read-only access to all findings (SAST, SCA, Secrets)                                         |
| `ORG_VIEWER` or `TENANT_VIEWER` | *(Optional)* Grants cross-namespace visibility, if applicable                                        |
| `REPO_VIEWER`, `PACKAGE_VIEWER` | *(Optional)* Required to resolve parent asset relationships (e.g. RepositoryVersion, PackageVersion) |

**Built-In Roles with Findings Access**:

* Security Analyst
* Platform Engineer (in orgs focused on dependency/package scans)
* Any custom role with `Findings:Read` permissions

**Where to Verify**:

You can verify or assign these permissions in the Endor Labs Console:

Settings → Access Management → Service Accounts

Select the token in use and check its assigned roles or scopes.

#### Supported From Version

Supported from Axonius version 6.1.74

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Endor Labs server.
2. **API Key** and **Secret** - The API Key and API Secret for an account that has the Required Permissions to fetch assets. For information on how to authenticate, see [Authentication](https://docs.endorlabs.com/rest-api/authentication/).
3. **Namespace** - A way to organize organizational units into virtual groupings of resources. Namespaces must be a fully qualified name. For example, the child namespace of the namespace "endor.prod" called "app" is called "endor.prod.app".

![Endor Labs.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Endor%20Labs.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).