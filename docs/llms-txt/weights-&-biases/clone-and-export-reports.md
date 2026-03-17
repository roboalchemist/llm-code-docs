# Source: https://docs.wandb.ai/models/reports/clone-and-export-reports.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Export W&B Reports as PDF or LaTeX files, and clone reports using the App UI or the Report and Workspace API.

# Clone and export reports

<Note>
  W\&B Report and Workspace API is in Public Preview.
</Note>

## Export reports

Export a report as a PDF or LaTeX. Within your report, select the kebab icon to expand the dropdown menu. Choose **Download and** select either PDF or LaTeX output format.

## Cloning reports

<Tabs>
  <Tab title="W&B App">
    Within your report, select the kebab icon to expand the dropdown menu. Choose the **Clone this report** button. Pick a destination for your cloned report in the modal. Choose **Clone report**.

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/uqPGOvf46GQ1vVUB/images/reports/clone_reports.gif?s=c8fe974436e77e379836c73a1be5e8b3" alt="Cloning reports" width="2672" height="1168" data-path="images/reports/clone_reports.gif" />
    </Frame>

    Clone a report to reuse a project's template and format. Cloned projects are visible to your team if you clone a project within the team's account. Projects cloned within an individual's account are only visible to that user.
  </Tab>

  <Tab title="Report and Workspace API">
    Load a Report from a URL to use it as a template.

    ```python  theme={null}
    report = wr.Report(
        project=PROJECT, title="Quickstart Report", description="That was easy!"
    )  # Create
    report.save()  # Save
    new_report = wr.Report.from_url(report.url)  # Load
    ```

    Edit the content within `new_report.blocks`.

    ```python  theme={null}
    pg = wr.PanelGrid(
        runsets=[
            wr.Runset(ENTITY, PROJECT, "First Run Set"),
            wr.Runset(ENTITY, PROJECT, "Elephants Only!", query="elephant"),
        ],
        panels=[
            wr.LinePlot(x="Step", y=["val_acc"], smoothing_factor=0.8),
            wr.BarPlot(metrics=["acc"]),
            wr.MediaBrowser(media_keys="img", num_columns=1),
            wr.RunComparer(diff_only="split", layout={"w": 24, "h": 9}),
        ],
    )
    new_report.blocks = (
        report.blocks[:1] + [wr.H1("Panel Grid Example"), pg] + report.blocks[1:]
    )
    new_report.save()
    ```
  </Tab>
</Tabs>
