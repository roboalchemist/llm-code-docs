# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/write-metadata/options-write-metadata-step/metadata-tab-write-metadata-step.md

# Metadata tab

In this tab, specify any of the existing metadata tags you want to associate with the data resources identified in the **Input** tab. This PDI option matches the **Add a tag** feature for a data resource in the Data Catalog.

For example, if your transformation uses the Catalog Input step to create or update a data resource in Data Catalog, you could use this step to inject resource IDs into your transformation and add tags to those data resources.

![Metadata tab](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-39cb54ddb2e70b863acc47be5dd88b0462162efe%2Fpdi_write_catalog_metadata_step_metadata_tab_populated_02.png?alt=media)

Use the drop-down menu to select a tag, or several tags, from the existing tags that are available through your Data Catalog connection. Enter a description for this tag or group of tags in the **Description** field, or edit the existing description.

| Field           | Description                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------ |
| **Description** | Type or revise the description for the tag or group of tags you selected with the **Tags** option.     |
| **Tags**        | Select any existing tags you want associated with, and assigned to, the resource ID and click **ADD**. |

**Note:** If missing or incomplete data is returned, you may need to change the default limit for returned results. See [Data Catalog searches returning incomplete or missing data](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/lumada-data-catalog-searches-returning-incomplete-or-missing-data) for information.
