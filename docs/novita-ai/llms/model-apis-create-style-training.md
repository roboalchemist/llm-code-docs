# Source: https://novita.ai/docs/api-reference/model-apis-create-style-training.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LoRA for Style Training

**You can train a LoRA model to generate images that emulate a specific artistic style.**

## Create Style Training Task

`POST https://api.novita.ai/v3/training/style`

**Use this API to start a style training task.**

> This is an **asynchronous API**; only the **task\_id** is returned initially. Utilize this **task\_id** to query the **Task Result API** at [Get Style Training Result API](#get-style-training-result) to retrieve the results of the image generation.

### Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

### Request Body

<ParamField body="name" type="string" required={true}>
  Task name for this model training.
</ParamField>

<ParamField body="base_model" type="string" required={true}>
  Base models used for training.<br />
  Enum: `stable-diffusion-xl-base-1.0`, `dreamshaperXL09Alpha_alpha2Xl10_91562`, `protovisionXLHighFidelity3D_release0630Bakedvae_154359`, `v1-5-pruned-emaonly`, `epicrealism_naturalSin_121250`, `chilloutmix_NiPrunedFp32Fix`, `abyssorangemix3AOM3_aom3a3_10864`, `dreamshaper_8_93211`, `WFChild_v1.0`, `majichenmixrealistic_v10`, `realisticVisionV51_v51VAE_94301`, `sdxlUnstableDiffusers_v11_216694`, `realisticVisionV40_v40VAE_81510`, `epicrealismXL_v10_247189`, `somboy_v10_172675`, `yesmixXL_v10_283329`, `animagineXLV31_v31_325600`
</ParamField>

<ParamField body="width" type="integer" required={true}>
  Width of training images, must be > 0
</ParamField>

<ParamField body="height" type="integer" required={true}>
  Height of training images, must be > 0
</ParamField>

<ParamField body="image_dataset_items" type="object[]" required={true}>
  Image asset IDs and their captions.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="assets_id" type="integer" required={true}>
      Image asset ID; see <a href="#_1-upload-images-for-training">Upload Images For Training</a> for reference.
    </ParamField>

    <ParamField body="caption" type="string" required={true}>
      Image caption; refer to <a href="/guides/model-apis-training-guidance">Training Image Caption Guidance</a> for more information.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="expert_setting" type="object" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="train_batch_size" type="integer" required={false}>
      batch size of training, Range \[1, 4]
    </ParamField>

    <ParamField body="learning_rate" type="number(float)" required={false}>
      This parameter controls the extent of model parameter updates during each iteration. A higher learning rate results in larger updates, potentially speeding up the learning process but risking overshooting the optimal solution. Conversely, a lower learning rate ensures smaller, more precise adjustments, which may lead to a more stable convergence at the cost of slower training.<br />
      Enum: `1e-4, 1e-5, 1e-6, 2e-4, 5e-5`
    </ParamField>

    <ParamField body="max_train_steps" type="integer" required={false}>
      This parameter specifies the maximum number of training steps to be executed before halting the training process. It sets a limit on the duration of training, ensuring that the model does not continue to train indefinitely. If the `max_train_steps` set to 2000 and images amount in parameter `image_dataset_items` is 10, the number of training steps per graph is 200. Minimum value is 1.
    </ParamField>

    <ParamField body="seed" type="integer" required={false}>
      A seed is a number from which Stable Diffusion generates noise, which, makes training deterministic. Using the same seed and set of parameters will produce identical LoRA each time, Minimum 1.
    </ParamField>

    <ParamField body="lr_scheduler" type="string" required={false}>
      This parameter specifies the type of learning rate scheduler to be used during the training process. The scheduler dynamically adjusts the learning rate according to one of the specified strategies. `constant`: Maintains a fixed learning rate throughout training. `linear`: Gradually decreases the learning rate linearly from a higher to a lower value. `cosine`: Adjusts the learning rate following a cosine curve, decreasing it initially and then increasing towards the end. `cosine_with_restarts`: Similar to cosine, but resets the rate periodically to avoid local minima. `polynomial`: Decreases the learning rate according to a polynomial decay. `constant_with_warmup`: Starts with a lower learning rate and warms up to a constant rate after a specified number of steps.<br />
      Enum: `constant, linear, cosine, cosine_with_restarts, polynomial, constant_with_warmup`
    </ParamField>

    <ParamField body="lr_warmup_steps" type="integer" required={false}>
      This parameter determines the number of initial training steps during which the learning rate increases gradually, effective only when the lr\_scheduler is set to one of the following modes: linear, cosine, cosine\_with\_restarts, polynomial, or constant\_with\_warmup. The warmup phase helps in stabilizing the training process before the main learning rate schedule begins. The minimum value for this parameter is 0, indicating no warmup, Minimum 0.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="components" type="object[]" required={true}>
  Common parameters configured for training.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="name" type="string" required={true}>
      Type of components. When set to `face_crop_region`, args can be set to args: \[name: ratio, value: 1.0], ratio > 1 means more non-facial area will be included. When set to `resize`, args can be set to args: \[name: width, value: 512, name: height, value: 512], which mean all the images will be cropped to 512\*512. When set to `face_restore`, args can be set to args: \[name: method, value:gfpgan\_1.4], which mean face restore will be open.<br />
      Enum: `face_crop_region`, `resize`, `face_restore`
    </ParamField>

    <ParamField body="args" type="object[]" required={true}>
      Component detail settings.

      <Expandable title="properties" defaultOpen={true}>
        <ParamField body="name" type="string" required={true}>
          Name of argument.
        </ParamField>

        <ParamField body="value" type="string" required={true}>
          Argument value.
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

### Response

<ResponseField name="task_id" type="string" required={false}>
  Utilize this `task_id` to query the Task Result API at <a href="#get-style-training-result">Get style training result</a>.
</ResponseField>

## Get style training result

`GET https://api.novita.ai/v3/training/style`

**Use this API to get the style training result, including the model.**

### Request Headers

<ParamField header="Authorization" type="string" required={true}>
  In Bearer \{\{API Key}} format.
</ParamField>

### Request Body

<ParamField body="task_id" type="string" required={true} />

### Response

<ResponseField name="task_id" type="string" required={false}>
  The task id of training.
</ResponseField>

<ResponseField name="task_status" type="string" required={false}>
  Represents the current status of a task, particularly useful for monitoring and managing the progress of training tasks. Each status indicates a specific phase in the task's lifecycle.<br />
  Enum: `UNKNOWN`, `QUEUING`, `TRAINING`, `SUCCESS`, `CANCELED`, `FAILED`
</ResponseField>

<ResponseField name="model_type" type="string" required={false}>
  Model trained type.<br />
  Enum: `lora`
</ResponseField>

<ResponseField name="models" type="object[]" required={false}>
  models info

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="model_name" type="string" required={false}>
      model file name.
    </ResponseField>

    <ResponseField name="model_status" type="string" required={false}>
      model status.<br />
      Enum: `DEPLOYING`, `SERVING`
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="extra" type="object" required={false}>
  extra info

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="eta_relative" type="number" required={false}>
      Estimated time of arrival in seconds.
    </ResponseField>

    <ResponseField name="progress_percent" type="number" required={false}>
      The progress percent with a range of 0 to 100.
    </ResponseField>
  </Expandable>
</ResponseField>

## Example

<u>**In this document we will explain step by step how to use our API for LoRA model training.**</u>

Generally, model training involves following steps.

* Upload the images for model training.
* Set training parameters and start the training.
* Get the training results and generate images with the trained model.

### 1. Upload images for training

* Currently we only supports uploading images in `png` / `jpeg` / `webp` format.
* Each task supports uploading up to 50 images. In order to make the final effect good, the images uploaded should meet some basic conditions, such as: "portrait in the center", "no watermark", "clear picture", etc.

#### 1.1 Get image upload URL

* This interface returns the URL for single image to upload and can be called multiple times to upload images for training.

```bash  theme={"system"}
curl --location --request POST 'https://api.novita.ai/v3/assets/training_dataset' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "file_extension": "png"
}'
```

`Response:`

```js  theme={"system"}
{
    "assets_id": "34558688e2f42a0137ca2d5274a8cf43",
    "upload_url": "https://faas-training-dataset.s3.ap-southeast-1.amazonaws.com/test/******",
    "method": "PUT",
    "headers": {
        "Host": {
            "values": [
                "faas-training-dataset.s3.ap-southeast-1.amazonaws.com"
            ]
        }
    }
}
```

* `assets_id`: The unique identifier of the image, which will be used in the training task.
* `upload_url`: The URL for image upload.
* `method`: The HTTP method for image upload.

#### 1.2 Upload images

After obtaining the `upload_url` at step `Get image upload URL`, please refer to the following document to complete the image upload: [https://docs.aws.amazon.com/zh\_cn/AmazonS3/latest/userguide/PresignedUrlUploadObject.html.](https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/userguide/PresignedUrlUploadObject.html)

`Put images:`

```bash  theme={"system"}
curl -X PUT -T "{{filepath}}" "{{upload_url}}"
```

`or`

```
curl --location --request PUT '{{upload_url}}' \
--header 'Content-Type: image/png' \
--data '{{filepath}}'
```

### 2. Start training task and configure parameters

In this step, we will begin the model training process, which is expected to take approximately 10 minutes, depending on the actual server's availability.

There are four types of parameters for model traning: `Model info parameters`, `dataset parameters`, `components parameters`,`expert parameters`, you can set them according to our tables below.

Here are some tips to train a good model:

* At least 10 photos of faces that meet the requirements.
* For parameters `instance_prompt`, we suggests using "a close photo of ohwx \<man|\woman>"
* For parameters `base_model`, value `v1-5-pruned-emaonly` has better generalization ability and can be used in combination with various Base models, such as `dreamshaper 2.5D`, value `epic-realism` has a strong sense of reality.

| Type                  | Parameters                         | Description                                                                                                                                     |
| :-------------------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| Model info parameters | name                               | Name of your training model                                                                                                                     |
| Model info parameters | base\_model                        | base\_model type                                                                                                                                |
| Model info parameters | width                              | Target image width                                                                                                                              |
| Model info parameters | height                             | Target image height                                                                                                                             |
| dataset parameters    | image\_dataset\_items              | Array: consist of `imageUrl` and image `caption`                                                                                                |
| dataset parameters    | - image\_dataset\_items.assets\_id | images assets\_id, which can be found in step `Get image upload URL`                                                                            |
| components parameters | components                         | Array: consist of `name` and `args`, this is a common parameters configured for training.                                                       |
| components parameters | - components.name                  | Type of components, Enum: `face_crop_region`, `resize`, `face_restore`                                                                          |
| components parameters | - components.args                  | Detail values of components.name                                                                                                                |
| expert parameters     | expert\_setting                    | expert parameters.                                                                                                                              |
| expert parameters     | - instance\_prompt                 | Captions for all the training images, here is a guidance of how to make a effective prompt : [Click Here](/guides/model-apis-training-guidance) |
| expert parameters     | - batch\_size                      | batch size of training.                                                                                                                         |
| expert parameters     | - max\_train\_steps                | Max train steps, 500 is enought for lora model training.                                                                                        |
| expert parameters     | - ......                           | More expert parameters can be access at api reference.                                                                                          |

**Here is a example of how to start training:**

```bash  theme={"system"}
curl --location --request POST 'https://api.novita.ai/v3/training/style' \
--header 'Accept: <Accept>' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API Key}}' \
--data-raw '{
    "name": "test_style_01",
    "base_model": "v1-5-pruned-emaonly",
    "width": 512,
    "height": 512,
    "image_dataset_items": [
        {
          "assets_id": "34558688e2f42a0137ca2d5274a8cf43"
        },
        {
          "assets_id": "1231231243f42a0137ca2d5274a8cf43"
        }
    ],
    "expert_setting": {
        "instance_prompt": "Xstyle, of a young woman, profile shot, from side,sitting, looking at viewer, smiling, head tilt, eyes open,long black hair, glowing skin,light smile,cinematic lighting,dark environment",
        "class_prompt": "person"
    },
    "components": [
        {
            "name": "face_crop_region",
            "args": [
                {
                    "name": "ratio",
                    "value": "1"
                }
            ]
        },
        {
          "name": "resize",
          "args": [
              {"name": "width", "value": "512"},
              {"name": "height", "value": "512"}
          ]
        },
        {
          "name": "face_restore",
            "args": [
                {"name": "method", "value": "gfpgan_1.4"},
                {"name": "upscale", "value": "1.0"}
            ]
        }
    ]
}'
```

Response:

```bash  theme={"system"}
{
    "task_id": "d660cdd0-ab9b-4a55-8b78-4bc851051fb0"
}
```

The `task_id` is the unique identifier of the training task, which can be used to query the training status and results.

### 3. Get training status

#### 3.1 Get model training and deployment status

In this step, we will obtain the progress of model training and the status of model deployment after training

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/training/style?task_id=d660cdd0-ab9b-4a55-8b78-4bc851051fb0' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```bash  theme={"system"}
{
    "task_id": "d660cdd0-ab9b-4a55-8b78-4bc851051fb0",
    "task_status": "SUCCESS",
    "model_type": "",
    "models": [
        {
            "model_name": "model_1698904832_F2BB461625.safetensors",
            "model_status": "DEPLOYING"
        }
    ]
}
```

* `task_status`: The status of the training task, Enum: `UNKNOWN`, `QUEUING`, `TRAINING`, `SUCCESS`, `CANCELED`, `FAILED`.
* `model_status`: The status of the model, Enum: `DEPLOYING`, `SERVING`.
* `model_name`: The name of the model, which can be used to generate images in next step.

When the `task_status` is `SUCCESS`, the `model_status` is `SERVING` we can starting to use the lora model.

#### 3.2 Start using the trained model

After model deployed successfully, we can download the model files or generate images directly.

##### 3.2.1 Use the generated models to create images

In order to use the trained lora models, We need to add `model_name` into the `request` of endpoint `/v3/async/txt2img` or `/v3/async/img2img`. **Currently trained lora model can not be used in /v3 endpoint.**

Below is a example of how to generate images with trained model:

Please set the **`Content-Type`** header to **`application/json`** in your HTTP request to indicate that you are sending JSON data. Currently, **only JSON format is supported**.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/txt2img' \
--header 'Authorization: Bearer {{API Key}};' \
--header 'Content-Type;' \
--data '{
  "extra": {
    "response_image_type": "jpeg"
  },
  "request": {
    "model_name": "realisticVisionV51_v51VAE_94301.safetensors",
    "prompt": "a young woman",
    "negative_prompt": "bottle, bad face",
    "sd_vae": "",
    "loras": [
      {
        "model_name": "model_1698904832_F2BB461625.safetensors",
        "strength": 0.7
      }
    ],
    "embeddings": [
      {
        "model_name": ""
      }
    ],
    "hires_fix": {
      "target_width": 1024,
      "target_height": 768,
      "strength": 0.5
    },
    "refiner": {
      "switch_at": null
    },
    "width": 512,
    "height": 384,
    "image_num": 2,
    "steps": 20,
    "seed": 123,
    "clip_skip": 1,
    "guidance_scale": 7.5,
    "sampler_name": "Euler a"
  }
}'
```

`Response:`

```bash  theme={"system"}
{
    "code": 0,
    "msg": "",
    "data": {
        "task_id": "bec2bcfe-47c6-4536-af34-f26cfe6fd457"
    }
}
```

**Use `task_id` to get images**

HTTP status codes in the 2xx range indicate that the request has been successfully accepted, while status codes in the 5xx range indicate internal server errors.

You can get images url in `imgs` of response.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/task-result?task_id=bec2bcfe-47c6-4536-af34-f26cfe6fd457' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```js  theme={"system"}
{
  "task": {
    "task_id": "bec2bcfe-47c6-4536-af34-f26cfe6fd457",
    "status": "TASK_STATUS_SUCCEED",
    "reason": ""
  },
  "images": [
    {
      "image_url": "https://faas-output-image.s3.ap-southeast-1.amazonaws.com/dev/replace_object_a910c8f7-76ce-40bd-b805-f00f3ddd7dc1_0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20231019%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20231019T084537Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=b9ad40a5cb3aecf89602c15fe72d28be5d8a33e0bfe3656ce968295fde1aab31",
      "image_url_ttl": 3600,
      "image_type": "png"
    }
  ],
  "videos": [
    {
      "video_url": "https://faas-output-image.s3.ap-southeast-1.amazonaws.com/dev/replace_object_a910c8f7-76ce-40bd-b805-f00f3ddd7dc1_0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20231019%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20231019T084537Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=b9ad40a5cb3aecf89602c15fe72d28be5d8a33e0bfe3656ce968295fde1aab31",
      "video_url_ttl": "3600",
      "video_type": "png"
    }
  ]
}
```

#### 3.3 List training tasks

In this step, we can obtain all the info of trained models.

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/training?pagination.limit=10&pagination.cursor=c_0' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```js  theme={"system"}
{
    "tasks": [
        {
          "task_name": "test_01",
            "task_id": "a0c4cc90-0296-4972-a1d8-e6e227daf094",
            "task_type": "style",
            "task_status": "SUCCESS",
            "created_at": 1699325415,
            "models": [
                {
                    "model_name": "model_1699325939_E83A88DAC5.safetensors",
                    "model_status": "SERVING"
                }
            ]
        },
        {
          "task_name": "test_02",
          "task_id": "51e9bf41-8f7a-464d-b5ad-2fa217a1ec93",
          "task_type": "style",
          "task_status": "SUCCESS",
          "created_at": 1699267268,
          "models": [
              {
                  "model_name": "model_1699267603_27F0D9C81C.safetensors",
                  "model_status": "SERVING"
              }
          ]
        },
        {
          "task_name": "test_03",
            "task_id": "7bd205ab-63e9-452b-9a66-39c597000eaa",
            "task_type": "style",
            "task_status": "FAILED",
            "created_at": 1699264338,
            "models": []
        }
    ],
    "pagination": {
        "next_cursor": "c_10"
    }
}
```

* `task_name` : The name of the training task.
* `task_id` : The unique identifier of the training task, which can be used to query the training status and results.
* `task_type` : The type of the training task.
* `task_status`: The status of the training task, Enum: `UNKNOWN`, `QUEUING`, `TRAINING`, `SUCCESS`, `CANCELED`, `FAILED`.
* `created_at`: The time when the training task was created.
* `model`: The trained model.
* `model_name`: The sd name of the model.
* `model_status`: The status of the model, Enum: `DEPLOYING`, `SERVING`.

### 4. Training playground

You can also use our training playground to train models in a user-friendly way at: [Click Here](https://huggingface.co/spaces/novita-ai/Face-Stylization-Playground)

#### 4.1 Input Novita AI API Key, images and select training type

<Frame>
  <img height="430" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/training_playground01.png" />
</Frame>

#### 4.2 Switch to the inferencing tab and add more detail

<Frame>
  <img height="430" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/training_playground02.png" />
</Frame>

<Frame>
  <img height="430" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/training_playground03.png" />
</Frame>

#### Review the training results

<Frame>
  <img height="430" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/training_playground04.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).