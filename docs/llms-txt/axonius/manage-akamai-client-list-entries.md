# Source: https://docs.axonius.com/docs/manage-akamai-client-list-entries.md

# Akamai Client List - Append, Delete, and Update entries in a list

**Akamai Client List - Append, Delete, and Update entries in a list** appends, deletes, and updates client list entries in Akamai for:

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

## Required Fields

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Host Name or IP Address** - The hostname or IP address of the Akamai client list API server that Axonius can communicate with via the [Required Ports](#required-ports).

* **Client Token**, **Client Secret**, and **Access Token** - The credentials for a user account that has the [Required Permissions](#required-permissions) to edit client list entries. To create a **Client Token**, **Client Secret**, and **Access Token**, refer to [Create an API client with custom permissions (EdgeGrid)](https://techdocs.akamai.com/developer/docs/edgegrid).

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Asset Main Configuration

These fields must be configured to run the Enforcement Action. (**Entry Type** is only required for the **append** action.)

* **List ID** - The ID of the Akamai client list whose entries are to be managed.

* **Action to Perform** - The action to be performed on the Akamai client list entries:
  * **append** - Append entries to the client list.
  * **delete** - Delete entries from the client list.
  * **update** - Update entries in the client list.

* **Map Axonius fields to Akamai client list entry fields** - Use the **Field Mapping Wizard** to map Axonius fields to fields in the Akamai client list platform. In this way you can transfer data found in Axonius into the Akamai client list platform. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily. For details, see [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping).
  The following Akamai client list entry fields can be mapped to Axonius fields:

  * **value** - Required for all action types. This is the identifier of the client list entry. It can be one of the following: IP address, Autonomous System Number (ASN), Geo location, TLS fingerprint, or file hash. It has a string length between 1 and 255 characters.
  * **description** - An additional description of the client list entry, up to 255 characters.
  * **expirationDate** - An ISO 8601 timestamp indicating when the entry expires.
  * **tags** - Any defined tags for a specified client list.

* **Entry Type** - Required for the **append** action. Specifies the entry type in the Akamai client list. Available entry types: IP, GEO, ASN, TLS\_FINGERPRINT, FILE\_HASH, USER.

## Additional Fields

These fields are optional.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Akamai Client Lists](https://techdocs.akamai.com/client-lists/reference/api) API, specifically the section on:

* Update client list entries - Append, delete, and update entries in a single batch.

## Required Ports

Axonius must be able to communicate with the Akamai client list API server via the following ports:

* 80/443

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* **READ-WRITE** access to the 'Client Lists' (also known as 'Network Lists') service.
  Configure these permissions as follows:

  1. In the Akamai Control Center, navigate to **Identity & Access** `>` **API Clients**.
  2. Select your client.
  3. Select **APIs**.
  4. Find **Network Lists** (sometimes labeled **Client Lists**).
  5. Set to **READ‑WRITE**.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).