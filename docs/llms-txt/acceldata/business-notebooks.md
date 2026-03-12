# Source: https://docs.acceldata.io/documentation/business-notebooks.md

# Business Notebooks

## What are Business Notebooks?

**Business Notebooks** let you organize, run, and schedule sets of queries for automated monitoring and reporting. Unlike ad-hoc conversations, notebooks provide a structured, repeatable way to execute predefined queries on a schedule and share results with your team.

Think of a notebook as a curated list of questions you want answered regularly—e.g., data quality checks, pipeline health, or daily/weekly business reports.

## Why use Notebooks?

Notebooks support four core needs:

- **Scheduled monitoring:** Run checks automatically and notify stakeholders when issues occur.
- **Standardized reporting:** Ensure consistent, comparable results every run.
- **Knowledge preservation:** Capture critical queries so teams can reuse them.
- **Team collaboration:** Share notebooks to align monitoring across roles.

## Notebook vs. Conversation

| Aspect | Conversation | Business Notebook | 
| ---- | ---- | ---- | 
| **Purpose** | Interactive, ad-hoc exploration | Scheduled execution of predefined queries | 
| **Content** | Contextual dialogue | Fixed, self-contained queries | 
| **Execution** | On demand | Automated on a schedule (or manual) | 
| **Query context** | Can reference prior turns | Each query must be self-contained | 
| **Output** | Natural-language responses | Structured results and summaries | 
| **Sharing** | View/continue a thread | View, execute, schedule, and notify | 
| **Use case** | Discovery, troubleshooting, learning | Monitoring, reporting, alerting | 


## Creating Your First Notebook

1. Open **Business Notebooks**.
2. Use tabs to browse **All**, **Starred**, and **Shared** notebooks.
3. Click **+ New Notebook** (top-right).
4. Enter a descriptive name (e.g., _Daily Data Quality Check_ or _Weekly Pipeline Summary_).
5. Save.

## Adding Queries to Your Notebook

Notebook queries are added **from conversations** so you can verify results first.

**To add a query:**

1. Ask your question in a conversation.
2. Review the response.
3. Click **Add to Notebook** in the conversation.
4. Choose the target notebook.

**Guidelines for notebook queries (must be self-contained):**

**Good**

- “Show all data quality policies that failed in the last 24 hours.”
- “List tables in the `CUSTOMER` database not updated in the past week.”
- “What is the freshness status of all critical assets?”
- “Show pipeline runs that exceeded their SLA today.”

**Poor**

- “What about the other policies?”
- “Show me those tables.”
- “And yesterday’s results?”

Good queries state the scope and timeframe explicitly; poor queries rely on prior context.

## Understanding Query Limits

Currently, you can add up to 15 queries to a single notebook. While the interface may show the total count, you can scroll within the notebook to view all queries. This limit ensures notebooks remain focused and execute efficiently.

If you need to monitor more than 15 aspects of your data, consider creating multiple notebooks organized by theme or purpose. For example, you might have one notebook for data quality monitoring, another for pipeline performance, and a third for asset freshness.

## Running Your Notebook

- **Run now:** Click the **Play (  )** button to execute immediately.
- **Test schedule:** Use only if the notebook has queries.
- **Run history:** Click **Show Runs** to see timestamps, status, and details.

**Execution behavior**

- Queries run **sequentially** in the order listed.
- A failed query does **not** stop subsequent queries.
- Results are collected in the run details and sent to the notification group (if configured).

## Scheduling Automated Runs

1. Click the **Schedule** icon for the notebook.
2. Choose **Daily**, **Weekly**, or **Custom**.
3. Set **time** and **timezone** (searchable).
4. Select a **notification group**.
5. Save.

**Notes**

- Do not enable scheduling for empty notebooks.
- You can edit or disable schedules at any time.
- Scheduled runs appear in history with a _Scheduled_ indicator.

## Notification Groups

When you schedule a notebook, you'll need to specify a notification group. Notification groups are collections of users who should receive the results when the notebook runs. This ensures that the right people are informed about important data quality issues or monitoring results.

Setting up effective notification groups helps ensure accountability and quick response to issues. Consider creating different notification groups for different types of notebooks:

- **Data Quality Team**: For notebooks monitoring data quality policies
- **Pipeline Engineers**: For notebooks tracking pipeline performance
- **Business Analysts**: For notebooks generating business reports

**Incident Response**: For notebooks detecting critical issues requiring immediate attention

## Managing your notebooks

- **Star** important notebooks for quick access.
- **Share** notebooks with teammates (requires permissions).
- **Open** a notebook to view:
    - The query list
    - Query count (e.g., _3 Questions_)
    - Run count (e.g., _Runs: 19_)
    - Run history and statuses
    - Notebooks are shown in **reverse chronological** order by default.

## Best Practices for Notebook Design

Creating effective notebooks requires thoughtful planning. Here are some proven strategies:

**Keep Notebooks Focused**: Rather than creating one massive notebook with dozens of queries, create multiple focused notebooks. For example, instead of "Daily Monitoring," create separate notebooks like "Daily Data Quality Check," "Daily Pipeline Health," and "Daily Asset Freshness."

**Use Descriptive Names**: Your notebook names should clearly indicate their purpose and frequency. Good examples include:

- "Hourly Critical Alerts"
- "Daily Customer Data Quality Report"
- "Weekly Data Warehouse Health Check"
- "Monthly Asset Inventory"

**Order Queries Strategically**: Arrange queries from most to least critical. Since notebooks execute sequentially, putting high-priority checks first ensures you get the most important information even if later queries have issues.

**Test Before Scheduling**: Always run your notebook manually several times before setting up automated scheduling. This helps you verify that:

- All queries return the expected results
- Execution completes in a reasonable time
- The information provided is actually useful
- No queries depend on contextual information

**Review and Maintain**: Notebooks aren't "set it and forget it" tools. Regularly review your notebooks to:

- Remove queries that are no longer relevant
- Update queries when data structures change
- Adjust schedules based on actual needs
- Archive notebooks that are no longer used

## Understanding Run History

Run history shows:

- **Date and time**
- **Status** (success/failure)
- **Duration**
- **Trigger** (manual, scheduled, event)

Click **View Details** to inspect per-query results for a run.
History is retained for **90 days**; export important outputs if you need a longer record.

## Troubleshooting Common Issues

- **Empty notebook warning:** Add queries from conversations first.
- **Sharing permissions:** If users aren’t visible, you may need `view:user`. Contact your admin.
- **Duplicate queries:** The system allows duplicates; avoid redundant entries.
- **Schedule not running:**
    - Ensure the notebook has queries
    - Confirm timezone and schedule are correct
    - Verify a notification group is set
    - Confirm the schedule is enabled

- **Query fails in notebook but not in conversation:**
    - Remove reliance on conversation context
    - Specify time ranges and parameters explicitly
    - Check data source access for scheduled runs

## Advanced Use Cases

**Incident Management Workflows**: Notebooks can be used to define standardized steps for incident resolution. When a data quality issue is detected, a notebook can guide the response process with predefined queries that help diagnose and document the issue.

**SLA Monitoring**: Create notebooks that track whether your data pipelines meet their service level agreements. By scheduling these notebooks to run after expected completion times, you can automatically detect and alert on SLA violations.

**Compliance Reporting**: Use notebooks to generate regular compliance reports. By running the same queries on a schedule, you create consistent documentation that can be used for audit purposes.

**Data Drift Detection**: Set up notebooks to run regular comparisons between production and reference datasets, automatically flagging unexpected changes in data distributions or patterns.

## Notebook Permissions and Access Control

- **Create** notebooks: requires role permission.
- **View** notebooks: creators and shared recipients.
- **Execute** notebooks: requires access to relevant data sources.
- **Schedule** notebooks: requires additional permission.
- **Share** notebooks: requires sharing permission; admins may need to grant it.

Contact your administrator if you encounter permission errors.

## Integration with Other ADM Features

- **Knowledge Bases:** Queries can reference organization documents for context.
- **Conversations:** Every notebook query originates from a validated conversation.
- **Dashboards:** Visualize notebook results over time.
- **Agents:** Notebooks use the same agent framework as conversations for consistency.