# Source: https://docs.axonius.com/docs/proofpoint-security-education.md

# Proofpoint Security Awareness Training

Proofpoint Security Awareness Training provides interactive and customizable security awareness training.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Proofpoint Security Awareness Training server. When using cloud hosted Proofpoint Security Awareness Training you will need to enter one of the following hostnames, depending on your region.[ Refer to  Proofpoint Security Awareness Training API](https://proofpoint.securityeducation.com/api/reporting/documentation/#api-API_Endpoints)
   * US: results.us.securityeducation.com

   * EU: results.eu.securityeducation.com

   * AP: results.ap.securityeducation.com

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ProofPointSecAwareness](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProofPointSecAwareness.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Endpoints Config**  - By default the adapter enriches users via various endpoints. Click on `>` to open the following settings for configurable endpoints:
  * **Fetch User Tags** - Select this option to fetch user tags.
  * **Enrich Users with Knowledge Assessments** - Toggle off to not enrich with knowledge assessments.
  * **Enrich Users with Phishing Alarms** - Toggle off to not enrich users with phishing alarms.
  * **Enrich Users with Phishings** - Toggle off to not enrich users with phishings.
  * **Enrich Users with Trainings** - Toggle off to not enrich users with trainings.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Proofpoint Security Awareness Training Results API](https://proofpoint.securityeducation.com/api/reporting/documentation/).

## Supported From Version

Supported from Axonius version 4.8