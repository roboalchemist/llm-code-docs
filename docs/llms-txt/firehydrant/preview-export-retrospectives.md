# Source: https://docs.firehydrant.com/docs/preview-export-retrospectives.md

# Preview & Export Retrospectives

An important part of retrospectives is the ability to share them. FireHydrant offers several capabilities to flexibly export incident reviews.

## Customizable Export Templates

![](https://files.readme.io/09e673062679226ce1de222602cf077688327e08fa57c63fb1665f243f2d8a67-image.png)

You can now customize how your retrospectives export by configuring export templates directly within your Retrospective Template settings. This gives you full control over what gets included when you share retrospectives via PDF, Confluence, or Google Docs.

### What You Can Customize

Within each Retrospective Template, you can configure:

* **Section selection** - Choose which sections and fields to include in exports
* **Layout and formatting** - Control how information is structured and displayed
* **Custom text fields** - Add custom content or context to your exports
* **Field ordering** - Arrange sections in the order that makes sense for your audience

These export configurations are tied to each Retrospective Template, meaning you can have different export formats for different incident types or teams. When you export via PDF, Confluence, or Google Docs, the system will use your configured template to generate the export exactly as you've specified.

### Retrospective Export Templates

<Image align="center" caption="Customize Retro Export Button" src="https://files.readme.io/8dd5557d7caf3168017a12fb69ac70bc31b835be83f9552528b98c303d6f5ac4-image.png" />

You may update the export format for a specific Retrospective Template by creating a specific retro export. When you select Customize or Edit, you will then be brought to the export template builder experience. Within the export template builder you can order and customize the specific data to be presented from a completed retrospective.

<Image align="center" caption="Incident Specific Modify Export Template Button" src="https://files.readme.io/9799be4c3d063f1d7d2cc14467aa80b41da9ed1bba33a5c0937122c8bd4c9da5-image.png" />

You may also edit a retrospective specific to an incident. From within an incident, you can view the export of a retrospective and made edits to fit your exact needs. Any changes made to an incident specific retrospective export template will only be saved for that specific incident, not applied to the base template.

***

## Email Share

<Image align="center" caption="Retrospective Share Button" src="https://files.readme.io/820aae52cde4ef782d74005667a33acc4b74f8f39ff843813262e5e9b27e13f5-image.png" />

When finished with the Retrospective, you can click "Share" at the top right when on the "Retrospectives" tab. This will open a modal where you can confirm who you'd like to email or share the retrospective with (by default, all assignees on the incident will be included). Once confirmed, the link to this Retrospective will be sent via email.

## Export PDF

<Image align="center" caption="Show export button" src="https://files.readme.io/ddafa693305655b45faafc16e1a10e9dabde40b606557d16ed5b2c5edb26f86c-image.png" />

Within a retrospective tab, you can select the "Show export" button. This will dynamically render a PDF preview according to the current template being viewed, and this includes all the questions within the template as well as the details and other data shown on the right-hand side.

<Image align="center" caption="Download PDF button" src="https://files.readme.io/504f973e8bcc7942ba139422bc5601cfc6ea0aa28054ddb85d679a57b4257e2c-image.png" />

You can then select Export -> Download PDF to begin the download of the report. If there are required fields, a warning will be displayed if those haven't been filled out.

## Confluence

<Image align="center" alt="Example Confluence export" caption="Example Confluence export" src="https://files.readme.io/d65109874ee76fe887177bd08a82988da38773837e7983eccfd6a4031bc75067-CleanShot_2025-03-25_at_12.46.47.png" width="400px" />

FireHydrant has a [Confluence Cloud](https://docs.firehydrant.com/docs/confluence-cloud-integration) integration that allows exporting retrospectives and postmortems to Confluence documents. If you haven't already, you'll first need to setup the integration.

### Runbook Steps

Once done, there will be two new Runbooks available to you:

* [Export Incident Retrospective Template(s) to Confluence](https://docs.firehydrant.com/docs/export-incident-retrospective-templates-to-confluence) - Exports all attached Retrospective templates as configured to Confluence.
* [Export Retrospective to Confluence](https://docs.firehydrant.com/docs/runbook-step-export-retrospective-to-confluence) - Exports a specific, configurable template in Confluence's Markdown flavor to Confluence, which is fully configurable and editable within the Runbook step

For most users, the first step to export Template(s) will meet use cases as they directly utilize configured [Retrospective Templates](https://docs.firehydrant.com/docs/retrospective-templates) settings.

However, for advanced users who want more control, the other step will allow full configuration and control over the template, with [Markdown Support](https://docs.firehydrant.com/docs/markdown-support) and [Template Variables](https://docs.firehydrant.com/docs/template-variables) support.

### Manually-initiated export

<br />

<Image align="center" caption="Manual &#x22;Export to Confluence&#x22; Button" src="https://files.readme.io/8ae239cf4fa737a24528b43a378d30e4f14b57cdf5e2b8da9b7a95891772ac25-image.png" />

Outside of Runbooks, you can also directly initiate an export to Confluence by clicking the Export in the Retrospective view and choosing "Export to Confluence." This requires the integration to be installed but does not require the Runbook step.

## Google Docs

<Image align="center" alt="Example Google Docs export" caption="Example Google Docs export" src="https://files.readme.io/edd0109993b8d20fe2c00a587693ac85035b431d133bd234ee5fdf2489651e0b-CleanShot_2025-03-25_at_13.12.49.png" width="400px" />

Like the Confluence export, [Google Docs](https://docs.firehydrant.com/docs/google-docs-integration) also supports two different Runbook steps:

* [Export Incident Retrospective Template(s) to Google Docs](https://docs.firehydrant.com/docs/export-incident-retrospective-templates-to-google-docs) - Exports all attached Retrospective templates as configured to Google Docs
* [Export Retrospective to Google Docs](https://docs.firehydrant.com/docs/runbook-step-export-to-google-docs) - Exports a specific, configurable template in standard Markdown to Google Docs, which is fully configurable and editable within the Runbook step

Generally the first step to export Template(s) will meet most use cases, but advanced users who want full control and configurability over what gets exported to Google Docs can use the 2nd step which supports [Markdown](https://docs.firehydrant.com/docs/markdown-support) and [Template Variables](https://docs.firehydrant.com/docs/template-variables).

### Manually-initiated export

<Image align="center" caption="Manual &#x22;Export to Google Docs&#x22; Button" src="https://files.readme.io/b0b426250679f8033abe5b285f2960eaef1f11b3d4760fe5899f189dd02650f9-image.png" />

Outside of Runbooks, you can also directly initiate an export to Google Docs by clicking "Export" button in the Retrospective view and choosing "Export to Google Docs." This requires the integration to be installed but does not require the Runbook step.

## Webhook & Template Variables

If the above options don't work for you, you can also make full use of [Template Variables](https://docs.firehydrant.com/docs/template-variables) in [Send a Webhook](https://docs.firehydrant.com/docs/runbook-step-send-a-webhook) Runbook step.

This step allows you full control over a payload that is sent to any external destination reachable by HTTPS, so this can be used to send any incident data practically anywhere else. For more information, visit the links above.