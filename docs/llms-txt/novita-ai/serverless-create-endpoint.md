# Source: https://novita.ai/docs/api-reference/serverless-create-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Endpoint

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="endpoint" type="object" required={true}>
  Endpoint configuration.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="name" type="string" required={false}>
      Endpoint name. String with a length limit of 0-220 characters.
    </ParamField>

    <ParamField body="appName" type="string" required={false}>
      Application name (reflected in the URL). The application name is part of the Endpoint URL, supports customization, and defaults to the Endpoint ID.
    </ParamField>

    <ParamField body="workerConfig" type="object" required={true}>
      Worker configuration. The valid range is dynamically retrieved through the parameter limits API.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="minNum" type="integer" required={true}>
          Minimum number of workers.
        </ParamField>

        <ParamField body="maxNum" type="integer" required={true}>
          Maximum number of workers.
        </ParamField>

        <ParamField body="freeTimeout" type="integer" required={true}>
          Idle timeout in seconds.
        </ParamField>

        <ParamField body="maxConcurrent" type="integer" required={true}>
          Maximum concurrency.
        </ParamField>

        <ParamField body="gpuNum" type="integer" required={true}>
          Number of GPUs per worker.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="ports" type="object[]" required={true}>
      HTTP ports. Only one port is supported. Supported port range: 1-65535, excluding internal ports 2222, 2223, and 2224.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="port" type="string" required={true}>
          HTTP port.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="policy" type="object" required={true}>
      Scaling policy. The valid range is dynamically retrieved through the parameter limits API.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="type" type="string" required={true}>
          Scaling policy type. Available values:

          * `queue`: Queue latency policy, scales workers based on request wait time in the queue.
          * `concurrency`: Queue request policy, scales workers based on the number of requests in the queue.
        </ParamField>

        <ParamField body="value" type="integer" required={true}>
          The meaning of value depends on the type:

          * When type = queue, value represents the queue wait time in seconds.
          * When type = concurrency, value represents the maximum number of requests in the queue.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="image" type="object" required={true}>
      Container image configuration.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="image" type="string" required={true}>
          Image address. String with a length limit of 0-511 characters.
        </ParamField>

        <ParamField body="authId" type="string" required={false}>
          Private image credential ID (not required for public images or platform user images). String with a length limit of 0-255 characters.
        </ParamField>

        <ParamField body="command" type="string" required={false}>
          Container startup command. String with a length limit of 0-2047 characters.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="products" type="object[]" required={true}>
      Product information.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="id" type="string" required={true}>
          Product ID.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="rootfsSize" type="integer" required={true}>
      Root filesystem size in GB. Currently fixed at 100.
    </ParamField>

    <ParamField body="volumeMounts" type="object[]" required={true}>
      Storage configuration in GB.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="type" type="string" required={true}>
          Storage type. Available values:

          * `local`: Local storage.
          * `network`: Network storage.
        </ParamField>

        <ParamField body="size" type="integer" required={false}>
          Local storage size, currently fixed at 30. Not required for network storage.
        </ParamField>

        <ParamField body="id" type="string" required={false}>
          Network storage ID. Not required for local storage.
        </ParamField>

        <ParamField body="mountPath" type="string" required={true}>
          Storage mount path. String with a length limit of 0-255 characters.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="clusterID" type="string" required={false}>
      Cluster information. Required when mounting cloud storage and must match the cluster ID where the cloud storage is located. String with a length limit of 0-255 characters.
    </ParamField>

    <ParamField body="envs" type="object[]" required={false}>
      Environment variables.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="key" type="string" required={true}>
          Environment variable name.
        </ParamField>

        <ParamField body="value" type="string" required={true}>
          Environment variable value.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="healthy" type="object" required={true}>
      Health check endpoint configuration.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="path" type="string" required={true}>
          The path to check when performing HTTP health checks.
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="id" type="string" required={false}>
  The created Endpoint ID.
</ResponseField>


Built with [Mintlify](https://mintlify.com).