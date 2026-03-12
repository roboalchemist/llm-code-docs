# Source: https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/edit-a-transformation-or-job.md

# Source: https://docs.pentaho.com/pdia-data-integration/pipeline-designer/edit-a-transformation-or-job.md

# Edit a transformation or job

Edit an existing transformation or job to rename it, add new steps, edit steps, configure hops, edit properties, reset it, or save it in a different location.

To edit a transformation or job, complete the following steps:

1. Log into the Pentaho User Console.
2. Open **Pipeline Designer**:&#x20;

   * If you are using the **Modern Design**, in the menu on the left side of the page, click **Pipeline Designer**.&#x20;
   * If you are using the **Classic Design**, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Pipeline Designer**.&#x20;

   **Pipeline Designer** opens with the **Quick Access** section expanded.
3. In the table at the bottom of the screen, select either the **Recently opened** or **Favorites** tab.
4. Open a transformation or job:&#x20;
   1. Search for or browse to the transformation or job, and then click **Open**.
   2. Click **Open files**, and then in the **Select File or Directory** dialog box, search for or browse to the transformation or job and click **Open**.
5. Edit the transformation or job by taking one or more of the following actions:
   * **Rename a transformation or job**

     1. In the transformation or job tab, click the name to make it editable.
     2. Type a new name and press **Enter**.

     **Note:** You can also change the name of a transformation or job in the properties window. For details see [Configure transformation properties](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/broken-reference) or [Configure job properties](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/broken-reference).

   * **Add a new step**
     1. In the **Design** pane, search for or browse to a step you want to use in the transformation. You may need to expand sections in the **Design** pane to find steps.
     2. Drag the step you want to add onto the canvas.&#x20;

   * **Edit steps**&#x20;

     Hover over a step to open the step menu, and then select one of the following options for either a transformation or job:&#x20;

     <table><thead><tr><th width="169.22210693359375">Step option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Delete</strong></td><td>Deletes the step from the canvas.</td></tr><tr><td><strong>Edit</strong> </td><td><p>Opens the <em><strong>Step Name</strong></em> window where you can configure the properties of the step. Step properties may appear in multiple sections, tabs, or both. </p><p><strong>Note:</strong> To learn more about the step you're configuring, in the lower-left corner of the <strong>Step Name</strong> window, click <strong>Help</strong>.</p></td></tr><tr><td><strong>Duplicate</strong></td><td>Adds a copy of the step to the canvas.</td></tr></tbody></table>

     For transformations only, you can select one of the following additional options:

     <table><thead><tr><th width="169.22210693359375">Step option</th><th>Description</th></tr></thead><tbody><tr><td><strong>More Actions</strong> > <strong>Change Number of Copies</strong></td><td>Opens the <strong>Number of copies</strong> dialog box, where you can enter a number or a variable to specify how many copies of the step are processed in parallel when the transformation or job is run. To find a variable, in the <strong>Number of copies (1 or higher</strong>) box, click the <strong>Select variable to insert</strong> icon.</td></tr><tr><td><strong>More Actions</strong> > <strong>Data Movement</strong></td><td><p>Opens a list of data movement options for you to select from to specify how data rows are distributed to the next steps of the transformation or job. Round-Robin is the default setting.</p><ul><li><strong>Round-Robin:</strong> Distributes rows evenly across all parallel step copies using round-robin logic. This setting optimizes load balancing when the transformation includes multiple instances of the next step. </li><li><strong>Load Balance:</strong> Routes rows to the step copy with the lightest processing load. This setting can improve performance when processing times vary across parallel step instances.</li><li><strong>Copy Data to Next Steps:</strong> Sends each row to all parallel step copies. Use this setting when every downstream branch must process the complete dataset independently.</li></ul></td></tr></tbody></table>

   * **Configure hops**
     * To add hops between steps, hover over a step’s handle until a plus sign (+) appears, then drag the connection to the handle of another step.
     * Disable a hop by selecting it and clicking the **Disable** icon.
     * Delete the hop by selecting it and clicking the **Delete** icon.

   * **Edit transformation or job properties**
     * In the **Canvas Action** toolbar, click the **Settings** icon. The **Transformation Properties** or **Job Properties** window opens.
     * Change properties in one or more tabs. For details, see [Transformation properties](#transformation-properties) or [Job properties](#job-properties).

   * **Reset the transformation or job**

     **Note:** Resetting a transformation or job clears all steps and connections from the transformation or job and cannot be undone.

     1. In the **Canvas Action** toolbar, click the **Reset** icon. The **Confirm Reset** window opens.
     2. Click **Reset**. All steps and connections are removed from the transformation or job.

   * **Save transformation or job in a different location**
     1. Click **Save as**. The **Select File or Directory** dialog box opens.
     2. Search for or browse to the folder in the repository where you want to save the transformation or job.
     3. (Optional) To create a new folder in the repository, click the **New Folder** icon, and then in the **New folder** dialog box, enter a **New folder name** and click **Save**.&#x20;
     4. (Optional) To delete a folder from the repository, select the folder and click the **Delete** icon.
     5. In the **Select File or Directory** dialog box, click **Save**. The **Save Change** dialog box opens.
     6. Click **Yes** to confirm that you want to save the transformation or job.
