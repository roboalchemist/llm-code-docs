# Source: https://novita.ai/docs/api-reference/model-apis-image-to-image-v2-deprecated.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image to Image V2

<Warning>
  **The Image-to-Image V2 API is deprecated and will be removed in the future. Please migrate to [Image-to-Image V3](/api-reference/model-apis-img2img).**
</Warning>

## POST Image to Image V2

This is the image-to-image endpoint. Only a `task_id` will be returned. You should use the `task_id` to call the `/v2/progress` API endpoint in order to retrieve the image generation results. The output is provided in the format of "image/png". We will gradually phase out the V2 endpoints, and it is recommended to use the V3 endpoints to generate images.

## Request Headers

<ParamField header="Authorization" type="string" required={true} />

## Request Body

<ParamField body="extra" type="object" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="enable_nsfw_detection" type="boolean" required={false}>
      When set to true, NSFW detection will be enabled, incurring an additional cost of \$0.0015 for each generated image.
    </ParamField>

    <ParamField body="nsfw_detection_level" type="integer" required={false}>
      \*\*\* 0 - Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols. \*\*\* 1 - Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols; Non-Explicit Nudity, Obstructed Intimate Parts, Kissing on the Lips. \*\*\* 2 - Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols; Non-Explicit Nudity, Obstructed Intimate Parts, Kissing on the Lips; Female Swimwear or Underwear, Male Swimwear or Underwear.<br />
      Enum: `0`, `1`, `2`
    </ParamField>

    <ParamField body="enable_progress_info" type="boolean¦null" required={false}>
      You will receive empty preview images after setting enable\_progress\_info to false.
    </ParamField>

    <ParamField body="response_image_type" type="string" required={false}>
      The format of returned images, default: `png`<br />
      Enum: `png`, `jpeg`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="prompt" type="string¦null" required={true}>
  Positive prompt words, separated by commas. If you want to use LoRA, you can call the `/v3/model` endpoint with the parameter filter.types=lora to retrieve the `sd_name_in_api` field as the `model_name`. Remember that the format for LoRA models is `<lora:$sd_name:$weight>`.
</ParamField>

<ParamField body="negative_prompt" type="string¦null" required={false}>
  Negative prompt words, separated by commas.
</ParamField>

<ParamField body="sampler_name" type="string¦null" required={true}>
  This denoising process is called sampling because Stable Diffusion generates a new sample image at each step.<br />
  Enum: `DPM++ 2M Karras`, `DPM++ SDE Karras`, `DPM++ 2M SDE Exponential`, `DPM++ 2M SDE Karras`, `Euler a`, `Euler`, `LMS`, `Heun`, `DPM2`, `DPM2 a`, `DPM++ 2S a`, `DPM++ 2M`, `DPM++ SDE`, `DPM++ 2M SDE`, `DPM++ 2M SDE Heun`, `DPM++ 2M SDE Heun Karras`, `DPM++ 2M SDE Heun Exponential`, `DPM++ 3M SDE`, `DPM++ 3M SDE Karras`, `DPM++ 3M SDE Exponential`, `DPM fast`, `DPM adaptive`, `LMS Karras`, `DPM2 Karras`, `DPM2 a Karras`, `DPM++ 2S a Karras`, `Restart`, `DDIM`, `PLMS`, `UniPC`
</ParamField>

<ParamField body="batch_size" type="integer¦null" required={true}>
  Number of images generated in a single generation. Range: \[0, 8]
</ParamField>

<ParamField body="n_iter" type="integer¦null" required={true}>
  Number of generations. Range: \[0, 8]
</ParamField>

<ParamField body="steps" type="integer¦null" required={true}>
  Think of steps as iterations of the image creation process. Range: (0, 50]
</ParamField>

<ParamField body="cfg_scale" type="number¦null" required={true}>
  This setting indicates how closely Stable Diffusion will adhere to your prompt. Range: (0, 30]
</ParamField>

<ParamField body="seed" type="integer¦null" required={false}>
  A seed is a number from which Stable Diffusion generates noise.
</ParamField>

<ParamField body="height" type="integer" required={true}>
  Height of the image. Range: (0, 2048]
</ParamField>

<ParamField body="width" type="integer" required={true}>
  Width of the image. Range: (0, 2048]
</ParamField>

<ParamField body="model_name" type="string" required={true}>
  Name of the stable diffusion model. You can call the `/v3/model` endpoint with the parameter filter.types=checkpoint to retrieve the `sd_name_in_api` field as the `model_name`.
</ParamField>

<ParamField body="init_images" type="string[]" required={true} />

<ParamField body="denoising_strength" type="number¦null" required={false}>
  Indicates how much to transform the reference init\_images. Must be between 0 and 1. init\_images will be used as a starting point, with more noise added as the strength increases. The number of denoising steps depends on the amount of noise initially added. When denoising\_strength is 1, added noise will be maximum, and the denoising process will run for the full number of iterations specified in steps. A value of 1, therefore, essentially ignores init\_images.
</ParamField>

<ParamField body="restore_faces" type="boolean¦null" required={false}>
  Enable Stable Diffusion restore faces plugin.
</ParamField>

<ParamField body="sd_vae" type="string¦null" required={false}>
  VAE(Variational Auto Encoder),sd\_vae can be access in api /v3/model with query params filter.types=vae to retrieve the `sd_name` field as the `sd_vae`.
</ParamField>

<ParamField body="clip_skip" type="integer¦null" required={false}>
  This parameter indicates the number of layers to stop from the bottom during optimization, so clip\_skip on 2 would mean, that in SD1.x model where the CLIP has 12 layers, you would stop at 10th layer.
</ParamField>

<ParamField body="mask" type="string" required={false}>
  Base64 of png, mask of inpaintings.
</ParamField>

<ParamField body="mask_blur" type="integer" required={false}>
  Sets the degree of blurring of the border of the filled area.
</ParamField>

<ParamField body="resize_mode" type="integer¦null" required={false}>
  Resize mode, while, 0 represent Just resize, 1 represent Crop and resize, 2 represent Resize and fill, 3 represent Just resize(latent upscale)<br />
  Enum: `0`, `1`, `2`, `3`
</ParamField>

<ParamField body="image_cfg_scale" type="integer¦null" required={false}>
  Image cfg scale
</ParamField>

<ParamField body="inpainting_fill" type="integer¦null" required={false}>
  How to redraw the filled areas. 0: fill,  Redraw based on the surrounding color 1: original,  Redraw based on the original image 2: latent noise,  Change back to noise and redraw 3: latent nothing, based on the color of the filled area<br />
  Enum: `0`, `1`, `2`, `3`
</ParamField>

<ParamField body="inpaint_full_res" type="integer¦null" required={false}>
  Specify whether to apply or protect the filled area. 0: Whole picture the entire illustration and change the filled parts. 1: Only masked Draws only the filled area and then restores the original image.<br />
  Enum: `0`, `1`
</ParamField>

<ParamField body="inpaint_full_res_padding" type="integer¦null" required={false}>
  This settings controls how many additional pixels can be used as a reference point for only masked mode. You can increase the amount if you are having trouble with producing a proper image. This is a numerical value for how much margin to set when Only masked is selected. The downside of increasing this value is that it will decrease the quality of output. Guidance: [https://civitai.com/articles/161/basic-inpainting-guide](https://civitai.com/articles/161/basic-inpainting-guide)
</ParamField>

<ParamField body="inpainting_mask_invert" type="integer" required={false}>
  Specify whether to invert the mask. 0 - Inpaint Masked 1 - Inpaint Not Masked<br />
  Enum: `0`, `1`
</ParamField>

<ParamField body="initial_noise_multiplier" type="number" required={false}>
  Noise multiplier for img2img in settings. This scaling factor is applied to the random latent tensor for img2img. Lowering it reduces flickering.
</ParamField>

<ParamField body="img_expire_ttl" type="integer" required={false}>
  Image storage time (seconds). Range \[0, 604800]
</ParamField>

<ParamField body="sd_refiner" type="object" required={false}>
  Refiner infos to enhances the image details.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="checkpoint" type="string" required={true}>
      Refiner checkpoint name. Currently only `sd_xl_refiner_1.0.safetensors` supported.<br />
      Enum: `sd_xl_refiner_1.0.safetensors`
    </ParamField>

    <ParamField body="switch_at" type="number" required={true}>
      Weight of refiner. From 0 to 1
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="controlnet_units" type="object[]¦null" required={false}>
  ControlNet.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="model" type="string" required={true}>
      Model to use on the image passed to this unit before using it for conditioning. \*\*\*Controlnets for SD 1.5: control\_v11e\_sd15\_ip2p, control\_v11e\_sd15\_shuffle, control\_v11f1e\_sd15\_tile, control\_v11f1p\_sd15\_depth, control\_v11p\_sd15\_canny, control\_v11p\_sd15\_inpaint, control\_v11p\_sd15\_lineart, control\_v11p\_sd15\_mlsd, control\_v11p\_sd15\_normalbae, control\_v11p\_sd15\_openpose, control\_v11p\_sd15\_scribble, control\_v11p\_sd15\_seg, control\_v11p\_sd15\_softedge, control\_v11p\_sd15s2\_lineart\_anime, ip-adapter-plus-face\_sd15, ip-adapter\_sd15\_plus, ip-adapter\_sd15; \*\*\*Controlnets for SDXL: t2i-adapter\_diffusers\_xl\_canny, t2i-adapter\_diffusers\_xl\_depth\_midas, t2i-adapter\_diffusers\_xl\_depth\_zoe, t2i-adapter\_diffusers\_xl\_lineart, t2i-adapter\_diffusers\_xl\_openpose, t2i-adapter\_diffusers\_xl\_sketch, t2i-adapter\_xl\_canny, t2i-adapter\_xl\_openpose, t2i-adapter\_xl\_sketch, ip-adapter\_xl
    </ParamField>

    <ParamField body="weight" type="number¦null" required={true}>
      weight of this unit. defaults to 1
    </ParamField>

    <ParamField body="input_image" type="string" required={true}>
      base64 of input image
    </ParamField>

    <ParamField body="module" type="string" required={true}>
      preprocessor to use on the image passed to this unit before using it for conditioning.<br />
      Enum: `none`, `canny`, `depth`, `depth_leres`, `depth_leres++`, `hed`, `hed_safe`, `mediapipe_face`, `mlsd`, `normal_map`, `openpose`, `openpose_hand`, `openpose_face`, `openpose_faceonly`, `openpose_full`, `clip_vision`, `color`, `pidinet`, `pidinet_safe`, `pidinet_sketch`, `pidinet_scribble`, `scribble_xdog`, `scribble_hed`, `segmentation`, `threshold`, `depth_zoe`, `normal_bae`, `oneformer_coco`, `oneformer_ade20k`, `lineart`, `lineart_coarse`, `lineart_anime`, `lineart_standard`, `shuffle`, `tile_resample`, `invert`, `lineart_anime_denoise`, `reference_only`, `reference_adain`, `reference_adain+attn`, `inpaint`, `inpaint_only`, `inpaint_only+lama`, `tile_colorfix`, `tile_colorfix+sharp`, `depth_anything`
    </ParamField>

    <ParamField body="control_mode" type="integer¦null" required={true}>
      0 for Balanced,1 for My prompt is more important 2 for ControlNet is more important<br />
      Enum: `0`, `1`, `2`
    </ParamField>

    <ParamField body="mask" type="string¦null" required={false}>
      Base64 of mask images, support jpg, jpeg and png format images. Only take effect when controlnet\_units.model set to control\_v11p\_sd15\_inpaint.
    </ParamField>

    <ParamField body="resize_mode" type="integer¦null" required={false}>
      How to resize the input image so as to fit the output resolution of the generation.<br />
      Enum: `0`, `1`, `2`
    </ParamField>

    <ParamField body="processor_res" type="integer¦null" required={false}>
      Resolution of the preprocessor.
    </ParamField>

    <ParamField body="threshold_a" type="integer¦null" required={false}>
      First parameter of the preprocessor, only takes effect when preprocessor accepts arguments.
    </ParamField>

    <ParamField body="threshold_b" type="integer¦null" required={false}>
      Second parameter of the preprocessor, only takes effect when preprocessor accepts arguments.
    </ParamField>

    <ParamField body="guidance_start" type="number¦null" required={false}>
      ratio of generation where this unit starts to have an effect.
    </ParamField>

    <ParamField body="guidance_end" type="number¦null" required={false}>
      ratio of generation where this unit stops to have an effect.
    </ParamField>

    <ParamField body="pixel_perfect" type="boolean¦null" required={false}>
      Enable pixel-perfect preprocessor, when set to false, it means not to resize images.
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="code" type="integer" required={false} />

<ResponseField name="msg" type="string" required={false} />

<ResponseField name="data" type="object" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="task_id" type="string" required={false} />

    <ResponseField name="warn" type="string" required={false} />
  </Expandable>
</ResponseField>

## Example

request

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v2/img2img' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
  'extra': {
    'enable_nsfw_detection': false,
    'nsfw_detection_level': 0,
    'enable_progress_info': false
  },
  'prompt': 'Photographic of a woman sitting at a cafe. 35mm photograph, film, bokeh, professional, 4k, highly detailed',
  'negative_prompt': 'ng_deepnegative_v1_75t, badhandv4, (worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)), ((grayscale)), watermark',
  'sampler_name': 'Euler a',
  'batch_size': 1,
  'n_iter': 1,
  'steps': 20,
  'cfg_scale': 7,
  'seed': -1,
  'height': 1024,
  'width': 1024,
  'model_name': 'sd_xl_base_1.0.safetensors',
  'init_images': [
    '{{base64 encoded image}}'
  ],
  'denoising_strength': 0.5,
  'restore_faces': false,
  'sd_vae': 'sdxl_vae.safetensors',
  'clip_skip': 1,
  'mask': '',
  'mask_blur': null,
  'resize_mode': 0,
  'image_cfg_scale': null,
  'inpainting_fill': 0,
  'inpaint_full_res': 0,
  'inpaint_full_res_padding': null,
  'inpainting_mask_invert': 0,
  'initial_noise_multiplier': null,
  'img_expire_ttl': null,
  'sd_refiner': {
    'checkpoint': 'sd_xl_refiner_1.0.safetensors',
    'switch_at': 1
  },
  'controlnet_units': [
    {
      'model': 't2i-adapter_xl_sketch',
      'weight': 0.5,
      'input_image': '{{base64 encoded image}}',
      'module': 'none',
      'control_mode': 0,
      'mask': '',
      'resize_mode': 0,
      'processor_res': null,
      'threshold_a': null,
      'threshold_b': null,
      'guidance_start': null,
      'guidance_end': null,
      'pixel_perfect': false,
      'lowvram': true
    }
  ],
  'controlnet_no_detectmap': true
}'
```

response

```json  theme={"system"}
{
  "code": 0,
  "msg": "",
  "data": {
    "task_id": "d4cf3973-8414-4a5e-aa6f-ef54caf73662"
  }
}
```


Built with [Mintlify](https://mintlify.com).