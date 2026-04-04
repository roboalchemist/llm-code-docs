# Source: https://img.ly/docs/cesdk/renderer/get-started/commandline-4231be/

---
title: "Licensed codec setup"
description: "Setting up the avlicensed variant of CE.SDK Renderer"
platform: renderer
url: "https://img.ly/docs/cesdk/renderer/get-started/commandline-4231be/"
---

> This is one page of the CE.SDK Renderer documentation. For a complete overview, see the [Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/renderer/llms-full.txt).

**Navigation:** [Get Started](https://img.ly/docs/cesdk/renderer/get-started/overview-e18f40/) > [Licensed codec setup](https://img.ly/docs/cesdk/renderer/get-started/commandline-4231be/)

---

The **avlicensed** commercial variant of CE.SDK Renderer includes products, performing audio and video encoding and decoding functions, which are provided by and are copyright of Fluendo S.A..

See the [Patents & Acknowledgements](https://img.ly/docs/cesdk/renderer/get-started/patents-acknowledgements-9k2p4m/) section for more details on the proprietary technologies.

This version can only be obtained through our dashboard and after signing up for a CE.SDK subscription from a private container registry we provide.

It's also subject to a concurrency limit as negotiated in your contract, only a specified number of CE.SDK Renderer instances can be running simultaneously.

## Authenticating with the private IMG.LY Container Registry

Assuming you've already set up a valid Docker daemon on your system, you can log into our private registry with the API key associated with your Linux codec license from the Dashboard:

```bash
sudo docker login container.img.ly -u "oauth" -p "YOUR-API-KEY"
```

The login will locally store an authentication token in your user's docker configuration file, valid for 1 hour without automatic renewal.
After one hour, the authentication step has to be done again if further access to the container registry is needed.
We recommend fetching and mirroring the containers you need to your own private container registry, like the Elastic Container Registry in Amazon Web Services or the Google Artifact Registry if using the Google Cloud Platform.

### Fetching the AV-licensed containers

Container variants with proprietary codec technology are pushed to that registry and can be fetched with these tags:

```bash
# Assetless variant for use with your own assets tree or CDN
sudo docker pull container.img.ly/imgly/cesdk-renderer-avlicensed-assetless:$UBQ_VERSION$
# Variant with bundled assets for faster exports without a network round-trip needed for most scene elements
sudo docker pull container.img.ly/imgly/cesdk-renderer-avlicensed:$UBQ_VERSION$
```

### Usage of the AV-licensed containers

The containers can be used exactly like their non-avlicensed counterparts, the only difference is the requirement for a codec license API key to unlock the patented codec technology.

## Troubleshooting & Common Errors

**❌ Error encountered while creating an EGL hardware-accelerated context, falling back to CPU rendering: EGL initialize error: UNKNOWN**

- Make sure the GPU setup instructions were followed, this error indicates that a hardware OpenGL context could not be created inside the container.
- This could also be expected if testing the container on a machine without a GPU.

**❌ Error: `Invalid license key`**

- Verify that your **license key** is correct and not expired, or remove the key entirely to get watermarked output.

**❌ Error: `Max concurrency reached`**

- The avlicensed variant of the Renderer only allows up to a certain number of instances running simultaneously, as negotiated in your contract. To avoid running into the limit, limit your max deployment size to below this limit, or implement an exponential backoff retry system.



---

## More Resources

- **[Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md)** - Browse all Renderer documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/renderer/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/renderer/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
