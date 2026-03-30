# Source: https://docs.pentaho.com/pba-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/data-sources-perspective-ctools-cde/queries-with-parameters.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/data-sources-perspective-ctools-cde/queries-with-parameters.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/data-sources-perspective-ctools-cde/queries-with-parameters.md

# Queries with parameters

Parameterized queries allow for dynamic dashboards by translating user interactions via selectors. For example, you can set a parameterized query for the generation of result sets which reflect the visualization needs of the user. Query parameterization is done by enclosing the parameter name you want to pass to the query in curly brackets preceded by a dollar sign: *${parameterName}*. The following query is an example of a parameterized query. In this query, we want to use the status parameter.

```
select {[Measures].[Sales], [Measures].[Quantity]} ON COLUMNS,
NON EMPTY [Time].Children ON ROWS
from [SteelWheelsSales]
where ([Order Status].[${status}])
```
