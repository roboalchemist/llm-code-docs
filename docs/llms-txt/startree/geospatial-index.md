# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/geospatial-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GeoSpatial Overview

> H3 hexagonal indexing, multiple data formats, and spatial functions for real-time location analytics.

Build location-based analytics with geospatial support powered by Apache Pinot's spatial indexing capabilities. Query geographic data at scale with sub-second performance using H3 hexagonal indexing.

## What is GeoSpatial Support?

GeoSpatial support enables you to:

* **Store and query location data** efficiently using industry-standard formats
* **Perform spatial operations** like distance calculations, containment checks, and area measurements
* **Accelerate spatial queries** using H3 hexagonal indexing for sub-second performance
* **Analyze spatiotemporal data** by combining location and time-series queries

## Key Capabilities

### **GeoSpatial Data Types**

* **Geometry**: For Cartesian plane calculations (meters, feet, etc.)
* **Geography**: For spherical Earth calculations (longitude/latitude)
* **Format Support**: WKT (Well-Known Text), WKB (Well-Known Binary), and **GeoJSON**

### **Spatial Operations**

* Distance calculations (`ST_Distance`)
* Containment relationships (`ST_Within`, `ST_Contains`)
* Area and measurement functions (`ST_Area`)
* Geometric constructors and converters

### **H3 Hexagonal Indexing**

* Hierarchical hexagonal grid system
* Multiple resolution levels for different precision needs
* Dramatically improves query performance
* Industry-standard spatial indexing approach

## Sample Query

Here's a simple example of a geospatial query to find nearby stores:

```sql  theme={null}
SELECT store_name, address, 
       ST_Distance(location, ST_Point(-122.4194, 37.7749)) as distance_meters
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000
ORDER BY distance_meters
LIMIT 10;
```

This query finds all stores within 5km of San Francisco city center, using the H3 index for fast filtering.

## Common Use Cases

### **Location-Based Services**

* Find nearby restaurants, stores, or services
* Delivery radius calculations
* Service area analysis

### **Fleet & Asset Tracking**

* Vehicle location monitoring
* Route optimization
* Geofencing alerts

### **Real Estate & Urban Planning**

* Property search by location
* Market analysis by geographic region
* Demographic studies

### **IoT & Sensor Data**

* Environmental monitoring by location
* Smart city analytics
* Weather and climate analysis

## Performance Benefits

With proper geospatial indexing, you can expect:

* **10-100x faster** spatial queries compared to non-indexed queries
* **Sub-second response times** for complex spatial operations on large datasets
* **Scalable performance** across distributed Pinot clusters
* **Efficient memory usage** through H3's hierarchical structure

## Explore GeoSpatial Documentation

<CardGroup cols={2}>
  <Card title="Data Types & Formats" href="/corecapabilities/manage-data/indexes/geospatial-data-types" icon="globe">
    Learn about geometry vs geography types, WKT, WKB, and GeoJSON format support
  </Card>

  <Card title="Functions Reference" href="/corecapabilities/manage-data/indexes/geospatial-functions" icon="function">
    Complete catalog of geospatial functions including constructors, measurements, and relationships
  </Card>

  <Card title="Index Configuration" href="/corecapabilities/manage-data/indexes/geospatial-configuration" icon="gear">
    H3 index setup, resolution selection, and performance configuration
  </Card>

  <Card title="Performance & Optimization" href="/corecapabilities/manage-data/indexes/geospatial-performance" icon="chart-line">
    Query optimization, performance tuning, and best practices
  </Card>

  <Card title="Examples & Use Cases" href="/corecapabilities/manage-data/indexes/geospatial-examples" icon="code">
    Real-world examples, common patterns, and complete implementations
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
