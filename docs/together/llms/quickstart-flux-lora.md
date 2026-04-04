# Source: https://docs.together.ai/docs/quickstart-flux-lora.md

# Quickstart: Flux LoRA Inference

Together AI now provides a high-speed endpoint for the FLUX.1 \[dev] model with integrated LoRA support. This enables swift and high-quality image generation using pre-trained LoRA adaptations for personalized outputs, unique styles, brand identities, and product-specific visualizations.

**Fine-tuning for FLUX LoRA is not yet available.**

## Generating an image using Flux LoRAs

Some Flux LoRA fine-tunes need to be activated using a trigger phrases that can be used in the prompt and can typically be found in the model cards. For example with: [https://huggingface.co/multimodalart/flux-tarot-v1](https://huggingface.co/multimodalart/flux-tarot-v1), you should use `in the style of TOK a trtcrd tarot style` to trigger the image generation.

You can add up to 2 LoRAs per image to combine the style from the different fine-tunes. The `scale` parameter allows you to specify the strength of each LoRA. Typically values of `0.3-1.2` will produce good results.

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()
  response = client.images.generate(
      prompt="a BLKLGHT image of man walking outside on rainy day",
      model="black-forest-labs/FLUX.1-dev-lora",
      width=1024,
      height=768,
      steps=28,
      n=1,
      response_format="url",
      image_loras=[
          {"path": "https://replicate.com/fofr/flux-black-light", "scale": 0.8},
          {
              "path": "https://huggingface.co/XLabs-AI/flux-RealismLora",
              "scale": 0.8,
          },
      ],
  )
  print(response.data[0].url)
  ```

  ```sh cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations"
  -H "Authorization: Bearer $TOGETHER_API_KEY"
  -H "Content-Type: application/json"
  -d '{
      "model": "black-forest-labs/FLUX.1-dev-lora",
      "prompt": "cute dog",
      "width": 1024,
      "height": 768,
      "steps": 28,
      "n": 1,
      "response_format": "url",
      "image_loras": [{"path":"https://huggingface.co/XLabs-AI/flux-RealismLora","scale":1},
          {"path": "https://huggingface.co/XLabs-AI/flux-RealismLora", "scale": 0.8}]
     }'
  ```
</CodeGroup>

## Acceptable LoRA URL formats

You can point to any URL that has a `.safetensors` file with a valid Flux LoRA fine-tune.

| Format                                        | Example                                                                                                                                                                                                                                        |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HuggingFace Repo Link                         | [https://huggingface.co/multimodalart/flux-tarot-v1](https://huggingface.co/multimodalart/flux-tarot-v1)                                                                                                                                       |
| HuggingFace Direct File Link with "resolve"\* | [https://huggingface.co/XLabs-AI/flux-lora-collection/resolve/main/anime\_lora.safetensors](https://huggingface.co/XLabs-AI/flux-lora-collection/resolve/main/anime_lora.safetensors)                                                          |
| Civit Download Link                           | [https://civitai.com/api/download/models/913438?type=Model\&format=SafeTensor](https://civitai.com/api/download/models/913438?type=Model\&format=SafeTensor)                                                                                   |
| Replicate Fine-tuned Flux Model Link          | [https://replicate.com/fofr/flux-black-light](https://replicate.com/fofr/flux-black-light)                                                                                                                                                     |
| Replicate Fine-tuned Flux Version Link        | [https://replicate.com/fofr/flux-black-light/versions/d0d48e298dcb51118c3f903817c833bba063936637a33ac52a8ffd6a94859af7](https://replicate.com/fofr/flux-black-light/versions/d0d48e298dcb51118c3f903817c833bba063936637a33ac52a8ffd6a94859af7) |
| Direct file link ending with ".safetensors"   | [https://mybucket.s3.amazonaws.com/my\_special\_lora.safetensors](https://mybucket.s3.amazonaws.com/my_special_lora.safetensors)                                                                                                               |

\*Note: the HuggingFace web page for a file ([https://huggingface.co/XLabs-AI/flux-lora-collection/blob/main/anime\_lora.safetensors](https://huggingface.co/XLabs-AI/flux-lora-collection/blob/main/anime_lora.safetensors)) will NOT work

If the safetensors file has incompatible keys, you'll get the message " has unused keys \<keys...>". This will happen if you pass a finetune of a non-flux model or an otherwise invalid file.

## Examples

The example below produces a realistic tarot card of a panda:

```py Python theme={null}
prompt = "a baby panda eating bamboo in the style of TOK a trtcrd tarot style"

response = client.images.generate(
    prompt=prompt,
    model="black-forest-labs/FLUX.1-dev-lora",
    width=1024,
    height=768,
    steps=28,
    n=1,
    response_format="url",
    image_loras=[
        {
            "path": "https://huggingface.co/multimodalart/flux-tarot-v1",
            "scale": 1,
        },
        {
            "path": "https://huggingface.co/Shakker-Labs/FLUX.1-dev-LoRA-add-details",
            "scale": 0.8,
        },
    ],
)
```

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=cb73a699bcb42f2deec002a9670cb4d6" alt="" data-og-width="1218" width="1218" data-og-height="918" height="918" data-path="images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a176678d92b45daa26c77ada7aa668b3 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=30d0981ee82e0beb8711bfdb78d3bb03 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=64a9e45ac4f261e8568a9d089b21f65d 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8077759db2f874c8daf5cf83e5d503ce 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a9c6a5082858a26e6990d556502964fd 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b64bfe2edff61a5e2ffe31803ddc557e 2500w" />
</Frame>

## Pricing

Your request costs \$0.035 per megapixel. For \$1, you can run this model approximately 29 times. Image charges are calculated by rounding up to the nearest megapixel.

Note: Due to high demand, FLUX.1 \[schnell] Free has a model specific rate limit of 10 img/min.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt