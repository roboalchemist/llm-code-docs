# Source: https://docs.axonius.com/docs/vulnerabilities-repository.md

# Vulnerabilities Repository

The **Vulnerabilities Repository** page shows all of the vulnerabilities defined as CVEs by NVD whether discovered or not, and all vulnerabilities that were discovered on assets in the system whether CVEs or non-CVEs.   Both discovered and undiscovered vulnerabilities from the National Vulnerability Database (NVD) are accessible through the **Vulnerabilities Repository** from the Vulnerability Inventory. The **Vulnerabilities Repository**  enables you to explore and manage vulnerabilities even before they surface, fostering a proactive approach towards cybersecurity and ensuring readiness in the unpredictable landscape of threat detection. If a vulnerability  is discovered on your system it is automatically added to the Vulnerabilities inventory, along with all its tags, custom data and more.  It is also marked as **Detected** on this page.  You can then proactively track zero-day CVEs by connecting relevant automated actions in the **Enforcement Center** or **Findings** rules in advance.  In addition, when working with Exclusion rules, the  **Vulnerabilities Repository** shows you for each Vulnerability whether a rule exists and its status.

To view the **Vulnerabilities Repository**, go to the **Aggregated Security Findings** page and click **Repository**.

![NavigateToRepository](https://files.readme.io/46dd74174947b4ac0afd8b21ff73023df7c30753fd12c360321bfae31cb9bbcd-image.png)

Fields displayed on the **Vulnerabilities Repository** page are similar to those on the [Aggregated Security Findings page](/docs/vulnerabilities#vulnerabilities-fields) when relevant:

Not all of the fields are displayed by default. Use **Edit Columns** to add or remove columns. For more information, see [Setting Page Columns Displays](/docs/setting-page-columns-display).

**Adapter Connections**  -  The icon next to Adapter Connections shows the source from which the vulnerability is fetched. When a vulnerability is not discovered and is available only in the **Vulnerabilities Repository**, it will not have any adapters apart from enrichments such as  NVD, CISA and EPSS.

Click the arrow next to any of the fields to see which sources fetched which values.

**Detected** - This field indicates whether the vulnerability was detected on your system (the value is either **Detected**  or **Not Detected**.

<Callout icon="📘" theme="info">
  Note

  The **Detected** field is only relevant for vulnerabilities scanned and fetched actively by adapters. For vulnerabilities coming from enrichment sources, the status is **Not Detected** by default.
</Callout>

## Excluded Vulnerabilities

Information about excluded vulnerabilities is displayed on the Vulnerabilities Repository page. This page shows all known vulnerabilities, so it therefore shows excluded Vulnerabilities (which do not appear on the Vulnerabilities page once they are excluded).
For Excluded Vulnerabilities the following fields are displayed:

* **Exclusion Status** - The Exclusion Status
  * **Excluded** - This vulnerability is excluded
  * **Partially Excluded** -  A vulnerability that  is only excluded on specific devices.
  * **Pending** - A rule was set for the vulnerability, but it was not yet applied (rules are only applied when the Discovery Cycle runs)
* **Related Rules** - The name of the Rule(s), with a link to open the Rule Configuration Drawer.

### Managing Exclusions

You can manage exclusions from the Vulnerabilities Repository page.

1. Hover over a row, the **Manage Exclusion** button is displayed, or select one or more items and choose **Manage Exclusion**.
2. If the Vulnerability is already excluded, choose **Include Vulnerability**. A notification is displayed and from the next discovery cycle, the Vulnerability will be included again in the inventory. The Exclusion Status is changed to *Pending*.
3. To add a Vulnerability to a rule, choose **Exclude Vulnerability** the  **Create Exclusion Rule** dialog opens with the Vulnerability you selected filled in. You can assign a name to the Exclusion Rule and configure it as required. A notification is displayed and from the next discovery cycle, the Vulnerability will be excluded from the inventory according to the definitions in the rule. The Exclusion Status is changed to Pending.

## Creating Queries on Vulnerabilities Repository

You can use the **Vulnerabilities Repository** Query Wizard to create queries on the **Vulnerabilities Repository**. For instance to identify vulnerabilities of high priority on your system. You can also use these queries to present them in charts.
Refer to [Creating Queries with the Queries Wizard](/docs/query-wizard-and-query-filter) to learn more about creating queries.

You can use the **Custom Data** or **Tags** that you add to a Vulnerability in the **Vulnerabilities Repository**  in queries that you create on the **Vulnerabilities** page. They can then be used   as part of  Enforcement Actions or Rules to perform specific actions if the Vulnerability is then discovered or identified in your system using these Custom Data  or Tags.

## Adding Custom Data to a Vulnerability in the Repository

You can add custom fields to one or more vulnerabilities at the same time. Any custom fields you add here will remain on the vulnerability if it is later discovered on your system, and later remediated.
Select one or more applications and from the **Actions** menu choose **Add Custom Fields**.

Refer to [Working with Custom Data](/docs/working-with-custom-data) to learn about adding custom fields.

## Add Tags to Vulnerabilities

Use tags to assign context to the vulnerabilities  for granular filters and queries. Apply new or existing tags to the selected vulnerabilities.   Any  tags you add here will remain on the vulnerability if it is later discovered on your system, and later remediated.

Refer to [Working with Tags](/docs/working-with-tags) to learn about adding tags to applications.

Once you remediate a vulnerability and it is no longer part of your system, it will then only be displayed  on the  **Vulnerabilities Repository** table.

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).