# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-rules-cp-ag/pdc-manage-metadata-rules-cp.md

# Manage metadata rules

With Data Catalog metadata rules, you can assign business terms, tags, or properties to, or remove them from, already-scanned or ingested metadata. By doing so, you can streamline the process of searching for data while minimizing the potential for errors.

If your assigned role allows it, you see a Metadata Rules card on the Data Catalog Data Operations page. If you have a license for Pentaho Data Optimizer and your assigned role allows it, you can perform additional optimization actions within metadata rules.

Leveraging the Data Optimizer metadata rule engine capabilities, you can simplify data management by setting up rules to automate your data tiering, purging, and rehydration operations. You can use a rule definition on any data source type because rule definitions are data source agnostic, and you can use a single rule to both identify and move data.

The rules engine in Data Optimizer runs within a framework you can use to set the scope and action of rule-performed operations. Use the following workflow when creating metadata rules:

1. Create a rule definition. A rule definition sets the criteria and the action of the rule, which is translated and evaluated into a query for execution against the metadata of any scanned resource.
2. Create a metadata rule. A metadata rule can perform an array of tasks on a selected data source.

You can use the Manage Metadata Rules page to view, create, edit, and delete rule definitions and metadata rules.

**Note:** To perform rules-governed data operations, you may also need to perform some workflow tasks.
