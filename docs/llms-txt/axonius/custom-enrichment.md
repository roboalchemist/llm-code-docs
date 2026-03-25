# Source: https://docs.axonius.com/docs/custom-enrichment.md

# Custom Enrichment

Use Custom Enrichment to enrich the asset data received from adapters and add columns (fields or aggregated field values) containing additional useful information. This allows you to add a large number of custom or proprietary fields and tailor the data to meet your specific needs.

You can create Custom Enrichments manually through System Settings or automatically using the **Manage Custom Enrichment - Enrich assets with CSV file** Enforcement Action.

To use Custom Enrichment (via an Enforcement Action or System Settings), you need to do the following:

* [Create a statement](/docs/creating-custom-enrichments) that describes how to add information to an asset. The statements are built using syntax similar to SQL.

* Supply a CSV ENUM file that contains the columns that will be added to the asset. See [Creating the Custom Enrichment CSV File](/docs/creating-the-custom-enrichment-csv-file) on how to create the CSV file.

Using the Enforcement Action adds powerful scheduling and customization capabilities to Custom Enrichment, enabling more precise and automated data management.