# Source: https://docs.zenml.io/concepts/steps_and_pipelines/execution.md

# Execution

This page explains what happens under the hood when ZenML executes steps in static and dynamic pipelines. Regardless of where or how a step executes (inline or in an isolated environment, synchronous or concurrent), ZenML applies the same core semantics: inputs are loaded via materializers, outputs are materialized as versioned artifacts, lineage/metadata and logs are recorded, caching policies are respected, and step/run status is published consistently.

## Static pipelines

In static pipelines, ZenML executes the pipeline function before running the pipeline to compile a DAG of steps, which the orchestrator then schedules according to their upstream dependencies. This pre-compilation allows ZenML to optimize execution order and validate the DAG structure before any steps run.

### Execution scenarios

![Static pipeline](https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-1ac3d5cbe1ec72b8daee4922d18b606da488b763%2Fexecution-static.png?alt=media) ![Static pipeline with step operator](https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-723920fc6e89bc0b1f9b591858849ce465068f1f%2Fexecution-static-step-operator.png?alt=media)

## Dynamic pipelines

[Dynamic pipelines](https://docs.zenml.io/concepts/steps_and_pipelines/dynamic_pipelines) execute the pipeline function at runtime. Each step executed inside the pipeline function can be:

* **Inline** (runs inside the orchestration environment)
* **Isolated** (runs in a separate environment via the orchestrator or a step operator)

And each step call can be:

* **Synchronous** (via `my_step(...)`): blocks until completion and returns the step output artifacts.
* **Concurrent** (via `my_step.submit(...)`): starts step execution in a separate thread and returns a future. The pipeline function resumes execution immediately.

### Execution scenarios

#### Synchronous inline

The step runs in-process inside the orchestration environment. The pipeline function blocks until the step completes.

![Dynamic pipeline, synchronous inline step](https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-5e44f5ac7b46db840c553bcf4ad7d32a70e44f91%2Fexecution-dynamic-sync-inline.png?alt=media)

#### Concurrent inline

The step runs in-process in a separate thread. The pipeline function continues immediately and only waits when results are consumed.

![Dynamic pipeline, concurrent inline step](https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-98cf90483e34ea7940231932c837846b4b12a944%2Fexecution-dynamic-concurrent-inline.png?alt=media)

#### Synchronous isolated

The step runs in a separate environment (via the orchestrator or step operator). The pipeline function blocks until the job completes.

![Dynamic pipeline, synchronous isolated step](https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-a2e7d2e2ad54b826a67e5b963b8b6ae6b450cdb4%2Fexecution-dynamic-sync-isolated.png?alt=media)

#### Concurrent isolated

The step runs in a separate environment (via the orchestrator or step operator). The pipeline function continues immediately and only waits when results are consumed.

![Dynamic pipeline, concurrent isolated step](https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-0227fb4502635214ec7fd2fc44e1e8b9d17d6e4c%2Fexecution-dynamic-concurrent-isolated.png?alt=media)
