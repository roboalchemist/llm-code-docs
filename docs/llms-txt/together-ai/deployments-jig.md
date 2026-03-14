# Source: https://docs.together.ai/docs/deployments-jig.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Jig CLI

> Build, push, and deploy containers to Together's managed GPU infrastructure.

Jig is a lightweight CLI for building Docker images from a `pyproject.toml`, pushing them to Together's private container registry, and managing deployments. It's included with the [Together Python library](https://github.com/togethercomputer/together-python).

<Tip>
  **See Jig in action:** Check out our end-to-end examples for [Image Generation with Flux2](/docs/dedicated_containers_image) and [Video Generation with Wan 2.1](/docs/dedicated_containers_video).
</Tip>

## The Deploy Workflow

Jig combines several steps into a single `deploy` command:

1. **Init** — `together beta jig init` scaffolds a `pyproject.toml` with sensible defaults
2. **Build** — Generates a Dockerfile from your config and builds the image locally
3. **Push** — Pushes the image to Together's registry at `registry.together.xyz`
4. **Deploy** — Creates or updates the deployment on Together's infrastructure

<CodeGroup>
  ```shell Shell theme={null}
  # One command does it all
  together beta jig deploy

  # Or step by step
  together beta jig build
  together beta jig push
  together beta jig deploy --image registry.together.xyz/myproject/mymodel@sha256:abc123
  ```
</CodeGroup>

Once deployed, monitor your containers:

<CodeGroup>
  ```shell Shell theme={null}
  together beta jig status
  together beta jig logs --follow
  ```
</CodeGroup>

For the full list of commands and flags, see the [Jig CLI Reference](/reference/dci-reference-jig).

<Tip>
  Jig builds images locally and pushes them to Together's registry. ML images can be 10GB+, so building on a machine with a fast network connection saves significant time compared to pushing from a laptop over wifi.
</Tip>

## Cache Warmup

The `--warmup` option lets you pre-generate inference engine compile caches — such as those created by `torch.compile` or TensorRT — at build time, rather than waiting for the first request in production. This can significantly reduce cold-start latency.

<CodeGroup>
  ```shell Shell theme={null}
  together beta jig deploy --warmup
  together beta jig build --warmup   # Build only, no deploy
  ```
</CodeGroup>

### How It Works

1. **Build phase**: Jig builds the base image normally
2. **Warmup phase**: Jig runs the container with GPU access, mounting your local workspace to `/app`
3. **Cache capture**: The container runs your Sprocket's `warmup_inputs`, generating compile caches
4. **Final image**: Jig builds a new image layer with the cache baked in

The cache location inside the container is controlled by `WARMUP_ENV_NAME` (default: `TORCHINDUCTOR_CACHE_DIR`) and `WARMUP_DEST` (default: `torch_cache`).
Jig sets the environment variable to point to the cache directory during warmup and copies its contents into the final image.

### Sprocket Integration

Define `warmup_inputs` on your Sprocket class to specify what inputs to run during warmup:

<CodeGroup>
  ```python app.py theme={null}
  import base64
  import logging
  import os
  from io import BytesIO

  import sprocket
  import torch
  from diffusers import Flux2Pipeline


  class Flux2Sprocket(sprocket.Sprocket):
      # Define inputs to run during warmup - this pre-generates compile caches
      warmup_inputs = [
          {"prompt": "a white cat"},
      ]

      def setup(self) -> None:
          device = "cuda" if torch.cuda.is_available() else "cpu"

          logging.info(f"Loading Flux2 pipeline on {device}...")
          self.pipe = Flux2Pipeline.from_pretrained(
              "diffusers/FLUX.2-dev-bnb-4bit",
              torch_dtype=torch.bfloat16,
          ).to(device)
          logging.info("Pipeline loaded successfully!")

      def predict(self, args: dict) -> dict:
          prompt = args.get("prompt", "a cat")
          num_inference_steps = args.get("num_inference_steps", 28)
          guidance_scale = args.get("guidance_scale", 4.0)

          logging.info(f"Generating image for prompt: {prompt[:50]}...")
          image = self.pipe(
              prompt=prompt,
              num_inference_steps=num_inference_steps,
              guidance_scale=guidance_scale,
          ).images[0]

          # Convert to base64
          buffered = BytesIO()
          image.save(buffered, format="PNG")
          img_str = base64.b64encode(buffered.getvalue()).decode()

          return {"image": img_str, "format": "png", "encoding": "base64"}


  if __name__ == "__main__":
      queue_name = os.environ.get(
          "TOGETHER_DEPLOYMENT_NAME", "sprocket-flux2-dev"
      )
      sprocket.run(Flux2Sprocket(), queue_name)
  ```
</CodeGroup>

Warmup runs each input in `warmup_inputs` once. If `warmup_inputs` is empty or not defined, warmup runs `predict({})` once. Make sure all the compile paths would be exercised by the warmup inputs.

Since the local workspace is mounted to `/app`, model weights and example inputs can live in your project directory and be referenced directly.

### Requirements

* A GPU on your build machine — warmup runs your model locally to generate caches. If you don't have a local GPU, [Together Instant Clusters](/docs/gpu-clusters-overview) provide on-demand H100s with fast connectivity to Together's container registry.
* `warmup_inputs` defined on your Sprocket with representative inputs
* Weights and example inputs accessible in local workspace

## Secrets

Secrets are encrypted environment variables injected into your container at runtime. Use them for API keys, tokens, and other sensitive values that shouldn't be baked into the image.

<CodeGroup>
  ```shell Shell theme={null}
  together beta jig secrets set --name HF_TOKEN --value hf_xxxxx --description "Hugging Face token"
  together beta jig secrets list
  together beta jig secrets unset HF_TOKEN
  ```
</CodeGroup>

Reference your secrets in `pyproject.toml` as environment variables, and they'll be available to your container at runtime. See the [Jig CLI Reference](/reference/dci-reference-jig#secrets-commands) for all secrets commands.

## Volumes

Volumes let you mount read-only data — like model weights — into your container without baking them into the image. This keeps images small and lets you update weights independently of code.

Create a volume and upload files:

<CodeGroup>
  ```shell Shell theme={null}
  together beta jig volumes create --name my-weights --source ./model_weights/
  ```
</CodeGroup>

Then mount it in your `pyproject.toml`:

```toml  theme={null}
[[tool.jig.volume_mounts]]
name = "my-weights"
mount_path = "/models"
```

See the [Jig CLI Reference](/reference/dci-reference-jig#volumes-commands) for all volume commands.


Built with [Mintlify](https://mintlify.com).