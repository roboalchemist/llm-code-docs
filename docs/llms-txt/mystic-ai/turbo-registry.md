# Source: https://docs.mystic.ai/docs/turbo-registry.md

# Turbo Registry

The fastest docker cold starts in the world!

Mystic AI introduces Turbo Registry (TR), an advanced solution designed to optimise AI/ML inference deployment loading times. By reengineering parts of Kubernetes and Containerd, Turbo Registry significantly reduces cold start times for Docker images. **Turbo Registry is between x8-x12 faster** than standard Kubernetes and cloud provider docker registries. This documentation will walk you through the steps to integrate and utilise Turbo Registry, ensuring faster and more efficient AI/ML inference deployments.

> 📘 You must be on a team plan to use this feature
>
> To use the Turbo Registry, you must have a Starter, Pro, or BYOC plan.

At the end of this document you can see some more info on roadmap and limitations of the current implementation. **TR introduces a V3 API specification to the docker standard**, this will be included in the open source repository to be released later this year.

# Benchmarks

Common container sizes we see are 5GB, 10GB and 20GB. Stable Diffusion with all of it's python dependencies and model weights normally comes in between 8-13GB for a full container as a point of reference. The below benchmarks were carried out on GCP in `europe-west4` on a `c3d-standard-30` for the registry with tier 1 networking. The pulling machines used were `a2-highgpu-4g`, these machines have 4x A100 40GB GPUs.

| Docker image size | Standard docker & containerd | TR & updated containerd | Performance gain |
| :---------------- | :--------------------------- | :---------------------- | :--------------- |
| 5GB               | 82.21s                       | **10.23s**              | **x8.0**         |
| 10GB              | 147.00s                      | **14.75s**              | **x10.0**        |
| 20GB              | 270.47s                      | **23.72s**              | **x11.4**        |

As shown above, the Turbo Registry sees greater performance gains as the image size increases. This is due to our downloading techniques removing the previous limitations in pulling of containerd.

*These tests were conducted by performing a run via the Mystic API, and the round trip time used as the cold start. This means that the pure container cold start without python environment initialising with FastAPI is around 1-4s faster than what's recorded.*

*The container used has the base set of dependencies for a pipeline per the pipeline building quickstart guide, the pipeline immediately returns a string when initialised. This cold start time includes the python environment starting and returning the run result.*

# Building and Pushing

> 📘 Make sure you create a pipeline first!
>
> Find out more here [Quickstart](https://docs.mystic.ai/docs/quickstart).

To use the TR you have to make sure you're on the latest pipeline-ai package, and add in an additional field on the `pipeline.yaml` config file:

```yaml
...
extras:
    turbo_registry: true
```

You will then need to build the container as normal, by running:

```shell
pipeline container build
pipeline container up -d
```

It's important to run the container locally to validate that it functions!

Now you can upload with:

```shell
pipeline container push
```

# Limitations

Right now there's a few limitations to using Turbo Registry:

1. Images are compressed into a single layer. This means if there's any change to your code the whole thing has to be re-uploaded. Please see our roadmap for how we're going to solve this!
2. Additional RAM usage on machines that pull from TR. To make the image pull as fast as possible we use some RAM continuously once the container has started up. This will be fixed shortly.

# Roadmap

There's a lot that we're going to be doing with this incredible feature:

1. Server side container layer flattening. Right now you have to upload one file which contains the entire container, we're going to change this to traditional image uploading and then flatten it on the registry itself. This will make uploading much nicer!
2. Multithreaded uploading. Docker registries are notoriously slow to upload to, we can make this a lot faster but initially chose to focus on the downloading side.
3. Removing persistent RAM usage post container setup.
4. Open source! We're going to be open sourcing all of this work likely Q4 2024.
5. There's a lot more we're going to be improving but a lot of it is closed source behind the scenes for now, it's going to get a lot faster!