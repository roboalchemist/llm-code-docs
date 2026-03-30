# Source: https://docs.axonius.com/docs/sonatype.md

# Sonatype

Sonatype provides software supply chain management with a focus on speed and security in open source development.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users, Vulnerabilities, Roles, Business Applications, SaaS Applications, Organizational Units

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Sonatype server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password/Applications Token** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Sonatype" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sonatype.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Enrich Users with Role Membership** - Enable this option to enrich Users with Role Membership.
2. **Fetch OrganizationalUnits from Organizations** - Enable this option to fetch OrganizationalUnits from Organizations.
3. **Fetch SecurityRoles from Roles** - Enable this option to fetch SecurityRoles from Roles.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the following APIs:

* /api/v2/users - [Sonatype User REST API](https://help.sonatype.com/en/user-rest-api.html)
* /api/v2/applications - [Sonatype Application REST API](https://help.sonatype.com/en/application-rest-api.html)
* /api/v2/reports/applications - [Sonatype Report REST APIs - reportId](https://help.sonatype.com/en/report-rest-api.html#reportid)
* /api/v2/organizations - [Sonatype Organizations REST API](https://help.sonatype.com/en/organizations-rest-api.html)
* /api/v2/roleMemberships/application/`{applicationInternalId}` - [Sonatype Authorization Configuration REST API](https://help.sonatype.com/en/authorization-configuration-rest-api.html)
* [Sonatype Report REST APIs - Downloading Component Information](https://help.sonatype.com/en/report-rest-api.html#step-2---downloading-component-information)

## Supported From Version

Supported from Axonius version 6.1