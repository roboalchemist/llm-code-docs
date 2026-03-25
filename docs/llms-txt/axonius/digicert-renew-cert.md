# Source: https://docs.axonius.com/docs/digicert-renew-cert.md

# DigiCert - Renew Certificate

**DigiCert - Renew Certificate** renews expired certificates for:

* Assets returned by the selected query or assets selected on the relevant asset page.

<Callout icon="💡" theme="warn">
  Important

  Only certificates from certificate profiles configured with `enrollment_method: rest_api` and `authentication_method: third_party_app` can be renewed using this Enforcement Action.
</Callout>

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

* **Use stored credentials from DigiCert CertCentral adapter** - Select this option to use credentials from the adapter connection.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [DigiCert CertCentral](https://docs.axonius.com/axonius-help-docs/docs/digicert-certcentral) adapter connection.
  </Callout>

* **Host Name or IP Address** -  The hostname or IP address of the DigiCert server.

* **API Key** - For instructions on generating an API Key, refer to [DigiCert Trust Lifecycle Manager REST API](https://one.digicert.com/mpki/docs/swagger-ui/index.html) (under Authentication).

* **Renewal Duration in Days** *(default: 30)* - The number of days the renewal will be set for.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [ DigiCert API](https://one.digicert.com/mpki/docs/swagger-ui/index.html).

## Version Matrix

This Enforcement Action was tested only with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| API v1  | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).