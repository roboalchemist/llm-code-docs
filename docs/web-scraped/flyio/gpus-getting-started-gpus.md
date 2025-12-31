# Source: https://fly.io/docs/gpus/getting-started-gpus/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Getting Started with Fly GPUs 

## [](#how-do-i-run-a-gpu-machine-on-fly-io)[How do I run a GPU Machine on Fly.io?] 

A Fly GPU Machine works very similarly to a CPU-only (or "normal") Fly Machine, and has access to the same platform features by default. It boots up with GPU drivers installed and you can run `nvidia-smi` right away. So running a Fly App that uses CUDA compute is a slight variation on running any Fly App. In a nutshell:

1.  Make sure GPUs are enabled on your Fly Organization.
2.  Tell the Fly Platform to provision your Machines on Fly GPU hosts.
3.  Provide a Docker image or Dockerfile for your project that installs the NVIDIA libraries your project uses, alongside the rest of your project.
4.  Carry on as you would for any Fly App, tailoring it to the needs of your application.

**Aside:** Firecracker doesnâ€™t do GPUs, so GPU-enabled Machines run under Cloud Hypervisor instead. This means youâ€™ll see some different output in logs, but in general you donâ€™t have to think about this.

## [](#placing-your-machines-on-gpu-hosts)[Placing your Machines on GPU hosts] 

Not all of Fly.io's physical servers have GPUs attached to them, so you have to tell the platform your requirements before the Machine is created on a host.

Configuration is done by different means depending on whether you're using Fly Launch to manage your app, or running Machines individually using the API or the [`fly machine run` command](/docs/machines/run/).

### [](#specify-the-gpu-model)[Specify the GPU model] 

Assuming that you're going the [Fly Launch](/docs/launch/) way and configuring your Machines app-wide, you can include a line like the following in your `fly.toml` file before running `fly deploy` for the first time:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
vm.size = "a100-40gb"
```

The `a100-40gb` preset is the `a100-pcie-40gb` GPU with theÂ `performance-8x`Â CPU config and 32GB RAM. You can exert more granular control over resources using the [`[[vm]]` table](/docs/reference/configuration/#the-vm-section) in `fly.toml`.

Run `fly platform vm-sizes` to get the list of presets, and check out the [pricing page](/docs/about/pricing/#gpus-and-fly-machines) to help you plan ahead.

### [](#specify-the-region)[Specify the region] 

But you're not done! For `fly deploy` to succeed in provisioning your Machine(s), the app's `primary_region` must match a region that hosts the kind of GPU you're asking for. At the time of writing, `a100-40gb` GPUs are only available in `ord`. Set the initial region in `fly.toml`:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
primary_region = "ord"  # If you change this, ensure it's to a region that offers the GPU model you want
```

Currently GPUs are available in the following regions:

-   `a10`:Â `ord`
-   `l40s`:Â `ord`
-   `a100-40gb`:Â `ord`
-   `a100-80gb`:Â `iad`,Â `sjc`,Â `syd`, `ams`

### [](#change-gpu-model)[Change GPU model] 

GPU models are located in different regions, so you'll likely have to destroy any existing Machines before redeploying using a different GPU spec.

## [](#choosing-a-docker-base-image)[Choosing a Docker base image] 

Many open-source ML projects have ready-made Docker images; for example: [Ollama![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgY2xhc3M9ImlubGluZS1mbGV4IG1sLTIgc2VsZi1jZW50ZXIgcG9pbnRlci1ldmVudHMtbm9uZSIgdmlld2JveD0iMCAwIDE0IDE0Ij48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS4zIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMi42MjUgNC44MjVjMC0yLjMxOC0xLjg4Mi00LjItNC4yLTQuMmgtMy42YTQuMjAyIDQuMjAyIDAgMDAtNC4yIDQuMnYzLjZjMCAyLjMxOCAxLjg4MiA0LjIgNC4yIDQuMmgzLjZjMi4zMTggMCA0LjItMS44ODIgNC4yLTQuMnYtMy42ek00LjQ4MiA4LjYyNWw0LTQiPjwvcGF0aD48cGF0aCBkPSJNOC40ODIgNy4yOTdWNC42MjVINS44MSI+PC9wYXRoPjwvZz48L3N2Zz4=)](https://ollama.ai/blog/ollama-is-now-available-as-an-official-docker-image), [Basaran![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgY2xhc3M9ImlubGluZS1mbGV4IG1sLTIgc2VsZi1jZW50ZXIgcG9pbnRlci1ldmVudHMtbm9uZSIgdmlld2JveD0iMCAwIDE0IDE0Ij48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS4zIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMi42MjUgNC44MjVjMC0yLjMxOC0xLjg4Mi00LjItNC4yLTQuMmgtMy42YTQuMjAyIDQuMjAyIDAgMDAtNC4yIDQuMnYzLjZjMCAyLjMxOCAxLjg4MiA0LjIgNC4yIDQuMmgzLjZjMi4zMTggMCA0LjItMS44ODIgNC4yLTQuMnYtMy42ek00LjQ4MiA4LjYyNWw0LTQiPjwvcGF0aD48cGF0aCBkPSJNOC40ODIgNy4yOTdWNC42MjVINS44MSI+PC9wYXRoPjwvZz48L3N2Zz4=)](https://github.com/hyperonym/basaran), [LocalAI![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgY2xhc3M9ImlubGluZS1mbGV4IG1sLTIgc2VsZi1jZW50ZXIgcG9pbnRlci1ldmVudHMtbm9uZSIgdmlld2JveD0iMCAwIDE0IDE0Ij48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS4zIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMi42MjUgNC44MjVjMC0yLjMxOC0xLjg4Mi00LjItNC4yLTQuMmgtMy42YTQuMjAyIDQuMjAyIDAgMDAtNC4yIDQuMnYzLjZjMCAyLjMxOCAxLjg4MiA0LjIgNC4yIDQuMmgzLjZjMi4zMTggMCA0LjItMS44ODIgNC4yLTQuMnYtMy42ek00LjQ4MiA4LjYyNWw0LTQiPjwvcGF0aD48cGF0aCBkPSJNOC40ODIgNy4yOTdWNC42MjVINS44MSI+PC9wYXRoPjwvZz48L3N2Zz4=)](https://localai.io/basics/getting_started/). Check out [GitHub `fly-apps` repos with theÂ `gpu`Â topic![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgY2xhc3M9ImlubGluZS1mbGV4IG1sLTIgc2VsZi1jZW50ZXIgcG9pbnRlci1ldmVudHMtbm9uZSIgdmlld2JveD0iMCAwIDE0IDE0Ij48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS4zIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMi42MjUgNC44MjVjMC0yLjMxOC0xLjg4Mi00LjItNC4yLTQuMmgtMy42YTQuMjAyIDQuMjAyIDAgMDAtNC4yIDQuMnYzLjZjMCAyLjMxOCAxLjg4MiA0LjIgNC4yIDQuMmgzLjZjMi4zMTggMCA0LjItMS44ODIgNC4yLTQuMnYtMy42ek00LjQ4MiA4LjYyNWw0LTQiPjwvcGF0aD48cGF0aCBkPSJNOC40ODIgNy4yOTdWNC42MjVINS44MSI+PC9wYXRoPjwvZz48L3N2Zz4=)](https://github.com/orgs/fly-apps/repositories?q=topic%3Agpu) for some examples.

If you're building your own image, choose a base image that [NVIDIA supports![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgY2xhc3M9ImlubGluZS1mbGV4IG1sLTIgc2VsZi1jZW50ZXIgcG9pbnRlci1ldmVudHMtbm9uZSIgdmlld2JveD0iMCAwIDE0IDE0Ij48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS4zIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMi42MjUgNC44MjVjMC0yLjMxOC0xLjg4Mi00LjItNC4yLTQuMmgtMy42YTQuMjAyIDQuMjAyIDAgMDAtNC4yIDQuMnYzLjZjMCAyLjMxOCAxLjg4MiA0LjIgNC4yIDQuMmgzLjZjMi4zMTggMCA0LjItMS44ODIgNC4yLTQuMnYtMy42ek00LjQ4MiA4LjYyNWw0LTQiPjwvcGF0aD48cGF0aCBkPSJNOC40ODIgNy4yOTdWNC42MjVINS44MSI+PC9wYXRoPjwvZz48L3N2Zz4=)](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#system-requirements);Â `ubuntu:22.04`Â is a solid choice that's compatible with the CUDA driver GPU Machines use. You canÂ launch a vanilla Ubuntu image and run `nvidia-smi` with no further setup.

From there, install whatever packages your project needs. This will include some libraries from NVIDIA if you want to do something more than admire the output of `nvidia-smi`.

## [](#installing-nvidia-libraries)[Installing NVIDIA libraries] 

You don't need to install any `cuda-drivers` packages in the Docker image, but you'll want some subset of [NVIDIA's GPU-accelerated libraries![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgY2xhc3M9ImlubGluZS1mbGV4IG1sLTIgc2VsZi1jZW50ZXIgcG9pbnRlci1ldmVudHMtbm9uZSIgdmlld2JveD0iMCAwIDE0IDE0Ij48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS4zIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMi42MjUgNC44MjVjMC0yLjMxOC0xLjg4Mi00LjItNC4yLTQuMmgtMy42YTQuMjAyIDQuMjAyIDAgMDAtNC4yIDQuMnYzLjZjMCAyLjMxOCAxLjg4MiA0LjIgNC4yIDQuMmgzLjZjMi4zMTggMCA0LjItMS44ODIgNC4yLTQuMnYtMy42ek00LjQ4MiA4LjYyNWw0LTQiPjwvcGF0aD48cGF0aCBkPSJNOC40ODIgNy4yOTdWNC42MjVINS44MSI+PC9wYXRoPjwvZz48L3N2Zz4=)](https://developer.nvidia.com/gpu-accelerated-libraries). `libcublas-12-2` (linear algebra) and `libcudnn8` (deep-learning primitives) are a common combination, along with [`cuda-nvcc`![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgY2xhc3M9ImlubGluZS1mbGV4IG1sLTIgc2VsZi1jZW50ZXIgcG9pbnRlci1ldmVudHMtbm9uZSIgdmlld2JveD0iMCAwIDE0IDE0Ij48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS4zIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMi42MjUgNC44MjVjMC0yLjMxOC0xLjg4Mi00LjItNC4yLTQuMmgtMy42YTQuMjAyIDQuMjAyIDAgMDAtNC4yIDQuMnYzLjZjMCAyLjMxOCAxLjg4MiA0LjIgNC4yIDQuMmgzLjZjMi4zMTggMCA0LjItMS44ODIgNC4yLTQuMnYtMy42ek00LjQ4MiA4LjYyNWw0LTQiPjwvcGF0aD48cGF0aCBkPSJNOC40ODIgNy4yOTdWNC42MjVINS44MSI+PC9wYXRoPjwvZz48L3N2Zz4=)](https://developer.nvidia.com/cuda-llvm-compiler) for compiling stuff with CUDA support.

In general, you'll install NVIDIA libs using your Linux package manager. In a Python environment, it's possible to skip system-wide installation and use pip packages instead.

Tips:

-   Be deliberate about how much cruft you put in your Docker image. Avoid meta-packages likeÂ `cuda-runtime-*`.
-   `cuda-libraries-12-2`Â is a convenient, but bulky, start. Once you know what libs are needed at build and runtime, pick accordingly to optimize final image size.
-   Use multi-stage docker builds as much as possible.

To install packages from NVIDIA repos, you'll need the `ca-certificates` and `cuda-keyring` packages first.

## [](#where-to-store-data)[Where to store data] 

Machine learning tends to involve large quantities of data. We're working with a few constraints:

-   Large Docker images (many gigabytes) can be very unwieldy to push and pull, particularly over large geographical distances.
-   The root file system of a Fly Machine is ephemeral -- it's reset from its Docker image on every restart. It's also limited to 50GB on GPU-enabled Machines.
-   Fly Volumes are limited to 500GB, and are attached to a physical server. The Machine must run on the same hardware as the volume it mounts.

Unless you've got a constant workload, you'll likely want to shut down GPU Machines when they're not needed---you can do this manually withÂ `fly machine stop`, [have the main process exit](/docs/launch/autostop-autostart/#apps-that-shut-down-when-idle) when idle, or use the Fly Proxy [autostop and autostart](/docs/launch/autostop-autostart/) features---to save money. Saving data on a persistent Fly Volume means you don't have to download large amounts of data, or reconstitute a large Docker image into a rootfs, whenever the Machine restarts. You'll probably want to store models, at least, on a volume.

## [](#using-swap)[Using swap] 

Designing your workload and provisioning appropriate resources for it are the first line of defense against losing work by running out of memory (system RAM or VRAM).

You can also enable swap for system RAM on a Fly Machine, simply by including a line like the following in `fly.toml`:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
swap_size_mb = 8192    # This enables 8GB swap
```

Keep in mind that this consumes the commensurate amount of space on the Machine's root file system, leaving less capacity for whatever else you want to store there.

If you need more system RAM and faster performance, also scale up withÂ `fly scale memory`.

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fgpus%2Fgetting-started-gpus.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Getting+Started+with+Fly+GPUs%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fgpus%2Fgetting-started-gpus%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fgpus%2Fgetting-started-gpus.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Getting+Started+with+Fly+GPUs%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/gpus/getting-started-gpus.html.md)