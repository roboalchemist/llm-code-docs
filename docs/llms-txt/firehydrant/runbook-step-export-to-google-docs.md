# Source: https://docs.firehydrant.com/docs/runbook-step-export-to-google-docs.md

# Export Retrospective to Google Docs

<Image alt="Example Google Docs Retrospective Export" align="center" width="650px" src="https://files.readme.io/40e9ee3-image.png">
  Example Google Docs Retrospective Export
</Image>

## Prerequisites

Configure your [Google Docs](https://docs.firehydrant.com/docs/google-docs-integration) integration if you haven't already.

## Configuration

<Image alt="Export Retrospective to Google Docs step" align="center" width="650px" src="https://files.readme.io/d8a24ad-image.png">
  Export Retrospective to Google Docs step
</Image>

FireHydrant provides default templating, but you can customize the content optionally. The template fields support [Template Variables](https://docs.firehydrant.com/docs/template-variables).

* **Title Template:** This is the name of the new Google Doc that will be created
* **Body Template:** This is the body of the Google Doc we will create. This field also accepts variables, so you can automatically include details such as when the incident started, the incident summary, severity, roles involved, etc.

Ensure settings are configured per your requirements on the **Conditions & scheduling** tab. The default configuration is "When current <Glossary>Milestone</Glossary> == Retrospective Completed."

Remember that for this step to execute successfully, the step must run after the Retrospective has at least started. Valid conditions include:

* When the current milestone is Retrospective Started
* When the current milestone is Retrospective Completed
* Time since Retrospective Started/Completed

> 🚧 Note:
>
> If using in a [Private Incident](https://docs.firehydrant.com/docs/private-incidents)/private runbook, you must uncheck "Execute Automatically." For security and safety reasons, FireHydrant does not allow these retrospective steps to execute automatically for Private incidents, and you must set the step to execute manually.

## Runbook Execution

Upon completion of Retrospective, the export step [may take a few minutes to execute](/docs/runbook-conditions#resolved-and-retrospective-states). Once the export is complete, a link to the exported document will be attached to the incident like so:

<Image alt="Confluence export link included on the incident's data" align="center" width="400px" src="https://files.readme.io/6b91a88-Screenshot_2023-12-21_at_5.36.34_PM.png">
  Google Doc export link included on the incident's data
</Image>

Exported retrospectives are stored in a folder named **FireHydrant Retrospectives** at the Google Drive root of the user who authorized the integration.

The document will export with edit permissions for the organization by default.

> 📘 Note:
>
> This step will only be able to execute once, even if included in multiple Runbooks. Subsequent executions after the first will fail.