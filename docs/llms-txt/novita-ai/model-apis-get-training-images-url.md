# Source: https://novita.ai/docs/api-reference/model-apis-get-training-images-url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Images URL

**This API provides an S3 pre-signed uploading URL for training images.**

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="file_extension" type="string" required={true}>
  Enum: `png`, `webp`, `jpeg`
</ParamField>

## Response

<ResponseField name="assets_id" type="integer" required={false}>
  The asset ID.
</ResponseField>

<ResponseField name="upload_url" type="string" required={false}>
  The S3 pre-signed uploading URL.
</ResponseField>

<ResponseField name="method" type="string" required={false}>
  The method for uploading.<br />
  Enum: `PUT`
</ResponseField>

<ResponseField name="headers" type="object" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="Host" type="object" required={false}>
      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="values" type="string[]" required={false}>
          The host value.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

## Example

request

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/assets/training_dataset' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
  "file_extension": "png"
}'
```

response

```json  theme={"system"}
{
  "assets_id": 100024,
  "upload_url": "https://faas-training-dataset.s3.ap-southeast-1.amazonaws.com/test/743567e210ff505ce5502cfb46659c8e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20231102%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20231102T060519Z&X-Amz-Expires=120&X-Amz-SignedHeaders=host&x-id=PutObject&X-Amz-Signature=781d2156b707b7cfa87d94fb2836838e114c3afe4588368b9503c618ac125a67",
  "method": "PUT",
  "headers": {
    "Host": {
      "values": ["faas-training-dataset.s3.ap-southeast-1.amazonaws.com"]
    }
  }
}
```


Built with [Mintlify](https://mintlify.com).