# Source: https://docs.axonius.com/docs/pivotal-cloud-foundry.md

# Pivotal Cloud Foundry

Pivotal Cloud Foundry is an application development and deployment platform for public and private clouds.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Domain** *(required)* - The hostname or IP address of the Pivotal Cloud Foundry server.

<Callout icon="📘" theme="info">
  NOTE

  The supplied value should not include an "api" prefix.
</Callout>

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Domain**.

5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="image.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1660).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Async chunks in parallel** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the Pivotal Cloud Foundry server in parallel at any given point.
2. **Use API V2** *(optional)* - Select whether to use Cloud Controller API V3 or Cloud Controller API V2 (deprecated version).
   * If selected,  the adapter connection will use Cloud Controller API V2.
   * If cleared, the adapter connection will use Cloud Controller API V3.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the following APIs:

* [Cloud Controller API V3 (default)](http://v3-apidocs.cloudfoundry.org/version/3.82.0/index.html#links)
* Cloud Controller API V2 (deprecated)

## Required Permissions

The value supplied in [User Name](#parameters) must have the following permissions to fetch assets:

* Global Auditor role on CloudFoundry
* cloud\_controller.global\_auditor scope granted to the user on UAA (the auth server used for CloudFoundry)

To create a Global Auditor account, see [Create a Global Auditor](https://docs.cloudfoundry.org/uaa/uaa-user-management.html#global-auditor).

For more information about assigning  roles and scopes, see [Orgs, Spaces, Roles, and Permissions](https://docs.cloudfoundry.org/concepts/roles.html).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may also work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version                      | Supported | Notes |
| ---------------------------- | --------- | ----- |
| Cloud Foundry V3 (v. 3.82.0) | Yes       |       |