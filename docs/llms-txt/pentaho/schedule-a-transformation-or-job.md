# Source: https://docs.pentaho.com/pba/pentaho-user-console/modern-design/scheduler/schedule-a-transformation-or-job.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/schedule-perspective-in-the-pdi-client/schedule-a-transformation-or-job.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/schedule-perspective-in-the-pdi-client/schedule-a-transformation-or-job.md

# Schedule a transformation or job

You can schedule transformations and jobs to run at specific times by performing the following steps:

1. Connect to the Pentaho Repository.
2. Open a job or transformation from the Pentaho Repository, then select **Action** > **Schedule**. The Schedule window appears.

   ![Schedule window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-fc2b9da197136eecda7414246cb84f21ef79396a%2Fscheduler.png?alt=media)
3. In the **Start** section, either select **Now** to schedule a transformation or job to run immediately, or select **Date**, and then enter a date, time, and time zone to run it later.
4. In the **Repeat** section, either select **Run Once** to run the transformation or job once or select **Seconds**, **Minutes**, **Weekly**, **Hourly**, **Monthly**, or **Yearly** to run it at regular intervals.
5. In the **End** section, either select **No end** to indicate that the schedule will never expire, or select **Date** to enter a schedule expiration date.
6. To run the scheduled transformation or job in safe mode, select the **Enable Safe Mode** checkbox.

   Safe mode checks every row that passes through the stream to ensure that all layouts are the same as the first row. If the layout differs, an error is generated and reported.
7. Select the **Log Level**.

   Logging levels are addressed in detail in the [Logging levels](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/logging-levels) article.
8. If you have specified parameters, variables, or arguments in a transformation or job, they appear in the bottom part of the window. Adjust values as needed.
9. When done, click **OK**.

   **Note:** If you want to access a Google Drive via your scheduled transformation, copy the **StoredCredential** token into the `pentaho-server/pentaho-solutions/system/kettle/plugins/pentaho-googledrive-vfs/credentials` directory on your Pentaho Server. See [Access to a Google Drive](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/access-to-a-google-drive) for information on how to obtain a **StoredCredential** token.
