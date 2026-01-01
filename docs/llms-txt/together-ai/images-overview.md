# Source: https://docs.together.ai/docs/images-overview.md

# Images

> Generate high-quality images from text + image prompts.

## Generating an image

To query an image model, use the `.images` method and specify the image model you want to use.

<CodeGroup>
  ```py Python theme={null}
  client = Together()

  # Generate an image from a text prompt
  response = client.images.generate(
      prompt="A serene mountain landscape at sunset with a lake reflection",
      model="black-forest-labs/FLUX.1-schnell",
      steps=4,
  )

  print(f"Image URL: {response.data[0].url}")
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.generate({
      prompt: "A serene mountain landscape at sunset with a lake reflection",
      model: "black-forest-labs/FLUX.1-schnell",
      steps: 4,
    });

    console.log(response.data[0].url);
  }

  main();
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A serene mountain landscape at sunset with a lake reflection",
         "steps": 4
       }'
  ```
</CodeGroup>

Example response structure and output:

```json  theme={null}
{
  "id": "oFuwv7Y-2kFHot-99170ebf9e84e0ce-SJC",
  "model": "black-forest-labs/FLUX.1-schnell",
  "data": [
    {
      "index": 0,
      "url": "https://api.together.ai/v1/images/..."
    }
  ]
}
```

<img src="https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=4d99c87bb633262fdb932f3f9a9fa436" alt="Reference image: image-overview1.png" width="350" data-og-width="1024" data-og-height="1024" data-path="images/image-overview1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=280&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=8a8cc7b204ced18a0f54475d6c29d083 280w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=560&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=7b9316fc8048f5099c9fc93ea7d0f8f9 560w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=840&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=6c4e6b322d745bde355f796f173f3acf 840w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=1100&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=b508dae30e522a828fec8a36d1bcfdff 1100w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=1650&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=3975e1d0af34f521c5bdf143df8cd11a 1650w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=2500&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=0130a5593fd60a023b9e0960a4824464 2500w" />

## Provide reference image

Use a reference image to guide the generation:

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.images.generate(
      model="black-forest-labs/FLUX.1-kontext-pro",
      width=1024,
      height=768,
      prompt="Transform this into a watercolor painting",
      image_url="https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
  )
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.images.generate({
    model: "black-forest-labs/FLUX.1-kontext-pro",
    width: 1024,
    height: 768,
    prompt: "Transform this into a watercolor painting",
    image_url:
      "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
  });
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-kontext-pro",
         "width": 1024,
         "height": 768,
         "prompt": "Transform this into a watercolor painting",
         "image_url": "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg"
       }'
  ```
</CodeGroup>

Example output:

<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=2f4036b77e23ee90388200b71abfc7af" alt="Reference image: reference_image.png" data-og-width="989" width="989" data-og-height="360" height="360" data-path="images/reference_image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=280&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=09e764929470af3788d2be654ad50464 280w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=560&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=e45d47b542c051c2e2f375a4f357a79f 560w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=840&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=748b9876fb4984438c0acc635fa2314d 840w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=1100&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=da6a7a5a109aa3c7321871e17e020293 1100w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=1650&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=eb058db20b8898e80f62a2da77f23b6c 1650w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=2500&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4a5ba1b910dba43bee558540f35124f9 2500w" />

## Supported Models

See our [models page](/docs/serverless-models#image-models) for supported image models.

## Parameters

| Parameter         | Type    | Description                                                                              | Default      |
| ----------------- | ------- | ---------------------------------------------------------------------------------------- | ------------ |
| `prompt`          | string  | Text description of the image to generate                                                | **Required** |
| `model`           | string  | Model identifier                                                                         | **Required** |
| `width`           | integer | Image width in pixels                                                                    | 1024         |
| `height`          | integer | Image height in pixels                                                                   | 1024         |
| `n`               | integer | Number of images to generate (1-4)                                                       | 1            |
| `steps`           | integer | Diffusion steps (higher = better quality, slower)                                        | 1-50         |
| `seed`            | integer | Random seed for reproducibility                                                          | any          |
| `negative_prompt` | string  | What to avoid in generation                                                              | -            |
| `frame_images`    | array   | **Required for Kling model.** Array of images to guide video generation, like keyframes. | -            |

* `prompt` is required for all models except Kling
* `width` and `height` will rely on defaults unless otherwise specified - options for dimensions differ by model
* Flux Schnell and Kontext \[Pro/Max/Dev] models use the `aspect_ratio` parameter to set the output image size whereas Flux.1 Pro, Flux 1.1 Pro, and Flux.1 Dev use `width` and `height` parameters.

## Generating Multiple Variations

Generate multiple variations of the same prompt to choose from:

<CodeGroup>
  ```py Python theme={null}
  response = client.images.generate(
      prompt="A cute robot assistant helping in a modern office",
      model="black-forest-labs/FLUX.1-schnell",
      n=4,
      steps=4,
  )

  print(f"Generated {len(response.data)} variations")
  for i, image in enumerate(response.data):
      print(f"Variation {i+1}: {image.url}")
  ```

  ```ts TypeScript theme={null}
  const response = await together.images.generate({
    prompt: "A cute robot assistant helping in a modern office",
    model: "black-forest-labs/FLUX.1-schnell",
    n: 4,
    steps: 4,
  });

  console.log(`Generated ${response.data.length} variations`);

  response.data.forEach((image, i) => {
    console.log(`Variation ${i + 1}: ${image.url}`);
  });
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A cute robot assistant helping in a modern office",
         "n": 4,
         "steps": 4
       }'
  ```
</CodeGroup>

Example output:
<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4662cd539affb47b8b31d363690a809b" alt="Multiple generated image variations" data-og-width="1166" width="1166" data-og-height="1190" height="1190" data-path="images/variations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=280&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=93ce50657e7617eede86cdc398a8cae8 280w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=560&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=5faa41043c62d7de67af33a993ecdde9 560w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=840&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=52a3acce05e8bcf79199cdb6017f7532 840w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=1100&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=97a98672d86219304b56546b0f25d197 1100w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=1650&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=aa884d182ac397f5d42095d73662461f 1650w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=2500&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=727080d2779f9ca84713b1c4e0b92c9d 2500w" />

## Custom Dimensions & Aspect Ratios

Different aspect ratios for different use cases:

<CodeGroup>
  ```py Python theme={null}
  # Square - Social media posts, profile pictures
  response_square = client.images.generate(
      prompt="A peaceful zen garden with a stone path",
      model="black-forest-labs/FLUX.1-schnell",
      width=1024,
      height=1024,
      steps=4,
  )

  # Landscape - Banners, desktop wallpapers
  response_landscape = client.images.generate(
      prompt="A peaceful zen garden with a stone path",
      model="black-forest-labs/FLUX.1-schnell",
      width=1344,
      height=768,
      steps=4,
  )

  # Portrait - Mobile wallpapers, posters
  response_portrait = client.images.generate(
      prompt="A peaceful zen garden with a stone path",
      model="black-forest-labs/FLUX.1-schnell",
      width=768,
      height=1344,
      steps=4,
  )
  ```

  ```ts TypeScript theme={null}
  // Square - Social media posts, profile pictures
  const response_square = await together.images.generate({
    prompt: "A peaceful zen garden with a stone path",
    model: "black-forest-labs/FLUX.1-schnell",
    width: 1024,
    height: 1024,
    steps: 4,
  });

  // Landscape - Banners, desktop wallpapers
  const response_landscape = await together.images.generate({
    prompt: "A peaceful zen garden with a stone path",
    model: "black-forest-labs/FLUX.1-schnell",
    width: 1344,
    height: 768,
    steps: 4,
  });

  // Portrait - Mobile wallpapers, posters
  const response_portrait = await together.images.generate({
    prompt: "A peaceful zen garden with a stone path",
    model: "black-forest-labs/FLUX.1-schnell",
    width: 768,
    height: 1344,
    steps: 4,
  });
  ```

  ```curl cURL theme={null}
  # Square - Social media posts, profile pictures
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A peaceful zen garden with a stone path",
         "width": 1024,
         "height": 1024,
         "steps": 4
       }'

  # Landscape - Banners, desktop wallpapers
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A peaceful zen garden with a stone path",
         "width": 1344,
         "height": 768,
         "steps": 4
       }'

  # Portrait - Mobile wallpapers, posters
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A peaceful zen garden with a stone path",
         "width": 768,
         "height": 1344,
         "steps": 4
       }'
  ```
</CodeGroup>

<img src="https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=4f81f0c9d03a7334a193c2416557a0be" alt="Reference image: dims.png" data-og-width="1391" width="1391" data-og-height="990" height="990" data-path="images/dims.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=280&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=fb9e0821836ed9861a522698f5948224 280w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=560&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=31194ec41bed9963e9a7324149eb1551 560w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=840&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=062be3089cbc119efac695191a12e5bf 840w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=1100&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=0d77614e227264a1c2c7bae6d2fe12ad 1100w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=1650&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=a205e3cd5d3de30a59af5ddc0cfbadf4 1650w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=2500&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=868d9308fc95e6b4c518cb98a3b01797 2500w" />

## Quality Control with Steps

Compare different step counts for quality vs. speed:

```python  theme={null}
import time

prompt = "A majestic mountain landscape"
step_counts = [1, 6, 12]

for steps in step_counts:
    start = time.time()
    response = client.images.generate(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell",
        steps=steps,
        seed=42,  # Same seed for fair comparison
    )
    elapsed = time.time() - start
    print(f"Steps: {steps} - Generated in {elapsed:.2f}s")
```

<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=c6dad7983bb96503032966b36ad41716" alt="Reference image: steps.png" data-og-width="1458" width="1458" data-og-height="511" height="511" data-path="images/steps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=280&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4ac6dc13d95356376c441407f9e3aea3 280w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=560&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4441ef2ff0f4f656dfe005c46d001b1d 560w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=840&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=ed6e70593fcdbd62d8387a57b1e05e4c 840w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=1100&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=b28573546f8b32bbb049a6f7d5de7dd0 1100w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=1650&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=60a317f47e10d95ed43d6e32e194fc2b 1650w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=2500&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=d32a39c2ef3ac49c5d0e48e6b3f2d87f 2500w" />

## Base64 Images

If you prefer the image data to be embedded directly in the response, set `response_format` to "base64".

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.images.generate(
      model="black-forest-labs/FLUX.1-schnell",
      prompt="a cat in outer space",
      response_format="base64",
  )

  print(response.data[0].b64_json)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const response = await client.images.generate({
    model: "black-forest-labs/FLUX.1-schnell",
    prompt: "A cat in outer space",
    response_format: "base64",
  });

  console.log(response.data[0].b64_json);
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A cat in outer space",
         "response_format": "base64"
       }'
  ```
</CodeGroup>

When you do, the model response includes a new `b64_json` field that contains the image encoded as a base64 string.

```json  theme={null}
{
  "id": "oNM6X9q-2kFHot-9aa9c4c93aa269a2-PDX",
  "data": [
    {
      "b64_json": "/9j/4AAQSkZJRgABAQA",
      "index": 0,
      "type": null,
      "timings": {
        "inference": 0.7992482790723443
      }
    }
  ],
  "model": "black-forest-labs/FLUX.1-schnell",
  "object": "list"
}

```

## Safety Checker

We have a built in safety checker that detects NSFW words but you can disable it by passing in `disable_safety_checker=True`. This works for every model except Flux Schnell Free and Flux Pro. If the safety checker is triggered and not disabled, it will return a `422 Unprocessable Entity`.

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.images.generate(
      prompt="a flying cat",
      model="black-forest-labs/FLUX.1-schnell",
      steps=4,
      disable_safety_checker=True,
  )

  print(response.data[0].url)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.generate({
      prompt: "a flying cat",
      model: "black-forest-labs/FLUX.1-schnell",
      steps: 4,
      disable_safety_checker: true,
    });

    console.log(response.data[0].url);
  }

  main();
  ```
</CodeGroup>

## Troubleshooting

**Image doesn't match prompt well**

* Make prompt more descriptive and specific
* Add style references (e.g., "National Geographic style")
* Use negative prompts to exclude unwanted elements
* Try increasing steps to 30-40

**Poor image quality**

* Increase `steps` to 30-40 for production
* Add quality modifiers: "highly detailed", "8k", "professional"
* Use negative prompt: "blurry, low quality, distorted, pixelated"
* Try a higher-tier model

**Inconsistent results**

* Use `seed` parameter for reproducibility
* Keep the same seed when testing variations
* Generate multiple variations with `n` parameter

**Wrong dimensions or aspect ratio**

* Specify `width` and `height` explicitly
* Common ratios:
  * Square: 1024x1024
  * Landscape: 1344x768
  * Portrait: 768x1344
* Ensure dimensions are multiples of 8


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt