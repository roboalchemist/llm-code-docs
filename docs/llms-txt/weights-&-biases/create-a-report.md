# Source: https://docs.wandb.ai/models/reports/create-a-report.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Create a W&B Report with the W&B App or programmatically.

# Create a report

<Note>
  W\&B Report and Workspace API is in Public Preview.
</Note>

Select a tab below to learn how to create a report in the W\&B App or programmatically with the W\&B Report and Workspace API.

See this [Google Colab](https://colab.research.google.com/github/wandb/examples/blob/master/colabs/intro/Report_API_Quickstart.ipynb) for an example on how to programmatically create a report.

<Tabs>
  <Tab title="W&B App">
    1. Navigate to your project workspace in the W\&B App.

    2. Click **Create report** in the upper right corner of your workspace.

       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/uqPGOvf46GQ1vVUB/images/reports/create_a_report_button.png?fit=max&auto=format&n=uqPGOvf46GQ1vVUB&q=85&s=45ede188f3d7c839f54dae2397f7907d" alt="Create report button" width="2510" height="462" data-path="images/reports/create_a_report_button.png" />
       </Frame>

    3. A modal will appear. Select the charts you would like to start with. You can add or delete charts later from the report interface.

       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/uqPGOvf46GQ1vVUB/images/reports/create_a_report_modal.png?fit=max&auto=format&n=uqPGOvf46GQ1vVUB&q=85&s=1cbc7a3366b472bd9da4aeb3ef8b602a" alt="Create report modal" width="920" height="840" data-path="images/reports/create_a_report_modal.png" />
       </Frame>

    4. Select the **Filter run sets** option to prevent new runs from being added to your report. You can toggle this option on or off. Once you click **Create report,** a draft report will be available in the report tab to continue working on.
  </Tab>

  <Tab title="Report tab">
    1. Navigate to your project workspace in the W\&B App.
    2. Select to the **Reports** tab (clipboard image) in your project.
    3. Select the **Create Report** button on the report page.

       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/uqPGOvf46GQ1vVUB/images/reports/create_report_button.png?fit=max&auto=format&n=uqPGOvf46GQ1vVUB&q=85&s=2c71a7c7f3d091e481aed0a0c0a07938" alt="Create report button" width="2542" height="1614" data-path="images/reports/create_report_button.png" />
       </Frame>
  </Tab>

  <Tab title="Report and Workspace API">
    Create a report programmatically:

    1. Install W\&B SDK (`wandb`) and Report and Workspace API (`wandb-workspaces`):
       ```bash  theme={null}
       pip install wandb wandb-workspaces
       ```

    2. Next, import workspaces
       ```python  theme={null}
       import wandb
       import wandb_workspaces.reports.v2 as wr
       ```

    3. Create a report with `wandb_workspaces.reports.v2.Report`. Create a report instance with the Report Class Public API ([`wandb.apis.reports`](/models/ref/python/public-api/api#reports)). Specify a name for the project.
       ```python  theme={null}
       report = wr.Report(project="report_standard")
       ```

    4. Save the report. Reports are not uploaded to the W\&B server until you call the .`save()` method:
       ```python  theme={null}
       report.save()
       ```

    For information on how to edit a report interactively with the App UI or programmatically, see [Edit a report](/models/reports/edit-a-report/).
  </Tab>
</Tabs>
