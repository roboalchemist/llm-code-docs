# Source: https://docs.acceldata.io/api/create-and-execute-your-first-pipeline.md

# Create and Execute Your First Pipeline

This is your hands-on guide to creating a complete data pipeline from scratch in ADOC. You'll learn the full lifecycle: defining the pipeline structure, setting up jobs, creating execution tracking, and monitoring the results.

---

## Why This Matters

Creating a pipeline in ADOC isn't just about moving data - it's about establishing **observability**. Every step you define here becomes visible, traceable, and debuggable. When something goes wrong (and it will), you'll know exactly where, when, and why.

---

## Real-World Scenario

### The Challenge

Your company needs to sync customer data daily from your Athena data lake to Redshift for analytics. The business team needs:

- Fresh data every morning by 8 AM
- Quality checks to catch issues early
- Clear visibility when something breaks
- Ability to trace data lineage

### The Solution

Build a fully observable pipeline with three jobs:

1. **Extract**: Pull customer data from Athena
2. **Transform**: Clean and validate the data
3. **Load**: Write to Redshift for analytics

Each step will be tracked with spans and events, giving you complete visibility into execution.

---

## What You'll Build

```none
┌─────────────────────────────────────────────────────────────┐
│                    Customer ETL Pipeline                      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  [Athena Table]                                              │
│        │                                                      │
│        ├──→ [Extract Job] ──→ Span: span-extract            │
│                   │                                          │
│                   ├──→ [Transform Job] ──→ Span: span-transform │
│                            │                                 │
│                            ├──→ [Load Job] ──→ Span: span-load  │
│                                     │                        │
│                                     └──→ [Redshift Table]    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```



---

## Prerequisites

- **API Credentials**: accessKey and secretKey
- **Data Source UID**: Your Athena table identifier (e.g., `AwsDataCatalog.production.customers`)
- **Data Destination UID**: Your Redshift table identifier (e.g., `warehouse.public.customers`)
- **Understanding**: Basic ETL concepts

## **Tip**

## The Complete Workflow

We'll execute **8 steps** using **6 APIs**:

1. Design your pipeline (planning)
2. Create the pipeline structure
3. Create a pipeline run
4. Define job nodes (3 jobs)
5. Create spans for tracking (4 spans)
6. Start execution
7. Record events as work progresses
8. Mark completion

---

## Step 1: Design Your Pipeline

Before touching any APIs, map out your pipeline on paper.

### Questions to Answer

1. **What data are you moving?**
    -  Source: Athena table `AwsDataCatalog.production.customers`
    - Destination: Redshift table `warehouse.public.customers`

2. **What transformations are needed?**
    - Remove duplicate customer IDs
    - Validate email formats
    - Calculate customer lifetime value

3. **What are the dependencies?**
    - Extract must complete before Transform
    - Transform must complete before Load

4. **Who owns this?**
    - Team: data-engineering
    - Owner: [data-team@company.com](mailto:data-team@company.com)
    - On-call: #data-alerts Slack channel

### Pipeline Design

```none
Pipeline: "Customer ETL Pipeline"
UID: "customer-etl-daily"
Schedule: Manual (for now, we'll automate later)

Jobs:
  1. Extract (uid: job-extract-customers)
     - Input: Athena table
     - Output: None (passes data in memory)
  
  2. Transform (uid: job-transform-customers)
     - Input: Extract job output
     - Output: None (passes data in memory)
  
  3. Load (uid: job-load-redshift)
     - Input: Transform job output
     - Output: Redshift table
```



**Checkpoint**: You should have job names, UIDs, and data sources documented.

---

## Step 2: Create the Pipeline

Register your pipeline in ADOC.

### API Call

```bash
PUT /torch-pipeline/api/pipelines
```



**Parameters:** None

### Request

```json
{
  "pipeline": {
    "name": "Customer ETL Pipeline",
    "description": "Daily customer data sync from Athena to Redshift",
    "uid": "customer-etl-daily",
    "enabled": true,
    "scheduled": false,
    "schedulerType": "INTERNAL",
    "tags": ["production", "daily", "customer-data"],
    "meta": {
      "owner": "data-team@company.com",
      "team": "data-engineering",
      "codeLocation": "https://github.com/company/pipelines/customer-etl",
      "slackChannel": "#data-alerts",
      "sla": "30 minutes"
    }
  }
}
```



### Field Explanations

| Field | Purpose | Your Value | 
| ---- | ---- | ---- | 
| name | Display name | Customer ETL Pipeline | 
| uid | Unique identifier (use for lookups) | customer-etl-daily | 
| enabled | Can this pipeline run? | true | 
| scheduled | Runs automatically? | false (manual for now) | 
| schedulerType | Who manages scheduling? | INTERNAL (ADOC manages) | 
| tags | For filtering/organizing | production, daily, customer-data | 
| meta.owner | Who to contact | [data-team@company.com](mailto:data-team@company.com) | 
| meta.sla | Expected completion time | 30 minutes | 


### Success Response

```json
{
  "pipeline": {
    "id": 15,
    "uid": "customer-etl-daily",
    "name": "Customer ETL Pipeline",
    "enabled": true,
    "createdAt": "2024-12-05T10:00:00Z"
  }
}
```



**Save This**: `pipeline.id = 15` - You'll need this for the next steps!

---

## Step 3: Create a Pipeline Run

A "run" is a single execution instance of your pipeline. Think of it like pressing "play" - you're about to execute all the jobs.

### API Call

```bash
POST /torch-pipeline/api/pipelines/15/runs
```



**Path Parameters:**

| Parameter | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| pipelineId | integer | Yes | The numeric ID from Step 2 (e.g., `15`) | 


### Request

```json
{
  "run": {
    "continuationId": "run-2024-12-05-001"
  }
}
```



**What is continuationId?** A unique identifier for this specific run. Use format: `run-YYYY-MM-DD-NNN` where NNN is a sequence number.

### Success Response

```json
{
  "run": {
    "id": 109133,
    "pipelineId": 15,
    "continuationId": "run-2024-12-05-001",
    "status": "CREATED"
  }
}
```



**Save This**: `run.id = 109133` - You'll use this for jobs and spans!

---

## Step 4: Define Job Nodes

Jobs are the actual work units in your pipeline. You'll create three jobs that form the ETL chain.

### API Call

```bash
PUT /torch-pipeline/api/pipelines/15/jobs
```



**Path Parameters:**

| Parameter | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| pipelineId | integer | Yes | The numeric ID of the pipeline (e.g., `15`) | 


**Important**: Call this endpoint **three times** (once per job).

---

### Job 1: Extract Customer Data

This job reads from your Athena table.

```json
{
  "name": "Extract Customer Data",
  "uid": "job-extract-customers",
  "pipeLineRunId": 109133,
  "inputs": [],
  "outputs": [
    {
      "source": "ATHENA-DS",
      "asset_uid": "AwsDataCatalog.production.customers"
    }
  ],
  "meta": {
    "owner": "data-team@company.com",
    "team": "data-engineering",
    "estimatedDuration": "5 minutes",
    "dataVolume": "~100K rows"
  }
}
```



**Why no inputs?** This is the first job - it starts from a data source, not from another job.

**What's asset_uid?** The fully qualified name of your Athena table in ADOC's asset catalog.

---

### Job 2: Transform Customer Data

This job processes the data from the Extract job.

```json
{
  "name": "Transform Customer Data",
  "uid": "job-transform-customers",
  "pipeLineRunId": 109133,
  "inputs": [
    {
      "jobUid": "job-extract-customers"
    }
  ],
  "outputs": [],
  "meta": {
    "owner": "data-team@company.com",
    "team": "data-engineering",
    "transformations": ["deduplicate", "validate_emails", "calculate_ltv"]
  }
}
```



**Key Point**: `inputs` references the Extract job by its `jobUid`. This creates the dependency chain.

---

### Job 3: Load to Redshift

This job writes the transformed data to Redshift.

```json
{
  "name": "Load to Redshift",
  "uid": "job-load-redshift",
  "pipeLineRunId": 109133,
  "inputs": [
    {
      "jobUid": "job-transform-customers"
    }
  ],
  "outputs": [
    {
      "source": "REDSHIFT-DS",
      "asset_uid": "warehouse.public.customers"
    }
  ],
  "meta": {
    "owner": "data-team@company.com",
    "team": "data-engineering",
    "loadMethod": "UPSERT"
  }
}
```



**The Flow**: Extract → Transform → Load

**Checkpoint**: You should have created 3 jobs. They define WHAT to do, but haven't executed yet.

---

## Step 5: Create Spans to Track Execution

Spans are how ADOC tracks execution. Each span represents a unit of work being performed.

### API Call

```bash
POST /torch-pipeline/api/pipelines/runs/109133/spans
```



**Path Parameters:**

| Parameter | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| runId | integer | Yes | The numeric ID of the run (e.g., `109133`) | 


**Important**: Call this endpoint **four times** (1 root + 3 job spans).

---

### Span 1: Root Span (Pipeline Level)

This represents the entire pipeline execution.

```json
{
  "span": {
    "uid": "span-pipeline-root"
  }
}
```



**Response**:

```json
{
  "span": {
    "id": 5000,
    "uid": "span-pipeline-root"
  }
}
```



**Save This**: `span.id = 5000` - You'll use this as `parentSpanId` for job spans!

---

### Span 2: Extract Span

```json
{
  "span": {
    "uid": "span-extract",
    "parentSpanId": 5000
  }
}
```



### Span 3: Transform Span

```json
{
  "span": {
    "uid": "span-transform",
    "parentSpanId": 5000
  }
}
```



### Span 4: Load Span

```json
{
  "span": {
    "uid": "span-load",
    "parentSpanId": 5000
  }
}
```



**Understanding Span Hierarchy**:

```none
span-pipeline-root (5000)
  ├── span-extract (5001)
  ├── span-transform (5002)
  └── span-load (5003)
```



**Checkpoint**: You've created the execution tracking structure. Now it's time to actually run!

---

## Step 6: Start Execution

Mark the run as started - this signals that work is beginning.

### API Call

```bash
PUT /torch-pipeline/api/pipelines/runs/109133
```



**Path Parameters:**

| Parameter | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| runId | integer | Yes | The numeric ID of the run (e.g., `109133`) | 


### Request

```json
{
  "run": {
    "status": "STARTED"
  }
}
```



**Status Change**: CREATED → STARTED

---

## Step 7: Record Span Events

As each job executes, record events to track progress. This is what makes your pipeline observable!

### API Call

```bash
POST /torch-pipeline/api/pipelines/spans/<span-id>/events
```



**Path Parameters:**

| Parameter | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| spanId | integer | Yes | The numeric ID of the span (e.g., `5001`, `5002`, `5003`) | 


---

### Event Flow for Each Span

For **each** of your 3 job spans (extract, transform, load), record these events:

#### 1. Start Event (When job begins)

```json
{
  "eventType": "START",
  "timestamp": "2024-12-05T10:00:00Z"
}
```



#### 2. Progress Events (Optional, during execution)

```json
{
  "eventType": "LOG",
  "timestamp": "2024-12-05T10:02:00Z",
  "contextData": {
    "message": "Extracted 50,000 of 100,000 rows",
    "progress": "50%"
  }
}
```



#### 3. End Event (When job completes successfully)

```json
{
  "eventType": "END",
  "timestamp": "2024-12-05T10:05:00Z",
  "contextData": {
    "rowsProcessed": 100000,
    "duration": "5 minutes"
  }
}
```



#### 4. Error Event (If something fails)

```json
{
  "eventType": "FAILED",
  "timestamp": "2024-12-05T10:03:00Z",
  "alert": "ERROR",
  "contextData": {
    "error": "Connection timeout to Athena",
    "details": "Network unreachable",
    "retryAfter": "30 seconds"
  }
}
```



---

### Complete Event Sequence Example

**For Extract Job (span 5001)**:

```bash
POST /torch-pipeline/api/pipelines/spans/5001/events
# Event: START at 10:00

POST /torch-pipeline/api/pipelines/spans/5001/events
# Event: LOG "50% complete" at 10:02

POST /torch-pipeline/api/pipelines/spans/5001/events
# Event: END at 10:05
```



**For Transform Job (span 5002)**:

```bash
POST /torch-pipeline/api/pipelines/spans/5002/events
# Event: START at 10:05

POST /torch-pipeline/api/pipelines/spans/5002/events
# Event: END at 10:20
```



**For Load Job (span 5003)**:

```bash
POST /torch-pipeline/api/pipelines/spans/5003/events
# Event: START at 10:20

POST /torch-pipeline/api/pipelines/spans/5003/events
# Event: END at 10:30
```



**Pro Tip**: The more events you log, the better visibility you'll have when debugging issues later!

---

## Step 8: Mark Run Completion

When all jobs finish, update the run status.

### API Call

```bash
PUT /torch-pipeline/api/pipelines/runs/109133
```



**Path Parameters:**

| Parameter | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| runId | integer | Yes | The numeric ID of the run (e.g., `109133`) | 


### Request (Success)

```json
{
  "run": {
    "status": "COMPLETED"
  }
}
```



### Request (Failure)

```json
{
  "run": {
    "status": "FAILED",
    "result": "FAILED"
  }
}
```



**Status Changes**:

- Success: STARTED → COMPLETED
- Failure: STARTED → FAILED

## API Call Summary

**You used 6 APIs**:

1. `PUT /pipelines` - Created pipeline → Got pipeline.id = 15
2. `POST /pipelines/15/runs` - Created run → Got run.id = 109133
3. `PUT /pipelines/15/jobs` - Created 3 jobs
4. `POST /pipelines/runs/109133/spans` - Created 4 spans
5. `PUT /pipelines/runs/109133` - Updated run status (2x: START, COMPLETE)
6. `POST /pipelines/spans/:spanId/events` - Recorded events (multiple times)

---

## Troubleshooting

| Issue | Cause | Solution | 
| ---- | ---- | ---- | 
| Pipeline creation fails | UID already exists | Choose a unique uid or delete old pipeline | 
| Job creation fails | Invalid asset_uid | Verify asset exists in ADOC catalog | 
| Span creation fails | Invalid parentSpanId | Ensure root span created first | 
| Wrong field error | Using "ID" instead of "uid" | Always use lowercase "uid" in requests | 
| Events not showing | Wrong span ID | Verify span.id from creation response | 
| Run stuck in STARTED | Never marked complete | Always send final status update | 


---