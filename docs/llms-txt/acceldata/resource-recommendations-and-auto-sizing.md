# Source: https://docs.acceldata.io/documentation/resource-recommendations-and-auto-sizing.md

# Resource Recommendations and Auto-Sizing

The **Resource Recommendation** feature in ADOC helps automatically choose the right amount of memory, CPU cores, and Spark settings for each job. This improves job success rates, reduces cost by avoiding overprovisioning, and eliminates the guesswork involved in configuring compute resources.

This feature is configured at the Data Plane level, meaning each Data Plane can have its own resource settings based on its environment and data load.

## What Are Resource Recommendations?

Instead of manually defining memory and cores for Spark jobs, ADOC suggests the best-fit configuration based on:

- Predefined resource profiles (Small, Medium, Large)
- Real-time job failures (like memory issues)
- Node hardware specs and expected data size (if you provide them)

This improves job reliability, saves cost, and speeds up execution—especially in Kubernetes Spark Engine environments.

## Where to Access Resource Recommendations

To configure and manage Spark job resources for a specific Data Plane, follow these steps:

1. From the left-hand navigation menu, click **Register**.
2. In the Register page, go to the **Data Planes** tab.
3. Locate the Data Plane you want to configure.
4. Click the three-dot menu (**⋮**) next to the Data Plane name.
5. Select **Resource Configuration** from the dropdown menu.

This will open the **Resource Configuration page** where you'll see two tabs:

- Strategies
- Node Details

These settings only apply to jobs running on the selected Data Plane.

## Strategies: Define or Reuse Pre-Configured Resource Levels

The Strategies tab allows you to manage resource configuration templates (aka "T-shirt sizes"). These are saved at the Data Plane level and reused for jobs and policies.

Strategies help make sure jobs across the platform use the right amount of compute and memory. You can use them in:

- Data Quality Policies – Pick a strategy to control how much compute is used for validation rules.
- Profiling Jobs – Use a larger strategy when profiling big datasets.
- Scheduled Crawler Runs – Adjust resources for data sources that need more or less power.
- Custom Pipelines – Choose the right size for multi-step processing jobs.

Using strategies this way helps keep performance smooth and costs under control—without having to set resources manually each time.

### Preloaded Sizes

- **Small**: Light jobs with small datasets
- **Medium (default)**: Balanced setting for most workloads
- **Large**: Memory or compute-heavy jobs

You can also add your own sizes (e.g., X-Large) via the **Add Strategy** button.

**Default Strategy**: A green checkmark shows which size is currently the default. This strategy is used unless a job or policy overrides it.

Actions Menu (⋮)

Each row has a 3-dot menu to:

- **Edit**: Change memory, cores, or executor settings
- **Delete**: Remove the strategy
- **View Details**: Inspect full configuration

All these settings are saved in the Data Plane context.

Each strategy contains:

**Spark Driver Configuration: Configure core resource for the Spark driver pod**

| Setting | Description | Example | 
| ---- | ---- | ---- | 
| Driver Cores | Number of CPU cores Spark uses for scheduling tasks (controls parallelism) | 1, 2, 4 | 
| Driver Memory | JVM heap memory for the driver (include unit, e.g., m, g) | 512m, 2g, 4g | 
| Memory Overhead Factor | Extra memory allocated for non-heap usage (for example, 0.1 = 10%) | 0.1 | 
| Driver CPU Limit | Maximum CPU the driver pod can use at the Kubernetes level (supports whole cores or millicores) | 1000m, 2, 4 | 
| Driver CPU Request | Minimum CPU guaranteed to the driver pod by Kubernetes (supports whole cores or millicores) | 500m, 1, 2 | 


**Spark Executor Configuration**

| Setting | Description | Example | 
| ---- | ---- | ---- | 
| Executor Cores | Number of CPU cores Spark uses per executor (controls parallelism) | 1, 2, 4 | 
| Executor Memory | JVM heap memory per executor | 512m, 1g, 4g | 
| Memory Overhead Factor | Extra memory allocated for non-heap usage | 0.1 | 
| Executor CPU Limit | Maximum CPU allowed per executor pod at the Kubernetes level (supports whole cores or millicores) | 600m, 2, 4 | 
| Executor CPU Request | Minimum CPU guaranteed per executor pod by Kubernetes (supports whole cores or millicores) | 300m, 1, 2 | 


**Scaling Policy**

| Setting | Description | Example | 
| ---- | ---- | ---- | 
| Minimum Executors | Minimum number of executor pods to maintain | 1 | 
| Maximum Executors | Maximum number of executor pods allowed to scale up | 5 | 


## Node Details: Improve Accuracy of Recommendations

The Node Details tab allows you to inform ADOC about the infrastructure behind your Data Plane. This makes recommendations more accurate.

| Field | Explanation | Example | 
| ---- | ---- | ---- | 
| Cores Per Node | Total CPUs per node | 8 | 
| Memory Per Node | RAM per node | 32 GB | 
| Disk Attached Per Node | Disk storage | 100 GB | 
| Disk Spill % | How much data you expect might spill to disk during processing | 30% | 
| No. of Nodes | Number of nodes available for processing | 10 | 
| Min/Max Data Size | Typical uncompressed data size processed by jobs | 5–50 GB | 


After filling this in, click **Save and Recommend**. ADOC will:

- Adjust memory/core recommendations
- Fine-tune retry behavior
- Optimize executor scaling

These settings do not directly affect jobs, but improve the recommendation logic behind the scenes.

### Auto-Retry: Handling Failures Automatically

One of the biggest advantages of ADOC’s Resource Recommendations is that it automatically retries jobs with higher resources if they fail due to memory-related issues.

Two Retry Strategies

1. Inventory-Driven Retry (T-Shirt Sizes)
    1. If a job using "Small" fails due to memory, ADOC retries using "Medium", then "Large"
    2. Based on the order defined in the Strategies tab
    3. Retries up to 3 times

2. Custom-Driven Retry
    1. If using a custom config (not Small/Medium/Large), ADOC doubles the driver and executor memory for each retry (e.g., 4 GB → 8 GB → 16 GB)
    2. Retries also capped at 3 attempts
    3. This system reduces manual tuning and recovers failed jobs automatically.

> While ADOC’s resource recommendations and auto-retry features are powerful, there are a few important limitations to keep in mind:> > - **Only Memory-Related Failures Trigger Auto-Retry**: Auto-retry is only triggered if the job fails due to memory issues (e.g., out-of-memory errors). Failures caused by syntax errors, data corruption, network timeouts, or invalid configurations will not invoke a retry.> - **Not All Engines Fully Support Auto-Sizing**: Resource recommendations and auto-sizing are primarily optimized for the Kubernetes-based Spark Engine. Other execution environments may have limited or no support for auto-sizing or auto-retry logic.> - **Recommendations Depend on Node Details**: If Node Details (cores, memory per node, etc.) are not configured, the quality of recommendations may degrade, especially for large or complex jobs.> - **Custom Strategies Bypass Dynamic Escalation**: Jobs using fixed custom configurations (outside the T-shirt sizes) do not benefit from the tiered fallback to Medium/Large. Instead, they only retry with incremented resource values up to a fixed cap.> - **Retries May Increase Cost**: Although retrying failed jobs improves success rates, each attempt uses more compute. This may lead to higher costs if retries are frequent. Consider this when setting retry limits.

## Viewing What Resources Were Used (Audit Trail)

Each Spark job shows what configuration was applied.

To view, Navigate to the **Job Resource** section in the **Job Details** page.

You’ll see:

- What strategy was used (e.g., "Medium")
- Whether a retry occurred (and how many times)
- Actual memory and core values applied
- If it was a custom vs. inventory-based strategy

This helps you debug slow or failed jobs, understand trends, and optimize future runs.

---

## Best Practices

**1. Use T-Shirt Sizes (Small, Medium, Large) Wisely**

- Start with Medium for most jobs—this is the default for a reason.
- Use Small only for lightweight or exploratory jobs (e.g., previewing small datasets).
- Choose Large when working with known high-volume data or complex pipelines.
- Avoid frequent custom resource tweaking unless you have strong technical understanding.

Let ADOC’s auto-sizing and retry handle resource escalation when possible.

**2. Define Clear Naming for Custom Strategies**

- Use descriptive names like:
- XL – High-Memory Ingestion,
- Small – Metadata Cleanup,
- Custom – ML Training 4vCPU/16GB
- Include core/memory details in the description field so team members understand the resource plan at a glance.

This helps with auditability, team collaboration, and debugging.

**3. Keep the Retry Count to 3 (Default)**

- The default 3 retry attempts (with increasing resource sizes) is a safe and efficient balance.
- Only raise retry attempts if you have frequent intermittent failures and cost is not a concern.

Avoid infinite or excessive retries—they may incur high costs or hold up pipelines.

**4. Always Configure Node Details (Under Tab 2)**

- Fill in Cores/Memory per Node, Disk Size, and Expected Data Size.
- These inputs improve the accuracy of auto-sizing and recommendations.
- This also helps ADOC understand your hardware boundaries, reducing over- or under-sizing.

Even rough estimates help improve performance and reduce job failure.

**5. Review the Job Resource Audit Regularly**

- Go to the Job Resource section after job runs to see:
- What strategy was used
- Whether a retry happened
- If any failures occurred
- Use this data to refine your default strategy and reduce job latency or failure.

Make audits part of your job monitoring checklist—especially in production Data Planes.

**6. Scope Strategies Per Data Plane**

- Each Data Plane (dev, staging, prod) may have different compute capacity.
- Configure different strategies depending on:
- Expected data size
- Cluster size (nodes, memory)
- SLA expectations

Don’t assume that what works in staging will work in production—customize per environment.

**7. Avoid Over-Provisioning “Just in Case”**

- Don’t default everything to Large or X-Large—this wastes resources and money.
- Trust the auto-retry mechanism to scale up only when needed.
- Optimize for the most likely success case, not the worst case.

Resource efficiency leads to cost savings—especially in multi-job pipelines.

**8. Test Custom Strategies in Lower Environments First**

- When creating new custom configurations (e.g., for ML workloads), validate them in dev/staging.
- Once tested, replicate successful configs into the production Data Plane.

Minimize risk of failures or resource wastage in production.

**9. Clean Up Unused Strategies**

- Periodically review the list of strategies under the Strategies tab.
- Remove outdated or duplicate entries to keep the configuration clean and easy to manage.

A clutter-free strategy list reduces confusion and speeds up job setup.

**10. Collaborate with Data Engineers on Strategy Design**

- Involve data engineers or platform owners when defining baseline resource strategies.
- Ensure that business users understand what the resource levels mean.
- Set documentation or internal notes for default sizing guidelines.

Cross-functional clarity ensures better system performance and lower support overhead.