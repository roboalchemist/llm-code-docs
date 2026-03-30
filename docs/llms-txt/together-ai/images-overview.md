# Source: https://docs.together.ai/docs/images-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Generation

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

<img src="https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=4d99c87bb633262fdb932f3f9a9fa436" alt="Reference image: image-overview1.png" width="350" data-path="images/image-overview1.png" />

## Provide reference image

Some image models support editing or transforming an existing image. The parameter you use depends on the model:

| Parameter          | Type       | Models                                                     | Description                                |
| ------------------ | ---------- | ---------------------------------------------------------- | ------------------------------------------ |
| `image_url`        | `string`   | FLUX.1 Kontext (pro/max), FLUX.2 (pro/flex)                | A single image URL to edit or transform    |
| `reference_images` | `string[]` | FLUX.2 (pro/dev/flex), Gemini 3 Pro Image, Flash Image 2.5 | An array of image URLs to guide generation |

<Note>`reference_images` is recommended for FLUX.2 and Google models as it supports multiple input images. FLUX.2 \[pro] and \[flex] also accept `image_url` for single-image edits, but FLUX.2 \[dev], Gemini 3 Pro Image, and Flash Image 2.5 only support `reference_images`.</Note>

### Using `image_url` (Kontext models)

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

<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=2f4036b77e23ee90388200b71abfc7af" alt="Reference image: reference_image.png" width="989" height="360" data-path="images/reference_image.png" />

### Using `reference_images` (FLUX.2 & Google models)

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.images.generate(
      model="black-forest-labs/FLUX.2-pro",
      width=1024,
      height=768,
      prompt="Replace the color of the car to blue",
      reference_images=[
          "https://images.pexels.com/photos/3729464/pexels-photo-3729464.jpeg"
      ],
  )
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.images.generate({
    model: "black-forest-labs/FLUX.2-pro",
    width: 1024,
    height: 768,
    prompt: "Replace the color of the car to blue",
    reference_images: [
      "https://images.pexels.com/photos/3729464/pexels-photo-3729464.jpeg",
    ],
  });
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.2-pro",
         "width": 1024,
         "height": 768,
         "prompt": "Replace the color of the car to blue",
         "reference_images": ["https://images.pexels.com/photos/3729464/pexels-photo-3729464.jpeg"]
       }'
  ```
</CodeGroup>

For more details on multi-image editing, image indexing, and color control with FLUX.2, see the [FLUX.2 Quickstart](/docs/quickstart-flux#image-to-image-with-reference-images).

## Supported Models

See our [models page](/docs/serverless-models#image-models) for supported image models.

## Parameters

| Parameter          | Type    | Description                                                                              | Default      |
| ------------------ | ------- | ---------------------------------------------------------------------------------------- | ------------ |
| `prompt`           | string  | Text description of the image to generate                                                | **Required** |
| `model`            | string  | Model identifier                                                                         | **Required** |
| `width`            | integer | Image width in pixels                                                                    | 1024         |
| `height`           | integer | Image height in pixels                                                                   | 1024         |
| `n`                | integer | Number of images to generate (1-4)                                                       | 1            |
| `steps`            | integer | Diffusion steps (higher = better quality, slower)                                        | 1-50         |
| `seed`             | integer | Random seed for reproducibility                                                          | any          |
| `negative_prompt`  | string  | What to avoid in generation                                                              | -            |
| `image_url`        | string  | URL of a reference image to edit. Used by Kontext models.                                | -            |
| `reference_images` | array   | Array of image URLs for image-to-image editing. Used by FLUX.2 and Google models.        | -            |
| `frame_images`     | array   | **Required for Kling model.** Array of images to guide video generation, like keyframes. | -            |

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
<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4662cd539affb47b8b31d363690a809b" alt="Multiple generated image variations" width="1166" height="1190" data-path="images/variations.png" />

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

<img src="https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=4f81f0c9d03a7334a193c2416557a0be" alt="Reference image: dims.png" width="1391" height="990" data-path="images/dims.png" />

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

<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=c6dad7983bb96503032966b36ad41716" alt="Reference image: steps.png" width="1458" height="511" data-path="images/steps.png" />

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


Built with [Mintlify](https://mintlify.com).