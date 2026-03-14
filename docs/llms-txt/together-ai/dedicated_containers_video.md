# Source: https://docs.together.ai/docs/dedicated_containers_video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Video Generation with Wan 2.1

> Deploy a multi-GPU video generation model on Together's managed GPU infrastructure using Dedicated Containers.

This example demonstrates deploying a multi-GPU video generation model using Dedicated Containers. You'll build a Sprocket worker that uses `torchrun` for distributed inference across multiple GPUs and deploy it to Together's managed infrastructure.

## What You'll Learn

* Deploying multi-GPU models with Sprocket and Jig
* Using `use_torchrun=True` for distributed inference
* Automatic file upload with `FileOutput`
* Submitting jobs via the Queue API and polling for results

## Prerequisites

* **Together API Key** – Get one from [together.ai](https://together.ai)
* **Dedicated Containers access** – Contact [support@together.ai](mailto:support@together.ai) to enable for your organization
* **Docker** – For building container images. [Install Docker](https://docs.docker.com/engine/install)
* **Together CLI** – Install with `pip install together --upgrade` or `uv tool install together`

Set your API key:

```shell  theme={null}
export TOGETHER_API_KEY=your_key_here
```

Install Together library:

<CodeGroup>
  ```shell pip theme={null}
  pip install together
  ```

  ```shell uv theme={null}
  uv add together
  ```
</CodeGroup>

## Overview

This example deploys a Wan 2.1 text-to-video model as a Dedicated Container with multi-GPU support. The Sprocket worker handles distributed inference across 2 GPUs, and Together manages provisioning, autoscaling, and observability.

**Output specs:**

* Resolution: 480×832
* Frames: 81 (5.4 seconds at 15fps)
* Format: MP4

**Why multi-GPU?**

* Video generation requires significant VRAM for temporal attention
* Context parallelism splits the sequence dimension across GPUs
* 2x H100 allows comfortable generation without memory pressure

## How It Works

1. **Build** – Jig builds a Docker image from your `pyproject.toml` configuration
2. **Push** – The image is pushed to Together's private container registry
3. **Deploy** – Together provisions 2x H100 GPUs and starts your container
4. **Torchrun** – Sprocket's `use_torchrun=True` launches child processes (one per GPU)
5. **Queue** – Jobs are submitted to the managed queue, broadcast to all GPU ranks, and processed in parallel

## Project Structure

```
sprocket_wan2.1/
├── pyproject.toml    # Configuration with torchrun command
└── run_wan.py        # Distributed Sprocket worker
```

## Implementation

### Sprocket Worker Code

<CodeGroup>
  ```python run_wan.py theme={null}
  import os
  from typing import Optional

  import torch
  import torch.distributed as dist
  from diffusers import WanPipeline
  from diffusers.utils import export_to_video
  from para_attn.context_parallel import init_context_parallel_mesh
  from para_attn.context_parallel.diffusers_adapters import parallelize_pipe

  import sprocket


  class WanSprocket(sprocket.Sprocket):
      def setup(self) -> None:
          dist.init_process_group()
          torch.cuda.set_device(dist.get_rank())

          pipe = WanPipeline.from_pretrained("Wan-AI/Wan2.1-T2V-1.3B-Diffusers")
          self.pipe = pipe.to("cuda")

          para_mesh = init_context_parallel_mesh(self.pipe.device.type)
          parallelize_pipe(self.pipe, mesh=para_mesh)

      def predict(self, args: dict) -> Optional[dict]:
          video = self.pipe(
              prompt=args["prompt"],
              negative_prompt="",
              height=480,
              width=832,
              num_frames=81,
              num_inference_steps=int(args.get("num_inference_steps", 30)),
              output_type="pil" if dist.get_rank() == 0 else "pt",
          ).frames[0]

          if dist.get_rank() == 0:
              print("Saving video to output.mp4")
              export_to_video(video, "output.mp4", fps=15)
              return {"url": sprocket.FileOutput("output.mp4")}


  if __name__ == "__main__":
      queue_name = os.environ.get("TOGETHER_DEPLOYMENT_NAME", "wan-ai/wan2.1")
      sprocket.run(WanSprocket(), queue_name, use_torchrun=True)
  ```
</CodeGroup>

### Configuration

<CodeGroup>
  ```toml pyproject.toml theme={null}
  [project]
  name = "sprocket-wan2.1"
  version = "0.1.0"
  dependencies = [
      "diffusers==0.33.0",
      "transformers>=4.44.0",
      "para_attn",
      "ftfy",
      "accelerate",
      "einops",
      "omegaconf",
      "pillow",
      "ffmpeg-python",
      "opencv-python",
      "torch",
      "sprocket",
  ]

  [[tool.uv.index]]
  name = "together-pypi"
  url = "https://pypi.together.ai/"

  [tool.uv.sources]
  sprocket = { index = "together-pypi" }

  [tool.jig.image]
  python_version = "3.11"
  system_packages = ["libgl1", "libglx-mesa0", "ffmpeg"]
  cmd = "torchrun --standalone --nproc_per_node=2 run_wan.py"
  auto_include_git = false
  copy = ["run_wan.py"]

  [tool.jig.deploy]
  description = "Wan2.1 Video Generation with Sprocket"
  gpu_type = "h100-80gb"
  gpu_count = 2
  cpu = 4
  memory = 32
  port = 8000
  min_replicas = 1
  max_replicas = 1
  ```
</CodeGroup>

## Key Concepts

### How `use_torchrun=True` Works

When you call `sprocket.run(..., use_torchrun=True)`, Sprocket handles multi-GPU orchestration automatically.

**Flow:**

1. Parent process receives a job from Together's queue
2. Job payload is broadcast to all child processes via Unix socket
3. Each rank executes `setup()` once at startup, then `predict()` for each job
4. Ranks synchronize via NCCL during forward pass
5. Only rank 0 saves output and returns result
6. Parent uploads `FileOutput` and reports job completion

### Distributed Process Initialization

Each worker process must initialize its distributed context before loading the model:

```python  theme={null}
def setup(self) -> None:
    # Required: Initialize the process group for NCCL communication
    dist.init_process_group()

    # Required: Set the correct GPU for this rank
    torch.cuda.set_device(dist.get_rank())

    # Now load and parallelize the model...
```

This is handled automatically by `torchrun`, which sets `RANK`, `LOCAL_RANK`, `WORLD_SIZE`, and other environment variables.

### Rank 0 Output Pattern

In distributed inference, only rank 0 should handle I/O and return results:

```python  theme={null}
def predict(self, args: dict) -> Optional[dict]:
    # Generate on all ranks (synchronized via NCCL)
    video = self.pipe(
        prompt=args["prompt"],
        # Rank 0 needs PIL for saving; others use tensors (less memory)
        output_type="pil" if dist.get_rank() == 0 else "pt",
    ).frames[0]

    # Only rank 0 saves and returns
    if dist.get_rank() == 0:
        export_to_video(video, "output.mp4", fps=15)
        return {"url": sprocket.FileOutput("output.mp4")}

    # Other ranks implicitly return None
```

**Why this pattern?**

* Avoids duplicate file writes
* Reduces memory on non-rank-0 GPUs (tensor output vs PIL)
* Sprocket collects output from rank 0 only

### Automatic File Upload with `FileOutput`

Wrapping a path in `FileOutput` triggers automatic upload:

```python  theme={null}
return {"url": sprocket.FileOutput("output.mp4")}
```

**What happens:**

1. Sprocket detects the `FileOutput` in the response
2. Uploads the file to Together's storage
3. Replaces `FileOutput` with the public URL in the final response

The client receives (when polling job status):

```json  theme={null}
{
  "request_id": "req_abc123",
  "status": "done",
  "outputs": {
    "url": "https://..."
  }
}
```

### Multi-GPU Configuration

For multi-GPU deployments, configure `gpu_count` in your deployment settings and use `torchrun` in your startup command:

```toml  theme={null}
[tool.jig.image]
cmd = "torchrun --standalone --nproc_per_node=2 run_wan.py"

[tool.jig.deploy]
gpu_count = 2  # Must match --nproc_per_node
```

When you pass `use_torchrun=True` to `sprocket.run()`, Sprocket handles the coordination between the parent process and GPU workers automatically.

## Deployment

### Deploy

<CodeGroup>
  ```shell Shell theme={null}
  # Deploy (builds, pushes, and creates deployment)
  together beta jig deploy

  # Or deploy with cache warmup to reduce cold start latency
  together beta jig deploy --warmup

  # Monitor startup
  together beta jig logs --follow
  ```
</CodeGroup>

### Check Deployment Status

<CodeGroup>
  ```shell Shell theme={null}
  # View deployment status and replica health
  together beta jig status
  ```
</CodeGroup>

Wait until the deployment shows `running` and replicas are ready before submitting jobs.

### Submit Jobs

Jobs are submitted to the managed queue and processed asynchronously. Video generation typically takes 30-75 seconds depending on settings.

<CodeGroup>
  ```python Python SDK theme={null}
  from together import Together
  import time

  client = Together()
  deployment = "sprocket-wan2.1"

  # Submit job to queue
  job = client.beta.queue.submit(
      model=deployment,
      payload={
          "prompt": "A serene lake at sunset with mountains in the background",
          "num_inference_steps": 30,
      },
  )
  print(f"Job submitted: {job.request_id}")

  # Poll for completion
  while True:
      status = client.beta.queue.retrieve(
          request_id=job.request_id,
          model=deployment,
      )

      print(f"Status: {status.status}")

      if status.status == "done":
          print(f"Video URL: {status.outputs['url']}")
          break
      elif status.status == "failed":
          print(f"Job failed: {status.error}")
          break

      time.sleep(5)
  ```

  ```python requests theme={null}
  import requests
  import time

  api_key = "your_key_here"
  deployment = "sprocket-wan2.1"

  # Submit job to queue
  response = requests.post(
      "https://api.together.ai/v1/queue/submit",
      headers={"Authorization": f"Bearer {api_key}"},
      json={
          "model": deployment,
          "payload": {
              "prompt": "A cat playing with a ball of yarn",
              "num_inference_steps": 30,
          },
      },
  )
  job = response.json()
  print(f"Job submitted: {job['request_id']}")

  # Poll for completion
  while True:
      status_response = requests.get(
          f"https://api.together.ai/v1/queue/status?request_id={job['request_id']}&model={deployment}",
          headers={"Authorization": f"Bearer {api_key}"},
      )
      status = status_response.json()

      print(f"Status: {status['status']}")

      if status["status"] == "done":
          print(f"Video URL: {status['outputs']['url']}")
          break
      elif status["status"] == "failed":
          print(f"Job failed: {status.get('error')}")
          break

      time.sleep(5)
  ```

  ```shell cURL theme={null}
  # Submit job
  curl -X POST https://api.together.ai/v1/queue/submit \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sprocket-wan2.1",
      "payload": {
        "prompt": "A serene lake at sunset with mountains in the background",
        "num_inference_steps": 30
      }
    }'

  # Response: {"request_id": "req_abc123", "status": "pending"}

  # Poll for result (replace REQUEST_ID with actual value)
  curl "https://api.together.ai/v1/queue/status?request_id=REQUEST_ID&model=sprocket-wan2.1" \
    -H "Authorization: Bearer $TOGETHER_API_KEY"

  # When status is "done", the video URL is in outputs.url
  ```
</CodeGroup>

## Input Parameters

| Parameter             | Type   | Default  | Description                                                 |
| --------------------- | ------ | -------- | ----------------------------------------------------------- |
| `prompt`              | string | Required | Text description of the video to generate                   |
| `num_inference_steps` | int    | `30`     | Number of denoising steps (higher = better quality, slower) |

## Output

When the job completes, the status response contains:

```json  theme={null}
{
  "request_id": "req_abc123",
  "status": "done",
  "outputs": {
    "url": "https://..."
  }
}
```

* `url`: Public URL to the generated MP4 video file (480×832, 81 frames, 15fps)

### Scaling to More GPUs

To scale for higher throughput, increase `max_replicas` to add more workers:

```toml  theme={null}
[tool.jig.deploy]
min_replicas = 1
max_replicas = 10

[tool.jig.autoscaling]
profile = "QueueBacklogPerWorker"
targetValue = "1.05"
```

To scale to zero when idle, specify `min_replicas = 0` (saves costs but adds cold start latency).

## Cleanup

When you're done, delete the deployment:

<CodeGroup>
  ```shell Shell theme={null}
  together beta jig destroy
  ```
</CodeGroup>

## Next Steps

* [Image Generation Example](/docs/dedicated_containers_image) – Single-GPU inference with Flux2
* [Quickstart](/docs/containers-quickstart) – Deploy your first container in 20 minutes
* [Sprocket SDK](/reference/dci-reference-sprocket) – Full SDK reference for workers
* [Jig CLI Reference](/reference/dci-reference-jig) – CLI commands and configuration options
* [Deployments API Reference](/reference/deployments-list) – REST API for deployments, secrets, storage, and queues


Built with [Mintlify](https://mintlify.com).