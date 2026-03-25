# Source: https://docs.snowflake.com/en/release-notes/2024/other/2024-06-28-geospatial-h3-functions-ga.md

# June 28, 2024 — New geospatial H3 functions — *General Availability*

H3 is a [hierarchical geospatial index](https://h3geo.org/docs/highlights/indexing) that partitions
the world into hexagonal cells in a [discrete global grid system](https://en.wikipedia.org/wiki/Discrete_global_grid).

The following H3 functions are now generally available:

* [H3_COMPACT_CELLS](../../../sql-reference/functions/h3_compact_cells.md)
* [H3_COMPACT_CELLS_STRINGS](../../../sql-reference/functions/h3_compact_cells_strings.md)
* [H3_IS_PENTAGON](../../../sql-reference/functions/h3_is_pentagon.md)
* [H3_IS_VALID_CELL](../../../sql-reference/functions/h3_is_valid_cell.md)
* [H3_TRY_COVERAGE](../../../sql-reference/functions/h3_try_coverage.md)
* [H3_TRY_COVERAGE_STRINGS](../../../sql-reference/functions/h3_try_coverage_strings.md)
* [H3_TRY_GRID_DISTANCE](../../../sql-reference/functions/h3_try_grid_distance.md)
* [H3_TRY_GRID_PATH](../../../sql-reference/functions/h3_try_grid_path.md)
* [H3_TRY_POLYGON_TO_CELLS](../../../sql-reference/functions/h3_try_polygon_to_cells.md)
* [H3_TRY_POLYGON_TO_CELLS_STRINGS](../../../sql-reference/functions/h3_try_polygon_to_cells_strings.md)
* [H3_UNCOMPACT_CELLS](../../../sql-reference/functions/h3_uncompact_cells.md)
* [H3_UNCOMPACT_CELLS_STRINGS](../../../sql-reference/functions/h3_uncompact_cells_strings.md)

For more information, see [Geospatial data types](../../../sql-reference/data-types-geospatial.md) and
[Geospatial functions](../../../sql-reference/functions-geospatial.md).
