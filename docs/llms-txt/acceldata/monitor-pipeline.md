# Source: https://docs.acceldata.io/api/monitor-pipeline.md

# Monitor an Existing Pipeline

This guide teaches you how to monitor pipelines in production - tracking their health, performance, and execution history. You'll learn to spot problems before they become incidents and understand exactly what's happening inside your data pipelines.

---

## Why This Matters

A pipeline that runs silently is dangerous. Without monitoring, you won't know:

- If it failed overnight
- If it's running slower than usual
- If data quality issues are creeping in
- Which step is the bottleneck

Good monitoring means catching issues in minutes, not hours or days.

---

## Real-World Scenarios

### Scenario 1: Daily Health Check

"It's 8 AM. Did our customer pipeline run successfully last night?"

**Solution**: Check `GET /pipelines/15/latestRun` to see status, duration, and any errors. Takes 5 seconds.

### Scenario 2: Performance Degradation

"Our pipeline used to finish in 20 minutes, now it takes 45. What changed?"

**Solution**: Use `GET /pipelines/15/runs?limit=30` to see the last 30 runs and spot when slowdown began. Then drill into spans to find the bottleneck.

### Scenario 3: Debugging for On-Call

"I got paged at 2 AM. The pipeline failed but I need details fast."

**Solution**: Get latest run → list spans → find failed span → get events → get error logs. Full investigation in under 2 minutes.

### Scenario 4: Capacity Planning

"Should we add more resources? Is our pipeline hitting limits?"

**Solution**: Analyze historical runs to see execution time trends, event counts, and identify patterns.

---

## Prerequisites

- Pipeline ID or UID you want to monitor
- API credentials
- Understanding of what the pipeline does

---

## Monitoring Dashboard - API Workflow

Build a complete monitoring view using these **6 APIs**:

1. `GET /pipelines/:pipelineId/latestRun` - Current status
2. `GET /pipelines/:pipelineId/runs` - Historical runs
3. `GET /pipelines/runs/:runId/spans` - Execution breakdown
4. `GET /pipelines/spans/:spanId/events` - Event details
5. `GET /pipelines/spans/events/:eventId/log` - Deep logs
6. `GET /pipelines/runs/:runId/span-job-associations` - Job mappings

## Overview

This workflow covers:

- Listing all runs for a pipeline
- Getting the latest run status
- Viewing span execution details
- Querying span events and logs
- Understanding job-span associations

**APIs Used**: 5 endpoints

---

## Prerequisites

- Pipeline ID or UID
- API credentials
- Understanding of pipeline execution concepts

---

## Step 1: Get Latest Run Status

Check the most recent execution of your pipeline.

### API Call

```bash
GET /torch-pipeline/api/pipelines/15/latestRun
```



### Response

```json
{
  "run": {
    "id": 109133,
    "pipelineId": 15,
    "continuationId": "run-2024-12-05-001",
    "status": "RUNNING",
    "startedAt": "2024-12-05T10:00:00Z",
    "avgExecutionTime": "1800000",
    "successEvents": 2,
    "errorEvents": 0,
    "warningEvents": 1
  }
}
```



### Key Metrics

| Field | Description | 
| ---- | ---- | 
| status | Current execution status (CREATED, RUNNING, COMPLETED, FAILED) | 
| startedAt | When execution began | 
| avgExecutionTime | Average execution time in milliseconds | 
| successEvents | Count of successful span events | 
| errorEvents | Count of error events | 
| warningEvents | Count of warning events | 


### Use Cases

- Dashboard displays showing current pipeline status
- Quick health checks
- Alerting based on execution metrics

---

## Step 2: List All Pipeline Runs

View historical execution data for analysis.

### API Call

```bash
GET /torch-pipeline/api/pipelines/15/runs
```



### Query Parameters

| Parameter | Type | Description | Default | 
| ---- | ---- | ---- | ---- | 
| limit | integer | Number of runs to return | 50 | 
| offset | integer | Pagination offset | 0 | 


### Example with Pagination

```bash
GET /torch-pipeline/api/pipelines/15/runs?limit=10&offset=0
```



### Response

```json
{
  "runs": [
    {
      "id": 109133,
      "pipelineId": 15,
      "continuationId": "run-2024-12-05-001",
      "status": "COMPLETED",
      "result": "SUCCESS",
      "startedAt": "2024-12-05T10:00:00Z",
      "finishedAt": "2024-12-05T10:30:00Z",
      "avgExecutionTime": "1800000"
    },
    {
      "id": 109132,
      "pipelineId": 15,
      "continuationId": "run-2024-12-04-001",
      "status": "COMPLETED",
      "result": "SUCCESS",
      "startedAt": "2024-12-04T10:00:00Z",
      "finishedAt": "2024-12-04T10:28:00Z",
      "avgExecutionTime": "1680000"
    }
  ],
  "total": 245,
  "limit": 10,
  "offset": 0
}
```



### Use Cases

- Analyzing execution trends over time
- Identifying performance degradation
- Generating historical reports
- Debugging recurring failures

---

## Step 3: List All Spans for a Run

View the execution tree of a specific run.

### API Call

```bash
GET /torch-pipeline/api/pipelines/runs/109133/spans
```



### Response

```json
{
  "spans": [
    {
      "id": 5000,
      "uid": "span-pipeline-root",
      "pipelineRunId": 109133,
      "parentSpanId": null,
      "status": "COMPLETED",
      "startedAt": "2024-12-05T10:00:00Z",
      "finishedAt": "2024-12-05T10:30:00Z",
      "totalTime": 1800000,
      "successEvents": 5,
      "errorEvents": 0,
      "warningEvents": 1
    },
    {
      "id": 5001,
      "uid": "span-extract",
      "pipelineRunId": 109133,
      "parentSpanId": 5000,
      "status": "COMPLETED",
      "startedAt": "2024-12-05T10:00:00Z",
      "finishedAt": "2024-12-05T10:05:00Z",
      "totalTime": 300000,
      "successEvents": 2,
      "errorEvents": 0,
      "warningEvents": 0
    },
    {
      "id": 5002,
      "uid": "span-transform",
      "pipelineRunId": 109133,
      "parentSpanId": 5000,
      "status": "COMPLETED",
      "startedAt": "2024-12-05T10:05:00Z",
      "finishedAt": "2024-12-05T10:20:00Z",
      "totalTime": 900000,
      "successEvents": 2,
      "errorEvents": 0,
      "warningEvents": 1
    },
    {
      "id": 5003,
      "uid": "span-load",
      "pipelineRunId": 109133,
      "parentSpanId": 5000,
      "status": "COMPLETED",
      "startedAt": "2024-12-05T10:20:00Z",
      "finishedAt": "2024-12-05T10:30:00Z",
      "totalTime": 600000,
      "successEvents": 2,
      "errorEvents": 0,
      "warningEvents": 0
    }
  ]
}
```



### Use Cases

- Understanding execution flow
- Identifying bottlenecks
- Debugging span-level issues
- Visualizing execution timeline

---

## Step 4: Get Events for a Specific Span

View detailed events that occurred during span execution.

### API Call

```bash
GET /torch-pipeline/api/pipelines/spans/5002/events
```



### Response

```json
{
  "events": [
    {
      "id": 1001,
      "spanId": 5002,
      "eventType": "START",
      "timestamp": "2024-12-05T10:05:00Z"
    },
    {
      "id": 1002,
      "spanId": 5002,
      "eventType": "LOG",
      "timestamp": "2024-12-05T10:10:00Z",
      "contextData": {
        "message": "Processing 10,000 records",
        "recordCount": 10000
      }
    },
    {
      "id": 1003,
      "spanId": 5002,
      "eventType": "LOG",
      "timestamp": "2024-12-05T10:15:00Z",
      "contextData": {
        "message": "Data quality check passed with 1 warning",
        "warningType": "MISSING_VALUES",
        "affectedRows": 5
      },
      "alert": "WARNING"
    },
    {
      "id": 1004,
      "spanId": 5002,
      "eventType": "END",
      "timestamp": "2024-12-05T10:20:00Z"
    }
  ]
}
```



### Event Types

| Type | Description | 
| ---- | ---- | 
| START | Span execution began | 
| END | Span execution completed successfully | 
| FAILED | Span execution failed | 
| LOG | Informational log message | 
| ABORT | Span execution was aborted | 


### Use Cases

- Debugging span failures
- Understanding execution steps
- Tracking data quality issues
- Performance analysis

---

## Step 5: Get Detailed Event Logs

Retrieve detailed logs for a specific event.

### API Call

```bash
GET /torch-pipeline/api/pipelines/spans/events/1003/log
```



### Response

```json
{
  "log": {
    "eventId": 1003,
    "spanId": 5002,
    "timestamp": "2024-12-05T10:15:00Z",
    "level": "WARNING",
    "message": "Data quality check passed with 1 warning",
    "details": {
      "checkType": "MISSING_VALUES",
      "table": "customers_staging",
      "column": "email",
      "affectedRows": 5,
      "totalRows": 10000,
      "percentage": "0.05%"
    },
    "stackTrace": null
  }
}
```



### Use Cases

- Investigating specific warnings or errors
- Root cause analysis
- Compliance and audit trails

---

## Step 6: Get Job-Span Associations

Understand which jobs are associated with which spans.

### API Call

```bash
GET /torch-pipeline/api/pipelines/runs/109133/span-job-associations
```



### Response

```json
{
  "associations": [
    {
      "spanId": 5001,
      "spanUid": "span-extract",
      "jobUid": "job-extract-customers"
    },
    {
      "spanId": 5002,
      "spanUid": "span-transform",
      "jobUid": "job-transform-customers"
    },
    {
      "spanId": 5003,
      "spanUid": "span-load",
      "jobUid": "job-load-redshift"
    }
  ]
}
```



### Use Cases

- Mapping execution to pipeline structure
- Debugging job-specific issues
- Understanding execution flow

---

## Monitoring Dashboard Workflow

Build a complete monitoring view:

### Real-time Status

```bash
1. GET /torch-pipeline/api/pipelines/15/latestRun
   → Display: Current status, execution time, event counts
```



### Execution Timeline

```bash
2. GET /torch-pipeline/api/pipelines/runs/109133/spans
   → Display: Span hierarchy, durations, statuses
```



### Drill-down Investigation

```bash
3. GET /torch-pipeline/api/pipelines/spans/5002/events
   → Display: Detailed event log for selected span
```



### Deep Analysis

```bash
4. GET /torch-pipeline/api/pipelines/spans/events/1003/log
   → Display: Full log details for selected event
```



---

## Performance Monitoring Pattern

**Track execution trends:**

```bash
# Get last 30 runs
GET /torch-pipeline/api/pipelines/15/runs?limit=30&offset=0

# Analyze:
- Average execution time trends
- Failure rate over time
- Event count patterns
- Performance degradation indicators
```



---

## Complete API Call Sequence

1. `GET /torch-pipeline/api/pipelines/:pipelineId/latestRun` - Current status
2. `GET /torch-pipeline/api/pipelines/:pipelineId/runs` - Historical data
3. `GET /torch-pipeline/api/pipelines/runs/:runId/spans` - Execution tree
4. `GET /torch-pipeline/api/pipelines/spans/:spanId/events` - Event details
5. `GET /torch-pipeline/api/pipelines/spans/events/:spanEventId/log` - Deep logs
6. `GET /torch-pipeline/api/pipelines/runs/:runId/span-job-associations` - Job mappings

---

## Troubleshooting

| Issue | Solution | 
| ---- | ---- | 
| No runs returned | Verify pipeline has been executed at least once | 
| Missing spans | Check that run ID is correct | 
| No events | Verify spans have recorded events during execution | 
| Empty logs | Check that event ID is valid | 


---