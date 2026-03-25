# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/unique-rows-hashset/general-unique-rows-hashset-reuse/settings-unique-rows-hashset-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/unique-rows-hashset/general-unique-rows-hashset-reuse/settings-unique-rows-hashset-reuse.md

# Settings

The Unique Rows (HashSet) step requires definitions for the following options and parameters:

| Option                              | Description                                                                                                                                                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Compare using stored row values** | Select this option to store values for the selected fields in memory for every record. Storing row values requires more memory, but it prevents possible false positives if there are hash collisions. |
| **Redirect duplicate row**          | Select this option to process duplicate rows as an error and redirect them to the error stream of the step. If you do not select this option, the duplicate rows are deleted.                          |
| **Error description**               | Specify the error handling description that displays when the step detects duplicate rows. This description is only available when **Redirect duplicate row** is selected.                             |
| **Fields to compare table**         | <p>Specify the field names for which you want to find unique values.</p><p>-OR-</p><p>Select <strong>Get</strong> to insert all the fields from the input stream.</p>                                  |
