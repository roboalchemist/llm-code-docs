# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/execute-sql-script-cp/notes-execute-sql-script-pdi-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/execute-sql-script-cp/notes-execute-sql-script-pdi-step.md

# Notes

* Prepared SQL statements are not used due to the scripting and dynamic operation of this step, which can adversely affect transformation performance. If optimal performance is desired, then Pentaho recommends using dedicated steps like [Table Output](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Table%20Output=GUID-F21F31DE-45AA-41B2-90DA-61A952C30276=2=en=.md), [Table Input](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Table%20Input=GUID-54C57371-70B3-4AB4-A2D6-1EAFA7CA713F=2=en=.md), [Update](https://wiki.pentaho.com/display/EAI/Update), or [Delete](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/delete-step-pdi).
* If the transformation halts unexpectedly, verify whether the **Execute for each row?** option is selected. For the SQL to start at the initialization phase of the transformation, ensure that **Execute for each row?** is not selected.
