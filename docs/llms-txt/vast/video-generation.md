# Source: https://docs.vast.ai/video-generation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Video Generation

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Generate Videos Using ComfyUI on Vast.ai",
  "description": "A comprehensive guide to setting up and using ComfyUI for video generation on Vast.ai, including template configuration, model download, and workflow execution.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Select the ComfyUI Template",
      "text": "Navigate to the Templates tab and search for 'ComfyUI' among recommended templates. The ComfyUI template provides a powerful node-based interface for designing advanced pipelines. It includes access through Jupyter and SSH, Instance Portal, token-based authentication, and built-in provisioning script for models and custom nodes."
    },
    {
      "@type": "HowToStep",
      "name": "Configure Template Environment Variables",
      "text": "Edit your template configuration with environment variables: COMFYUI_ARGS for launch arguments, WEB_ENABLE_HTTPS and WEB_ENABLE_AUTH for security settings, CF_TUNNEL_TOKEN for Cloudflare Zero Trust, CIVITAI_TOKEN and HF_TOKEN for accessing gated models, and PROVISIONING_SCRIPT for custom setup. Never save template as public if tokens are included."
    },
    {
      "@type": "HowToStep",
      "name": "Create Instance and Connect",
      "text": "In the Search interface, look for machines with sufficient VRAM for your video model (check model requirements carefully). Click RENT to create an instance. Go to Instances tab and when the blue button says 'OPEN', click it to access the Instance Portal. Click the direct link or cloudflare quick tunnel link to access ComfyUI."
    },
    {
      "@type": "HowToStep",
      "name": "Select Video Workflow and Download Models",
      "text": "In ComfyUI, use the workflow browser to choose a template (e.g., LTX Video workflow). ComfyUI will alert you to missing models. Download required models to your instance using SSH with wget/curl commands to the correct directories (e.g., 'wget --content-disposition -P /workspace/ComfyUI/models/checkpoints/' for model files). Refresh browser after downloads complete."
    },
    {
      "@type": "HowToStep",
      "name": "Run the Workflow",
      "text": "Click the Run button to process the workflow. Feel free to modify prompts and experiment with different settings. You can also use pre-configured templates like 'ComfyUI + LTX Video' or 'Open-Sora' for faster setup."
    }
  ]
})
}}
/>

# Video Generation Guide: Using ComfyUI on Vast.ai

This guide will walk you through setting up and using ComfyUI for video generation on Vast.ai. ComfyUI provides a powerful node-based interface for creating advanced stable diffusion pipelines, making it ideal for video generation workflows.

## Prerequisites

* A Vast.ai account
* Basic familiarity with image or video generation models
* [(Optional) Read Jupyter guide](/documentation/instances/jupyter)
* [(Optional) SSH client installed on your local machine and SSH public key added in Account tab at cloud.vast.ai](/documentation/instances/sshscp)

## Setting Up Your Instance

### 1. Select the Right Template

Navigate to the Templates tab to view available templates. For video generation, we recommend searching for "ComfyUI" among the recommended templates.  [The ComfyUI template](https://cloud.vast.ai/?ref_id=62897\&creator_id=62897\&name=ComfyUI) provides a powerful and modular stable diffusion GUI for designing and executing advanced pipelines using a graph/nodes/flowchart based interface.

**Template Features:**

* Access through both Jupyter and SSH
* Instance Portal
* Token-based authentication enabled by default
* Built-in provisioning script for models and custom nodes

### 2. **Edit your Template Configuration**

**Add/update these environment variables as needed:**

```bash Bash theme={null}
# Core Settings
COMFYUI_ARGS="--disable-auto-launch --port 18188 --enable-cors-header"         # ComfyUI launch arguments

# Authentication
WEB_ENABLE_HTTPS=false   # Enable/disable direct HTTPS
WEB_ENABLE_AUTH=true    # Enable/disable authentication

# Access Tokens
CF_TUNNEL_TOKEN=""      # Cloudflare Zero Trust token
CIVITAI_TOKEN=""        # Access gated Civitai models
HF_TOKEN=""            # Access gated HuggingFace models

# Custom Setup
PROVISIONING_SCRIPT=""  # URL to custom provisioning script
```

**Provisioning Script:**

* Default script includes popular image models and custom nodes
* Fully customizable - Create your own script for a custom instance
* Must be Bash-compatible and start with `#!/bin/bash`
* Upload modified script to a GitHub Gist or respository and update the PROVISIONING\_SCRIPT variable to point to the raw file

<Warning>
  **Important: Never save your template as public if you've included tokens or other secrets in the Docker Options field.**
</Warning>

Select your template from '[My Templates](https://cloud.vast.ai/templates/)' after making any desired edits to it.

### 3. Create Your Instance

1. In the [Search interface](https://cloud.vast.ai/create/), look for machines that have **sufficient VRAM** to handle your chosen video model.  ⚠All models are different so check the model requirements carefully.
2. Click RENT to create an instance on the machine with the GPU of your choice

### 3. Connect to Your Instance

1. Go to [Instances tab](https://cloud.vast.ai/instances/) to see your instance loading
2. When the blue button says "OPEN", click this button to access the [Instance Portal](/documentation/instances/instance-portal) which will provide access to ComfyUI and other useful applications.
3. Click the direct link or cloudflare quick tunnel link to access ComfyUI. Here's a [beginner's guide to using ComfyUI](https://stable-diffusion-art.com/comfyui/).

### 4.  Select a Video Workflow

ComfyUI has a workflow browser, so for a quick start you can choose on of their templates

<Frame caption="ComfyUI Workflows">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation.png?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=efdb8c17316d44d1e12ce771385acb2a" alt="ComfyUI template workflows" data-og-width="1280" width="1280" data-og-height="623" height="623" data-path="images/use-cases-ai-video-generation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation.png?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=07e30c3fa5617278687a226a5a4a2cbf 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation.png?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=f15b6cc24ef1e38fd5a373896ff51094 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation.png?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=8bda75981991d22fdcf0b3bc0637298d 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation.png?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=9a9094ac13b9e21f16d2ce5b5f0f4993 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation.png?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=47495cdec8f5bccb759ae3336b14792b 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation.png?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=43cf5a5e8b2a9a84d8e51f0bd123e56c 2500w" />
</Frame>

We'll pick the LTX Video workflow for this guide.  Simply click it to proceed.

### 5. Download Missing Files

Your new instance will not yet have the required models, but fortunately ComfyUI will alert us to this and offer the models for download.

<img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-2.png?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=b11356de47a6b85046304819d2e8f93f" alt="ComfyUI template workflows" data-og-width="800" width="800" data-og-height="634" height="634" data-path="images/use-cases-ai-video-generation-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-2.png?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=90b23d7efe224df2413e7cb90b2594ca 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-2.png?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=7d178e1e0d718177447d44972a87c8d9 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-2.png?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=eb0327ae5bf24a8846e36864aa56d4ae 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-2.png?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=449287dac3896af2456cdfa01f564c46 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-2.png?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=923fbc1ad92eb52377eb671b521d6efc 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-2.png?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=4e3956d83979beedf27e4b22c1b1384f 2500w" />

Unfortunately, the interface does not know it is running in the cloud so clicking the download buttons will download the models to your local machine.  To work around this you can either:&#x20;

* Download the models to your computer and then upload them to the instance
* SSH to the instance and use `curl` or `wget` to directly download the models to their correct locations

To complete this guide we will use SSH

```bash Bash theme={null}
# Download the models
wget --content-disposition -P /workspace/ComfyUI/models/checkpoints/ "https://huggingface.co/Lightricks/LTX-Video/resolve/main/ltx-video-2b-v0.9.safetensors"
wget --content-disposition -P /workspace/ComfyUI/models/clip/ "https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors"

# Download the workflow source image
wget --content-disposition -P /workspace/ComfyUI/input/ "https://comfyanonymous.github.io/ComfyUI_examples/ltxv/island.jpg"
```

The above commands will download the required models into the instance.  When the downloads have completed you can refresh the browser window to clear the missing models error.

### 6. Run the Workflow

Finally, click the **Run** button to process the workflow.

<img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-3.png?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=58da0d2e64c44d049ca77eb3734267f1" alt="" data-og-width="1280" width="1280" data-og-height="611" height="611" data-path="images/use-cases-ai-video-generation-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-3.png?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=820ea14cb9b3f04ed69a10aa171c37a5 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-3.png?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=0fbbee485aa6b943c85327e146020238 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-3.png?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=ebbca017626d9161476926f5236ef45e 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-3.png?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=06074c1591266a8e3cbf4b6961931f48 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-3.png?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=a3914834059527694dad708276a9bbf6 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-video-generation-3.png?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=25fecb8e64f06fa34c0145a148e7dfa9 2500w" />

Feel free to modify the prompts and experiement!

## Pre-Configured Templates

We have some pre-configured ComfyUI templates - And one for this guide.  Check them out here

* [ComfyUI + LTX Video](https://cloud.vast.ai/?ref_id=62897\&creator_id=62897\&name=ComfyUI%20%2B%20LTX%20Video)
* [Open-Sora](https://cloud.vast.ai/?ref_id=62897\&creator_id=62897\&name=Open-Sora)

## Resources and Further Reading

1. [ComfyUI Official Repository](https://github.com/comfyanonymous/ComfyUI)
2. [Vast.ai Documentation](/documentation/get-started/index)
3. [Comfy Workflows](https://comfyworkflows.com/)
4. [Vast.ai support chat on website](https://vast.ai/)

Remember to always check VRAM usage and adjust parameters accordingly. Start with smaller frames and resolutions, then scale up as you become more comfortable with the workflow.
