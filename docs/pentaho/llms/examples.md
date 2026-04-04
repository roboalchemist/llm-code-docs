# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/schedules/schedule-reports/set-relative-date-schedules/examples.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/set-relative-date-schedules/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/select-values/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/row-normaliser/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/row-denormaliser/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/regex-evaluation/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/json-input/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/select-values/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/row-normaliser/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/row-denormaliser/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/regex-evaluation/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/json-input/examples.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/discover-metadata-from-a-text-file/examples.md

# Examples

Your Pentaho distribution includes several sample transformations and datasets in the `design-tools/data-integration/samples/transformations/discover-metadata-from-textfile` directory.

The following code is a portion of the `Sample1.txt` file found in the directory:

```
policyID,county,eq_site_limit,eq_site_deductible,point_longitude
710400,CLAY COUNTY,0,0,-81.71624
703001,CLAY COUNTY,0,0,-81.706865
352792,CLAY COUNTY,0,0,-81.718452
717603,CLAY COUNTY,0,0,-81.718452
937659,SUWANNEE COUNTY,0,0,-82.926659
294022,SUWANNEE COUNTY,0,0,-82.926659
410500,SUWANNEE COUNTY,0,0,-82.926659
524433,SUWANNEE COUNTY,218475,0,-82.926155
972562,SUWANNEE COUNTY,0,0,-82.933777

```

When the step is run, the file is scanned to determine a consistent number of fields using the tab character, then the semi-colon, then the comma (default). When the **Header column name detection strategy** is set to **First possible line containing only strings**, the step identifies the first row as the header row. The following table shows the column names and data types.

| column name          | data type |
| -------------------- | --------- |
| policylD2            | Integer   |
| county               | String    |
| eq\_site\_limit      | BigNumber |
| eq\_site\_deductible | Integer   |
| point\_longitude     | BigNumber |

If any of the fields in the first row are numbers or dates, the row is considered data, which means there is no header row in this example.
