# Source: https://novita.ai/docs/api-reference/serverless-list-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Endpoints

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="pageSize" type="integer" required={true}>
  Maximum number of items returned per page.
</ParamField>

<ParamField query="pageNum" type="integer" required={true}>
  Current page number.
</ParamField>

## Response

<ResponseField name="endpoints" type="object[]" required={true}>
  Endpoint information.

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="id" type="string" required={true}>
      Endpoint ID.
    </ResponseField>

    <ResponseField name="name" type="string" required={true}>
      Endpoint name.
    </ResponseField>

    <ResponseField name="appName" type="string" required={true}>
      Application name.
    </ResponseField>

    <ResponseField name="state" type="object" required={true}>
      Endpoint status.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="state" type="string" required={true}>
          Endpoint status. When the value is `serving`, the endpoint is available for service.
        </ResponseField>

        <ResponseField name="error" type="string" required={false}>
          Error code when the endpoint is in an abnormal state.
        </ResponseField>

        <ResponseField name="message" type="string" required={false}>
          Error message when the endpoint is in an abnormal state.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="url" type="string" required={true}>
      Endpoint URL. You can access your HTTP service via this URL.
    </ResponseField>

    <ResponseField name="workerConfig" type="object" required={true}>
      Worker configuration for the endpoint.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="minNum" type="integer" required={true}>
          Minimum number of workers.
        </ResponseField>

        <ResponseField name="maxNum" type="integer" required={true}>
          Maximum number of workers.
        </ResponseField>

        <ResponseField name="freeTimeout" type="string" required={true}>
          Idle timeout, in seconds.
        </ResponseField>

        <ResponseField name="maxConcurrent" type="string" required={true}>
          Maximum concurrency.
        </ResponseField>

        <ResponseField name="gpuNum" type="integer" required={true}>
          Number of GPUs per worker.
        </ResponseField>

        <ResponseField name="cudaVersion" type="string" required={true}>
          CUDA version.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="policy" type="object" required={true}>
      Auto-scaling policy for the endpoint.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="type" type="string" required={true}>
          Policy type. Options:

          * `queue`: Queue latency policy, adjusts the number of workers based on the waiting time of requests in the queue.
          * `concurrency`: Queue request policy, automatically adjusts the number of workers based on the number of requests in the queue.
        </ResponseField>

        <ResponseField name="value" type="string" required={true}>
          The meaning of value depends on the type:

          * If type = queue, value is the queue waiting time in seconds.
          * If type = concurrency, value is the maximum number of requests in the queue.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="image" type="object" required={true}>
      Image configuration for the endpoint.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="image" type="string" required={true}>
          Image URL.
        </ResponseField>

        <ResponseField name="authId" type="string" required={true}>
          Image repository credential.
        </ResponseField>

        <ResponseField name="command" type="string" required={true}>
          Container startup command.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="rootfsSize" type="integer" required={true}>
      System disk size.
    </ResponseField>

    <ResponseField name="volumeMounts" type="object[]" required={true}>
      Storage configuration for the endpoint.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="type" type="string" required={true}>
          Storage type. Options:

          * `local`: Local storage.
          * `network`: Cloud storage.
        </ResponseField>

        <ResponseField name="id" type="string" required={true}>
          Cloud storage ID. Returned when type = network.
        </ResponseField>

        <ResponseField name="size" type="integer" required={false}>
          Returned when type = local, indicates the size of the local disk.
        </ResponseField>

        <ResponseField name="mountPath" type="string" required={true}>
          Mount path for the storage.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="envs" type="object[]" required={true}>
      Environment variables.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="key" type="string" required={true}>
          Environment variable name.
        </ResponseField>

        <ResponseField name="value" type="string" required={true}>
          Environment variable value.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="ports" type="object[]" required={true}>
      HTTP ports.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="port" type="string" required={true}>
          HTTP port.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="workers" type="object[]" required={true}>
      Worker information for the endpoint.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="id" type="string" required={true}>
          Worker ID.
        </ResponseField>

        <ResponseField name="state" type="object" required={true}>
          Worker status.

          <Expandable title="properties" defaultOpen={true}>
            <ResponseField name="state" type="string" required={true}>
              Worker status. When the value is `running`, the worker is available for service.
            </ResponseField>

            <ResponseField name="error" type="string" required={false}>
              Error code when the worker is in an abnormal state.
            </ResponseField>

            <ResponseField name="message" type="string" required={false}>
              Error message when the worker is in an abnormal state.
            </ResponseField>
          </Expandable>
        </ResponseField>

        <ResponseField name="log" type="string" required={true}>
          Log path for the worker.
        </ResponseField>

        <ResponseField name="metrics" type="string" required={true}>
          Monitoring information for the worker.
        </ResponseField>

        <ResponseField name="healthy" type="boolean" required={true}>
          Whether the worker is healthy.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="products" type="object[]" required={true}>
      Product information.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="id" type="string" required={true}>
          Product ID.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="healthy" type="object" required={true}>
      Health check configuration for the endpoint.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="path" type="string" required={true}>
          Path to be checked via HTTP request for health monitoring.
        </ResponseField>

        <ResponseField name="initialDelay" type="integer" required={true}>
          Time to wait after startup before starting health checks, in seconds.
        </ResponseField>

        <ResponseField name="period" type="integer" required={true}>
          Interval between health checks, in seconds.
        </ResponseField>

        <ResponseField name="timeout" type="integer" required={true}>
          Timeout for health checks, in seconds.
        </ResponseField>

        <ResponseField name="successThreshold" type="integer" required={true}>
          Number of consecutive successes required to consider the check successful after a previous failure.
        </ResponseField>

        <ResponseField name="failureThreshold" type="integer" required={true}>
          Number of consecutive failures required to consider the check failed after a previous success.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="clusterID" type="string" required={true}>
      Cluster ID where the cloud storage resides. Returned when using cloud storage.
    </ResponseField>

    <ResponseField name="log" type="string" required={true}>
      Log path for the endpoint.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="total" type="integer" required={true}>
  Total number of results.
</ResponseField>


Built with [Mintlify](https://mintlify.com).