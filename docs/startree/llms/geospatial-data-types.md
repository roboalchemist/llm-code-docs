# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/geospatial-data-types.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GeoSpatial Data Types & Formats

> Geometry vs geography types, format conversions, and choosing the right spatial data representation.

Apache Pinot supports multiple geospatial data types and formats, enabling you to work with location data in the most appropriate format for your use case.

## Data Type Overview

### **Geometry vs Geography**

Understanding the difference between geometry and geography types is crucial for choosing the right approach for your spatial data:

<CardGroup cols={2}>
  <Card title="Geometry Type" icon="square">
    **Cartesian Plane Calculations**

    * Treats coordinates as X/Y values on a flat surface
    * Distance measurements in coordinate units (often degrees)
    * Best for smaller areas where Earth's curvature is negligible
    * Faster calculations but less accurate over large distances
  </Card>

  <Card title="Geography Type" icon="globe">
    **Spherical Earth Calculations**

    * Accounts for Earth's curvature in all calculations
    * Distance measurements always in meters
    * More accurate for large distances and areas near poles
    * Slightly slower but geographically correct
  </Card>
</CardGroup>

### **When to Use Each Type**

| Use Case                 | Recommended Type | Reason                           |
| ------------------------ | ---------------- | -------------------------------- |
| City-wide analysis       | Geometry         | Fast, sufficient accuracy        |
| Global applications      | Geography        | Accurate across all locations    |
| Small regions (\< 100km) | Either           | Difference is minimal            |
| Navigation/GPS data      | Geography        | Requires precise distances       |
| Engineering/CAD data     | Geometry         | Working in projected coordinates |

## Supported Data Formats

Apache Pinot supports three industry-standard geospatial formats:

### **1. Well-Known Text (WKT)**

Human-readable text format that's easy to understand and debug.

**Supported WKT Types:**

```sql  theme={null}
-- Basic shapes
POINT (longitude latitude)
LINESTRING (x1 y1, x2 y2, x3 y3)
POLYGON ((x1 y1, x2 y2, x3 y3, x1 y1))

-- Multi-geometries  
MULTIPOINT ((x1 y1), (x2 y2))
MULTILINESTRING ((x1 y1, x2 y2), (x3 y3, x4 y4))
MULTIPOLYGON (((x1 y1, x2 y2, x3 y3, x1 y1)), ((x4 y4, x5 y5, x6 y6, x4 y4)))

-- Complex collections
GEOMETRYCOLLECTION(POINT(x1 y1), POLYGON((x2 y2, x3 y3, x4 y4, x2 y2)))
```

**Examples:**

```sql  theme={null}
-- San Francisco coordinates
POINT (-122.4194 37.7749)

-- Simple route
LINESTRING (-122.4194 37.7749, -122.4094 37.7849, -122.3994 37.7949)

-- Golden Gate Park boundary (simplified)
POLYGON ((-122.5137 37.7694, -122.4529 37.7694, -122.4529 37.7849, -122.5137 37.7849, -122.5137 37.7694))
```

### **2. Well-Known Binary (WKB)**

Compact binary format optimized for storage and transmission.

```sql  theme={null}
-- Create from WKB
SELECT ST_GeomFromWKB(wkb_column) FROM spatial_data;

-- Convert to WKB for storage
SELECT ST_AsBinary(ST_Point(-122.4194, 37.7749));
```

### **3. GeoJSON Format**

**NEW**: Full GeoJSON support for modern web applications and APIs.

**Supported GeoJSON Types:**

* Point, LineString, Polygon
* MultiPoint, MultiLineString, MultiPolygon
* GeometryCollection
* Feature, FeatureCollection

#### **GeoJSON Functions**

| Function                     | Purpose                       | Example                              |
| ---------------------------- | ----------------------------- | ------------------------------------ |
| `ST_GeomFromGeoJson(string)` | Create geometry from GeoJSON  | Convert GeoJSON to internal format   |
| `ST_GeogFromGeoJson(string)` | Create geography from GeoJSON | Same but with spherical calculations |
| `ST_AsGeoJson(binary)`       | Convert to GeoJSON            | Export data for web applications     |

#### **GeoJSON Examples**

**Point Geometry:**

```sql  theme={null}
-- Convert GeoJSON to geometry
SELECT ST_AsText(ST_GeomFromGeoJson('{"type":"Point","coordinates":[-122.4194,37.7749]}'))
-- Returns: POINT (-122.4194 37.7749)

-- Convert WKT to GeoJSON  
SELECT ST_AsGeoJson(ST_GeomFromText('POINT (-122.4194 37.7749)'))
-- Returns: {"type":"Point","coordinates":[-122.4194,37.7749],"crs":{"type":"name","properties":{"name":"EPSG:0"}}}
```

**Point Geography:**

```sql  theme={null}
-- Create geography from GeoJSON
SELECT ST_AsGeoJson(ST_GeogFromGeoJson('{"type":"Point","coordinates":[-122.4194,37.7749]}'))
-- Returns: {"type":"Point","coordinates":[-122.4194,37.7749],"crs":{"type":"name","properties":{"name":"EPSG:4326"}}}
```

**Complex Geometries:**

```sql  theme={null}
-- MultiLineString example
SELECT ST_AsGeoJson(ST_GeomFromText('MULTILINESTRING ((1 1, 5 1), (2 4, 4 4))'))
-- Returns:
{
  "type":"MultiLineString",
  "coordinates":[[[1,1],[5,1]],[[2,4],[4,4]]],
  "crs":{"type":"name","properties":{"name":"EPSG:0"}}
}

-- Convert back from GeoJSON
SELECT ST_AsText(ST_GeomFromGeoJson('{"type":"MultiLineString","coordinates":[[[1,1],[5,1]],[[2,4],[4,4]]]}'))
-- Returns: MULTILINESTRING ((1 1, 5 1), (2 4, 4 4))
```

**Feature Collections:**

```sql  theme={null}
-- Working with GeoJSON Features
SELECT ST_GeomFromGeoJson('{
  "type": "Feature",
  "geometry": {
    "type": "Point", 
    "coordinates": [-122.4194, 37.7749]
  },
  "properties": {
    "name": "San Francisco",
    "population": 875000
  }
}')
```

## Data Type Conversion

### **Between Geometry and Geography**

```sql  theme={null}
-- Convert geometry to geography (for spherical calculations)
SELECT toSphericalGeography(ST_GeomFromText('POINT(-122.4194 37.7749)'))

-- Convert geography back to geometry  
SELECT toGeometry(geography_column) FROM my_table
```

### **Format Conversions**

```sql  theme={null}
-- WKT ↔ WKB
SELECT ST_AsText(ST_GeomFromWKB(wkb_data))        -- WKB to WKT
SELECT ST_AsBinary(ST_GeomFromText(wkt_string))   -- WKT to WKB

-- WKT ↔ GeoJSON  
SELECT ST_AsGeoJson(ST_GeomFromText(wkt_string))  -- WKT to GeoJSON
SELECT ST_AsText(ST_GeomFromGeoJson(geojson))     -- GeoJSON to WKT

-- WKB ↔ GeoJSON
SELECT ST_AsGeoJson(ST_GeomFromWKB(wkb_data))     -- WKB to GeoJSON  
SELECT ST_AsBinary(ST_GeomFromGeoJson(geojson))   -- GeoJSON to WKB
```

## Schema Configuration

### **Basic Geospatial Column**

```json  theme={null}
{
  "schemaName": "spatial_data",
  "dimensionFieldSpecs": [
    {
      "name": "location",
      "dataType": "BYTES",
      "transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"
    }
  ]
}
```

### **Transform Function Examples**

Choose the appropriate transform function based on your data source and application requirements:

**For Global Applications** (prefer geography):

```json  theme={null}
{
  "name": "location",
  "dataType": "BYTES",
  "transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"
}
```

**For Regional Analysis** (geometry may be sufficient):

```json  theme={null}
{
  "name": "local_coords", 
  "dataType": "BYTES",
  "transformFunction": "stPoint(x_coordinate, y_coordinate)"
}
```

**For Existing GeoJSON Data**:

```json  theme={null}
{
  "name": "geojson_geom",
  "dataType": "BYTES",
  "transformFunction": "ST_GeogFromGeoJson(geojson_field)"
}
```

## Best Practices

### **Coordinate Order**

<Warning>
  **Important**: Always use longitude, latitude order (X, Y) in functions, which matches GeoJSON standard but differs from some other systems that use latitude, longitude.
</Warning>

```sql  theme={null}
-- Correct: longitude first, latitude second
ST_Point(-122.4194, 37.7749)  -- San Francisco

-- Incorrect: would place point in Antarctica  
ST_Point(37.7749, -122.4194)
```

### **Performance Considerations**

* **Geography calculations** are \~10-20% slower than geometry but more accurate

* **ST\_Distance with geography** only supports point geometries (use geometry types for linestrings/polygons)

* **GeoJSON parsing** has slight overhead compared to WKT

* **WKB format** is most compact for storage

* **Multiple formats** in the same table are supported but increase storage

Built with [Mintlify](https://mintlify.com).
