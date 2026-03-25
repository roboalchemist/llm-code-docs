# Source: https://docs.axonius.com/docs/snyk-add-ignore-vuln.md

# Snyk - Add Vulnerability Ignore

**Snyk - Add Vulnerability Ignore** allows you to ignore Security Findings fetched from different adapters.
For example, you can use this action to ignore Security Findings whose status is 'Fixed', or Security Findings with a certain severity or risk score.

<Callout icon="📘" theme="info">
  Note

  This action is only applicable to Security Findings assets, and is only available for customers with the **Exposures** product.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the adapter** - Select this option to use credentials from the adapter connection.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Snyk](/docs/snyk) adapter connection.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** *(default: `https://api.snyk.io`)* - The hostname or IP address of the Snyk server.

  * **API Token** - An API Token associated with a user account that has the permissions to fetch assets. Refer to [Snyk API](https://docs.snyk.io/snyk-api-info) for information on how to obtain the API Key.

  * **Group ID** - Snyk Group ID. Either use a Group ID or an Organization ID. Using a group ID will fetch all users in the group (across all organizations).

  * **Organzation ID** - Snyk Organization ID. Either use a Group ID or an Organization ID. Using an organization ID will fetch all users in the organization.

  <Callout icon="📘" theme="info">
    Note

    If both are supplied, default to the group ID.
  </Callout>

  * **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

  * **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [Snyk API](https://docs.snyk.io/snyk-api/reference/ignores-v1#post-org-orgid-project-projectid-ignore-issueid).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* View organization
* View project ignores
* Create new project ignores

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).