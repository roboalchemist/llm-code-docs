# Source: https://docs.snowflake.com/en/sql-reference/functions-geospatial.md

# Geospatial functions

Geospatial functions operate on
[GEOGRAPHY](data-types-geospatial.md) and [GEOMETRY](data-types-geospatial.md) and convert GEOGRAPHY and GEOMETRY
values to and from other representations (such as VARCHAR).

| Sub-category | Function | Notes |
| --- | --- | --- |
| Conversion / Input / Parsing | [ST_GEOGFROMGEOHASH](functions/st_geogfromgeohash.md) | GEOGRAPHY only |
|  | [ST_GEOGPOINTFROMGEOHASH](functions/st_geogpointfromgeohash.md) | GEOGRAPHY only |
|  | [ST_GEOGRAPHYFROMWKB](functions/st_geographyfromwkb.md) | GEOGRAPHY only |
|  | [ST_GEOGRAPHYFROMWKT](functions/st_geographyfromwkt.md) | GEOGRAPHY only |
|  | [ST_GEOMETRYFROMWKB](functions/st_geometryfromwkb.md) | GEOMETRY only |
|  | [ST_GEOMETRYFROMWKT](functions/st_geometryfromwkt.md) | GEOMETRY only |
|  | [ST_GEOMFROMGEOHASH](functions/st_geomfromgeohash.md) | GEOMETRY only |
|  | [ST_GEOMPOINTFROMGEOHASH](functions/st_geompointfromgeohash.md) | GEOMETRY only |
|  | [TO_GEOGRAPHY](functions/to_geography.md) | GEOGRAPHY only |
|  | [TO_GEOMETRY](functions/to_geometry.md) | GEOMETRY only |
|  | [TRY_TO_GEOGRAPHY](functions/try_to_geography.md) | GEOGRAPHY only |
|  | [TRY_TO_GEOMETRY](functions/try_to_geometry.md) | GEOMETRY only |
| Conversion / Output / Formatting | [ST_ASGEOJSON](functions/st_asgeojson.md) |  |
|  | [ST_ASWKB](functions/st_aswkb.md) |  |
|  | [ST_ASBINARY](functions/st_aswkb.md) | Alias for ST_ASWKB |
|  | [ST_ASEWKB](functions/st_asewkb.md) |  |
|  | [ST_ASWKT](functions/st_aswkt.md) |  |
|  | [ST_ASTEXT](functions/st_aswkt.md) | Alias for ST_ASWKT |
|  | [ST_ASEWKT](functions/st_asewkt.md) |  |
|  | [ST_GEOHASH](functions/st_geohash.md) |  |
| Constructor Functions | [ST_MAKELINE](functions/st_makeline.md) |  |
|  | [ST_MAKEGEOMPOINT](functions/st_makegeompoint.md) | GEOMETRY only |
|  | [ST_GEOMPOINT](functions/st_makegeompoint.md) | Alias for ST_MAKEGEOMPOINT |
|  | [ST_MAKEPOINT](functions/st_makepoint.md) | GEOGRAPHY only |
|  | [ST_POINT](functions/st_makepoint.md) | Alias for ST_MAKEPOINT |
|  | [ST_MAKEPOLYGON](functions/st_makepolygon.md) |  |
|  | [ST_POLYGON](functions/st_makepolygon.md) | Alias for ST_MAKEPOLYGON |
|  | [ST_MAKEPOLYGONORIENTED](functions/st_makepolygonoriented.md) | GEOGRAPHY only |
| Accessor Functions | [ST_DIMENSION](functions/st_dimension.md) |  |
|  | [ST_ENDPOINT](functions/st_endpoint.md) |  |
|  | [ST_POINTN](functions/st_pointn.md) |  |
|  | [ST_SRID](functions/st_srid.md) |  |
|  | [ST_STARTPOINT](functions/st_startpoint.md) |  |
|  | [ST_X](functions/st_x.md) |  |
|  | [ST_XMAX](functions/st_xmax.md) |  |
|  | [ST_XMIN](functions/st_xmin.md) |  |
|  | [ST_Y](functions/st_y.md) |  |
|  | [ST_YMAX](functions/st_ymax.md) |  |
|  | [ST_YMIN](functions/st_ymin.md) |  |
| Relationship and Measurement Functions | [HAVERSINE](functions/haversine.md) |  |
|  | [ST_AREA](functions/st_area.md) |  |
|  | [ST_AZIMUTH](functions/st_azimuth.md) |  |
|  | [ST_CONTAINS](functions/st_contains.md) |  |
|  | [ST_COVEREDBY](functions/st_coveredby.md) |  |
|  | [ST_COVERS](functions/st_covers.md) |  |
|  | [ST_DISJOINT](functions/st_disjoint.md) |  |
|  | [ST_DISTANCE](functions/st_distance.md) |  |
|  | [ST_DWITHIN](functions/st_dwithin.md) | GEOGRAPHY only |
|  | [ST_HAUSDORFFDISTANCE](functions/st_hausdorffdistance.md) | GEOGRAPHY only |
|  | [ST_INTERSECTS](functions/st_intersects.md) |  |
|  | [ST_LENGTH](functions/st_length.md) |  |
|  | [ST_NPOINTS](functions/st_npoints.md) |  |
|  | [ST_NUMPOINTS](functions/st_npoints.md) | Alias for ST_NPOINTS |
|  | [ST_PERIMETER](functions/st_perimeter.md) |  |
|  | [ST_WITHIN](functions/st_within.md) |  |
| Transformation Functions | [ST_BUFFER](functions/st_buffer.md) | GEOMETRY only |
|  | [ST_CENTROID](functions/st_centroid.md) |  |
|  | [ST_COLLECT](functions/st_collect.md) (Scalar and Aggregate) | GEOGRAPHY only |
|  | [ST_DIFFERENCE](functions/st_difference.md) | GEOGRAPHY only |
|  | [ST_ENVELOPE](functions/st_envelope.md) | Deprecated for GEOGRAPHY |
|  | [ST_INTERPOLATE](functions/st_interpolate.md) | GEOGRAPHY only |
|  | [ST_INTERSECTION](functions/st_intersection.md) | GEOGRAPHY only |
|  | [ST_INTERSECTION_AGG](functions/st_intersection_agg.md) (Scalar and Aggregate) | GEOGRAPHY only |
|  | [ST_SETSRID](functions/st_setsrid.md) | GEOMETRY only |
|  | [ST_SIMPLIFY](functions/st_simplify.md) |  |
|  | [ST_SYMDIFFERENCE](functions/st_symdifference.md) | GEOGRAPHY only |
|  | [ST_TRANSFORM](functions/st_transform.md) | GEOMETRY only |
|  | [ST_UNION](functions/st_union.md) | GEOGRAPHY only |
|  | [ST_UNION_AGG](functions/st_union_agg.md) (Scalar and Aggregate) | GEOGRAPHY only |
| Utility Functions | [ST_ISVALID](functions/st_isvalid.md) |  |
| H3 Functions | [H3_CELL_TO_BOUNDARY](functions/h3_cell_to_boundary.md) | GEOGRAPHY only |
|  | [H3_CELL_TO_CHILDREN](functions/h3_cell_to_children.md) | GEOGRAPHY only |
|  | [H3_CELL_TO_CHILDREN_STRING](functions/h3_cell_to_children_string.md) | GEOGRAPHY only |
|  | [H3_CELL_TO_PARENT](functions/h3_cell_to_parent.md) | GEOGRAPHY only |
|  | [H3_CELL_TO_POINT](functions/h3_cell_to_point.md) | GEOGRAPHY only |
|  | [H3_COMPACT_CELLS](functions/h3_compact_cells.md) | GEOGRAPHY only |
|  | [H3_COMPACT_CELLS_STRINGS](functions/h3_compact_cells_strings.md) | GEOGRAPHY only |
|  | [H3_COVERAGE](functions/h3_coverage.md) | GEOGRAPHY only |
|  | [H3_COVERAGE_STRINGS](functions/h3_coverage_strings.md) | GEOGRAPHY only |
|  | [H3_GET_RESOLUTION](functions/h3_get_resolution.md) | GEOGRAPHY only |
|  | [H3_GRID_DISTANCE](functions/h3_grid_distance.md) | GEOGRAPHY only |
|  | [H3_GRID_DISK](functions/h3_grid_disk.md) | GEOGRAPHY only |
|  | [H3_GRID_PATH](functions/h3_grid_path.md) | GEOGRAPHY only |
|  | [H3_INT_TO_STRING](functions/h3_int_to_string.md) | GEOGRAPHY only |
|  | [H3_IS_PENTAGON](functions/h3_is_pentagon.md) | GEOGRAPHY only |
|  | [H3_IS_VALID_CELL](functions/h3_is_valid_cell.md) | GEOGRAPHY only |
|  | [H3_LATLNG_TO_CELL](functions/h3_latlng_to_cell.md) | GEOGRAPHY only |
|  | [H3_LATLNG_TO_CELL_STRING](functions/h3_latlng_to_cell_string.md) | GEOGRAPHY only |
|  | [H3_POINT_TO_CELL](functions/h3_point_to_cell.md) | GEOGRAPHY only |
|  | [H3_POINT_TO_CELL_STRING](functions/h3_point_to_cell_string.md) | GEOGRAPHY only |
|  | [H3_POLYGON_TO_CELLS](functions/h3_polygon_to_cells.md) | GEOGRAPHY only |
|  | [H3_POLYGON_TO_CELLS_STRINGS](functions/h3_polygon_to_cells_strings.md) | GEOGRAPHY only |
|  | [H3_STRING_TO_INT](functions/h3_string_to_int.md) | GEOGRAPHY only |
|  | [H3_TRY_COVERAGE](functions/h3_try_coverage.md) | GEOGRAPHY only |
|  | [H3_TRY_COVERAGE_STRINGS](functions/h3_try_coverage_strings.md) | GEOGRAPHY only |
|  | [H3_TRY_GRID_DISTANCE](functions/h3_try_grid_distance.md) | GEOGRAPHY only |
|  | [H3_TRY_GRID_PATH](functions/h3_try_grid_path.md) | GEOGRAPHY only |
|  | [H3_TRY_POLYGON_TO_CELLS](functions/h3_try_polygon_to_cells.md) | GEOGRAPHY only |
|  | [H3_TRY_POLYGON_TO_CELLS_STRINGS](functions/h3_try_polygon_to_cells_strings.md) | GEOGRAPHY only |
|  | [H3_UNCOMPACT_CELLS](functions/h3_uncompact_cells.md) | GEOGRAPHY only |
|  | [H3_UNCOMPACT_CELLS_STRINGS](functions/h3_uncompact_cells_strings.md) | GEOGRAPHY only |
