# Source: https://docs.axonius.com/docs/add-or-remove-assets-from-watchlist.md

# Recorded Future - Add or Remove Assets To/From Watchlist

**Recorded Future - Add or Remove Assets To/From Watchlist** adds devices to or remove them from a watchlist in Recorded Future for:

* Assets returned by the selected query or assets selected on the relevant asset page. This action is supported only for devices.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Recorded Future adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Recorded Future](/docs/recorded-future) adapter connection.
  </Callout>

* **Watchlist Name** - Enter the watchlist's name.

* **Action Type** - Select between Add and Remove.

* **Recorded Future Entity Type** - The Recorded Future entity type of the watchlist entries.

* **Map Axonius field to pull entity names from** - Use the **Field Mapping Wizard** to translate Recorded Future entities to Axonius fields. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily to each `entity_name`. For a detailed explanation, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** *(default: `https://api.recordedfuture.com`)* - The host name or IP address of a Recorded Future server.

  * **API key** - Specify the API key you have defined.

  * **List of CIDR** - Specify a comma-separated list of CIDR blocks (for example: 192.168.20.0/24,192.168.30.0/24) to connect to.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Create a new list** - Enable this to create a new list under the name you entered for **Watchlist Name**.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).