# Source: https://docs.pentaho.com/pba-ctools/create-a-dashboard-that-uses-a-streaming-service-as-a-data-source.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/create-a-dashboard-that-uses-a-streaming-service-as-a-data-source.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/create-a-dashboard-that-uses-a-streaming-service-as-a-data-source.md

# Create a dashboard that uses a streaming service as a data source

With the Community Dashboard Editor (CDE), you can create a dashboard that uses a streaming service as its data source. First, define the streaming data service in Pentaho Data Integration, then create a dashboard in CDE that uses the streaming service as its data source.

## Prerequisites

In Pentaho Data Integration, define a streaming Pentaho Data Service by building a transformation that has a streaming step, such as MQTT Producer or Generate Rows transformation steps. For best results with Generate Rows, activate the option to keep generating rows. Perform the following steps to define a streaming data service:

1. Open Pentaho Data Integration and connect to the Pentaho Repository.
2. Create a streaming transformation and **Save** it to the Repository.
3. In the transformation's streaming step, right click, select **Data Services**, then **New**.
4. Create a data service with a unique **Service Name** (for example: `streaming_dataservice`) and set the **Data Service Type** to **Streaming**.

   **Note:** Each streaming data service in the Pentaho Repository must have a unique name.
5. **Save** the transformation again.

The data service you defined is now available for use in CDE as a data source for a dashboard.

## Create a streaming dashboard

To create a CDE dashboard with a data source from a Pentaho Data Integration streaming Data Service, perform the following steps:

1. In Pentaho User Console, create a new CDE dashboard. For instructions, see [Create and save a new dashboard](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide/create-your-first-cde-dashboard#create-and-save-a-new-dashboard).
2. From the Data Sources perspective, add the data source type streaming over dataservices (found in the **DATASERVICES Queries** list).
3. Set the parameters as follows:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>Name</strong></td><td>Specify the name you want to assign to this data source. For example: <code>mydatasource</code></td></tr><tr><td><strong>Streaming Data Service Name</strong></td><td>Specify the same <strong>Data Services</strong> name you created in the <a href="#prerequisites">Prerequisites</a> section above. For example: <code>streaming_dataservice</code></td></tr><tr><td><strong>Query</strong></td><td><p>In <strong>SELECT * FROM dataservicename</strong> replace <strong>dataservicename</strong> with the identical data service name you entered in the <strong>Streaming Data Service Name</strong> parameter above. For example:</p><pre class="language-sql"><code class="lang-sql">SELECT * FROM "streaming_dataservice"
</code></pre></td></tr><tr><td><strong>Window Mode</strong></td><td>Select <code>Row Based</code> to indicate the window mode to use when this data source is used, which can be either row-based or time-based.</td></tr><tr><td><strong>Window Size</strong></td><td>Specify <code>50</code> to indicate the number of rows that a window will have (row-based), or the time frame (time-based) for which you want to capture new rows in the window.</td></tr><tr><td><strong>Window Every</strong></td><td>Specify <code>1</code> to indicate the rate at which each streaming data window is generated, either the number of rows (row-based) or the time in milliseconds (time-based).</td></tr><tr><td><strong>Window Limit</strong></td><td>Specify <code>0</code> to indicate the maximum number of rows (row-based) or milliseconds (time-based) which will be used to wait for a new window to be generated.</td></tr><tr><td><strong>Component Refresh Period</strong></td><td>Specify <code>2</code> to indicate the amount of time in seconds used by the component to refresh.</td></tr></tbody></table>

4\. Create or apply an existing layout to the dashboard. For instructions, see [Create the layout for the dashboard](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide/create-your-first-cde-dashboard#create-the-layout-for-the-dashboard).&#x20;

5. Add a table component to the layout and enter the following properties:

   | Parameter                              | Value                                                                                                        |
   | -------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
   | **Datasource**                         | Specify the same data source name you created for the **Name** parameter above. For example: mydatasource    |
   | **Don't Block the UI While Executing** | Select `True` to indicate that the user interface is not blocked while loading and executing this component. |
   | **Clears Before Pre Execution**        | Select `False` to indicate that `Clear` is not executed before the component's execution phase.              |
6. Add a **Community Charting Components (CCC) Line Chart** component to the layout.

   For instructions, see [Add a line chart](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide/create-your-first-cde-dashboard#add-a-line-chart). Give the **Line Chart** component the properties listed in the table below. Omit the optional parameters if you do not need the Tick requirement.

   | Parameter                                        | Value                                                                                                         |
   | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
   | **Datasource**                                   | Specify the same data source name you created for the **Name** parameter above. For example: mydatasource     |
   | **Don't Block the UI While Executing**           | Select `True` to indicate that the UI is not blocked while loading and executing this dashboard.              |
   | **Clears Before Pre Execution**                  | Select `False` to indicate that `Clear` is not executed before the component's execution phase.               |
   | **Animate**                                      | Select `False` to indicate that the chart should not show an entry animation every time it is fully rendered. |
   | **Render Mode (Optional)**                       | Select `Partial - Same Metadata` to indicate the type of render to use when updating the component.           |
   | **Sliding Window (Optional)**                    | Select `True` to indicate the existence of a sliding window.                                                  |
   | **Base Axis Preserve Tick Alignment (Optional)** | Select `True` to re-use the horizontal axis ticks for continuity.                                             |
   | **New data adds to existing data (Optional)**    | Select `False` to indicate that new data replaces the existing data in the visualization.                     |
7. To view and test your streaming dashboard, click the **Preview Your Dashboard** icon located in the **CDE Perspectives** toolbar.

   The Preview window displays.
