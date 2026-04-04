# Source: https://docs.pentaho.com/pba-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-2-adjust-for-calculated-members-and-named-sets.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-2-adjust-for-calculated-members-and-named-sets.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-2-adjust-for-calculated-members-and-named-sets.md

# Step 2: Adjust for calculated members and named sets

If your Mondrian schema defines calculated members or named sets that reference MDX members without the dimension prefix, then you must set `mondrian.olap.elements.NeedDimensionPrefix` to `false` in your `mondrian.properties` file. Under all other conditions you would set this property to `true` because it increases Mondrian performance, as well as the readability of the schema XML file.
