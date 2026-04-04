# Source: https://novita.ai/docs/api-reference/model-apis-img2img.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image to Image

**Generate images with Stable Diffusion Models from Image and Text Prompts.**

> This is an **asynchronous API**; only the **task\_id** is returned initially. Use this **task\_id** to query the [**Task Result API**](/api-reference/model-apis-task-result) to retrieve the results of the image generation.

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
      0: Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols.<br /> 1: Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols; Non-Explicit Nudity, Obstructed Intimate Parts, Kissing on the Lips.<br /> 2: Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols; Non-Explicit Nudity, Obstructed Intimate Parts, Kissing on the Lips; Female Swimwear or Underwear, Male Swimwear or Underwear.
      Enum: `0`, `1`, `2`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="request" type="object" required={true}>
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="model_name" type="string" required={true}>
      This parameter specifies the name of the model checkpoint. Retrieve the corresponding sd\_name value by invoking the <a href="/api-reference/model-apis-get-model" target="_blank">Query Model</a> API with filter.types=checkpoint as the query parameter.
    </ParamField>

    <ParamField body="image_base64" type="string" required={true}>
      The base64 of original image, with a maximum resolution of 16 megapixels and a maximum file size of 10 Mb.
    </ParamField>

    <ParamField body="prompt" type="string" required={true}>
      Text input required to guide the image generation, divided by `,` . Range \[1, 1024].
    </ParamField>

    <ParamField body="width" type="integer" required={true}>
      Width of image. Range \[128, 2048].
    </ParamField>

    <ParamField body="height" type="integer" required={true}>
      Height of image. Range \[128, 2048].
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

    <ParamField body="negative_prompt" type="string" required={false}>
      Text input that specifies what to exclude from the generated images, divided by `,` . Range \[1, 1024].
    </ParamField>

    <ParamField body="sd_vae" type="string" required={false}>
      VAE (Variational Auto Encoder). sd\_vae can be accessed in the API /v3/models with query params type=vae, like sd\_name: customVAE.safetensors. Get reference at [A Brief Introduction to VAE](/guides/model-apis-vae).
    </ParamField>

    <ParamField body="controlnet" type="object" required={false}>
      The ControlNet configuration provides a greater degree of control over text-to-image generation by conditioning the model on additional inputs such as edge maps, depth maps, segmentation maps, and keypoints for pose detection.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="units" type="object[]" required={true}>
          <Expandable title="properties" defaultOpen={true}>
            <ParamField body="model_name" type="string" required={true}>
              Preprocessor to use on the image passed to this unit before using it for conditioning. \*\*\*ControlNets for SD 1.5: control\_v11e\_sd15\_ip2p, control\_v11e\_sd15\_shuffle, control\_v11f1e\_sd15\_tile, control\_v11f1p\_sd15\_depth, control\_v11p\_sd15\_canny, control\_v11p\_sd15\_inpaint, control\_v11p\_sd15\_lineart, control\_v11p\_sd15\_mlsd, control\_v11p\_sd15\_normalbae, control\_v11p\_sd15\_openpose, control\_v11p\_sd15\_scribble, control\_v11p\_sd15\_seg, control\_v11p\_sd15\_softedge, control\_v11p\_sd15s2\_lineart\_anime, control\_v1p\_sd15\_brightness, control\_v1p\_sd15\_qrcode\_monster, control\_v1p\_sd15\_qrcode\_monster\_v2, \*\*\*ControlNets for SDXL: controlnet-canny-sdxl-1.0, controlnet-depth-sdxl-1.0, controlnet-openpose-sdxl-1.0, controlnet-softedge-sdxl-1.0
            </ParamField>

            <ParamField body="image_base64" type="string" required={true}>
              base64 of input controlNet image
            </ParamField>

            <ParamField body="strength" type="number" required={true}>
              The strength of this unit, defaults to 1. Range \[0, 1]; the larger the value, the more biased the effect is towards ControlNet.
            </ParamField>

            <ParamField body="preprocessor" type="string" required={false}>
              Preprocessor to use on the image passed to this unit before using it for conditioning.<br />
              Enum: `scribble_hed`, `softedge_hed`, `scribble_hedsafe`, `softedge_hedsafe`, `depth_midas`, `mlsd`, `openpose`, `openpose_face`, `openpose_faceonly`, `openpose_full`, `openpose_hand`, `dwpose`, `scribble_pidinet`, `softedge_pidinet`, `scribble_pidsafe`, `softedge_pidsafe`, `normal_bae`, `lineart_coarse`, `lineart_realistic`, `lineart_anime`, `lineart`, `depth_zoe`, `shuffle`, `mediapipe_face`, `canny`, `depth`, `depth_leres`, `depth_leres++`
            </ParamField>

            <ParamField body="guidance_start" type="number" required={false}>
              Ratio of generation where this unit starts to impact the process. Range \[0, 1].
            </ParamField>

            <ParamField body="guidance_end" type="number" required={false}>
              Ratio of generation where this unit stops impacting the process. Range \[0, 1].
            </ParamField>
          </Expandable>
        </ParamField>
      </Expandable>
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

    <ParamField body="ip_adapters" type="object[]" required={false}>
      IP-Adapter is an image prompt adapter that can be plugged into diffusion models to enable image prompting without any changes to the underlying model. Furthermore, adapter can be reused with other models finetuned from the same base model and it can be combined with other adapters like ControlNet, currenlty supports up to 1 IP-Adapter.

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="model_name" type="string" required={true}>
          IP-Adapter model name, if the base model of your checkpoint is SDXL, then you should select ip-adapter\_sdxl.bin. Alternatively, if the base model of your checkpoint is SD1.x, then you should select ip-adapter\_sd15.bin.<br />
          Enum: `ip-adapter_sd15.bin`, `ip-adapter_sdxl.bin`
        </ParamField>

        <ParamField body="image_base64" type="string" required={true}>
          The base64 decoded content for input image.
        </ParamField>

        <ParamField body="strength" type="number(float)" required={true}>
          Range \[0, 1], this value represents the strength of this unit. The larger the value, the more pronounced the effect of the IP-Adapter becomes.
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={false}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

### 1. Image to image request with normal parameter.

Please set the **`Content-Type`** header to **`application/json`** in your HTTP request to indicate that you are sending JSON data. Currently, **only JSON format is supported**.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/img2img' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "extra": {
        "response_image_type": "jpeg"
    },
    "request": {
        "model_name": "sd_xl_base_1.0.safetensors",
        "prompt": "a cute dog",
        "negative_prompt": "",
        "height": 512,
        "width": 384,
        "image_num": 1,
        "steps": 20,
        "seed": -1,
        "clip_skip": 1,
        "guidance_scale": 7.5,
        "sampler_name": "Euler a",
        "embeddings": [
            {
                "model_name": "pureerosface_v1_5162.pt"
            }
        ],
        "loras": [
            {
              "model_name": "add_detail_44319",
              "strength": 0.7
            },
            {
              "model_name": "more_details_59655",
              "strength": 0.7
            }
        ],
        "image_base64": "{{Base64 encode image}}"
    }
}'
```

`Response:`

```js  theme={"system"}
{
    "code": 0,
    "msg": "",
    "data": {
        "task_id": "73fab7c0-e24f-4027-9df0-81ff8ce4bc1f"
    }
}
```

**Use `task_id` to get images**

HTTP status codes in the 2xx range indicate that the request has been successfully accepted, while status codes in the 5xx range indicate internal server errors.

You can get images url in `imgs` of response.

`Request:`

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/async/task-result?task_id=73fab7c0-e24f-4027-9df0-81ff8ce4bc1f' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```js  theme={"system"}
{
    "extra": {
        "seed": "1434608307"
    },
    "task": {
        "task_id": "73fab7c0-e24f-4027-9df0-81ff8ce4bc1f",
        "task_type": "IMG_TO_IMG",
        "status": "TASK_STATUS_SUCCEED",
        "reason": "",
        "eta": 0,
        "progress_percent": 0
    },
    "images": [
        {
            "image_url": "https://faas-output-image.s3.ap-southeast-1.amazonaws.com/prod/73fab7c0-e24f-4027-9df0-81ff8ce4bc1f/d54551765e41409fbc80f7c23dc89241.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20240115%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20240115T083555Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=92dca9221e620d708c29ec525ed50ceb984dda23d8b7a352b4a19be682c8906e",
            "image_url_ttl": "3600",
            "image_type": "jpeg"
        }
    ],
    "videos": []
}
```

### 2. Image to image request with controlNet.

Please set the **`Content-Type`** header to **`application/json`** in your HTTP request to indicate that you are sending JSON data. Currently, **only JSON format is supported**.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/img2img' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "extra": {
        "response_image_type": "jpeg"
    },
    "request": {
        "model_name": "realcartoon25D_v3_240762.safetensors",
        "prompt": "1girl",
        "negative_prompt": "bad quality, bad anatomy, worst quality, low quality, lowres, extra fingers, blur, blurry, ugly, wrong proportions, watermark, image artifacts, bad eyes, bad hands, bad arms",
        "height": 1024,
        "width": 1024,
        "image_num": 1,
        "steps": 20,
        "seed": -1,
        "clip_skip": 1,
        "guidance_scale": 7,
        "sampler_name": "Euler",
        "controlnet": {
            "units": [
                {
                    "model_name": "control_v11p_sd15_openpose",
                    "image_base64": "{{Base64 encode image}}",
                    "strength": 0.5,
                    "preprocessor": "openpose"
                }
            ]
        },
        "image_base64": "{{Base64 encode image}}"
    }
}'
```

`Response:`

```bash  theme={"system"}
{
    "code": 0,
    "msg": "",
    "data": {
        "task_id": "5867de36-7b76-4dc7-876e-818e3ffe683e"
    }
}
```

**Use `task_id` to get images**

HTTP status codes in the 2xx range indicate that the request has been successfully accepted, while status codes in the 5xx range indicate internal server errors.

You can get images url in `imgs` of response.

`Request:`

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/async/task-result?task_id=5867de36-7b76-4dc7-876e-818e3ffe683e' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```js  theme={"system"}
{
    "extra": {
        "seed": "632855931",
        "enable_nsfw_detection": false
    },
    "task": {
        "task_id": "5867de36-7b76-4dc7-876e-818e3ffe683e",
        "task_type": "IMG_TO_IMG",
        "status": "TASK_STATUS_SUCCEED",
        "reason": "",
        "eta": 0,
        "progress_percent": 0
    },
    "images": [
        {
            "image_url": "https://faas-output-image.s3.ap-southeast-1.amazonaws.com/prod/5867de36-7b76-4dc7-876e-818e3ffe683e/6569906512e14c2da82d74e69882b3a4.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20240307%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20240307T064348Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=f506cd2dc7ed7526bfe1cf4074722a1178efe242db6ca56e1e7dbca9b67230d2",
            "image_url_ttl": "3600",
            "image_type": "jpeg",
            "nsfw_detection_result": null
        }
    ],
    "videos": []
}
```

### 3. Image to image request with Textual Inversion(embedding).

Please set the **`Content-Type`** header to **`application/json`** in your HTTP request to indicate that you are sending JSON data. Currently, **only JSON format is supported**.

`Request for textual inversion names:`

```
curl --location --request GET 'https://api.novita.ai/v3/model?filter.visibility=public&pagination.limit=100&pagination.cursor=c_0&filter.types=textualinversion&filter.source=civitai' \
--header 'Authorization: Bearer {{API Key}}' | jq '.models[].sd_name'
```

`Response:`

```txt  theme={"system"}
"epiCPhotoGasm-colorfulPhoto-neg_108119.pt"
"epiCNegative_66017.pt"
"verybadimagenegative_v1.3_21434.pt"
"FastNegativeV2_65067.pt"
"AS-YoungV2.pt"
"AS-YoungV2-neg.pt"
"AS-YoungestV2.pt"
"AS-YoungerV2.pt"
"AS-MidAged.pt"
"AS-Elderly.pt"
"AS-Adult.pt"
"AS-Adult-neg.pt"
"Adult.pt"
"MidAged.pt"
"unaestheticXLv13_98060.safetensors"
"unaestheticXL_Sky3.1_134255.safetensors"
"EasyNegativeV2_75525.safetensors"
"BadDream_53202.pt"
"UnrealisticDream_53204.pt"
"negative_hand-neg_43127.pt"
"bad_prompt_version2-neg_42594.pt"
"Asian-Less-Toon_39763.pt"
"badhandv4_16755.pt"
"easynegative_8955.safetensors"
"aestheticc-65800_8615.pt"
"corneo_side_deepthroat_6490.pt"
"corneo_tentacle_sex.pt"
"By bad artist -neg_6310.pt"
"dpthrt_5441.pt"
"ng_deepnegative_v1_75t_5845.pt"
"pureerosface_v1_5162.pt"
```

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/img2img' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "extra": {
        "response_image_type": "jpeg"
    },
    "request": {
        "model_name": "realcartoon25D_v3_240762.safetensors",
        "prompt": "dark theme girl",
        "negative_prompt": "",
        "height": 1024,
        "width": 1024,
        "image_num": 1,
        "steps": 20,
        "seed": 123,
        "clip_skip": 1,
        "guidance_scale": 7.5,
        "sampler_name": "Euler a",
        "embeddings": [
            {
                "model_name": "badhandv4_16755.pt"
            },
            {
                "model_name": "BadDream_53202.pt"
            }
        ],
        "image_base64": "{{Base64 encode image}}"
    }
}'
```

`Response:`

```js  theme={"system"}
{
    "code": 0,
    "msg": "",
    "data": {
        "task_id": "6411f576-1c62-48b4-a0d5-427488721159"
    }
}
```

**Use `task_id` to get images**

HTTP status codes in the 2xx range indicate that the request has been successfully accepted, while status codes in the 5xx range indicate internal server errors.

You can get images url in `imgs` of response.

`Request:`

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/async/task-result?task_id=6411f576-1c62-48b4-a0d5-427488721159' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```js  theme={"system"}
{
    "extra": {
        "seed": "170871295",
        "enable_nsfw_detection": false
    },
    "task": {
        "task_id": "6411f576-1c62-48b4-a0d5-427488721159",
        "task_type": "IMG_TO_IMG",
        "status": "TASK_STATUS_SUCCEED",
        "reason": "",
        "eta": 0,
        "progress_percent": 0
    },
    "images": [
        {
            "image_url": "https://faas-output-image.s3.ap-southeast-1.amazonaws.com/prod/6411f576-1c62-48b4-a0d5-427488721159/ede3a87d667e4371abc687b9ede03938.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20240307%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20240307T065015Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=228bb2254bf7de328814c89b200287ab903f7f5690033f810c745ae7be902b76",
            "image_url_ttl": "3600",
            "image_type": "jpeg",
            "nsfw_detection_result": null
        }
    ],
    "videos": []
}
```

### 4. Img2img request with nsfw\_detection.

When set `enable_nsfw_detection` true, NSFW detection will be enabled, incurring an additional cost of \$0.0015 for each generated image.

`nsfw_detection_level`, nsfw check level, ranging from 0 to 2, with higher levels indicating stricter NSFW detection criteria. The default value is 0. The following table lists the NSFW detection criteria for each level.

* 0: Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols.
* 1: Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols; Non-Explicit Nudity, Obstructed Intimate Parts, Kissing on the Lips.
* 2: Explicit Nudity, Explicit Sexual Activity, Sex Toys; Hate Symbols; Non-Explicit Nudity, Obstructed Intimate Parts, Kissing on the Lips; Female Swimwear or Underwear, Male Swimwear or Underwear.

Please set the **`Content-Type`** header to **`application/json`** in your HTTP request to indicate that you are sending JSON data. Currently, **only JSON format is supported**.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/img2img' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "extra": {
        "response_image_type": "jpeg",
        "enable_nsfw_detection": true,
        "nsfw_detection_level": 2
    },
    "request": {
        "model_name": "chilloutmix_NiPrunedFp32Fix.safetensors",
        "prompt": "a cute dog",
        "negative_prompt": "",
        "height": 512,
        "width": 384,
        "image_num": 1,
        "steps": 20,
        "seed": 123,
        "clip_skip": 1,
        "guidance_scale": 7.5,
        "sampler_name": "Euler a",
        "embeddings": [
            {
                "model_name": "pureerosface_v1_5162.pt"
            }
        ],
        "loras": [
            {
                "model_name": "MS_Real_AssSpread",
                "strength": 0.7
            },
            {
                "model_name": "MS_Real_Cameltoe_Lite",
                "strength": 0.9
            }
        ],
        "controlnet": {
            "units": [
                {
                    "model_name": "control_v11f1e_sd15_tile",
                    "image_base64": "{{Base64 encode image}}",
                    "strength": 1,
                    "preprocessor": "openpose"
                }
            ]
        },
        "image_base64": "{{Base64 encode image}}"
    }
}'
```

`Response:`

```js  theme={"system"}
{
    "code": 0,
    "msg": "",
    "data": {
        "task_id": "741597cc-8e27-4932-9d75-34f07b96413e"
    }
}
```

**Use `task_id` to get images**

HTTP status codes in the 2xx range indicate that the request has been successfully accepted, while status codes in the 5xx range indicate internal server errors.

You can get images url in `imgs` of response.

There are two results in reponse.

* `enable_nsfw_detection`, when return with `true` means NSFW detection is enabled.

* `nsfw_detection_result`, presenting an array of NSFW detection outcomes for each image. The order of elements in the nsfw\_detection\_result array corresponds one-to-one with the sequence of images in the `images` field in the response. The `valid` field denotes the success of the NSFW detection process, while the `confidence` field, ranging from 0 to 100, signifies the confidence level of the NSFW detection result. Higher confidence values, nearing 100, suggest a greater likelihood of the corresponding image containing NSFW content.

`Request:`

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/async/task-result?task_id=741597cc-8e27-4932-9d75-34f07b96413e' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```js  theme={"system"}
{
    "extra": {
        "seed": "3183986171",
        "enable_nsfw_detection": true
    },
    "task": {
        "task_id": "741597cc-8e27-4932-9d75-34f07b96413e",
        "task_type": "TXT_TO_IMG",
        "status": "TASK_STATUS_SUCCEED",
        "reason": "",
        "eta": 0,
        "progress_percent": 0
    },
    "images": [
        {
            "image_url": "https://faas-output-image.s3.ap-southeast-1.amazonaws.com/prod/741597cc-8e27-4932-9d75-34f07b96413e/6e38c309732f4241b99f75e54ffdb54a.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20240124%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20240124T141031Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=9edf916b9f3148207953140d0ec545a468e50fc80e635d4a7fa182c67989ced8",
            "image_url_ttl": "3600",
            "image_type": "jpeg",
            "nsfw_detection_result": {
                "valid": true,
                "confidence": 0
            }
        },
        {
            "image_url": "https://faas-output-image.s3.ap-southeast-1.amazonaws.com/prod/741597cc-8e27-4932-9d75-34f07b96413e/b8346c9cbe494102be2a28f29c0005b1.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20240124%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20240124T141031Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=d81316dea2446aab04cd5e559504a2a8fa7245958d766afd8f372e7e8fb02fb9",
            "image_url_ttl": "3600",
            "image_type": "jpeg",
            "nsfw_detection_result": {
                "valid": true,
                "confidence": 0
            }
        },
        {
            "image_url": "https://faas-output-image.s3.ap-southeast-1.amazonaws.com/prod/741597cc-8e27-4932-9d75-34f07b96413e/f6e0f939a5e4466990595445a41e75ef.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20240124%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20240124T141031Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=6d719fe7e4e6cb0f93ec07616b20e968f659b12102e4b11c866016780eb2eb6c",
            "image_url_ttl": "3600",
            "image_type": "jpeg",
            "nsfw_detection_result": {
                "valid": true,
                "confidence": 0
            }
        },
        {
            "image_url": "https://faas-output-image.s3.ap-southeast-1.amazonaws.com/prod/741597cc-8e27-4932-9d75-34f07b96413e/ddbc7d39db1d4468bd3c9d92556b99ee.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20240124%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20240124T141031Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=259a5d358175132a2c0adfcd23142bb8227cd6e68052b99779686956c04a713a",
            "image_url_ttl": "3600",
            "image_type": "jpeg",
            "nsfw_detection_result": {
                "valid": true,
                "confidence": 0
            }
        }
    ],
    "videos": []
}
```


Built with [Mintlify](https://mintlify.com).