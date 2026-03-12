# Source: https://docs.pentaho.com/pba-report-designer/add-report-elements-in-report-designer-cp/refer-to-report-elements-by-name-or-column-position.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/add-report-elements-in-report-designer-cp/refer-to-report-elements-by-name-or-column-position.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/add-report-elements-in-report-designer-cp/refer-to-report-elements-by-name-or-column-position.md

# Refer to report elements by name or column position

If you enabled **Display the index columns in the Report Designer's field selectors...** in **Preferences**, you can refer to report elements by field name or by column position. This feature allows you to create a report that isn't locked to a field name, rather it is locked to the position of the query when the report runs; for example, column 0, column 1, column 2, and so on.

Locking to the query can be particularly useful when users create their own queries. When the report renders, the data displays in predictably mapped columns. This feature works with all data field types, groups, and formulas and functions.

Locking elements and formulas to the column position allows report designers to have more flexibility so that a single report can be used with any query regardless of the data source type (JDBC, Mondrian, Pentaho Metadata, and so on.). For example, this feature may be used by a report designer where the designer substitutes fields of report based on different queries that have a completely different set of column names.
