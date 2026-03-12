# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/stop-your-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/stop-your-transformation.md

# Stop your transformation

There are two different methods you can use to stop transformations running in the PDI client. The method you use depends on the processing requirements of your ETL task. Most transformations can be stopped immediately without concern. However, since some transformations are ingesting records using messaging or streaming data, such incoming data may need to be stopped safely so that the potential for data loss is avoided.

To stop a transformation running in the [Data Integration perspective](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/get-started-with-the-pdi-client-1/use-the-pdi-client-perspectives#data-integration-perspective) of the PDI client:

* Use **Stop** if your ETL task should stop processing all data immediately.
* Use **Stop input processing** if your ETL task needs to finish any records already initiated or retrieved before stopping.
