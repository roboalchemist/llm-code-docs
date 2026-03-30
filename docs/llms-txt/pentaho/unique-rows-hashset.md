# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/unique-rows-hashset.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/unique-rows-hashset.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/unique-rows-hashset.md

# Unique Rows (HashSet)

The Unique Rows (HashSet) step removes duplicate rows and filters only the unique rows as input data for the step.

This step differs from the Unique Rows transformation step by keeping track of the duplicate rows in memory and does not require a sorted input to process duplicate rows.

**Note:** Because of memory allocation issues, this step is intended for non-client machines. The required amount of memory and hardware will vary based on the size of the data you are processing.
