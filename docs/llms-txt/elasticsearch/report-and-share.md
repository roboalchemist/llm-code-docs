# Source: https://www.elastic.co/docs/explore-analyze/report-and-share

﻿---
title: Reporting and sharing
description: Kibana provides you with several options to share Discover sessions, Dashboards, Visualize Library visualizations, and Canvas workpads. These sharing...
url: https://www.elastic.co/docs/explore-analyze/report-and-share
products:
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Reporting and sharing
Kibana provides you with several options to share **Discover** sessions, **Dashboards**, **Visualize Library** visualizations, and **Canvas** workpads. These sharing options are available from the icons **Share** `share` and **Export** `download` in the toolbar.

## Permissions

To be able to share objects or generate reports, you must have a role that allows these actions on the specific Elasticsearch indices and Kibana applications containing the data that you want to share. Check [Configuring reporting](https://www.elastic.co/docs/deploy-manage/kibana-reporting-configuration) for more information.

## Share with a direct link

You can share direct links to saved Discover sessions, dashboards, and visualizations. To do that, look for the `share` **Share** icon.
<applies-to>Elastic Stack: Generally available since 9.1</applies-to> When applicable, you can choose to share the object using a relative or an absolute time range:
- **Relative time range**: The link shows current data. For example, if you share a "Last 7 days" view, users will see the most recent 7 days when they open the link.
- **Absolute time range** (default): The link shows a fixed time period. For example, if you share a "Last 7 days" view on January 7, 2025, the link will always show that exact week of January 1-7, 2025, regardless of when users open the link.

<tip>
  When sharing an object with unsaved changes, you get a temporary link that might break in the future, for example in case of upgrade. Save the object to get a permanent link instead.
</tip>

To access the object shared with the link, users need to authenticate.
Anonymous users can also access the link if you have configured [Anonymous authentication](/docs/deploy-manage/users-roles/cluster-or-deployment-auth/kibana-authentication#anonymous-authentication) and your anonymous service account has privileges to access what you want to share.

## Export as a file

<note>
  For more information on how to configure reporting in Kibana, refer to [Configure reporting in Kibana](https://www.elastic.co/docs/deploy-manage/kibana-reporting-configuration).
</note>

Create and download PDF, PNG, or CSV reports of saved Discover sessions, dashboards, visualizations, and workpads.
- **PDF** <applies-to>Elastic Cloud Serverless: Unavailable</applies-to> — Generate and download PDF files of dashboards, visualizations, and **Canvas** workpads. PDF reports are a [subscription feature](https://www.elastic.co/subscriptions).
- **PNG** <applies-to>Elastic Cloud Serverless: Unavailable</applies-to> — Generate and download PNG files of dashboards and visualizations. PNG reports are a [subscription feature](https://www.elastic.co/subscriptions).
- **CSV Reports** — Generate CSV reports of saved Discover sessions. [Certain limitations apply](#csv-limitations).
- **CSV Download** — Generate and download CSV files of **Lens** visualizations.
- **Download as JSON** — Generate and download JSON files of **Canvas** workpads.


The layout and size of the report depends on what you are sharing. For saved Discover sessions, dashboards, and visualizations, the layout depends on the size of the panels. For workpads, the layout depends on the size of the worksheet dimensions.
To change the output size, change the size of the browser, which resizes the shareable container before the report generates. It might take some trial and error before you’re satisfied.
In the following dashboard, the shareable container is highlighted:
![Shareable Container](https://www.elastic.co/docs/explore-analyze/images/kibana-shareable-container.png)

1. Open the saved Discover session, dashboard, visualization, or **Canvas** workpad you want to share.
2. Choose a file type for the report.
   - <applies-to>Elastic Stack: Generally available since 9.1</applies-to> From the toolbar, click the `download` **Export** icon, then choose a file type.
- <applies-to>Elastic Stack: Generally available in 9.0</applies-to> From the toolbar, click **Share** > **Export** tab, then choose a file type. Note that when you create a dashboard report that includes a data table or Discover session, the PDF includes only the visible data.
   <note>
   When you create a dashboard report that includes a data table or Discover session, the PDF includes only the visible data.
   </note>
   <tip>
   Tips for generating PDF reports:
   - If you are creating dashboard PDFs, select **For printing** to create printer-friendly PDFs with multiple A4 portrait pages and two visualizations per page.
   - If you are creating workpad PDFs, select **Full page layout** to create PDFs without margins that surround the workpad.
   </tip>
3. Click the button that generates or exports the report. A message appears, indicating that the report is in the export queue.
   <note>
   To generate the report from outside of Kibana or from Watcher, use the POST URL, then submit an HTTP `POST` request using a script or Watcher.<applies-to>Elastic Stack: Generally available since 9.1</applies-to> You can schedule a recurring task in Kibana that generates reports on a repeating basis. Refer to [Automatically generate reports](https://www.elastic.co/docs/explore-analyze/report-and-share/automating-report-generation) to learn more.
   </note>

Go to the **Reporting** page to access all of your reports. To find the page, navigate to **Stack Management > Alerts and Insights > Reporting** in the main menu, or use the [global search field](https://www.elastic.co/docs/explore-analyze/find-and-organize/find-apps-and-objects).
<note>
  In self-managed installations and Elastic Cloud Hosted deployments, reports are stored in Elasticsearch and managed by the `kibana-reporting` index lifecycle management (ILM) policy. By default, the policy stores reports forever. To learn more about ILM policies, refer to the Elasticsearch [ILM documentation](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management).
</note>


### CSV report limitations

We recommend using CSV reports to export moderate amounts of data only. The feature enables analysis of data in external tools, but it is not intended for bulk export or to backup Elasticsearch data. Report timeout and incomplete data issues are likely if you are exporting data where:
- More than 250 MB of data is being exported
- Data is stored on slow storage tiers
- Any shard needed for the search is unavailable
- Network latency between nodes is high
- Cross-cluster search is used
- ES|QL is used and result row count exceeds the limits of ES|QL queries

To work around the limitations, use filters to create multiple smaller reports, or extract the data you need directly with the Elasticsearch APIs.
For more information on using Elasticsearch APIs directly, see [Scroll API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-scroll), [Point in time API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-open-point-in-time), [ES|QL](https://www.elastic.co/docs/reference/query-languages/esql/esql-rest) or [SQL](https://www.elastic.co/docs/reference/query-languages/sql/sql-rest-format#_csv) with CSV response data format. We recommend that you use an official Elastic language client: details for each programming language library that Elastic provides are in the [Elasticsearch Client documentation](https://www.elastic.co/docs/reference/elasticsearch-clients).
[Reporting parameters](https://www.elastic.co/docs/reference/kibana/configuration-reference/reporting-settings) can be adjusted to overcome some of these limiting scenarios. Results are dependent on data size, availability, and latency factors and are not guaranteed.

### PNG/PDF report limitations

<applies-to>
  - Elastic Cloud Serverless: Unavailable
</applies-to>

We recommend using PNG/PDF reports to export moderate amounts of data only. The feature enables a high-level export capability, but it’s not intended for bulk export. If you need to export several pages of image data, consider using multiple report jobs to export a small number of pages at a time. If the screenshot of exported dashboard contains a large number of pixels, consider splitting the large dashboard into smaller artifacts to use less memory and CPU resources.
For the most reliable configuration of PDF/PNG reporting features, consider installing Kibana using [Docker](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana-with-docker) or using [Elastic Cloud](https://cloud.elastic.co).

## Create JSON files

Create and share JSON files for workpads.
1. Go to **Canvas**.
2. Open the workpad you want to share.
3. From the toolbar, click `download` **Export**, then select **JSON**.


## Embed outside of Kibana

<applies-to>
  - Elastic Cloud Serverless: Unavailable
</applies-to>

- <applies-to>Elastic Stack: Beta</applies-to> **Share on a website** — Download and securely share **Canvas** workpads on any website.
- **Embed code** — Embed fully interactive dashboards as an iframe on web pages.

<note>
  For Elastic Cloud Hosted deployments, Kibana instances require a minimum of 2GB RAM to generate PDF or PNG reports. To change Kibana sizing, [edit the deployment](https://cloud.elastic.co?page=docs&placement=docs-body).
</note>


### Share workpads on a website

<applies-to>
  - Elastic Cloud Serverless: Unavailable
  - Elastic Stack: Beta
</applies-to>

Create and securely share static **Canvas** workpads on a website. To customize the behavior of the workpad on your website, you can choose to autoplay the pages or hide the workpad toolbar.
1. Go to **Canvas**.
2. Open the workpad you want to share.
3. Click **Share > Share on a website**.
4. To customize the workpad behavior to autoplay the pages or hide the toolbar, use the inline parameters.
   To make sure that your data remains secure, the data in the JSON file is not connected to Kibana. **Canvas** does not display elements that manipulate the data on the workpad.
   <note>
   Shareable workpads encode the current state of the workpad in a JSON file. When you make changes to the workpad, the changes do not appear in the shareable workpad on your website.
   </note>
5. To change the settings, click the settings icon, then choose the settings you want to use.


### Embed code

<applies-to>
  - Elastic Cloud Serverless: Unavailable
  - Elastic Stack: Generally available
</applies-to>

Display your dashboards on an internal company website or personal web page with an iframe. To embed other Kibana objects, manually create the HTML code.
For information about granting access to embedded dashboards, refer to [Authentication](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/user-authentication).
1. Open the dashboard you want to share.
2. Click **Share > Embed code**.
3. Specify which parts of the dashboard you want to include: Top menu, query, time filter, and filter bar.
4. Click **Copy embed code**.