# Source: https://docs.acceldata.io/api/pipeline-information---management.md

# Pipeline Information & Management

This guide covers the foundational APIs for discovering, exploring, and managing pipelines in Acceldata ADOC. Think of this as your "getting to know the system" workflow - you'll learn how to find pipelines, understand their structure, and navigate your data observability landscape.

### Why This Matters

Before you can monitor, debug, or create pipelines, you need to understand what's already in your system. These APIs help you:

- **Discover existing pipelines** across your organization
- **Understand pipeline structure** through visual graphs
- **Find the right pipeline** when investigating data issues
- **Explore data lineage** by viewing how data flows through jobs and assets
- **Organize pipelines** using tags and metadata

---

## Real-World Scenarios

### Scenario 1: New Team Member Onboarding

"I just joined the data engineering team. What pipelines do we have?"

**Solution**: Use `GET /pipelines/summary` to see all pipelines with their current status, then drill into specific ones using `GET /pipelines/:identity`.

### Scenario 2: Investigating a Data Quality Issue

"Our customer dashboard shows outdated data. Which pipeline feeds it?"

**Solution**: Search for pipelines by name or tag, then use `GET /pipelines/:pipelineId/graph` to see the data flow and identify the bottleneck.

### Scenario 3: Understanding System Architecture

"I need to document our data pipelines for compliance."

**Solution**: List all pipelines, retrieve their graphs, and export the structure showing inputs, transformations, and outputs.

### Scenario 4: Finding Related Pipelines

"We're migrating from Athena to Snowflake. Which pipelines will be affected?"

**Solution**: Use `GET /tags` to find all pipelines tagged with "athena" or search by data source in pipeline metadata.

---

## Prerequisites

- API credentials (accessKey and secretKey)
- Basic understanding of your organization's data infrastructure
- Access to Acceldata ADOC

---

## API Reference

This workflow uses **6 APIs**:

1. `GET /pipelines/summary` - List all pipelines
2. `GET /pipelines/:identity` - Get specific pipeline details
3. `GET /pipelines/:pipelineId/graph` - View pipeline structure
4. `GET /tags` - List available tags
5. `PUT /pipelines` - Create or update pipeline
6. `GET /nodes/:nodeId` - Get node details

---

## Workflow: Discover and Explore Pipelines

### Step 1: List All Pipelines

Get an overview of all pipelines in your system.

#### API Call

```bash
GET /torch-pipeline/api/pipelines/summary
```



**Query Parameters** (optional):

- `page`: Page number (default: "0")
- `size`: Results per page (default: "50")

#### Example Request

```bash
GET /torch-pipeline/api/pipelines/summary?page=0&size=50
```



#### Response

```json
{
  "pipelines": [
    {
      "id": 15,
      "uid": "customer-etl-daily",
      "name": "Customer ETL Pipeline",
      "description": "Daily customer data sync",
      "enabled": true,
      "scheduled": false,
      "totalRunsCount": 245,
      "lastRunStatus": "SUCCESS",
      "lastRunTime": "2024-12-05T10:30:00Z"
    },
    {
      "id": 23,
      "uid": "sales-analytics-hourly",
      "name": "Sales Analytics Pipeline",
      "description": "Hourly sales data aggregation",
      "enabled": true,
      "scheduled": true,
      "totalRunsCount": 1456,
      "lastRunStatus": "SUCCESS",
      "lastRunTime": "2024-12-05T11:00:00Z"
    }
  ],
  "total": 47
}
```



#### What to Look For

- **enabled**: Is the pipeline currently active?
- **scheduled**: Does it run automatically?
- **lastRunStatus**: Recent execution status
- **totalRunsCount**: How often it's been executed

 **Tip**: Filter by status to find problematic pipelines or sort by `totalRunsCount` to identify critical pipelines.

---

### Step 2: Get Detailed Pipeline Information

Once you've identified a pipeline of interest, get its full details.

#### API Call

```bash
GET /torch-pipeline/api/pipelines/:identity
```



**Path Parameter**:

- `identity`: Pipeline ID (numeric like `15`) or UID (string like `customer-etl-daily`)

#### Example Requests

**By numeric ID:**

```bash
GET /torch-pipeline/api/pipelines/15
```



**By string UID:**

```bash
GET /torch-pipeline/api/pipelines/customer-etl-daily
```



#### Response

```json
{
  "pipeline": {
    "id": 15,
    "uid": "customer-etl-daily",
    "name": "Customer ETL Pipeline",
    "description": "Daily customer data sync from Athena to Redshift",
    "enabled": true,
    "scheduled": false,
    "schedulerType": "INTERNAL",
    "tags": ["production", "customer-data", "critical"],
    "createdAt": "2024-08-20T05:15:46.569Z",
    "updatedAt": "2024-12-05T10:00:00Z",
    "meta": {
      "owner": "data-team@company.com",
      "team": "data-engineering",
      "codeLocation": "https://github.com/company/pipelines/customer-etl",
      "slackChannel": "#data-alerts"
    }
  }
}
```



#### What This Tells You

- **Owner & Team**: Who to contact for questions
- **Tags**: How it's categorized
- **Code Location**: Where to find the implementation
- **Scheduler Type**: INTERNAL (ADOC manages) or EXTERNAL (like Airflow)

---

### Step 3: Visualize Pipeline Structure

Understand how data flows through the pipeline.

#### API Call

```bash
GET /torch-pipeline/api/pipelines/:pipelineId/graph
```



**Path Parameter**:

- `pipelineId`: Numeric pipeline ID (e.g., `15`)

#### Example Request

```bash
GET /torch-pipeline/api/pipelines/15/graph
```



#### Response

```json
{
  "graph": {
    "nodes": [
      {
        "id": 101,
        "uid": "job-extract-customers",
        "name": "Extract Customer Data",
        "type": "JOB",
        "status": "ACTIVE"
      },
      {
        "id": 102,
        "uid": "job-transform-customers",
        "name": "Transform Customer Data",
        "type": "JOB",
        "status": "ACTIVE"
      },
      {
        "id": 103,
        "uid": "job-load-redshift",
        "name": "Load to Redshift",
        "type": "JOB",
        "status": "ACTIVE"
      },
      {
        "id": 2001,
        "uid": "AwsDataCatalog.production.customers",
        "name": "customers",
        "type": "ASSET",
        "assetType": "TABLE"
      },
      {
        "id": 2002,
        "uid": "RedshiftCluster.warehouse.public.customers",
        "name": "customers",
        "type": "ASSET",
        "assetType": "TABLE"
      }
    ],
    "edges": [
      {
        "source": "AwsDataCatalog.production.customers",
        "target": "job-extract-customers",
        "type": "INPUT"
      },
      {
        "source": "job-extract-customers",
        "target": "job-transform-customers",
        "type": "FLOW"
      },
      {
        "source": "job-transform-customers",
        "target": "job-load-redshift",
        "type": "FLOW"
      },
      {
        "source": "job-load-redshift",
        "target": "RedshiftCluster.warehouse.public.customers",
        "type": "OUTPUT"
      }
    ]
  }
}
```



#### Understanding the Graph

**Nodes** represent:

- **JOB**: Processing steps (extract, transform, load)
- **ASSET**: Data sources and destinations (tables, files)

**Edges** represent:

- **INPUT**: Data source → Job
- **FLOW**: Job → Job (dependency)
- **OUTPUT**: Job → Data destination

**Visualization Tip**:

```none
[Athena Table] → [Extract] → [Transform] → [Load] → [Redshift Table]
```



---

### Step 4: Explore Pipeline Tags

Find pipelines by category or purpose.

#### API Call

```bash
GET /torch-pipeline/api/tags
```



**Parameters**: None

#### Response

```json
{
  "tags": [
    "production",
    "staging",
    "customer-data",
    "sales-data",
    "etl",
    "streaming",
    "critical",
    "hourly",
    "daily",
    "weekly"
  ]
}
```



#### How to Use Tags

- **Environment**: production, staging, dev
- **Data Domain**: customer-data, sales-data, inventory
- **Frequency**: hourly, daily, weekly, real-time
- **Priority**: critical, standard, low-priority
- **Type**: etl, streaming, batch

**Tip**: Use tags to filter pipelines in Step 1 by adding them to your search criteria.

---

### Step 5: Get Detailed Node Information

Drill into specific jobs or assets in the pipeline graph.

#### API Call

```bash
GET /torch-pipeline/api/pipelines/nodes/:nodeId
```



**Path Parameter**:

- `nodeId`: Numeric node ID from the graph (e.g., `101`)

#### Example Request

```bash
GET /torch-pipeline/api/pipelines/nodes/101
```



#### Response

```json
{
  "data": {
    "node": {
      "id": 101,
      "uid": "job-extract-customers",
      "name": "Extract Customer Data",
      "pipelineId": 15,
      "type": "JOB",
      "status": "ACTIVE",
      "meta": {
        "owner": "data-team@company.com",
        "estimatedDuration": "5 minutes",
        "dataVolume": "~100K rows",
        "dependencies": []
      }
    }
  }
}
```



#### What This Reveals

- Job configuration and metadata
- Performance expectations
- Ownership and contacts
- Dependencies and constraints

---

## Common Workflow Patterns

### Pattern 1: Pipeline Discovery

```bash
# Step 1: Get overview
GET /torch-pipeline/api/pipelines/summary

# Step 2: Find pipeline by name or tag
GET /torch-pipeline/api/pipelines/customer-etl-daily

# Step 3: View structure
GET /torch-pipeline/api/pipelines/15/graph

# Step 4: Examine specific job
GET /torch-pipeline/api/pipelines/nodes/101
```



### Pattern 2: Impact Analysis

"If I modify this Athena table, what breaks?"

```bash
# 1. Search for pipelines using that table
GET /torch-pipeline/api/pipelines/summary

# 2. For each pipeline, check the graph
GET /torch-pipeline/api/pipelines/15/graph

# 3. Look for your table in the nodes
# Find edges where your table is the source
```



### Pattern 3: Creating Documentation

```bash
# 1. List all pipelines
GET /torch-pipeline/api/pipelines/summary

# 2. For each pipeline:
#    - Get details
GET /torch-pipeline/api/pipelines/:identity

#    - Get graph structure
GET /torch-pipeline/api/pipelines/:pipelineId/graph

# 3. Export to documentation format
```



---

## Quick Reference

| What You Want | API to Use | Key Info | 
| ---- | ---- | ---- | 
| See all pipelines | `GET /pipelines/summary` | Overview with status | 
| Find specific pipeline | `GET /pipelines/:identity` | Full details | 
| Understand data flow | `GET /pipelines/:pipelineId/graph` | Visual structure | 
| Browse by category | `GET /tags` | Available tags | 
| Inspect a job/asset | `GET /nodes/:nodeId` | Node details | 


---

## Troubleshooting

| Issue | Solution | 
| ---- | ---- | 
| Too many results | Use pagination: `?page=0&size=25` | 
| Can't find pipeline | Try searching by UID instead of ID | 
| Empty graph | Pipeline may not have jobs defined yet | 
| Missing metadata | Owner can update via `PUT /pipelines` | 
