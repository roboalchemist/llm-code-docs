# Source: https://novita.ai/docs/api-reference/gpu-instance-list-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Templates

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="pageSize" type="integer" required={false}>
  Page size. Integer, value >= 0.
</ParamField>

<ParamField query="pageNum" type="integer" required={false}>
  Page number. Integer, value >= 0.
</ParamField>

<ParamField query="name" type="string" required={false}>
  Filter the templates by name (fuzzy match). String, length limit: 1-255 characters.
</ParamField>

<ParamField query="type" type="string" required={false}>
  Filter the templates by type.
</ParamField>

<ParamField query="channel" type="string" required={true}>
  Filter the templates by channel.<br />
  Enum: `official`, `community`, `private`
</ParamField>

<ParamField query="isMyCommunity" type="boolean" required={true}>
  Template visibility scope. Values: `true`, `false`.<br />
  Note:

  * Query official/community templates: set to `false`
  * Query private templates: set to `true`
</ParamField>

## Response

<ResponseField name="template" type="object[]" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="Id" type="string" required={false}>
      Template ID.
    </ResponseField>

    <ResponseField name="name" type="string" required={false}>
      Template name.
    </ResponseField>

    <ResponseField name="readme" type="string" required={false}>
      Template README content (in Markdown format).
    </ResponseField>

    <ResponseField name="type" type="string" required={false}>
      Template type.Enum: `instance`
    </ResponseField>

    <ResponseField name="channel" type="string" required={false}>
      Template channel.Enum: `official`, `community`, `private`
    </ResponseField>

    <ResponseField name="image" type="string" required={false}>
      Docker image address for instance startup.
    </ResponseField>

    <ResponseField name="imageAuth" type="string" required={false}>
      Image repository authentication ID for private images.
    </ResponseField>

    <ResponseField name="startCommand" type="string" required={false}>
      Startup command for the instance.
    </ResponseField>

    <ResponseField name="entrypoint" type="string" required={false}>
      Instance startup entrypoint.
    </ResponseField>

    <ResponseField name="rootfsSize" type="integer" required={false}>
      Rootfs storage (GB).
    </ResponseField>

    <ResponseField name="ports" type="object[]" required={false}>
      Exposed ports settings.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="type" type="string" required={false}>
          Exposed port types.Enum: `http, tcp`
        </ResponseField>

        <ResponseField name="ports" type="[integer]" required={false}>
          Exposed ports (maximum 10).
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="envs" type="object[]" required={false}>
      Environment variables injected into instance.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="key" type="string" required={false}>
          Environment variable key.
        </ResponseField>

        <ResponseField name="value" type="string" required={false}>
          Environment variable value.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="tools" type="object[]" required={false}>
      Template built-in tools (only available for official templates).

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="name" type="string" required={false}>
          Tool name.
        </ResponseField>

        <ResponseField name="describe" type="string" required={false}>
          Tool description.
        </ResponseField>

        <ResponseField name="port" type="integer" required={false}>
          Tool port.
        </ResponseField>

        <ResponseField name="type" type="string" required={false}>
          Tool protocol type. Enum: `http`, `tcp`
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="createdAt" type="string" required={false}>
      Template creation timestamp (Unix seconds).
    </ResponseField>

    <ResponseField name="recommendCards" type="object[]" required={false}>
      Recommended GPU card specs (only available for official templates).

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="gpuSpecId" type="string" required={false}>
          GPU spec ID.
        </ResponseField>

        <ResponseField name="cardNum" type="string" required={false}>
          Recommended card number.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="minCudaVersion" type="string" required={false}>
      Minimum required CUDA version, e.g. 11.8, 12.4.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="total" type="integer" required={false}>
  Total number of templates.
</ResponseField>

## Example

Request

```bash  theme={"system"}
curl --request GET \
  --url 'https://api.novita.ai/gpu-instance/openapi/v1/templates' \
  --header 'Authorization: Bearer {{API Key}}'
```

Response

````json  theme={"system"}
{
  "template": [
    {
      "Id": "100",
      "name": "name",
      "readme": "```\nreadme\n```\n# uiohiu\n68686",
      "type": "instance",
      "channel": "official",
      "image": "image",
      "imageAuth": "",
      "startCommand": "startCommand",
      "entrypoint": "",
      "rootfsSize": 10,
      "ports": [
        {
          "type": "tcp",
          "ports": [8080, 8090]
        },
        {
          "type": "http",
          "ports": [6000, 60001]
        }
      ],
      "envs": [
        {
          "key": "testkey",
          "value": "123"
        }
      ],
      "tools": [
        {
          "name": "Jupyter",
          "describe": "Start Jupyter Notebook",
          "port": 8888,
          "type": "http"
        }
      ],
      "createdAt": "1711995567",
      "recommendCards": [
        {
          "gpuSpecId": "4090.18c.60g",
          "cardNum": "2"
        }
      ],
      "minCudaVersion": "11.8"
    }
  ],
  "total": 10
}
````


Built with [Mintlify](https://mintlify.com).