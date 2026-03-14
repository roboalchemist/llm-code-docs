# Source: https://novita.ai/docs/api-reference/gpu-instance-get-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Instance

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="instanceId" type="string" required={true}>
  ID of the instance being queried.
</ParamField>

## Response

<ResponseField name="id" type="string" required={true}>
  Instance ID.
</ResponseField>

<ResponseField name="name" type="string" required={true}>
  Instance name.
</ResponseField>

<ResponseField name="clusterId" type="string" required={true}>
  Cluster ID.
</ResponseField>

<ResponseField name="clusterName" type="string" required={true}>
  Name of the cluster.
</ResponseField>

<ResponseField name="imageUrl" type="string" required={true}>
  Container image URL.
</ResponseField>

<ResponseField name="imageAuthId" type="string" required={true}>
  Image registry authentication information.
</ResponseField>

<ResponseField name="command" type="string" required={true}>
  Container startup command.
</ResponseField>

<ResponseField name="entrypoint" type="string" required={true}>
  Container startup entrypoint.
</ResponseField>

<ResponseField name="cpuNum" type="string" required={true}>
  Number of CPU cores allocated to the instance.
</ResponseField>

<ResponseField name="memory" type="string" required={true}>
  Memory size allocated to the instance, in GB.
</ResponseField>

<ResponseField name="gpuNum" type="string" required={true}>
  Number of GPU cards allocated to the instance.
</ResponseField>

<ResponseField name="status" type="string" required={true}>
  Instance status. Possible values:

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

<ResponseField name="network" type="object" required={false}>
  VPC network information for the instance.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="id" type="string" required={false}>
      VPC network ID.
    </ResponseField>

    <ResponseField name="ip" type="string" required={false}>
      Instance IP address.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="portMappings" type="object[]" required={true}>
  Instance port mapping information.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="port" type="integer" required={true}>
      Port number.
    </ResponseField>

    <ResponseField name="endpoint" type="string" required={true}>
      Endpoint.
    </ResponseField>

    <ResponseField name="type" type="string" required={true}>
      Protocol type.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="volumeMounts" type="object[]" required={false}>
  Storage configuration for the instance.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="type" type="string" required={false}>
      Storage type. Possible values:

      * network: Cloud storage.
      * local: Local storage.
    </ResponseField>

    <ResponseField name="size" type="number" required={false}>
      Storage capacity.
    </ResponseField>

    <ResponseField name="id" type="string" required={false}>
      Cloud storage ID. Only present when the storage type is "network".
    </ResponseField>

    <ResponseField name="mountPath" type="string" required={false}>
      Mount path for the storage.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="node" type="object[]" required={false}>
  Node information.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="maxRootfsSize" type="number" required={false}>
      Maximum available system disk size.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="jobs" type="object[]" required={false}>
  Tasks currently running on the instance.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="id" type="string" required={false}>
      Task ID.
    </ResponseField>

    <ResponseField name="type" type="string" required={false}>
      Task type. Currently, only saveImage is supported, which indicates saving an image.
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

<ResponseField name="connectComponentSSH" type="object" required={false}>
  Instance SSH connection information.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="sshCommand" type="string" required={false}>
      Command for SSH remote login.
    </ResponseField>

    <ResponseField name="password" type="string" required={false}>
      Password for SSH remote login.
    </ResponseField>

    <ResponseField name="isRunning" type="boolean" required={false}>
      Whether SSH remote login is active.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="connectComponentWebTerminal" type="object" required={false}>
  Instance WebSSH connection information.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="address" type="string" required={false}>
      Address for web-based remote login.
    </ResponseField>

    <ResponseField name="username" type="string" required={false}>
      Username for web-based remote login.
    </ResponseField>

    <ResponseField name="password" type="string" required={false}>
      Password for web-based remote login.
    </ResponseField>

    <ResponseField name="isRunning" type="boolean" required={false}>
      Whether web-based remote login is active.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="connectComponentJupyter" type="object" required={false}>
  Jupyter connection information for the instance (if available).

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="port" type="integer" required={false}>
      Connection port.
    </ResponseField>

    <ResponseField name="address" type="string" required={false}>
      Connection address.
    </ResponseField>

    <ResponseField name="isRunning" type="boolean" required={false}>
      Whether Jupyter remote login is active.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="connectComponentLog" type="object" required={false}>
  Instance log connection information (HTTP Stream).

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="systemLogAddress" type="string" required={false}>
      System log address.
    </ResponseField>

    <ResponseField name="instanceLogAddress" type="string" required={false}>
      Instance log address.
    </ResponseField>

    <ResponseField name="isRunning" type="boolean" required={false}>
      Whether log connection is active.
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

<ResponseField name="freeStorageSize" type="integer" required={false}>
  Free system disk size (GB).
</ResponseField>

<ResponseField name="keepDataDay" type="integer" required={false}>
  Number of days data is retained after the instance is shut down.
</ResponseField>


Built with [Mintlify](https://mintlify.com).