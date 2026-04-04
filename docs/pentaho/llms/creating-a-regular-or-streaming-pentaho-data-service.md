# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/creating-a-regular-or-streaming-pentaho-data-service.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/creating-a-regular-or-streaming-pentaho-data-service.md

# Creating a regular or streaming Pentaho Data Service

You can create either a regular data service or a [streaming data](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/streaming-analytics) service. A streaming data service is commonly used when creating a streaming data dashboard with CTools. See **Pentaho CTools**.

Perform the following steps to create a data service, name it, then select the step that outputs the data you want to be exposed to the data service:

1. [Create or open a transformation in the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp).

   It is helpful to review [Pentaho Data Service SQL support reference and other development considerations](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results/pentaho-data-service-sql-support-reference-and-other-development-considerations) as you create or review the transformation so that you understand which SQL commands are supported.
2. Save the transformation to the Pentaho Server.
3. Right-click the transformation step that outputs the data you want to make available as a data service, then select **Data Services** > **New**.
4. Enter a unique name for the data service in the **Service Name (Virtual Table Name)** text box.

   The virtual table that the data service creates has the same name as the data service.

   **Note:** Ensure the name is unique; no other data service stored locally or published to the Pentaho Server should have the same name.
5. Verify that the Output step is the step you selected to become the data service in Step 3. If you need to change it, select the correct step name from the list.
6. If you are working with streaming data, select **Streaming** for the **Data Service Type**.
7. Click **OK** to save the data service and exit the window.

   The [data service badge](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/creating-a-regular-or-streaming-pentaho-data-service/data-service-badge) is added to the step icon.

A recommended but optional step, is to follow the steps in [Test a Pentaho Data Service](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service) so that you can test your data service. Testing can help you correct, refine, and optimize your data service so it runs more efficiently.
