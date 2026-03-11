# Source: https://docs.axonius.com/docs/create-cherwell-incident-per-entity.md

# Cherwell IT Service Management - Create Incident per Asset

**Cherwell IT Service Management - Create Incident per Asset** (Create Cherwell Incident per Entity) creates an incident in Cherwell for **each** for each of the assets returned by the selected query or selected on the relevant asset page.

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

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Cherwell adapter**   - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

<Callout icon="📘" theme="info">
  NOTE

  * To use this option, you must successfully configure a [Cherwell IT Service Management](/docs/cherwell) adapter connection.

  * The user name and the password used for the adapter connection must be user with permissions to create new incidents.
</Callout>

* **Incident description**   - Specify an incident description.
* **Priority** *(required, default: 5)* - Specify the incident priority.
* **Instance Name**  - The Axonius node to use when connecting to the specified host. For more details, see [Connecting Additional Axonius Nodes](/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

> 💡 Connection and Credentials
>
> When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.
>
> * **Cherwell Domain**   - The hostname or IP address of the Cherwell server.
>
> * **User Name** and **Password**  - The user name and the password of a user with permissions to create new incidents.
>
> * **Client ID**    - Enter the client ID created in the CSM Administrator. For details, see [Cherwell - Obtaining API Client IDs](https://help.cherwell.com/bundle/cherwell_rest_api_940_help_only/page/oxy_ex-1/content/system_administration/rest_api/csm_rest_obtaining_client_ids.html#ObtainingApiClientIds#OpenSwagger#ObtainingApiClientIds#OpenSwagger).
>
> * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
>
> * **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Cherwell Domain**.
>
> * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Cherwell Domain**.
>
> * If not supplied, Axonius will connect directly to the value supplied in **Cherwell Domain**.

* **Sleep 1 second every token request**   - Select this option to wait before sending authentication tokens.

* **Short description**   - Specify the incident title.

* **Add default incident description**   - Select whether to send the incident description to Cherwell.
  * If enabled, Axonius will include the default incident description (mentioned below) in the Cherwell incident.
  * If disabled, Axonius will not include the default incident description (mentioned below) in the Cherwell incident.

* **Message example:**
  *Alert - "test" for the following query has been triggered: Missing Sophos*

*Alert Details*
*The alert was triggered because: The number of entities is above 0
The number of devices returned by the query:4
The previous number of devices was:4*

*You can view the query and its results here: [https://demo-latest.axonius.com/devices?view=Missing](https://demo-latest.axonius.com/devices?view=Missing) Sophos*

* **Customer display name**   - Specify the customer display name.
* Multiple optional incident related settings  :
  * **Source**
  * **Service**
  * **Category**
  * **Subcategory**
  * **Incident type**
  * **Status**

<Callout icon="📘" theme="info">
  NOTE

  Since the valid values of the different parameters are customer specific, Axonius does not validate any of those parameters values. You must make sure inserted values are correct, otherwise, the request might fail.
</Callout>

* **Additional fields** *(optional, default: empty)* - Specify additional fields to be added as part of the incident as key/value pairs in a JSON format. For example:

```json
{"field1": "value1", "field2": "value2"}
```

.

* If supplied, Axonius will add the specified fields and values to the created incident. If one of the specified fields is invalid, the request might fail.
* If not supplied, Axonius will not add any additional fields to the created incident.
* **Axonius to Cherwell field mapping**  -  Use to map Axonius fields to the CMDB fields. The input should be key/value pairs in a JSON format.
  For example:

```json
{`'axonius_field1`:`servicenow_field1`, `axonius_field2`:`servicenow_field2`}
```

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).