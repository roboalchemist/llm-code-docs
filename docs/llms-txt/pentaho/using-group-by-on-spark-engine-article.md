# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/group-by-landing-page-article/select-an-engine-group-by/using-group-by-on-spark-engine-article.md

# Using the Group By step on the Spark engine

You can set up the Group By step to run on the Spark engine.

When Spark is processing the transformation, the rows are sorted by the group fields. The field names cannot contain spaces, dashes, or special characters. Each field name must start with a letter.

Optionally, you can use the Sort step before the Group By step. If your existing transformations contains a Sort step before the Group By step, it will run successfully.

**Note:** The Group By and the Memory Group By steps work the same.
