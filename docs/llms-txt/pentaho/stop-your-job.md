# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/stop-your-job.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/stop-your-job.md

# Stop your job

There are two different methods you can use to stop jobs running in the PDI client. The method you use depends on the processing requirements of your ETL activity. Most jobs can be stopped immediately without concern. However, since some jobs are ingesting records using messaging or streaming data, such incoming data may need to be stopped safely so that the potential for data loss is avoided.

To stop a job running in the [Data Integration perspective](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/get-started-with-the-pdi-client-1/use-the-pdi-client-perspectives#data-integration-perspective) of the PDI client:

* Use **Stop** if your ETL activity should stop processing all data immediately.
* Use **Stop input processing** if your ETL activity needs to finish any records already initiated or retrieved before stopping.
