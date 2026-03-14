# Source: https://docs.mystic.ai/docs/fractional-gpus-gpu-sharing.md

# Fractional GPUs & GPU sharing

Learn how to lower costs by using a GPU slice instead of a whole GPU!

> 👍 Fractional GPUs are available on all Mystic platforms
>
> Even when deploying on your own cloud with [BYOC](https://www.mystic.ai/bring-your-own-cloud)

In an ideal world, it's best to run as much as you can on a single GPU. The main limitation here is the amount of memory available. Our production [Stable Diffusion](https://www.mystic.ai/stabilityai/stable-diffusion/play) uses 13GB of VRAM when first loaded, and gets close to 20GB when creating two 1024x1024 images. We used to run this on a whole A100 40GB and just accepted the inefficiency, but now offer the perfect solution: Fractional GPUs.

NVIDIA offers a few techniques to split up GPUs into smaller pieces so that you can maximise the GPU to its full potential:

* **Time Slicing** - This allows docker containers to attach to the full GPU and have access to all of it's memory.
* **MIG (Multi-instance GPU)** - This virtualises a GPU into smaller chunks and docker containers can attach to each chunk. Memory between chunks is not accessible.

We use the MIG technology to break apart GPUs. This is a new method and as such is only supported by A100s and A10s in our GPU offering (H100s coming soon).

The following fractions are available on Mystic currently:

* A100-40GB **5GB**
* A100-40GB **10GB**
* A100-40GB **20GB**

We also support the following fractions on our BYOC offering (including the above):

* A100-80GB **10GB**
* A100-80GB **20GB**
* A100-80GB **40GB**
* A10 **4GB**
* A10 **8GB**
* A10 **12GB**

# How to use them

Our goal is to make sure you can access the latest technology possible without needing to get into the weeds of how it works. To use this technology you just need to change the accelerator field in your `pipeline.yaml`, here's an example for the 5GB A100 chunk:

```yaml
runtime:
  container_commands:
    ...
  python:
    ...
accelerators: ["nvidia_a100_5gb"]
pipeline_graph: new_pipeline:my_new_pipeline
pipeline_name: paulh/a-cool-model
readme: README.md
...
```

# Pricing

Fractional GPUs are a great way to save costs on your project, they also have much lower cold starts than a whole GPU and due to this we offer no low volume premium and have a completely flat time based pricing:

| Name               | Per second cost | Per hour cost |
| :----------------- | :-------------- | :------------ |
| `nvidia_a100_5gb`  | $0.000119       | $0.429        |
| `nvidia_a100_10gb` | $0.000278       | $1            |
| `nvidia_a100_20gb` | $0.0004165      | $1.5          |

## BYOC

For BYOC users that get their GPUs at cost, you are only charged for the whole GPU by the cloud provider. Say you are running 3x10GB fractions on an A100 40GB, you will only be billed for the A100 by the provider even though you're running 3 models on the GPU concurrently.

# Cold starts

Cold starts are traditionally really long in AI, we have an in-depth article on this and how to optimise it here: [How to reduce cold starts in ML models running in production](https://docs.mystic.ai/docs/how-to-reduce-cold-starts-in-ml-models). Fractional GPUs however, do not require a full machine to start up every time as they will use a fraction of an existing GPU. This means cold starts are typically substantially lower. We highly recommend using the fractional GPUs instead of a full A100!