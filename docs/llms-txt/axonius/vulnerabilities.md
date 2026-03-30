# Source: https://docs.axonius.com/docs/vulnerabilities.md

# Aggregated Security Findings Page

Explore the Aggregated Security Findings page for a comprehensive view of cybersecurity vulnerabilities, enabling prioritization based on asset criticality and potential impact.

Use **Aggregated Security Findings** to see a consolidated view of all the vulnerabilities in your organization from all sources. The Aggregated Security Findings page delivers increased visibility into cybersecurity vulnerabilities and risks. It helps security, IT, and risk teams identify vulnerabilities across fleets of assets, enabling them to prioritize vulnerabilities based on asset criticality, potential impact, and recognized threats.

A vulnerability is a software defect that could allow hackers to gain control of a system. Axonius presents vulnerabilities as defined by the [Common Vulnerabilities and Exposures (CVE) list](https://cve.mitre.org/cve/). Axonius discovers vulnerabilities by extracting CVE information fetched from adapters.

<Callout icon="📘" theme="info">
  Note

  Some adapters, such as Tenable.sc, require selecting the **Fetch Vulnerabilities** advanced setting before viewing their vulnerability information on the Aggregated Security Findings page.
</Callout>

To access the page, from the **Assets** menu, expand **Exposures** and select **Aggregated Security Findings**.

![AggregatedSecurityFindingsMainPage](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/exposures/Aggregated%20SF_main%20page.png)

The total number of unique devices on which vulnerabilities were found is shown above the Aggregated Security Findings table. Click on the number of devices to open the devices on which vulnerabilities were found on the **Devices** page.

![DeviceCount](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-LFKF4PTU.png)

## Aggregated Security Findings Fields

Fields displayed on the Aggregated Security Findings page include:

* **Adapter Connections** - shows the icons of the adapter connections or enrichment from which the Aggregated Security Findings originate.

* **Vuln ID** - The identifier of the vulnerability. This can be either a CVE ID or a different vulnerability identifier provided by some adapters.
  * When the value is a CVE ID, it contains is a clickable link to the CVE details in the NIST National Vulnerability Database (NVD).
  * When the vulnerability identifier isn't a CVE type but is fetched from an adapter, such as from a Tenable adapter, the vulnerability ID appears without a CVE prefix. When a link is available for a specific vulnerability identifier, you can click it to learn more about the vulnerability and how to remediate it.

    <Callout icon="📘" theme="info">
      Note

      For supported adapters that fetch "non-CVE" vulnerability identifier information:

      * A prefix of the adapter appears before the value displayed in the **Vuln ID** column.

      * An optional **Is CVE** column displays ‘No’ for non-CVE vulnerabilities and ‘Yes’ for CVE vulnerabilities.
    </Callout>

* **Device Count** - The **Device Count** shows the number of devices affected by this specific vulnerability. Click a **Device Count** to open the **Devices** page with the devices affected by this vulnerability. Devices present *Total CVE Count by Severity*. CVEs are only counted if the CVE was validated on NVD.

* **Software Name** and **Software Vendor** - When a CVE is applicable for multiple software, these fields are populated as "Multiple Software" and "Multiple Vendors".

* **NVD published date** - The date the vulnerability was added to the NVD database.

* **NVD Modified date** - The date the vulnerability was modified.

* **CVSS** -[Common Vulnerability Scoring System (CVSS)](https://nvd.nist.gov/vuln-metrics/cvss), a numeric score used to supply a qualitative measure of severity. The CVSS rating is fetched from the source (v2,0, v3.0, v4.0, etc.).

* **CVE Exploitability Score** - How likely it is that a vulnerability will be exploited according to NIST.

* **EPSS Score** - How likely it is that a software vulnerability will be exploited in the wild according to [EPSS](https://www.first.org/epss/model).

* **CVE severity** -[NONE, LOW, MEDIUM, HIGH, CRITICAL](https://nvd.nist.gov/vuln-metrics/cvss), UNTRIAGED, NEGLIGIBLE, INFO, MODERATE, SERIOUS, SEVERE, URGENT, or CRITICAL value which are based on the CVSS rating.

* **CVE description, Synopsis, and Reference**

* [**CVE Vector information**](/docs/vulnerabilities#cve-vector-information)

* **First Seen, Last Seen** - The time when an adapter first or last detected the vulnerability.

Not all available fields are displayed by default. Use **Edit Columns** to add or remove columns. See [Setting Page Columns Display](https://docs.axonius.com/axonius-help-docs/docs/setting-page-columns-display) for more information.

You can add the **CWE ID** column to view corresponding vulnerabilities appearing in the [Common Weakness Enumeration (CWE) list](https://cwe.mitre.org/data/index.html). Click a specific **CWE ID** link to learn more about the vulnerability and how to remediate it.

### Data Enrichments

Axonius uses a variety of sources to collect information on reported CVEs and other Security Findings, and enriches them with that information. The icon of the enrichment from which the vulnerabilities originate is displayed under the Adapter Connection column. See [Vulnerability Enrichment](https://docs.axonius.com/axonius-help-docs/docs/vulnerability-enrichment) for detailed information on the enrichment sources.

### CVE Vector Information

To view CVE Vector information add these columns to the Aggregated Security Findings page. See [Setting Page Columns Display](/docs/setting-page-columns-display) for more information.

The following fields are available:

| Vector                          | Available in CVSS Version | Notes                                                            |
| ------------------------------- | ------------------------- | ---------------------------------------------------------------- |
| CVE Vector: Access Complexity   | 2.X                       | Describes whether the access complexity is low, medium, or high  |
| CVE Vector: Access Vector       | 2.X                       | Describes whether the Access Vector is local or on a network     |
| CVE Vector: Attack Complexity   | 3.X                       |                                                                  |
| CVE Vector: Attack Vector       | 3.X                       |                                                                  |
| CVE Vector: Authentication      | 2.0                       | Returns **None** if no CVE Vector Authentication exists          |
| CVE Vector: Availability        |                           |                                                                  |
| CVE Vector: Confidentiality     |                           |                                                                  |
| CVE Vector: Integrity           |                           |                                                                  |
| CVE Vector: Privileges Required | 3.X                       | Reports whether privileges or required, and what level, if known |
| CVE Vector: Scope               | 3.X                       |                                                                  |
| CVE Vector: User Interaction    | 3.X                       |                                                                  |
| CVE Vector: Version             | 3.1, 3.0, 2.0             |                                                                  |

## Creating Queries on Aggregated Security Findings

Use Queries on the Aggregated Security Findings page to create a unique set of queries. Create queries using either of the following modes:

* **Query Wizard** (the default) - Create a query using the **Query Wizard**, or in the query bar, selecting a saved query or writing a query.

* **Basic** mode - Create a query by selecting filters. Learn more and [how to create Queries in Basic mode](/docs/basic-query-mode).

Aggregated Security Finding queries with the Query Wizard are created on two levels:

1. The first level of the query focuses on **vulnerability parameters**: fields such as the CVSS score, severity, or attack vector.
2. The second level queries **devices**, such as operating system, installed software, or the last update date. Use these queries to find out which critical vulnerabilities exist and whether they impact critical assets in your environment; or, how many vulnerabilities exist, and whether they appear on devices with open ports/a specific patch applied.

After running the query, the table shows the vulnerabilities queried, filtered by the devices they affect.
For example, this query shows vulnerabilities with the CVSS score over 8, only on devices where the operating system is Windows:

<Image align="center" alt="AggregatedSecurityFindingsQuery" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/exposures/ASF%20query.png" />

<Callout icon="📘" theme="info">
  Note

  While it's recommended to get more context for the results, you don't have to fill in the Device section of the query to find vulnerabilities in your environment.
</Callout>

To learn more on Axonius queries, see [Working with the Query Wizard](https://docs.axonius.com/axonius-help-docs/docs/working-with-the-query-wizard) and [Saved Queries](https://docs.axonius.com/axonius-help-docs/docs/saved-queries-devices).

### Refining the Device Count Displayed from Device-based Fields in Aggregated Security Findings

It can be very useful to refine the device count displayed for device connected fields in Aggregated Security Findings. For example, in this query:

1. Build a query on an Aggregated Security Finding field on the table, such as CVSS Severity is High.
2. Filter the findings displayed by a Device query to show the Aggregated Security Finding in your environment by a defined Device query, such as Windows Devices.
3. After running the query, the table shows the Aggregated Security Findings queried, filtered by the devices they affect.

Once you get results for a query like this, to further refine the device count for such a query, use the **Data Refinement** field on the **Device Count** column for unique Aggregated Security Findings fields that are found on devices.
For example: there might be 50 devices with *CVSS Severity is High*, and 20 with *Mitigated Yes* (and 30 with *Mitigated no*). To display the number of devices where both *Mitigated Yes* matches those exact devices who also have *CVSS Severity is High*, perform the following data refinement:

1. Click the **Refine Data** (filter) icon next to the **Device Count** column.

   ![RefineDataIcon](https://files.readme.io/0cfb3c17810d72cbd6085387d59bc5c39d43b3577f1a87cda72b5d0d5437b3ca-image.png)

   <br />
2. From the Refine Data dialog, under **Device related asset entities - refine by condition**, the **Security Finding** complex object field is pre-selected on the first row. From second row select the device-related Aggregated Security Finding field that you want to filter by and click **Done**.\
   For example, select **Mitigated yes** to display the exact number of devices where the selected Aggregated Security Finding on them has a mitigated field with yes.

   <Image align="center" alt="RefineDataDialog" width="600px" src="https://files.readme.io/cbf20c6c0c4741043113cfdefa04ce0b53b00d429c950417e43cb34bcfa56117-image.png" />

   <br />

The **Aggregated Security Findings** page now shows the device count that matches the number of devices on which the vulnerabilities were found. If the device count is zero the row is hidden.
Click on the **Device Count** to open these devices on the **Devices** page.

You can also [refine the data displayed on the Aggregated Security Findings page](/docs/setting-page-columns-display#refining-the-data-displayed-in-table-columns-and-rows) in additional ways.

## Additional Actions on the Aggregated Security Findings page

From Aggregated Security Findings page you can perform the following actions on the data:

[Displaying Historical Data](https://docs.axonius.com/docs/assets-page#displaying-historical-data)

[Exporting Asset Data to CSV](https://docs.axonius.com/docs/exporting-devices-data-to-csv)

[Tagging Assets](https://docs.axonius.com/docs/devices-actions#tag)

[Adding Custom Data to Assets](https://docs.axonius.com/docs/working-with-custom-data)

And more actions as detailed in the [Asset Actions page](https://docs.axonius.com/docs/devices-actions).

### Managing Exclusions

You can manage exclusions from the Aggregated Security Findings page.

To add an Aggregated Security Finding to a rule, hover over a row and click the **Exclude** button, or select one or more items and then click **Exclude**. The **Create Exclusion Rule** dialog opens with the Aggregated Security Finding(s) you selected filled in.

Learn more about creating [Vulnerabilities Exclusion Rules](https://docs.axonius.com/axonius-help-docs/docs/vulnerabilities-exclusion-rules).

## Using Aggregated Security Findings Queries in Enforcement Actions

The following Enforcement Center Actions can be used with Aggregated Security Findings queries:

* [Axonius - Push System Notification](/docs/push-system-notification)
* [Axonius - Send Email](/docs/send-email)
* [Email - Send per Asset](/docs/email-send-per-asset)
* [Axonius - Add Custom Data to Assets](/docs/add-custom-data)
* [Axonius - Remove Custom Data from Assets](/docs/remove-custom-data)
* [Manage Custom Enrichment - Enrich assets with CSV file](/docs/add-enrichment)
* [Axonius - Add Tag](/docs/add-remove-tag)
* [Axonius - Remove Tag](/docs/add-remove-tag)
* [Axonius - Calculate Risk Score](/docs/risk-score)
* [Cherwell - Create Incident](/docs/create-cherwell-incident)
* [Cherwell - Create Incident per Asset](/docs/create-cherwell-incident-per-entity)
* [Freshservice - Create Ticket](/docs/create-freshservice-ticket)
* [Freshservice - Create Ticket per Asset](/docs/create-fresh-service-ticket-per-entity)
* [Ivanti Security Controls - Patch Group](/docs/ivanti-patch-group)
* [Jira - Create Issue](/docs/create-jira-issue)
* [Jira - Create Issue per Asset](/docs/create-jira-issue-per-entity)
* [Jira Service Management - Create Issue](/docs/create-jira-service-desk-ticket)
* [Jira Service Management - Create Issue per Asset ](/docs/create-jira-service-desk-incident-per-entity)
* [Jira Service Management - Create Ticket](/docs/create-jira-service-desk-ticket)
* [Jira Service Management - Create Ticket per Asset](/docs/create-jira-service-desk-incident-per-entity)
* [Jira Service Management - Update Tickets](/docs/update-tickets-jira)
* [ServiceNow - Create Incident](/docs/create-servicenow-incident)
* [ServiceNow - Create Incident per Asset](/docs/create-servicenow-incident-per-entity)

For more details on creating and working with Enforcement Actions, see [Creating Enforcement Sets](/docs/create-ec-set).