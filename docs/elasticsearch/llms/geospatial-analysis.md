# Source: https://www.elastic.co/docs/explore-analyze/geospatial-analysis

﻿---
title: Geospatial analysis
description: Did you know that Elasticsearch has geospatial capabilities? Elasticsearch and geo go way back, to 2010. A lot has happened since then and today Elasticsearch...
url: https://www.elastic.co/docs/explore-analyze/geospatial-analysis
products:
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Geospatial analysis
Did you know that Elasticsearch has geospatial capabilities? [Elasticsearch and geo](https://www.elastic.co/blog/geo-location-and-search) go way back, to 2010. A lot has happened since then and today Elasticsearch provides robust geospatial capabilities with speed, all with a stack that scales automatically.
Not sure where to get started with Elasticsearch and geo? Then, you have come to the right place.

## Geospatial mapping

Elasticsearch supports two types of geo data: [geo_point](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-point) fields which support lat/lon pairs, and [geo_shape](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape) fields, which support points, lines, circles, polygons, multi-polygons, and so on. Use [explicit mapping](https://www.elastic.co/docs/manage-data/data-store/mapping/explicit-mapping) to index geo data fields.
Have an index with lat/lon pairs but no geo_point mapping? Use [runtime fields](https://www.elastic.co/docs/manage-data/data-store/mapping/map-runtime-field) to make a geo_point field without reindexing.

## Ingest

Data is often messy and incomplete. [Ingest pipelines](https://www.elastic.co/docs/manage-data/ingest/transform-enrich/ingest-pipelines) lets you clean, transform, and augment your data before indexing.
- Use [CSV](https://www.elastic.co/docs/reference/enrich-processor/csv-processor) together with [explicit mapping](https://www.elastic.co/docs/manage-data/data-store/mapping/explicit-mapping) to index CSV files with geo data. Kibana’s [Import CSV](https://www.elastic.co/docs/explore-analyze/visualize/maps/import-geospatial-data) feature can help with this.
- Use [GeoIP](https://www.elastic.co/docs/reference/enrich-processor/geoip-processor) to add geographical location of an IPv4 or IPv6 address.
- Use [geo-grid processor](https://www.elastic.co/docs/reference/enrich-processor/ingest-geo-grid-processor) to convert grid tiles or hexagonal cell ids to bounding boxes or polygons which describe their shape.
- Use [geo_match enrich policy](https://www.elastic.co/docs/manage-data/ingest/transform-enrich/example-enrich-data-based-on-geolocation) for reverse geocoding. For example, use [reverse geocoding](https://www.elastic.co/docs/explore-analyze/visualize/maps/reverse-geocoding-tutorial) to visualize metropolitan areas by web traffic.


## Query

[Geo queries](https://www.elastic.co/docs/reference/query-languages/query-dsl/geo-queries) answer location-driven questions. Find documents that intersect with, are within, are contained by, or do not intersect your query geometry. Combine geospatial queries with full text search queries for unparalleled searching experience. For example, "Show me all subscribers that live within 5 miles of our new gym location, that joined in the last year and have running mentioned in their profile".

## ES|QL

[ES|QL](https://www.elastic.co/docs/reference/query-languages/esql) has support for [Geospatial Search](https://www.elastic.co/docs/reference/query-languages/esql/functions-operators/spatial-functions) functions, enabling efficient index searching for documents that intersect with, are within, are contained by, or are disjoint from a query geometry. In addition, the `ST_DISTANCE` function calculates the distance between two points.
- [`ST_INTERSECTS`](https://www.elastic.co/docs/reference/query-languages/esql/functions-operators/spatial-functions/st_intersects)
- [`ST_DISJOINT`](https://www.elastic.co/docs/reference/query-languages/esql/functions-operators/spatial-functions/st_disjoint)
- [`ST_CONTAINS`](https://www.elastic.co/docs/reference/query-languages/esql/functions-operators/spatial-functions/st_contains)
- [`ST_WITHIN`](https://www.elastic.co/docs/reference/query-languages/esql/functions-operators/spatial-functions/st_within)
- [`ST_DISTANCE`](https://www.elastic.co/docs/reference/query-languages/esql/functions-operators/spatial-functions/st_distance)


## Aggregate

[Aggregations](https://www.elastic.co/docs/explore-analyze/query-filter/aggregations) summarizes your data as metrics, statistics, or other analytics. Use [bucket aggregations](https://www.elastic.co/docs/reference/aggregations/bucket) to group documents into buckets, also called bins, based on field values, ranges, or other criteria. Then, use [metric aggregations](https://www.elastic.co/docs/reference/aggregations/metrics) to calculate metrics, such as a sum or average, from field values in each bucket. Compare metrics across buckets to gain insights from your data.
Geospatial bucket aggregations:
- [Geo-distance aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-geodistance-aggregation) evaluates the distance of each geo_point location from an origin point and determines the buckets it belongs to based on the ranges (a document belongs to a bucket if the distance between the document and the origin falls within the distance range of the bucket).
- [Geohash grid aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-geohashgrid-aggregation) groups geo_point and geo_shape values into buckets that represent a grid.
- [Geohex grid aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-geohexgrid-aggregation) groups geo_point and geo_shape values into buckets that represent an H3 hexagonal cell.
- [Geotile grid aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-geotilegrid-aggregation) groups geo_point and geo_shape values into buckets that represent a grid. Each cell corresponds to a [map tile](https://en.wikipedia.org/wiki/Tiled_web_map) as used by many online map sites.

Geospatial metric aggregations:
- [Geo-bounds aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-geobounds-aggregation) computes the geographic bounding box containing all values for a Geopoint or Geoshape field.
- [Geo-centroid aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-geocentroid-aggregation) computes the weighted centroid from all coordinate values for geo fields.
- [Geo-line aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-geo-line) aggregates all geo_point values within a bucket into a LineString ordered by the chosen sort field. Use geo_line aggregation to create [vehicle tracks](https://www.elastic.co/docs/explore-analyze/visualize/maps/asset-tracking-tutorial).

Combine aggregations to perform complex geospatial analysis. For example, to calculate the most recent GPS tracks per flight, use a [terms aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-terms-aggregation) to group documents into buckets per aircraft. Then use geo-line aggregation to compute a track for each aircraft. In another example, use geotile grid aggregation to group documents into a grid. Then use geo-centroid aggregation to find the weighted centroid of each grid cell.

## Integrate

Use [vector tile search API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-mvt) to consume Elasticsearch geo data within existing GIS infrastructure.

## Visualize

Visualize geo data with [Kibana](https://www.elastic.co/docs/explore-analyze/visualize/maps). Add your map to a [dashboard](https://www.elastic.co/docs/explore-analyze/dashboards) to view your data from all angles.
This dashboard shows the effects of the [Cumbre Vieja eruption](https://www.elastic.co/blog/understanding-evolution-volcano-eruption-elastic-maps/).
![Kibana dashboard showing Cumbre Vieja eruption from Aug 31 2021 to Dec 14 2021](https://www.elastic.co/docs/explore-analyze/images/elasticsearch-reference-cumbre_vieja_eruption_dashboard.png)

## Machine learning

Put machine learning to work for you and find the data that should stand out with anomaly detections. Find credit card transactions that occur in an unusual locations or a web request that has an unusual source location. [Location-based anomaly detections](https://www.elastic.co/docs/explore-analyze/machine-learning/anomaly-detection/geographic-anomalies) make it easy to find and explore and compare anomalies with their typical locations.

## Alerting

Let your location data drive insights and action with [geographic alerts](https://www.elastic.co/docs/explore-analyze/alerting/alerts/geo-alerting). Commonly referred to as geo-fencing, track moving objects as they enter or exit a boundary to receive notifications through common business systems (email, Slack, Teams, PagerDuty, and more).
Interested in learning more? Follow [step-by-step instructions](https://www.elastic.co/docs/explore-analyze/visualize/maps/asset-tracking-tutorial) for setting up tracking containment alerts to monitor moving vehicles.