# Source: https://docs.axonius.com/docs/snyk.md

# Snyk

Snyk is a developer security platform integrating directly into development tools, workflows, and automation pipelines.

### Asset Types Fetched

* Devices, Users, Aggregated Security Findings, SaaS Applications, Application Resources

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### APIs

Axonius uses the [Snyk API](https://snyk.docs.apiary.io/#).

You must have a Snyk Business or Enterprise plan to access the API. For more information, see [Snyk API documentation](https://docs.snyk.io/snyk-api-info).

### Permissions

The value supplied in [API Token](#required-parameters) must be associated with credentials that have Group Viewer (when using Group ID) permissions or Organization Collaborator (when using Org ID) permissions, in order to fetch assets.

In order to fetch devices View Project, View Project Snapshot permissions are required.

#### Supported From Version

Supported from Axonius version 4.7

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://api.snyk.io`)* - The hostname or IP address of the Snyk server.
2. **API Token** - An API Token associated with a user account that has the permissions to fetch assets. Refer to [Snyk API](https://docs.snyk.io/snyk-api-info) for information on how to obtain the API Key.

![SnykParameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-G06J2M8G.png)

### Optional Parameters

1. **API Prefix** - Select between *Standard (api/v1)* (default) and *Alternate (v1)*.
2. **Group ID** - Snyk Group ID. Either use a Group ID or an Organization ID. Using a group ID will fetch all users in the group (across all organizations).
3. **Organzation ID** - Snyk Organization ID. Either use a Group ID or an Organization ID. Using an organization ID will fetch all users in the organization.

<Callout icon="📘" theme="info">
  Note

  If both are supplied, default to the group ID.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Projects (Application Resources)** - Select to fetch projects with their vulnerabilities. If you selected a Group ID on the main configuration screen, it will fetch all devices from all organizations in the group.
2. **Enrich Projects (Application Resources) with Issues** - Select to enrich fetched projects with additional issue information.
3. **Issues per page** *(default: 100)* - Specify the number of issues per page.
4. **Issue Fetch Filter** - From the dropdown, select whether to filter open or resolved issues.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                       | Supported | Notes                                                        |
| --------------------------------------------- | --------- | ------------------------------------------------------------ |
| Snyk API v1                                   | Yes       |                                                              |
| Snyk REST API (formerly known as Snyk API v3) | No        | [Snyk API](https://docs.snyk.io/snyk-api-info#snyk-rest-api) |

### Related Enforcement Actions

* [Snyk - Add Vulnerability Ignore](/docs/snyk-add-ignore-vuln)
* [Snyk - Create Jira Issue](/docs/snyk-create-jira-issue)