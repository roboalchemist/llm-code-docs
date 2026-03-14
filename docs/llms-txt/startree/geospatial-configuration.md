# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/geospatial-configuration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GeoSpatial Index Configuration

> H3 resolution selection, schema setup, and index optimization for maximum spatial query performance.

This guide covers everything you need to know about configuring geospatial indexes in Apache Pinot for optimal spatial query performance.

## Overview

Apache Pinot uses **H3 (Hierarchical Hexagons)** indexing system for geospatial operations. H3 divides the Earth's surface into hexagonal cells at multiple resolution levels, enabling fast spatial filtering before applying precise geospatial calculations.

<CardGroup cols={2}>
  <Card title="H3 Indexing Benefits" icon="hexagon">
    * **Fast spatial filtering** using hexagonal grids
    * **Configurable precision** with H3 resolution levels
    * **Hierarchical structure** for efficient range queries
    * **10-100x performance improvement** over non-indexed queries
  </Card>

  <Card title="Configuration Steps" icon="list-check">
    1. Define geospatial column as BYTES in schema
    2. Add transform function for data conversion
    3. Configure H3 index with appropriate resolutions
    4. Disable dictionary encoding (use RAW)
  </Card>
</CardGroup>

## H3 Resolution Levels

Understanding H3 resolution levels is crucial for optimal configuration:

### **Resolution to Precision Mapping**

| Resolution | Hex Edge Length | Hex Area        | Use Case                 |
| ---------- | --------------- | --------------- | ------------------------ |
| 0          | \~1,107 km      | \~4,250,547 km² | Continental analysis     |
| 1          | \~418 km        | \~607,220 km²   | Country-level analysis   |
| 2          | \~158 km        | \~86,745 km²    | State/province level     |
| 3          | \~59 km         | \~12,392 km²    | Regional analysis        |
| 4          | \~22 km         | \~1,770 km²     | Metropolitan areas       |
| 5          | \~8.2 km        | \~252.9 km²     | City-wide analysis       |
| 6          | \~3.1 km        | \~36.1 km²      | Urban districts          |
| 7          | \~1.2 km        | \~5.2 km²       | Neighborhood level       |
| 8          | \~461 m         | \~0.73 km²      | Block-level precision    |
| 9          | \~174 m         | \~0.10 km²      | Building-level precision |
| 10         | \~65 m          | \~0.015 km²     | Property-level precision |
| 11         | \~25 m          | \~0.002 km²     | Room-level precision     |
| 12         | \~9.4 m         | \~0.0003 km²    | Meter-level precision    |
| 13         | \~3.5 m         | \~0.00004 km²   | Sub-meter precision      |
| 14         | \~1.3 m         | \~0.000006 km²  | Centimeter precision     |
| 15         | \~0.5 m         | \~0.0000009 km² | Millimeter precision     |

### **Resolution Selection Guidelines**

<Tabs>
  <Tab title="Use Case Based">
    **Global Applications (0-4)**

    * Cross-country logistics
    * International commerce
    * Climate/weather analysis

    **Regional Applications (5-8)**

    * City-wide services
    * Delivery optimization
    * Urban planning

    **Local Applications (9-12)**

    * Store locators
    * Asset tracking
    * Navigation systems

    **Precision Applications (13-15)**

    * Indoor positioning
    * IoT sensors
    * Robotics/automation
  </Tab>

  <Tab title="Query Pattern Based">
    **Large Radius Queries (>10km)**

    * Use resolutions 3-7
    * Example: "Find all stores within 50km"

    **Medium Radius Queries (1-10km)**

    * Use resolutions 6-10
    * Example: "Find restaurants within 5km"

    **Small Radius Queries (\<1km)**

    * Use resolutions 9-13
    * Example: "Find nearby parking spots"

    **Precision Queries (\<100m)**

    * Use resolutions 11-15
    * Example: "Find exact building entrance"
  </Tab>
</Tabs>

## Basic Configuration

### **Step 1: Schema Configuration**

Define your geospatial column in the table schema:

```json  theme={null}
{
  "schemaName": "spatial_data",
  "dimensionFieldSpecs": [
    {
      "name": "location",
      "dataType": "BYTES",
      "transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"
    }
  ],
  "dateTimeFieldSpecs": [
    {
      "name": "timestamp",
      "dataType": "TIMESTAMP", 
      "format": "1:MILLISECONDS:EPOCH",
      "granularity": "1:MILLISECONDS"
    }
  ]
}
```

### **Step 2: Table Configuration**

Configure the H3 index in your table config:

```json  theme={null}
{
  "tableName": "spatial_data",
  "tableType": "REALTIME",
  "segmentsConfig": {
    "timeColumnName": "timestamp",
    "schemaName": "spatial_data",
    "replication": "1"
  },
  "fieldConfigList": [
    {
      "name": "location",
      "encodingType": "RAW",
      "indexes": {
        "h3": {
          "resolution": [8]
        }
      }
    }
  ],
  "tableIndexConfig": {
    "loadMode": "MMAP",
    "noDictionaryColumns": ["location"]
  }
}
```

## Advanced Configuration Examples

### **Single Resolution Strategy**

Configure a single H3 resolution appropriate for your query patterns:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "location",
      "encodingType": "RAW",
      "indexes": {
        "h3": {
          "resolution": [8]
        }
      }
    }
  ]
}
```

**Why Single Resolution?**
The H3 index operators (`H3IndexFilterOperator` and `H3InclusionIndexFilterOperator`) use only the **lowest (most coarse-grained) resolution** from your configuration. Multiple resolutions provide no performance benefit and may increase storage overhead unnecessarily.

**Distance vs Resolution Matching**:
Choose your resolution based on typical query distances. If your query distance is >100x the hexagon edge length, the index will automatically revert to full scan.

Example:

* **Resolution 8** (hex edge \~461m): Good for queries up to \~46km
* **Resolution 5** (hex edge \~8.2km): Good for queries up to \~820km
* **Resolution 11** (hex edge \~65m): Good for queries up to \~6.5km

### **Legacy Configuration Format**

The older configuration format is still supported:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "location",
      "encodingType": "RAW",
      "indexTypes": ["H3"],
      "properties": {
        "resolutions": "8"
      }
    }
  ]
}
```

<Info>
  **Note**: In legacy format, use "resolutions" as a string. In the current format, use "resolution" as an array.
</Info>

## Transform Function Options

### **Basic Point Creation**

```json  theme={null}
{
  "name": "location",
  "dataType": "BYTES",
  "transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"
}
```

### **From Existing WKT Data**

```json  theme={null}
{
  "name": "geom_location", 
  "dataType": "BYTES",
  "transformFunction": "ST_GeomFromText(wkt_column)"
}
```

### **From GeoJSON Data**

```json  theme={null}
{
  "name": "geojson_location",
  "dataType": "BYTES", 
  "transformFunction": "ST_GeogFromGeoJson(geojson_column)"
}
```

### **Conditional Transform Functions**

```json  theme={null}
{
  "name": "processed_location",
  "dataType": "BYTES",
  "transformFunction": "CASE WHEN longitude IS NOT NULL THEN toSphericalGeography(stPoint(longitude, latitude)) ELSE ST_GeogFromText(wkt_backup) END"
}
```

## Real-World Configuration Examples

### **Ride-Sharing Service**

```json  theme={null}
{
  "schemaName": "ride_requests",
  "dimensionFieldSpecs": [
    {
      "name": "pickup_location",
      "dataType": "BYTES", 
      "transformFunction": "toSphericalGeography(stPoint(pickup_lon, pickup_lat))"
    },
    {
      "name": "dropoff_location",
      "dataType": "BYTES",
      "transformFunction": "toSphericalGeography(stPoint(dropoff_lon, dropoff_lat))"
    }
  ]
}
```

**Table Config:**

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "pickup_location",
      "encodingType": "RAW",
      "indexes": {
        "h3": {
          "resolution": [8]
        }
      }
    },
    {
      "name": "dropoff_location", 
      "encodingType": "RAW",
      "indexes": {
        "h3": {
          "resolution": [8]
        }
      }
    }
  ]
}
```

### **Retail Store Locator**

```json  theme={null}
{
  "schemaName": "stores",
  "dimensionFieldSpecs": [
    {
      "name": "store_location",
      "dataType": "BYTES",
      "transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"
    },
    {
      "name": "delivery_zone",
      "dataType": "BYTES", 
      "transformFunction": "ST_GeogFromText(delivery_polygon_wkt)"
    }  
  ]
}
```

**Table Config:**

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "store_location",
      "encodingType": "RAW", 
      "indexes": {
        "h3": {
          "resolution": [9]
        }
      }
    },
    {
      "name": "delivery_zone",
      "encodingType": "RAW",
      "indexes": {
        "h3": {
          "resolution": [7]
        }
      }
    }
  ]
}
```

### **IoT Sensor Network**

```json  theme={null}
{
  "schemaName": "sensor_readings",
  "dimensionFieldSpecs": [
    {
      "name": "sensor_location", 
      "dataType": "BYTES",
      "transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"
    }
  ]
}
```

**Table Config:**

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "sensor_location",
      "encodingType": "RAW",
      "indexes": {
        "h3": {
          "resolution": [11]
        }
      }
    }
  ]
}
```

## Configuration Best Practices

### **Required Configuration**

1. **Disable dictionary encoding** with `"encodingType": "RAW"` (required for H3 index to work)
2. **Add to noDictionaryColumns** in tableIndexConfig (achieves the same as above - can use both for safety)
3. **Use BYTES data type** for geospatial columns in schema
4. **Choose single resolution** appropriate for your query patterns (only lowest resolution is used by index operators)

### **Common Configuration Errors**

1. **Using "resolutions" instead of "resolution"** in current config format - will cause indexer to fail
2. **Forgetting RAW encoding** - index won't work with dictionary encoding
3. **Using multiple resolutions** - only the lowest resolution is used, others waste storage
4. **Wrong data type** - must use BYTES, not STRING for geospatial columns
5. **Resolution too high for query distances** - when query distance is >100x the hexagon size, index is bypassed and reverts to full scan

## Validation and Testing

### **Verify Index Creation**

Check if your index was created successfully:

```sql  theme={null}
-- Verify index usage with EXPLAIN PLAN
EXPLAIN PLAN FOR 
SELECT * FROM your_table 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;
```

Look for these operators in the query plan:

* `FILTER_H3_INDEX` - Index is being used for ST\_Distance
* `INCLUSION_FILTER_H3_INDEX` - Index is being used for ST\_Within/ST\_Contains

### **Test Query Performance**

```sql  theme={null}
-- Test different query ranges
SELECT COUNT(*) FROM your_table 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 1000;   -- Should use high resolution

SELECT COUNT(*) FROM your_table  
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 50000;  -- Should use low resolution
```

### **Monitor Index Effectiveness**

```sql  theme={null}
-- Compare performance with and without index
-- (Create a duplicate table without index for comparison)

-- Indexed query
SELECT COUNT(*) FROM spatial_data_indexed 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;

-- Non-indexed query  
SELECT COUNT(*) FROM spatial_data_no_index
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;
```

## Migration from Non-Indexed Tables

### **Adding Index to Existing Table**

1. **Update table configuration**:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "existing_location_column",
      "encodingType": "RAW",
      "indexes": {
        "h3": {
          "resolution": [8]
        }
      }
    }
  ]
}
```

1. **Reload table configuration**:

```bash  theme={null}
# Use Pinot admin tools or REST API
curl -X PUT "http://controller:9000/tables/tableName" \
  -H "Content-Type: application/json" \
  -d @updated_table_config.json
```

1. **Refresh/rebuild segments** to apply the new index

```bash  theme={null}
# Use Pinot admin tools or REST API
curl -X POST "http://controller:9000/segments/tableName/reload?type=OFFLINE&forceDownload=false"
```

Built with [Mintlify](https://mintlify.com).
