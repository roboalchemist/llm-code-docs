# Source: https://docs.axonius.com/docs/run-ansible-command.md

# Red Hat Ansible Tower - Run Command

**Red Hat Ansible Tower - Run Command** runs a Red Hat Ansible command on:

* Assets returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Red Hat Automation Controller (Ansible Tower) adapter** - Select this option to use the the first connected Red Hat Automation Controller (Ansible Tower) adapter credentials.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Red Hat Automation Controller (Ansible Tower)](/docs/red-hat-ansible-tower) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Ansible Tower Domain** - The domain of the Red Hat Ansible Tower on which to run the command. This field is filled in automatically when **Use stored credentials...** is enabled
* **Name** - The name of the command.
* **Organization ID** - The ID of the organization within Red Hat Ansible Tower.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this Enforcement Action.

  * **API Token** - The API token for the supplied username and password.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Description** - Description of the command.
* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Additional fields** - Specify additional fields to be added as key/value pairs in a JSON format.\
  For example:

```json
{"field1": "value1", "field2": "value2"}
```

If one of the specified fields is invalid, the request might fail.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Tower API Reference Guide — Ansible Tower API Guide v3.8.6 ](https://docs.ansible.com/ansible-tower/latest/html/towerapi/api_ref.html#) API.

## Required Permissions

The values supplied in [Connection Parameters](#connection-parameters) above must have the  permissions to perform the command you want to run.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).