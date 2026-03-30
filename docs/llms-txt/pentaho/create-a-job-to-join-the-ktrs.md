# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/using-table-input-to-table-output-steps-with-ael-for-managed-tables-in-hive/create-a-job-to-join-the-ktrs.md

# Create a job to join the KTRs

Follow the steps below to create a job to process managed tables in Hive.

1. Select **File** > **New** > **Job** in the PDI client window to create a new job.

   A new canvas opens.
2. On the **Design** tab, click **General** and then double-click **Start**.

   The Start entry appears on the canvas.
3. Under **General**, double-click **Transformation**.

   The Transformation entry appears on the canvas and is connected by a hop from the Start entry.
4. Double-click the Transformation entry.

   The Transformation entry dialog box appears.
5. Browse to your saved Table input KTR file, then enter a name, such as `Table_In`. Click **OK** to save the entry.
6. Under **General**, double-click **Transformation**.

   The Transformation entry appears on the canvas and is connected by a hop from the previous Transformation entry.
7. Double-click the Transformation entry.

   The Transformation entry dialog box appears.
8. Browse to your saved Table output KTR file, then enter a name such as `Table_Out`. Click **OK** to save the entry.
9. (Optional) Add a Dummy entry joined by an error hop to each Transformation entry to handle any false results.
10. Under **General**, double-click **Success**.

    The **Success** entry appears on the canvas and is connected by a hop from the Transformation entry.
11. Click **File** > **Save As** and enter a name for the file. Save it.
12. Press **Run** to execute the job.

    The following example illustrates the job on the canvas:

    ![PDI sample job](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-6cdcf1202d6d27692691c60fa4d6e12386c0b747%2FPDI_TableInputOutput_Sample%20Job.png?alt=media)

The content of your managed table in Hive was correctly processed using the job.
