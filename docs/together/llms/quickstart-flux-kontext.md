# Source: https://docs.together.ai/docs/quickstart-flux-kontext.md

> Learn how to use Flux's new in-context image generation models

# Quickstart: Flux Kontext

## Flux Kontext

Black Forest Labs has released FLUX Kontext with support on Together AI. These models allow you to generate and edit images through in-context image generation.

Unlike existing text-to-image models, FLUX.1 Kontext allows you to prompt with both text and images, and seamlessly extract and modify visual concepts to produce new, coherent renderings.

The Kontext family includes three models optimized for different use cases: Pro for balanced speed and quality, Max for maximum image fidelity, and Dev for development and experimentation.

## Generating an image

Here's how to use the new Kontext models:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  imageCompletion = client.images.generate(
      model="black-forest-labs/FLUX.1-kontext-pro",
      width=1536,
      height=1024,
      steps=28,
      prompt="make his shirt yellow",
      image_url="https://github.com/nutlope.png",
  )

  print(imageCompletion.data[0].url)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.generate({
      model: "black-forest-labs/FLUX.1-kontext-pro",
      width: 1536,
      height: 1024,
      steps: 28,
      prompt: "make his shirt yellow",
      image_url: "https://github.com/nutlope.png",
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
         "model": "black-forest-labs/FLUX.1-kontext-pro",
         "width": 1536,
         "height": 1024,
         "steps": 28,
         "prompt": "make his shirt yellow",
         "image_url": "https://github.com/nutlope.png"
       }'
  ```
</CodeGroup>

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=66b5f695ba162346d8079ab48b8f1de3" alt="" data-og-width="904" width="904" data-og-height="492" height="492" data-path="images/hassan-yellow-shirt.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=280&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=cd46f805ebdb73e6a437c6c9cc27e526 280w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=560&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=c4a2d6508e33ede4a7670d26e8423d6a 560w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=840&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=1fcbe3d062c2ca60cf785152728bdf27 840w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=1100&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=45ec4ec28b0e72b7534ebfbc253d7f9f 1100w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=1650&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=3009ea540ed84dbc06d69314337b7c63 1650w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=2500&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=745dce4b24cc380ac3cda271cee8fc15 2500w" />
</Frame>

## Available Models

Flux Kontext offers different models for various needs:

* **FLUX.1-kontext-pro**: Best balance of speed and quality (recommended)
* **FLUX.1-kontext-max**: Maximum image quality for production use
* **FLUX.1-kontext-dev**: Development model for testing

## Common Use Cases

* **Style Transfer**: Transform photos into different art styles (watercolor, oil painting, etc.)
* **Object Modification**: Change colors, add elements, or modify specific parts of an image
* **Scene Transformation**: Convert daytime to nighttime, change seasons, or alter environments
* **Character Creation**: Transform portraits into different styles or characters

## Key Parameters

Flux Kontext models support the following key parameters:

* `model`: Choose from `black-forest-labs/FLUX.1-kontext-pro`, `black-forest-labs/FLUX.1-kontext-max`, or `black-forest-labs/FLUX.1-kontext-dev`
* `prompt`: Text description of the transformation you want to apply
* `image_url`: URL of the reference image to transform
* `aspect_ratio`: Output aspect ratio (e.g., "1:1", "16:9", "9:16", "4:3", "3:2") - alternatively, you can use `width` and `height` for precise pixel dimensions
* `steps`: Number of diffusion steps (default: 28, higher values may improve quality)
* `seed`: Random seed for reproducible results

For complete parameter documentation, see the [Images Overview](/docs/images-overview#parameters).

See all available image models: [Image Models](/docs/serverless-models#image-models)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt