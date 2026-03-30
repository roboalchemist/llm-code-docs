# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-streaming-optimization/how-the-streaming-optimization-technique-works.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-streaming-optimization/how-the-streaming-optimization-technique-works.md

# How the streaming optimization technique works

You can customize the amount of the records used for processing by specifying a maximum limit for time or rows in the window mode. You can optimize data service processing by specifying a **Rows Limit** (the maximum number of rows that a window can have). If the value in the **Rows Limit** is reached, a new window is created. You can also optimize data service processing by specifying a **Time Limit** (the maximum elapsed time to create a new window).
