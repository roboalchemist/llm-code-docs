# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/text-file-output-cp.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/text-file-output-cp.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/text-file-output-cp.md

# Text File Output

The Text file output step exports data to a text file. This step is commonly used to generate comma separated values (CSV) files that can be read by spreadsheet applications, and can also be used to generate files of a specific length.

**Note:** It is not possible to execute this step in parallel to write to the same file. Instead, use the **Include stepnr in filename** option and then merge the files afterward.
