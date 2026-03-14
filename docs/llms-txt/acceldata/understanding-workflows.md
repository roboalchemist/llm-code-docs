# Source: https://docs.acceldata.io/documentation/understanding-workflows.md

# Understanding Workflows

## What Are Workflows?

**Workflows** in ADM are pre-built, multi-step intelligent processes that help you perform complex data management tasks through an interactive, guided experience. Instead of manually configuring each step, workflows combine **AI-powered automation** with **human validation** to streamline tasks such as policy creation, asset classification, and data quality remediation.

### Key Characteristics

Workflows represent a shift from one-time queries to orchestrated, multi-stage operations that deliver end-to-end outcomes.

| **Feature** | **Description** | 
| ---- | ---- | 
| **Template-Based** | Begin from pre-configured templates built for specific use cases. | 
| **Interactive Execution** | Combine automated processing with user checkpoints and approvals. | 
| **AI-Assisted** | Intelligent agents analyze context and make data-driven recommendations. | 
| **Guided Experience** | Clear, step-by-step progression with visible status indicators. | 
| **Configurable** | Customize workflow behavior using prompts, parameters, and optional scheduling. | 


### Workflow vs. Simple Query

| **Aspect** | **Simple Query** | **Workflow** | 
| ---- | ---- | ---- | 
| **Complexity** | Single-step request | Multi-step coordinated process | 
| **User Interaction** | One-time | Interactive with validation points | 
| **Duration** | Seconds | Minutes to hours | 
| **Validation** | Automatic | User-reviewed at key stages | 
| **Output** | Response or insight | Configuration, policy, or applied action | 
| **Resumability** | Not applicable | Can be paused and resumed | 


## Accessing Workflows

### Workflow Library

To access workflows:

1. Navigate to **Workflows** in ADM.
2. The **Workflow Library** opens, displaying all available templates.

The library provides:

- **Browse Templates** – View available workflow templates with descriptions.
- **Search Functionality** – Find workflows by name or use case.
- **Template Details** – Each template displays:
    - Workflow name and icon
    - Short description
    - Number of steps
    - Category or tag
    - **Use This Template** button

### Available Workflow Templates

| **Template Name** | **Description** | 
| ---- | ---- | 
| **Intelligent Asset Classification and Compliance Workflow** | Classifies data assets across taxonomies with confidence scoring and generates detailed reports. | 
| **Business Context Generation Workflow** | Analyzes metadata to produce business context and documentation for assets. | 
| **Data Quality Remediation Workflow** | Identifies data quality issues, determines root causes, and applies automated fixes. | 
| **Policy Creation Workflow** | Analyzes policy requirements and automatically generates data quality policies. | 
| **Policy Description Workflow** | Summarizes and documents existing policies for reporting or audit readiness. | 


## Creating and Executing a Workflow

### Starting a Workflow

1. In the **Workflow Library**, click **Use This Template**.
2. The **Create New Workflow** dialog appears.
3. Provide the following details:
    - **Workflow Name** – Enter a descriptive name for the instance.
    - **Description (optional)** – Add context or purpose.
    - **Enable Scheduler** – Toggle ON to schedule automatic runs.

4. Click **Save Workflow**.

Your new workflow opens in the **Execution View**.

### Workflow Step Types

| **Step Type** | **Purpose** | 
| ---- | ---- | 
| **User Request** | Capture user instructions or parameters. | 
| **Intent Validation** | Confirm requirements and identify required resources. | 
| **Processing** | Execute automated or AI-driven analysis. | 
| **Generation** | Produce configurations, reports, or artifacts. | 
| **Review and Save** | Present results for approval before saving or applying. | 


## Managing Workflow Runs

### Workflow Dashboard

The **Workflows** page serves as the central management dashboard.

| **Column** | **Description** | 
| ---- | ---- | 
| **Instance Name** | Custom name for the workflow (clickable for details). | 
| **Last Run** | Timestamp of the most recent execution. | 
| **Last Run Status** | Indicates _Success_, _Failed_, or _In Progress_. | 
| **Last Updated** | Date of the last modification. | 
| **Created** | Original creation timestamp. | 
| **Actions** | Edit or delete workflow. | 


**Dashboard Features**

- **Search Bar** – Find workflows by name.
- **Refresh Button** – Reloads latest run statuses.
- **Browse Templates** – Opens the Workflow Library.
- **Pagination and Row Settings** – Adjust view preferences.

### Viewing Execution Details

Click any workflow name to view:

- **Execution Timeline** – Visual flow of completed steps.
- **Step Details** – Inputs, logs, outputs, and execution time.
- **Error Messages** – Visible for failed steps.
- **Run History** – Records of all previous executions.

### Workflow States

| **State** | **Symbol** | **Description** | 
| ---- | ---- | ---- | 
| **Not Started** |  | - Step hasn't begun execution\n- Prerequisites not yet met\n- Waiting for previous step to complete | 
| **Running** |  | - Step is actively executing\n- AI agents processing data\n- Background operations in progress\n- May take several seconds to minutes depending on complexity | 
| **Waiting for Input** |  | - Step requires user review or decision\n- Validation checkpoint reached\n- User must provide input to continue | 
| **Completed** |  | - Step finished successfully\n- Output generated and available\n- Ready to proceed to next step | 
| **Failed** | **X** | - Step encountered an error\n- Execution stopped\n- Requires user intervention\n- May offer retry or skip options | 


## Working with Workflow Results

### Reviewing Outputs

Outputs vary by workflow type and may include:

- Generated **data quality policies**
- Detailed **classification reports**
- Automated **remediation plans**
- Enriched **business context** and metadata

### Saving and Applying Results

1. **Review** outputs after execution.
2. **Modify** configurations if needed.
3. **Validate** correctness.
4. Click **Save** to persist results.
5. Verify that changes were applied successfully in ADM.

## Best Practices

| **Stage** | **Recommendations** | 
| ---- | ---- | 
| **Before Starting** | Define objectives, identify data assets, confirm permissions, estimate duration. | 
| **During Execution** | Monitor progress, review checkpoints, provide clear input, and avoid navigation during critical steps. | 
| **After Completion** | Verify results, document changes, save reusable workflows, review logs for any issues. | 


### Troubleshooting Failed Workflows

1. **Check Error Message** – Identify the failing step.
2. **Verify Prerequisites** – Ensure data sources and permissions are valid.
3. **Retry Step** – Many failures are transient.
4. **Adjust Input** – Refine parameters if validation fails.
5. **Contact Support** – Provide workflow name, step logs, and context for assistance.

## Workflow Scheduler

The **Scheduler** enables automated execution of workflows at predefined intervals.

| **Action** | Description | 
| ---- | ---- | 
| **Enable During Creation** | Toggle **Enable Scheduler** when setting up a workflow. | 
| **Automatic Runs** | Executes on schedule without manual input. | 
| **Notebook Integration** | Can trigger scheduled notebook runs automatically. | 
| **Disable Option** | Turn off to stop automatic execution. | 


> Note Scheduler is disabled by default. A message appears: _“Scheduler is disabled. This notebook will not run automatically.”_

## Workflow Templates by Use Case

| **Template Type** | **Purpose** | 
| ---- | ---- | 
| **Asset Classification** | Validates and classifies assets with confidence scoring and report generation. | 
| **Policy Creation** | Analyzes requirements, selects assets, and creates rules for data quality policies. | 
| **Data Quality** | Detects quality issues, analyzes error patterns, and suggests automated remediation. | 
| **Business Context** | Collects metadata, execution history, and samples to generate descriptive documentation. | 


## Workflow Execution Tips

### Prompt Customization

- Be specific and concise when defining objectives.
- Reference relevant datasets or rules.
- Indicate constraints, preferences, or success conditions.
- Use natural language — ADM understands context intuitively.

### Managing Long-Running Workflows

- Workflows with multiple steps may take several minutes.
- You can navigate away and return later; ADM preserves progress.
- Real-time status indicators show running or failed steps.

### Workflow Versioning

- Each execution is stored as a unique run.
- Compare outputs across versions to refine performance.
- Use successful runs as templates for future automation.