# Source: https://docs.acceldata.io/api/set-up-pipeline-monitoring-and-alerting.md

# Set Up Pipeline Monitoring and Alerting

Reactive monitoring isn't enough - you need proactive alerting. This guide shows you how to set up intelligent monitoring that catches problems before they become incidents and alerts the right people at the right time.

---

## Why This Matters

Without proactive monitoring:

- You learn about failures from angry users
- Issues compound before you notice
- You can't spot degrading performance trends
- Your team wastes time on manual checks

With it:

- Alerts arrive before users notice
- Trends reveal problems early
- Your team focuses on fixes, not checking dashboards
- SLAs are protected

---

## Real-World Scenarios

### Scenario 1: The Silent Slowdown

"Pipeline execution time crept from 20 to 40 minutes over 2 weeks. Nobody noticed until monthly reports were late."

**Prevention**: Alert when execution time exceeds baseline by 50%.

**Impact**: Caught performance issues early, optimized queries, stayed within SLA.

### Scenario 2: The Weekend Outage

"Pipeline failed Friday night. Team discovered Monday morning. Weekend data missing."

**Prevention**: Immediate Slack/PagerDuty alert on any failure.

**Impact**: On-call engineer fixed it within 30 minutes. Zero data loss.

### Scenario 3: The Data Quality Drift

"Customer ages gradually became invalid. 1000 records corrupted before anyone noticed."

**Prevention**: Alert on warning event threshold (&gt;5 warnings = investigation needed).

**Impact**: Caught validation issues immediately, fixed upstream source.

### Scenario 4: The Capacity Crunch

"Pipeline hitting resource limits. Started failing intermittently."

**Prevention**: Alert when consecutive failures &gt; 2.

**Impact**: Identified capacity issue, scaled resources proactively.

---

## Prerequisites

- Existing pipeline with execution history
- Alert destination (Slack, PagerDuty, email)
- Baseline performance metrics (from historical runs)
- On-call rotation schedule

---

## Monitoring Strategy

Use these **4 APIs** to build proactive monitoring:

1. `PUT /pipelines` - Configure monitoring settings
2. `GET /pipelines/:pipelineId/runs` - Analyze history
3. `GET /pipelines/:pipelineId/latestRun` - Monitor current state
4. Investigation APIs - When alerts trigger

## Overview

This workflow covers:

- Setting up pipeline monitoring
- Configuring baseline metrics
- Querying execution history
- Building alerting logic using API data

**APIs Used**: 4 endpoints

---

## Prerequisites

- Existing pipeline with execution history
- API credentials
- Monitoring/alerting system (e.g., Slack, PagerDuty, custom dashboard)

---

## Step 1: Establish Baseline Metrics

Configure baseline metrics for your pipeline.

### API Call

```bash
PUT /torch-pipeline/api/pipelines
```



### Request

```json
{
  "pipeline": {
    "uid": "customer-etl-daily",
    "name": "Customer ETL Pipeline",
    "description": "Daily customer data sync from Athena to Redshift",
    "enabled": true,
    "scheduled": true,
    "schedulerType": "INTERNAL",
    "schedule": "0 2 * * *",
    "tags": ["production", "critical"],
    "pipelineBaselineMetric": {
      "includeSuccessfulRunsOnly": true,
      "metrics": 10,
      "unit": "RUNS"
    },
    "notificationChannels": "slack-data-alerts",
    "meta": {
      "owner": "data-team@company.com",
      "team": "data-engineering",
      "sla": "30_minutes",
      "alertThreshold": "2_failures"
    }
  }
}
```



### Key Configuration

| Field | Value | Purpose | 
| ---- | ---- | ---- | 
| pipelineBaselineMetric | Object | Define performance baseline | 
| notificationChannels | String | Alert destination | 
| meta.sla | String | Expected completion time | 
| meta.alertThreshold | String | When to trigger alerts | 


---

## Step 2: Collect Historical Performance Data

Gather execution history to establish normal behavior.

### API Call

```bash
GET /torch-pipeline/api/pipelines/15/runs?limit=30
```



### Response Analysis

```json
{
  "runs": [
    {
      "id": 109133,
      "status": "COMPLETED",
      "result": "SUCCESS",
      "startedAt": "2024-12-05T02:00:00Z",
      "finishedAt": "2024-12-05T02:28:00Z",
      "avgExecutionTime": "1680000"
    },
    {
      "id": 109132,
      "status": "COMPLETED",
      "result": "SUCCESS",
      "startedAt": "2024-12-04T02:00:00Z",
      "finishedAt": "2024-12-04T02:30:00Z",
      "avgExecutionTime": "1800000"
    }
  ]
}
```



### Calculate Baselines

From 30 runs, calculate:

- **Average execution time**: 28 minutes
- **Success rate**: 93% (28 success / 30 total)
- **Typical start time**: 2:00 AM
- **SLA**: 30 minutes (worst case)

---

## Step 3: Monitor Current Execution

Build real-time monitoring by polling latest run.

### API Call

```bash
GET /torch-pipeline/api/pipelines/15/latestRun
```



### Monitoring Logic

```javascript
// Pseudo-code for monitoring system
function checkPipelineHealth(pipelineId) {
  const latestRun = GET(`/pipelines/${pipelineId}/latestRun`)
  
  // Check 1: Execution time
  if (latestRun.avgExecutionTime > BASELINE * 1.5) {
    alert('SLOW_EXECUTION', latestRun)
  }
  
  // Check 2: Status
  if (latestRun.status === 'COMPLETED' && latestRun.result === 'FAILED') {
    alert('PIPELINE_FAILED', latestRun)
  }
  
  // Check 3: Error events
  if (latestRun.errorEvents > 0) {
    alert('ERRORS_DETECTED', latestRun)
  }
  
  // Check 4: Warning accumulation
  if (latestRun.warningEvents > 5) {
    alert('EXCESSIVE_WARNINGS', latestRun)
  }
}

// Poll every 5 minutes
setInterval(() => checkPipelineHealth(15), 300000)
```



---

## Step 4: Deep Dive on Anomalies

When alerts trigger, gather detailed information.

### Get Span Details

```bash
GET /torch-pipeline/api/pipelines/runs/109134/spans
```



**Look for:**

- Spans with excessive duration
- Spans with high error/warning counts
- Skipped spans indicating failures

### Get Error Events

```bash
GET /torch-pipeline/api/pipelines/spans/5012/events
```



**Look for:**

- FAILED event types
- Alert levels (ERROR, WARNING)
- Context data with error details

### Get Detailed Logs

```bash
GET /torch-pipeline/api/pipelines/spans/events/2003/log
```



**Extract:**

- Error messages
- Stack traces
- Affected data samples

---

## Step 5: Build Alerting Rules

### Alert Rule 1: Pipeline Failure

```javascript
function checkFailure(pipelineId) {
  const run = GET(`/pipelines/${pipelineId}/latestRun`)
  
  if (run.result === 'FAILED') {
    const spans = GET(`/pipelines/runs/${run.id}/spans`)
    const failedSpan = spans.find(s => s.status === 'FAILED')
    
    sendAlert({
      severity: 'CRITICAL',
      title: `Pipeline ${pipelineId} Failed`,
      message: `Run ${run.id} failed in span ${failedSpan.uid}`,
      runId: run.id,
      spanId: failedSpan.id
    })
  }
}
```



### Alert Rule 2: SLA Breach

```javascript
function checkSLA(pipelineId, slaMinutes) {
  const run = GET(`/pipelines/${pipelineId}/latestRun`)
  const executionMinutes = run.avgExecutionTime / 60000
  
  if (run.status === 'RUNNING' && executionMinutes > slaMinutes) {
    sendAlert({
      severity: 'WARNING',
      title: `Pipeline ${pipelineId} Exceeding SLA`,
      message: `Run ${run.id} has been running for ${executionMinutes} minutes (SLA: ${slaMinutes} min)`,
      runId: run.id
    })
  }
}
```



### Alert Rule 3: Increasing Error Rate

```javascript
function checkErrorTrend(pipelineId) {
  const runs = GET(`/pipelines/${pipelineId}/runs?limit=10`)
  
  const errorRate = runs.filter(r => r.result === 'FAILED').length / runs.length
  
  if (errorRate > 0.3) { // 30% failure rate
    sendAlert({
      severity: 'HIGH',
      title: `High Failure Rate for Pipeline ${pipelineId}`,
      message: `${errorRate * 100}% of last 10 runs failed`,
      recentRuns: runs.slice(0, 5)
    })
  }
}
```



### Alert Rule 4: Data Quality Warnings

```javascript
function checkDataQuality(pipelineId) {
  const run = GET(`/pipelines/${pipelineId}/latestRun`)
  
  if (run.warningEvents > 5) {
    const spans = GET(`/pipelines/runs/${run.id}/spans`)
    const spanWithWarnings = spans.find(s => s.warningEvents > 0)
    const events = GET(`/pipelines/spans/${spanWithWarnings.id}/events`)
    
    sendAlert({
      severity: 'MEDIUM',
      title: `Data Quality Issues in Pipeline ${pipelineId}`,
      message: `Run ${run.id} has ${run.warningEvents} warnings`,
      details: events.filter(e => e.alert === 'WARNING')
    })
  }
}
```



---

## Step 6: Dashboard Metrics

Build a monitoring dashboard using these metrics.

### Overall Health

```bash
GET /torch-pipeline/api/pipelines/summary
```



Display:

- Total pipelines
- Active vs disabled
- Success rate across all pipelines

### Per-Pipeline Status

```bash
GET /torch-pipeline/api/pipelines/15/latestRun
```



Display:

- Current status (RUNNING, COMPLETED, FAILED)
- Execution time vs baseline
- Error/warning counts
- Last successful run time

### Historical Trends

```bash
GET /torch-pipeline/api/pipelines/15/runs?limit=50
```



Display:

- Success rate chart (last 50 runs)
- Execution time trend
- Failure patterns by time of day

### Execution Timeline

```bash
GET /torch-pipeline/api/pipelines/runs/109133/spans
```



Display:

- Span execution timeline
- Bottleneck identification
- Duration breakdown by job

---

## Monitoring Workflow Summary

### Setup Phase (Once)

```bash
1. PUT /pipelines
   → Configure baseline metrics and notification channels

2. GET /pipelines/:pipelineId/runs?limit=30
   → Collect historical data for baseline calculation
```



### Runtime Monitoring (Continuous)

```bash
3. GET /pipelines/:pipelineId/latestRun
   → Poll current status (every 5 min)

4. If anomaly detected:
   GET /pipelines/runs/:runId/spans
   GET /pipelines/spans/:spanId/events
   GET /pipelines/spans/events/:eventId/log
   → Gather details for alert
```



---

## Complete Monitoring System Example

### Monitoring Script (Pseudo-code)

```javascript
// Configuration
const PIPELINES = [15, 16, 17]
const POLL_INTERVAL = 300000 // 5 minutes
const SLA_MINUTES = 30

// Baseline data (from historical analysis)
const BASELINES = {
  15: { avgTime: 1680000, successRate: 0.93 },
  16: { avgTime: 2400000, successRate: 0.95 },
  17: { avgTime: 900000, successRate: 0.98 }
}

// Main monitoring loop
setInterval(() => {
  PIPELINES.forEach(pipelineId => {
    monitorPipeline(pipelineId)
  })
}, POLL_INTERVAL)

function monitorPipeline(pipelineId) {
  const run = GET(`/pipelines/${pipelineId}/latestRun`)
  const baseline = BASELINES[pipelineId]
  
  // Check multiple conditions
  checkFailure(run, pipelineId)
  checkSLA(run, SLA_MINUTES)
  checkPerformance(run, baseline)
  checkErrorRate(pipelineId)
}

function checkFailure(run, pipelineId) {
  if (run.result === 'FAILED') {
    const details = investigateFailure(run.id)
    sendAlert('CRITICAL', details)
  }
}

function checkPerformance(run, baseline) {
  const slowness = run.avgExecutionTime / baseline.avgTime
  
  if (slowness > 1.5) {
    sendAlert('WARNING', {
      message: `Pipeline running ${slowness}x slower than baseline`
    })
  }
}

function investigateFailure(runId) {
  const spans = GET(`/pipelines/runs/${runId}/spans`)
  const failedSpan = spans.find(s => s.status === 'FAILED')
  const events = GET(`/pipelines/spans/${failedSpan.id}/events`)
  const errorEvent = events.find(e => e.eventType === 'FAILED')
  const log = GET(`/pipelines/spans/events/${errorEvent.id}/log`)
  
  return {
    runId,
    spanId: failedSpan.id,
    error: log.message,
    details: log.details
  }
}
```



---

## Complete API Call Sequence

1. `PUT /torch-pipeline/api/pipelines` - Configure monitoring
2. `GET /torch-pipeline/api/pipelines/:pipelineId/runs` - Historical analysis
3. `GET /torch-pipeline/api/pipelines/:pipelineId/latestRun` - Current status
4. `GET /torch-pipeline/api/pipelines/runs/:runId/spans` - Anomaly investigation
5. `GET /torch-pipeline/api/pipelines/spans/:spanId/events` - Error details
6. `GET /torch-pipeline/api/pipelines/spans/events/:eventId/log` - Deep logs

---

## Alerting Best Practices

### Alert Fatigue Prevention

- Use tiered severity (CRITICAL, HIGH, MEDIUM, LOW)
- Aggregate similar alerts
- Set cooldown periods between alerts

### Actionable Alerts

Include in every alert:

- Direct link to run/span
- Error message summary
- Recommended next steps
- Runbook link

### Alert Escalation

1. **First failure**: INFO alert to team Slack
2. **Second consecutive failure**: HIGH alert to on-call
3. **Third consecutive failure**: CRITICAL page to manager

---

## Troubleshooting

| Issue | Solution | 
| ---- | ---- | 
| Too many alerts | Adjust thresholds, add cooldown periods | 
| Missing alerts | Lower polling interval, check alert logic | 
| False positives | Refine baseline calculations | 
| Alert fatigue | Implement tiered severity system | 


---