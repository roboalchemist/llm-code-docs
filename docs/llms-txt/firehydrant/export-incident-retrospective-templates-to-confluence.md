# Source: https://docs.firehydrant.com/docs/export-incident-retrospective-templates-to-confluence.md

# Export Incident Retrospective Template(s) to Confluence

<Image alt="Example Confluence export" align="center" width="650px" src="https://files.readme.io/d65109874ee76fe887177bd08a82988da38773837e7983eccfd6a4031bc75067-CleanShot_2025-03-25_at_12.46.47.png">
  Example Confluence export
</Image>

## Prerequisites

Configure your [Confluence Cloud](https://docs.firehydrant.com/docs/confluence-cloud-integration) integration if you haven't already.

## Configuration

<Image alt="Export Retrospective to Confluence step" align="center" width="650px" src="https://files.readme.io/4b078430cb89b50c496a4a0a9027f6dd5217019cb080348dcb32ccfa4d813af8-CleanShot_2025-03-25_at_16.31.20.png">
  Export incident retrospective template(s) to Confluence step
</Image>

This step is different than the [Export Retrospective to Confluence](https://docs.firehydrant.com/docs/runbook-step-export-retrospective-to-confluence) step, which enables configuring and fully customizing the template or data exported to Confluence. Instead, this step exports your configured [Retrospective Templates](https://docs.firehydrant.com/docs/retrospective-templates).

On the **Conditions & scheduling** tab, ensure settings are configured per your requirements. The default configuration is "When current <Glossary>Milestone</Glossary> == Retrospective Completed."

> 🚧 Note:
>
> If using in a [Private Incident](https://docs.firehydrant.com/docs/private-incidents) or private runbook, you must uncheck "Execute Automatically." For security and safety reasons, FireHydrant does not allow these retrospective steps to execute automatically for Private incidents, and you must set the step to execute manually.

## Runbook Execution

Upon completion of Retrospective, the export step [may take a few minutes to execute](/docs/runbook-conditions#resolved-and-retrospective-states) in Confluence. Once the export is complete, a link to the exported document will attach to the incident. You can find the links on the Incident view within the **Links** section or the Retrospectives view right at the top as well as under **Resources** > **Links**.

<Image alt="Retrospectives view with exported templates" align="center" width="650px" src="https://files.readme.io/5b3805f1a59c7cb264b53bd9c0795d0fa6b50689e3e39b69fd21416023a43546-CleanShot_2025-03-25_at_16.48.00.png">
  Retrospectives view with exported templates
</Image>