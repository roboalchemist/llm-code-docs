# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/merge-rows-diff/select-an-engine-merge-rows-diff/using-merge-rows-diff-on-spark-engine-article.md

# Using Merge rows (diff) on the Spark engine

You can set up the Merge rows (diff) step to run on the Spark engine. On the Spark engine, Merge rows (diff) compares and merges data from two source datasets into two rows of data, based on key comparison matching. Sorting is not required to produce correct results. Additionally, output from the Merge rows (diff) step is not automatically sorted. When Spark is processing the transformation, the rows are sorted by the group fields. The field names cannot contain spaces, dashes, or special characters. Each field name must start with a letter.
