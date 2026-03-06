# Source: https://docs.vast.ai/documentation/templates/creating-templates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Templates

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Create Templates on Vast.ai",
  "description": "A step-by-step tutorial on creating your first Vast.ai template, from opening the template editor to saving and launching your configured instance.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Open the Template Editor",
      "text": "Go to cloud.vast.ai/templates and find a recommended template like NVIDIA CUDA. Click the pencil icon to edit. You'll see two tabs: Config and ReadMe. Stay on the Config tab."
    },
    {
      "@type": "HowToStep",
      "name": "Give Your Template a Name",
      "text": "In the Identification section, change the Template Name to something descriptive (e.g., 'My First Template'). Add a Template Description if you'd like (optional)."
    },
    {
      "@type": "HowToStep",
      "name": "Choose Your Docker Image",
      "text": "In the Docker Repository And Environment section, enter the Image Path:Tag field. You can use any public Docker image (e.g., nginx:latest, postgres:14), Vast.ai base images (e.g., vastai/base-image, vastai/pytorch), or your own custom images from any registry."
    },
    {
      "@type": "HowToStep",
      "name": "Configure Ports and Environment Variables (Optional)",
      "text": "If your application needs external access, add ports in the Ports section. If your Docker image requires environment variables, add them in the Environment Variables section. Never put sensitive information in template environment variables if you plan to make the template public."
    },
    {
      "@type": "HowToStep",
      "name": "Choose a Launch Mode",
      "text": "Select how you want to access your instance: Jupyter + SSH (best for interactive development), SSH only (if you don't need Jupyter), or docker ENTRYPOINT (if you want the container to run exactly as designed). For most use cases, keep the default (Jupyter + SSH)."
    },
    {
      "@type": "HowToStep",
      "name": "Save Your Template",
      "text": "Scroll to the bottom and click one of the save buttons: Create (saves the template to 'My Templates' for later use) or Create & Use (saves and immediately takes you to the offers page to rent an instance)."
    }
  ]
})
}}
/>

## Introduction

Creating a template is simple - it's just telling Vast.ai how you want your instances to be configured. This guide will walk you through creating your first template step by step.

## Prerequisites

* A Vast.ai account
* [SSH client installed on your local machine and SSH public key added in the SSH Keys tab in the Keys section of your console](https://cloud.vast.ai/manage-keys/)&#x20;
* [(Optional) Install and use vast-cli](/cli/get-started)&#x20;

## Ways to Create Templates

You have three options:

### 1. Edit an Existing Template (Recommended for Beginners)

Start with one of our recommended templates and customize it to your needs. This is the easiest way to get started.

**Best for:** First-time users, quick customization of existing setups

### 2. Create from Scratch

Click "+ New" on the templates page for a blank template and configure everything yourself.

**Best for:** Users who know exactly what they need

### 3. Use an Existing Docker Image

Find a Docker image on DockerHub or another registry and create a template around it.

**Best for:** Users with a specific application in mind (e.g., nginx, postgres, a specific ML framework)

## Tutorial: Create Your First Template

Let's create a simple template together. We'll edit the NVIDIA CUDA template from the [Quick Start](/documentation/templates/quickstart) guide.

### Step 1: Open the Template Editor

1. Go to [cloud.vast.ai/templates](https://cloud.vast.ai/templates/)
2. Find the "NVIDIA CUDA" template (or any recommended template)
3. Click the pencil icon to edit

<Frame caption="Template editor showing Config tab">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=92d2cbbecc86af090d7d43a8e6409515" alt="Template editor showing Config tab" data-og-width="936" width="936" data-og-height="294" height="294" data-path="images/console-templates-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=b326bc9a8573f910771c8078028477b3 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=1e16e256733332321ed15b0477c7c5d4 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=960ce67c4b5e6bef28204d285e9d6af5 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e9a3251d5cc29821078a0c685735afb4 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=9bf15355378ba5f5f296b6a27c689aab 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=c6fb73fca150d0b06f40a727e01de7d0 2500w" />
</Frame>

You'll see two tabs: `Config` and `ReadMe`. Stay on the Config tab.

### Step 2: Give Your Template a Name

In the **Identification** section:

* Change the **Template Name** to something descriptive (e.g., "My First Template")
* Add a **Template Description** if you'd like (optional)

### Step 3: Choose Your Docker Image

In the **Docker Repository And Environment** section, you'll see the **Image Path:Tag** field.

You can use:

* **Any public Docker image** (e.g., `nginx:latest`, `postgres:14`, `python:3.11`)
* **Vast.ai base images** (e.g., `vastai/base-image`, `vastai/pytorch`)
* **Your own custom images** from any registry

For this tutorial, keep the existing NVIDIA CUDA image or try `nginx:latest` for a simple web server.

<Note>
  For a complete explanation of all Docker settings, see our [Template Settings](/documentation/templates/template-settings#docker-repository-and-environment) guide.
</Note>

### Step 4: Add Ports (Optional)

If your application needs external access, add ports in the **Ports** section.

For example, if you're running nginx, add port `80`.

### Step 5: Set Environment Variables (Optional)

If your Docker image requires environment variables, add them in the **Environment Variables** section.

<Warning>
  Never put sensitive information (passwords, API keys) in template environment variables if you plan to make the template public. Use your [account settings](https://cloud.vast.ai/account/) instead.
</Warning>

### Step 6: Choose a Launch Mode

Select how you want to access your instance:

* **Jupyter + SSH** - Best for interactive development (default for most use cases)
* **SSH only** - If you don't need Jupyter
* **docker ENTRYPOINT** - If you want the container to run exactly as designed

For this tutorial, keep the default (Jupyter + SSH).

<Note>
  For detailed information about launch modes, see our [Template Settings](/documentation/templates/template-settings#select-launch-mode) guide.
</Note>

### Step 7: Save Your Template

Scroll to the bottom and click one of the save buttons:

* **Create** - Saves the template to "My Templates" for later use
* **Create & Use** - Saves and immediately takes you to the offers page to rent an instance

<Frame caption="Save buttons">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=204e5427f10491896bdfd3da4001ef7e" alt="Save buttons" data-og-width="800" width="800" data-og-height="139" height="139" data-path="images/console-templates-15.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=882f55ab8e980cee4c909756332105d2 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=3c762e2f60ae6b0e493a7fb390f8f684 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ffa93edd1d40351184f2741d546fe37c 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e7455ee727b36380074c4f246719f09b 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=4a4996d972ab492832c1443938572b2e 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ff72dd2126f7020597b1e9c21c0c14aa 2500w" />
</Frame>

Congratulations! You've created your first template.

## Next Steps

Now that you know the basics, you can:

### Explore All Template Options

See our [Template Settings](/documentation/templates/template-settings) for complete documentation of every field in the template editor.

### Add Advanced Customization

Learn about runtime customization and building custom Docker images in our [Advanced Setup](/documentation/templates/advanced-setup) guide:

* **PROVISIONING\_SCRIPT** - Run setup scripts when instances start
* **PORTAL\_CONFIG** - Configure the Instance Portal
* **Base Images** - Build custom Docker images with Vast.ai security features
* **VM Templates** - When to use virtual machines instead of containers

### Manage Your Templates

Learn how to update, share, and troubleshoot templates in our [Managing Templates](/documentation/templates/managing-templates) guide.

### See Real Examples

Check out our [GROBID example](/documentation/templates/examples/grobid) to see a complete template creation workflow for a real application.

## Common Use Cases

### I want to run a specific application (e.g., nginx, postgres)

1. Find the official Docker image on [DockerHub](https://hub.docker.com/)
2. Create a template with that image path
3. Add required ports and environment variables
4. Save and launch

### I want to customize a Vast recommended template

1. Edit one of our recommended templates
2. Add a PROVISIONING\_SCRIPT environment variable pointing to your setup script
3. See [Advanced Setup](/documentation/templates/advanced-setup#provisioning-script) for details

### I want to build my own custom Docker image

1. Create a Dockerfile (optionally FROM a Vast base image)
2. Build and push to a container registry
3. Create a template with your custom image path
4. See [Advanced Setup](/documentation/templates/advanced-setup#building-custom-docker-images) for details
