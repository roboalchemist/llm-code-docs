# Source: https://docs.axonius.com/docs/illumio-delete-workload.md

# Illumio - Delete Workload

**Illumio - Delete Workload** Deletes workloads for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** *(required)* - The hostname or IP address of the Illumio Core server that Axonius can communicate with via the [Required Ports](#required-ports).

  * **Port** - The port for connection. The default is 8443.

  * **Authentication User Name**  *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. This is a randomized name generated when a user creates an API key.

  * **API Secret** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

  * **Organization ID** *(required)* - Auto generated when the API Secret is created.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Illumio Core 24.5.0 - Delete a Workload](https://product-docs-repo.illumio.com/Tech-Docs/Core/24.5/REST-APIs/REST_API_24.5/index.html#delete-a-workload) REST API.

### Required Permissions

The API key must have the following permissions configured in Illumio to use this action:

* Workload write access - Permission to delete workloads via the REST API
* Organization access - Valid access to the specified Organization ID
* Appropriate role assignment - Owner, Workload Manager, or a custom role with workload delete permissions
* Label scope access - Either unscoped (full organization access) or scoped to specific labels where workloads will be deleted
* Recommended Role: Workload Manager or Owner role for service account-based API keys.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).