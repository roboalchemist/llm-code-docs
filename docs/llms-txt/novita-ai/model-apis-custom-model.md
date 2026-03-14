# Source: https://novita.ai/docs/guides/model-apis-custom-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload Custom LoRA Models

<Tip>
  * Currently, the Model Upload feature only supports LoRA models, with a limit of 5 uploads per user. We plan to gradually lift these restrictions in the future;
  * The Model Upload feature is temporarily available free of charge. However, we may introduce a fee for this service in the future. Please stay tuned for future announcements;
  * If you have any questions, please contact our customer service or technical team through the [Discord Channel](https://discord.gg/YyPRAzwp7P).
</Tip>

Please follow the steps below to upload your custom LoRA models.

1. Log in to your account and go to the [Model Management Page](https://novita.ai/models-console/model-management).

2. Click the `Upload Model` button to upload your models.

3. Upload the LoRA model and fill in the form. Please note that the model name cannot be modified after submission.

4. After the model is uploaded successfully, you can use the model from the model list.

**For example:**

<Tip>
  In the following example, the LoRA model name `test_sd_name_in_api.safetensors` can be found in the `MODEL NAME IN API` column in your private model list.
</Tip>

```bash  theme={"system"}
curl --location --request POST 'https://api.novita.ai/v3/async/txt2img' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API Key}}' \
--data-raw '{
    "model_name": "AnythingV5_v5PrtRE.safetensors",
    "width": 512,
    "height": 768,
    "prompt": "a body stood high, behind him, looking down.",
    "negative_prompt": "",
    "sampler_name": "DPM++ 2S a Karras",
    "guidance_scale": 7.5,
    "steps": 30,
    "image_num": 1,
    "clip_skip": 0,
    "seed": -1,
    "loras": [
        {"model_name":"test_sd_name_in_api.safetensors", "strength":0.7}
    ]
}'
```


Built with [Mintlify](https://mintlify.com).