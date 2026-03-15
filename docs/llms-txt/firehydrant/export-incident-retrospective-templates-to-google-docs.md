# Source: https://docs.firehydrant.com/docs/export-incident-retrospective-templates-to-google-docs.md

# Export Incident Retrospective Template(s) to Google Docs

<Image alt="Example Google Docs export" align="center" width="650px" src="https://files.readme.io/edd0109993b8d20fe2c00a587693ac85035b431d133bd234ee5fdf2489651e0b-CleanShot_2025-03-25_at_13.12.49.png">
  Example Google Docs template export
</Image>

## Prerequisites

Configure your [Google Docs](https://docs.firehydrant.com/docs/google-docs-integration) integration if you haven't already.

## Configuration

<Image alt="Export Retrospective to Google Docs step" align="center" width="650px" src="https://files.readme.io/8a60762023e9f9ccbb2e628c80dccbcf0a3f7830192d8c5ef0cfda1b87122a9c-CleanShot_2025-03-25_at_16.58.34.png">
  Export incident retrospective template(s) to Google Docs step
</Image>

This step is different than the [Export Retrospective to Google Docs](https://docs.firehydrant.com/docs/runbook-step-export-to-google-docs) step, which enables configuring and fully customizing the template or data exported to Google Docs. Instead, this step exports your configured [Retrospective Templates](https://docs.firehydrant.com/docs/retrospective-templates).

On the **Conditions & scheduling** tab, ensure settings are configured per your requirements. The default configuration is "When current <Glossary>Milestone</Glossary> == Retrospective Completed."

> 🚧 Note:
>
> If using in a [Private Incident](https://docs.firehydrant.com/docs/private-incidents) or private runbook, you must uncheck "Execute Automatically." For security and safety reasons, FireHydrant does not allow these retrospective steps to execute automatically for Private incidents, and you must set the step to execute manually.

## Runbook Execution

Upon completion of Retrospective, the export step [may take a few minutes to execute](/docs/runbook-conditions#resolved-and-retrospective-states). Once the export is complete, a link to the exported document will be attached to the incident like so:

<Image alt="Confluence export link included on the incident's data" align="center" width="650px" src="https://files.readme.io/042bc41c559ae2a61b6cdce2f7c0c38178db20b42e54d9e1f95d05810ef0f380-CleanShot_2025-03-25_at_17.01.43.png">
  Google Doc export link included on the incident's data
</Image>

Exported retrospectives are stored in a folder named **FireHydrant Retrospectives** at the Google Drive root of the user who authorized the integration.

The document will export with edit permissions for the organization by default.

> 📘 Note:
>
> This step will only be able to execute once, even if included in multiple Runbooks. Subsequent executions after the first will fail.