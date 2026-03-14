# Source: https://novita.ai/docs/api-reference/gpu-instance-list-instances.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Instances

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="pageSize" type="integer" required={true}>
  Maximum number of items returned per page. Integer, value >= 0.
</ParamField>

<ParamField query="pageNum" type="integer" required={true}>
  Page number to retrieve. Integer, value >= 0.
</ParamField>

<ParamField query="name" type="string" required={false}>
  Instance name (supports fuzzy search). String, length limit: 0-255 characters.
</ParamField>

<ParamField query="productName" type="string" required={false}>
  Product name (supports fuzzy search). String, length limit: 0-255 characters.
</ParamField>

<ParamField query="status" type="string" required={false}>
  Instance status. String, length limit: 0-63 characters. Possible values:

  * `toCreate`: Pending creation
  * `creating`: Creating
  * `pulling`: Pulling image
  * `running`: Running
  * `toStart`: Pending start
  * `starting`: Starting
  * `toStop`: Pending stop
  * `stopping`: Stopping
  * `exited`: Stopped
  * `toRestart`: Pending restart
  * `restarting`: Restarting
  * `toRemove`: Pending deletion
  * `removing`: Deleting
  * `removed`: Deleted
  * `toReset`: Pending reset (upgrade)
  * `resetting`: Resetting
  * `migrating`: Migrating
  * `freezing`: Freezing
</ParamField>

## Response

<ResponseField name="instances" type="object[]" required={true}>
  Instance information.

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="id" type="string" required={true}>
      Instance ID.
    </ResponseField>

    <ResponseField name="name" type="string" required={true}>
      Instance name.
    </ResponseField>

    <ResponseField name="clusterId" type="string" required={true}>
      Cluster ID.
    </ResponseField>

    <ResponseField name="clusterName" type="string" required={false}>
      Cluster name.
    </ResponseField>

    <ResponseField name="status" type="string" required={true}>
      Instance status.
    </ResponseField>

    <ResponseField name="imageUrl" type="string" required={true}>
      Container image URL.
    </ResponseField>

    <ResponseField name="imageAuthId" type="string" required={false}>
      Image repository authentication information.
    </ResponseField>

    <ResponseField name="command" type="string" required={false}>
      Container startup command.
    </ResponseField>

    <ResponseField name="entrypoint" type="string" required={false}>
      Container startup entrypoint.
    </ResponseField>

    <ResponseField name="cpuNum" type="string" required={true}>
      Number of CPU cores for the instance.
    </ResponseField>

    <ResponseField name="memory" type="string" required={true}>
      Memory size of the instance (GB).
    </ResponseField>

    <ResponseField name="gpuNum" type="string" required={true}>
      Number of GPUs for the instance.
    </ResponseField>

    <ResponseField name="portMappings" type="object[]" required={false}>
      Instance port information.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="port" type="integer" required={true}>
          Port value.
        </ResponseField>

        <ResponseField name="type" type="string" required={true}>
          Port type.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="productId" type="string" required={true}>
      Product ID used to deploy the instance.
    </ResponseField>

    <ResponseField name="productName" type="string" required={true}>
      Product name used to deploy the instance.
    </ResponseField>

    <ResponseField name="rootfsSize" type="integer" required={true}>
      Root filesystem size (GB).
    </ResponseField>

    <ResponseField name="volumeMounts" type="object[]" required={false}>
      Instance storage configuration.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="type" type="string" required={false}>
          Storage type. Values:

          * network: Cloud storage.
          * local: Local storage.
        </ResponseField>

        <ResponseField name="size" type="string" required={false}>
          Storage capacity.
        </ResponseField>

        <ResponseField name="id" type="string" required={false}>
          Cloud storage ID. Returned when type = network.
        </ResponseField>

        <ResponseField name="mountPath" type="string" required={false}>
          Storage mount path.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="statusError" type="object" required={false}>
      Error information when instance creation fails or the instance is unavailable.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="state" type="string" required={false}>
          Abnormal instance status.
        </ResponseField>

        <ResponseField name="message" type="string" required={false}>
          Error message.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="envs" type="object[]" required={false}>
      Instance environment variable information.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="key" type="string" required={false}>
          Environment variable name.
        </ResponseField>

        <ResponseField name="value" type="string" required={false}>
          Environment variable value.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="kind" type="string" required={false}>
      Instance type.
    </ResponseField>

    <ResponseField name="billingMode" type="string" required={true}>
      Billing mode for the instance. Values:

      * onDemand: Pay-as-you-go billing.
      * monthly: Subscription (monthly or yearly) billing.
      * spot: Spot instance billing.
    </ResponseField>

    <ResponseField name="endTime" type="string" required={false}>
      Expiration time for subscription instances. For pay-as-you-go instances, returns -1.
    </ResponseField>

    <ResponseField name="spotStatus" type="string" required={false}>
      Spot instance status. Values:

      * `running`: Running
      * `notified`: Notified for reclaim
      * `reclaiming`: Being reclaimed
      * `terminated`: Terminated
    </ResponseField>

    <ResponseField name="spotReclaimTime" type="string" required={false}>
      Spot instance reclaim time. Value "0" means reclaim has not started.
    </ResponseField>
  </Expandable>
</ResponseField>

<ParamField name="total" type="integer" required={false}>
  Total number of results.
</ParamField>


Built with [Mintlify](https://mintlify.com).