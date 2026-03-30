# Source: https://novita.ai/docs/api-reference/gpu-instance-create-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Template

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="template" type="object" required={true}>
  Template settings.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="name" type="string" required={true}>
      Template name. String, length limit: 1-255 characters.
    </ParamField>

    <ParamField body="readme" type="string" required={false}>
      Template README content (in Markdown format). String, length limit: 0-102400 characters.
    </ParamField>

    <ParamField body="type" type="string" required={true}>
      Template type.<br />
      Enum: `instance`
    </ParamField>

    <ParamField body="channel" type="string" required={true}>
      Template channel.<br />
      Enum: `private`
    </ParamField>

    <ParamField body="image" type="string" required={true}>
      Docker image address for instance startup. String, length limit: 1-500 characters.
    </ParamField>

    <ParamField body="imageAuth" type="string" required={false}>
      Image repository authentication ID for private images. String, length limit: 0-255 characters.
    </ParamField>

    <ParamField body="startCommand" type="string" required={false}>
      Startup command for the instance. String, length limit: 0-2047 characters.
    </ParamField>

    <ParamField body="entrypoint" type="string" required={false}>
      Instance startup entrypoint. This setting will override the Docker image's ENTRYPOINT. String, length limit: 0-2047 characters.
    </ParamField>

    <ParamField body="rootfsSize" type="integer" required={true}>
      Root filesystem storage (GB). Integer, value must be greater than 0.
    </ParamField>

    <ParamField body="ports" type="object[]" required={false}>
      Exposed port settings.

      <Expandable title="properties" defaultOpen={true}>
        <ParamField body="type" type="string" required={true}>
          Exposed port types.<br />
          Enum: `http`, `tcp`
        </ParamField>

        <ParamField body="ports" type="integer[]" required={true}>
          Exposed ports (maximum of 10). Supported port range: 1-65535, except for 2222, 2223, 2224 which are reserved for internal use.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="envs" type="object[]" required={false}>
      Environment variables injected into the instance. Up to 100 environment variable pairs can be created.

      <Expandable title="properties" defaultOpen={true}>
        <ParamField body="key" type="string" required={false}>
          Environment variable key. String, length limit: 0-511 characters.
        </ParamField>

        <ParamField body="value" type="string" required={false}>
          Environment variable value. String, length limit: 0-4095 characters.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="minCudaVersion" type="string" required={false}>
      Minimum supported CUDA version. String, length limit: 0-255 characters. Format example: 11.8, 12.4.
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="templateId" type="string" required={false}>
  ID of the created template.
</ResponseField>

## Example

Request

```bash  theme={"system"}

curl --request POST \
  --url 'https://api.novita.ai/gpu-instance/openapi/v1/template/create' \
  --header 'Authorization: Bearer {{API Key}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "template": {
      "name": "test",
      "readme": "readme",
      "type": "instance",
      "channel": "private",
      "readme": "test create template",
      "image": "nginx",
      "imageAuth": "",
      "startCommand": "echo test",
      "entrypoint": "",
      "rootfsSize": 60,
      "ports": [
        {
          "type": "http",
          "ports": [80, 443]
        },
        {
          "type": "tcp",
          "ports": [90, 95]
        }
      ],
      "envs": [
        {
          "key": "test1",
          "value": "template1"
        },
        {
          "key": "test2",
          "value": "test2"
        }
      ],
      "minCudaVersion": "11.8"
    }
  }'
```

Response

```json  theme={"system"}
{
  "templateId": "1"
}
```


Built with [Mintlify](https://mintlify.com).