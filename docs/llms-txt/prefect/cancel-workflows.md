# Source: https://docs.prefect.io/v3/advanced/cancel-workflows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# How to cancel running workflows

You can cancel a scheduled or in-progress flow run from the CLI, UI, REST API, or Python client.

When requesting cancellation, the flow run moves to a "Cancelling" state.
If the deployment is associated with a work pool, then the worker monitors
the state of flow runs and detects that cancellation is requested.
The worker then sends a signal to the flow run infrastructure, requesting termination of the run.
If the run does not terminate after a grace period (default of 30 seconds), the infrastructure is killed, ensuring the flow run exits.

<Warning>
  **A deployment is required**

  Flow run cancellation requires that the flow run is associated with a deployment.
  A monitoring process must be running to enforce the cancellation.

  Inline nested flow runs (those created without `run_deployment`), cannot be cancelled without cancelling the parent flow run.
  To cancel a nested flow run independent of its parent flow run, we recommend deploying it separately
  and starting it using the [run\_deployment](/v3/deploy/index)
  function.
</Warning>

Cancellation is resilient to restarts of Prefect workers.
To enable this, we attach metadata about the created infrastructure to the flow run.
Internally, this is referred to as the `infrastructure_pid` or infrastructure identifier.
Generally, this is composed of two parts:

* Scope: identifying where the infrastructure is running.
* ID: a unique identifier for the infrastructure within the scope.

The scope ensures that Prefect does not kill the wrong infrastructure.
For example, workers running on multiple machines may have overlapping process IDs but should not have a matching scope.

The identifiers for infrastructure types are:

* Processes: The machine hostname and the PID.
* Docker Containers: The Docker API URL and container ID.
* Kubernetes Jobs: The Kubernetes cluster name and the job name.

While the cancellation process is robust, there are a few issues than can occur:

* If the infrastructure for the flow run does not support cancellation, cancellation will not work.
* If the identifier scope does not match when attempting to cancel a flow run, the worker cannot cancel the flow run.
  Another worker may attempt cancellation.
* If the infrastructure associated with the run cannot be found or has already been killed, the worker marks the flow run as cancelled.
* If the `infrastructre_pid` is missing, the flow run is marked as cancelled but cancellation cannot be enforced.
* If the worker runs into an unexpected error during cancellation, the flow run may or may not be cancelled
  depending on where the error occurred. The worker will try again to cancel the flow run. Another worker may attempt cancellation.

### Cancel through the CLI

From the command line in your execution environment, you can cancel a flow run by using the
`prefect flow-run cancel` CLI command, passing the ID of the flow run.

```bash  theme={null}
prefect flow-run cancel 'a55a4804-9e3c-4042-8b59-b3b6b7618736'
```

### Cancel through the UI

Navigate to the flow run's detail page and click `Cancel` in the upper right corner.

<img src="https://mintcdn.com/prefect-bd373955/dwD6EJObIjtIzwSC/v3/img/ui/flow-run-cancellation-ui.png?fit=max&auto=format&n=dwD6EJObIjtIzwSC&q=85&s=6e692111f666595d04889e2e26186ebb" alt="Prefect UI" width="2484" height="619" data-path="v3/img/ui/flow-run-cancellation-ui.png" />


Built with [Mintlify](https://mintlify.com).