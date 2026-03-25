# Source: https://docs.pentaho.com/pdc-use/pdc-lineage/pdc-data-lineage-cp.md

# Data lineage

In the Data Canvas, Data Catalog displays a visual representation of the lineage of the selected data, including its origin, flow, and transformations. Data lineage provides visibility into the data’s historical context and authenticity, which helps in understanding how data is manipulated and transformed across different processes and systems.

If you have Pentaho Data Integration (PDI), you can configure PDI to send lineage to Data Catalog. PDI sends lineage information to the configured Data Catalog API at key lineage events, such as the start or completion of a transformation. PDI and Data Catalog support the OpenLineage open framework for data lineage collection and analysis.

## Supported lineage steps

PDI sends lineage to Data Catalog only for the supported steps listed below.

### **Native steps**

These steps are implemented directly by the PDI platform and supported by the OpenLineage Plug-in:

* Text file input (local files, Minio/HCP S3)
* Text file output (local files, Minio/HCP S3) (\*)
* Table input (MySQL, PostgreSQL, Oracle, Vertica, SQL Server, Snowflake, Google Big Query)
* Table output (MySQL, PostgreSQL, Oracle, Vertica, SQL Server, Snowflake)

### **Non-native steps**

These steps are implemented by plugins that are loaded when PDI is initialized and consequently are supported by a plugin extension:

* S3 CSV input
* S3 file output (\*)
* Microsoft Excel Writer (\*)
* Microsoft Excel input

**Note:** The steps marked with (\*) allow splitting files based on content. If they are set with the option *Add filenames to result*, they will work without any limitation. Otherwise, PDI only supports naming without any customization (such as date, time, or partitions).

Data Catalog continuously runs an API that captures the lineage information from PDI. To set up the connection between PDI and Data Catalog, see **Configure Pentaho Data Integration to send lineage to Pentaho Data Catalog** in the **Administration Guide**.

## View lineage detail

You can see lineage information for a resource in the Data Canvas.

Perform the following steps to view more detail about the lineage.

1. In the Data Canvas, navigate to a resource to view and click the **Summary** tab if it is not already displayed.
2. On the **Lineage** pane, click **View Lineage**.

   ![Data Canvas with View Lineage button](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-6c12af2a50113799b6d149bba098dc7130284337%2FPDC%20Data%20Canvas%20lineage%20View%20Lineage%20button%20with%20blur.png?alt=media)

   The Lineage page opens. The large rectangles represent data sources, and the smaller rectangle within a rectangle represents the resource, such as a table, column, or field.

   ![Lineage page](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-3a99f69c3207e4b464c2b2b8a18a5b58b0328e66%2FPDC%20Lineage%20page%20with%20blur.png?alt=media)
3. Click the smaller rectangle for the resource.

   A side panel opens, with more detail about the resource, such as its **Sensitivity**.

   ![Lineage page with side panel and resource selected](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-e72e3ad482f192fe78474ccdc05cc0679711b34f%2FPDC%20Lineage%20side%20panel%20with%20box.png?alt=media)

   On the Lineage page, you can also use the following actions to explore the lineage:

   <table><thead><tr><th width="164.44439697265625">Field or Icon</th><th>Action</th></tr></thead><tbody><tr><td><strong>Find in graph</strong></td><td>Search the lineage graph</td></tr><tr><td><strong>Upstream</strong></td><td>Select a number corresponding to the number of hops upstream from the resource that you want to view</td></tr><tr><td><strong>Downstream</strong></td><td>Select a number corresponding to the number of hops downstream from the resource that you want to view</td></tr><tr><td><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-e5ae088db1a94be0885b6e686c88fb41192cd101%2FPDC%20Lineage%20zoom%20out%20icon%20(inline).png?alt=media" alt="A minus symbol"></td><td>Zoom out</td></tr><tr><td><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-541784258b919995239fa3bffe1bed10b498404f%2FPDC%20Lineage%20reset%20icon%20(inline).png?alt=media" alt="A square with only the corners shown"></td><td>Reset the lineage graph size</td></tr><tr><td><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-d4815f8c4d971c2c3e6b022497e9be6a20d6ee2f%2FPDC%20Lineage%20zoom%20in%20icon%20(inline).png?alt=media" alt="A plus symbol"></td><td>Zoom in</td></tr><tr><td><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-360145e942fdda803ebc12e0aa7ae4b823435777%2FPDC%20lineage%20job%20icon%20(inline).png?alt=media" alt=""></td><td>Display the action that was performed on the data</td></tr><tr><td><strong>Add Lineage</strong></td><td>Manually add a resource to the lineage graph. See <a href="broken-reference">Add manual lineage</a>.</td></tr></tbody></table>

## Add manual lineage

If you know the source of a specific resource, and the source does not appear on the lineage graph for the resource, you can add it to the lineage graph. Adding manual lineage involves selecting a Target resource and adding another resource to it, which becomes the Source resource.

Use the following steps to add manual lineage.

1. If you are not already viewing resource data in the Data Canvas, navigate to a resource in the Data Canvas and from the **Summary** tab, click **View Lineage**.

   The Lineage page opens.
2. In the lineage graph, click a resource to use as the Target resource.

   ![Lineage page with side panel and resource selected](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-e72e3ad482f192fe78474ccdc05cc0679711b34f%2FPDC%20Lineage%20side%20panel%20with%20box.png?alt=media)
3. Click **Add Lineage**.

   The **Add Lineage** window opens.

   ![Add Lineage window on Lineage page](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-dce32574888a770fcb83c5f4b67fe0e1808aa1d0%2FPDC%20Lineage%20page%20Add%20Lineage%20window.png?alt=media)
4. Navigate to a resource to add to the lineage and select its checkbox.

   The **Add** button displays the number of resources that are selected.

   This resource will be added as the Source of the Target resource.
5. Click **Add**.

The resource is added to the lineage graph.
