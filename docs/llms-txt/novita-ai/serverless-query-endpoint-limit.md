# Source: https://novita.ai/docs/api-reference/serverless-query-endpoint-limit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Endpoint Parameter Limit Ranges

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Response

<ResponseField name="minRootfsSize" type="integer" required={true}>
  Minimum root filesystem size (GB).
</ResponseField>

<ResponseField name="maxRootfsSize" type="integer" required={true}>
  Maximum root filesystem size (GB).
</ResponseField>

<ResponseField name="freeRootfsSize" type="integer" required={true}>
  Free root filesystem size (GB).
</ResponseField>

<ResponseField name="minLocalVolumeSize" type="integer" required={true}>
  Minimum local volume size (GB).
</ResponseField>

<ResponseField name="maxLocalVolumeSize" type="integer" required={true}>
  Maximum local volume size (GB).
</ResponseField>

<ResponseField name="freeLocalVolumeSize" type="integer" required={true}>
  Free local volume size (GB).
</ResponseField>

<ResponseField name="minWorkerNum" type="integer" required={true}>
  Minimum number of worker nodes.
</ResponseField>

<ResponseField name="maxWorkerNum" type="integer" required={true}>
  Maximum number of worker nodes.
</ResponseField>

<ResponseField name="minFreeTimeout" type="integer" required={true}>
  Minimum idle timeout (seconds).
</ResponseField>

<ResponseField name="maxFreeTimeout" type="integer" required={true}>
  Maximum idle timeout (seconds).
</ResponseField>

<ResponseField name="minConcurrencyNum" type="integer" required={true}>
  Minimum concurrency.
</ResponseField>

<ResponseField name="maxConcurrencyNum" type="integer" required={true}>
  Maximum concurrency.
</ResponseField>

<ResponseField name="minQueueWaitTime" type="integer" required={true}>
  Minimum queue wait time (seconds).
</ResponseField>

<ResponseField name="maxQueueWaitTime" type="integer" required={true}>
  Maximum queue wait time (seconds).
</ResponseField>

<ResponseField name="minRequestNum" type="integer" required={true}>
  Minimum number of requests.
</ResponseField>

<ResponseField name="maxRequestNum" type="integer" required={true}>
  Maximum number of requests.
</ResponseField>

<ResponseField name="minGPUNum" type="integer" required={true}>
  Minimum number of GPUs.
</ResponseField>

<ResponseField name="maxGPUNum" type="integer" required={true}>
  Maximum number of GPUs.
</ResponseField>

<ResponseField name="cudaVersionList" type="string[]" required={true}>
  Supported CUDA version list.
</ResponseField>


Built with [Mintlify](https://mintlify.com).