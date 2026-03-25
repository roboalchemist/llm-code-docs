# Source: https://novita.ai/docs/api-reference/model-apis-get-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Model

**This API endpoint is designed to retrieve information on both public and private models. It allows users to access details such as model specifications, status, and usage guidelines, ensuring comprehensive insights into the available modeling resources.**

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="filter.visibility" type="string" required={false}>
  Model types: `public` or `private`. If not set, the interface will query all types of models.
</ParamField>

<ParamField query="filter.source" type="string" required={false}>
  Source of the model.<br />
  Enum: `civitai`, `training`, `uploading`
</ParamField>

<ParamField query="filter.types" type="string" required={false}>
  Specifies the types of models to include in the query.<br />
  Enum: `checkpoint`, `lora`, `vae`, `controlnet`, `upscaler`, `textualinversion`
</ParamField>

<ParamField query="filter.is_sdxl" type="boolean" required={false}>
  Whether the model is SDXL or not. Setting this parameter to `true` includes only SDXL models in the query results, which are typically large-scale, high-performance models designed for extensive data processing tasks. Conversely, setting it to `false` excludes these models from the results. If left unspecified, the filter will not discriminate based on the SDXL classification, including all model types in the search results.
</ParamField>

<ParamField query="filter.query" type="string" required={false}>
  Searches the content of sd\_name, name, and tags.
</ParamField>

<ParamField query="filter.is_inpainting" type="boolean" required={false}>
  If set to true, it will filter out the checkpoints used for inpainting. The default is false.
</ParamField>

<ParamField query="pagination.limit" type="string" required={false}>
  Number of models to query per request, range (0, 100].
</ParamField>

<ParamField query="pagination.cursor" type="string" required={false}>
  pagination.cursor is used to specify which record to start returning from. If it is empty, it means to get it from the beginning. Generally, the content of the next page is obtained by passing in the next\_cursor field value from the response packet.
</ParamField>

## Response

<ResponseField name="models" type="object[]" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="id" type="integer" required={false}>
      ID of the model.
    </ResponseField>

    <ResponseField name="name" type="string" required={false}>
      Model name.
    </ResponseField>

    <ResponseField name="hash_sha256" type="string" required={false}>
      Hash of the model file.
    </ResponseField>

    <ResponseField name="sd_name" type="string" required={false}>
      Model file name.
    </ResponseField>

    <ResponseField name="type" type="object" required={false}>
      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="name" type="string" required={false}>
          Model type name.
        </ResponseField>

        <ResponseField name="display_name" type="string" required={false} />
      </Expandable>
    </ResponseField>

    <ResponseField name="categories" type="string[]" required={false}>
      Model categories.
    </ResponseField>

    <ResponseField name="status" type="integer" required={false}>
      Model status: 0 for unavailable, 1 for available.
    </ResponseField>

    <ResponseField name="download_url" type="string" required={false}>
      Model download URL.
    </ResponseField>

    <ResponseField name="tags" type="string[]" required={false}>
      Model tags, such as photorealistic, anatomical, base model, CGI, realistic, semi-realistic.
    </ResponseField>

    <ResponseField name="cover_url" type="string" required={false}>
      Model cover image URL.
    </ResponseField>

    <ResponseField name="source" type="string" required={false}>
      The source of the model, such as civitai, training, uploading.
    </ResponseField>

    <ResponseField name="base_model" type="string" required={false}>
      Base model of the model, such as SD 1.5 or SDXL 1.0.
    </ResponseField>

    <ResponseField name="base_model_type" type="string" required={false}>
      Base model type of the model, such as Inpainting or Standard.
    </ResponseField>

    <ResponseField name="download_url_ttl" type="integer" required={false}>
      The expiration time of the download URL in seconds, default is 1 day.
    </ResponseField>

    <ResponseField name="sd_name_in_api" type="string" required={false}>
      The name users can add in the interface.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="pagination" type="object" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="next_cursor" type="string" required={false}>
      Next request starting cursor.
    </ResponseField>
  </Expandable>
</ResponseField>

## Example

request

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/model?filter.visibility=public&pagination.limit=2&pagination.cursor=c_0' \
--header 'Authorization: Bearer {{API Key}}'
```

response

```json  theme={"system"}
{
  "models": [
    {
      "id": 114600,
      "name": "V4.0-inpainting (VAE)",
      "hash_sha256": "1A805277C8",
      "sd_name": "realisticVisionV40_v40VAE-inpainting_81543.safetensors",
      "type": {
        "name": "checkpoint",
        "display_name": "Checkpoint"
      },
      "categories": [],
      "status": 1,
      "tags": [
        "photorealistic",
        "anatomical",
        "base model",
        "cgi",
        "realistic",
        "semi-realistic"
      ],
      "cover_url": "https://next-app-static.s3.amazonaws.com/images-prod/xG1nkqKTMzGDvpLrqFT7WA/f291a219-4a86-45ab-96eb-c53446b3e4df/width=450/1495044.jpeg",
      "base_model": "SD 1.5",
      "base_model_type": "Inpainting",
      "download_url_ttl": 2592000,
      "sd_name_in_api": "realisticVisionV40_v40VAE-inpainting_81543.safetensors",
      "is_sdxl": false
    },
    {
      "id": 55199,
      "name": "beta2",
      "hash_sha256": "BA43B0EFEE",
      "sd_name": "GoodHands-beta2_39807.safetensors",
      "type": {
        "name": "locon",
        "display_name": "locon"
      },
      "categories": [],
      "status": 1,
      "tags": ["photorealistic", "concept", "hands"],
      "cover_url": "https://next-app-static.s3.amazonaws.com/images-prod/xG1nkqKTMzGDvpLrqFT7WA/031a378c-3d66-45da-5d67-966c47cd4800/width=450/599083.jpeg",
      "base_model": "SD 1.5",
      "base_model_type": "Standard",
      "download_url_ttl": 2592000,
      "sd_name_in_api": "GoodHands-beta2_39807",
      "is_sdxl": false
    }
  ],
  "pagination": {
    "next_cursor": "c_WzgwNDY2NiwiNTUxOTkiXQ=="
  }
}
```


Built with [Mintlify](https://mintlify.com).