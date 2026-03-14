# Source: https://novita.ai/docs/api-reference/model-apis-text-to-image-v2-deprecated.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Text to Image V2

<Warning>
  **The Text-to-Image V2 API is deprecated and will be removed in the future. Please migrate to [Text-to-Image V3](/api-reference/model-apis-txt2img).**
</Warning>

## POST Text to Image V2

The text-to-image endpoint will return only a `task_id`. You should use the `task_id` to call the /v2/progress API endpoint to retrieve the image generation results. We will gradually phase out the V2 endpoints. It is recommended to use the V3 endpoints to generate images.

## Request Headers

<ParamField header="Authorization" type="string" required={true} />

## Request Body

<ParamField body="extra" type="object" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="enable_nsfw_detection" type="boolean" required={false}>
      When set to true, NSFW detection will be enabled, incurring an additional cost of \$0.0015 for each generated image.
    </ParamField>

    <ParamField body="nsfw_detection_level" type="integer" required={false}>
      \*\*\* 0 - Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols.\*\*\* 1 - Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols; Non-Explicit Nudity, Obstructed Intimate Parts, Kissing on the Lips.\*\*\* 2 - Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols; Non-Explicit Nudity, Obstructed Intimate Parts, Kissing on the Lips; Female Swimwear or Underwear, Male Swimwear or Underwear.<br />
      Enum: `0`, `1`, `2`
    </ParamField>

    <ParamField body="enable_progress_info" type="boolean¦null" required={false}>
      You will receive empty preview images if `enable_progress_info` is set to false.
    </ParamField>

    <ParamField body="response_image_type" type="string" required={false}>
      The format of the returned images; default: png<br />
      Enum: `png`, `jpeg`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Positive prompt words, separated by `,`. If you want to use LoRA, you can call the `/v3/model` endpoint with the parameter `filter.types=lora` to retrieve the `sd_name_in_api` field as the `model_name`. Remember that the format for LoRA models is `<lora:$sd_name:$weight>`.
</ParamField>

<ParamField body="negative_prompt" type="string" required={true}>
  Negative prompt words, separated by `,`.
</ParamField>

<ParamField body="sampler_name" type="string" required={true}>
  This denoising process is called sampling because Stable Diffusion generates a new sample image at each step.<br />
  Enum: `DPM++ 2M Karras`, `DPM++ SDE Karras`, `DPM++ 2M SDE Exponential`, `DPM++ 2M SDE Karras`, `Euler a`, `Euler`, `LMS`, `Heun`, `DPM2`, `DPM2 a`, `DPM++ 2S a`, `DPM++ 2M`, `DPM++ SDE`, `DPM++ 2M SDE`, `DPM++ 2M SDE Heun`, `DPM++ 2M SDE Heun Karras`, `DPM++ 2M SDE Heun Exponential`, `DPM++ 3M SDE`, `DPM++ 3M SDE Karras`, `DPM++ 3M SDE Exponential`, `DPM fast`, `DPM adaptive`, `LMS Karras`, `DPM2 Karras`, `DPM2 a Karras`, `DPM++ 2S a Karras`, `Restart`, `DDIM`, `PLMS`, `UniPC`
</ParamField>

<ParamField body="batch_size" type="integer" required={true}>
  The number of images generated in one single generation. Range: \[0, 8]
</ParamField>

<ParamField body="n_iter" type="integer" required={true}>
  The number of generations. Range: \[0, 8]
</ParamField>

<ParamField body="steps" type="integer" required={true}>
  Think of steps as iterations in the image creation process. Range: (0, 50]
</ParamField>

<ParamField body="cfg_scale" type="integer" required={true}>
  This setting determines how closely Stable Diffusion will adhere to your prompt. Range: (0, 30]
</ParamField>

<ParamField body="seed" type="integer" required={true}>
  A seed is a number from which Stable Diffusion generates noise.
</ParamField>

<ParamField body="height" type="integer" required={true}>
  Height of the image. Range: (0, 2048]
</ParamField>

<ParamField body="width" type="integer" required={true}>
  Width of the image. Range: (0, 2048]
</ParamField>

<ParamField body="model_name" type="string" required={true}>
  Name of the Stable Diffusion model. You can call the `/v3/model` endpoint with the parameter `filter.types=checkpoint` to retrieve the `sd_name_in_api` field as the `model_name`.
</ParamField>

<ParamField body="restore_faces" type="boolean" required={true}>
  Enable the Stable Diffusion face restoration plugin.
</ParamField>

<ParamField body="restore_faces_model" type="null" required={true} />

<ParamField body="sd_vae" type="string¦null" required={false}>
  VAE (Variational Auto Encoder). `sd_vae` can be accessed in the API /v3/model with query parameters `filter.types=vae` to retrieve the `sd_name` field as the `sd_vae`.
</ParamField>

<ParamField body="clip_skip" type="integer" required={false}>
  This parameter indicates the number of layers to stop from the bottom during optimization, so clip\_skip on 2 would mean, that in SD1.x model where the CLIP has 12 layers, you would stop at 10th layer.
</ParamField>

<ParamField body="enable_hr" type="boolean¦null" required={false}>
  Hires.fix function switch.
</ParamField>

<ParamField body="hr_upscaler" type="string¦null" required={false}>
  Upscalers model names. AI upscalers are models trained with massive amounts of data.<br />
  Enum: `Latent`, `ESRGAN_4x`, `R-ESRGAN 4x+`, `R-ESRGAN 4x+ Anime6B`
</ParamField>

<ParamField body="hr_scale" type="number¦null" required={false}>
  The magnification factor of the image, if params hr\_resize\_x and hr\_resize\_y are set, this parameter will be ignored.<br />
  Enum: `1`, `2`
</ParamField>

<ParamField body="hr_resize_x" type="integer¦null" required={false}>
  The target image width, the maximum image size is 2048, only take effect when parameters hr\_scale=1.
</ParamField>

<ParamField body="hr_resize_y" type="integer¦null" required={false}>
  The target image hight, the maximum image size is 2048, only take effect when parameters hr\_scale=1.
</ParamField>

<ParamField body="img_expire_ttl" type="integer¦null" required={false}>
  Image storage time (seconds). Range \[0, 604800]
</ParamField>

<ParamField body="sd_refiner" type="object¦null" required={false}>
  Refiner infos to enhances the image details.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="checkpoint" type="string" required={true}>
      Refiner checkpoint name. Currently only `sd_xl_refiner_1.0.safetensors` supported.<br />
      Enum: `sd_xl_refiner_1.0.safetensors`
    </ParamField>

    <ParamField body="switch_at" type="number" required={true}>
      weight of refiner, from 0 to 1.
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
      How to resize the input image so as to fit the output resolution of the generation. 0 represent JUST\_RESIZE, 1 represent RESIZE\_OR\_CORP, 2 represent RESIZE\_AND\_FILL<br />
      Enum: `0`, `1`, `2`
    </ParamField>

    <ParamField body="processor_res" type="integer" required={false}>
      Resolution of the preprocessor.
    </ParamField>

    <ParamField body="threshold_a" type="integer" required={false}>
      First parameter of the preprocessor, only takes effect when preprocessor accepts arguments.
    </ParamField>

    <ParamField body="threshold_b" type="integer" required={false}>
      Second parameter of the preprocessor, only takes effect when preprocessor accepts arguments.
    </ParamField>

    <ParamField body="guidance_start" type="number" required={false}>
      ratio of generation where this unit starts to have an effect.
    </ParamField>

    <ParamField body="guidance_end" type="number" required={false}>
      ratio of generation where this unit stops to have an effect.
    </ParamField>

    <ParamField body="pixel_perfect" type="boolean" required={false}>
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
curl --location 'https://api.novita.ai/v2/txt2img' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
  'extra': {
    'enable_nsfw_detection': false,
    'nsfw_detection_level': 0,
    'enable_progress_info': false
  },
  'prompt': 'Luxury suite design, Spacious suite area, Luxuriously plush large bed, Refined office desk, Carefully selected furniture for the luxurious suite, High-end and opulent decor, Private office and lounge area, Comfortably luxurious office chair, Amenities for luxury travelers, Premium bedding and linens, Uniquely designed lighting fixtures, Luxurious suite curtain design, Private work corner, Luxurious amenities, Lavish lounge area, Sophisticated indoor plant, decorations, Exquisite luxury design, Exclusive services for the luxury suite, Luxury color scheme. Exclusive furniture for the luxury suite, a bedroom with a large bed and a desk',
  'negative_prompt': '(badhandv4:1.2),(worst quality:2),(low quality:2),(normal quality:2),lowres,bad anatomy,bad hands,((monochrome)),((grayscale)) watermark,moles, easynegative ng_deepnegative_v1_75t, (oversized head:2), (big head:2), (deformed face:1.5),( blurry face:2), bad eyes, irregular eyes, asymmetric eyes, ugly, teeth, (navel:0.9), artefact, jpg artefact, blurry face, blurry, blurred, pixelated, bad eyes, crossed eyes, blurry eyes',
  'sampler_name': 'DPM++ 2M Karras',
  'batch_size': 1,
  'n_iter': 1,
  'steps': 25,
  'cfg_scale': 7,
  'seed': -1,
  'height': 512,
  'width': 512,
  'model_name': 'sd_xl_base_0.9.safetensors',
  'restore_faces': false,
  'restore_faces_model': '',
  'sd_vae': '',
  'clip_skip': 1,
  'enable_hr': false,
  'hr_upscaler': 'Latent',
  'hr_scale': 1,
  'hr_resize_x': null,
  'hr_resize_y': null,
  'img_expire_ttl': null,
  'sd_refiner': {
    'checkpoint': 'sd_xl_refiner_1.0.safetensors',
    'switch_at': null
  },
  'controlnet_units': [
    {
      'model': '',
      'weight': null,
      'input_image': '',
      'module': 'none',
      'control_mode': 0,
      'mask': '',
      'resize_mode': 0,
      'processor_res': null,
      'threshold_a': null,
      'threshold_b': null,
      'guidance_start': null,
      'guidance_end': null,
      'pixel_perfect': false
    }
  ]
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