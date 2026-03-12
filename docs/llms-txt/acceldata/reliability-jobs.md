# Source: https://docs.acceldata.io/documentation/reliability-jobs.md

# Monitoring and Managing Jobs

Reliable data doesn’t just happen—it is the result of continuous checks and processes running behind the scenes. **Data Reliability Jobs** page in Acceldata Data Observability Cloud (ADOC) gives you visibility into those processes. They help you track whether data profiling, quality checks, reconciliation, and other reliability tasks are running successfully and delivering the results you expect.

Monitoring jobs ensures you can:

- **Stay informed** about whether data checks have run and completed on time.
- **Take action quickly** by rerunning failed or incomplete tasks.
- **Validate governance rules** and data health across critical assets.
- **Plan ahead** by checking what jobs are scheduled next.

Jobs provide the operational backbone for your reliability program. Jobs tell you **what is happening right now** and whether your policies are working as expected.

## What you can do with jobs

With Data Reliability Jobs, you can:

- **Monitor** the status of profiling, quality, reconciliation, and discovery tasks.
- **Manage** outcomes by rerunning failed or incomplete jobs without reconfiguration.
- **Validate** governance and reference rules to ensure consistency.
- **Track schedules** for upcoming jobs to avoid surprises.
- **Drill into details** when you need execution logs, error insights, or performance metrics.

This helps both technical teams and business stakeholders stay aligned—knowing not only the current state of data health, but also how reliability is actively maintained.

## Types of jobs

| Job Type | Description | What You Can Do | 
| ---- | ---- | ---- | 
| **Profile Jobs** | Capture profiling runs to understand the shape and readiness of data assets. | - Track profiling status (queued, in progress, succeeded, failed) - Use mini-profiling for quick, in-database checks | 
| **Data Quality Jobs** | Validate whether quality policies are applied and meeting expectations. | - Check pass, warning, fail, or error results - Rerun errored or aborted jobs - View detailed execution logs | 
| **Reconciliation Jobs** | Ensure consistency between source and target datasets. | - Confirm reconciliation results - Rerun failed checks - Review policy-level details | 
| **Upcoming Jobs** | Anticipate upcoming workload by reviewing scheduled tasks. | - Review upcoming executions - Refresh to update schedules - Adjust views to see more jobs | 
| **Policy Import Jobs** | Track the outcome of importing new or updated policies. | - See counts of created or updated policies - Review execution duration - Confirm completion status | 
| **Reference Validation Jobs** | Verify that lookup rules and reference datasets are valid. | - Check validation results - Identify and resolve errors | 
| **Rule Set Jobs** | Monitor how rule sets are applied across assets. | - Review job status, execution mode, and timestamps - Confirm assets scanned and policies updated | 
| **Cadence Jobs** | Detect anomalies in schedules and monitor data freshness. | - Track hourly executions for freshness - Review results, including partial or completed analyses | 
| **Crawler Jobs** | Discover and catalog metadata from connected data sources. | - Monitor crawler runs by type, duration, and outcome - Review discovered entities (tables, views, columns, databases) - Expand results for coverage details | 


## Best practices

- Rerun failed jobs promptly to maintain trust in data health.
- Use upcoming jobs to anticipate workloads and plan monitoring windows.
- Review logs to diagnose recurring issues.

## Next steps

With Data Reliability Jobs, you can:

- Monitor ongoing reliability processes.
- Manage and rerun tasks that affect data quality.
- Validate rule sets, policies, and reconciliations.
- Track discovery and profiling to ensure data coverage.