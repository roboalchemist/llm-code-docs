# Source: https://docs.acceldata.io/documentation/control-pipeline.md

# Control Pipeline

Pipeline control in **Acceldata Data Observability Cloud (ADOC)** gives you the ability to actively manage pipeline runs — not just observe them. These controls let you react quickly when data issues, system maintenance, or failures occur, ensuring that your pipelines remain reliable and efficient.

This page explains how to:

- [Configure a comparison baseline](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/control-pipeline#configure-a-comparison-baseline)
- [Configure monitoring policies](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/control-pipeline#configure-a-monitoring-policy)
- [Automate data reliability](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/control-pipeline#automate-data-reliability)

---

## Configure a Comparison Baseline

Baselines help you evaluate **new runs against past performance**. ADOC compares new runs to a baseline, detecting significant changes like increased execution time.

To configure the baseline:

1. **Set the number of runs:** In the **Compared to average of last** field, enter the number of recent runs to include in the baseline calculation (e.g., 10, 50, or 100).
2. **Filter by run status:** To prevent failed or cancelled runs from skewing the average performance time, select the **Only include successful runs** checkbox.
This is the recommended setting for a stable performance baseline.

> The baseline you configure here directly affects how pipeline level aggregate metrics are displayed in ADOC.> > For example, on dashboards, the percentage change shown next to the average run time will now be calculated by comparing the most recent results to the baseline you set.

---

## Configure a Monitoring Policy

Monitoring policies enforce **pipeline SLAs** and trigger alerts when performance or reliability benchmarks are breached.

The main view displays all existing policies and provides two primary areas of configuration:

### Pipeline Execution Failure Settings

This is a global alert that triggers if the pipeline fails for any reason not covered by a more specific rule.

1. Click **Edit** to expand the section and configure the following:
    - **Alert Name**:  A system-generated name for this default failure alert. 
    - **Severity**: Set the severity level (e.g., Medium, High) for the alert. 
    - **Notification Channels**: Choose where to send the alert when the pipeline fails.

2. Click **Save** to apply the changes.

### Monitoring Policies List

This is a detailed list of all your custom monitoring policies, grouped by the entity type they apply to **Pipeline**, **Job**, **Span**, and **Event**.
You can expand each entity to see the specific rules, their severity, and their conditions.

#### Create a New Monitoring Policy

To create a new set of custom rules, click the **Add Monitoring Policy** button. 

This will open the **Define metrics** screen. 

Add multiple rules to a policy with **Add Another Metric**. Toggle each rule on/off using the **Enabled** switch.

1. Choose monitoring level: **Pipeline**, **Job**, **Span**, or **Event**. Selected entity defines metrics.
2. Define monitoring rules: Create one or more rules per metric type.

Note Configuration fields are dynamic. It changes with the Metric _Type_ and _Comparison_ method.    Examples cover common scenarios.

Configure fields:

**A. Configure the Comparison Method**

When setting up a rule for a time-based or numerical metric, you will need to choose a comparison method. The options that follow will change based on your choice:

- **User Threshold:** 
    - Triggers an alert based on a **fixed value** you define.
    - You will then set a **Threshold** like _Greater Than_ _`00:10:00`_.

- **Previous Executions:** 
    - Triggers an alert by comparing the current run to a **historical baseline**. When you select this, you must also configure:
        - The **baseline period** (e.g., average of the last _`10`_ successful runs).
        - The **Threshold** for deviation (e.g., _`Increased By` `20%`_).

**B. Understand Rule Structure by Example**

The specific fields for a rule are tailored to the metric you choose. Here are two common examples to illustrate the differences:

**Example 1: Creating a Time-Based Rule (for Pipeline Duration)**

When you select a metric like _Pipeline Duration_, you will configure these five steps:

1. **Select Metric:** `Pipeline Duration`
2. **Configure Comparison:** Choose `User Threshold` or `Previous Executions`.
3. **Configure Threshold:** Define the condition (e.g., `Greater Than` `00:10:00`).
4. **Set Alert Severity:** `Critical`, `High`, etc.
5. **Select Notification Channel:** Choose where to send the alert.

**Example 2: Creating an Event Metadata Rule**

When you select the `Event` metric type and want to monitor its data, the rule structure changes completely:

1. **Monitor in context of span:** (Optional) Associate the event with a specific code segment (span).
2. **Select Metadata Key:** Choose the specific key from the event's data that you want to check.
3. **Alert when key's value:** Define the logic for the alert (e.g., `Equals`, `Not` `Equals`, `In`) and provide the value(s) to check against.
4. **Set Alert Severity:** `Critical`, `High`, etc.
5. **Select Notification Channel:** Choose where to send the alert.
6. **Save** the Policy.

#### Managing Existing Policies

To edit or delete an existing rule:

1. Navigate to the Monitoring Policies List
2. Expand the relevant entity, and click the **ellipsis icon ⋮**
3. Edit or delete the rule.

---

## Automate Data Reliability

Automate data quality checks, profiling, or reconciliation policies triggered by pipeline, job, or span outcomes.
Automating data reliability tasks ensures they run at crucial moments in your data lifecycle.

The main view displays all existing automations and their status, including type, targeted data asset, and triggering pipeline event.

#### Creating a New Automation

To begin, click the **Add Automation** button.

This opens the **Setup Data Reliability Automation** form.

The form is divided into two main parts: 

- defining **when** the automation runs (the trigger) and 
- what it does (the action).

**1. Configure the Trigger**

In the **Execute automation on completion of** section, define the event that will start your automation:

- **Select the trigger entity:** Choose `Pipeline`, `Job`, or `Span`.
- **Select the trigger status:** Choose the outcome that triggers the automation, such as `Success`, `Aborted`, or `Failed`.
- **Select the specific instance:** From the dropdown that appears, choose the specific pipeline, job, or span name to monitor.

**2. Define the Action**

Next, specify what data reliability task the automation will perform:

- **Automation Type:** Select the type of task to perform:
    - **Profiling:** Runs a data profiling job on the selected asset to generate statistics and metadata.
    - **Data Quality:** Executes a set of predefined data quality rules against the asset.
    - **Reconciliation:** Performs a reconciliation check, typically comparing two datasets to ensure consistency.

- **Select an asset:** Search for and select the data asset (e.g., a database table) that the automation will run on.
- **Execution Type:** Choose how the task runs.
    - `Full` processes the entire dataset,
while `Incremental` typically processes only new or changed data since the last run.

**3. Save the Automation**

Click **Save** to create and activate the automation. It will now appear in the automations list on the main dashboard.

#### Managing Existing Automations

To edit or delete an existing automation:

1. Navigate to the **Automated Data Reliability** list.
2. Use the  **Edit** and  **Delete** icons on the right of each row.