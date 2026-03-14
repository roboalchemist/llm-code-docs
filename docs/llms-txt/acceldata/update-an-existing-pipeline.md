# Source: https://docs.acceldata.io/api/update-an-existing-pipeline.md

# Update an Existing Pipeline

Pipelines evolve - requirements change, data sources move, optimizations are needed. This guide shows you how to safely update pipeline configurations, modify job structures, and verify your changes.

---

## Why This Matters

Updating a production pipeline is risky. Done wrong, you can:

- Break downstream systems
- Lose data
- Create silent failures
- Disrupt on-call schedules

This workflow minimizes risk by showing you how to update pipelines safely and verify changes before they impact production.

---

## Real-World Scenarios

### Scenario 1: New Team Ownership

"Data engineering is splitting into two teams. We need to update pipeline ownership."

**Change**: Update metadata (owner, team, Slack channel) 

**Risk**: Low 

**Solution**: Simple `PUT /pipelines` with new metadata

### Scenario 2: Add Data Quality Check

"We're getting bad data. Need to add a validation step between Extract and Load."

**Change**: Insert new job into pipeline 

**Risk**: Medium (changes data flow) 

**Solution**: Create new job, update dependencies, verify graph

### Scenario 3: Migrate Data Source

"We're moving from Athena to Snowflake. Update all pipelines."

**Change**: Update asset_uid in job configurations 

**Risk**: High (wrong UID = data loss) 

**Solution**: Test in staging, verify connections, gradual rollout

### Scenario 4: Enable Scheduling

"Manual pipeline is stable. Time to automate with daily schedule."

**Change**: Update `scheduled: true` and add cron expression 

**Risk**: Low 

**Solution**: Update pipeline config, monitor first few automated runs

---

## Prerequisites

- Pipeline ID or UID to update
- New configuration values
- Understanding of current pipeline structure
- (Recommended) Testing environment

---

## Update Strategies

Use these **3 APIs** to modify pipelines:

1. `GET /pipelines/:identity` - Get current config
2. `PUT /pipelines` - Update pipeline
3. `GET /pipelines/:pipelineId/graph` - Verify changes

## Overview

This workflow covers:

- Retrieving current pipeline configuration
- Updating pipeline metadata and settings
- Modifying the pipeline graph structure
- Verifying changes were applied

**APIs Used**: 3 endpoints

---

## Prerequisites

- Pipeline ID or UID to update
- API credentials
- Understanding of desired changes

---

## Step 1: Get Current Pipeline Configuration

Before making changes, retrieve the current configuration.

### API Call

```bash
GET /torch-pipeline/api/pipelines/customer-etl-daily
```



### Response

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
    "tags": ["production", "daily"],
    "createdAt": "2024-08-20T05:15:46.569Z",
    "updatedAt": "2024-12-05T10:00:00Z",
    "meta": {
      "owner": "data-team@company.com",
      "team": "data-engineering",
      "codeLocation": "https://github.com/company/pipelines/customer-etl"
    }
  }
}
```



**Save this configuration** - you'll modify and send it back.

---

## Step 2: Modify Pipeline Configuration

Update the pipeline using the same endpoint as creation.

### API Call

```bash
PUT /torch-pipeline/api/pipelines
```



### Update Scenarios

#### Scenario 1: Enable Scheduling

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
    "tags": ["production", "daily", "scheduled"],
    "meta": {
      "owner": "data-team@company.com",
      "team": "data-engineering",
      "codeLocation": "https://github.com/company/pipelines/customer-etl"
    }
  }
}
```



**Changes:**

- `scheduled`: false → true
- `schedule`: Added cron expression (2 AM daily)
- `tags`: Added "scheduled" tag

#### Scenario 2: Change Ownership

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
    "tags": ["production", "daily", "scheduled"],
    "meta": {
      "owner": "analytics-team@company.com",
      "team": "analytics",
      "codeLocation": "https://github.com/company/pipelines/customer-etl"
    }
  }
}
```



**Changes:**

- `meta.owner`: data-team → analytics-team
- `meta.team`: data-engineering → analytics

#### Scenario 3: Disable Pipeline

```json
{
  "pipeline": {
    "uid": "customer-etl-daily",
    "name": "Customer ETL Pipeline",
    "description": "Daily customer data sync from Athena to Redshift - TEMPORARILY DISABLED",
    "enabled": false,
    "scheduled": true,
    "schedulerType": "INTERNAL",
    "schedule": "0 2 * * *",
    "tags": ["production", "daily", "scheduled", "disabled"],
    "meta": {
      "owner": "analytics-team@company.com",
      "team": "analytics",
      "codeLocation": "https://github.com/company/pipelines/customer-etl"
    }
  }
}
```



**Changes:**

- `enabled`: true → false
- `description`: Added "TEMPORARILY DISABLED" note
- `tags`: Added "disabled" tag

---

## Step 3: Update Pipeline Jobs

Modify job structure by creating/updating job nodes.

### API Call

```bash
PUT /torch-pipeline/api/pipelines/15/jobs
```



### Scenario: Add a New Job

Add a data quality validation job between extract and transform.

```json
{
  "name": "Validate Customer Data",
  "uid": "job-validate-customers",
  "pipeLineRunId": 109135,
  "inputs": [
    {
      "jobUid": "job-extract-customers"
    }
  ],
  "outputs": [],
  "meta": {
    "owner": "analytics-team@company.com",
    "team": "analytics",
    "validationType": "schema_and_quality"
  }
}
```



### Scenario: Update Existing Job

Update the transform job to take input from validation instead of extract.

```json
{
  "name": "Transform Customer Data",
  "uid": "job-transform-customers",
  "pipeLineRunId": 109135,
  "inputs": [
    {
      "jobUid": "job-validate-customers"
    }
  ],
  "outputs": [],
  "meta": {
    "owner": "analytics-team@company.com",
    "team": "analytics"
  }
}
```



**Result**: Pipeline flow is now:
Extract → Validate → Transform → Load

---

## Step 4: Verify Pipeline Graph

Check that your changes are reflected in the pipeline graph.

### API Call

```bash
GET /torch-pipeline/api/pipelines/15/graph
```



### Response

```json
{
  "graph": {
    "nodes": [
      {
        "id": 101,
        "uid": "job-extract-customers",
        "name": "Extract Customer Data",
        "type": "JOB"
      },
      {
        "id": 104,
        "uid": "job-validate-customers",
        "name": "Validate Customer Data",
        "type": "JOB"
      },
      {
        "id": 102,
        "uid": "job-transform-customers",
        "name": "Transform Customer Data",
        "type": "JOB"
      },
      {
        "id": 103,
        "uid": "job-load-redshift",
        "name": "Load to Redshift",
        "type": "JOB"
      }
    ],
    "edges": [
      {
        "source": "job-extract-customers",
        "target": "job-validate-customers",
        "type": "FLOW"
      },
      {
        "source": "job-validate-customers",
        "target": "job-transform-customers",
        "type": "FLOW"
      },
      {
        "source": "job-transform-customers",
        "target": "job-load-redshift",
        "type": "FLOW"
      }
    ]
  }
}
```



**Verification:**

- New validation job (104) is present
- Flow goes: extract → validate → transform → load
- All connections are correct

---

## Step 5: Verify Configuration Changes

Retrieve the pipeline again to confirm your updates.

### API Call

```bash
GET /torch-pipeline/api/pipelines/customer-etl-daily
```



### Response

```json
{
  "pipeline": {
    "id": 15,
    "uid": "customer-etl-daily",
    "name": "Customer ETL Pipeline",
    "description": "Daily customer data sync from Athena to Redshift - TEMPORARILY DISABLED",
    "enabled": false,
    "scheduled": true,
    "schedulerType": "INTERNAL",
    "schedule": "0 2 * * *",
    "tags": ["production", "daily", "scheduled", "disabled"],
    "createdAt": "2024-08-20T05:15:46.569Z",
    "updatedAt": "2024-12-05T15:30:00Z",
    "meta": {
      "owner": "analytics-team@company.com",
      "team": "analytics",
      "codeLocation": "https://github.com/company/pipelines/customer-etl"
    }
  }
}
```



**Verification:**

- `enabled`: false (as requested)
- `scheduled`: true with cron schedule
- `meta.owner` and `meta.team`: Updated
- `updatedAt`: Timestamp reflects recent change
- `tags`: Includes all new tags

---

## Common Update Patterns

### Pattern 1: Gradual Rollout

1. **Disable production pipeline**

```json
{"enabled": false}
```



2. **Test changes in dev/staging**
3. **Re-enable with new configuration**

```json
{"enabled": true}
```



### Pattern 2: Add Monitoring

1. **Update pipeline with notification channels**

```json
{
  "pipeline": {
    "notificationChannels": "slack-data-team",
    ...
  }
}
```



2. **Set baseline metrics**

```json
{
  "pipeline": {
    "pipelineBaselineMetric": {
      "includeSuccessfulRunsOnly": true,
      "metrics": 10,
      "unit": "RUNS"
    },
    ...
  }
}
```



### Pattern 3: Modify Data Flow

1. **Get current graph structure**

```bash
GET /pipelines/15/graph
```



2. **Add/modify jobs**

```bash
PUT /pipelines/15/jobs
```



3. **Verify new graph**

```bash
GET /pipelines/15/graph
```



---

## Update Workflow Summary

### Simple Configuration Update (2 API calls)

```bash
1. GET /pipelines/:identity
   → Get current config

2. PUT /pipelines
   → Send modified config
```



### Complex Structure Update (4 API calls)

```bash
1. GET /pipelines/:identity
   → Get current config

2. GET /pipelines/:pipelineId/graph
   → View current structure

3. PUT /pipelines/:pipelineId/jobs
   → Add/modify jobs

4. GET /pipelines/:pipelineId/graph
   → Verify changes
```



---

## Complete API Call Sequence

1. `GET /torch-pipeline/api/pipelines/:identity` - Get current configuration
2. `PUT /torch-pipeline/api/pipelines` - Update pipeline
3. `PUT /torch-pipeline/api/pipelines/:pipelineId/jobs` - Modify jobs (optional)
4. `GET /torch-pipeline/api/pipelines/:pipelineId/graph` - Verify structure (optional)

---

## Important Notes

### Update vs Create

The `PUT /pipelines` endpoint does **both** create and update:

- If `uid` exists → Update
- If `uid` doesn't exist → Create

### Immutable Fields

These fields cannot be changed after creation:

- `id` (system-assigned)
- `uid` (unique identifier)
- `createdAt` (creation timestamp)

### Versioning

Pipeline updates don't create versions automatically. If you need versioning:

- Use different `uid` values (e.g., `customer-etl-v2`)
- Store version info in `meta` object
- Track changes in your version control system

---

## Troubleshooting

| Issue | Solution | 
| ---- | ---- | 
| Update not applied | Verify `uid` matches exactly | 
| Graph not updating | Job changes require new run to take effect | 
| Schedule not working | Check `scheduled: true` and valid cron expression | 
| Changes lost | Ensure you're sending complete pipeline object | 


---