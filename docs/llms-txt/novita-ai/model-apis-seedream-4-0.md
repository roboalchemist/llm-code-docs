# Source: https://novita.ai/docs/api-reference/model-apis-seedream-4-0.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedream 4.0

Seedream 4.0 is a cutting-edge image generation model that provides flexible image creation features, including 4K resolution support. The Seedream 4.0 API enables image generation from both text and other images.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="prompt" type="string" required={true}>
  The prompt for image generation.

  The recommended length is no more than 600 English words. If the prompt is too long, the information may become scattered. The model might ignore details and only concentrate on the main points, resulting in a image with missing elements.
</ParamField>

<ParamField body="images" type="string[]" required={false}>
  Enter the Base64 encoding or an accessible URL of the image to edit. Supports inputting a single image or multiple images.

  * Image URL: Make sure that the image URL is accessible.
  * Base64 encoding: The format must be `data:image/<image format>;base64,<Base64 encoding>`. <br />

    An input image must meet the following requirements:

    * Image format: jpeg, png
    * Aspect ratio (width/height): In the range \[1/3, 3]
    * Width and height (px): > 14
    * Size: No more than 10 MB
    * The value of total pixels: No more than 6000×6000
    * supports uploading a maximum of 10 reference images.
</ParamField>

<ParamField body="size" type="string" required={false}>
  Set the specification for the generated image. Two methods are available but cannot be used together.

  * Method 1, specify the resolution.
    * Optional values: `1K`, `2K`, `4K`
  * Method 2, specify the width and height of the generated image in pixels.
    * Default: `2048x2048`
    * The value range of total pixels: `[1024x1024, 4096x4096]`
    * The aspect ratio value range: `[1/16, 16]`

  Recommended width and height:

  | Aspect ratio | Width and Height Pixel Values |
  | ------------ | ----------------------------- |
  | 1:1          | 2048x2048                     |
  | 4:3          | 2304x1728                     |
  | 3:4          | 1728x2304                     |
  | 16:9         | 2560x1440                     |
  | 9:16         | 1440x2560                     |
  | 3:2          | 2496x1664                     |
  | 2:3          | 1664x2496                     |
  | 21:9         | 3024x1296                     |
</ParamField>

<ParamField body="sequential_image_generation" type="string" required={false} default="disabled">
  Controls whether to disable the batch generation feature.

  * `auto`: In automatic mode, the model automatically determines whether to return multiple images and how many images it will contain based on the user's prompt.
  * `disabled`: Disables batch generation feature. The model will only generate one image.
</ParamField>

<ParamField body="max_images" type="integer" required={false} default={15}>
  Specifies the maximum number of images to generate in this request. This parameter is only effective when `sequential_image_generation` is set to `auto`.

  Value range: `[1, 15]`

  <Tip>
    Description

    The actual number of generated images is affected by `max_images` and the number of input reference images. Number of input reference images + Number of generated images ≤ 15.
  </Tip>
</ParamField>

<ParamField body="watermark" type="boolean" required={false} default={true}>
  Adds a watermark to the generated image.

  * `false`: Does not add a watermark.
  * `true`: Adds a watermark with the text "AI generated" in the bottom-right corner of the image.
</ParamField>

## Response

<ResponseField name="images" type="string[]" required={false}>
  An array containing links to download the generated images.
</ResponseField>


Built with [Mintlify](https://mintlify.com).