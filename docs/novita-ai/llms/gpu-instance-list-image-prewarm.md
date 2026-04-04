# Source: https://novita.ai/docs/api-reference/gpu-instance-list-image-prewarm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Image Prewarm Tasks

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="page" type="integer" required={false}>
  Page number. Default: 1.
</ParamField>

<ParamField query="pageSize" type="integer" required={false}>
  Page size. Default: 10.
</ParamField>

<ParamField query="state" type="string" required={false}>
  Prewarm task state. Valid values: `Pending`, `Running`, `Succeeded`, `Failed`.
</ParamField>

<ParamField query="clusterId" type="string" required={false}>
  Cluster ID.
</ParamField>

<ParamField query="name" type="string" required={false}>
  Image name or task note for fuzzy matching.
</ParamField>

## Response

<ResponseField name="data" type="object[]" required={true}>
  List of prewarm tasks.

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="id" type="string" required={true}>
      Prewarm task ID.
    </ResponseField>

    <ResponseField name="imageName" type="string" required={true}>
      Image name (the last segment of the image URL without the tag).
    </ResponseField>

    <ResponseField name="imageUrl" type="string" required={true}>
      Image URL.
    </ResponseField>

    <ResponseField name="repositoryAuth" type="string" required={false}>
      Image registry authentication ID.
    </ResponseField>

    <ResponseField name="clusterId" type="string" required={true}>
      Cluster ID.
    </ResponseField>

    <ResponseField name="clusterName" type="string" required={true}>
      Cluster name.
    </ResponseField>

    <ResponseField name="products" type="object[]" required={true}>
      Products to prewarm.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="productId" type="string" required={true}>
          Product ID.
        </ResponseField>

        <ResponseField name="productName" type="string" required={true}>
          Product name.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="imageSize" type="string" required={false}>
      Image size in bytes.
    </ResponseField>

    <ResponseField name="createTime" type="string" required={true}>
      Task creation time (Unix timestamp in seconds).
    </ResponseField>

    <ResponseField name="state" type="string" required={true}>
      Task state. Valid values: `Pending`, `Running`, `Succeeded`, `Failed`.
    </ResponseField>

    <ResponseField name="completeTime" type="string" required={false}>
      Task completion time (Unix timestamp in seconds).
    </ResponseField>

    <ResponseField name="note" type="string" required={false}>
      Task note.
    </ResponseField>

    <ResponseField name="reason" type="string[]" required={false}>
      Reason messages.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="total" type="integer" required={true}>
  Total number of tasks.
</ResponseField>


Built with [Mintlify](https://mintlify.com).