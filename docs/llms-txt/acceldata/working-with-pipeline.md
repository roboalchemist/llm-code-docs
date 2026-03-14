# Source: https://docs.acceldata.io/documentation/working-with-pipeline.md

# Working with Pipelines

Pipelines in ADOC can be created and managed in different ways depending on your workflow. You don’t always have to create them manually — pipelines may also be registered automatically when your instrumented jobs report metadata. 

## Create a Pipeline

There are two main ways pipelines appear in ADOC:

### Manual Creation (UI or SDK)

You can explicitly create a pipeline when you want to model a workflow before instrumenting jobs.

**When to use this approach:**

- You want a pipeline in place before jobs start reporting runs.
- You want to assign ownership, teams, or tags up front.
- You want to design the logical structure of jobs and assets.

**Steps (UI):**

1. Navigate to **Pipelines &gt; Add Pipeline**.
2. Enter pipeline details:
    1. **Name**: User friendly and unique name for the pipeline
    2. **UID:** A permanent, unique pipeline ID. ID cannot be changed later.
    3. **Description** (Optional): A brief explanation of the pipeline's purpose.
    4. **Owner** (Optional): Name of pipeline owner or service account.
    5. **Team** (Optional): The name of the team that owns the pipeline.
    6. **Code Location** (Optional): A pipeline source code repository or definition file URL.
    7. **Context** (Optional): A key-value field for custom metadata or annotations.
    8. **Tags** (Optional): Classify and filter pipelines with descriptive tags. Add more tags by pressing the **Enter** key. 

3. Click **Save**.

**Steps (SDK)**

You can also call the [Create Pipeline API](https://api.acceldata.io/#33a61d84-47bb-4bee-b02c-1b8915dc087f) or use the [SDK](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/sdk) to programmatically define a pipeline with metadata.

The ADOC UI monitors pipelines, whereas the Acceldata SDK registers new ones. Add your pipeline using these steps.

1. **Environment Configuration:** First prepare your development environment with the required components.
    1. **Install the SDK**: Install `acceldata-sdk` for Python or `adoc-java-sdk` for Java using pip.
    2. **Generate API Keys**: Your `accessKey` and `secretKey` can be generated from **Admin &gt; API Keys** in the ADOC UI. These are needed for request authentication.
    3. **Start the Client**: Create an SDK client using your ADOC URL and API keys.

2. **Define the Pipeline Object:** Next, specify the pipeline object's core attributes.
    1. **Instantiate Object**: Create a Python `CreatePipeline` object or use `CreatePipeline.builder()` in Java.
    2. **Required fields**: Provide a pipeline uid and name.
    3. **Optional fields**: Use context to provide a description, owner information (meta), and other annotations.

3. **Register the Pipeline: Send the object to the ADOC server :** Call the `create_pipeline()`method on your initialized client, passing in the pipeline object. This action registers the new pipeline in ADOC.
4. **Run Pipeline:** Finally, run the pipeline to collect observability data.

Apply `create_pipeline_run()` to the previous response object.

This starts the first run instance, letting ADOC track executions, performance data, and alerts. 

You can now view the created pipeline in the ADOC pipeline list.

### Automatic Creation (SDK Instrumentation)

If you instrument your jobs with the ADOC SDK or supported connectors, pipelines can be created automatically the first time metadata is reported.

- Jobs report a `pipeline_uid` when runs are sent to ADOC.
- If no pipeline with that UID exists, ADOC automatically registers a new pipeline.
- If the pipeline already exists (either manually created or auto-created earlier), the job’s runs are grouped under that pipeline.

**Example:**

You instrument an Airflow DAG (Directed Acyclic Graph)  called `orders_etl` and configure it with `pipeline_uid="orders_pipeline"`.

When the DAG runs and reports to ADOC, the system will either:

- Create a new pipeline called `orders_pipeline` (if it doesn’t exist yet), or
- Attach the run to the existing `orders_pipeline`. 

---

## Run a Pipeline

Each execution of a pipeline is called a pipeline run. Runs can be:

- **Triggered manually** via UI or SDK
- **Triggered automatically** when instrumented jobs execute and report data to ADOC:

**Runs Capture:**

- **Job Status:** Step-by-step success/failure
- **Spans & Events:** Detailed timing and logs
- **Asset Nodes:** Input/output data health
- **Policy Compliance:** Checks for quality, schema drift, reconciliation, etc.

For example, you can identify which job failed during an ETL process and why, so corrective action can be taken quickly.

---

## Edit a Pipeline

To edit a pipeline:

1. For the selected pipeline, click the **ellipsis icon ⋮** .
2. Select the  **pen icon**.
3. Make the changes. Click **Save**.

---

## Delete a Pipeline

To delete a pipeline:

1. For the selected pipeline, click the  **ellipsis icon**.
2. Select the  **bin icon.**
3. Click **Confirm.**