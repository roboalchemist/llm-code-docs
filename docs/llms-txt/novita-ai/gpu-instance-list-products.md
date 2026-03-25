# Source: https://novita.ai/docs/api-reference/gpu-instance-list-products.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List GPU Products

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="clusterId" type="string" required={false}>
  Filter by specified cluster ID. String, length limit: 0-255 characters.
</ParamField>

<ParamField query="gpuNum" type="integer" required={false}>
  Filter by number of GPUs. Integer, valid range: \[0, 8].
</ParamField>

<ParamField query="productName" type="string" required={false}>
  Filter by product name (fuzzy match). String, length limit: 0-255 characters.
</ParamField>

<ParamField query="minCpuPerGpu" type="integer" required={false}>
  Filter by minimum CPU cores per GPU. Integer, value must be greater than or equal to 0.
</ParamField>

<ParamField query="minMemoryPerGpu" type="integer" required={false}>
  Filter by minimum memory per GPU (GB). Integer, value must be greater than or equal to 0.
</ParamField>

<ParamField query="minRootFSSize" type="integer" required={false}>
  Filter by minimum root filesystem size per GPU (GB). Integer, value must be greater than or equal to 0.
</ParamField>

<ParamField query="billingMethod" type="string" required={false}>
  Filter by billing method. Options:

  * `onDemand`: Pay-as-you-go instance (default)
  * `monthly`: Subscription instance (monthly or yearly)
  * `spot`: Spot instance billing
</ParamField>

## Response

<ResponseField name="data" type="object[]" required={true}>
  GPU product information.

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="id" type="string" required={true}>
      Product ID.
    </ResponseField>

    <ResponseField name="name" type="string" required={true}>
      Product name.
    </ResponseField>

    <ResponseField name="cpuPerGpu" type="integer" required={true}>
      Number of CPU cores per GPU.
    </ResponseField>

    <ResponseField name="memoryPerGpu" type="integer" required={true}>
      Memory size per GPU (GB).
    </ResponseField>

    <ResponseField name="diskPerGpu" type="integer" required={true}>
      Disk size per GPU (GB).
    </ResponseField>

    <ResponseField name="availableDeploy" type="boolean" required={true}>
      Whether this product can be used to create an instance. Values:

      * true: The product can be used to create an instance.
      * false: Insufficient resources, cannot create an instance.
    </ResponseField>

    <ResponseField name="minRootFS" type="integer" required={true}>
      Minimum available root filesystem size (GB).
    </ResponseField>

    <ResponseField name="maxRootFS" type="integer" required={true}>
      Maximum available root filesystem size (GB).
    </ResponseField>

    <ResponseField name="minLocalStorage" type="integer" required={true}>
      Minimum available local storage size (GB).
    </ResponseField>

    <ResponseField name="maxLocalStorage" type="integer" required={true}>
      Maximum available local storage size (GB).
    </ResponseField>

    <ResponseField name="regions" type="[string]" required={true}>
      Available clusters. Indicates that this product is only available in the specified clusters. If the list is empty, the product is available in all clusters.
    </ResponseField>

    <ResponseField name="price" type="integer" required={true}>
      Price for creating a pay-as-you-go instance with this product.
    </ResponseField>

    <ResponseField name="monthlyPrice" type="object[]" required={true}>
      Price for creating a subscription (monthly or yearly) instance with this product.

      <Expandable title="properties" defaultOpen={true}>
        <ResponseField name="price" type="integer" required={true}>
          Unit price for the subscription instance.
        </ResponseField>

        <ResponseField name="month" type="integer" required={true}>
          Subscription duration, in months.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="billingMethods" type="string[]" required={true}>
      The billing methods supported by this product. Valid values:

      * `onDemand`: Pay-as-you-go billing
      * `monthly`: Monthly subscription billing
      * `spot`: Spot instance billing
    </ResponseField>

    <ResponseField name="spotPrice" type="string" required={false}>
      Spot billing instance price.
    </ResponseField>

    <ResponseField name="inventoryState" type="string" required={false}>
      Product inventory status:

      * `none`: Out of stock
      * `low`: Low stock
      * `normal`: Normal stock
      * `high`: Sufficient stock
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).