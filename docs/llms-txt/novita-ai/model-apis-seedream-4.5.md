# Source: https://novita.ai/docs/api-reference/model-apis-seedream-4.5.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedream 4.5

API for the Seedream 4.5 image generation model, supporting text-to-image, single image-to-image, multi-image-to-image, and sequential image generation features.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="size" type="string" default="2048x2048">
  Specifies the size of the generated image. Method 1: Specify resolution (2K, 4K); Method 2: Specify width and height in pixels (e.g., 2048x2048). Total pixel range: \[3686400, 16777216], aspect ratio range: \[1/16, 16].
</ParamField>

<ParamField body="image" type="array">
  Array of input image information, supporting URL or Base64 encoding. Up to 14 reference images can be provided. Supported image formats: jpeg, png, webp, bmp, tiff, gif.

  Array length: 1 - 14
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  The prompt used to generate images, supporting both Chinese and English. Recommended not to exceed 300 Chinese characters or 600 English words.
</ParamField>

<ParamField body="watermark" type="boolean" default={true}>
  Whether to add a watermark to the generated images.
</ParamField>

<ParamField body="optimize_prompt_options" type="object">
  Configuration for the prompt optimization feature.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="mode" type="string" default="standard">
      Sets the mode for the prompt optimization feature. standard: Standard mode, higher quality but longer processing time; fast: Fast mode, shorter processing time but average quality. Currently only standard mode is supported.

      Optional values: `standard`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="sequential_image_generation" type="string" default="disabled">
  Controls whether to disable the sequential image generation feature. auto: Automatic mode, the model determines whether to return sequential images based on the prompt; disabled: Disables sequential image generation, only generates one image.

  Optional values: `auto`, `disabled`
</ParamField>

<ParamField body="sequential_image_generation_options" type="object">
  Configuration for the sequential image generation feature. Only effective when sequential\_image\_generation is set to auto.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="max_images" type="integer" default={15}>
      Specifies the maximum number of images that can be generated in this request. Number of input reference images + number of generated images ≤ 15.

      Value range: \[1, 15]
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="images" type="string[]" required={false}>
  Array of generated image information.
</ResponseField>


Built with [Mintlify](https://mintlify.com).