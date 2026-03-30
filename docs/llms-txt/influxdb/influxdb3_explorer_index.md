---
title: InfluxDB 3 Explorer documentation
description: InfluxDB 3 Explorer is a standalone web-based interface for interacting with InfluxDB 3 Core and Enterprise. Visualize, query, and manage your time series data efficiently.
url: https://docs.influxdata.com/influxdb3/explorer/
estimated_tokens: 590
product: InfluxDB 3 Explorer
version: explorer
---

# InfluxDB 3 Explorer documentation

InfluxDB 3 Explorer is the standalone web application designed for visualizing, querying, and managing your data stored in InfluxDB 3 Core and Enterprise. Explorer provides an intuitive interface for interacting with your time series data, streamlining database operations and enhancing data insights.

## Key features

Use InfluxDB 3 Explorer for:

-   **Database management**: Create and manage InfluxDB 3 instances, databases, tokens, plugins, and more
-   **Data visualization and analysis**: Query data with a built-in visualizer for enhanced data insights
-   **Data ingestion**: Write new data and setup Telegraf configurations

## Quick start

Run the Docker image to start InfluxDB 3 Explorer:

```sh
# Pull the Docker image
docker pull influxdata/influxdb3-ui

# Run the Docker container
docker run --detach \
  --name influxdb3-explorer \
  --publish 8888:80 \
  --publish 8889:8888 \
  influxdata/influxdb3-ui \
  --mode=admin

# Visit http://localhost:8888 in your browser to begin using InfluxDB 3 Explorer
```

For installation and configuration options, see [Install and run InfluxDB 3 Explorer](/influxdb3/explorer/install/). [Get started using InfluxDB 3 Explorer](/influxdb3/explorer/get-started/)
