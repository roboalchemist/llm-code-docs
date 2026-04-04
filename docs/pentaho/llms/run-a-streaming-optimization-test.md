# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/run-a-streaming-optimization-test.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/run-a-streaming-optimization-test.md

# Run a streaming optimization test

To test streaming data, the records of the stream must be partitioned into windows (batching) for processing. How the records are batched depends on the window mode you choose. A window can be time-based or row-based. A time-based window is created within a specified interval of time. A row-based window is created per the specified number of rows collected for processing.

To run an optimization test on a streaming data service, perform the following steps:

1. Verify **Data Service Type** is set to **Streaming**.
2. Perform one of the following actions to open the Test Data Service window:
   * In the Data Service window, click **Test Data Service**.
   * In the **View** tab of the PDI client **Explore** pane, click **Data Services**. Right-click the name of the data service you want to test, then select **Test**.
   * Right-click the step in the transformation (identified by the data service badge) that attaches to the data service, then select **Data Services** > **Test**.
3. Select the window mode (**Time Based** or **Row Based**) used for processing during the test, and specify the times (in milliseconds) or number of rows depending on the window mode for the following settings:
   * **Window Size**: Defines the number of rows that a window will have (row-based), or the time frame, in milliseconds, for capturing new rows to a window (time-based).
   * **Every**: Sets the number of rows (row-based), or milliseconds (time-based) that should elapse before creating a new window.
   * **Limit**: Sets the maximum number of milliseconds (row-based) or rows (time-based) to wait for a new window to be generated.
4. If needed, adjust the following optional settings:
   * **Log Level**: Sets the amount of detail shown in the logs the test generates. Log results appear in the **Query Results**, **Optimized Queries**, **Service Transformation Logging**, **Generated Transformation Logging**, **Service Metrics**, and **SQL Trans Metrics** tabs. These tabs are detailed in [Examine test results](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results).
   * **Max Rows**: Sets the maximum number of rows you want to see in your test results.
5. To run the test, click **Execute SQL**.
6. Examine the test results using the instructions in [Examine test results](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results).
7. Click **Stop** to stop execution of the test.
8. Click **Close** to exit the window.
9. Optionally, you can choose to [add an optimization](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service) if you want to make it run more efficiently.
10. [Publish a Pentaho Data Service](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/publish-a-pentaho-data-service).
