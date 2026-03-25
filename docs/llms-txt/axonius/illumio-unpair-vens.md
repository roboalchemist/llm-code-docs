# Source: https://docs.axonius.com/docs/illumio-unpair-vens.md

# Illumio - Unpair VEN from Workload

**Illumio - Unpair VEN from Workload** unpairs VEN from a workload for:

* Workload devices returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Illumio Adaptive Security Platform (ASP) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      Note

      To use this option, you must successfully configure an [Illumio Adaptive Security Platform (ASP)](/docs/illumio-asp) adapter connection.
    </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Firewall Restore** - Select the method for restoring the firewall state after the VEN is uninstalled. The available options are: **default**, **saved**, or **disable**.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** *(required)* - The hostname or IP address of the Illumio Core server that Axonius can communicate with via the [Required Ports](#required-ports).

  * **Port** - The port for connection. The default is 8443.

  * **Authentication User Name**  *(required)* - The credentials for a user account that has the Permissions to fetch assets. This is a randomized name generated when a user creates an API key.

  * **API Secret** *(required)* - An API Key associated with a user account that has Permissions to fetch assets.

  * **Organization ID** *(required)* - Auto generated when the API Secret is created.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Illumio Core 24.5.0 - Get the collection of all VENs](https://product-docs-repo.illumio.com/Tech-Docs/Core/24.5/REST-APIs/REST_API_24.5/index.html#get-the-collection-of-all-vens) REST API.

### Required Permissions

The API key must have the following permissions configured in Illumio to use this action:

* VEN write access - Permission to unpair VENs via the REST API.
* Organization access - Valid access to the specified Organization ID.
* Appropriate role assignment - Owner, Workload Manager, or a custom role with workload write permissions.
* Label scope access - Either unscoped (full organization access) or scoped to specific labels where workloads will be created.
* Firewall restore option - Optional parameter to control firewall state after unpairing (saved, default, or disable).
* Recommended Role: Workload Manager or Owner role for service account-based API keys.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).