# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-business-intelligence-components.md

# Manage Business Intelligence components

In Pentaho Data Catalog, under the **Business Intelligence** section, you can create (locally), import, organize, and maintain metadata for third-party Business Intelligence (BI) components. This section provides step-by-step guides for all available actions under the **Actions** menu, including how to add BI servers, folders, reports, charts, datasets, data flows, and so on.

Using these actions, you can manually build or extend the BI hierarchy, which is especially useful when simulating environments, onboarding external metadata, or customizing catalog content. You can also use options such as **Import** and **Export** to synchronize with external BI tools like Tableau server and Power BI servers or to migrate metadata across environments.

## Import and sync BI server (Tableau or Power BI) components into Data Catalog

In Data Catalog, you can import and sync metadata and components from a connected Tableau and Power BI server to populate the Business Intelligence hierarchy. Imported components can include sites or tenants, projects or workspaces or apps, reports or dashboards, report pages, charts or visuals, datasets, tables, fields, and dataflows.

Importing BI server components helps you to visualize and manage reporting structures within Data Catalog. It enables governance activities such as classification, tagging, and sensitivity labeling of BI components. Importing also ensures that the metadata stays up to date with the source system. This guide depicts the procedure to import BI server components.

Before you begin, make sure the connection between Data Catalog and your BI server is configured.

* For Tableau, see [Configure a Tableau server connection in Data Catalog](https://docs.pentaho.com/pdc-admin/ldc-advanced-configuration-ut_cp#configure-a-tableau-server-connection-in-data-catalog).
* For Power BI, see [Configure a Power BI server connection in Data Catalog](https://docs.pentaho.com/pdc-admin/ldc-advanced-configuration-ut_cp#configure-a-power-bi-service-connection-in-data-catalog).

Perform the following steps to import and sync Tableau server components into Data Catalog:

1. On the left navigation menu, click **Management**.

   The Manage Your Environment page opens.
2. In the **Synchronize** card, click **View Synchronize**.

   The Synchronize page opens with a list of configured external data sources.
3. Identify the Tableau or Power BI server from which you want to import or sync the metadata and components, and then click **Import**.

   The import worker starts the import process.

You have successfully imported and synced the metadata and components from the selected Tableau or Power BI server into Data Catalog. Once the job is complete, they are now visible in the **Business Intelligence** section. You can browse them in the hierarchy, Table view, or Galaxy view, and continue with governance tasks such as adding business terms, tags, and trust scores.

## Add a new BI server locally to Data Catalog

You can manually add a new Business Intelligence (BI) server locally to Data Catalog to simulate a BI environment, create a placeholder for metadata that will be imported later, or organize components into a custom hierarchy. It represents a Site for Tableau and a Tenant or Environment for Power BI. This top-level node lets you group projects or folders, datasets, reports, and visualizations under a single logical container.

{% hint style="info" %}
A locally created BI server exists only in Data Catalog. It does not create or modify a Site in Tableau or a Tenant or Environment in Power BI.
{% endhint %}

Perform the following steps to create a new BI server locally in Data Catalog:

1. In the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with the list of existing BI servers and their hierarchy.
2. On the Business Intelligence panel, click the **Actions** and select **Add New BI Server**.

   The Create BI Server dialog box appears.
3. In the **BI Server Name** field, enter a name for the BI server
4. Click **Create**.

You have successfully created a Business Intelligence (BI) server locally to Data Catalog. The new BI server appears in the Business Intelligence hierarchy. In the **Properties** section, you will see the status as **Draft**. This value can be changed by the Data Steward and Administrator.

You can now add BI folders, datasets, reports, data entities, and dataflows under this server to build a complete metadata structure.

## Add a new BI folder locally to Data Catalog

In Data Catalog, you can add a Business Intelligence (BI) folder locally under a BI server to group related datasets, reports, and visualizations. A BI folder represents a project within a BI server. It represents a Project for Tableau and a Workspace or App for Power BI. Creating folders locally helps you simulate real-world project structures, clarify ownership, and improve metadata management.

Perform the following steps to create a new BI folder locally to Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with a list of BI servers.
2. (Optional) Select the BI server where you want to add the folder.

   If a BI server is selected, it will be prepopulated in the **Parent** field of the dialog box.
3. Click the **Actions** menu and select **Add New BI Folder**.

   The Create BI Folder dialog box appears
4. In the **BI Folder Name** field, enter a name for the folder.
5. In the **Parent** field, select the BI server under which the folder should be created.
6. Click **Create**.

You have successfully created a Business Intelligence (BI) folder locally to Data Catalog. The new BI folder appears under the selected BI server in the Business Intelligence hierarchy.

You can now add datasets, reports, and other BI components locally to Data Catalog under this folder to build a structured metadata hierarchy.

## Add a new BI report locally to Data Catalog

In Data Catalog, you can create a Business Intelligence (BI) report locally under a BI folder to document custom reports, simulate a reporting structure, or prepare for future metadata imports. A BI report represents a Workbook for Tableau and a Report or Dashboard for Power BI.

Perform the following steps to create a new BI report locally to Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with the list of BI servers and folders.
2. (Optional) Select the BI folder under which you want to add the report.

   If a BI folder is selected, it will be prepopulated in the **Parent** field of the dialog box.
3. Click the **Actions** menu and select **Add New BI Report**.

   The Create BI Report dialog box appears.
4. In the **BI Report Name** field, enter a name for the report.
5. In the **Parent** field, select the BI folder under which the report should be created.
6. Click **Create**.

You have successfully created a Business Intelligence (BI) report locally to Data Catalog. The new BI report appears under the selected BI folder in the Business Intelligence hierarchy.

You can now add report pages, charts, and report attributes locally to Data Catalog under this report to represent its structure and content.

## Add a new BI report page locally to Data Catalog

In Data Catalog, you can create a Business Intelligence (BI) report page locally within a BI report to define the structure and layout of the report and to enable metadata enrichment at a finer level. A BI report page represents a Dashboard or Sheet for Tableau and a Report Page for Power BI.

Perform the following steps to create a new BI report page locally to Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with a list of BI components.
2. (Optional) Select the BI report under which you want to add the report page.

   If a BI report is selected, it will be prepopulated in the **Parent** field of the dialog box
3. Click the **Actions** menu and select **Add New BI Report Page**.

   The Create BI Report Page dialog box appears.
4. In the **BI Report Page Name** field, enter a name for the report page.
5. In the **Parent** field, select the BI report under which the report page should be created.
6. Click **Create**.

You have successfully created a Business Intelligence (BI) report page locally to Data Catalog. The new report page appears under the selected BI report in the Business Intelligence hierarchy.

You can now add charts and report attributes locally to Data Catalog under this report page to represent its visual content and data structure.

## Add a new BI chart locally to Data Catalog

In Data Catalog, you can create a Business Intelligence (BI) chart locally under a BI report or a BI report page to represent how data is visualized, such as a bar chart, pie chart, or line graph, typically found within a dashboard or report. A BI chart represents a View for Tableau and a Visual or Tile for Power BI.

Perform the following steps to create a new BI chart locally to Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with a list of BI components.
2. (Optional) Select the BI report or report page under which you want to add the chart.

   If a BI report is selected, it will be prepopulated in the **Parent** field of the dialog box
3. Click the **Actions** menu and select **Add New BI Chart**.

   The Create BI chart dialog box appears.
4. In the **BI Chart Name** field, enter a name for the chart.
5. In the **Parent** field, select the BI report or report page under which the chart should be created.
6. Click **Create**.

You have successfully created a Business Intelligence (BI) chart locally to Data Catalog. The new chart appears under the selected parent in the Business Intelligence hierarchy.

You can now add report attributes under this chart to document the fields or measures used in the visualization.

## Add a new BI report attribute locally to Data Catalog

In Data Catalog, you can create a Business Intelligence (BI) report attribute locally under a BI chart to define the data used in a specific visualization, such as a dimension, measure, or calculated value. A BI report attribute represents a Field used in a View for Tableau and visual element information, such as a field or measure for Power BI. Adding a report attribute helps you to document and govern individual data fields used in reports.

Perform the following steps to create a new BI report attribute in Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with a list of BI components.
2. (Optional) Select the BI chart under which you want to add the report attribute.

   If a BI chart is selected, it will be prepopulated in the **Parent** field of the dialog box
3. Click the **Actions** menu and select **Add New Report Attribute**.

   The Create BI Report Attribute dialog box appears.
4. In the **BI Report Attribute Name** field, enter a name for the report attribute.
5. In the **Parent** field, select the BI chart under which the report attribute should be created.
6. Click **Create**.

You have successfully created a Business Intelligence (BI) report attribute locally to Data Catalog. The new report attribute appears under the selected BI chart in the Business Intelligence hierarchy.

You can now assign business terms, apply sensitivity labels, or classify this attribute for governance and discovery.

## Add a new BI dataset locally to Data Catalog

In Data Catalog, you can create a Business Intelligence (BI) dataset locally under a BI folder to define and manage data sources that one or more reports use. A BI dataset represents a Published Data Source for Tableau and a Dataset for Power BI.

Perform the following steps to create a new BI dataset in Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with the list of BI components.
2. (Optional) Select the BI folder under which you want to add the dataset.

   If a BI folder is selected, it will be prepopulated in the **Parent** field of the dialog box.
3. Click the **Actions** menu and select **Add New BI Dataset**.

   The Create BI Dataset dialog box appears.
4. In the **BI Dataset Name** field, enter a name for the dataset.
5. In the **Parent** field, select the BI folder under which the dataset should be created.
6. Click **Create**.

You have successfully created a Business Intelligence (BI) dataset locally to Data Catalog. The new dataset appears under the selected BI folder in the Business Intelligence hierarchy.

You can now add data entities and data attributes under this dataset to document table-level and field-level metadata.

## Add a new BI data entity locally to Data Catalog

In Data Catalog, you can create a Business Intelligence (BI) data entity locally under a BI dataset to represent a logical or physical table within that dataset. It is typically used to organize and manage grouped data structures that support reporting or dashboard use cases. A BI data entity represents a Table or Logical Table for Tableau and a Table for Power BI. You can use data entities to define the table-level structure of a dataset, improve clarity, support lineage and governance, and classify downstream data elements such as columns and attributes.

Perform the following steps to create a new BI data entity in Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with the list of components.
2. (Optional) Select the BI dataset under which you want to add the data entity.

   If a BI dataset is selected, it will be prepopulated in the **Parent** field of the dialog box.
3. Click the **Actions** menu and select **Add New BI Data Entity**.

   The Create BI Data Entity dialog box appears.
4. In the **BI Dataset Data Entity** field, enter a name for the data entity.
5. In the **Parent** field, select the BI dataset under which the data entity should be created.
6. Click **Create**.

You have successfully created a Business Intelligence (BI) data entity locally to Data Catalog. The new data entity appears under the selected BI dataset in the Business Intelligence hierarchy.

You can now add data attributes under this data entity to define columns or fields that belong to this table.

## Add a new BI data attribute locally to Data Catalog

In Data Catalog, you can create a Business Intelligence (BI) data attribute locally under a BI data entity to represent a column or field within that table. It typically corresponds to a schema element in a table, such as customer ID, order date, or revenue. A BI data attribute represents a Column for Tableau and a Field for Power BI. You can use data attributes to document the structure of tabular data used in business reports, such as Customer ID, Order Date, or Revenue.

Perform the following steps to create a new BI data attribute in Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with the list of BI components.
2. (Optional) Select the BI data entity under which you want to add the data attribute.

   If a BI data entity is selected, it will be prepopulated in the **Parent** field of the dialog box.
3. Click the **Actions** menu and select **Add New BI Data Attribute**.

   The Create BI Data Entity dialog box appears.
4. In the **BI Dataset Data Attribute** field, enter a name for the data attribute.
5. In the **Parent** field, select the BI data entity under which the data attribute should be created.
6. Click **Create**.

You have successfully created a Business Intelligence (BI) data attribute locally to Data Catalog. The new attribute appears under the selected data entity in the Business Intelligence hierarchy.

You can now classify, tag, or associate this data attribute with glossary terms and apply sensitivity labels for governance.

## Add a new BI dataflow locally to Data Catalog

In Data Catalog, you can create a Business Intelligence (BI) dataflow locally to describe how data moves or is transformed between datasets, reports, or other components within a BI environment. A BI dataflow represents Workbook Relationships or a Prep Flow for Tableau and a Dataflow for Power BI. Perform the following steps to create a new BI dataflow in Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with the list of BI servers and folders.
2. (Optional) Select the BI folder under which you want to add the dataflow.

   If a BI folder is selected, it will be prepopulated in the **Parent** field of the dialog box.
3. Click the **Actions** menu and select **Add New BI Dataflow**.

   The Create BI Dataflow dialog box appears.
4. In the **BI Dataflow Name** field, enter a name for the dataflow.
5. In the **Parent** field, select the BI folder under which the dataflow should be created.
6. Click **Create**.

You have successfully created a Business Intelligence (BI) dataflow locally to Data Catalog. The new dataflow appears under the selected BI folder in the Business Intelligence hierarchy.

You can now use the Galaxy view to visualize relationships and use metadata tagging to enrich and trace data lineage across BI components. To learn more, see [Report Lineage](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-lineage/pdc-report-lineage) in [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/).

## Delete a BI server component

In Data Catalog, you can delete a Business Intelligence (BI) component, such as a BI server, folder, report, dataset, or dataflow, if it is no longer needed. Deleting unused or obsolete components helps keep the BI hierarchy clean, relevant, and easier to manage.

**CAUTION:** Once you delete a component, it cannot be recovered. Use caution when deleting a component, especially if it has nested children. Removing a parent will also remove all associated child components from the Business Intelligence hierarchy.

Perform the following steps to delete a BI server component in Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears with the BI server hierarchy.
2. Select the BI component you want to delete.
3. Click the **More** icon (three vertical dots) next to the component name and click **Delete**.

   A confirmation message appears.
4. Click **Confirm** to delete the component.

You have successfully deleted a BI server component in Data Catalog. However, it does not remove the component from the original source BI server.

## Import BI server components

In Data Catalog, you can import the Business Intelligence (BI) server components and bring the entire BI server structure into the **Business Intelligence** section from a file in one of the following file types:

* JSON Lines (Not JSON. See more here <https://jsonlines.org/>)
* Comma Separated Values (text/csv)

This includes importing BI server components such as a BI server, folder, report, dataset, dataflow, or more, without rebuilding BI server component hierarchies manually in each environment, which is time-consuming and error-prone. Whether the hierarchy was exported from another Data Catalog instance or generated externally, you can restore or replicate it in just a few steps, preserving the metadata relationships and integrity.

Perform the following steps to import the BI server components into the **Business Intelligence** hierarchy:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears.
2. Click **Actions** and select **Import**.

   The Import Assets dialog box appears.
3. Drag and drop your .jsonl or .csv file or browse and select the file you want to import and click **Submit**.

   Ensure the file format and structure align with the requirements of the Business Intelligence feature.

You have successfully imported the BI server components into the **Business Intelligence** hierarchy and you see the status value as Imported in the properties section.

You can also export the BI hierarchy for Data Catalog. For more information, see [Export BI server components](#export-bi-server-components).

## Export BI server components

In Data Catalog, you can export the complete structure and metadata of Business Intelligence (BI) components including server, folder, report, dataset, dataflow, or more and save them into a structured file, CSV and JSON, making it easy to backup, share, or migrate BI assets between environments or with other teams.

{% hint style="info" %}
Exporting content from Data Catalog does not change or remove anything in Tableau Server or in the Power BI service.
{% endhint %}

Perform the following steps to export Business Intelligence (BI) components from Data Catalog:

1. On the left navigation menu, click **Business Intelligence**.

   The Business Intelligence page appears.
2. Click **Actions** and select **Export**.

   The **Export Assets** dialog box appears.
3. Select what to export. Select individual components, or choose **Select all** to export every component in the list.\
   You can also use **Search** to find items. The counter (for example, **0/11**) shows how many are selected.
4. Select the file type (CSV or JSON) to which you want to export the **Business Intelligence** hierarchy, and then click **Submit**.

   The file containing the Business Intelligence (BI) server components in the selected format will be downloaded into the local folder.

You have successfully exported BI server components from Data Catalog Business Intelligence section.

You can also import BI components into Data Catalog Business Intelligence section. For more information, see [Import BI server components](#import-bi-server-components).
