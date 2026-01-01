# Source: https://docs.together.ai/docs/videos-overview.md

# Videos

> Generate high-quality videos from text and image prompts.

## Generating a video

Video generation is asynchronous. You create a job, receive a job ID, and poll for completion.

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  # Create a video generation job
  job = client.videos.create(
      prompt="A serene sunset over the ocean with gentle waves",
      model="minimax/video-01-director",
      width=1366,
      height=768,
  )

  print(f"Job ID: {job.id}")

  # Poll until completion
  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print("Video generation failed")
          break

      # Wait before checking again
      time.sleep(5)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    // Create a video generation job
    const job = await together.videos.create({
      prompt: "A serene sunset over the ocean with gentle waves",
      model: "minimax/video-01-director",
      width: 1366,
      height: 768,
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log("Video generation failed");
        break;
      }

      // Wait before checking again
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }

  main();
  ```
</CodeGroup>

Example output when the job is complete:

```json  theme={null}
{
  "id": "019a0068-794a-7213-90f6-cc4eb62e3da7",
  "model": "minimax/video-01-director",
  "status": "completed",
  "info": {
    "user_id": "66f0bd504fb9511df3489b9a",
    "errors": null
  },
  "inputs": {
    "fps": null,
    "guidance_scale": null,
    "height": 768,
    "metadata": {},
    "model": "minimax/video-01-director",
    "output_quality": null,
    "prompt": "A serene sunset over the ocean with gentle waves",
    "seconds": null,
    "seed": null,
    "steps": null,
    "width": 1366
  },
  "outputs": {
    "cost": 0.28,
    "video_url": "https://api.together.ai/shrt/DwlaBdSakNRFlBxN"
  },
  "created_at": "2025-10-20T06:57:18.154804Z",
  "claimed_at": "0001-01-01T00:00:00Z",
  "done_at": "2025-10-20T07:00:12.234472Z"
}
```

**Job Status Reference:**

| Status        | Description                            |
| ------------- | -------------------------------------- |
| `queued`      | Job is waiting in queue                |
| `in_progress` | Video is being generated               |
| `completed`   | Generation successful, video available |
| `failed`      | Generation failed, check `info.errors` |
| `cancelled`   | Job was cancelled                      |

## Parameters

| Parameter         | Type    | Description                                                                                                                                                              | Default      |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| `prompt`          | string  | Text description of the video to generate                                                                                                                                | **Required** |
| `model`           | string  | Model identifier                                                                                                                                                         | **Required** |
| `width`           | integer | Video width in pixels                                                                                                                                                    | 1366         |
| `height`          | integer | Video height in pixels                                                                                                                                                   | 768          |
| `seconds`         | integer | Length of video (1-10)                                                                                                                                                   | 6            |
| `fps`             | integer | Frames per second                                                                                                                                                        | 15-60        |
| `steps`           | integer | Diffusion steps (higher = better quality, slower)                                                                                                                        | 10-50        |
| `guidance_scale`  | float   | How closely to follow prompt                                                                                                                                             | 6.0-10.0     |
| `seed`            | integer | Random seed for reproducibility                                                                                                                                          | any          |
| `output_format`   | string  | Video format (MP4, GIF)                                                                                                                                                  | MP4          |
| `output_quality`  | integer | Bitrate/quality (lower = higher quality)                                                                                                                                 | 20           |
| `negative_prompt` | string  | What to avoid in generation                                                                                                                                              | -            |
| `frame_images`    | Array   | Array of images to guide video generation, like keyframes.  If size 1, starting frame, if size 2, starting and ending frame, if more than 2 then frame must be specified |              |

* `prompt` is required for all models except Kling
* `width` and `height` will rely on defaults unless otherwise specified - options for dimensions vary by model

These parameters vary by model, please refer to the [models table](/docs/videos-overview#supported-model-details) for details.

Generate customized videos using the above parameters:

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A futuristic city at night with neon lights reflecting on wet streets",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      seconds=6,
      fps=30,
      steps=30,
      guidance_scale=8.0,
      output_format="MP4",
      output_quality=20,
      seed=42,
      negative_prompt="blurry, low quality, distorted",
  )

  print(f"Job ID: {job.id}")

  # Poll until completion
  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          print(f"Cost: ${status.outputs.cost}")
          break
      elif status.status == "failed":
          print("Video generation failed")
          break

      # Wait before checking again
      time.sleep(5)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A futuristic city at night with neon lights reflecting on wet streets",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      seconds: 6,
      fps: 30,
      steps: 30,
      guidance_scale: 8.0,
      output_format: "MP4",
      output_quality: 20,
      seed: 42,
      negative_prompt: "blurry, low quality, distorted"
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        console.log(`Cost: $${status.outputs.cost}`);
        break;
      } else if (status.status === "failed") {
        console.log("Video generation failed");
        break;
      }

      // Wait before checking again
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }

  main();
  ```
</CodeGroup>

## Reference Images

Guide your video's visual style with reference images:

<CodeGroup>
  ```py Python theme={null}
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A cat dancing energetically",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      seconds=6,
      reference_images=[
          "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
      ],
  )

  print(f"Job ID: {job.id}")

  # Poll until completion
  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print("Video generation failed")
          break

      # Wait before checking again
      time.sleep(5)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A cat dancing energetically",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      seconds: 6,
      reference_images: [
        "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
      ]
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log("Video generation failed");
        break;
      }

      // Wait before checking again
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }

  main();
  ```
</CodeGroup>

## Keyframe Control

Control specific frames in your video for precise transitions.

**Single Keyframe:** Set a single(for the example below this is the first frame) frame to a specific image.

Depending on the model you can also specify to set multiple keyframes please refer to the [models table](/docs/videos-overview#supported-model-details) for details.

<CodeGroup>
  ```py Python theme={null}
  import base64
  import requests
  import time
  from together import Together

  client = Together()

  # Download image and encode to base64
  image_url = (
      "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg"
  )
  response = requests.get(image_url)
  base64_image = base64.b64encode(response.content).decode("utf-8")

  # Single keyframe at start
  job = client.videos.create(
      prompt="Smooth transition from day to night",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      fps=24,
      frame_images=[{"input_image": base64_image, "frame": 0}],  # Starting frame
  )

  print(f"Job ID: {job.id}")

  # Poll until completion
  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print("Video generation failed")
          break

      # Wait before checking again
      time.sleep(5)
  ```

  ```ts TypeScript theme={null}
  import * as fs from 'fs';
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    // Load and encode your image
    const imageBuffer = fs.readFileSync('keyframe.jpg');
    const base64Image = imageBuffer.toString('base64');

    // Single keyframe at start
    const job = await together.videos.create({
      prompt: "Smooth transition from day to night",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      fps: 24,
      frame_images: [
        {
          input_image: base64Image,
          frame: 0  // Starting frame
        }
      ]
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log("Video generation failed");
        break;
      }

      // Wait before checking again
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }

  main();
  ```
</CodeGroup>

**💡 Tip:** Frame number = seconds × fps

## Guidance Scale

Controls how closely the model follows your prompt:

* **6.0-7.0**: More creative, less literal
* **7.0-9.0**: Sweet spot for most use cases
* **9.0-10.0**: Strict adherence to prompt
* **>12.0**: Avoid - may cause artifacts

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  # Low guidance - more creative interpretation
  job_creative = client.videos.create(
      prompt="an astronaut riding a horse on the moon",
      model="minimax/hailuo-02",
      guidance_scale=6.0,
      seed=100,
  )

  # High guidance - closer to literal prompt
  job_literal = client.videos.create(
      prompt="an astronaut riding a horse on the moon",
      model="minimax/hailuo-02",
      guidance_scale=10.0,
      seed=100,
  )
  ```

  ```ts TypeScript theme={null}
  // Low guidance - more creative interpretation
  import Together from "together-ai";

  const together = new Together();

  const jobCreative = await together.videos.create({
    prompt: "an astronaut riding a horse on the moon",
    model: "minimax/hailuo-02",
    guidance_scale: 6.0,
    seed: 100
  });

  // High guidance - closer to literal prompt
  const jobLiteral = await together.videos.create({
    prompt: "an astronaut riding a horse on the moon",
    model: "minimax/hailuo-02",
    guidance_scale: 10.0,
    seed: 100
  });
  ```
</CodeGroup>

## Quality Control with Steps

Trade off between generation time and quality:

* **10 steps**: Quick testing, lower quality
* **20 steps**: Standard quality, good balance
* **30-40 steps**: Production quality, slower
* **>50 steps**: Diminishing returns

<CodeGroup>
  ```py Python theme={null}
  # Quick preview
  job_quick = client.videos.create(
      prompt="A person walking through a forest",
      model="minimax/hailuo-02",
      steps=10,
  )

  # Production quality
  job_production = client.videos.create(
      prompt="A person walking through a forest",
      model="minimax/hailuo-02",
      steps=40,
  )
  ```

  ```ts TypeScript theme={null}
  // Quick preview
  import Together from "together-ai";

  const together = new Together();

  const jobQuick = await together.videos.create({
    prompt: "A person walking through a forest",
    model: "minimax/hailuo-02",
    steps: 10
  });

  // Production quality
  const jobProduction = await together.videos.create({
    prompt: "A person walking through a forest",
    model: "minimax/hailuo-02",
    steps: 40
  });
  ```
</CodeGroup>

## Supported Model Details

See our supported video models and relevant parameters below.

| **Organization** | **Name**             | **Model API String**          | **Duration** | **Dimensions**                                                                                      | **FPS** | **Keyframes** | **Prompt**  |
| :--------------- | :------------------- | :---------------------------- | :----------- | :-------------------------------------------------------------------------------------------------- | :------ | :------------ | :---------- |
| **MiniMax**      | MiniMax 01 Director  | `minimax/video-01-director`   | 5s           | 1366×768                                                                                            | 25      | First         | 2-3000 char |
| **MiniMax**      | MiniMax Hailuo 02    | `minimax/hailuo-02`           | 10s          | 1366×768, 1920×1080                                                                                 | 25      | First         | 2-3000 char |
| **Google**       | Veo 2.0              | `google/veo-2.0`              | 5s           | 1280×720, 720×1280                                                                                  | 24      | First, Last   | 2-3000 char |
| **Google**       | Veo 3.0              | `google/veo-3.0`              | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **Google**       | Veo 3.0 + Audio      | `google/veo-3.0-audio`        | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **Google**       | Veo 3.0 Fast         | `google/veo-3.0-fast`         | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **Google**       | Veo 3.0 Fast + Audio | `google/veo-3.0-fast-audio`   | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **ByteDance**    | Seedance 1.0 Lite    | `ByteDance/Seedance-1.0-lite` | 5s           | 864×480, 736×544, 640×640, 960×416, 416×960, 1248×704, 1120×832, 960×960, 1504×640, 640×1504        | 24      | First, Last   | 2-3000 char |
| **ByteDance**    | Seedance 1.0 Pro     | `ByteDance/Seedance-1.0-pro`  | 5s           | 864×480, 736×544, 640×640, 960×416, 416×960, 1248×704, 1120×832, 960×960, 1504×640, 640×1504        | 24      | First, Last   | 2-3000 char |
| **PixVerse**     | PixVerse v5          | `pixverse/pixverse-v5`        | 5s           | 640×360, 480×360, 360×360, 270×360, 360×640, 960×540, 720×540, 540×540, 405×540, 540×960, 1280×720, |         |               |             |
|                  |                      |                               |              | 960×720, 720×720, 540×720, 720×1280, 1920×1080, 1440×1080, 1080×1080, 810×1080, 1080×1920           | 16, 24  | First, Last   | 2-2048 char |
| **Kuaishou**     | Kling 2.1 Master     | `kwaivgI/kling-2.1-master`    | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First         | 2-2500 char |
| **Kuaishou**     | Kling 2.1 Standard   | `kwaivgI/kling-2.1-standard`  | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First         | ❌           |
| **Kuaishou**     | Kling 2.1 Pro        | `kwaivgI/kling-2.1-pro`       | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First, Last   | ❌           |
| **Kuaishou**     | Kling 2.0 Master     | `kwaivgI/kling-2.0-master`    | 5s           | 1280×720, 720×720, 720×1280                                                                         | 24      | First         | 2-2500 char |
| **Kuaishou**     | Kling 1.6 Standard   | `kwaivgI/kling-1.6-standard`  | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 30, 24  | First         | 2-2500 char |
| **Kuaishou**     | Kling 1.6 Pro        | `kwaivgI/kling-1.6-pro`       | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First         | ❌           |
| **Wan-AI**       | Wan 2.2 I2V          | `Wan-AI/Wan2.2-I2V-A14B`      | -            | -                                                                                                   | -       | -             | -           |
| **Wan-AI**       | Wan 2.2 T2V          | `Wan-AI/Wan2.2-T2V-A14B`      | -            | -                                                                                                   | -       | -             | -           |
| **Vidu**         | Vidu 2.0             | `vidu/vidu-2.0`               | 8s           | 1920×1080, 1080×1080, 1080×1920, 1280×720, 720×720, 720×1280, 640×360, 360×360, 360×640             | 24      | First, Last   | 2-3000 char |
| **Vidu**         | Vidu Q1              | `vidu/vidu-q1`                | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First, Last   | 2-3000 char |
| **OpenAI**       | Sora 2               | `openai/sora-2`               | 8s           | 1280×720, 720×1280                                                                                  | -       | First         | 1-4000 char |
| **OpenAI**       | Sora 2 Pro           | `openai/sora-2-pro`           | 8s           | 1280×720, 720×1280                                                                                  | -       | First         | 1-4000 char |

## Troubleshooting

**Video doesn't match prompt well:**

* Increase `guidance_scale` to 8-10
* Make prompt more descriptive and specific
* Add `negative_prompt` to exclude unwanted elements

**Video has artifacts:**

* Reduce `guidance_scale` (keep below 12)
* Increase `steps` to 30-40
* Adjust `fps` if motion looks unnatural

**Generation is too slow:**

* Reduce `steps` (try 10-20 for testing)
* Use shorter `seconds` during development
* Lower `fps` for slower-paced scenes

**URLs expire:**

* Download videos immediately after completion
* Don't rely on URLs for long-term storage


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt