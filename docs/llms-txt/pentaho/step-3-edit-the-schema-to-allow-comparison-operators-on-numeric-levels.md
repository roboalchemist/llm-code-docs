# Source: https://docs.pentaho.com/pba-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-3-edit-the-schema-to-allow-comparison-operators-on-numeric-levels.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-3-edit-the-schema-to-allow-comparison-operators-on-numeric-levels.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-3-edit-the-schema-to-allow-comparison-operators-on-numeric-levels.md

# Step 3: Edit the schema to allow comparison operators on numeric levels

Set the level type in the Mondrian schema to either `Numeric` or `Integer` to enable the comparison operators, as shown below:

`<Dimension foreignKey="CUSTOMERNUMBER" name="Credit Limit"> <Hierarchy hasAll="true" primaryKey="CUSTOMERNUMBER"> <Table name="CUSTOMER_W_TER"> </Table> <Level name="Credit Limit" levelType="Regular" column="CREDITLIMIT" type="Numeric" uniqueMembers="true" hideMemberIf="Never"> <Annotations> <Annotation name="AnalyzerBusinessGroup">Customers</Annotation></Annotations> </Level> </Hierarchy> </Dimension>`

**Note:** If the Level is both Numeric and Time (for example, type = Integer, levelType = TimeYears and Annotation name = AnalyzerDateFormat, then the level will maintain the existing behavior for the relative date operators and not the comparison operators.

## MDX performance

The performance of these comparison operators is highly dependent on the following Mondrian property:

```
# Max number of constraints in a single 'IN' SQL clause.
mondrian.rolap.maxConstraints=1000
```

Under ideal conditions, the join between the numeric level and other report levels is done in the database so that only tuples with data are processed in Mondrian. This can only occur if, after applying the comparison operator, the number of members is less than the **maxConstraints** setting.
