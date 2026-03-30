# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/discover-metadata-from-a-text-file.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/discover-metadata-from-a-text-file.md

# Discover metadata from a text file

Use the **Discover metadata from a Text file** step to determine the structure and metadata of delimited text files for which you have limited knowledge of the structure. Enter a list of possible delimiters, enclosures, and escape characters to determine the configuration that produces the most consistent match of data in the file. Consistency is determined by the count of fields in the rows. For example, when testing a semi-colon as the delimiter, the count of fields in the first three rows is 3, 8, and 4, which means the field count is inconsistent; therefore, the semi-colon is not the correct delimiter. When testing a comma delimiter on those rows produces a field count of 6, 6, and 6, this is considered a consistent delimiter and is an acceptable candidate for use.

You can use this step to generate data to send to the **ETL Metadata Injection** step. The **ETL Metadata Injection** step can then set up the metadata in the **Text File Input** step for use in your transformations or jobs.

The **Discover metadata from a Text file** step also determines the field names from the header row and predicts the data types for the list of fields.

**Note:** This step opens and reads the file 4 times to gather all the required information. On very large files, this may take a long time if you do not specify a row limit using the **Limit scanned rows** option on the Input tab.
