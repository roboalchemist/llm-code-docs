# Source: https://docs.pentaho.com/pba/data-source-model-editor-cp/data-source-model-editor-tips.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/data-source-model-editor-cp/data-source-model-editor-tips.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/data-source-model-editor-cp/data-source-model-editor-tips.md

# Data Source Model Editor tips

The following tips are helpful when working with specific data sources:

* Creating a data source from a CSV file treats all columns as if they are in a single table, with no limitations on where measures come from or which fields can be grouped in a hierarchy.
* Creating a data source from a database table for reporting and analysis requires you to specify a fact table. Only numeric columns from the fact table can be used as measures. Also, all levels in a single hierarchy must come from the same dimension table.
* If you add or edit annotations on the data model in Analyzer, these annotations will not be visible when viewing the model in the Data Source Wizard. For example, if you add a calculated measure to the model in Analyzer, it will not display in the list of measures when viewing the model in the wizard. Saving the model in the wizard will overwrite any annotations which were added to the model in Analyzer.
