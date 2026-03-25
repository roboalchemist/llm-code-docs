# Source: https://docs.firehydrant.com/docs/runbook-step-export-retrospective-to-confluence.md

# Export Retrospective to Confluence

<Image alt="Example Retrospective export to Confluence" align="center" width="650px" src="https://files.readme.io/65f256b-image.png">
  Example Retrospective export to Confluence
</Image>

## Prerequisites

Configure your [Confluence Cloud](https://docs.firehydrant.com/docs/confluence-cloud-integration) integration if you haven't already.

## Configuration

<Image alt="Export Retrospective to Confluence step" align="center" width="650px" src="https://files.readme.io/b8c0b5a-image.png">
  Export Retrospective to Confluence step
</Image>

FireHydrant provides default templating, but you can optionally customize the content. The template fields support [Template Variables](https://docs.firehydrant.com/docs/template-variables).

* **Parent Page:** This refers to the main page that the new Confluence page will be created within. Leave empty to save at the top level in your Confluence workspace.
* **Title Template:** This is the name of the new Confluence page that will be created
* **Body Template:** This is the body of the page that we will create in Confluence. This field also accepts variables, so you can automatically include details such as when the incident started, the incident summary, severity, roles involved, etc.\*\*

> 📘 \*\*Note:
>
> The Runbook step supports [Markdown](https://docs.firehydrant.com/docs/markdown-support) and not Confluence Wiki markup syntax.

On the **Conditions & scheduling** tab, ensure settings are configured per your requirements. The default configuration is "When current <Glossary>Milestone</Glossary> == Retrospective Completed."

Remember that for this step to execute successfully, the step must run after the Retrospective has at least started. Valid conditions include:

* When the current milestone is Retrospective Started
* When the current milestone is Retrospective Completed
* Time since Retrospective Started/Completed

> 🚧 Note:
>
> If using in a [Private Incident](https://docs.firehydrant.com/docs/private-incidents)/private runbook, you must uncheck "Execute Automatically." For security and safety reasons, FireHydrant does not allow these retrospective steps to execute automatically for Private incidents, and you must set the step to execute manually.

## Runbook Execution

Upon completion of Retrospective, the export step [may take a few minutes to execute](/docs/runbook-conditions#resolved-and-retrospective-states) in Confluence. Once the export is complete, a link to the exported document will attach to the incident, like so:

<Image alt="Confluence export link included on the incident's data" align="center" width="400px" src="https://files.readme.io/37cd87b-Screenshot_2023-12-21_at_5.22.27_PM.png">
  Confluence export link included on the incident's data
</Image>

> 📘 Note:
>
> This step will only be able to execute once, even if included in multiple Runbooks. Subsequent executions after the first will fail.

## Troubleshooting

### Atlassian converting ADF to storage format error

The Atlassian Confluence API occasionally returns the following error when a Confluence runbook export is initiated:

<Image align="center" src="https://files.readme.io/758606a-runbooks-confluence-step-failure.png" />

This intermittent error has been reported on the [Confluence developer forum](https://community.atlassian.com/t5/Confluence-discussions/Problem-Your-work-is-safe-but-there-s-an-issue-Refresh-the-page/td-p/1667062). If this happens, retry the step by going to the incident page and then clicking on **Runbooks> nbook]**, expa\*\*, expanding the step, and then clicking "Retry step."