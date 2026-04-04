# Source: https://docs.acceldata.io/api/debug-a-failed-pipeline-run.md

# Debug a Failed Pipeline Run

This is your troubleshooting guide - how to investigate pipeline failures quickly and systematically. You'll learn to identify exactly what failed, why it failed, and where the problem originated.

---

## Why This Matters

When a pipeline fails at 2 AM, you need answers fast:

- **What** failed? (Which job/span?)
- **When** did it fail? (Exact timestamp)
- **Why** did it fail? (Error message and context)
- **Where** in the code? (Stack traces and logs)

Without this workflow, you're guessing. With it, you have forensics.

---

## Real-World Scenarios

### Scenario 1: The Midnight Page

"Production pipeline failed. Data team needs it fixed in 1 hour for morning reports."

**Pressure**: High. Time: Limited. Need: Fast root cause.

**Solution**: Follow this workflow in 5 minutes to find exact error, affected data, and next steps.

### Scenario 2: The Mystery Failure

"Pipeline ran fine for 3 months, then started failing every day this week."

**Challenge**: Something changed, but what?

**Solution**: Compare failed runs with successful runs. Look for patterns in error events, execution times, and data volumes.

### Scenario 3: Data Quality Crisis

"Dashboard shows missing customer records. Pipeline says 'success' but data is wrong."

**Problem**: Silent failure - no error but wrong results.

**Solution**: Check span events for warnings, examine event logs for data quality metrics, trace exactly which records were processed.

### Scenario 4: The Cascading Failure

"One pipeline failed and now 5 downstream pipelines are broken."

**Urgency**: Fix root cause to unblock everything else.

**Solution**: Identify the first failure point, understand what data was missing, coordinate fixes.

---

## Prerequisites

- Pipeline ID with failed runs
- API credentials
- Basic understanding of your pipeline structure
- (Optional) Access to your code repository for context

---

## The Debug Workflow

Use these **5 APIs** to investigate failures:

1. `GET /pipelines/:pipelineId/latestRun` - Identify failure
2. `GET /pipelines/runs/:runId/spans` - Find failed span
3. `GET /pipelines/spans/:spanId/events` - Get error events
4. `GET /pipelines/spans/events/:eventId/log` - Get error details
5. `GET /pipelines/runs/:runId/span-job-associations` - Map to code

---

## Overview

This workflow covers:

- Identifying which run failed
- Finding the failing span
- Analyzing error events
- Reviewing detailed error logs
- Understanding span-job mappings for root cause

**APIs Used**: 5 endpoints

---

## Prerequisites

- Pipeline ID that has failed runs
- API credentials
- Basic understanding of your pipeline structure

---

## Step 1: Identify the Failed Run

Start by getting the latest run to see if it failed.

### API Call

```bash
GET /torch-pipeline/api/pipelines/15/latestRun
```



### Response (Failed Run)

```json
{
  "run": {
    "id": 109134,
    "pipelineId": 15,
    "continuationId": "run-2024-12-05-002",
    "status": "COMPLETED",
    "result": "FAILED",
    "startedAt": "2024-12-05T14:00:00Z",
    "finishedAt": "2024-12-05T14:15:00Z",
    "avgExecutionTime": "900000",
    "successEvents": 3,
    "errorEvents": 2,
    "warningEvents": 0
  }
}
```



**Key Indicators:**

- `status: "COMPLETED"` - Run finished
- `result: "FAILED"` - Run failed
- `errorEvents: 2` - Two errors occurred

### Alternative: List Recent Runs

If you need to see multiple failed runs:

```bash
GET /torch-pipeline/api/pipelines/15/runs?limit=10
```



Filter response for runs where `result: "FAILED"`.

---

## Step 2: Get All Spans for the Failed Run

Identify which span(s) failed.

### API Call

```bash
GET /torch-pipeline/api/pipelines/runs/109134/spans
```



### Response

```json
{
  "spans": [
    {
      "id": 5010,
      "uid": "span-pipeline-root",
      "pipelineRunId": 109134,
      "parentSpanId": null,
      "status": "COMPLETED",
      "successEvents": 3,
      "errorEvents": 2
    },
    {
      "id": 5011,
      "uid": "span-extract",
      "pipelineRunId": 109134,
      "parentSpanId": 5010,
      "status": "COMPLETED",
      "startedAt": "2024-12-05T14:00:00Z",
      "finishedAt": "2024-12-05T14:05:00Z",
      "successEvents": 2,
      "errorEvents": 0
    },
    {
      "id": 5012,
      "uid": "span-transform",
      "pipelineRunId": 109134,
      "parentSpanId": 5010,
      "status": "FAILED",
      "startedAt": "2024-12-05T14:05:00Z",
      "finishedAt": "2024-12-05T14:15:00Z",
      "successEvents": 1,
      "errorEvents": 2
    },
    {
      "id": 5013,
      "uid": "span-load",
      "pipelineRunId": 109134,
      "parentSpanId": 5010,
      "status": "SKIPPED",
      "successEvents": 0,
      "errorEvents": 0
    }
  ]
}
```



**Analysis:**

- Extract span (5011) - COMPLETED successfully
- Transform span (5012) - FAILED with 2 errors
- Load span (5013) - SKIPPED (didn't run due to previous failure)

**The transform span is the culprit!**

---

## Step 3: Get Events for the Failed Span

Examine what happened during the failed span.

### API Call

```bash
GET /torch-pipeline/api/pipelines/spans/5012/events
```



### Response

```json
{
  "events": [
    {
      "id": 2001,
      "spanId": 5012,
      "eventType": "START",
      "timestamp": "2024-12-05T14:05:00Z"
    },
    {
      "id": 2002,
      "spanId": 5012,
      "eventType": "LOG",
      "timestamp": "2024-12-05T14:07:00Z",
      "contextData": {
        "message": "Starting data transformation",
        "inputRecords": 10000
      }
    },
    {
      "id": 2003,
      "spanId": 5012,
      "eventType": "FAILED",
      "timestamp": "2024-12-05T14:10:00Z",
      "alert": "ERROR",
      "contextData": {
        "error": "NullPointerException",
        "message": "Column 'customer_age' contains null values",
        "affectedRows": 150
      }
    },
    {
      "id": 2004,
      "spanId": 5012,
      "eventType": "FAILED",
      "timestamp": "2024-12-05T14:15:00Z",
      "alert": "ERROR",
      "contextData": {
        "error": "TransformationAborted",
        "message": "Transformation aborted due to data quality issues"
      }
    }
  ]
}
```



**Root Cause Identified:**

- Error event at 14:10:00: `NullPointerException`
- Problem: Column 'customer_age' has 150 null values
- Result: Transformation aborted

---

## Step 4: Get Detailed Error Log

Get full details for the specific error event.

### API Call

```bash
GET /torch-pipeline/api/pipelines/spans/events/2003/log
```



### Response

```json
{
  "log": {
    "eventId": 2003,
    "spanId": 5012,
    "timestamp": "2024-12-05T14:10:00Z",
    "level": "ERROR",
    "message": "Column 'customer_age' contains null values",
    "details": {
      "errorType": "NullPointerException",
      "errorCode": "DATA_QUALITY_001",
      "column": "customer_age",
      "table": "customers_staging",
      "affectedRows": 150,
      "totalRows": 10000,
      "percentage": "1.5%",
      "sampleValues": [
        {"customer_id": "C12345", "customer_age": null},
        {"customer_id": "C12388", "customer_age": null},
        {"customer_id": "C12401", "customer_age": null}
      ]
    },
    "stackTrace": "at com.acceldata.transform.AgeValidator.validate(AgeValidator.java:45)\nat com.acceldata.transform.DataTransformer.transform(DataTransformer.java:112)"
  }
}
```



**Complete Picture:**

- **What**: NullPointerException in customer_age column
- **Where**: AgeValidator.validate() method
- **Impact**: 150 rows (1.5% of data)
- **Sample Data**: Includes customer IDs with null ages

---

## Step 5: Map Span to Job

Identify which job in your pipeline corresponds to the failed span.

### API Call

```bash
GET /torch-pipeline/api/pipelines/runs/109134/span-job-associations
```



### Response

```json
{
  "associations": [
    {
      "spanId": 5011,
      "spanUid": "span-extract",
      "jobUid": "job-extract-customers"
    },
    {
      "spanId": 5012,
      "spanUid": "span-transform",
      "jobUid": "job-transform-customers"
    },
    {
      "spanId": 5013,
      "spanUid": "span-load",
      "jobUid": "job-load-redshift"
    }
  ]
}
```



**Failed Job Identified:**

- Span 5012 (span-transform) → Job: `job-transform-customers`

Now you know exactly which job code to fix!

---

## Step 6: Get Specific Span Details (Optional)

For additional context about the failed span.

### API Call

```bash
GET /torch-pipeline/api/pipelines/runs/109134/spans/5012
```



This uses the `:identity` parameter to get a specific span.

### Response

```json
{
  "span": {
    "id": 5012,
    "uid": "span-transform",
    "pipelineRunId": 109134,
    "parentSpanId": 5010,
    "status": "FAILED",
    "startedAt": "2024-12-05T14:05:00Z",
    "finishedAt": "2024-12-05T14:15:00Z",
    "totalTime": 600000,
    "avgExecutionTime": "900000",
    "successEvents": 1,
    "errorEvents": 2,
    "warningEvents": 0
  }
}
```



---

## Debugging Workflow Summary

### Quick Debug (5 API calls)

```bash
1. GET /pipelines/15/latestRun
   → Confirm failure, get run ID

2. GET /pipelines/runs/109134/spans
   → Find which span failed

3. GET /pipelines/spans/5012/events
   → See error events

4. GET /pipelines/spans/events/2003/log
   → Get full error details

5. GET /pipelines/runs/109134/span-job-associations
   → Map span to job code
```



---

## Common Failure Patterns

### Pattern 1: Data Quality Issues

**Symptoms:**

- FAILED events in transform/validation spans
- Error messages about null values, data types, or constraints

**Debug Steps:**

1. Check span events for specific error messages
2. Review event logs for sample data
3. Examine upstream extraction job

### Pattern 2: Connection Failures

**Symptoms:**

- FAILED events in extract or load spans
- Timeout or connection error messages

**Debug Steps:**

1. Check span events for connection errors
2. Verify source/destination availability
3. Review network/credential configuration

### Pattern 3: Resource Exhaustion

**Symptoms:**

- FAILED events after long execution times
- Out-of-memory or timeout errors

**Debug Steps:**

1. Compare span execution times across runs
2. Check for unusual data volume
3. Review resource allocation

---

## Resolution Steps

Once you've identified the issue:

### 1. Fix the Code/Configuration

Based on the error identified:

- **Data Quality**: Add null handling or validation
- **Connection**: Fix credentials or endpoints
- **Resource**: Optimize query or increase resources

### 2. Test the Fix

Use the "Create and Execute" workflow to test your changes.

### 3. Monitor the Next Run

Use the "Monitor" workflow to verify the fix worked.

---

## Complete API Call Sequence

1. `GET /torch-pipeline/api/pipelines/:pipelineId/latestRun` - Identify failure
2. `GET /torch-pipeline/api/pipelines/:pipelineId/runs` - Alternative: list recent runs
3. `GET /torch-pipeline/api/pipelines/runs/:runId/spans` - Find failed span
4. `GET /torch-pipeline/api/pipelines/spans/:spanId/events` - Get error events
5. `GET /torch-pipeline/api/pipelines/spans/events/:spanEventId/log` - Get error details
6. `GET /torch-pipeline/api/pipelines/runs/:runId/span-job-associations` - Map to job
7. `GET /torch-pipeline/api/pipelines/runs/:runId/spans/:identity` - Optional: specific span details

---

## Troubleshooting

| Issue | Solution | 
| ---- | ---- | 
| No failed runs found | Check pipeline ID is correct | 
| Can't find failed span | Look for `errorEvents > 0` or `status: "FAILED"` | 
| Events don't show error | Check for FAILED event type or alert: "ERROR" | 
| No log details | Verify event ID is correct | 
| Can't map span to job | Check span-job-associations response | 


---