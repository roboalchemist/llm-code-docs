# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/execute-row-sql-script-cp.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/execute-row-sql-script-cp.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/execute-row-sql-script-cp.md

# Execute Row SQL Script

The Execute row SQL script step executes an SQL statement or file for every input row, allowing you to dynamically assemble SQL for the creation of indexes, partitions, and tables.

**Note:** Prepared SQL statements are not used due to the scripting and dynamic operation of this step, which can slow transformation performance. For optimal performance, Pentaho recommends using dedicated steps like [Table Output](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Table%20Output=GUID-F21F31DE-45AA-41B2-90DA-61A952C30276=2=en=.md), [Table Input](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Table%20Input=GUID-54C57371-70B3-4AB4-A2D6-1EAFA7CA713F=2=en=.md), [Update](https://wiki.pentaho.com/display/EAI/Update), [Delete](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/delete-step-pdi), etc.
