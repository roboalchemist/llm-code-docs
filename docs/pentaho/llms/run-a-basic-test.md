# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/run-a-basic-test.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/run-a-basic-test.md

# Run a basic test

To run a basic test on a regular data service, perform the following steps:

1. Verify **Data Service Type** is set to **Regular**.
2. Perform one of the following actions to open the Test Data Service window:
   * In the Data Service window, click **Test Data Service**.
   * In the **View** tab of the PDI client **Explore** pane, click **Data Services**. Right-click the name of the data service you want, then select **Test**.
   * Right-click the step attached to the data service as indicated by the data service badge, then select **Data Services** > **Test**.
3. If needed, adjust the following optional settings:
   * **Log Level**: Sets the amount of detail shown in the logs the test generates. Log results appear in the **Query Results**, **Optimized Queries**, **Service Transformation Logging**, **Generated Transformation Logging**, **Service Metrics**, and `SQL Trans Metrics` tabs. These tabs are detailed in **Examine Test Results**.
   * **Max Rows**: Sets the maximum number of rows you want to see in your test results.
4. To run the test, click **Execute SQL**.
5. Examine the test results using the instructions in [Examine test results](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results).
6. If you need to run another test, [clear the cache](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-the-service-cache-optimization/clear-the-cache), then run the test again.
7. Click **Close** to exit the window.
8. Optionally, you can choose to [add an optimization](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service) if you want to make it run more efficiently.
9. [Publish a Pentaho Data Service](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/publish-a-pentaho-data-service).
