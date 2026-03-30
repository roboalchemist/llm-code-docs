# Source: https://docs.axonius.com/docs/creating-custom-enrichments.md

# Creating the Custom Enrichment Statement

The general format of an Enrichment Statement is:

enrich Type with Fields on Rule

The first part of the enrichment statement (*enrich 'Type' with 'Fields'* ) determines which data from the CSV is added to the asset. The **Rule** determines which specific assets are enriched.

* In the **Type** field, list the asset type enclosed in single quotes. For example, *'devices'*.
* In the **Fields** field, list the names of the columns in the CSV file, comma separated in parentheses. For example, *(fieldA,fieldB)*. You can also use a wildcard '\*' in the **Fields** field instead of listing all of the columns in the CSV file. The wildcard represents all the columns in the same row. Note that for list fields in the CSV file, only unique values are used to enrich assets.
* In the **Rule** field, enter the rule that defines when the Enrichment will be used. Learn [how to create a Custom Enrichment rule](/docs/creating-the-custom-enrichment-rule).