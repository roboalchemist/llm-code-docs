# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/geospatial-functions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GeoSpatial Functions Reference

> SQL/MM compliant spatial functions for creating, measuring, and analyzing geographic data with practical examples.

Apache Pinot provides a comprehensive set of geospatial functions that follow the SQL/MM specification with the `ST_` prefix. These functions enable you to create, manipulate, measure, and analyze spatial data.

## Function Categories

<CardGroup cols={2}>
  <Card title="Constructors" href="#constructors" icon="hammer">
    Create geospatial objects from coordinates, WKT, WKB, and GeoJSON
  </Card>

  <Card title="Measurements" href="#measurements" icon="ruler">
    Calculate distances, areas, and geometric properties
  </Card>

  <Card title="Relationships" href="#relationships" icon="sitemap">
    Test spatial relationships like containment and intersection
  </Card>

  <Card title="Outputs" href="#outputs" icon="file-export">
    Convert geospatial objects to various formats
  </Card>

  <Card title="Conversions" href="#conversions" icon="arrows-rotate">
    Transform between geometry and geography types
  </Card>

  <Card title="Aggregations" href="#aggregations" icon="layer-group">
    Combine multiple geometries into collections
  </Card>
</CardGroup>

***

## Constructors

Functions for creating geospatial objects from various input formats.

### **ST\_Point**

Creates a point geometry from X,Y coordinates.

```sql  theme={null}
ST_Point(double x, double y) → Point
```

**Examples:**

```sql  theme={null}
-- Create San Francisco point
SELECT ST_Point(-122.4194, 37.7749) as sf_point;

-- Use in query to find nearby locations
SELECT store_name 
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 1000;
```

### **ST\_GeomFromText**

Creates geometry from Well-Known Text (WKT) representation.

```sql  theme={null}
ST_GeomFromText(String wkt) → Geometry
```

**Examples:**

```sql  theme={null}
-- Create various geometry types
SELECT ST_GeomFromText('POINT(-122.4194 37.7749)') as point_geom;
SELECT ST_GeomFromText('LINESTRING(-122.4194 37.7749, -122.4094 37.7849)') as line_geom;
SELECT ST_GeomFromText('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))') as poly_geom;
```

### **ST\_GeomFromWKB**

Creates geometry from Well-Known Binary (WKB) representation.

```sql  theme={null}
ST_GeomFromWKB(bytes wkb) → Geometry
```

**Examples:**

```sql  theme={null}
-- Create geometry from stored WKB data
SELECT ST_GeomFromWKB(wkb_column) FROM spatial_table;

-- Round-trip conversion
SELECT ST_GeomFromWKB(ST_AsBinary(ST_Point(-122.4194, 37.7749)));
```

### **ST\_Polygon**

Creates a polygon geometry from WKT representation.

```sql  theme={null}
ST_Polygon(String wkt) → Polygon
```

**Examples:**

```sql  theme={null}
-- Create a simple rectangle
SELECT ST_Polygon('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))');

-- Use in spatial queries
SELECT * FROM locations 
WHERE ST_Within(point_column, ST_Polygon('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))'));
```

### **ST\_GeogFromText**

Creates geography from Well-Known Text with spherical calculations.

```sql  theme={null}
ST_GeogFromText(String wkt) → Geography
```

**Examples:**

```sql  theme={null}
-- Create geography for accurate distance calculations
SELECT ST_GeogFromText('POINT(-122.4194 37.7749)') as sf_geography;

-- Use with ST_Distance for meter-based results
SELECT ST_Distance(
  ST_GeogFromText('POINT(-122.4194 37.7749)'),
  ST_GeogFromText('POINT(-74.0060 40.7128)')
) as nyc_to_sf_meters;
```

### **ST\_GeogFromWKB**

Creates geography from Well-Known Binary representation.

```sql  theme={null}
ST_GeogFromWKB(bytes wkb) → Geography
```

**Examples:**

```sql  theme={null}
-- Create geography from WKB data column
SELECT ST_GeogFromWKB(wkb_geography_column) FROM geo_table;

-- Convert point to WKB and back to geography
SELECT ST_Point(-122, 37) AS point,
       ST_GeogFromWKB(
         ST_AsBinary(ST_Point(-122, 37))
       ) AS geography_from_wkb
FROM ignoreMe;
```

### **ST\_GeomFromGeoJson**

Creates geometry from GeoJSON string.

```sql  theme={null}
ST_GeomFromGeoJson(string geojson) → Geometry
```

**Examples:**

```sql  theme={null}
-- Create point from GeoJSON
SELECT ST_GeomFromGeoJson('{"type":"Point","coordinates":[-122.4194,37.7749]}');

-- Create polygon from GeoJSON
SELECT ST_GeomFromGeoJson('{
  "type":"Polygon",
  "coordinates":[[
    [-122.5,37.7],[-122.4,37.7],[-122.4,37.8],[-122.5,37.8],[-122.5,37.7]
  ]]
}');

-- Handle Feature objects
SELECT ST_GeomFromGeoJson('{"type":"Feature","geometry":{"type":"Point","coordinates":[-122.4194,37.7749]}}');
```

### **ST\_GeogFromGeoJson**

Creates geography from GeoJSON string.

```sql  theme={null}
ST_GeogFromGeoJson(string geojson) → Geography
```

**Examples:**

```sql  theme={null}
-- Create geography for accurate calculations
SELECT ST_GeogFromGeoJson('{"type":"Point","coordinates":[-122.4194,37.7749]}');

-- Use in distance calculations
SELECT ST_Distance(
  location_geography,
  ST_GeogFromGeoJson('{"type":"Point","coordinates":[-122.4194,37.7749]}')
) as distance_meters FROM stores;
```

***

## Measurements

Functions for calculating spatial measurements and properties.

### **ST\_Distance**

Calculates distance between two geometries or geographies.

```sql  theme={null}
ST_Distance(Geometry/Geography g1, Geometry/Geography g2) → double
```

**For Geometry**: Returns 2D Cartesian distance in coordinate units\
**For Geography**: Returns great-circle distance in meters

<Warning>
  **Geography Limitation**: When using geography types, `ST_Distance` only accepts **POINT** geometries. For other geometry types (LINESTRING, POLYGON), use geometry types instead.
</Warning>

**Examples:**

```sql  theme={null}
-- Distance with geometry types (any geometry supported)
SELECT ST_Distance(
  ST_GeomFromText('LINESTRING(-122.4194 37.7749, -122.4094 37.7849)'),
  ST_GeomFromText('POINT(-74.0060 40.7128)')
) as coordinate_distance;

-- Distance with geography types (points only)
SELECT ST_Distance(
  ST_GeogFromText('POINT(-122.4194 37.7749)'),
  ST_GeogFromText('POINT(-74.0060 40.7128)')
) as meters_distance;

-- Find nearby stores (indexed query)
SELECT store_name, address
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000
ORDER BY ST_Distance(location, ST_Point(-122.4194, 37.7749));
```

### **ST\_Area**

Calculates the area of a polygon geometry or geography.

```sql  theme={null}
ST_Area(Geometry/Geography g) → double
```

**For Geometry**: Returns 2D Euclidean area in coordinate units²\
**For Geography**: Returns area in square meters using spherical model

**Examples:**

```sql  theme={null}
-- Area of a polygon in coordinate units²
SELECT ST_Area(ST_GeomFromText('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))'));

-- Area in square meters using geography
SELECT ST_Area(ST_GeogFromText('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))'));

-- Calculate area of all regions
SELECT region_name, ST_Area(boundary_geography) as area_sqm 
FROM geographic_regions 
ORDER BY area_sqm DESC;
```

### **ST\_GeometryType**

Returns the type of a geometry or geography as a string.

```sql  theme={null}
ST_GeometryType(Geometry/Geography g) → String
```

**Examples:**

```sql  theme={null}
-- Works with geometry types
SELECT ST_GeometryType(ST_Point(-122.4194, 37.7749));  -- Returns: ST_Point
SELECT ST_GeometryType(ST_GeomFromText('LINESTRING(0 0, 1 1)'));  -- Returns: ST_LineString
SELECT ST_GeometryType(ST_GeomFromText('POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))'));  -- Returns: ST_Polygon

-- Works with geography types  
SELECT ST_GeometryType(ST_GeogFromText('POINT(-122.4194 37.7749)'));  -- Returns: ST_Point

-- Filter by geometry type
SELECT * FROM mixed_geometries 
WHERE ST_GeometryType(geom_column) = 'ST_Point';
```

***

## Relationships

Functions for testing spatial relationships between geometries.

### **ST\_Contains**

Tests if the first geometry completely contains the second.

```sql  theme={null}
ST_Contains(Geometry/Geography g1, Geometry/Geography g2) → boolean
```

Returns true if no points of g2 lie outside g1, and at least one interior point of g1 lies in the interior of g2.

<Warning>
  **Note**: ST\_Contains on Geography types provides close approximation, not exact results.
</Warning>

**Examples:**

```sql  theme={null}
-- Check if polygon contains points
SELECT COUNT(*) as points_in_region
FROM locations 
WHERE ST_Contains(
  ST_GeomFromText('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))'),
  location_point
);

-- Boundary vs Interior distinction
-- Returns true: linestring goes from boundary to interior
SELECT ST_Contains(
  ST_GeogFromText('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))'),
  ST_GeogFromText('LINESTRING(-122.5 37.7, -122.45 37.75)')
); -- Returns: 1 (true)

-- Returns false: linestring lies exactly on boundary 
SELECT ST_Contains(
  ST_GeogFromText('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))'),
  ST_GeogFromText('LINESTRING(-122.5 37.7, -122.4 37.7)')
); -- Returns: 0 (false)

-- Find all stores within a delivery zone
SELECT store_name, address
FROM stores 
WHERE ST_Contains(delivery_zone_polygon, store_location);

-- **Index Usage**: First argument must be literal, second must be column
WHERE ST_Contains('<polygon_literal>', point_column)  -- Uses index
```

### **ST\_Within**

Tests if the first geometry is completely within the second.

```sql  theme={null}
ST_Within(Geometry/Geography g1, Geometry/Geography g2) → boolean
```

Returns true if every point of g1 is a point of g2, and the interiors of the two geometries have at least one point in common.

**Examples:**

```sql  theme={null}
-- Find points within a region
SELECT location_name 
FROM locations 
WHERE ST_Within(
  location_point,
  ST_GeomFromText('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))')
);

-- Check if delivery addresses are within service area
SELECT customer_id, address
FROM customers 
WHERE ST_Within(delivery_address, service_boundary);

-- **Index Usage**: First argument must be column, second must be literal
WHERE ST_Within(point_column, '<polygon_literal>')  -- Uses index
```

### **ST\_Equals**

Tests if two geometries or geographies represent the same geometry.

```sql  theme={null}
ST_Equals(Geometry/Geography g1, Geometry/Geography g2) → boolean
```

Returns true if g1 and g2 have at least one point in common, and no point of either lies in the exterior of the other.

**Examples:**

```sql  theme={null}
-- Check if two geometries are identical
SELECT ST_Equals(
  ST_GeomFromText('POINT(-122.4194 37.7749)'),
  ST_Point(-122.4194, 37.7749)
);  -- Returns: true

-- Works with geography types
SELECT ST_Equals(
  ST_GeogFromText('POINT(-122.4194 37.7749)'),
  ST_GeogFromText('POINT(-122.4194 37.7749)')
);  -- Returns: true

-- Find duplicate locations
SELECT COUNT(*) as duplicate_count
FROM locations l1, locations l2 
WHERE l1.id < l2.id 
  AND ST_Equals(l1.location, l2.location);
```

***

## Outputs

Functions for converting geospatial objects to various output formats.

### **ST\_AsText**

Converts geometry or geography to Well-Known Text (WKT).

```sql  theme={null}
ST_AsText(Geometry/Geography g) → string
```

**Examples:**

```sql  theme={null}
-- Convert geometry to readable text
SELECT ST_AsText(location_column) as wkt_location FROM spatial_data;

-- Debug spatial queries
SELECT store_name, ST_AsText(location) as location_wkt
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 1000;
```

### **ST\_AsBinary**

Converts geometry or geography to Well-Known Binary (WKB).

```sql  theme={null}
ST_AsBinary(Geometry/Geography g) → bytes
```

**Examples:**

```sql  theme={null}
-- Convert to binary format for storage
SELECT ST_AsBinary(location_geom) as wkb_data FROM locations;

-- Export binary data
SELECT id, ST_AsBinary(boundary) as boundary_wkb 
FROM regions 
WHERE region_type = 'administrative';
```

### **ST\_AsGeoJson**

Converts geometry or geography to GeoJSON format.

```sql  theme={null}
ST_AsGeoJson(Geometry/Geography g) → string
```

**Examples:**

```sql  theme={null}
-- Convert point to GeoJSON
SELECT ST_AsGeoJson(ST_Point(-122.4194, 37.7749));
-- Returns: {"type":"Point","coordinates":[-122.4194,37.7749],"crs":{"type":"name","properties":{"name":"EPSG:0"}}}

-- Export data for web applications
SELECT 
  store_name,
  ST_AsGeoJson(location) as geojson_location,
  category
FROM stores 
WHERE city = 'San Francisco';

-- Create GeoJSON FeatureCollection-ready output
SELECT json_object(
  'type', 'Feature',
  'geometry', json(ST_AsGeoJson(location)),
  'properties', json_object('name', store_name, 'category', category)
) as geojson_feature
FROM stores;
```

***

## Conversions

Functions for converting between geometry and geography types.

### **toSphericalGeography**

Converts a Geometry object to spherical geography.

```sql  theme={null}
toSphericalGeography(Geometry g) → Geography
```

**Examples:**

```sql  theme={null}
-- Convert geometry to geography for accurate distance calculations
SELECT toSphericalGeography(ST_GeomFromText('POINT(-122.4194 37.7749)'));

-- Use in transform functions
"transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"

-- Convert existing geometry column
SELECT 
  location_name,
  ST_Distance(
    toSphericalGeography(geometry_location),
    toSphericalGeography(ST_Point(-122.4194, 37.7749))
  ) as distance_meters
FROM locations;
```

### **toGeometry**

Converts a spherical geography object to geometry.

```sql  theme={null}
toGeometry(Geography g) → Geometry
```

**Examples:**

```sql  theme={null}
-- Convert geography back to geometry
SELECT toGeometry(geography_column) FROM spatial_data;

-- Use when you need faster calculations over small areas
SELECT location_name
FROM locations 
WHERE ST_Distance(
  toGeometry(geography_location),
  toGeometry(reference_geography)
) < 0.01;  -- Approximate distance in degrees
```

***

## Aggregations

Functions for combining multiple geometries.

### **ST\_Union**

Combines multiple geometries into a single MULTI geometry.

```sql  theme={null}
ST_Union(geometry[] g1_array) → Geometry
```

This aggregate function returns a MULTI geometry or NON-MULTI geometry from a set of geometries. It ignores NULL geometries.

**Examples:**

```sql  theme={null}
-- Combine all store locations into a MultiPoint
SELECT ST_Union(ARRAY_AGG(location)) as all_store_locations
FROM stores 
WHERE city = 'San Francisco';

-- Create union of all delivery zones
SELECT region, ST_Union(ARRAY_AGG(delivery_polygon)) as combined_delivery_area
FROM delivery_zones 
GROUP BY region;

-- Combine geometries by category
SELECT 
  store_category,
  ST_AsText(ST_Union(ARRAY_AGG(location))) as combined_locations
FROM stores 
GROUP BY store_category;
```

***

## Function Usage with Indexes

### **Functions that Use H3 Index**

These functions automatically leverage geospatial indexes when properly configured:

| Function      | Index Usage                  | Requirements                                                    |
| ------------- | ---------------------------- | --------------------------------------------------------------- |
| `ST_Distance` | FILTER\_H3\_INDEX            | Column as first arg, literal as second, used in range condition |
| `ST_Within`   | INCLUSION\_FILTER\_H3\_INDEX | Column as first arg, literal as second                          |
| `ST_Contains` | INCLUSION\_FILTER\_H3\_INDEX | Literal as first arg, column as second                          |

**Index-Optimized Query Patterns:**

```sql  theme={null}
-- These queries use the H3 index:
WHERE ST_Distance(location_column, ST_Point(-122, 37)) < 5000
WHERE ST_Within(location_column, ST_GeomFromText('POLYGON(...)'))  
WHERE ST_Contains(ST_GeomFromText('POLYGON(...)'), location_column)

-- These queries do NOT use the index:
WHERE ST_Distance(ST_Point(-122, 37), location_column) < 5000  -- Arguments reversed
WHERE ST_Within(ST_GeomFromText('POLYGON(...)'), location_column)  -- Arguments reversed
```

### **Checking Index Usage**

Use `EXPLAIN PLAN FOR` to verify index usage:

```sql  theme={null}
EXPLAIN PLAN FOR 
SELECT * FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;
```

Look for these operators in the query plan:

* `FILTER_H3_INDEX` - ST\_Distance queries using index
* `INCLUSION_FILTER_H3_INDEX` - ST\_Within/ST\_Contains queries using index

***

## Best Practices

### **Performance Tips**

* **Use geography types** for global applications requiring meter-based distances
* **Use geometry types** for regional analysis where coordinate units are acceptable
* **Index your spatial columns** with appropriate H3 resolutions
* **Structure queries** to leverage indexes (proper argument order)

### **Function Selection Guide**

```sql  theme={null}
-- For distance-based queries
ST_Distance + geography types = Most accurate (points only)
ST_Distance + geometry types = Faster, accepts any geometry type

-- For containment queries  
ST_Within = Point-in-polygon testing
ST_Contains = Polygon-contains-point testing (reverse of ST_Within)

-- For data export
ST_AsGeoJson = Modern web applications
ST_AsText = Debugging and human-readable output
ST_AsBinary = Compact storage and transmission
```

Built with [Mintlify](https://mintlify.com).
