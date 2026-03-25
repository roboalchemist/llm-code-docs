# Source: https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/stop-transformations-and-jobs.md

# Source: https://docs.pentaho.com/pdia-data-integration/pipeline-designer/stop-transformations-and-jobs.md

# Stop transformations and jobs

There are two different methods you can use to stop a transformation or job running in the Pipeline Designer. The method you use depends on the processing requirements of your ETL task. Most transformations and jobs can be stopped immediately without concern. However, since some transformations and jobs are ingesting records using messaging or streaming data, such incoming data might need to be stopped safely so that the potential for data loss is avoided.

In the **Canvas Action** toolbar, take one of the following actions:

* To stop processing all data immediately, click **Stop**.
* To make the transformation or job finish any records that were initiated or retrieved before it stops processing data, click the arrow next to **Stop,** and then select **Stop input processing.**&#x20;
