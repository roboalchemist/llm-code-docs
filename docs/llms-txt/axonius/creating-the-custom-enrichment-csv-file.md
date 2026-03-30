# Source: https://docs.axonius.com/docs/creating-the-custom-enrichment-csv-file.md

# Creating the Custom Enrichment CSV File

The CSV file contains headers and values.

* The first column of the CSV file lists data that identifies which assets to enrich, such as an asset name or ID.

* The other columns in the CSV file include the data that will be added to the asset.

* The column headers/field names can include characters, spaces, and underscores " \_ ".  Hyphens " - " are not allowed. See note below for an explanation of how white spaces in column headers are processed.

* When the value in the asset matches the value in the first column, the values in the other columns are added to the asset.

* When the headers of these other columns match the names of existing Axonius fields in the asset, these fields are updated with the values in the corresponding columns.

* Otherwise, new fields are added to the asset and the headings are used to name the enrichment fields in the asset with **Enrichment** prepended to the column heading when enriched based on a specific adapter, and **Common Enrichment** when enriched based on an aggregated field (created using System Settings or the [Manage Custom Enrichment - Enrich assets with CSV file Enforcement Action](/docs/add-enrichment) with the default configuration).

* When there is no value in a column for a particular asset, that asset is not enriched with that field.

* When creating the Custom Enrichment using the [Manage Custom Enrichment - Enrich assets with CSV file Enforcement Action](/docs/add-enrichment) with the option enabled to write enriched values, the headings are used to name the Enrichment fields in the EC Artifacts adapter with **Enrichment** prepended to the column heading, and then those enriched field values are added as values to aggregated fields having the same name.

<Callout icon="📘" theme="info">
  Note

  When using CSV files for custom enrichment, be aware of how white spaces in column headers are processed:

  * Field comparison: During comparison with existing Axonius fields, any white space in a header is treated as an underscore ("\_").

  * Axonius Enrichment field names: White spaces are replaced with underscores (e.g., "user name" is stored as "user\_name").

  * Custom Enrichment rule restrictions: Column headers used as *source.* fields in [custom enrichment rules](/docs/creating-the-custom-enrichment-rule) must not contain any white spaces.
</Callout>

### An Example CSV File

In the example CSV file below, the **id** column is what identifies which assets to enrich. When this value matches the value from the asset, that asset with that **id** is enriched with the data in the **Name**, **Email\_address** and **Physical\_address** columns.

<Image alt="SAmpleCSVEnrichmentFile.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAmpleCSVEnrichmentFile.png" />

The asset with **id** of 3 will be enriched with the data from that row in the CSV as follows:

* **Name** - John
* **Email\_address** - [John@example.com](mailto:John@example.com)
* **Physical\_address** - 190 Circle Road

<Callout icon="📘" theme="info">
  Note

  When there is no value in a column for a particular asset, that asset is not enriched with that field. In the example above, the asset with an **id** of **8** would only be enriched with the fields **Name** and **Email\_address**.
</Callout>