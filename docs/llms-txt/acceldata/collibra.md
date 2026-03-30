# Source: https://docs.acceldata.io/documentation/collibra.md

# Collibra

Integrate **Collibra** with **Acceldata Data Observability Cloud (ADOC)** to bridge the gap between data governance and data observability.

This integration allows Collibra users to access Acceldata’s data quality and reliability insights directly within the Collibra platform, ensuring unified visibility and trust in enterprise data assets.

---

## Overview

The Collibra integration enables governance users to assess data reliability and quality without leaving the Collibra environment.

By connecting Collibra as a **data catalog source** in ADOC, organizations can map existing ADOC data sources (such as Snowflake or Hive) to corresponding Collibra assets using unique identifiers (UIDs).

When reliability policies execute on a mapped ADOC data source, the **execution results** — including data quality metrics and reliability scores — are automatically **published to the mapped asset in Collibra**.

If a mapped Collibra asset exists, results are displayed on that asset’s **Collibra Overview page**; if not, they are ignored.

This integration delivers a governance-grade, automated publishing workflow, ensuring that data reliability insights from ADOC remain continuously synchronized with Collibra’s data catalog.

---

## Supported Authentication Methods

| Authentication Type | Description | 
| ---- | ---- | 
| **Basic Authentication** | Authenticate using your Collibra username and password for secure connection. | 
| **Collibra OAuth 2.0 (Client Credentials Flow)** | Authenticate securely using Collibra’s built-in OAuth mechanism with a Client ID, Client Secret, and Token URL. This is Collibra’s proprietary OAuth 2.0 implementation used to generate API access tokens. | 


---

## Key Capabilities

- **Unified Governance and Observability:** View Acceldata data quality and reliability insights directly within Collibra.
- **Automated Publishing Workflow:** Reliability scores and data quality metrics automatically sync after each policy run in ADOC.
- **Always Up-to-Date Metrics:** No manual export or synchronization required—data is refreshed automatically.
- **Secure Integration:** Supports both Basic and OAuth authentication modes for secure, enterprise-ready connectivity.
- **Streamlined Experience:** Collibra users can assess asset health without switching between platforms. Users are provided with a link to navigate back to the ADOC platform and view execution results.

---

## Prerequisites

Before configuring the Collibra connector, ensure that:

1. You have valid **Collibra credentials** (Username/Password or OAuth credentials).
2. The Collibra REST API must be accessible from your ADOC **Control Plane** network. The Control Plane handles configuration, API communication, and metadata publishing to Collibra.
3. At least one ADOC data source to be mapped with a data source in Collibra.

---

## Add Collibra as a Data Source

Follow these steps to register Collibra in ADOC:

1. Navigate to **Register** -&gt; **Data Sources** in ADOC.
2. Click **Add Data Source**.
3. Select **Collibra** from the list of available connectors.
4. Enter the **Data Source Name** and optional **Description**.
5. Click **Next** to open the **Connection Details** page.
6. Provide the following:
    1. **Collibra Base URL**: Enter the Collibra server or cloud URL. Example: `https://myorg.collibra.com` 
    2. **Authentication method**:
        - **If OAuth is enabled**: Provide OAuth Token URL, Client ID, and Client Secret.
        - **If OAuth is disabled:** Provide Username and Password.

7. Click **Test Connection** to validate access.
    - If successful, click **Next** to continue.
    - If unsuccessful, verify your credentials or network access.

8. On the **Observability Setup** page, map Collibra data source to ADOC data source:
    1. Select one or more **ADOC data sources** (e.g., Snowflake data source).
    2. Select corresponding **Collibra data source** to link them.
    3. Click **Add Mapping** to include additional pairs.

9. Click **Submit** to complete registration.

Once configured, ADOC automatically publishes reliability scores and data quality metrics to Collibra after each policy execution.

---

## Automated Data Publishing Workflow

After successful configuration:

- ADOC automatically sends data quality and reliability results to Collibra following each policy execution.
- Collibra’s data catalog reflects updated reliability scores, freshness metrics, and rule outcomes.
- Governance users can review these insights without leaving Collibra, ensuring both compliance and trust.

Note No manual export or synchronization is required. Updates occur automatically after every successful ADOC policy run.

---

## Viewing Reliability Insights in Collibra

Once Collibra has been integrated as a data source in ADOC and mappings are created between Collibra and ADOC data sources, Acceldata automatically publishes **reliability scores** and **data quality reports** to Collibra after every policy execution.

To make these insights visible within the Collibra platform, users must perform a one-time configuration in the Collibra UI to add Acceldata attributes to their asset layout.

### Step 1: Add Acceldata Attributes to Collibra Asset Layout

1. Log in to your **Collibra platform**.
2. Navigate to the **data source asset** (for example, a table, dataset, or system) that has been mapped to ADOC.
3. Click **Edit Layout** in the upper-right corner of the asset page.
4. In the layout editor, choose **Add Connection** -&gt; **Add Characteristic**.
5. In the search box, type **Acceldata** and select the following two characteristics:
    - **Reliability Score** (numeric value representing overall reliability)
    - **Data Quality Report** (text field containing summarized rule and policy outcomes)

6. Save and **Publish** the layout.

Once saved, these two attributes become visible in the asset overview section of Collibra.

### Step 2. View Published Insights in Collibra

After the next ADOC policy execution:

1. Navigate back to the same Collibra asset page.
2. The **Reliability Score** and **Data Quality Report** attributes will be populated automatically.
3. Click on the **Acceldata link** within the attribute to open the detailed results page in the ADOC platform.

This redirection allows users to analyze complete rule-level details, failed record counts, and trend metrics without leaving the governance context.

### Step 3. (Optional) Configure Layout for Multiple Assets

If reconciliation policies involve **two data sources** (e.g., left and right datasets), and both are registered in Collibra:

- Acceldata will publish reliability results for **each participating asset**.
- Ensure both assets in Collibra have the **Acceldata attributes** added to their layouts, so the results appear correctly.

---

## Next Steps

- Verify successful data publishing in Collibra’s **asset details view**.
- Schedule regular policy runs in ADOC to keep insights up to date.
- Enable **notifications** in Collibra for key updates or quality threshold breaches.