# Source: https://docs.baseten.co/observability/export-metrics/supported-metrics.md

# Metrics support matrix

> Which metrics can be exported

<Info> Exporting metrics is in beta mode. </Info>

## `baseten_inference_requests_total`

Cumulative number of requests to the model.

Type: `counter`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="status_code" type="label" required>
  The status code of the response.
</ParamField>

<ParamField query="is_async" type="label" required>
  Whether the request was an [async inference request](/inference/async).
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_end_to_end_response_time_seconds`

End-to-end response time in seconds.

Type: `histogram`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="status_code" type="label" required>
  The status code of the response.
</ParamField>

<ParamField query="is_async" type="label" required>
  Whether the request was an [async inference request](/inference/async).
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_container_cpu_usage_seconds_total`

Cumulative CPU time consumed by the container in core-seconds.

Type: `counter`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="replica" type="label" required>
  The ID of the replica.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_replicas_active`

Number of replicas ready to serve model requests.

Type: `gauge`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_replicas_starting`

Number of replicas starting up--i.e. either waiting for resources to be available or loading the model.

Type: `gauge`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_container_cpu_memory_working_set_bytes`

Cumulative CPU time consumed by the container in seconds.

Type: `gauge`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="replica" type="label" required>
  The ID of the replica.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_gpu_memory_used`

GPU memory used in MiB.

Type: `gauge`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="replica" type="label" required>
  The ID of the replica.
</ParamField>

<ParamField query="gpu" type="label" required>
  The ID of the GPU.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_gpu_utilization`

GPU utilization as a percentage (between 0 and 100).

Type: `gauge`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="replica" type="label" required>
  The ID of the replica.
</ParamField>

<ParamField query="gpu" type="label" required>
  The ID of the GPU.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the promote to production process. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>
