# Source: https://docs.acceldata.io/documentation/sdk.md

# SDK

## Introduction to Pipelines

Pipelines introduce data-aware performance, reliability, and timeliness observability to the multi-platform pipelines built on orchestration tools and data platforms of the modern data stack.

Before beginning pipeline instrumentation and monitoring, it is critical to understand the following components:

## Pipeline

The pipeline is the base entity in Acceldata Pipelines. Data pipeline executions, metadata, and metrics are encapsulated here for exploration and monitoring.

## Pipeline Run

Acceldata Pipelines keeps track of a pipeline's versioning, metadata, and metrics with each execution, or Pipeline Run. You can monitor, compare, and alert on performance changes across Pipeline Runs.

The entities of a Pipeline Run include:

| Entity | Description | 
| ---- | ---- | 
| **Job Nodes** | Job Nodes represent the execution steps in a data pipeline, such as reading or writing data to databases or executing validation on data assets to understand their overall data quality.\n\n\n\nTo build overall pipeline data lineage, Job Nodes can be linked to both input and output Asset Nodes. | 
| **Asset Nodes** | In a data pipeline, Asset Nodes represent the data that is consumed or produced by Job Nodes.\n\n\n\nWhen correlated to the catalog of data assets in Acceldata Data Reliability, you can use Data Reliability policies to observe and enforce the overall quality and reliability of data produced by the pipeline. | 
| **Spans** | Spans are used to provide more granular details about a job. You can create child spans to break down a job into multiple child spans and then track them individually if it involves multiple steps. You can also attach processors at a span to raise events. | 
| **Events** | You can raise events that contain information about the task being executed. A span is associated with an event. Multiple key-value pairs are used to raise events. You must first select a span to view the events associated with it. You can view all of the events associated with a pipeline run by selecting the root span. | 


A pipeline can be added using the UI or using SDK. The populating of a pipeline with details of jobs and related assets can only be done using SDK. For more information on how to create pipelines through the UI, see [Working with Pipelines](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/working-with-pipeline).