# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/using-table-input-to-table-output-steps-with-ael-for-managed-tables-in-hive/create-separate-input-and-output-ktrs.md

# Create separate input and output KTRs

Follow the steps below to create separate transformations to process managed tables in Hive.

**Note:** Depending on the size of your managed tables, use the noted alternative PDI transformation steps to maximize processing efficiency.

1. Select **File** > **New** > **Transformation** in the PDI client window to create a new transformation.

   A new canvas opens.
2. On the **Design** tab, click **Input** and then double-click **Table input**.

   The Table input step appears on the canvas.

   **Note:** As a best practice for smaller managed input tables, use the Copy rows to result step. For larger managed input tables, instead use the Set files in result step.
3. Enter your connection and option information in the Table input step.
4. Select **File** > **Save As** then enter a name for the file, such as `Table_In`. Save the file.
5. Select **File** > **New** > **Transformation** in the PDI client window to create a new transformation.

   A new canvas opens.
6. On the **Design** tab, click **Output** and then double-click **Table output**.

   The Table output step appears on the canvas.

   **Note:** As a best practice for smaller managed input tables, use the Get rows from result step. For larger managed input tables, instead use the Get files from result step.
7. Enter your configuration information for the target table in the Table output step.
8. Click **File** > **Save As** then enter a name for the file, such as `Table_Out`. Save the file.

You have now created separate transformation steps for data processing. Proceed to [Create a job to join the KTRs](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/using-table-input-to-table-output-steps-with-ael-for-managed-tables-in-hive/create-a-job-to-join-the-ktrs).
