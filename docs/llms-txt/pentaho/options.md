# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/xml-input-stream-stax/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/table-input/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/switch-case/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/sstable-output/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/set-field-value-to-a-constant/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/set-field-value/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-hcp/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mapreduce-output/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mapreduce-input/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mapping/mapping-output-specification/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mapping/mapping-input-specification/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/get-rows-from-result/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/get-records-from-stream/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/csv-file-input/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/couchdb-input/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/xml-input-stream-stax/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/table-input/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/switch-case/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/set-field-value-to-a-constant/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/set-field-value/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-hcp/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapreduce-output/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapreduce-input/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapping/mapping-output-specification/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mapping/mapping-input-specification/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/get-rows-from-result/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/get-records-from-stream/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/csv-file-input/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/couchdb-input/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/options.md

# Options

Errors, warnings, and other information generated as the transformation runs are stored in logs. You can specify how much information is in a log and whether the log is cleared each time through the **Options** section of this window. You can also enable safe mode and specify whether PDI should gather performance metrics. For more informaiton about the logging methods available in PDI, see [Logging and Performance Monitoring](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring).

| Option                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Clear log before running**   | Indicates whether to clear all your logs before you run your transformation. If your log is large, you might need to clear it before the next execution to conserve space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Log level**                  | <p>Specifies how much logging is performed and the amount of information captured:- <strong>Nothing</strong>: No logging occurs.</p><ul><li><strong>Error</strong>: Only errors are logged.</li><li><strong>Minimal</strong>: Only use minimal logging.</li><li><strong>Basic</strong>: This is the default level.</li><li><strong>Detailed</strong>: Give detailed logging output.</li><li><strong>Debug</strong>: For debugging purposes, very detailed output.</li><li><strong>Row Level</strong>: Logging at a row level, which generates a lot of log data.</li></ul><p><strong>Debug</strong> and <strong>Row Level</strong> logging levels contain information you may consider too sensitive to be shown. Consider the sensitivity of your data when selecting these logging levels. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for instructions on how best to use these logging methods.</p> |
| **Enable safe mode**           | Checks every row passed through your transformation and ensure all layouts are identical. If a row does not have the same layout as the first row, an error is generated and reported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Gather performance metrics** | Monitors the performance of your transformation execution through these metrics. [Use performance graphs](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/monitor-performance/use-performance-graphs) shows how to visually analyze these metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
