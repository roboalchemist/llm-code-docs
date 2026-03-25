# Source: https://novita.ai/docs/api-reference/model-apis-inpainting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Inpainting

**Inpainting is a conservation process in which damaged, deteriorated, or missing parts of an artwork are filled in to present a complete image.**

> This is an **asynchronous** API; only the **task\_id** will be returned. You should use the **task\_id** to request the [**Task Result API**](/api-reference/model-apis-task-result) to retrieve the image generation results.

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
      The returned image type. Default is png.<br />
      Enum: `png`, `webp`, `jpeg`
    </ParamField>

    <ParamField body="webhook" type="object" required={false}>
      Webhook settings. More details can be found at [Webhook Documentation](/api-reference/model-apis-webhook).

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="url" type="string" required={true}>
          The URL of the webhook endpoint. Novita AI will send the task generated outputs to your specified webhook endpoint.
        </ParamField>

        <ParamField body="test_mode" type="object" required={false}>
          By specifying Test Mode, a mock event will be sent to the webhook endpoint.

          <Expandable title="properties" defaultOpen={false}>
            <ParamField body="enabled" type="boolean" required={true}>
              Set to true to enable Test Mode, or false to disable it. The default is false.
            </ParamField>

            <ParamField body="return_task_status" type="string" required={true}>
              Control the data content of the mock event. When set to TASK\_STATUS\_SUCCEED, you'll receive a normal response; when set to TASK\_STATUS\_FAILED, you'll receive an error response.<br />
              Enum: `TASK_STATUS_SUCCEED`, `TASK_STATUS_FAILED`
            </ParamField>
          </Expandable>
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="custom_storage" type="object" required={false}>
      Customer storage settings for saving the generated outputs. <br /> By default, the generated outputs will be saved to Novita AI Storage temporarily and privately.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="aws_s3" type="object" required={false}>
          AWS S3 Bucket settings.

          <Expandable title="properties" defaultOpen={false}>
            <ParamField body="region" type="string" required={true}>
              AWS S3 regions, <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html" target="_blank">more details</a>.
            </ParamField>

            <ParamField body="bucket" type="string" required={true}>
              AWS S3 bucket name.
            </ParamField>

            <ParamField body="path" type="string" required={true}>
              AWS S3 bucket path for saving generated outputs.
            </ParamField>

            <ParamField body="save_to_path_directly" type="boolean" required={false}>
              Set this option to True to save the generated outputs directly to the specified path without creating any additional directory hierarchy. <br /> If set to False, Novita AI will create an additional directory in the path to save the generated outputs. The default is False.
            </ParamField>
          </Expandable>
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="enterprise_plan" type="object" required={false}>
      Dedicated Endpoints settings, which only take effect for users who have already subscribed to the [Dedicated Endpoints Documentation](/guides/model-apis-dedicated-endpoints).

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="enabled" type="boolean" required={false}>
          Set to true to schedule this task to use your Dedicated Endpoints's dedicated resources. Default is false.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="enable_nsfw_detection" type="boolean" required={false}>
      When set to true, NSFW detection will be enabled, incurring an additional cost of \$0.0015 for each generated image.
    </ParamField>

    <ParamField body="nsfw_detection_level" type="integer" required={false}>
      0: Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols.<br /> 1: Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols; Non-Explicit Nudity, Obstructed Intimate Parts, Kissing on the Lips.<br /> 2: Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols; Non-Explicit Nudity, Obstructed Intimate Parts, Kissing on the Lips; Female Swimwear or Underwear, Male Swimwear or Underwear.<br />
      Enum: `0`, `1`, `2`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="request" type="object" required={true}>
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="model_name" type="string" required={true}>
      This parameter specifies the name of the model checkpoint. Retrieve the corresponding sd\_name value by invoking the <a href="/api-reference/model-apis-get-model" target="_blank">Query Model</a> API with filter.types=checkpoint\&filter.is\_inpainting=true as the query parameter.
    </ParamField>

    <ParamField body="image_base64" type="string" required={true}>
      The base64 representation of the original image, with a maximum resolution of 16 megapixels and a maximum file size of 30 Mb.
    </ParamField>

    <ParamField body="mask_image_base64" type="string" required={true}>
      The base64 representation of the mask image, with a maximum resolution of 16 megapixels and a maximum file size of 30 Mb. The mask image should have the same resolution as the original image.
    </ParamField>

    <ParamField body="prompt" type="string" required={true}>
      Text input required to guide the image generation, divided by `,` . Range \[1, 1024].
    </ParamField>

    <ParamField body="image_num" type="integer" required={true}>
      Images numbers generated in one single generation. Range \[1, 8].
    </ParamField>

    <ParamField body="steps" type="integer" required={true}>
      The number of denoising steps. More steps usually can produce higher quality images, but take more time to generate, Range \[1, 100].
    </ParamField>

    <ParamField body="guidance_scale" type="number" required={true}>
      This setting says how close the Stable Diffusion will listen to your prompt, higer guidance forces the model to better follow the prompt, but result in lower quality output. Range \[1, 30].
    </ParamField>

    <ParamField body="sampler_name" type="string" required={true}>
      This parameter determines the denoising algorithm employed during the sampling phase of Stable Diffusion. Each option represents a distinct method by which the model incrementally generates new images. These algorithms differ significantly in their processing speed, output quality, and the specific characteristics of the images they generate, allowing users to tailor the image generation process to meet precise requirements. Get reference at [A brief introduction to Sampler](/guides/model-apis-sampler).<br />
      Enum: `Euler a`, `Euler`, `LMS`, `Heun`, `DPM2`, `DPM2 a`, `DPM++ 2S a`, `DPM++ 2M`, `DPM++ SDE`, `DPM fast`, `DPM adaptive`, `LMS Karras`, `DPM2 Karras`, `DPM2 a Karras`, `DPM++ 2S a Karras`, `DPM++ 2M Karras`, `DPM++ SDE Karras`, `DDIM`, `PLMS`, `UniPC`
    </ParamField>

    <ParamField body="mask_blur" type="integer" required={false}>
      Defines the degree of border blurring for the filled area. A lower value results in a sharper border, maintaining clear delineation between masked and unmasked areas. Conversely, a higher value increases the blur effect, creating a smoother, more blended transition at the borders. This adjustment allows for greater control over the visual integration of the mask with the original image. Range \[0, 64].
    </ParamField>

    <ParamField body="negative_prompt" type="string" required={false}>
      Text input that specifies what to exclude from the generated images, divided by `,` . Range \[1, 1024].
    </ParamField>

    <ParamField body="sd_vae" type="string" required={false}>
      VAE (Variational Auto Encoder). The sd\_vae can be accessed in the API /v3/models with query parameters type=vae, such as sd\_name: customVAE.safetensors. Get reference at [A brief introduction to VAE](/guides/model-apis-vae).
    </ParamField>

    <ParamField body="seed" type="integer" required={false}>
      A seed is a number from which Stable Diffusion generates noise, which, makes generation deterministic. Using the same seed and set of parameters will produce identical image each time, minimum -1. Defaults to -1.
    </ParamField>

    <ParamField body="loras" type="object[]" required={false}>
      LoRA is a fast and lightweight training method that inserts and trains a significantly smaller number of parameters instead of all the model parameters. Currently supports up to 5 LoRAs.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="model_name" type="string" required={true}>
          Name of lora, retrieve the corresponding sd\_name\_in\_api value by invoking the <a href="/api-reference/model-apis-get-model">Get Model API</a> endpoint with filter.types=lora as the query parameter.
        </ParamField>

        <ParamField body="strength" type="number" required={true}>
          The strength value of lora. The larger the value, the more biased the effect is towards lora, Range \[0, 1]
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="embeddings" type="object[]" required={false}>
      Textual Inversion is a training method for personalizing models by learning new text embeddings from a few example images, currently supports up to 5 embeddings.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="model_name" type="string" required={true}>
          Name of textual Inversion model, you can call the <a href="/api-reference/model-apis-get-model">Get Model API</a> endpoint with parameter filter.types=textualinversion to retrieve the sd\_name\_in\_api field as the model\_name.
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="clip_skip" type="integer" required={false}>
      This parameter indicates the number of layers to stop from the bottom during optimization, so clip\_skip on 2 would mean, that in SD1.x model where the CLIP has 12 layers, you would stop at 10th layer, Range \[1, 12], get reference at [A brief introduction to Clip Skip](/guides/model-apis-clip-skip).
    </ParamField>

    <ParamField body="strength" type="number(float)¦null" required={false}>
      Conceptually, the `strength` indicates the degree to which the reference `image_base64` should be transformed. Must be between 0 and 1. `image_base64` will be used as a starting point, with increasing levels of noise added as the strength value increases. The number of denoising steps depends on the amount of noise initially added. When `strength` is 1, added noise will be maximum and the denoising process will run for the full number of iterations specified in `steps`. A value of 1, therefore, essentially ignores `image_base64`.
    </ParamField>

    <ParamField body="inpainting_full_res" type="integer" required={false}>
      Specifies whether to apply or protect the filled area. When set to 0, the inpainting process considers the entire image, which may result in the mask area failing to present the correct details, but the mask area will look more natural or blend better with the whole image. When set to 1, only the masked area is inpainted, ignoring the unmasked areas, which can produce more detailed and natural results within the mask but may appear strange or incompatible with the original background. Default is 0.<br />
      Enum: `0`, `1`
    </ParamField>

    <ParamField body="inpainting_full_res_padding" type="integer" required={false}>
      This setting controls how many additional pixels can be used as a reference point for only masked mode. You can increase this amount if you are having trouble producing a proper image. This is a numerical value for how much margin to set when Only masked is selected. The downside of increasing this value is that it may decrease the quality of the output. Guidance: [https://civitai.com/articles/161/basic-inpainting-guide](https://civitai.com/articles/161/basic-inpainting-guide), Range \[0, 256]. Default is 8.
    </ParamField>

    <ParamField body="inpainting_mask_invert" type="integer" required={false}>
      Specifies whether to invert the mask. Set to 1 to invert the mask. Default is 0.<br />
      Enum: `0`, `1`
    </ParamField>

    <ParamField body="initial_noise_multiplier" type="number" required={false}>
      Noise multiplier for img2img settings. This scaling factor is applied to the random latent tensor for img2img. Lowering the value of this multiplier reduces the amount of noise introduced into the image transformation process, which can help reduce flickering or instability in the output image. Range \[0, 1.5]. Default is 0.5.
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={false}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

### I have no `mask` images. How do I generate `mask` parameters in the body?

You can use our playground to get the mask base64 information. Please be aware that mask images should have the same resolution as the input images. Guidance can be found here: [Click Here](https://novita.ai/playground#inpainting)

<Frame>
  <img height="410" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/inpainting-01.jpg" />
</Frame>

### I already have mask images. How do I convert `mask` images to base64?

You can use the following code to convert mask images to base64.

```python  theme={"system"}
import base64
# mask files path
filename_input = "mask_edited.png"

# read mask file
with open(filename_input, "rb") as f:
    base64_pic = base64.b64encode(f.read()).decode("utf-8")

# write mask file
with open("input.txt", "w") as f:
    f.write(base64_pic)
```

### Start requesting inpainting.

Please set the **`Content-Type`** header to **`application/json`** in your HTTP request to indicate that you are sending JSON data. Currently, **only JSON format is supported**.

`"model_name":"realisticVisionV40_v40VAE-inpainting_81543.safetensors"` in body represent inpainting models, which, can be accessed in API /v3/model with `sd_name` like %inpainting%.

`Request:`

```bash  theme={"system"}
curl --location --request POST 'http://api.novita.ai/v3/async/inpainting' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API Key}}' \
--data-raw '{
    "extra": {
        "response_image_type": "jpeg"
    },
    "request": {
        "model_name": "realisticVisionV40_v40VAE-inpainting_81543.safetensors",
        "prompt": "Leonardo DiCaprio",
        "negative_prompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime), text, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, BadDream, UnrealisticDream",
        "image_num": 1,
        "steps": 25,
        "seed": -1,
        "clip_skip": 1,
        "guidance_scale": 7.5,
        "sampler_name": "Euler a",
        "mask_blur": 1,
        "inpainting_full_res": 1,
        "inpainting_full_res_padding": 32,
        "inpainting_mask_invert": 0,
        "initial_noise_multiplier": 1,
        "strength": 0.85,
        "image_base64": "{{base64 encoded image}}",
        "mask_image_base64": "{{base64 encoded mask image}}"
    }
}'
```

`Response:`

`````js  theme={"system"}
{
    "code": 0,
    "msg": "",
    "data": {
        "task_id": "270f4fba-2cb0-4a56-8b82-xxxx"
    }
}
````"model_name":"realisticVisionV40_v40VAE-inpainting_81543.safetensors"` in body represent inpainting models, which, can be accessed in API /v3/model with `sd_name` like %inpainting%.

`Request:`
```bash
curl --location --request POST 'http://api.novita.ai/v3/async/inpainting' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API Key}}' \
--data-raw '{
    "extra": {
        "response_image_type": "jpeg"
    },
    "request": {
        "model_name": "realisticVisionV40_v40VAE-inpainting_81543.safetensors",
        "prompt": "Leonardo DiCaprio",
        "negative_prompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime), text, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, BadDream, UnrealisticDream",
        "image_num": 1,
        "steps": 25,
        "seed": -1,
        "clip_skip": 1,
        "guidance_scale": 7.5,
        "sampler_name": "Euler a",
        "mask_blur": 1,
        "inpainting_full_res": 1,
        "inpainting_full_res_padding": 32,
        "inpainting_mask_invert": 0,
        "initial_noise_multiplier": 1,
        "strength": 0.85,
        "image_base64": "{{base64 encoded image}}",
        "mask_image_base64": "{{base64 encoded mask image}}"
    }
}'
`````

`Response:`

```js  theme={"system"}
{
    "code": 0,
    "msg": "",
    "data": {
        "task_id": "270f4fba-2cb0-4a56-8b82-xxxx"
    }
}
```


Built with [Mintlify](https://mintlify.com).