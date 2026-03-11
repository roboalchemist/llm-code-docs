# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/geospatial-examples.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GeoSpatial Examples & Use Cases

> Industry-specific implementations from retail to IoT, with complete schemas, configurations, and optimized queries.

Explore practical implementations of geospatial analytics with Apache Pinot through real-world examples and industry-specific use cases.

<CardGroup cols={2}>
  <Card title="Location-Based Services" href="#location-based-services" icon="map-pin">
    Store locators, service areas, and proximity analysis
  </Card>

  <Card title="Transportation & Logistics" href="#transportation--logistics" icon="truck">
    Fleet tracking, route optimization, and delivery management
  </Card>

  <Card title="Real Estate & Urban Planning" href="#real-estate--urban-planning" icon="building">
    Property analysis, market research, and urban analytics
  </Card>

  <Card title="IoT & Sensor Networks" href="#iot--sensor-networks" icon="wifi">
    Environmental monitoring, smart cities, and sensor analytics
  </Card>
</CardGroup>

## Quick Start Example

Here's a step-by-step example to get you started with GeoSpatial queries:

### **1. Schema Definition**

Define your geospatial column in the table schema:

```json  theme={null}
{
  "schemaName": "stores",
  "dimensionFieldSpecs": [
    {
      "name": "store_name",
      "dataType": "STRING"
    },
    {
      "name": "address",
      "dataType": "STRING"
    },
    {
      "name": "location",
      "dataType": "BYTES",
      "transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"
    }
  ]
}
```

### **2. Index Configuration**

Configure the H3 index in your table configuration:

```json  theme={null}
{
  "tableName": "stores",
  "tableType": "REALTIME",
  "fieldConfigList": [
    {
      "name": "location",
      "encodingType": "RAW",
      "indexes": {
        "h3": {
          "resolution": [5, 8, 11]
        }
      }
    }
  ],
  "tableIndexConfig": {
    "noDictionaryColumns": ["location"]
  }
}
```

### **3. Sample Queries**

**Find nearby stores:**

```sql  theme={null}
SELECT store_name, address, 
       ST_Distance(location, ST_Point(-122.4194, 37.7749)) as distance_meters
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000
ORDER BY distance_meters
LIMIT 10;
```

**Count stores by distance range:**

```sql  theme={null}
SELECT 
  CASE 
    WHEN ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 1000 THEN 'Within 1km'
    WHEN ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000 THEN '1-5km away'
    ELSE 'More than 5km'
  END as distance_range,
  COUNT(*) as store_count
FROM stores
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 10000
GROUP BY distance_range;
```

## Complete Implementation Examples

### **Store Locator Application**

**Scenario**: Build a store locator that finds nearby locations with performance optimizations.

#### **Schema & Configuration**

```json  theme={null}
{
  "schemaName": "store_locations",
  "dimensionFieldSpecs": [
    {
      "name": "store_id",
      "dataType": "STRING"
    },
    {
      "name": "store_name", 
      "dataType": "STRING"
    },
    {
      "name": "address",
      "dataType": "STRING"
    },
    {
      "name": "city",
      "dataType": "STRING"
    },
    {
      "name": "category",
      "dataType": "STRING"
    },
    {
      "name": "location",
      "dataType": "BYTES",
      "transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"
    },
    {
      "name": "service_area",
      "dataType": "BYTES", 
      "transformFunction": "ST_GeogFromText(service_polygon_wkt)"
    }
  ],
  "metricFieldSpecs": [
    {
      "name": "rating",
      "dataType": "DOUBLE"
    },
    {
      "name": "review_count",
      "dataType": "INT"
    }
  ]
}
```

**Table Configuration:**

```json  theme={null}
{
  "tableName": "store_locations",
  "tableType": "REALTIME",
  "fieldConfigList": [
    {
      "name": "location",
      "encodingType": "RAW",
      "indexes": {
        "h3": {
          "resolution": [7, 10]
        }
      }
    },
    {
      "name": "service_area", 
      "encodingType": "RAW",
      "indexes": {
        "h3": {
          "resolution": [5, 8]
        }
      }
    }
  ],
  "tableIndexConfig": {
    "noDictionaryColumns": ["location", "service_area"]
  }
}
```

#### **Common Queries**

**Find Nearest Stores:**

```sql  theme={null}
SELECT 
  store_name,
  address, 
  category,
  rating,
  ST_Distance(location, ST_Point(-122.4194, 37.7749)) as distance_meters
FROM store_locations 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000
  AND rating >= 4.0
ORDER BY distance_meters
LIMIT 10;
```

**Store Density Analysis:**

```sql  theme={null}
SELECT 
  city,
  category,
  COUNT(*) as store_count,
  AVG(rating) as avg_rating,
  AVG(ST_Distance(location, ST_Point(-122.4194, 37.7749))) as avg_distance_from_center
FROM store_locations 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 25000
GROUP BY city, category
ORDER BY store_count DESC;
```

**Service Area Coverage:**

```sql  theme={null}
-- Find which stores can serve a specific location
SELECT 
  store_name,
  address,
  'delivers_to_location' as service_type
FROM store_locations 
WHERE ST_Contains(service_area, ST_Point(-122.4094, 37.7849))
UNION ALL
-- Find stores within walking distance
SELECT 
  store_name,
  address, 
  'walking_distance' as service_type
FROM store_locations
WHERE ST_Distance(location, ST_Point(-122.4094, 37.7849)) < 800;
```

***

## Location-Based Services

### **Food Delivery Platform**

**Use Case**: Real-time delivery optimization and customer matching.

#### **Dynamic Delivery Radius**

```sql  theme={null}
-- Find available restaurants based on delivery capacity and distance
WITH restaurant_capacity AS (
  SELECT 
    restaurant_id,
    location,
    CASE 
      WHEN active_orders < 10 THEN 5000  -- Extended radius when less busy
      WHEN active_orders < 20 THEN 3000  -- Standard radius
      ELSE 1500                          -- Reduced radius when busy
    END as delivery_radius
  FROM restaurants 
  WHERE is_open = true
)
SELECT 
  r.restaurant_name,
  r.cuisine_type,
  r.avg_delivery_time,
  ST_Distance(r.location, ST_Point(-122.4194, 37.7749)) as distance_meters
FROM restaurant_capacity rc
JOIN restaurants r ON rc.restaurant_id = r.restaurant_id
WHERE ST_Distance(rc.location, ST_Point(-122.4194, 37.7749)) < rc.delivery_radius
ORDER BY distance_meters, r.avg_delivery_time;
```

#### **Delivery Driver Optimization**

```sql  theme={null}
-- Find optimal driver assignments based on location and capacity
SELECT 
  d.driver_id,
  d.driver_name,
  COUNT(o.order_id) as current_orders,
  ST_Distance(d.current_location, ST_Point(-122.4194, 37.7749)) as distance_to_pickup,
  AVG(ST_Distance(o.delivery_location, ST_Point(-122.4194, 37.7749))) as avg_delivery_distance
FROM drivers d
LEFT JOIN active_orders o ON d.driver_id = o.assigned_driver
WHERE d.is_available = true
  AND ST_Distance(d.current_location, ST_Point(-122.4194, 37.7749)) < 3000
GROUP BY d.driver_id, d.driver_name, d.current_location
HAVING COUNT(o.order_id) < 3
ORDER BY distance_to_pickup, current_orders;
```

### **Healthcare Facility Finder**

**Use Case**: Emergency services and healthcare accessibility analysis.

```sql  theme={null}
-- Find nearest hospitals with specific capabilities
SELECT 
  h.hospital_name,
  h.hospital_type,
  h.capabilities,
  h.emergency_services,
  ST_Distance(h.location, ST_Point(-122.4194, 37.7749)) as distance_meters,
  h.wait_time_minutes
FROM hospitals h
WHERE ST_Distance(h.location, ST_Point(-122.4194, 37.7749)) < 15000
  AND h.emergency_services = true
  AND h.capabilities LIKE '%cardiology%'
  AND h.current_capacity > 0
ORDER BY 
  CASE 
    WHEN h.hospital_type = 'Level 1 Trauma' THEN 1
    WHEN h.hospital_type = 'Level 2 Trauma' THEN 2  
    ELSE 3
  END,
  distance_meters;
```

**Healthcare Accessibility Analysis:**

```sql  theme={null}
-- Analyze healthcare coverage by area
WITH coverage_areas AS (
  SELECT 
    ST_Point(longitude, latitude) as area_center,
    neighborhood_name,
    population
  FROM census_blocks
),
nearest_hospital AS (
  SELECT 
    ca.neighborhood_name,
    ca.population,
    MIN(ST_Distance(ca.area_center, h.location)) as distance_to_nearest_hospital,
    COUNT(CASE WHEN ST_Distance(ca.area_center, h.location) < 5000 THEN 1 END) as hospitals_within_5km
  FROM coverage_areas ca
  CROSS JOIN hospitals h
  GROUP BY ca.neighborhood_name, ca.population
)
SELECT 
  neighborhood_name,
  population,
  distance_to_nearest_hospital,
  hospitals_within_5km,
  CASE 
    WHEN distance_to_nearest_hospital > 10000 THEN 'Underserved'
    WHEN distance_to_nearest_hospital > 5000 THEN 'Limited Access'
    ELSE 'Good Access'
  END as accessibility_level
FROM nearest_hospital
ORDER BY distance_to_nearest_hospital DESC;
```

***

## Transportation & Logistics

### **Fleet Management System**

**Schema for Vehicle Tracking:**

```json  theme={null}
{
  "schemaName": "vehicle_tracking",
  "dimensionFieldSpecs": [
    {
      "name": "vehicle_id",
      "dataType": "STRING"
    },
    {
      "name": "driver_id", 
      "dataType": "STRING"
    },
    {
      "name": "location",
      "dataType": "BYTES",
      "transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"
    },
    {
      "name": "route_polygon",
      "dataType": "BYTES",
      "transformFunction": "ST_GeogFromText(route_wkt)"
    }
  ],
  "metricFieldSpecs": [
    {
      "name": "speed_kmh",
      "dataType": "DOUBLE"
    },
    {
      "name": "fuel_level",
      "dataType": "DOUBLE"
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

#### **Route Deviation Detection**

```sql  theme={null}
-- Identify vehicles that have deviated from their assigned routes
SELECT 
  v.vehicle_id,
  v.driver_id,
  v.timestamp,
  ST_AsText(v.location) as current_position,
  ST_Distance(v.location, 
    (SELECT location FROM route_waypoints rw 
     WHERE rw.route_id = v.assigned_route_id 
     ORDER BY ST_Distance(rw.location, v.location) 
     LIMIT 1)
  ) as deviation_distance_meters
FROM vehicle_tracking v
WHERE ST_Within(v.location, v.route_polygon) = false
  AND v.timestamp >= now() - INTERVAL '1' HOUR
  AND v.speed_kmh > 5  -- Exclude parked vehicles
ORDER BY deviation_distance_meters DESC;
```

#### **Geofencing Alerts**

```sql  theme={null}
-- Monitor vehicles entering/exiting specific zones
WITH zone_events AS (
  SELECT 
    v.vehicle_id,
    v.timestamp,
    z.zone_name,
    z.zone_type,
    CASE 
      WHEN ST_Within(v.location, z.zone_polygon) THEN 'ENTERED'
      WHEN ST_Distance(v.location, z.zone_polygon) < 100 THEN 'APPROACHING'
      ELSE 'OUTSIDE'
    END as zone_status
  FROM vehicle_tracking v
  CROSS JOIN geofence_zones z
  WHERE v.timestamp >= now() - INTERVAL '5' MINUTES
    AND (ST_Within(v.location, z.zone_polygon) 
         OR ST_Distance(v.location, z.zone_polygon) < 500)
)
SELECT 
  vehicle_id,
  zone_name,
  zone_type,
  zone_status,
  COUNT(*) as status_changes
FROM zone_events
WHERE zone_type IN ('RESTRICTED', 'CUSTOMER_SITE', 'DEPOT')
GROUP BY vehicle_id, zone_name, zone_type, zone_status
HAVING COUNT(*) > 1  -- Detect multiple status changes (potential issues)
ORDER BY status_changes DESC;
```

### **Airport Operations Analytics**

#### **Aircraft Positioning & Runway Management**

```sql  theme={null}
-- Monitor aircraft positions and runway conflicts
SELECT 
  a.flight_id,
  a.aircraft_type,
  a.status,
  ST_AsText(a.current_position) as position,
  r.runway_id,
  ST_Distance(a.current_position, r.runway_centerline) as distance_to_runway,
  CASE 
    WHEN ST_Within(a.current_position, r.runway_safety_zone) THEN 'IN_SAFETY_ZONE'
    WHEN ST_Distance(a.current_position, r.runway_centerline) < 100 THEN 'APPROACHING'
    ELSE 'CLEAR'
  END as runway_proximity
FROM aircraft_positions a
CROSS JOIN airport_runways r
WHERE a.airport_code = 'SFO'
  AND a.timestamp >= now() - INTERVAL '10' MINUTES
  AND (a.status IN ('LANDING', 'TAKEOFF', 'TAXIING') 
       OR ST_Distance(a.current_position, r.runway_centerline) < 500)
ORDER BY distance_to_runway;
```

***

## Real Estate & Urban Planning

### **Property Market Analysis**

#### **Comprehensive Property Valuation**

```sql  theme={null}
-- Analyze property values based on location and nearby amenities
WITH property_amenities AS (
  SELECT 
    p.property_id,
    p.address,
    p.price,
    p.square_feet,
    p.location,
    COUNT(CASE WHEN a.type = 'school' 
               AND ST_Distance(p.location, a.location) < 1000 THEN 1 END) as schools_nearby,
    COUNT(CASE WHEN a.type = 'transit' 
               AND ST_Distance(p.location, a.location) < 500 THEN 1 END) as transit_nearby,
    COUNT(CASE WHEN a.type = 'park' 
               AND ST_Distance(p.location, a.location) < 1000 THEN 1 END) as parks_nearby,
    MIN(CASE WHEN a.type = 'shopping' 
             THEN ST_Distance(p.location, a.location) END) as distance_to_shopping
  FROM properties p
  CROSS JOIN amenities a
  WHERE ST_Distance(p.location, a.location) < 2000
  GROUP BY p.property_id, p.address, p.price, p.square_feet, p.location
)
SELECT 
  property_id,
  address,
  price,
  price / square_feet as price_per_sqft,
  schools_nearby,
  transit_nearby, 
  parks_nearby,
  distance_to_shopping,
  -- Walkability score based on amenities
  (schools_nearby * 2 + transit_nearby * 3 + parks_nearby + 
   CASE WHEN distance_to_shopping < 800 THEN 3 ELSE 0 END) as walkability_score
FROM property_amenities
ORDER BY walkability_score DESC, price_per_sqft;
```

#### **Market Trend Analysis by Neighborhood**

```sql  theme={null}
-- Analyze price trends and market dynamics by geographic area
WITH neighborhood_analysis AS (
  SELECT 
    n.neighborhood_name,
    ST_Centroid(n.boundary_polygon) as neighborhood_center,
    COUNT(p.property_id) as total_properties,
    AVG(p.price) as avg_price,
    AVG(p.price / p.square_feet) as avg_price_per_sqft,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY p.price) as median_price,
    COUNT(CASE WHEN p.sale_date >= now() - INTERVAL '90' DAY THEN 1 END) as recent_sales
  FROM neighborhoods n
  JOIN properties p ON ST_Within(p.location, n.boundary_polygon)
  WHERE p.sale_date >= now() - INTERVAL '1' YEAR
  GROUP BY n.neighborhood_name, n.boundary_polygon
)
SELECT 
  na.neighborhood_name,
  na.total_properties,
  na.avg_price,
  na.avg_price_per_sqft,
  na.median_price,
  na.recent_sales,
  -- Calculate nearby neighborhood competition
  AVG(nearby.avg_price_per_sqft) as nearby_avg_price_per_sqft,
  na.avg_price_per_sqft - AVG(nearby.avg_price_per_sqft) as price_premium
FROM neighborhood_analysis na
JOIN neighborhood_analysis nearby 
  ON ST_Distance(na.neighborhood_center, nearby.neighborhood_center) < 5000
  AND na.neighborhood_name != nearby.neighborhood_name
GROUP BY na.neighborhood_name, na.total_properties, na.avg_price, 
         na.avg_price_per_sqft, na.median_price, na.recent_sales
ORDER BY price_premium DESC;
```

### **Urban Planning & Development**

#### **Population Density & Infrastructure Analysis**

```sql  theme={null}
-- Analyze population density and infrastructure adequacy
SELECT 
  cb.census_block_id,
  cb.population,
  ST_Area(cb.boundary_polygon) / 1000000 as area_km2,  -- Convert to km²
  cb.population / (ST_Area(cb.boundary_polygon) / 1000000) as population_density_per_km2,
  COUNT(CASE WHEN i.type = 'hospital' 
             AND ST_Distance(ST_Centroid(cb.boundary_polygon), i.location) < 5000 
             THEN 1 END) as hospitals_within_5km,
  COUNT(CASE WHEN i.type = 'school' 
             AND ST_Distance(ST_Centroid(cb.boundary_polygon), i.location) < 2000 
             THEN 1 END) as schools_within_2km,
  COUNT(CASE WHEN i.type = 'fire_station' 
             AND ST_Distance(ST_Centroid(cb.boundary_polygon), i.location) < 3000 
             THEN 1 END) as fire_stations_within_3km,
  -- Infrastructure adequacy score
  CASE 
    WHEN cb.population / (ST_Area(cb.boundary_polygon) / 1000000) > 10000 THEN 'High Density'
    WHEN cb.population / (ST_Area(cb.boundary_polygon) / 1000000) > 5000 THEN 'Medium Density'
    ELSE 'Low Density'
  END as density_category
FROM census_blocks cb
CROSS JOIN infrastructure i
WHERE ST_Distance(ST_Centroid(cb.boundary_polygon), i.location) < 10000
GROUP BY cb.census_block_id, cb.population, cb.boundary_polygon
ORDER BY population_density_per_km2 DESC;
```

***

## IoT & Sensor Networks

### **Environmental Monitoring System**

#### **Air Quality Analysis**

```json  theme={null}
{
  "schemaName": "air_quality_sensors",
  "dimensionFieldSpecs": [
    {
      "name": "sensor_id",
      "dataType": "STRING"
    },
    {
      "name": "sensor_location", 
      "dataType": "BYTES",
      "transformFunction": "toSphericalGeography(stPoint(longitude, latitude))"
    },
    {
      "name": "region",
      "dataType": "STRING"
    }
  ],
  "metricFieldSpecs": [
    {
      "name": "pm25_level",
      "dataType": "DOUBLE"
    },
    {
      "name": "pm10_level", 
      "dataType": "DOUBLE"
    },
    {
      "name": "ozone_level",
      "dataType": "DOUBLE"
    },
    {
      "name": "temperature_celsius",
      "dataType": "DOUBLE"
    }
  ]
}
```

**Air Quality Analysis Queries:**

```sql  theme={null}
-- Find air quality patterns and pollution hotspots  
WITH air_quality_analysis AS (
  SELECT 
    sensor_id,
    sensor_location,
    region,
    AVG(pm25_level) as avg_pm25,
    AVG(pm10_level) as avg_pm10,
    AVG(ozone_level) as avg_ozone,
    COUNT(*) as reading_count,
    CASE 
      WHEN AVG(pm25_level) > 35 THEN 'Unhealthy'
      WHEN AVG(pm25_level) > 12 THEN 'Moderate'
      ELSE 'Good'
    END as air_quality_category
  FROM air_quality_sensors 
  WHERE timestamp >= now() - INTERVAL '24' HOUR
  GROUP BY sensor_id, sensor_location, region
),
pollution_clusters AS (
  SELECT 
    aqa.sensor_id,
    aqa.region,
    aqa.avg_pm25,
    aqa.air_quality_category,
    COUNT(nearby.sensor_id) as nearby_unhealthy_sensors
  FROM air_quality_analysis aqa
  LEFT JOIN air_quality_analysis nearby 
    ON ST_Distance(aqa.sensor_location, nearby.sensor_location) < 2000
    AND nearby.air_quality_category = 'Unhealthy'
    AND aqa.sensor_id != nearby.sensor_id
  GROUP BY aqa.sensor_id, aqa.region, aqa.avg_pm25, aqa.air_quality_category
)
SELECT 
  region,
  air_quality_category,
  COUNT(*) as sensor_count,
  AVG(avg_pm25) as regional_avg_pm25,
  MAX(nearby_unhealthy_sensors) as max_pollution_cluster_size
FROM pollution_clusters
GROUP BY region, air_quality_category
ORDER BY regional_avg_pm25 DESC;
```

#### **Smart City Traffic Optimization**

```sql  theme={null}
-- Analyze traffic patterns and optimize signal timing
WITH traffic_analysis AS (
  SELECT 
    ts.intersection_id,
    ts.sensor_location,
    DATE_TRUNC('hour', ts.timestamp) as hour_window,
    AVG(ts.vehicle_count) as avg_vehicles_per_hour,
    AVG(ts.average_speed_kmh) as avg_speed,
    COUNT(CASE WHEN ts.congestion_level = 'HIGH' THEN 1 END) as high_congestion_periods
  FROM traffic_sensors ts
  WHERE ts.timestamp >= now() - INTERVAL '7' DAY
  GROUP BY ts.intersection_id, ts.sensor_location, DATE_TRUNC('hour', ts.timestamp)
),
congestion_impact AS (
  SELECT 
    ta.intersection_id,
    ta.hour_window,
    ta.avg_vehicles_per_hour,
    ta.avg_speed,
    -- Find nearby intersections affected by congestion
    COUNT(nearby.intersection_id) as affected_nearby_intersections,
    AVG(nearby.avg_speed) as nearby_avg_speed
  FROM traffic_analysis ta
  LEFT JOIN traffic_analysis nearby 
    ON ST_Distance(ta.sensor_location, nearby.sensor_location) < 1000
    AND ta.hour_window = nearby.hour_window
    AND ta.intersection_id != nearby.intersection_id
  WHERE ta.high_congestion_periods > 0
  GROUP BY ta.intersection_id, ta.hour_window, ta.avg_vehicles_per_hour, ta.avg_speed
)
SELECT 
  intersection_id,
  EXTRACT(hour FROM hour_window) as hour_of_day,
  AVG(avg_vehicles_per_hour) as peak_vehicle_count,
  AVG(avg_speed) as intersection_speed,
  AVG(nearby_avg_speed) as area_speed,
  AVG(affected_nearby_intersections) as congestion_spread,
  -- Recommend signal timing adjustments
  CASE 
    WHEN AVG(avg_speed) < 20 AND AVG(affected_nearby_intersections) > 3 THEN 'Increase green time'
    WHEN AVG(avg_speed) > 50 AND AVG(avg_vehicles_per_hour) < 100 THEN 'Reduce green time'
    ELSE 'Current timing OK'
  END as recommendation
FROM congestion_impact
GROUP BY intersection_id, EXTRACT(hour FROM hour_window)
ORDER BY intersection_id, hour_of_day;
```

## Advanced Spatial Analytics Patterns

### **Spatial Clustering Analysis**

**Find Business Clusters:**

```sql  theme={null}
-- Identify business clustering patterns using spatial density
WITH business_density AS (
  SELECT 
    b1.business_id,
    b1.business_name,
    b1.category,
    b1.location,
    COUNT(b2.business_id) as nearby_businesses,
    COUNT(CASE WHEN b2.category = b1.category THEN 1 END) as same_category_nearby
  FROM businesses b1 
  LEFT JOIN businesses b2 
    ON ST_Distance(b1.location, b2.location) < 500
    AND b1.business_id != b2.business_id
  GROUP BY b1.business_id, b1.business_name, b1.category, b1.location
),
cluster_analysis AS (
  SELECT 
    category,
    AVG(nearby_businesses) as avg_business_density,
    AVG(same_category_nearby) as avg_category_clustering,
    COUNT(*) as total_businesses,
    STDDEV(nearby_businesses) as density_variation
  FROM business_density
  GROUP BY category
)
SELECT 
  category,
  total_businesses,
  ROUND(avg_business_density, 2) as avg_nearby_businesses,
  ROUND(avg_category_clustering, 2) as category_clustering_index,
  ROUND(density_variation, 2) as clustering_consistency,
  CASE 
    WHEN avg_category_clustering > avg_business_density * 0.5 THEN 'Highly Clustered'
    WHEN avg_category_clustering > avg_business_density * 0.3 THEN 'Moderately Clustered'
    ELSE 'Dispersed'
  END as clustering_pattern
FROM cluster_analysis
ORDER BY category_clustering_index DESC;
```

### **Geospatial Time Series Analysis**

**Temporal-Spatial Pattern Detection:**

```sql  theme={null}
-- Analyze how spatial patterns change over time
WITH hourly_patterns AS (
  SELECT 
    EXTRACT(hour FROM timestamp) as hour_of_day,
    EXTRACT(dow FROM timestamp) as day_of_week,
    ST_Distance(event_location, ST_Point(-122.4194, 37.7749)) as distance_from_center,
    event_type,
    COUNT(*) as event_count
  FROM events 
  WHERE timestamp >= now() - INTERVAL '30' DAY
  GROUP BY 
    EXTRACT(hour FROM timestamp),
    EXTRACT(dow FROM timestamp), 
    ST_Distance(event_location, ST_Point(-122.4194, 37.7749)),
    event_type
),
pattern_analysis AS (
  SELECT 
    hour_of_day,
    day_of_week,
    event_type,
    AVG(distance_from_center) as avg_distance_from_center,
    SUM(event_count) as total_events,
    STDDEV(distance_from_center) as spatial_spread
  FROM hourly_patterns
  GROUP BY hour_of_day, day_of_week, event_type
)
SELECT 
  event_type,
  hour_of_day,
  CASE 
    WHEN day_of_week IN (0, 6) THEN 'Weekend'
    ELSE 'Weekday'
  END as day_type,
  total_events,
  ROUND(avg_distance_from_center, 0) as avg_distance_from_center,
  ROUND(spatial_spread, 0) as spatial_dispersion,
  CASE 
    WHEN avg_distance_from_center < 2000 THEN 'Central'
    WHEN avg_distance_from_center < 5000 THEN 'Urban'
    ELSE 'Suburban'
  END as spatial_pattern
FROM pattern_analysis
WHERE total_events > 10
ORDER BY event_type, day_type, hour_of_day;
```

## Performance Optimization Examples

### **Query Optimization Patterns**

**Efficient Multi-Location Analysis:**

```sql  theme={null}
-- Optimized approach for analyzing multiple locations
WITH locations_of_interest AS (
  SELECT * FROM (VALUES 
    ('Downtown SF', -122.4194, 37.7749),
    ('Mission District', -122.4194, 37.7589),
    ('SOMA', -122.3997, 37.7879)
  ) AS locations(area_name, longitude, latitude)
),
location_analysis AS (
  SELECT 
    loi.area_name,
    s.store_name,
    s.category,
    ST_Distance(s.location, ST_Point(loi.longitude, loi.latitude)) as distance
  FROM locations_of_interest loi
  CROSS JOIN stores s
  WHERE ST_Distance(s.location, ST_Point(loi.longitude, loi.latitude)) < 2000
)
SELECT 
  area_name,
  category,
  COUNT(*) as store_count,
  AVG(distance) as avg_distance,
  MIN(distance) as nearest_store_distance
FROM location_analysis
GROUP BY area_name, category
ORDER BY area_name, store_count DESC;
```

**Hierarchical Spatial Filtering:**

```sql  theme={null}
-- Use coarse-to-fine filtering for large datasets
WITH coarse_filter AS (
  -- First pass: larger radius for initial filtering
  SELECT store_id, location, category 
  FROM stores 
  WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 10000
),
fine_filter AS (
  -- Second pass: precise filtering on reduced dataset
  SELECT 
    store_id,
    location,
    category,
    ST_Distance(location, ST_Point(-122.4194, 37.7749)) as exact_distance
  FROM coarse_filter
  WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000
)
SELECT 
  category,
  COUNT(*) as matching_stores,
  AVG(exact_distance) as avg_distance,
  MIN(exact_distance) as nearest_distance
FROM fine_filter
GROUP BY category
ORDER BY nearest_distance;
```

## Next Steps & Integration

### **API Integration Patterns**

**GeoJSON Output for Web Applications:**

```sql  theme={null}
-- Format results for web mapping applications
SELECT json_object(
  'type', 'FeatureCollection',
  'features', json_arrayagg(
    json_object(
      'type', 'Feature',
      'geometry', json(ST_AsGeoJson(location)),
      'properties', json_object(
        'store_name', store_name,
        'category', category,
        'rating', rating,
        'distance', ST_Distance(location, ST_Point(-122.4194, 37.7749))
      )
    )
  )
) as geojson_result
FROM stores 
WHERE ST_Distance(location, ST_Point(-122.4194, 37.7749)) < 5000
  AND rating >= 4.0;
```

### **Implementation Guide**

1. **Choose Your Use Case**: Start with the example most similar to your requirements

2. **Adapt Schema**: Modify the schema to match your data structure

3. **Configure Indexes**: Set appropriate H3 resolutions based on query patterns

4. **Test Queries**: Validate performance using EXPLAIN PLAN

5. **Monitor & Optimize**: Use performance monitoring to fine-tune configuration

Built with [Mintlify](https://mintlify.com).
