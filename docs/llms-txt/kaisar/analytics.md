# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/analytics.md

# Analytics

Monitor and analyze your ML operations with comprehensive analytics and insights.

![Analytics Dashboard](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-4d79a8c4051c622332eef056669e8cba2bce4022%2Fanalytics_dashboard.png?alt=media)

## Overview

The Analytics Dashboard provides comprehensive insights and metrics for the Deep Learning Platform, helping you track performance, costs, and usage across all your ML operations.

## Dashboard Summary Cards

At the top of the dashboard, you'll see key metrics at a glance:

**Active Experiments**

* **Count**: Number of currently running ML experiments
* **Trend**: Percentage change from previous period

**Total Users**

* **Count**: Total number of platform users
* **Trend**: Percentage change from previous period

**Deployed Models**

* **Count**: Number of models in production
* **Trend**: Percentage change from previous period

**Total Projects**

* **Count**: Number of active projects
* **Trend**: Percentage change from previous period

**GPU Utilization**

* **Percentage**: Current GPU usage percentage
* **Status**: Infrastructure cost with trend indicators

**Total Cost** **Total Cost**

* **Amount**: Total infrastructure cost
* **Trend**: Percentage change from previous period

## Detailed Analytics

The dashboard provides detailed analytics with customizable time ranges (Last 24 Hours, Last 7 Days, Last 30 Days, etc.).

**Available Actions**:

* **Refresh**: Update data
* **Print**: Print dashboard
* **Export**: Export analytics data

### System Performance

Real-time monitoring of system resources:

**CPU Usage**

* Current utilization: 83.4%
* Visual progress bar indicator
* Color-coded (cyan)

**Memory Usage**

* Current utilization: 71.2%
* Visual progress bar indicator
* Color-coded (purple)

**GPU Usage**

* Current utilization: 89.1%
* Visual progress bar indicator
* Color-coded (green)

**Disk Usage**

* Current utilization: 45.0%
* Visual progress bar indicator
* Color-coded (lime green)

### Real-time CPU Usage

Interactive line chart showing CPU usage over time:

* Time-series visualization
* Real-time updates
* Hover for detailed values
* CPU % on Y-axis

### Cost Analytics

**Cost Analytics Chart**:

* Area chart showing cost trends over time
* Time-series data (hourly/daily)
* Cost ($) on Y-axis
* Visual trend analysis

**Cost by Service** (Pie Chart):

* **Data Transfer**: Largest portion (blue)
* **GPU Compute**: Second largest (purple/pink)
* **Load Balancing**: Smaller portion (cyan)
* **Storage**: Smallest portion (pink)
* Interactive legend

### Model Performance Metrics

Line chart tracking model performance:

* **Accuracy**: Green line
* **Precision**: Cyan line
* **Recall**: Purple line
* Time-series visualization
* Performance trends over time

### Cost by Environment

Pie chart showing cost distribution:

* **Development**: Largest portion (blue)
* **Production**: Medium portion (purple/pink)
* **Staging**: Smallest portion (pink)
* Interactive breakdown

## Key Features

### Experiment Analytics

* Training metrics over time
* Hyperparameter impact analysis
* Experiment comparison dashboards
* Success/failure rates
* Active experiment tracking

### Model Performance

* Model accuracy trends
* Inference latency tracking
* Model drift detection
* Performance metrics visualization
* Multi-metric comparison

### Resource Usage

* GPU/CPU utilization monitoring
* Memory consumption tracking
* Storage usage analysis
* Real-time performance graphs
* Resource optimization insights

### Deployment Metrics

* Request rate and throughput
* Error rates and types
* Latency percentiles (p50, p95, p99)
* Uptime and availability
* Deployment health status

### Cost Analysis

* Total infrastructure cost tracking
* Cost breakdown by service
* Cost by environment
* Trend analysis
* Budget monitoring

## Using the Dashboard

**Time Range Selection**:

1. Click the time range dropdown (default: "Last 24 Hours")
2. Select desired range:
   * Last 24 Hours
   * Last 7 Days
   * Last 30 Days
   * Custom range

**Refreshing Data**:

* Click **Refresh** button to update all metrics
* Dashboard auto-refreshes periodically

**Exporting Data**:

1. Click **Export** button
2. Choose export format
3. Download analytics report

**Printing**:

* Click **Print** button to print current dashboard view

## Monitoring Best Practices

**Regular Monitoring**:

* Check dashboard daily for anomalies
* Monitor GPU utilization for optimization
* Track cost trends to manage budget
* Review model performance metrics

**Setting Baselines**:

* Establish normal ranges for metrics
* Set up alerts for deviations
* Track trends over time

**Cost Optimization**:

* Identify high-cost services
* Optimize resource allocation
* Monitor environment-specific costs
* Review and adjust as needed

## Next Steps

* View detailed [Experiments](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/experiments) metrics
* Monitor [Deployments](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/deployments) performance
* Track [Models](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/models) accuracy
* Optimize resource usage based on insights
