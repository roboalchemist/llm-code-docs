# Source: https://docs.acceldata.io/api/persistence-paths.md

# Persistence Paths

When a Data Reliability policy runs (Data Quality, Reconciliation, Drift, Freshness, Anomaly, etc.), ADOC writes detailed execution results and roll-up summaries to storage. **Policy persistence paths** let you control _where_ those results land (for GOOD/BAD records, samples, and derived outputs) so you can plug them into downstream platforms, archives, or analytics.

Use these APIs when you want to:

- Route policy outputs to a specific storage prefix (for example, a cloud bucket folder per domain or per policy type). 
- Turn result persistence on/off for GOOD/BAD rows or sample-only outputs without editing the policy definition itself. 
- Manage persistence centrally by **policy ID** or **policy name**, depending on how your team references policies.

Starting in **ADOC v26.3.0**, persistence paths are managed using a **template-based configuration model**. This allows organizations to define flexible storage structures using predefined variables such as policy name, execution time, datasource name, and execution identifiers.

Persistence configurations can be defined at two levels:

- **Tenant level**: reusable persistence configurations that can be assigned to multiple policies.
- **Policy level**: a policy can either use the tenant default configuration, reference a saved configuration, or define a custom configuration

The APIs in this section allow users to:

- Retrieve and update persistence configuration for a policy
- Manage tenant-level persistence configurations
- Validate and preview persistence path templates
- Determine whether the data plane supports templated persistence paths

Supported storage formats:

- **PARQUET**
- **CSV**
- **JSON**
- **ORC**