# Source: https://docs.axonius.com/docs/bigfix-sca.md

# BigFix Compliance Analytics (formerly SCA)

BigFix Compliance Analytics (formerly SCA) is a web-based application designed to help you manage security, vulnerability, and risk assessment.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the BigFix Compliance Analysis server.

2. **Token** *(required)* - An  API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. You can see your API Token in the Account Preferences screen of the BigFix Compliance interface.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="BigFixComplianceAnalytics" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BigFixComplianceAnalytics.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch last seen X days ago** - Only fetch devices and enrichments that were last seen X days ago. Note that this filter option does not work on Exception Results.
2. **Checklist IDs** - Specify a comma-separated list of checklist IDs to fetch from.
3. **Entities per page** *(default: 200)* - Set the number of entities returned per page request.
4. **Fetch vulnerabilities** - Select this option to fetch vulnerabilities.
5. **Use asynchronous fetch** - Toggle on to use async fetch for endpoints. If selected, **Chunk size** is enabled.
   * **Chunk size** *(default: 10)* - Specify the chunk size for the async requests.
6. **Keys to remove from JSON** - Enter fields that you want to be removed from the JSON after parsing. This may be useful if parsing is longer than expected.
7. **List of custom properties numbers to fetch** - Add a list of computer custom property numbers to fetch.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [BigFix REST API](https://developer.bigfix.com/rest-api/gettingstarted.html). Before connecting to the BigFix REST API, certain actions must be completed. For more information, see [BigFix Developer Prerequisites](https://developer.bigfix.com/rest-api/prerequisites.html).

## Required Permissions

* The WebReports service must be running. If you installed multiple Web Reports servers, local or remote, the Web Reports server that is selected for using the REST API is the first entry that appears in the table *dbo.AGGREGATEDBY* contained in the database **BFEnterprise**.

* The user logging into the REST API must be defined as a [BigFix Console operator](https://help.hcltechsw.com/bigfix/10.0/platform/Platform/Console/c_adding_local_operators.html) with the *Can use REST API* and the *Custom Content* permissions set to **YES** in its definition or in one of the assigned roles.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                   | Supported | Notes |
| ----------------------------------------- | --------- | ----- |
| BigFix Compliance Analytics Version 2.0.8 | Yes       |       |

## Supported From Version

Supported from Axonius version 5.0