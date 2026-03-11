# Source: https://docs.axonius.com/docs/configuring-cache-and-performance.md

# Configuring Cache and Performance

**To configure cache and performance settings:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **Data**, and select **Cache and Performance**.

## Reports Generation Schedule

* **Enable reports generation schedule** *(required, default: switched off)* - Toggle on to enable custom scheduling for the generation of reports PDF files.
  * If switched on, specify the number of hours between report PDF file generation. The reports PDF files are also generated at the end of each discovery cycle.

  * If switched off, reports PDF files are generated at the end of the discovery cycle.

## Aggregated Security Findings Settings

* **Enable base device query caching in the Aggregated Security Findings table** *(default: false)* - Select this option to enable a query optimization feature which may improve performance on the Aggregated Security Findings table.
* **Don’t split source vulnerabilities into CVEs** - Select this option to present each source vulnerability as a vulnerability of its own, represented as a single row on the Aggregated Security Findings page instead of being broken down into each CVE included in the vulnerability. When you select this setting no CVE enhancement is done, that is, NVD and CISA enrichment are not performed and static analysis does not run. For example, for Tenable this  presents each Tenable plugin as a vulnerability of its own, represented as a single row on the Aggregated Security Findings page instead of being broken down into each CVE in the plugin. For Qualys a single finding that contains more than one CVE is presented as a single finding.

## Software Module Settings

* **Enable base device query caching in the Software Management module** *(default: false)* - Select this option to enable a query optimization feature which may improve performance on the Software Management Module.

## Cache Settings

* **Enable caching on recently used queries** *(required, default: switched off)* - Toggle on to cache recently used queries.
  * If switched on, each executed query is cached for the time specified in the **Cache Time-to-Live (TTL) in minutes** field. This means that a query that was recently executed is not executed again. The results for that query are loaded from the previous query execution. Note that when you click on a column and sort it, then the query is recalculated.
  * If switched off, apart from the last executed query, queries are not  cached, and the query results are not retrieved from the cache.
  * When **Enable caching on recently used queries** is switched on, the **Perform a query every keypress** settings checkbox (in GUI->UI system settings) is disabled.
  * When **Enable caching on recently used queries** is switched on, the dashboard charts that use this query load the cached query, and do not run a new query.

* **Cache Time-to-Live (TTL) in minutes** *(required, default: 60)* - Configure the time for which the cache of each query will be kept. Once this time has passed, the query executes again and does not load previous results.

## Refresh Rate

* **Auto-refresh rate** *(default: 60 seconds)* - Dictates the  auto refresh rate in seconds of Axonius tables. Auto refresh forces the tables to update the presented data.(note that this does not apply to charts)