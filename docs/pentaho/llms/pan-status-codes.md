# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-command-line-tools-to-run-transformations-and-jobs/pan-status-codes.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-command-line-tools-to-run-transformations-and-jobs/pan-status-codes.md

# Pan Status Codes

When you run Pan, there are seven possible return codes that indicate the result of the operation. All of them are defined below.

| Status Code | Definition                                                                  |
| ----------- | --------------------------------------------------------------------------- |
| 0           | The transformation ran without a problem.                                   |
| 1           | Errors occurred during processing                                           |
| 2           | An unexpected error occurred during loading / running of the transformation |
| 3           | Unable to prepare and initialize this transformation                        |
| 7           | The transformation couldn't be loaded from XML or the Repository            |
| 8           | Error loading steps or plugins (error in loading one of the plugins mostly) |
| 9           | Command line usage printing                                                 |
