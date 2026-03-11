# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/geospatial-performance.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GeoSpatial Performance & Optimization

> Query plan analysis, H3 index tuning, and optimization techniques for high-performance spatial queries.

Optimize geospatial query performance with Apache Pinot. This guide covers everything from basic performance principles to tuning techniques.

<CardGroup cols={2}>
  <Card title="Query Plan Analysis" href="#query-plan-analysis" icon="magnifying-glass">
    Use EXPLAIN PLAN to understand and verify index usage
  </Card>

  <Card title="Index Optimization" href="#index-optimization" icon="gauge-high">
    Configure H3 resolutions for optimal performance
  </Card>

  <Card title="Query Patterns" href="#optimized-query-patterns" icon="code">
    Structure queries to use geospatial indexes effectively
  </Card>

  <Card title="Performance Monitoring" href="#performance-monitoring" icon="chart-line">
    Monitor and measure geospatial query performance
  </Card>
</CardGroup>

## Performance Fundamentals

### **How H3 Index Acceleration Works**

Understanding the two-phase optimization approach is key to writing efficient queries:

<Steps>
  <Step title="Coarse Filtering (H3 Index)">
    The H3 index quickly identifies candidate records within nearby hexagons, eliminating the vast majority of data from consideration.
  </Step>

  <Step title="Precise Filtering (Geospatial Functions)">
    Only records in candidate hexagons undergo expensive precise geospatial calculations (ST\_Distance, ST\_Within, etc.).
  </Step>
</Steps>

**Example: Finding locations within 5km**

* **Without Index**: Calculate exact distance for ALL records (expensive)
* **With H3 Index**:
  1. Find hexagon containing given point
  2. Find hexagons fully contained within the searched area
  3. Include all points associated with those hexagons
  4. Find hexagons overlapping searched area
  5. Calculate exact distance for records in those hexagons

**Important**: If query distance is >100x the hexagon size, the index is automatically bypassed and falls back to full scan for performance reasons.

## Query Plan Analysis

### **Using EXPLAIN PLAN FOR**

The most important tool for geospatial performance optimization:
Single-stage query engine (SSQE):

```sql  theme={null}
EXPLAIN PLAN FOR
SELECT store_name, address, 
       ST_Distance(location, ST_Point(-122.4194, 37.7749)) as distance
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000
ORDER BY distance;
```

Multi-stage query engine MSQE:

```sql  theme={null}
set explainAskingServers=true;
EXPLAIN PLAN FOR
SELECT store_name, address,
       ST_Distance(location, ST_Point(-122.4194, 37.7749)) as distance
FROM stores
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000
ORDER BY distance;
```

Setting `explainAskingServers` query option is necessary for MSQE to show usage of segment-level indexes.

### **Index Usage Operators**

Look for these operators in your query plans:

<Tabs>
  <Tab title="FILTER_H3_INDEX">
    Shows as `FilterH3Index` in MSQE.
    **When**: ST\_Distance with range conditions

    ```sql  theme={null}
    WHERE ST_Distance(location_column, literal_point) < distance
    WHERE ST_Distance(location_column, literal_point) > distance  
    WHERE ST_Distance(location_column, literal_point) BETWEEN min_dist AND max_dist
    ```

    **Query Plan Example**:
    SSQE:

    ```
    BROKER_REDUCE(limit:1000)
    └── COMBINE_SELECT
        └── SELECT(selectList:[store_name, address, distance])
            └── TRANSFORM_PASSTHROUGH(distance:ST_DISTANCE(...))
                └── FILTER_H3_INDEX(predicate:ST_DISTANCE(...) < 5000)
                    └── SEGMENT_SCAN(table:stores)
    ```

    MSQE:

    ```
    PinotLogicalExchange(distribution=[broadcast])
      LeafStageCombineOperator(table=[stores])
        StreamingInstanceResponse
          StreamingCombineSelect
            SelectStreaming(segment=[stores_OFFLINE_0], table=[starbucksStores])
              Project(columns=[[store_name, address, distance]])
                DocIdSet(maxDocs=[10000])
                  FilterH3Index(predicate=[stdistance(...) < '5000.0'], indexLookUp=[h3_index], operator=[RANGE])
    ```
  </Tab>

  <Tab title="INCLUSION_FILTER_H3_INDEX">
    Shows as InclusionFilterH3Index in MSQE.
    **When**: ST\_Within and ST\_Contains functions

    ```sql  theme={null}
    WHERE ST_Within(location_column, literal_polygon)
    WHERE ST_Contains(literal_polygon, location_column)
    ```

    **Query Plan Example**:
    SSQE:

    ```
    BROKER_REDUCE(limit:1000)
    └── COMBINE_SELECT
        └── SELECT(selectList:[store_name, address])
            └── INCLUSION_FILTER_H3_INDEX(predicate:ST_WITHIN(...))
                └── SEGMENT_SCAN(table:stores)
    ```

    MSQE:

    ```
    PinotLogicalExchange(distribution=[broadcast])
      LeafStageCombineOperator(table=[stores])
        StreamingInstanceResponse
          StreamingCombineSelect
            SelectStreaming(segment=[stores_OFFLINE_0], table=[stores])
              Project(columns=[[store_name, address]])
                DocIdSet(maxDocs=[10000])
                  InclusionFilterH3Index(predicate=[stcontains(...) = '1'], operator=[EQ])
    ```
  </Tab>

  <Tab title="No Index Usage">
    **When**: Index not being used (performance problem!)

    ```
    BROKER_REDUCE(limit:1000)
    └── COMBINE_SELECT
        └── SELECT(selectList:[store_name, address])
            └── FILTER(predicate:ST_DISTANCE(...) < 5000)  -- No H3!
                └── SEGMENT_SCAN(table:stores)
    ```

    **Common Causes**:

    * Arguments in wrong order
    * Missing H3 index configuration
    * Dictionary encoding not disabled
  </Tab>
</Tabs>

### **EXPLAIN PLAN Examples**

Here are real examples of what you should see when H3 indexes are working:

**FILTER\_H3\_INDEX Example (ST\_Distance)**:

```sql  theme={null}
EXPLAIN PLAN FOR
SELECT * FROM starbucksStores
WHERE ST_Distance(location_st_point, ST_Point(-122.4194, 37.7749)) < 5000;
```

**Output**:

```
BROKER_REDUCE(limit:10)
COMBINE_SELECT
PLAN_START(numSegmentsForThisPlan:1)
SELECT(selectList:address, lat, location_st_point, lon, name)
PROJECT(name, lon, address, location_st_point, lat)
DOC_ID_SET
FILTER_H3_INDEX
```

**INCLUSION\_FILTER\_H3\_INDEX Example (ST\_Contains)**:

```sql  theme={null}
EXPLAIN PLAN FOR
SELECT * FROM starbucksStores
WHERE ST_Contains(ST_GeomFromText('POLYGON((0 0, 4 0, 4 4, 0 4, 0 0))'), location_st_point);
```

**Output**:

```
BROKER_REDUCE(limit:10)
COMBINE_SELECT
PLAN_START(numSegmentsForThisPlan:1)
SELECT(selectList:address, lat, location_st_point, lon, name)
PROJECT(name, lon, address, location_st_point, lat)
DOC_ID_SET
INCLUSION_FILTER_H3_INDEX
```

**Key Indicators**:

* `FILTER_H3_INDEX` for distance-based queries
* `INCLUSION_FILTER_H3_INDEX` for containment queries
* `DOC_ID_SET` showing efficient document filtering
* No `FILTER` operator (which would indicate full scan)

## Index Optimization

### **Resolution Selection Strategy**

Choose H3 resolutions based on your query patterns and performance requirements:

#### **Single Resolution Approach**

**When to use**: Uniform query patterns with consistent search radius

```json  theme={null}
{
  "indexes": {
    "h3": {
      "resolution": [8]  // ~500m precision, good for city-wide queries
    }
  }
}
```

**Query Performance**:

* Excellent for queries around the target resolution
* Suboptimal for very different search radii

#### **Multi-Resolution Approach** (Recommended)

**When to use**: Varied query patterns with different search radii

```json  theme={null}
{
  "indexes": {
    "h3": {
      "resolution": [5, 8, 11]  // Coarse, medium, fine
    }
  }
}
```

**Resolution Selection Algorithm**:

* **Resolution 5** (8km): For queries >20km radius
* **Resolution 8** (500m): For queries 1-20km radius
* **Resolution 11** (25m): For queries \<1km radius

### **Performance vs Storage Analysis**

| Resolutions        | Query Performance | Storage Overhead | Memory Usage | Use Case          |
| ------------------ | ----------------- | ---------------- | ------------ | ----------------- |
| \[8]               | ⭐⭐⭐               | ⭐⭐⭐⭐⭐            | Low          | Uniform patterns  |
| \[5, 8]            | ⭐⭐⭐⭐              | ⭐⭐⭐⭐             | Medium       | Most applications |
| \[5, 8, 11]        | ⭐⭐⭐⭐⭐             | ⭐⭐⭐              | Medium-High  | Varied patterns   |
| \[3, 6, 9, 12]     | ⭐⭐⭐⭐⭐             | ⭐⭐               | High         | Complex analytics |
| \[1, 4, 7, 10, 13] | ⭐⭐⭐⭐              | ⭐                | Very High    | Over-optimization |

### **Resolution Tuning Examples**

**Retail Store Locator**:

```json  theme={null}
{
  "resolution": [7, 10]  // 1.2km and 65m
}
```

* Resolution 7: "Stores within 5km" queries
* Resolution 10: "Nearest store" precision queries

**Logistics & Delivery**:

```json  theme={null}
{
  "resolution": [4, 7, 10]  // 22km, 1.2km, 65m
}
```

* Resolution 4: Regional route planning
* Resolution 7: City-wide delivery zones
* Resolution 10: Precise delivery locations

**Global IoT Network**:

```json  theme={null}
{
  "resolution": [2, 5, 8, 11]  // 158km, 8km, 500m, 25m
}
```

* Resolution 2: Country/region analysis
* Resolution 5: City-level aggregation
* Resolution 8: Local area monitoring
* Resolution 11: Device-level precision

## Optimized Query Patterns

### **Distance-Based Queries**

**Index-Optimized Patterns**:

```sql  theme={null}
-- Correct argument order (column first, literal second)
WHERE ST_Distance(location_column, ST_Point(-122.4194, 37.7749)) < 5000

-- Range queries work well
WHERE ST_Distance(location_column, ST_Point(-122.4194, 37.7749)) BETWEEN 1000 AND 5000

-- Use with ORDER BY for nearest neighbor
SELECT * FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 10000
ORDER BY ST_Distance(location, ST_Point(-122.4194, 37.7749))
LIMIT 10;
```

**Non-Optimized Patterns**:

```sql  theme={null}
-- Wrong argument order (literal first)
WHERE ST_Distance(ST_Point(-122.4194, 37.7749), location_column) < 5000

-- Both arguments are columns (can't use index)
WHERE ST_Distance(pickup_location, dropoff_location) < 5000

-- Complex expressions in spatial function
WHERE ST_Distance(location, ST_Point(lon_column, lat_column)) < 5000
```

### **Containment Queries**

**ST\_Within Optimization**:

```sql  theme={null}
-- Optimized: column first, literal second  
SELECT * FROM events
WHERE ST_Within(
  event_location,
  ST_GeomFromText('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))')
);

-- Not optimized: literal first
WHERE ST_Within(
  ST_GeomFromText('POLYGON(...)'),
  event_location
);
```

**ST\_Contains Optimization**:

```sql  theme={null}
-- Optimized: literal first, column second
SELECT * FROM delivery_addresses
WHERE ST_Contains(
  ST_GeomFromText('POLYGON((-122.5 37.7, -122.4 37.7, -122.4 37.8, -122.5 37.8, -122.5 37.7))'),
  address_location
);

-- Not optimized: column first  
WHERE ST_Contains(service_area, fixed_point);
```

### **Advanced Query Optimization**

**Multiple Spatial Conditions**:

```sql  theme={null}
-- Combine spatial and non-spatial filters efficiently
SELECT store_name, category
FROM stores 
WHERE category = 'restaurant'  -- Fast filter first
  AND ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 2000  -- Spatial filter
  AND rating > 4.0;  -- Additional filters after spatial
```

**Subquery Optimization**:

```sql  theme={null}
-- Use spatial filtering in subquery to reduce dataset
SELECT s.store_name, s.address, r.avg_rating
FROM (
  SELECT store_id, store_name, address 
  FROM stores 
  WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000
) s
JOIN ratings r ON s.store_id = r.store_id;
```

**Spatial Aggregations**:

```sql  theme={null}
-- Efficient spatial grouping
SELECT 
  region,
  COUNT(*) as store_count,
  AVG(ST_Distance(location, ST_Point(-122.4194, 37.7749))) as avg_distance
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 20000
GROUP BY region
ORDER BY avg_distance;
```

## Performance Monitoring

### **Key Performance Metrics**

<Tabs>
  <Tab title="Query Execution Time">
    **Monitor**:

    * Overall query response time
    * Spatial filter execution time
    * Index effectiveness ratio

    **Tools**:

    ```sql  theme={null}
    -- Enable query execution metrics
    SET enableQueryExecutionMetrics = true;

    -- Run your spatial query and check execution time
    SELECT store_name FROM stores 
    WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;
    ```
  </Tab>

  <Tab title="Index Effectiveness">
    **Measure**: Ratio of filtered docs to total docs

    ```sql  theme={null}
    EXPLAIN PLAN FOR 
    SELECT COUNT(*) FROM stores 
    WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;
    ```

    **Good Ratios**:

    * **>90% filtered**: Excellent index effectiveness
    * **50-90% filtered**: Good performance
    * **\<50% filtered**: Consider different resolutions
  </Tab>

  <Tab title="Resolution Utilization">
    **Check which resolutions are being used**:

    Test different query radii:

    ```sql  theme={null}
    -- Small radius - should use high resolution
    EXPLAIN PLAN FOR SELECT COUNT(*) FROM stores 
    WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 500;

    -- Large radius - should use low resolution  
    EXPLAIN PLAN FOR SELECT COUNT(*) FROM stores
    WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 50000;
    ```
  </Tab>
</Tabs>

### **Performance Benchmarking**

**Create Test Scenarios**:

```sql  theme={null}
-- Benchmark different query patterns
-- Small radius (high precision)
SELECT 'Small Radius' as test_type, COUNT(*) as result_count
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 1000;

-- Medium radius (typical use case)
SELECT 'Medium Radius' as test_type, COUNT(*) as result_count  
FROM stores
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;

-- Large radius (coarse filtering)
SELECT 'Large Radius' as test_type, COUNT(*) as result_count
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 25000;
```

**Performance Comparison**:

```sql  theme={null}
-- Compare indexed vs non-indexed performance
-- (Temporarily disable index for comparison)

-- Time indexed query
SELECT store_name FROM stores_indexed
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;

-- Time non-indexed query  
SELECT store_name FROM stores_no_index
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;
```

## Advanced Optimization Techniques

### **Query Rewriting for Performance**

**Distance Approximation**:

```sql  theme={null}
-- For very large datasets, use approximate filtering first
WITH nearby_candidates AS (
  SELECT store_id, location
  FROM stores 
  WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 6000  -- Slightly larger radius
)
SELECT s.store_name, s.address
FROM nearby_candidates nc
JOIN stores s ON nc.store_id = s.store_id
WHERE ST_Distance(nc.location, ST_Point(-122.4194, 37.7749)) < 5000;  -- Exact filter
```

**Batch Spatial Operations**:

```sql  theme={null}
-- Process multiple locations efficiently
WITH locations_of_interest(location_name, lon, lat) AS (
  VALUES 
    ('SF', -122.4194, 37.7749),
    ('Oakland', -122.2711, 37.8044),
    ('San Jose', -121.8863, 37.3382)
)
SELECT 
  loi.location_name,
  COUNT(*) as nearby_stores
FROM locations_of_interest loi
CROSS JOIN stores s
WHERE ST_Distance(s.location, ST_Point(loi.lon, loi.lat)) < 5000
GROUP BY loi.location_name;
```

### **Memory Optimization**

**Column Selection**:

```sql  theme={null}
-- Select only needed columns
SELECT store_name, address 
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;

-- Avoid SELECT * with spatial data
SELECT * FROM stores  -- Includes large spatial columns
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000;
```

**Result Set Limiting**:

```sql  theme={null}
-- Use LIMIT for interactive queries
SELECT store_name, 
       ST_Distance(location, ST_Point(-122.4194, 37.7749)) as distance
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 10000
ORDER BY distance
LIMIT 20;  -- Only get top 20 results
```

## Troubleshooting Performance Issues

### **Common Performance Problems**

<AccordionGroup>
  <Accordion title="Slow Query Performance">
    **Symptoms**: Queries taking >1 second, high CPU usage

    **Diagnosis**:

    ```sql  theme={null}
    EXPLAIN PLAN FOR your_slow_query;
    ```

    **Solutions**:

    * Verify H3 index operators are present
    * Check argument order in spatial functions
    * Ensure resolutions match query patterns
    * Add additional non-spatial filters
  </Accordion>

  <Accordion title="Index Not Being Used">
    **Symptoms**: EXPLAIN PLAN shows FILTER instead of FILTER\_H3\_INDEX

    **Diagnosis Checklist**:

    * [ ] Column configured with `encodingType: "RAW"`
    * [ ] Column in `noDictionaryColumns` array
    * [ ] H3 index configured with appropriate resolution
    * [ ] Query uses correct argument order
    * [ ] Spatial function is supported (ST\_Distance, ST\_Within, ST\_Contains)
    * [ ] Query distance is not >100x the hexagon size (auto-reverts to full scan)

    **Distance vs Resolution Check**:
    If your query distance is much larger than hexagon size, the H3IndexFilterOperator automatically reverts to non-indexed expression for performance reasons.

    **Fix Example**:

    ```json  theme={null}
    {
      "fieldConfigList": [{
        "name": "location",
        "encodingType": "RAW",  // Must be RAW
        "indexes": {
          "h3": {
            "resolution": [8]  // Single resolution only
          }
        }
      }]
    }
    ```
  </Accordion>

  <Accordion title="High Memory Usage">
    **Symptoms**: Out of memory errors, slow ingestion

    **Solutions**:

    * Reduce number of H3 resolutions (keep 2-3 max)
    * Remove very high resolutions (13-15) if not needed
    * Optimize query to select fewer columns
    * Use LIMIT in interactive queries

    **Memory-Optimized Config**:

    ```json  theme={null}
    {
      "indexes": {
        "h3": {
          "resolution": [6, 9]  // Reduced from [3, 6, 9, 12, 15]
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Poor Index Effectiveness">
    **Symptoms**: High filteredDocs/totalDocs ratio in query plans

    **Analysis**:

    ```sql  theme={null}
    -- Check filtering effectiveness
    EXPLAIN PLAN FOR 
    SELECT COUNT(*) FROM your_table 
    WHERE ST_Distance(location, ST_Point(-122.4, 37.7)) < your_radius;
    ```

    **Solutions**:

    * Adjust H3 resolutions to better match query radius
    * Add complementary non-spatial filters
    * Consider table partitioning strategies
  </Accordion>
</AccordionGroup>

### **Performance Tuning Workflow**

<Steps>
  <Step title="Baseline Measurement">
    Measure current performance and identify bottlenecks using EXPLAIN PLAN and query timing.
  </Step>

  <Step title="Index Configuration">
    Optimize H3 resolutions based on query patterns and test different configurations.
  </Step>

  <Step title="Query Optimization">
    Rewrite queries to use indexes effectively and add non-spatial filters where possible.
  </Step>

  <Step title="Validation">
    Verify improvements using query plans and performance benchmarks.
  </Step>

  <Step title="Monitoring">
    Set up ongoing monitoring of query performance and index effectiveness.
  </Step>
</Steps>

## Best Practices Summary

### **Configuration Best Practices**

* Use 2-3 H3 resolutions for most applications
* Choose resolutions based on typical query radius
* Always disable dictionary encoding (`encodingType: "RAW"`)
* Test resolution configurations with real query patterns

### **Query Best Practices**

* Use correct argument order in spatial functions
* Combine spatial and non-spatial filters efficiently
* Use EXPLAIN PLAN to verify index usage
* Limit result sets in interactive applications

### **Performance Monitoring**

* Monitor query execution times regularly

* Check index effectiveness ratios

* Benchmark different query patterns

* Set up alerts for performance degradation

Built with [Mintlify](https://mintlify.com).
