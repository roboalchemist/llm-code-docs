# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results/pentaho-data-service-sql-support-reference-and-other-development-considerations/other-development-considerations.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results/pentaho-data-service-sql-support-reference-and-other-development-considerations/other-development-considerations.md

# Other development considerations

There are a few considerations to keep in mind as you design your data service and transformation.

* You cannot `JOIN` one data service virtual table to another.
* Pentaho Data Services uses the Memory Group by step to group. This step keeps all the groups in memory to avoid sorts that can slow down the data service. But, if you plan to use many groups, watch your memory consumption on the server to make sure you don't exceed its limits.
* You cannot specify the same field twice in the same `SELECT` clause.
* Calculations and functions like string concatenation are not supported. But, you can do these things in the data service transformation.
