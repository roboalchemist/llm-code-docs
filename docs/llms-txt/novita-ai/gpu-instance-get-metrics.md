# Source: https://novita.ai/docs/api-reference/gpu-instance-get-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch Instance Monitor Metrics

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<Note>
  If the parameters endTime, startTime, or interval do not meet the requirements, default values will be used. There may be a delay of about one minute when retrieving real-time monitoring data.
</Note>

<ParamField query="instanceId" type="string" required={true}>
  Instance ID.
</ParamField>

<ParamField query="endTime" type="integer" required={false}>
  End time for querying monitoring data. Value range: (0, current timestamp], default: current timestamp.
</ParamField>

<ParamField query="startTime" type="integer" required={false}>
  Start time for querying monitoring data. Value range: (0, endTime - 60], default: current timestamp - 60.
</ParamField>

<ParamField query="interval" type="integer" required={false}>
  Time granularity for monitoring data, in seconds. Value must be greater than 15. Default: 15.
</ParamField>

## Response

<ResponseField name="cpuUtilization" type="array" required={true}>
  CPU utilization data.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="timestamp" type="string" required={true}>
      Timestamp.
    </ResponseField>

    <ResponseField name="value" type="number" required={true}>
      CPU utilization.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="memUtilization" type="array" required={true}>
  Memory utilization data.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="timestamp" type="string" required={true}>
      Timestamp.
    </ResponseField>

    <ResponseField name="value" type="number" required={true}>
      Memory utilization.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="rootDiskUtilization" type="array" required={true}>
  Root disk utilization data.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="timestamp" type="string" required={true}>
      Timestamp.
    </ResponseField>

    <ResponseField name="value" type="number" required={true}>
      Root disk utilization.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="gpuUtilization" type="object" required={true}>
  GPU utilization data.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="avg" type="array" required={true}>
      Average utilization across all GPUs.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="timestamp" type="string" required={true}>
          Timestamp.
        </ResponseField>

        <ResponseField name="value" type="number" required={true}>
          Utilization.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="gpuIds" type="array" required={true}>
      Utilization for each GPU.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="gpuId" type="string" required={true}>
          GPU ID in use.
        </ResponseField>

        <ResponseField name="items" type="array" required={true}>
          GPU utilization data.

          <Expandable title="properties" defaultOpen={false}>
            <ResponseField name="timestamp" type="string" required={true}>
              Timestamp.
            </ResponseField>

            <ResponseField name="value" type="number" required={true}>
              Utilization.
            </ResponseField>
          </Expandable>
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="gpuMemUtilization" type="object" required={true}>
  GPU memory utilization data.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="avg" type="array" required={true}>
      Average GPU memory utilization across all GPUs.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="timestamp" type="string" required={true}>
          Timestamp.
        </ResponseField>

        <ResponseField name="value" type="number" required={true}>
          Utilization.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="gpuIds" type="array" required={true}>
      GPU memory utilization for each GPU.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="gpuId" type="string" required={true}>
          GPU ID in use.
        </ResponseField>

        <ResponseField name="items" type="array" required={true}>
          GPU memory utilization data.

          <Expandable title="properties" defaultOpen={false}>
            <ResponseField name="timestamp" type="string" required={true}>
              Timestamp.
            </ResponseField>

            <ResponseField name="value" type="number" required={true}>
              Utilization.
            </ResponseField>
          </Expandable>
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).