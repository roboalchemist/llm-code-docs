# Source: https://docs.axonius.com/docs/pagerduty.md

# PagerDuty

PagerDuty is a digital operations platform for system administrators and support teams to manage incident response.

**Related Enforcement Actions**

* [Create Incident - PagerDuty](/docs/create-incident-pagerduty)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: api.pagerduty.com)* - The hostname or IP address of the PagerDuty server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Token** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. The API token for this adapter is static and in power of the PagerDuty user.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="PagerDuty" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PagerDuty.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enhance team information** - Select this option to add  more details regarding the teams associated with the user.
* **Fetch users escalation policies** - Select this option to add [escalation policies](https://developer.pagerduty.com/api-reference/51b21014a4f5a-list-escalation-policies) related to the users, to the 'user' fields, based on the "target" of the escalation policy.
* **Prefetch Priority IDs for Create Incident Enforcement Action** *(default: true)* - Select this option to automatically populate the **Priority ID** field when running the **Create Incident - PagerDuty** Enforcement Action.
* **Prefetch Service IDs for Create Incident Enforcement Action** *(default: false)* - Select this option to automatically populate the **Service ID** field when running the **Create Incident - PagerDuty** Enforcement Action.
* **Fetch EC Action ticket updates** *(default: true)* - Select this option to configure the adapter to fetch updates on tickets created by Axonius users. The updated ticket information is displayed in the Tickets table showing information on all tickets in the system (**Assets** `>` **Tickets**) or on Tickets of a specific asset (in the **Asset Profile** of the relevant asset).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [PagerDuty LIst Users API](https://developer.pagerduty.com/api-reference/c96e889522dd6-list-users).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**
* **Any customer-defined port used by the PagerDuty API**

## Required Permissions

The value supplied in [Token](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.7