# Source: https://docs.together.ai/docs/quickstart-flux-2.md

> Learn how to use FLUX.2, the next generation image model with advanced prompting capabilities

# Quickstart: FLUX.2

## FLUX.2

Black Forest Labs has released FLUX.2 with support on Together AI. FLUX.2 is the next generation of image models, featuring enhanced control through JSON structured prompts, HEX color code support, reference image editing, and exceptional text rendering capabilities.

Four model variants are available:

| Model              | Best For                | Key Features                                        |
| ------------------ | ----------------------- | --------------------------------------------------- |
| **FLUX.2 \[max]**  | Ultimate quality        | Highest fidelity output, best for premium use cases |
| **FLUX.2 \[pro]**  | Maximum quality         | Up to 9 MP output, fastest generation               |
| **FLUX.2 \[dev]**  | Development & iteration | Great balance of quality and flexibility            |
| **FLUX.2 \[flex]** | Maximum customization   | Adjustable steps & guidance, better typography      |

<Tip>
  **Which model should I use?**

  * Use **\[max]** for the ultimate quality and fidelity in premium production workloads
  * Use **\[pro]** for production workloads requiring high quality and speed
  * Use **\[dev]** for development, experimentation, and when you need a balance of quality and control
  * Use **\[flex]** when you need maximum control over generation parameters or require exceptional typography
</Tip>

## Generating an image

Here's how to generate images with FLUX.2:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.images.generate(
      model="black-forest-labs/FLUX.2-pro",
      prompt="A mountain landscape at sunset with golden light reflecting on a calm lake",
      width=1024,
      height=768,
  )

  print(response.data[0].url)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.create({
      model: "black-forest-labs/FLUX.2-pro",
      prompt: "A mountain landscape at sunset with golden light reflecting on a calm lake",
      width: 1024,
      height: 768,
    });

    console.log(response.data[0].url);
  }

  main();
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "black-forest-labs/FLUX.2-pro",
      "prompt": "A mountain landscape at sunset with golden light reflecting on a calm lake",
      "width": 1024,
      "height": 768
    }'
  ```
</CodeGroup>

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/1.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=ff5b67773912f821895e91f012b230a9" data-og-width="1024" data-og-height="768" data-path="images/flux2_images/1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/1.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=707005b7ebe38b36016d3233281fcd17 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/1.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=1b968521ee847a5edd4113bfab30e6fb 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/1.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=d78ae2a21eac91892c8698fd6aae5224 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/1.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=ff8665c2592e639781d3b964e33f2690 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/1.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=0c6b2d50e5aff9dd7d60883813d198e6 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/1.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=4680fb6fa8c1b4b00cdcd69774d60fb8 2500w" />

**Using FLUX.2 \[dev]**

The dev variant offers a great balance for development and iteration:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.images.generate(
      model="black-forest-labs/FLUX.2-dev",
      prompt="A modern workspace with a laptop, coffee cup, and plants, natural lighting",
      width=1024,
      height=768,
      steps=20,
  )

  print(response.data[0].url)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.create({
      model: "black-forest-labs/FLUX.2-dev",
      prompt: "A modern workspace with a laptop, coffee cup, and plants, natural lighting",
      width: 1024,
      height: 768,
      steps: 20,
    });

    console.log(response.data[0].url);
  }

  main();
  ```
</CodeGroup>

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/2.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=69a0a34677fc2e7e923834ff1c863865" data-og-width="1024" data-og-height="768" data-path="images/flux2_images/2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/2.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=a2ebc914febf10863394235821bc9fed 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/2.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=66d21011421481abcab85c9ee2941935 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/2.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=3cc7fddaea27d2074f741f45d3811f37 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/2.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=58e2444cb2293e5551d09ea94788ff80 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/2.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=8734811f7d6dff5d1d445bb94506a94a 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/2.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=0c7398af126fc3e8d561c76f97bc56b3 2500w" />

**Using FLUX.2 \[flex]**

The flex variant provides maximum customization with `steps` and `guidance` parameters. It also excels at typography and text rendering.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.images.generate(
      model="black-forest-labs/FLUX.2-flex",
      prompt="A vintage coffee shop sign with elegant typography reading 'The Daily Grind' in art deco style",
      width=1024,
      height=768,
      steps=28,
      guidance=7.5,
  )

  print(response.data[0].url)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.create({
      model: "black-forest-labs/FLUX.2-flex",
      prompt: "A vintage coffee shop sign with elegant typography reading 'The Daily Grind' in art deco style",
      width: 1024,
      height: 768,
      steps: 28,
      guidance: 7.5,
    });

    console.log(response.data[0].url);
  }

  main();
  ```
</CodeGroup>

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/3.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=05dadbcabdf279eaf78dc1f3b3e42743" data-og-width="1024" data-og-height="768" data-path="images/flux2_images/3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/3.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=a8e07c4f5a34ff189ce2ea4c30037f57 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/3.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=14c365a2bff2f0a79d153fed518324dd 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/3.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=a60372b4d672dddafce1bfae347d0864 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/3.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=9d5d69622d002deeadc81bd7a9ff780e 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/3.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=a217d55a00e1565adf2d8d56a88fd296 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/3.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=fc3ae3ff2d743032db8991bf5ccd5822 2500w" />

## Parameters

**Common Parameters (All Models)**

| Parameter           | Type    | Description                                        | Default      |
| ------------------- | ------- | -------------------------------------------------- | ------------ |
| `prompt`            | string  | Text description of the image to generate          | **Required** |
| `width`             | integer | Image width in pixels (256-1920)                   | 1024         |
| `height`            | integer | Image height in pixels (256-1920)                  | 768          |
| `seed`              | integer | Seed for reproducibility                           | Random       |
| `prompt_upsampling` | boolean | Automatically enhance prompt for better generation | true         |
| `output_format`     | string  | Output format: `jpeg` or `png`                     | jpeg         |
| `reference_images`  | array   | Reference image URL(s) for image-to-image editing  | -            |

**Additional Parameters for \[dev] and \[flex]**

FLUX.2 \[dev] and FLUX.2 \[flex] support additional parameters:

| Parameter  | Type    | Description                                                 | Default       |
| ---------- | ------- | ----------------------------------------------------------- | ------------- |
| `steps`    | integer | Number of inference steps (higher = better quality, slower) | Model default |
| `guidance` | float   | Guidance scale (higher values follow prompt more closely)   | Model default |

## Image-to-Image with Reference Images

FLUX.2 supports powerful image-to-image editing using the `reference_images` parameter. Pass one or more image URLs to guide generation.

**Core Capabilities:**

| Capability                  | Description                                                    |
| --------------------------- | -------------------------------------------------------------- |
| **Multi-reference editing** | Use multiple images in a single edit                           |
| **Sequential edits**        | Edit images iteratively                                        |
| **Color control**           | Specify exact colors using hex values or reference images      |
| **Image indexing**          | Reference specific images by number: "the jacket from image 2" |
| **Natural language**        | Describe elements naturally: "the woman in the blue dress"     |

**Single Reference Image**

Edit or transform a single input image:

```python  theme={null}
from together import Together

client = Together()

response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt="Replace the color of the car to blue",
    width=1024,
    height=768,
    reference_images=[
        "https://images.pexels.com/photos/3729464/pexels-photo-3729464.jpeg"
    ],
)

print(response.data[0].url)
```

<div style={{display: 'flex', alignItems: 'center', gap: '16px', margin: '20px 0'}}>
  <img src="https://images.pexels.com/photos/3729464/pexels-photo-3729464.jpeg" style={{width: '300px', height: '200px', objectFit: 'cover', borderRadius: '6px'}} />

  <span style={{fontSize: '24px', color: '#888'}}>→</span>

  <img src="https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/743703bf-6869-4185-9ba3-d9570abbd495.jpg?fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=5939a3d9b20a31a32f72180b21907697" style={{width: '300px', height: '200px', objectFit: 'cover', borderRadius: '6px'}} data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/flux2_images/743703bf-6869-4185-9ba3-d9570abbd495.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/743703bf-6869-4185-9ba3-d9570abbd495.jpg?w=280&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=7b34600d945e57637cc88c2795da61fa 280w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/743703bf-6869-4185-9ba3-d9570abbd495.jpg?w=560&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=5bf5d5c50b94dd3c5f628baea0bca70a 560w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/743703bf-6869-4185-9ba3-d9570abbd495.jpg?w=840&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=0979cabe3f6c5eca3e9fa48edaa95291 840w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/743703bf-6869-4185-9ba3-d9570abbd495.jpg?w=1100&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=7fc53eb237a310a3976677ed9b6c2459 1100w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/743703bf-6869-4185-9ba3-d9570abbd495.jpg?w=1650&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=5fc78f0e7215ec590c6cd5948473ee20 1650w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/743703bf-6869-4185-9ba3-d9570abbd495.jpg?w=2500&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=ba71618f10204cb1d9a2d95642565c5c 2500w" />
</div>

**Multiple Reference Images**

Combine elements from multiple images. Reference them by index (image 1, image 2, etc.):

```python  theme={null}
from together import Together

client = Together()

response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt="The person from image 1 is petting the cat from image 2, the bird from image 3 is next to them",
    width=1024,
    height=768,
    reference_images=[
        "https://t4.ftcdn.net/jpg/03/83/25/83/360_F_383258331_D8imaEMl8Q3lf7EKU2Pi78Cn0R7KkW9o.jpg",
        "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
        "https://images.unsplash.com/photo-1486365227551-f3f90034a57c",
    ],
)

print(response.data[0].url)
```

<div style={{display: 'flex', alignItems: 'center', gap: '12px', margin: '16px 0', flexWrap: 'wrap'}}>
  <div style={{display: 'flex', gap: '6px'}}>
    <img src="https://t4.ftcdn.net/jpg/03/83/25/83/360_F_383258331_D8imaEMl8Q3lf7EKU2Pi78Cn0R7KkW9o.jpg" style={{width: '80px', height: '80px', objectFit: 'cover', borderRadius: '6px'}} />

    <img src="https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg" style={{width: '80px', height: '80px', objectFit: 'cover', borderRadius: '6px'}} />

    <img src="https://images.unsplash.com/photo-1486365227551-f3f90034a57c" style={{width: '80px', height: '80px', objectFit: 'cover', borderRadius: '6px'}} />
  </div>

  <span style={{fontSize: '20px', color: '#888'}}>→</span>

  <img src="https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/2ecf17ed-2544-497d-8356-583f96974405.jpg?fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=8ff2564f9ddeaef1cb82d9da91e87bdc" style={{width: '260px', height: '195px', objectFit: 'cover', borderRadius: '6px'}} data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/flux2_images/2ecf17ed-2544-497d-8356-583f96974405.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/2ecf17ed-2544-497d-8356-583f96974405.jpg?w=280&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=4f60451f622d7ebf95deb070de647bb3 280w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/2ecf17ed-2544-497d-8356-583f96974405.jpg?w=560&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=313a1e1c2c8520a7ad51161ed79b6425 560w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/2ecf17ed-2544-497d-8356-583f96974405.jpg?w=840&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=2f4359f7490291a233deb1ad429fb353 840w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/2ecf17ed-2544-497d-8356-583f96974405.jpg?w=1100&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=2fcdc7fccfadc5d2fc958324c55baea3 1100w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/2ecf17ed-2544-497d-8356-583f96974405.jpg?w=1650&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=e2443e6bd1090f8a4f8064eba015d380 1650w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/2ecf17ed-2544-497d-8356-583f96974405.jpg?w=2500&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=be27ef2302db457cfacd700273c3cd3c 2500w" />
</div>

**Using Image Indexing**

Reference specific images by their position in the array:

```python  theme={null}
from together import Together

client = Together()

response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt="Replace the top of the person from image 2 with the one from image 1",
    width=1024,
    height=768,
    reference_images=[
        "https://img.freepik.com/free-photo/designer-working-3d-model_23-2149371896.jpg",
        "https://img.freepik.com/free-photo/handsome-young-cheerful-man-with-arms-crossed_171337-1073.jpg",
    ],
)

print(response.data[0].url)
```

<div style={{display: 'flex', alignItems: 'center', gap: '16px', margin: '20px 0', flexWrap: 'wrap'}}>
  <div style={{display: 'flex', gap: '10px'}}>
    <img src="https://img.freepik.com/free-photo/designer-working-3d-model_23-2149371896.jpg" style={{width: '150px', height: '113px', objectFit: 'cover', borderRadius: '8px'}} />

    <img src="https://img.freepik.com/free-photo/handsome-young-cheerful-man-with-arms-crossed_171337-1073.jpg" style={{width: '150px', height: '113px', objectFit: 'cover', borderRadius: '8px'}} />
  </div>

  <span style={{fontSize: '28px', color: '#888'}}>→</span>

  <img src="https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/826c4569-06fd-4fdc-b3b0-1b1833da89a0.jpg?fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=1837feeb10b479f481a8a14ec818429c" style={{width: '150px', height: '113px', objectFit: 'cover', borderRadius: '8px'}} data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/flux2_images/826c4569-06fd-4fdc-b3b0-1b1833da89a0.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/826c4569-06fd-4fdc-b3b0-1b1833da89a0.jpg?w=280&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=bb1eaf895c848d9685e0327a1ac6ef23 280w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/826c4569-06fd-4fdc-b3b0-1b1833da89a0.jpg?w=560&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=3c709f70a09f6c47d4ca1cb97fb54d27 560w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/826c4569-06fd-4fdc-b3b0-1b1833da89a0.jpg?w=840&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=01f6e9f1c505ba31b19dfbfd72ba7bae 840w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/826c4569-06fd-4fdc-b3b0-1b1833da89a0.jpg?w=1100&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=fbe867202fce0ab31c32cf1f4749af51 1100w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/826c4569-06fd-4fdc-b3b0-1b1833da89a0.jpg?w=1650&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=40c9f10f25c9460b23b653eb0beb3724 1650w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/826c4569-06fd-4fdc-b3b0-1b1833da89a0.jpg?w=2500&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=4d9d69b8588e1d4ae9ec367da7e2fb98 2500w" />
</div>

**Using Natural Language**

FLUX.2 understands the content in your images, so you can describe elements naturally:

```python  theme={null}
from together import Together

client = Together()

response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt="""The man is leaning against the wall reading a newspaper with the title "FLUX.2"
The woman is walking past him, carrying one of the tote bags and wearing the black boots.
The focus is on their contrasting styles — her relaxed, creative vibe versus his formal look.""",
    width=1024,
    height=768,
    reference_images=[
        "https://img.freepik.com/free-photo/handsome-young-cheerful-man-with-arms-crossed_171337-1073.jpg",
        "https://plus.unsplash.com/premium_photo-1690407617542-2f210cf20d7e",
        "https://www.ariat.com/dw/image/v2/AAML_PRD/on/demandware.static/-/Sites-ARIAT/default/dw00f9b649/images/zoom/10016291_3-4_front.jpg",
        "https://i.pinimg.com/736x/dc/71/1c/dc711cc4c3ebafcd21f2a61efe8fd6cd.jpg",
    ],
)

print(response.data[0].url)
```

<div style={{display: 'flex', alignItems: 'center', gap: '12px', margin: '16px 0', flexWrap: 'wrap'}}>
  <div style={{display: 'flex', gap: '6px'}}>
    <img src="https://img.freepik.com/free-photo/handsome-young-cheerful-man-with-arms-crossed_171337-1073.jpg" style={{width: '70px', height: '70px', objectFit: 'cover', borderRadius: '6px'}} />

    <img src="https://plus.unsplash.com/premium_photo-1690407617542-2f210cf20d7e" style={{width: '70px', height: '70px', objectFit: 'cover', borderRadius: '6px'}} />

    <img src="https://www.ariat.com/dw/image/v2/AAML_PRD/on/demandware.static/-/Sites-ARIAT/default/dw00f9b649/images/zoom/10016291_3-4_front.jpg" style={{width: '70px', height: '70px', objectFit: 'cover', borderRadius: '6px'}} />

    <img src="https://i.pinimg.com/736x/dc/71/1c/dc711cc4c3ebafcd21f2a61efe8fd6cd.jpg" style={{width: '70px', height: '70px', objectFit: 'cover', borderRadius: '6px'}} />
  </div>

  <span style={{fontSize: '20px', color: '#888'}}>→</span>

  <img src="https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/7d932be4-3e3f-4310-b6da-f530855c6b0b.jpg?fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=fe14655e61b0dccb454c8a9f61738da1" style={{width: '180px', height: '135px', objectFit: 'cover', borderRadius: '6px'}} data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/flux2_images/7d932be4-3e3f-4310-b6da-f530855c6b0b.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/7d932be4-3e3f-4310-b6da-f530855c6b0b.jpg?w=280&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=68de614c9233b064227f5790a62cb42e 280w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/7d932be4-3e3f-4310-b6da-f530855c6b0b.jpg?w=560&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=a685ddc90696368b1226bb7d88a5037b 560w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/7d932be4-3e3f-4310-b6da-f530855c6b0b.jpg?w=840&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=00bc242a3f865e3814033c08756e07c0 840w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/7d932be4-3e3f-4310-b6da-f530855c6b0b.jpg?w=1100&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=69ec6caabaa04050af98f2f27d8a2d72 1100w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/7d932be4-3e3f-4310-b6da-f530855c6b0b.jpg?w=1650&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=f55c8275c9daceb0ab60c0f1f850e63b 1650w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/7d932be4-3e3f-4310-b6da-f530855c6b0b.jpg?w=2500&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=b125e60a657e09b0c08161897b233ecb 2500w" />
</div>

**Color Editing with Reference Images**

To change colors precisely, provide a color swatch image as a reference:

```python  theme={null}
from together import Together

client = Together()

response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt="Change the color of the gloves to the color of image 2",
    width=1024,
    height=768,
    reference_images=[
        "https://cdn.intellemo.ai/int-stock/62c6cc300a6a222fb36a2c8e/62c6cc320a6a222fb36a2c8f-v376/premium_boxing_gloves_from_top_brand_l.jpg",
        "https://shop.reformcph.com/cdn/shop/files/Blue_9da983c6-f823-4205-bca1-b3b8470657cf_grande.png",
    ],
)

print(response.data[0].url)
```

<div style={{display: 'flex', alignItems: 'center', gap: '12px', margin: '16px 0', flexWrap: 'wrap'}}>
  <div style={{display: 'flex', gap: '6px'}}>
    <img src="https://cdn.intellemo.ai/int-stock/62c6cc300a6a222fb36a2c8e/62c6cc320a6a222fb36a2c8f-v376/premium_boxing_gloves_from_top_brand_l.jpg" style={{width: '180px', height: '135px', objectFit: 'cover', borderRadius: '6px'}} />

    <img src="https://shop.reformcph.com/cdn/shop/files/Blue_9da983c6-f823-4205-bca1-b3b8470657cf_grande.png" style={{width: '180px', height: '135px', objectFit: 'cover', borderRadius: '6px'}} />
  </div>

  <span style={{fontSize: '20px', color: '#888'}}>→</span>

  <img src="https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/9b88608b-d563-4e6e-ad7a-fbadc48187c8.jpg?fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=989cbfd3d66150a55fa8ce64864e3c1d" style={{width: '180px', height: '135px', objectFit: 'cover', borderRadius: '6px'}} data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/flux2_images/9b88608b-d563-4e6e-ad7a-fbadc48187c8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/9b88608b-d563-4e6e-ad7a-fbadc48187c8.jpg?w=280&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=3540f9b50c65435814c3258315c39cb9 280w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/9b88608b-d563-4e6e-ad7a-fbadc48187c8.jpg?w=560&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=16f55e13c10ab25bb4d753282a5482e2 560w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/9b88608b-d563-4e6e-ad7a-fbadc48187c8.jpg?w=840&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=ed883d6dc510ba7ad76e2cac8d6347e3 840w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/9b88608b-d563-4e6e-ad7a-fbadc48187c8.jpg?w=1100&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=63cc37eddeba6a3b4e9555bfec9f39ef 1100w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/9b88608b-d563-4e6e-ad7a-fbadc48187c8.jpg?w=1650&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=82fb51a95f69e711c5d534b73e39387c 1650w, https://mintcdn.com/togetherai-52386018/2TbiTdXLPmg4EhsP/images/flux2_images/9b88608b-d563-4e6e-ad7a-fbadc48187c8.jpg?w=2500&fit=max&auto=format&n=2TbiTdXLPmg4EhsP&q=85&s=d79e02b8d0729c72e2bea518e141a64d 2500w" />
</div>

**Best Practices for Reference Images**

1. **Use image indexing** — Reference images by number ("image 1", "image 2") for precise control
2. **Be descriptive** — Clearly describe what you want to change or combine
3. **Use high-quality inputs** — Better input images lead to better results
4. **Combine with HEX colors** — Use specific color codes or color swatch images for precise color changes

## JSON Structured Prompts

FLUX.2 is trained to understand structured JSON prompts, giving you precise control over subjects, composition, lighting, and camera settings.

**Basic JSON Prompt Structure**

```python  theme={null}
from together import Together

client = Together()

json_prompt = """{
  "scene": "Professional studio product photography setup",
  "subjects": [
    {
      "type": "coffee mug",
      "description": "Minimalist ceramic mug with steam rising from hot coffee",
      "pose": "Stationary on surface",
      "position": "foreground",
      "color_palette": ["matte black ceramic"]
    }
  ],
  "style": "Ultra-realistic product photography",
  "color_palette": ["matte black", "concrete gray", "soft white highlights"],
  "lighting": "Three-point softbox setup with soft, diffused highlights",
  "mood": "Clean, professional, minimalist",
  "background": "Polished concrete surface with studio backdrop",
  "composition": "rule of thirds",
  "camera": {
    "angle": "high angle",
    "distance": "medium shot",
    "focus": "sharp on subject",
    "lens": "85mm",
    "f-number": "f/5.6",
    "ISO": 200
  }
}"""

response = client.images.generate(
    model="black-forest-labs/FLUX.2-dev",  # Can also use FLUX.2-pro or FLUX.2-flex
    prompt=json_prompt,
    width=1024,
    height=768,
    steps=20,
)

print(response.data[0].url)
```

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/4.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=19c6b34bdbcb054a6b4b362858533e67" data-og-width="1024" data-og-height="768" data-path="images/flux2_images/4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/4.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=0b2e59fbd73b26bdebf09e0776e00abb 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/4.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=49f3b0fb238beeb790fab308ff98c80d 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/4.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=4844cb81a54ec602fbcd3f2d36d5c5ad 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/4.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=fd1079849f9f2db596cd4848559fc114 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/4.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=1537ae45da1139ce99b417e33d3c8d87 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/4.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=745da2a3a6944a2b0a4a46cac638c334 2500w" />

**JSON Schema Reference**

Here's the recommended schema for structured prompts:

```json  theme={null}
{
  "scene": "Overall scene setting or location",
  "subjects": [
    {
      "type": "Type of subject (e.g., person, object)",
      "description": "Physical attributes, clothing, accessories",
      "pose": "Action or stance",
      "position": "foreground | midground | background"
    }
  ],
  "style": "Artistic rendering style",
  "color_palette": ["color 1", "color 2", "color 3"],
  "lighting": "Lighting condition and direction",
  "mood": "Emotional atmosphere",
  "background": "Background environment details",
  "composition": "rule of thirds | golden spiral | minimalist negative space | ...",
  "camera": {
    "angle": "eye level | low angle | bird's-eye | ...",
    "distance": "close-up | medium shot | wide shot | ...",
    "focus": "deep focus | selective focus | sharp on subject",
    "lens": "35mm | 50mm | 85mm | ...",
    "f-number": "f/2.8 | f/5.6 | ...",
    "ISO": 200
  },
  "effects": ["lens flare", "film grain", "soft bloom"]
}
```

**Composition Options**

| Option                      | Description                  |
| --------------------------- | ---------------------------- |
| `rule of thirds`            | Classic balanced composition |
| `golden spiral`             | Fibonacci-based natural flow |
| `minimalist negative space` | Clean, spacious design       |
| `diagonal energy`           | Dynamic, action-oriented     |
| `vanishing point center`    | Depth and perspective focus  |
| `triangular arrangement`    | Stable, hierarchical layout  |

**Camera Angle Options**

| Angle               | Use Case                       |
| ------------------- | ------------------------------ |
| `eye level`         | Natural, relatable perspective |
| `low angle`         | Heroic, powerful subjects      |
| `bird's-eye`        | Overview, patterns             |
| `worm's-eye`        | Dramatic, imposing             |
| `over-the-shoulder` | Intimate, narrative            |

## HEX Color Code Prompting

FLUX.2 supports precise color control using HEX codes. Include the keyword "color" or "hex" followed by the code:

```python  theme={null}
from together import Together

client = Together()

response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt="A modern living room with a velvet sofa in color #2E4057 and accent pillows in hex #E8AA14, minimalist design with warm lighting",
    width=1024,
    height=768,
)

print(response.data[0].url)
```

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/5.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=21585fb60efac00254dee4a680c22d2e" data-og-width="1024" data-og-height="768" data-path="images/flux2_images/5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/5.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=523265450277a2a5603a23597fda799f 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/5.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=10f230a1b36f9ffc285d31f228a5294f 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/5.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=f376ab2c922a01c7efae562bc0e05dc1 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/5.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=60575a3250a9d4f9056269145a91c66b 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/5.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=dc6167f1099e0403c3e708db33c6676a 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/5.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=b007d226fd47ce1c6f9d154b756127ba 2500w" />

**Gradient Example**

```python  theme={null}
response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt="A ceramic vase on a table, the color is a gradient starting with #02eb3c and finishing with #edfa3c, modern minimalist interior",
    width=1024,
    height=768,
)
```

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/6.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=0f4c58ebc0a06b3d0240b9b94733cee8" data-og-width="1024" data-og-height="768" data-path="images/flux2_images/6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/6.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=7faa404be36d4a7546716bea17b688fa 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/6.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=39392e72b0f2f85b907e0cfaf27b0207 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/6.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=c40ccf61d6de1459f31a2619acc4ba60 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/6.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=197837c28e500793f8bac3d49398b964 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/6.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=eaa3197a42cee650659c868f8f96fcdc 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/6.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=235ea62ab5d27018637226ff1280ead3 2500w" />

## Advanced Use Cases

**Infographics**

FLUX.2 can create complex, visually appealing infographics. Specify all data and content explicitly:

```python  theme={null}
prompt = """Educational weather infographic titled 'WHY FREIBURG IS SO SUNNY' in bold navy letters at top on cream background, illustrated geographic cross-section showing sunny valley between two mountain ranges, left side blue-grey mountains labeled 'VOSGES', right side dark green mountains labeled 'BLACK FOREST', central golden sunshine rays creating 'SUNSHINE POCKET' text over valley, orange sun icon with '1,800 HOURS' text in top right corner, bottom beige panel with three facts in clean sans-serif text: First fact: 'Protected by two mountain ranges', Second fact: 'Creates Germany's sunniest microclimate', Third fact: 'Perfect for wine and solar energy', flat illustration style with soft gradients"""

response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt=prompt,
    width=1024,
    height=1344,
)
```

<img height="500" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/7.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=3efb2b9b7234b675b8576049e979fc54" data-og-width="1024" data-og-height="1344" data-path="images/flux2_images/7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/7.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=90482bb6652a439d17b3a73ddd99c32a 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/7.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=5ce4f82b1d0df5a826de67e0886b8121 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/7.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=8b4043496035dd70617ac2dfc8e1b5dc 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/7.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=a190fae2052fca749390caab3ca20f4e 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/7.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=60adcbf97a42dbf11ed9745cd18a2829 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/7.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=5d0fed17298d77c8bb6941b283b4131d 2500w" />

**Website & App Design Mocks**

Generate full web design mockups for prototyping:

```python  theme={null}
prompt = """Full-page modern meal-kit delivery homepage, professional web design layout. Top navigation bar with text links 'Plans', 'Recipes', 'How it works', 'Login' in clean sans-serif. Large hero headline 'Dinner, simplified.' in bold readable font, below it subheadline 'Fresh ingredients. Easy recipes. Delivered weekly.' Two CTA buttons: primary green rounded button with 'Get started' text, secondary outlined button with 'See plans' text. Right side features large professional food photography showing colorful fresh vegetables. Three value prop cards with icons and text 'Save time', 'Reduce waste', 'Cook better'. Bold green (#2ECC71) accent color, rounded buttons, crisp sans-serif typography, warm natural lighting, modern DTC aesthetic"""

response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt=prompt,
    width=1024,
    height=1344,
)
```

<img height="500" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/8.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=dd9df4bb83f673be5b613b6b3b6715b8" data-og-width="1024" data-og-height="1344" data-path="images/flux2_images/8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/8.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=eabcf0721e25a429a730aad3d4f9fb3c 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/8.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=75b7f62c8094c593782a79c04f8939f7 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/8.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=9f2b4641f6a0b14d87f34a38fca40d53 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/8.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=d261891dd648793911f6999af56aa0c8 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/8.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=aeba06418845819a67574b6d70066c14 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/8.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=dd6ae7ce7f401f496715926b15b3c800 2500w" />

**Comic Strips**

Create consistent comic-style illustrations:

```python  theme={null}
prompt = """Style: Classic superhero comic with dynamic action lines
Character: Diffusion Man (athletic 30-year-old with brown skin tone and short natural fade haircut, wearing sleek gradient bodysuit from deep purple to electric blue, glowing neural network emblem on chest, confident expression) extends both hands forward shooting beams of energy
Setting: Digital cyberspace environment with floating data cubes
Text: "Time to DENOISE this chaos!"
Mood: Intense, action-packed with bright energy flashes"""

response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt=prompt,
    width=1024,
    height=768,
)
```

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/9.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=d2b859fc9aefea9b81ba732f2bd2a4a4" data-og-width="1024" data-og-height="768" data-path="images/flux2_images/9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/9.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=839aaae8f10b128e8e0e77479e9768f6 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/9.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=da98e613eab8286d0be6bf34d106a994 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/9.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=0e3309ce94aafad6ef6090c91d35ee17 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/9.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=c294b1d2a37f1ffc91084f9cd635e44b 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/9.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=1236bd30116f4298a370897cdcd13770 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/9.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=339ccf5e0be7cd9b6ec374b9a4179c93 2500w" />

**Stickers**

Generate die-cut sticker designs:

```python  theme={null}
prompt = """A kawaii die-cut sticker of a chubby orange cat, featuring big sparkly eyes and a happy smile with paws raised in greeting and a heart-shaped pink nose. The design should have smooth rounded lines with black outlines and soft gradient shading with pink cheeks."""

response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt=prompt,
    width=768,
    height=768,
)
```

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/10.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=4d16e02c7c17d6924502bfc29c53e534" data-og-width="768" data-og-height="768" data-path="images/flux2_images/10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/10.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=90a80f389348ea4e380b34a968eaa51a 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/10.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=8f51fc75e09e308eba44d38d391e2629 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/10.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=551958e3f7361c75d2dfc073e9a37fbf 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/10.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=a5e649d5fd8fd634cc9e6f829e3fc348 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/10.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=212975ede0de0ecb910516f2e73eb7da 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/10.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=68e7f22d854508c2e8ab676149a2a27a 2500w" />

## Photography Styles

FLUX.2 excels at various photography aesthetics. Add style keywords to your prompts:

| Style               | Prompt Suffix                                          |
| ------------------- | ------------------------------------------------------ |
| Modern Photorealism | `close up photo, photorealistic`                       |
| 2000s Digicam       | `2000s digicam style`                                  |
| 80s Vintage         | `80s vintage photo`                                    |
| Analogue Film       | `shot on 35mm film, f/2.8, film grain`                 |
| Vintage Cellphone   | `picture taken from a vintage cellphone, selfie style` |

```python  theme={null}
# Example: 80s vintage style
response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt="A group of friends at an arcade, neon lights, having fun playing games, 80s vintage photo",
    width=1024,
    height=768,
)
```

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/11.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=b46015a976e4635a0daaa4258a6595e4" data-og-width="1024" data-og-height="768" data-path="images/flux2_images/11.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/11.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=045bbe58498a1f47cb6938e76b24c2a5 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/11.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=99b49603f577b2129cc4a6f93cacf6a2 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/11.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=0904afb8eb2005d8ed841dd04a51f995 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/11.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=3609f02d919c23531cb6fd5bc1d8b593 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/11.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=73b3d80f673c0e7b88c6f09d03c5702e 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/11.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=8aa3ae15dd324531e9e7e653a9871c3f 2500w" />

## Multi-Language Support

FLUX.2 supports prompting in many languages without translation:

```python  theme={null}
# French
response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt="Un marché alimentaire dans la campagne normande, des marchands vendent divers légumes, fruits. Lever de soleil, temps un peu brumeux",
    width=1024,
    height=768,
)
```

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/12.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=0fe035e538e84ba388871fac54a37336" data-og-width="1024" data-og-height="768" data-path="images/flux2_images/12.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/12.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=843db6bfba01902e6c01686c607b09a5 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/12.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=27f3e7b3577802e0365106f29097fb0e 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/12.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=ce04581b8bb644c0411bd9aff5bb925a 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/12.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=7b6f2157390fd4da4b8dc1d28af18a9b 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/12.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=97dc387eefaf7ea4c21bfd8400662f10 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/12.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=28d5a5c2429b5698e33eb2ef958e4fde 2500w" />

```python  theme={null}
# Korean
response = client.images.generate(
    model="black-forest-labs/FLUX.2-pro",
    prompt="서울 도심의 옥상 정원, 저녁 노을이 지는 하늘 아래에서 사람들이 작은 등불을 켜고 있다",
    width=1024,
    height=768,
)
```

<img height="400" src="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/13.jpg?fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=409ec3d12b70c04651cdc538e3b35b0f" data-og-width="1024" data-og-height="768" data-path="images/flux2_images/13.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/13.jpg?w=280&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=9f84f187286db01baae444533ed7135c 280w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/13.jpg?w=560&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=a4b3e33f2be0fc9dd724ef107c1263d4 560w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/13.jpg?w=840&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=bcdd69fe36d17e7d768832d78ecaa922 840w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/13.jpg?w=1100&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=1e3f41e10139c08305442182c9054f60 1100w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/13.jpg?w=1650&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=9638bdf704075e399115725463695e20 1650w, https://mintcdn.com/togetherai-52386018/ZI5bzy-9RHFbwI45/images/flux2_images/13.jpg?w=2500&fit=max&auto=format&n=ZI5bzy-9RHFbwI45&q=85&s=01388fcb079ce1e274221304731e715d 2500w" />

## Prompting Best Practices

**Golden Rules**

1. **Order by importance** — List the most important elements first in your prompt
2. **Be specific** — The more detailed, the more controlled the output

**Prompt Framework**

Follow this structure: **Subject + Action + Style + Context**

* **Subject**: The main focus (person, object, character)
* **Action**: What the subject is doing or their pose
* **Style**: Artistic approach, medium, or aesthetic
* **Context**: Setting, lighting, time, mood

**Avoid Negative Prompting**

FLUX.2 does **not** support negative prompts. Instead of saying what you don't want, describe what you do want:

| ❌ Don't                                   | ✅ Do                                                                                      |
| ----------------------------------------- | ----------------------------------------------------------------------------------------- |
| `portrait, --no text, --no extra fingers` | `tight head-and-shoulders portrait, clean background, natural hands at rest out of frame` |
| `landscape, --no people`                  | `serene mountain landscape, untouched wilderness, pristine nature`                        |

## Troubleshooting

**Text not rendering correctly**

* Use FLUX.2 \[flex] for better typography
* Put exact text in quotes within the prompt
* Keep text short and clear

**Colors not matching**

* Use HEX codes with "color" or "hex" keyword
* Be explicit about which element should have which color

**Composition not as expected**

* Use JSON structured prompts for precise control
* Specify camera angle, distance, and composition type
* Use position descriptors (foreground, midground, background)

Check out all available Flux models [here](/docs/serverless-models#image-models)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt