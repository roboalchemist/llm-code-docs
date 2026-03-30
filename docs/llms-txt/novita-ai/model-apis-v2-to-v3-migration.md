# Source: https://novita.ai/docs/guides/model-apis-v2-to-v3-migration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API V2 to V3 Migration Guide

## Text to Image

### Request Body Parameter Mapping

<table class="table">
  <thead>
    <tr>
      <th>V2</th>
      <th>V3</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**extra**<span class="type-desc">object</span></td>
      <td>**extra**<span class="type-desc">object</span></td>

      <td />
    </tr>

    <tr>
      <td class="list-col">enable\_nsfw\_detection<br /><span class="type-desc mt-1 ml-0">boolean</span></td>
      <td class="list-col">enable\_nsfw\_detection<br /><span class="type-desc mt-1 ml-0">boolean</span></td>

      <td />
    </tr>

    <tr>
      <td class="list-col">nsfw\_detection\_level<br /><span class="type-desc mt-1 ml-0">Enum: `0, 1, 2`</span></td>
      <td class="list-col">nsfw\_detection\_level<br /><span class="type-desc mt-1 ml-0">Enum: `0, 1, 2`</span></td>

      <td />
    </tr>

    <tr>
      <td class="list-col delete">enable\_progress\_info</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col">response\_image\_type<br /><span class="type-desc mt-1 ml-0">Enum: `png`, `jpeg`</span></td>
      <td class="list-col">response\_image\_type<br /><span class="type-desc mt-1 ml-0">Enum: `png, webp, jpeg`</span></td>
      <td>V3 adds support for `webp`image format</td>
    </tr>

    <tr>
      <td />

      <td>**request**<span class="type-desc">object</span></td>
      <td><span class="new-field">New Field</span><br />All image generation parameters must be passed via the `request`in V3</td>
    </tr>

    <tr>
      <td class="delete">**prompt**<span class="type-desc">string</span><br />\<lora:\$sd\_name:\$weight></td>
      <td class="list-col">prompt<span class="type-desc">string</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td />

      <td class="list-col">loras<span class="type-desc">object\[]</span></td>
      <td><span class="moved">Moved Inside</span><br />**Migrate LoRA usage: From **`prompt`** to **`request.loras`** parameter**</td>
    </tr>

    <tr>
      <td />

      <td class="list-sub-col">model\_name<span class="type-desc">string</span></td>
      <td><span class="new-field">New Field</span><br />Name of lora, retrieve the corresponding sd\_name\_in\_api value by invoking the [Get Model API](https://novita.ai/docs/api-reference/model-apis-get-model) endpoint with filter.types=lora as the query parameter.</td>
    </tr>

    <tr>
      <td />

      <td class="list-sub-col">strength<span class="type-desc">number(float32)</span></td>
      <td><span class="new-field">New Field</span><br />The strength value of lora. The larger the value, the more biased the effect is towards lora, Range \[0, 1]</td>
    </tr>

    <tr>
      <td class="delete">**negative\_prompt**<span class="type-desc">string</span></td>
      <td class="list-col">negative\_prompt<span class="type-desc">string</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**sampler\_name**<span class="type-desc">string</span></td>
      <td class="list-col">sampler\_name<span class="type-desc">string</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**batch\_size**<span class="type-desc">integer</span></td>
      <td class="list-col">image\_num<span class="type-desc">integer</span></td>
      <td><span class="moved">Changed</span><br /> `num_images` **→** `request.image_num`</td>
    </tr>

    <tr>
      <td class="delete">**n\_iter**</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">**steps**<span class="type-desc">string</span></td>
      <td class="list-col">steps<span class="type-desc">string</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**cfg\_scale**<span class="type-desc">integer</span></td>
      <td class="list-col">guidance\_scale<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td><span class="moved">Changed</span><br /> `cfg_scale`**→** `request.guidance_scale`</td>
    </tr>

    <tr>
      <td class="delete">**seed**<span class="type-desc">integer</span></td>
      <td class="list-col">seed<span class="type-desc">integer</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**height**<span class="type-desc">integer</span></td>
      <td class="list-col">height<span class="type-desc">integer</span></td>
      <td><span class="moved">Moved Inside</span><br />Range Change: \[128, 2048].</td>
    </tr>

    <tr>
      <td class="delete">**width**<span class="type-desc">integer</span></td>
      <td class="list-col">width<span class="type-desc">integer</span></td>
      <td><span class="moved">Moved Inside</span><br />Range Change: \[128, 2048].</td>
    </tr>

    <tr>
      <td class="delete">**model\_name**<span class="type-desc">string</span></td>
      <td class="list-col">model\_name<span class="type-desc">string</span></td>
      <td><span class="moved">Moved Inside</span><br />This parameter specifies the name of the model checkpoint. Retrieve the corresponding sd\_name value by invoking the [Query Model](https://novita.ai/docs/api-reference/model-apis-get-model) API with filter.types=checkpoint as the query parameter.</td>
    </tr>

    <tr>
      <td class="delete">**restore\_faces**<span class="type-desc">bool</span></td>
      <td class="list-col">restore\_faces<span class="type-desc">bool</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**restore\_faces\_model**</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">**sd\_vae**<span class="type-desc">string</span></td>
      <td class="list-col">sd\_vae<span class="type-desc">string</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**clip\_skip**<span class="type-desc">integer</span></td>
      <td class="list-col">clip\_skip<span class="type-desc">integer</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**enable\_hr**<span class="type-desc">boolean</span></td>
      <td class="list-col">hires\_fix<span class="type-desc">object</span></td>
      <td><span class="moved">Changed</span><br /> `enable_hr`**→** `request.hires_fix`</td>
    </tr>

    <tr>
      <td class="delete">**hr\_upscaler**<br /><span class="type-desc mt-1 ml-0">Enum:<br /> `Latent`, `ESRGAN_4x`, `R-ESRGAN 4x+`, `R-ESRGAN 4x+ Anime6B`</span></td>
      <td class="list-sub-col">upscaler<br /><span class="type-desc mt-1 ml-0">Enum: `RealESRGAN_x4plus_anime_6B`, `RealESRNet_x4plus,Latent`</span></td>
      <td><span class="moved">Changed</span><br /> `hr_upscaler`**→**`request.hires_fix.upscaler`</td>
    </tr>

    <tr>
      <td class="delete">**hr\_scale**<span class="type-desc">number</span></td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">**hr\_resize\_x**<span class="type-desc">integer</span></td>
      <td class="list-sub-col">target\_width<span class="type-desc">integer</span></td>
      <td><span class="moved">Changed</span><br /> `hr_resize_x`**→** `request.hires_fix.target_width`</td>
    </tr>

    <tr>
      <td class="delete">**hr\_resize\_y**<span class="type-desc">integer</span></td>
      <td class="list-sub-col">target\_height<span class="type-desc">integer</span></td>
      <td><span class="moved">Changed</span><br /> `hr_resize_y`**→** `request.hires_fix.target_height`</td>
    </tr>

    <tr>
      <td class="delete">**img\_expire\_ttl**<span class="type-desc">integer</span></td>

      <td />

      <td><span class="deprecated">Deprecated</span><br />Default 3600s</td>
    </tr>

    <tr>
      <td class="delete">**sd\_refiner**<span class="type-desc">object</span></td>
      <td class="list-col">refiner<span class="type-desc">object</span></td>
      <td><span class="moved">Changed</span><br /> `sd_refiner`**→** `request.refiner`</td>
    </tr>

    <tr>
      <td class="list-col delete">checkpoint<span class="type-desc">string</span></td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col delete">switch\_at<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td class="list-sub-col">switch\_at<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td><span class="moved">Changed</span><br /> `sd_refiner.switch_at`**→** `request.refiner.switch_at`</td>
    </tr>

    <tr>
      <td class="delete">**controlnet\_units**<span class="type-desc">object\[]</span></td>

      <td />

      <td><span class="deprecated">Deprecated</span><br /><span class="inline-block mt-2">`img2img` Only</span></td>
    </tr>
  </tbody>
</table>

### Response Parameter Mapping

<table class="table">
  <thead>
    <tr>
      <th>V2</th>
      <th>V3</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td class="delete">**code**</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">**msg**</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">**data**</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col delete">task\_id</td>
      <td>**task\_id**</td>
      <td><span class="moved">Changed</span><br /> `data.task_id`**→** `task_id`</td>
    </tr>

    <tr>
      <td class="list-col delete">warn</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>
  </tbody>
</table>

### Example

<CardGroup cols={2}>
  <Card title="Text to Image V2">
    * Request

    ```bash  theme={"system"}
    curl --location "https://api.novita.ai/v2/txt2img" \
    --header "Authorization: Bearer {{API Key}}" \
    --header "Content-Type: application/json" \
    --data '{
      "extra": {
        "enable_nsfw_detection": false,
        "nsfw_detection_level": 0,
        "response_image_type": "jpeg"
      },
      "prompt": "(masterpiece, best quality, ultra-detailed:1.3), <lora:AnimeStyle_XL_v1_AutoRunMech_103883:0.8>, 1girl, mecha armor, futuristic city background, glowing neon lights, dynamic pose, cyberpunk style, intricate mechanical details, (floating holographic interface:1.2), sparkling blue eyes, wind-blown hair, (steam and energy particles:1.1), cinematic lighting",
      "negative_prompt":"(worst quality, low quality:1.4), (deformed, distorted:1.3), disfigured, blurry, bad anatomy, extra limbs, (mutated hands:1.2), (text, watermark:1.5), 
    overexposed, underexposed, (cartoonish:1.2), (simplistic background:1.3), 
    grainy, (traditional drawing:1.2), (realistic:1.4), (noisy:1.3)",
      "sampler_name":"DPM++ 2M Karras",
      "batch_size": 1,
      "n_iter": 1,
      "steps": 25,
      "cfg_scale": 7,
      "seed": 65531,
      "height": 512,
      "width": 512,
      "model_name": "sd_xl_base_1.0.safetensors",
      "restore_faces": false,
      "restore_faces_model": "",
      "sd_vae": "",
      "clip_skip": 1,
      "enable_hr": true,
      "hr_upscaler": "Latent",
      "hr_scale": 2,
      "hr_resize_x": 1024,
      "hr_resize_y": 1024,
      "img_expire_ttl": 3600
    }'
    ```

    * Response

    ```
    {
      "code": 0,
      "msg": "",
      "data": {
        "task_id": "12905b6a-d436-4010-b199-d800130c0aab"
      }
    }
    ```
  </Card>

  <Card title="Text to Image V3">
    * Reqeust

    ```bash  theme={"system"}
    curl --location 'https://api.novita.ai/v3/async/txt2img' \
    --header 'Authorization: Bearer {{API Key}}' \
    --header 'Content-Type: application/json' \
    --data '{
        "extra": {
            "enable_nsfw_detection": false,
            "nsfw_detection_level": 0,
            "response_image_type": "jpeg"
        },
        "request": {
          "prompt": "(masterpiece, best quality, ultra-detailed:1.3), 1girl, mecha armor, futuristic city background, glowing neon lights, dynamic pose, cyberpunk style, intricate mechanical details,(floating holographic interface:1.2), sparkling blue eyes, wind-blown hair, (steam and energy particles:1.1), cinematic lighting",
          "negative_prompt": "(worst quality, low quality:1.4), (deformed, distorted:1.3), disfigured,blurry, bad anatomy, extra limbs, (mutated hands:1.2), (text, watermark:1.5),overexposed, underexposed,(cartoonish:1.2), (simplistic background:1.3), grainy, (traditional drawing:1.2),(realistic:1.4), (noisy:1.3)",
            "model_name": "sd_xl_base_1.0.safetensors",
            "width": 512,
            "height": 512,
            "image_num": 1,
            "steps": 25,
            "seed": 65531,
            "restore_faces": false,
            "clip_skip": 1,
            "sampler_name":"DPM++ 2M Karras",
            "guidance_scale": 7,
            "hires_fix": {
                "target_width": 1024,
                "target_height": 1024,
                "strength": 0.8,
                "upscaler": "Latent"
            },
            "loras": [
              {
                "model_name": "AnimeStyle_XL_v1_AutoRunMech_103883",
                "strength": 0.8
              }
            ]
        }
    }'
    ```

    * Repspone

    ```bash  theme={"system"}
    {
      "task_id":"0696ce57-22df-4a89-9efc-80c386a82dbd"
    }
    ```
  </Card>
</CardGroup>

## Image to Image

### Request Body Parameter Mapping

<table class="table">
  <thead>
    <tr>
      <th>V2</th>
      <th>V3</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**extra**<span class="type-desc">object</span></td>
      <td>**extra**<span class="type-desc">object</span></td>

      <td />
    </tr>

    <tr>
      <td class="list-col">enable\_nsfw\_detection<br /><span class="type-desc mt-1 ml-0">boolean</span></td>
      <td class="list-col">enable\_nsfw\_detection<br /><span class="type-desc mt-1 ml-0">boolean</span></td>

      <td />
    </tr>

    <tr>
      <td class="list-col">nsfw\_detection\_level<br /><span class="type-desc mt-1 ml-0">Enum: `0, 1, 2`</span></td>
      <td class="list-col">nsfw\_detection\_level<br /><span class="type-desc mt-1 ml-0">Enum: `0, 1, 2`</span></td>

      <td />
    </tr>

    <tr>
      <td class="list-col delete">enable\_progress\_info</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col">response\_image\_type<br /><span class="type-desc mt-1 ml-0">Enum: `png`, `jpeg`</span></td>
      <td class="list-col">response\_image\_type<br /><span class="type-desc mt-1 ml-0">Enum: `png, webp, jpeg`</span></td>
      <td>V3 adds support for `webp`image format</td>
    </tr>

    <tr>
      <td />

      <td>**request**<span class="type-desc">object</span></td>
      <td><span class="new-field">New field</span><br />All image generation parameters must be passed via the `request`in V3</td>
    </tr>

    <tr>
      <td class="delete">**prompt**<span class="type-desc">string</span><br />\<lora:\$sd\_name:\$weight></td>
      <td class="list-col">prompt<span class="type-desc">string</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td />

      <td class="list-col">loras<span class="type-desc">object\[]</span></td>
      <td><span class="moved">Moved Inside</span><br />**Migrate LoRA usage: From **`prompt`** to **`request.loras`** parameter**</td>
    </tr>

    <tr>
      <td />

      <td class="list-sub-col">model\_name<span class="type-desc">string</span></td>
      <td><span class="new-field">New Field</span><br />Name of lora, retrieve the corresponding sd\_name\_in\_api value by invoking the [Get Model API](https://novita.ai/docs/api-reference/model-apis-get-model) endpoint with filter.types=lora as the query parameter.</td>
    </tr>

    <tr>
      <td />

      <td class="list-sub-col">strength<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td><span class="new-field">New Field</span><br />The strength value of lora. The larger the value, the more biased the effect is towards lora, Range \[0, 1]</td>
    </tr>

    <tr>
      <td class="delete">**negative\_prompt**<span class="type-desc">string</span></td>
      <td class="list-col">negative\_prompt<br /><span class="type-desc mt-1 ml-0">string</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**sampler\_name**<span class="type-desc">string</span></td>
      <td class="list-col">sampler\_name<span class="type-desc">string</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**batch\_size**<span class="type-desc">integer</span></td>
      <td class="list-col">image\_num<span class="type-desc">integer</span></td>
      <td><span class="moved">Changed</span><br /> `batch_size`**→** `request.image_num`</td>
    </tr>

    <tr>
      <td class="delete">**n\_iter**<span class="type-desc">integer</span></td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">**steps**<span class="type-desc">string</span></td>
      <td class="list-col">steps<span class="type-desc">string</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**cfg\_scale**<span class="type-desc">integer</span></td>
      <td class="list-col">guidance\_scale<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td><span class="moved">Changed</span><br /> `cfg_scale`**→** `request.guidance_scale`</td>
    </tr>

    <tr>
      <td class="delete">**seed**<span class="type-desc">integer</span></td>
      <td class="list-col">seed<span class="type-desc">integer</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**height**<span class="type-desc">integer</span></td>
      <td class="list-col">height<span class="type-desc">integer</span></td>
      <td><span class="moved">Moved Inside</span><br />Range Change: \[128, 2048].</td>
    </tr>

    <tr>
      <td class="delete">**width**<span class="type-desc">integer</span></td>
      <td class="list-col">width<span class="type-desc">integer</span></td>
      <td><span class="moved">Moved Inside</span><br />Range Change: \[128, 2048].</td>
    </tr>

    <tr>
      <td class="delete">**model\_name**<span class="type-desc">string</span></td>
      <td class="list-col">model\_name<span class="type-desc">string</span></td>
      <td><span class="moved">Moved Inside</span><br />This parameter specifies the name of the model checkpoint. Retrieve the corresponding sd\_name value by invoking the [Query Model](https://novita.ai/docs/api-reference/model-apis-get-model) API with filter.types=checkpoint as the query parameter.</td>
    </tr>

    <tr>
      <td class="delete">**init\_images**<span class="type-desc">string\[]</span></td>
      <td class="list-col">image\_base64<span class="type-desc">string</span></td>
      <td><span class="moved">Changed</span><br /> `init_images`**→** `request.image_base64`</td>
    </tr>

    <tr>
      <td class="delete">**denoising\_strength**<br /><span class="type-desc mt-1 ml-0">number(float)</span></td>
      <td class="list-col">strength<br /><span class="type-desc mt-1 ml-0">number(float)</span></td>
      <td><span class="moved">Changed</span><br /> `denoising_strength`**→** `request.strength`</td>
    </tr>

    <tr>
      <td class="delete">**restore\_faces**<span class="type-desc">bool</span></td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">**sd\_vae**<span class="type-desc">string</span></td>
      <td class="list-col">sd\_vae<span class="type-desc">string</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**clip\_skip**<span class="type-desc">integer</span></td>
      <td class="list-col">clip\_skip<span class="type-desc">integer</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="delete">**mask**<span class="type-desc">string</span></td>

      <td />

      <td><span class="deprecated">Deprecated</span><br />Recommendation: Use V3 Inpainting API</td>
    </tr>

    <tr>
      <td class="delete">**mask\_blur**<span class="type-desc">integer</span></td>

      <td />

      <td><span class="deprecated">Deprecated</span><br />Recommendation: Use V3 Inpainting API</td>
    </tr>

    <tr>
      <td class="delete">**resize\_mode**<span class="type-desc">integer</span></td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">**image\_cfg\_scale**<span class="type-desc">integer</span></td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">**inpainting\_fill**<span class="type-desc">integer</span></td>

      <td />

      <td><span class="deprecated">Deprecated</span><br />Recommendation: Use V3 Inpainting API</td>
    </tr>

    <tr>
      <td class="delete">**inpaint\_full\_res**<span class="type-desc">integer</span></td>

      <td />

      <td><span class="deprecated">Deprecated</span><br />Recommendation: Use V3 Inpainting API</td>
    </tr>

    <tr>
      <td class="delete">**inpaint\_full\_res\_padding**<br /><span class="type-desc mt-1 ml-0">integer</span></td>

      <td />

      <td><span class="deprecated">Deprecated</span><br />Recommendation: Use V3 Inpainting API</td>
    </tr>

    <tr>
      <td class="delete">**inpainting\_mask\_invert**<br /><span class="type-desc mt-1 ml-0">integer</span></td>

      <td />

      <td><span class="deprecated">Deprecated</span><br />Recommendation: Use V3 Inpainting API</td>
    </tr>

    <tr>
      <td class="delete">**initial\_noise\_multiplier**<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">**img\_expire\_ttl**<span class="type-desc">integer</span></td>

      <td />

      <td><span class="deprecated">Deprecated</span><br />Default 3600s</td>
    </tr>

    <tr>
      <td class="delete">**sd\_refiner**<span class="type-desc">object</span></td>
      <td class="list-col">refiner<span class="type-desc">object</span></td>
      <td><span class="moved">Changed</span><br /> `sd_refiner`**→** `request.refiner`</td>
    </tr>

    <tr>
      <td class="list-col delete">checkpoint</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col delete">switch\_at<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td class="list-sub-col">switch\_at<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td />

      <td class="list-sub-col">controlnet<span class="type-desc">object</span></td>
      <td><span class="new-field">New Field</span></td>
    </tr>

    <tr>
      <td class="delete">**controlnet\_units**<span class="type-desc">object\[]</span></td>
      <td class="list-grandson-col">units<span class="type-desc">object\[]</span></td>
      <td><span class="moved">Changed</span><br /> `controlnet_units`**→** `request.controlnet.units`</td>
    </tr>

    <tr>
      <td class="list-col delete">model<span class="type-desc">string</span></td>
      <td class="list-grandson-sub-col ">model\_name<br /><span class="type-desc mt-1 ml-0">string</span></td>
      <td><span class="moved">Changed</span><br /> `controlnet_units.model`**→** <br />`request.controlnet.units.model_name`</td>
    </tr>

    <tr>
      <td class="list-col delete">weight<span class="type-desc">number</span></td>
      <td class="list-grandson-sub-col ">strength<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td><span class="moved">Changed</span><br /> `controlnet_units.weight`**→** <br />`request.controlnet.units.strength`</td>
    </tr>

    <tr>
      <td class="list-col delete">input\_image<span class="type-desc">string</span></td>
      <td class="list-grandson-sub-col ">image\_base64<br /><span class="type-desc mt-1 ml-0">string</span></td>
      <td><span class="moved">Changed</span><br /> `controlnet_units.input_image`**→** <br />`request.controlnet.units.image_base64`</td>
    </tr>

    <tr>
      <td class="list-col delete">module<span class="type-desc">string,Enum</span></td>
      <td class="list-grandson-sub-col ">preprocessor<br /><span class="type-desc mt-1 ml-0">string,Enum</span></td>
      <td><span class="moved">Changed</span><br />`controlnet_units.module`**→** <br />`request.controlnet.units.preprocessor`</td>
    </tr>

    <tr>
      <td class="list-col delete">control\_mode</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col delete">mask</td>

      <td />

      <td><span class="deprecated">Deprecated</span><br />Recommendation: Use V3 Inpainting API</td>
    </tr>

    <tr>
      <td class="list-col delete">resize\_mode</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col delete">processor\_res</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col delete">threshold\_a</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col delete">threshold\_b</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col delete">guidance\_start<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td class="list-grandson-sub-col">guidance\_start<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="list-col delete">guidance\_end<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td class="list-grandson-sub-col">guidance\_end<br /><span class="type-desc mt-1 ml-0">number(float32)</span></td>
      <td class="moved">Moved Inside</td>
    </tr>

    <tr>
      <td class="list-col delete">pixel\_perfect</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>
  </tbody>
</table>

### Response Parameter Mapping

<table class="table">
  <thead>
    <tr>
      <th>V2</th>
      <th>V3</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td class="delete">code</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">msg</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="delete">data</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>

    <tr>
      <td class="list-col delete">task\_id</td>
      <td>**task\_id**</td>
      <td><span class="moved">Changed</span><br /> `data.task_id`**→** `task_id`</td>
    </tr>

    <tr>
      <td class="list-col delete">warn</td>

      <td />

      <td class="deprecated">Deprecated</td>
    </tr>
  </tbody>
</table>

### Example

<CardGroup cols={2}>
  <Card title="Image to Image V2">
    * Request

    ```
    curl --request POST \
      --url https://api.novita.ai/v2/img2img \
      --header 'Authorization: <authorization>' \
      --header 'Content-Type: application/json' \
      --data '{
      "extra": {
        "enable_nsfw_detection": false,
        "nsfw_detection_level": 0,
        "response_image_type": "png"
      },
      "prompt": "realistic, photograph, (masterpiece), 8k quality, (detailed eyes:1.2), (highest quality:1.1), highly detailed, majestic, top quality, best quality, newest, ai-generated, (intricate details:1.1), extremely beautiful, elegant, majestic, immersive background+, (detailed face, perfect face), In the heart of a vibrant garden, a girl with red hair and brown eyes sits in contemplation of the nature around her.",
      "negative_prompt": "(worst quality:1.5), (low quality:1.5), (normal quality:1.5), anime, cartoon, painting, drawing, illustration, manga, sketch, nudity, young, child, hairband, headband, horns, lowres, bad anatomy, bad hands, multiple eyebrow, (cropped), extra limb, missing limbs, deformed hands, long neck, long body, long torso, (bad hands), signature, username, artist name, conjoined fingers, deformed fingers, ugly eyes, imperfect eyes, skewed eyes, unnatural face, unnatural body, error, grain, jpeg artifacts",
      "sampler_name":"DPM++ 2M Karras",
      "batch_size": 1,
      "n_iter": 1,
      "steps": 25,
      "cfg_scale": 7.5,
      "seed": 765824,
      "height": 768,
      "width": 512,
      "model_name": "cyberrealistic_v31_62396.safetensors",
      "init_images": [
        "<IMAGE_BASE64>"
      ],
      "denoising_strength": 0.8,
      "restore_faces": false,
      "clip_skip": 1,
      "img_expire_ttl": 3600,
      "controlnet_units": {
        "model": "control_v11p_sd15_lineart",
        "weight": 1,
        "input_image": "<IMAGE_BASE64>",
        "module": "lineart",
        "guidance_start": 0,
        "guidance_end": 1
      }
    }'
    ```

    * Response

    ```
    {
      "code": 0,
      "msg": "",
      "data": {
        "task_id": "a1b0d99b-2ef0-4b20-8eeb-c641ae84ed45"
      }
    }
    ```
  </Card>

  <Card title="Image to Image V3">
    * Request

    ```
    curl --request POST \
      --url https://api.novita.ai/v3/async/img2img \
      --header 'Authorization: <authorization>' \
      --header 'Content-Type: <content-type>' \
      --data '{
      "extra": {
        "enable_nsfw_detection": false,
        "nsfw_detection_level": 0,
        "response_image_type": "png"
      },
      "request": {
        "prompt": "realistic, photograph, (masterpiece), 8k quality, (detailed eyes:1.2), (highest quality:1.1), highly detailed, majestic, top quality, best quality, newest, ai-generated, (intricate details:1.1), extremely beautiful, elegant, majestic, immersive background+, (detailed face, perfect face), In the heart of a vibrant garden, a girl with red hair and brown eyes sits in contemplation of the nature around her.",
        "negative_prompt": "(worst quality:1.5), (low quality:1.5), (normal quality:1.5), anime, cartoon, painting, drawing, illustration, manga, sketch, nudity, young, child, hairband, headband, horns, lowres, bad anatomy, bad hands, multiple eyebrow, (cropped), extra limb, missing limbs, deformed hands, long neck, long body, long torso, (bad hands), signature, username, artist name, conjoined fingers, deformed fingers, ugly eyes, imperfect eyes, skewed eyes, unnatural face, unnatural body, error, grain, jpeg artifacts",
        "sampler_name": "DPM++ 2M Karras",
        "image_num": 1,
        "steps": 25,
        "guidance_scale": 7.5,
        "seed": 765824,
        "height": 768,
        "width": 512,
        "model_name": "cyberrealistic_v31_62396.safetensors",
            "image_base64": "<IMAGE_BASE64>",
        "strength": 0.8,
        "clip_skip": 1,
        "controlnet": {
          "units": [
            {
              "model_name": "control_v11p_sd15_lineart",
              "strength": 1,
              "image_base64": "<IMAGE_BASE64>",
              "preprocessor": "lineart",
              "guidance_start": 0,
              "guidance_end": 1
            }
          ]
        }
      }
    }'
    ```

    * Response

    ```bash  theme={"system"}
    {
      "task_id": "9490dde7-cd28-493e-9db0-8a38a65bf5e6"
    }
    ```
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).