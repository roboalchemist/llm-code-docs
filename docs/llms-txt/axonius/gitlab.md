# Source: https://docs.axonius.com/docs/gitlab.md

# GitLab

GitLab is an open-source DevOps lifecycle tool that provides a wiki, issue-tracking, and continuous integration and deployment pipeline features.

## Asset Types Fetched

* Devices, Users, Aggregated Security Findings, Roles, Groups, Application Settings, SaaS Applications, Application Resources

## Before You Begin

### APIs

Axonius uses the [GitLab v4 REST API](https://docs.gitlab.com/ee/api/README.html) and [GraphicQL API](https://docs.gitlab.com/api/graphql/).

### Required Permissions

The access token provided for the **API Token** parameter must have permission to fetch user information. To create such a token:

1. Log in to GitLab.
2. In the upper-right corner, click your avatar and select **Settings**.
3. On the **User Settings** menu, select **Access Tokens**.
4. Choose a name and optional expiry date for the token.
5. Choose the desired scopes:
   * read\_user - Allows access to the read-only endpoints under */users*. Essentially, any of the *GET* requests in the [Users API](https://docs.gitlab.com/ee/api/users.html) are allowed.
   * read\_api - Grants read access to the API, including all groups and projects, the container registry, and the package registry.
6. Click **Create personal access token**.
7. Save the personal access token somewhere safe. Once you leave or refresh the page, you won’t be able to access it again.

For more details, see [GitLab Docs - Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).

## Connecting the Adapter in Axonius

### Required Parameters

* **Host Name or IP Address** - The hostname or IP address of the GitLab server.
* **API Token** - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Image border={false} src="https://files.readme.io/1a646271915f2223bb6c1dd83a67a912d3074fa803991e6a0f2ffd27c7f0692b-image.png" />

### Optional Parameters

* **Verify SSL** - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-amp-ca-settings).
* * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
  * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
* **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
  * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
  * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
* For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

* **Async chunks in parallel** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the GitLab server in parallel at any given point.
* **Fetch projects as devices** *(required, default: False)* - Select whether to fetch projects as devices from GitLab.
  * If enabled, all connections for this adapter will fetch GitLab projects as devices.
  * If disabled, all connections for this adapter will not fetch GitLab projects.
* **Fetch Account Settings** - Select this option to fetch the GitLab account settings that appear in `admin/application_settings/general`.
  This setting requires administrator permission and is only relevant for GitLab accounts with Self-managed and GitLab Dedicated offerings. This setting has no effect on accounts with a GitLab.com offering.
* **Fetch Users unassigned to Groups or Projects** - Select this option to fetch users that are not included in any of the organization's groups or projects.
* **Exclude Public Groups and all resources within them** - Select to **not** fetch public groups and all the resources (repositories, groups, etc.) related to them.
* **Fetch Project Security Policies** - Select to enrich projects with Security Policies.
* **Fetch Archived Projects** - Select to fetch archived projects.

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

### Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                | Supported | Notes |
| ---------------------- | --------- | ----- |
| GitLab 11.0 and higher | Yes       |       |