# Source: https://docs.axonius.com/docs/viewing-custom-enriched-fields.md

# Viewing Custom Enriched Fields

Once you save the Custom Enrichment, the information is added to the target Axonius asset, either in an existing field or in a newly created field.
New fields created by Custom Enrichments are labeled with one of the following:

* **Enrichment** - When enriched based on a specific adapter.
* **Common Enrichment** - When enriched based on an aggregated field.

These labels apply whether the enrichments are created through [System Settings](/docs/configuring-enrichment-settings) or via the [Manage Custom Enrichment - Enrich assets with CSV file Enforcement Action](/docs/add-enrichment)(configured with the default settings).

<Callout icon="📘" theme="info">
  Note

  Fields, which are created by Custom Enrichments based on an aggregated field, using the [Manage Custom Enrichment - Enrich assets with CSV file Enforcement Action](/docs/add-enrichment) with the option enabled to write enriched values, are labeled with *Enrichment:* in the EC Artifacts adapter.
  ![ECArtifactsAdapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECArtifactsAdapter.png)
</Callout>

Each Enrichment field can contain more than one value as a list of values, that is if a certain asset answers to more than one rule, it is enriched with them all.

You can use a Query to retrieve the information added to the asset using Custom Enrichment.
The following screen shows a Query that retrieves devices with an Enrichment field (based on a specific adapter).
![EnrichmentEG.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EnrichmentEG.png)

The following screens show a query that retrieves devices with a Common Enrichment field (based on an aggregated adapter; created using System Settings or the [Manage Custom Enrichment - Enrich assets with CSV file Enforcement Action](/docs/add-enrichment) with the default settings), and the Asset Profile page of one of the devices returned by this query showing the enriched field and its values.

![EnrichmentWizard](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EnrichmentWizard.png)

![AssetProfileEnrichmentFIelds](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetProfileEnrichmentFIelds.png)

When Custom Enrichment based on an aggregated field is created using the [Manage Custom Enrichment - Enrich assets with CSV file Enforcement Action](/docs/add-enrichment) with the option enabled to write enriched values to the EC Artifacts adapter, enriched field values from that adapter are added to already existing aggregated fields. This is because values of fields from all adapters in the system (including the EC Artifacts adapter), which share the same name, are aggregated into a common field containing all the values.

In the following example, the Query returns assets with the Email Address value, regardless of whether the value came from the EC Artifacts adapter (enriched) or any other adapter.
![RegularQueryEmail](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RegularQueryEmail.png)