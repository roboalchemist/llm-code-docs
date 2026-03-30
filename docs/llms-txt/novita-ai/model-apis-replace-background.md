# Source: https://novita.ai/docs/api-reference/model-apis-replace-background.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Replace Background

**Replace the background of images according to your prompt.**

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="extra" type="object" required={false}>
  Optional extra parameters for the request.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="response_image_type" type="string" required={false}>
      The returned image type. Default is png.Enum: `png, webp, jpeg`
    </ParamField>

    <ParamField body="enterprise_plan" type="object" required={false}>
      Dedicated Endpoints settings, which only take effect for users who have already subscribed to the [Dedicated Endpoints Documentation](/guides/model-apis-dedicated-endpoints).

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="enabled" type="boolean" required={false}>
          Set to true to schedule this task to use your Dedicated Endpoints's dedicated resources. Default is false.
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="image_file" type="string" required={true}>
  The base64 of original image, with a maximum resolution of 2048 x 2048 and a maximum file size of 30 Mb (width \<= 4096, height \<= 4096).
</ParamField>

## Response

<ResponseField name="image_file" type="string" required={false}>
  The Base64-encoded content of the returned image.
</ResponseField>

<ResponseField name="image_type" type="string" required={false}>
  The returned image type.<br />
  Enum: `png`, `webp`, `jpeg`
</ResponseField>

## Example

This API allows you to replace the background of images according to your prompt.

**Try it in [playground](https://novita.ai/playground#replace-background).**

`Request:`

```bash  theme={"system"}
curl --location --request POST 'https://api.novita.ai/v3/replace-background' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"prompt":"in a warehouse",
"image_file":"{{Base64 encoded image}}"
}'
```

HTTP status codes in the 2xx range indicate that the request has been successfully accepted. A status code of 400 means there is an error with the request parameters, while status codes in the 5xx range indicate internal server errors.

You can obtain the image URL in the `image_file` field of the response in base64 format.

`Response:`

```js  theme={"system"}
{
    "image_file": "{{Base64 encoded image}}",
    "image_type": "png"
}
```

<Frame>
  <img height="420" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/UseCase_replace_background01.png" />
</Frame>

<Frame>
  <img height="420" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/UseCase_replace_background02.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).