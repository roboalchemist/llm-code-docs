# Source: https://novita.ai/docs/api-reference/model-apis-seedream-3-0-t2i.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedream 3.0 Text to Image

Experience fast and efficient image generation with Seedream 3.0, a state-of-the-art text-to-image model that produces high-quality images from textual prompts.

<Tip>
  Currently, only the model version `seedream-3-0-t2i-250415` is supported for Seedream 3.0.
</Tip>

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="prompt" type="string" required={true}>
  The text prompt used to generate the image.
</ParamField>

<ParamField body="model" type="string" required={false}>
  The Model ID or inference endpoint (Endpoint ID) to be used for this request. Currently, only `seedream-3-0-t2i-250415` for seedream 3.0 is supported.
</ParamField>

<ParamField body="response_format" type="string" required={false}>
  Specifies the format of the generated image returned in the response. Default is `url`.<br />
  Supported values:<br />

  * `"url"`: Returns a downloadable JPEG image link.
  * `"b64_json"`: Returns the image data as a Base64-encoded JSON string.
</ParamField>

<ParamField body="size" type="string" required={false}>
  Specifies the dimensions (width x height in pixels) of the generated image. Must be between \[512x512, 2048x2048]. Default is `1024x1024`.<br />
  Recommended aspect ratios and resolutions:<br />

  * `1024x1024` (1:1)
  * `864x1152` (3:4)
  * `1152x864` (4:3)
  * `1280x720` (16:9)
  * `720x1280` (9:16)
  * `832x1248` (2:3)
  * `1248x832` (3:2)
  * `1512x648` (21:9)
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  Random seed to control the stochasticity of image generation. Range: \[-1, 2147483647]. If not specified, a seed will be automatically generated. To reproduce the same output, use the same seed value. Default is `-1`.
</ParamField>

<ParamField body="guidance_scale" type="number" required={false}>
  Controls how closely the output image aligns with the input prompt. The higher the value, the less freedom the model has, and the stronger the prompt correlation. Range: \[1, 10]. Default is `2.5`.
</ParamField>

<ParamField body="watermark" type="boolean" required={false}>
  Specifies whether to add a watermark to the generated image. Default is `true`.<br />

  * `false`: No watermark.
  * `true`: Adds a watermark with the label "AI generated" in the bottom-right corner.
</ParamField>

## Response

<ResponseField name="image_urls" type="string[]" required={false}>
  Array of generated image URLs. When `response_format` is set to `"url"`, this array contains the downloadable image links for the generated images.
</ResponseField>

<ResponseField name="binary_data_base64" type="string[]" required={false}>
  Array of Base64-encoded image data. When `response_format` is set to `"b64_json"`, this array contains the generated images as Base64-encoded JSON strings.
</ResponseField>


Built with [Mintlify](https://mintlify.com).