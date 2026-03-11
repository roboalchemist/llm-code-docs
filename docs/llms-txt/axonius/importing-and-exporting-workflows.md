# Source: https://docs.axonius.com/docs/importing-and-exporting-workflows.md

# Importing and Exporting Workflows

You can import and export workflows to share them across environments. The workflow is exported in JSON format, including the complete definition of all nodes.

<Callout icon="📘" theme="info">
  Note

  Sensitive information, such as passwords, API keys, tokens, are not exported and need to be reconfigured after import.
</Callout>

**To export a workflow:**

1. In the Workflows page, hover over the workflow you want to export, and, from the 3-dot menu, select **Export Workflow**.
2. A pop-up notifies you that credentials and sensitive inputs are excluded and must be reconfigured when reimporting this workflow. To continue and export, click **Export**.
3. A file in JSON format is downloaded to your local computer.

<br />

**To import a workflow:**

1. From the **Create Workflow** list, select **Import Workflow**.
2. Select the workflow to import and click **Open**.
3. If a query or other data already exists in the environment to which you are importing the workflow, a warning dialog is displayed.

   <Image align="center" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/ImportWorkflowConflictNoticeBox.png" />
4. For each instance of a conflict, select how you want to resolve the conflict:
   1. **Save as copy** -  Creates a copy of the item.
   2. **Overwrite** - Overwrites the existing item with the one being imported.
5. Click **Import**. The imported workflow is added to the Workflows page, and the selections from the previous step are implemented.