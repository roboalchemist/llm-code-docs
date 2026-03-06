# Source: https://docs.vast.ai/documentation/templates/introduction.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Templates

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Introduction to Vast.ai Templates",
  "description": "Understanding Vast.ai templates as configuration wrappers for Docker instances, including recommended templates, Vast.ai base images, Instance Portal, and virtual machine templates.",
  "author": {
    "@type": "Organization",
    "name": "Vast.ai"
  },
  "datePublished": "2025-05-12",
  "dateModified": "2025-08-04",
  "articleSection": "Templates Documentation",
  "keywords": ["templates", "docker", "base images", "instance portal", "vast.ai", "GPU instances", "virtual machines"]
})
}}
/>

## What is a Template?

A template is how Vast helps you launch an instance, setting up your rented machine with whatever software and formatting you need. Templates are generally used for launching instances through the web interface, but they can also be used in the CLI or through the API.  In this document, we will focus on the web interface, but we will link to other relevant documentation throughout.

In the simplest technical terms, you can consider a template to be a wrapper around `docker run`. The template contains all of the information you want to pass to our systems to configure the environment.

You can browse the template section of the web interface at [cloud.vast.ai/templates](https://cloud.vast.ai/templates/)

## Recommended Templates

We provide several recommended templates to help you get started.  These are pre-configured environments that you can use as-is, or you can tweak them to your own requirements. &#x20;

<Note>
  It's a great idea to look at how these templates have been configured to guide you in creating your own.
</Note>

### Vast.ai Base Images

Our recommended templates are built on Vast.ai base images like `vastai/base-image` and `vastai/pytorch`. You can find the source code on [`GitHub`](https://github.com/vast-ai/base-image/).

These are large Docker images that contain CUDA development libraries, node + npm, OpenCL and other useful libraries. Despite their large size you'll find they generally start quickly because they have been cached on many of the host machines.

**Why use Vast.ai base images?**

* **Faster cold boots** due to frequent caching on host machines
* **Built-in security features** through Caddy proxy
* **Automatic TLS encryption** for web services
* **Authentication token protection** for all services
* **Proper isolation** between external and internal services
* **Instance Portal** integration (explained below)
* **PROVISIONING\_SCRIPT** support for easy customization

### Instance Portal

When you click the Open button on an instance running one of our recommended templates, you'll see the Instance Portal:

<Frame caption="Instance portal landing page">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-18.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f1c027a606889dd4301b0cbfbc1abe8b" alt="Instance portal landing page" data-og-width="1280" width="1280" data-og-height="509" height="509" data-path="images/console-templates-18.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-18.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=786b86dc4b009a122179aae08e3c6040 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-18.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=629b8c39a8b0a1e59c17cec237d56f1e 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-18.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f18aece8e32134eb4a7917f2de83b74b 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-18.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=1c2fbb97bded3f69d8fe77086c209b0e 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-18.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=54151d2738fc3df59ca2ba177119682e 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-18.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=0cdb5b424c06b59a5a1ed921d8bb5d24 2500w" />
</Frame>

The **Instance Portal** provides easy access links to services running in your instance. It places an authentication layer in front of these services to prevent access by anyone who does not have the correct authentication token. You can also create tunnels to your services without exposing ports.

Full documentation for the Instance Portal is available in our [Instance Portal guide](/documentation/instances/instance-portal).

## Instance Setup

### Docker Execution Environment

The standard and most common way to run instances on Vast.ai is using Docker containers. When you select a template, it launches a Docker container with your specified image and configuration.

**Docker templates are ideal for:**

* Running pre-configured ML frameworks (PyTorch, TensorFlow, etc.)
* Deploying web services and APIs
* Development environments with Jupyter notebooks
* Custom applications with specific dependencies

All of our recommended templates use Docker containers, providing isolation, reproducibility, and easy deployment across different host machines.

### Virtual Machine Templates

In addition to standard Docker container templates, we also offer Virtual Machine (VM) templates. These launch a full virtual machine environment rather than a docker container.

**When to use VM templates:**

* Run applications that require namespace support
* Run more than one Docker container in an instance
* Load kernel modules or run profiling jobs
* Mount remote drives with rclone or similar

You can edit VM templates just like regular templates, but you should not change the docker image field. Only the images we distribute from `docker.io/vastai/kvm` will work.

## Customizing Recommended Templates

To learn how to customize our recommended templates with provisioning scripts or build your own custom Docker images, see our [Advanced Setup](/documentation/templates/advanced-setup) guide.

## Next Steps

<CardGroup cols={3}>
  <Card title="Quick Start" href="/documentation/templates/quickstart" icon="rocket">
    Run your first template in minutes
  </Card>

  <Card title="Create Templates" href="/documentation/templates/creating-templates" icon="hammer">
    Build custom templates for your needs
  </Card>

  <Card title="Advanced Setup" href="/documentation/templates/advanced-setup" icon="cog">
    Provisioning scripts and Docker customization
  </Card>
</CardGroup>
