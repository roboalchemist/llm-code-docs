# Source: https://docs.pentaho.com/pdc-use/pdc-lineage/pdc-report-lineage.md

# Report lineage

The report lineage feature in Data Catalog provides a graphical view of how a report is constructed by visualizing its relationship to underlying data sources, datasets, and intermediate data entities. It helps users understand the complete data flow used to build a report, from raw tables and files, through transformations, to the final report and its visualizations.

**Note:** The report lineage is available only for Report and Report Page components of connected Business Intelligence (BI) servers, such as Tableau, and it can be accessed in the **Business Intelligence** section of Data Catalog. To learn more about Business Intelligence and its components, see [Business Intelligence](https://docs.pentaho.com/pdc-use/pdc-business-intelligence).

![](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-eddd29c452a335f51327f3aacb3150953a6ffdca%2FReport%20Lineage%3DGUID-993E711C-B640-4E34-8B10-3FFA2554E539%3D1%3Den%3DLow.png?alt=media)

By showing upstream and downstream connections of a report component, the lineage graph enhances data transparency, trust, and auditability. With this, you can trace the origin of data displayed in a report and assess the impact of changes to source data. In addition to automatically generated lineage, you can also manually add lineage. This is useful when:

* Metadata ingestion is incomplete or unsupported
* Data transformations occur outside of connected systems (such as in custom scripts or spreadsheets)
* You want to simulate lineage during development or validation

Manually adding lineage helps complete the data flow picture, improves traceability, and supports compliance and impact analysis even for disconnected or external processes.

## Key benefits of report lineage

The following are the key benefits of the report lineage. It:

* Provides a clear and visual representation of the report structure and its data lineage.
* Helps verify data accuracy and report reliability by tracing the source of the data.
* Supports compliance and governance initiatives (for example, GDPR, IFRS, CCPA) by showing how Personally Identifiable Information (PII) flows through reports.
* Enables impact analysis by identifying downstream components affected by dataset or schema changes.

The Report Lineage graph includes relationships between various components, such as:

* **Table/File** (source systems or file-based inputs)
* **Data Entity** (logical data layer within Data Catalog)
* **Dataset** (aggregated or transformed data)
* **Report** (such as Tableau Workbook)
* **Chart** (individual visual components of a report)

By understanding how these components are interconnected, you can make more informed decisions, ensure governance compliance, and resolve issues more efficiently.

## Prerequisites for report lineage

To view and explore report lineage in Data Catalog, make sure the following conditions are met:

* You must have the necessary access permissions in Data Catalog to configure, import, and view report components. For more information, see [User roles and permissions in Data Catalog](https://docs.pentaho.com/pdc-use/pdc-user-roles-and-permissions).
* You must configure and connect to a supported Business Intelligence (BI) server, such as Tableau server, in Data Catalog. For detailed steps, see the **Configure a Tableau server connection in Data Catalog** topic under the **Advanced Configurations** section in the **Administer Pentaho Data Catalog** document.
* After you configure the BI server connection, import metadata to enable report lineage. For detailed steps, see the **Import and sync Tableau server components into Data Catalog** topic under the **Manage Business Intelligence components** section in the **Administer Pentaho Data Catalog** document.

## How the report lineage works

Report lineage in Data Catalog visually maps the relationship between a report and the data used to generate it. The report lineage graph illustrates how data flows from source systems through various stages, including datasets and transformations, before being presented in a report or chart.

The report lineage graph uses a node-based layout, where each node represents a component involved in report generation. Arrows between nodes represent data flow, helping users trace the origin and usage of data across the reporting pipeline.

![PDC workflow of report lineage](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-da6240ae6043127a3e44ddb8557fa04e3920c743%2FPDC%20Workflow%20of%20Report%20Lineage.png?alt=media)

## Components in the report lineage graph

The following table shows the components of the report lineage graph:

<table><thead><tr><th width="151.77777099609375">Component</th><th>Description</th></tr></thead><tbody><tr><td>Table/File</td><td>Represents raw data sources, such as tables in databases or files in a file system.</td></tr><tr><td>Data Entity</td><td>Represents structured logical groupings of data imported into Data Catalog.</td></tr><tr><td>Dataset</td><td>Represents curated or transformed data prepared for reporting or analysis.</td></tr><tr><td>Report</td><td>Represents the main reporting object, such as a Tableau Workbook or Power BI Report.</td></tr><tr><td>Chart</td><td>Represents a visual element, such as a graph or table, within a report.</td></tr></tbody></table>

Each component appears with an icon that reflects its type, and the graph supports allowed predecessor relationships between components.

* **Example flow**

  A typical lineage path might look like this:

  ![PDC Lineage path](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-070c6c85094687c23a8590b20a4d9f5db542355c%2FPDC%20Flow%20components%20of%20Report%20Lineage.png?alt=media)

  For example:

  * A file named Customer.csv and a PostgreSQL table named Sales\_Orders are both imported.
  * These are grouped into a data entity called Orders and Returns.
  * The data entity feeds into a dataset named QuarterlySales.
  * The dataset is used to build a report named Q1\_Sales\_Report.
  * The report contains a chart named Top 10 Products\
    This graph helps users understand:
  * Which data sources feed into a report
  * What transformations or intermediate steps are involved
  * Where the report data is ultimately displayed

The graph supports both upstream (data origin) and downstream (data usage) navigation. You can expand or collapse nodes to explore specific parts of the lineage.

## View report lineage

You can view the report lineage for any report component that has been imported from a supported Business Intelligence (BI) server, such as Tableau. The lineage view is available only for report and report page components in the Business Intelligence section of Data Catalog.

Perform the following steps to view the report lineage

1. In the left navigation menu, select **Business Intelligence**.

   The Business Intelligence page appears.
2. Select the BI server (for example, Tableau server) where your reports are hosted.
3. Go to a report component within the hierarchy and select the report you want to explore.

   The Summary page appears.
4. On the Lineage pane, click **View Lineage**.

   ![PDC View Linage in Linage pane](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-833c0d6b0f8e396a3ffa97c7e5bf1db9aa07b870%2FPDC%20View%20Lineage.png?alt=media)

   The lineage graph appears, showing upstream and downstream relationships between the report and other components, such as datasets, data entities, tables, and charts.

   ![PDC Lineage](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-0c19946f7342500dee493bff3846355dba5a0267%2FPDC%20Lineage.png?alt=media)
5. Click the smaller rectangle for the resource.

   A side panel opens, providing more details about the resource, including job, actions, and transformations.

   ![PDC details of a particular lineage](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-0f05391d5661eb439529efd988532f57aa2160ff%2FPDC%20Details%20of%20Lineage.png?alt=media)

   On the Lineage page, you can also use the following actions to explore the lineage:

<table data-header-hidden><thead><tr><th width="168.4444580078125" align="center">Field or Icon</th><th>Action</th></tr></thead><tbody><tr><td align="center"><strong>Find in graph</strong></td><td>Search the lineage graph</td></tr><tr><td align="center"><strong>Upstream</strong></td><td>Select a number corresponding to the number of hops upstream from the resource that you want to view</td></tr><tr><td align="center"><strong>Downstream</strong></td><td>Select a number corresponding to the number of hops downstream from the resource that you want to view</td></tr><tr><td align="center"><p><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-e5ae088db1a94be0885b6e686c88fb41192cd101%2FPDC%20Lineage%20zoom%20out%20icon%20(inline).png?alt=media" alt="A minus symbol"></p></td><td>Zoom out</td></tr><tr><td align="center"><p><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-541784258b919995239fa3bffe1bed10b498404f%2FPDC%20Lineage%20reset%20icon%20(inline).png?alt=media" alt="A square with only the corners shown"></p></td><td>Reset the lineage graph size</td></tr><tr><td align="center"><p><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-d4815f8c4d971c2c3e6b022497e9be6a20d6ee2f%2FPDC%20Lineage%20zoom%20in%20icon%20(inline).png?alt=media" alt="A plus symbol"></p></td><td>Zoom in</td></tr><tr><td align="center"><p><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-dd6f9c9c8745533e52276715dc01a56a8abf1283%2FNode%20icon.png?alt=media" alt="PDC Node icon" width="21"></p></td><td>Display the action that was performed on the data</td></tr><tr><td align="center"><strong>Add Lineage</strong></td><td>Manually add a resource to the lineage graph. See <a href="broken-reference">Add manual lineage</a>.</td></tr></tbody></table>

## Add manual lineage to BI report components

In the Data Catalog, you can add manual lineage to BI reports in the Business Intelligence section, building a complete view of the data flow, even when the source or intermediate metadata is missing or unsupported. For example, if a report is created from an offline Excel file or a custom data transformation, you can manually link that file or dataset to the report in Data Catalog, so the lineage view reflects the actual data path. Manual lineage enhances trust, improves impact analysis, and supports governance by connecting disconnected components in your reporting pipeline.

**Note:** Adding manual lineage creates a visual and logical link in Data Catalog but does not affect the report content in the BI tool.

Perform the following steps to add manual lineage for BI reports in Data Catalog:

1. In the left navigation menu, select **Business Intelligence**.

   The Business Intelligence page appears with the list of existing BI servers and their hierarchy.
2. Go to a report or report page component for which you want to add a manual lineage.
3. On the component’s **Summary** tab, in the Lineage pane, click **View Lineage**.

   The Lineage page opens.
4. In the lineage graph, click the resource you want to add lineage to.

   The Details panel appears on the right side.

   ![PDC Manual Lineage Details panel](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-8594e8d4e74a5c9eea484c2956a124fd32ce807b%2FPDC%20Manual%20Lineage%20details.png?alt=media)
5. In the Details panel, click **Add Lineage**.

   The Add Lineage dialog box appears.

   ![PDC Add Lineage](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-64e698e29976c885c6985c09ffe20b2ea497455d%2FPDC%20Add%20Lineage_BI%20reports.png?alt=media)
6. In the Add Lineage dialog box, do one of the following:
   * To link a data asset from the **Data Canvas**, select the **Data Canvas** tab and choose the source item.
   * To link to another BI component, select the BI Reports tab and browse the BI server folders.
7. Click **Add**.

You have successfully added a manual lineage to the resource, and the new lineage connection is now visible in the graph. You can repeat these steps to add multiple manual connections to represent complex data flows.

## Remove manual lineage from BI report components

If a manually added lineage connection is no longer valid or was created by mistake, you can remove it from the Lineage view. This ensures that the lineage graph remains accurate and reflects the actual data flow used to build a report.

**Note:**

* You can only remove lineage connections that were manually added. Lineage generated automatically by metadata import cannot be removed.
* Removing a manual lineage link only removes the visual relationship from Data Catalog. It does not delete the source or target data assets.

Perform the following steps to remove manual lineage for BI reports in Data Catalog:

1. In the left navigation menu, select **Business Intelligence**.

   The Business Intelligence page appears with the list of existing BI servers and their hierarchy.
2. Navigate to a report or report page component for which you want to remove the lineage.
3. On the component’s **Summary** tab, in the Lineage pane, click **View Lineage**.

   The Lineage page opens.
4. In the lineage graph, click the **Node** (data asset or report) that is part of the manually added lineage you want to remove.

   The Details panel appears.
5. In the Details panel, under **Actions**, click **Remove**.
6. In the confirmation dialog box, click **Remove** again to delete the manual lineage connection.

You have successfully removed the manual lineage from the selected resource. The removed connection no longer appears in the lineage graph. You can repeat these steps to clean up or revise additional manual lineage relationships as needed.
