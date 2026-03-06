# Source: https://docs.vast.ai/documentation/templates/template-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Template Settings

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Vast.ai Template Settings Reference",
  "description": "Complete reference documentation for all settings and options available when configuring a Vast.ai template including Docker configuration, launch modes, environment variables, ports, authentication, and visibility settings.",
  "author": {
    "@type": "Organization",
    "name": "Vast.ai"
  },
  "articleSection": "Templates Documentation",
  "keywords": ["template settings", "docker configuration", "launch modes", "environment variables", "ports", "vast.ai", "reference", "documentation"]
})
}}
/>

## Overview

This guide documents all settings and options available when configuring a template. Use this guide when you need to understand what a specific setting does or how to configure a particular option.

For a step-by-step tutorial on creating your first template, see [Creating Templates](/documentation/templates/creating-templates).

For advanced customization techniques, see [Advanced Setup](/documentation/templates/advanced-setup).

## Identification

The first section helps you to keep your templates organized.

<Frame caption="Identification section of the template editor">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=92d2cbbecc86af090d7d43a8e6409515" alt="Identification section of the template editor" data-og-width="936" width="936" data-og-height="294" height="294" data-path="images/console-templates-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=b326bc9a8573f910771c8078028477b3 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=1e16e256733332321ed15b0477c7c5d4 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=960ce67c4b5e6bef28204d285e9d6af5 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e9a3251d5cc29821078a0c685735afb4 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=9bf15355378ba5f5f296b6a27c689aab 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-5.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=c6fb73fca150d0b06f40a727e01de7d0 2500w" />
</Frame>

**Template Name**

This will be displayed in bold on the template card. Choose something that helps you identify the template amongst your other templates.

**Template Description**

This field helps describe the function and purpose of the template. Completely optional for your own purposes, but very helpful if you intend to make this template public or share it with others.

## Docker Repository And Environment

This is where you define the Docker image you want to run, along with any options we want to pass into the container.

<Frame caption="Docker section of the template editor">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-6.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=2dd0053fa0ec8cd91fa23d4bf8185318" alt="Docker section of the template editor" data-og-width="844" width="844" data-og-height="775" height="775" data-path="images/console-templates-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-6.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=bfd7dbb3ce076232e55a8536bcba90cd 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-6.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=1516f5878cf2ac74fed48b159aaf48a9 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-6.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f987e6d61bf53e6921960aa8ecd08b9a 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-6.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=3bc65674968d0cd6fe5042bfff602a3b 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-6.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=cd79074383be2f3b0159c8d0510a8c74 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-6.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=152ce71cfb3f7357390cdd4700a8faaf 2500w" />
</Frame>

**Image Path:Tag**

Here is where you can define the docker image to run. This field must be in the format `repository/image_name:tag`.

Many of our templates pull from DockerHub but you can use any container registry - Just remember to add the full path if you're using an alternative registry. Eg. `nvcr.io/nvidia/pytorch:25.04-py3`

You can use any Docker image:

* Public images from DockerHub (e.g., `nginx:latest`, `postgres:14`, `python:3.11`)
* Vast.ai base images (e.g., `vastai/base-image`, `vastai/pytorch`)
* Your own custom images from any registry
* Images from alternative registries (GitHub Container Registry, Google Container Registry, etc.)

**Version Tag**

For many registries we are able to pull the available list of tags so this field allows you to quickly select another version.

There is also a special `[Automatic]` tag you can use. With this selected, the machine you choose for your instance will pull the most recent docker image that is compatible with that machine's own CUDA version.&#x20;

This will only work if the image tag contains the CUDA version string. For example: `my-image-cuda-12.8` would be loaded on a machine supporting CUDA 12.8, but a machine with only CUDA 12.6 would pull `my-image-cuda-12.6`

**Docker Options**

This field is a textual representation of the ports and environment variables declared in the sections beneath it. You can edit it directly or you can use the page widgets.

<Note>
  This field will only accept ports and environment variables. Other docker run options will be ignored.
</Note>

**Ports**

To access your instance via the external IP address, you will need to add some ports to the template. You can add both TCP and UDP ports.

When your instance is created, a port will be randomly assigned to the external interface which will map into the instance port you selected.

You can also use SSH to open a tunnel to access ports. Use a command like:

```text  theme={null}
ssh -p [SSH_PORT] [USER]@[REMOTE_HOST] -L [LOCAL_PORT]:localhost:[REMOTE_PORT]
ssh -p 22 user@remote.example.com -L 8080:localhost:8080
```

The machine will forward traffic from the host machine's public port to the container port you specified.

**Environment Variables**

Here you can add any environment variables that your docker image requires. Do not save any sensitive information here if you are planning to make the template public.

Place any variables with sensitive values into the Environment Variables section of your [account settings page](https://cloud.vast.ai/account/). They will then be made available in any instance you create, regardless of the template used.

Special environment variables like `PROVISIONING_SCRIPT` and `PORTAL_CONFIG` can be used to customize Vast templates - see our [Advanced Setup](/documentation/templates/advanced-setup) guide for details.

You can find out more about port mapping and special environment variables in our [Docker Execution Environment](/documentation/instances/docker-execution-environment) guide.

## Select Launch Mode

Templates offer three launch modes you can select from. Our recommended templates will usually launch in Jupyter mode for easiest access, but you are free to choose whichever suits your needs.

<Frame caption="Launch mode selection options">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-7.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=accc9a98a9c908de96ffd1be1b44979b" alt="Launch mode selection options" data-og-width="936" width="936" data-og-height="191" height="191" data-path="images/console-templates-7.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-7.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=fe6bd58c7bb8e942baa1e07f714df807 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-7.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ed25b25c7de241a57a6ef26b49fd8fe4 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-7.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=9c708ed19996a249cec72a6eae791bd1 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-7.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=56e8dcfd5d4704647e9391fcc013f3a2 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-7.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=9d57ee991fa568a44878ba3567799dc8 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-7.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=466d12e23ca96bc9d03d5059a428612d 2500w" />
</Frame>

**Jupyter-python notebook + SSH**

When you run the template in this mode, we will install Jupyter and SSH at runtime. Jupyter will be available on mapped port `8080` and SSH will be available on mapped port `22`.

**Interactive shell server, SSH**

As above, but SSH only with no Jupyter installation.

<Warning>
  In both Jupyter and SSH mode, the docker entrypoint for your image will not be run. It will be replaced with our instance setup script so you should use the on start section (documented below) to start any services.
</Warning>

**docker ENTRYPOINT**

In this mode, your Docker image will run precisely as it is. We will not include any additional software or access methods. If your Docker image does not offer SSH or another appropriate interface, please select one of the alternative modes if you need to interact with the running instance.

An additional field will be shown when using this launch mode to allow passing arguments to the image entrypoint.

<Frame caption="Field allowing for argument passing">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-8.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=afd38e3ca501849480e31ebb8cfd7215" alt="Field allowing for argument passing" data-og-width="936" width="936" data-og-height="63" height="63" data-path="images/console-templates-8.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-8.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f7441a7220cf1431cc15370a8e0dea82 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-8.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=34185f64e9d1438b0d61bb29c48a6564 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-8.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=cc6f950b7d52774f691832735d3d0090 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-8.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=699a98f18f6580f738e68a0cb084ac38 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-8.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=59b5ee232756140b55757c5e0c56cf34 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-8.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=1b624c363b9472bb7daee330e9862fe4 2500w" />
</Frame>

## On-start Script

Here you can enter a short Bash script which will be run during instance startup. It is only available when using the Jupyter or SSH launch modes, and is most useful for starting any services that your docker image would have launched if the entrypoint had been executed.

<Frame caption="On-start Script">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-9.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e5684180dfcbbb1b24441dda6dc62851" alt="On-start Script" data-og-width="936" width="936" data-og-height="177" height="177" data-path="images/console-templates-9.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-9.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ffc64a21cca13ae1be0deb35c3326204 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-9.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=462a27c896e9ffaf6457361c5beac9aa 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-9.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=8683feca744ec21671fdecb28838e1da 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-9.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=721f6644f78497b0cb094a25bf42e45c 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-9.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=d15e1062f506f6a6e2c149cf3cd6742b 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-9.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=c1c1676721633844f5bd8c65cec7bef4 2500w" />
</Frame>

**Additional On-start Script Examples**

You can execute custom startup scripts:

```text  theme={null}
chmod +x /usr/local/bin/start.sh
bash /usr/local/bin/start.sh
```

You can also overwrite existing files built into the image. Make sure you can switch to a user that has write permissions to that particular file.

For example, you can remove all instances of '-sslOnly' in a particular file using sed:

```text  theme={null}
sed -i 's/-sslOnly//g' /dockerstartup/vnc_startup.sh
```

You can also make directories:

```text  theme={null}
sudo -i -u kasm-user mkdir -p /home/kasm-user/Desktop
```

Make sure to append environment variables to /etc/environment file in your on-start section because this makes environment variables available to all users and processes and ensures they are persisted even if your instance/docker container is rebooted:

```text  theme={null}
env >> /etc/environment
```

Also make sure to find the image's ENTRYPOINT or CMD command and call that command at the end of the on-start section. We overwrite that command to set up jupyter/ssh server, etc. under the hood.

## Extra Filters

Use this area to place restrictions on the machines that should show up in the search page when the template is selected.

<Frame caption="Extra filters showing this template is configured for both AMD64 and ARM64 CPUs">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-10.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=d0b46d8718eeb1e6d03f1924c5592465" alt="Extra filters showing this template is configured for both AMD64 and ARM64 CPUs" data-og-width="936" width="936" data-og-height="142" height="142" data-path="images/console-templates-10.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-10.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=699da072b92ce3785faab1160c46ff77 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-10.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=14ca41c6b1b124d184bfa0e399d806de 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-10.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=d83cf565ea5ddbbc8a5b77cda3f6216d 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-10.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=b359635e7820d3288255405738ec54a0 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-10.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=587c7dc9d367a9aabdbe70bc3ba3b578 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-10.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f024b48bf616811eaea377b4c861c332 2500w" />
</Frame>

## Docker Repository Authentication

If you are using a private Docker image then you will need to add authentication credentials so the machine running the instance can download it.

<Frame caption="Docker Repository Authentication">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-11.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=845e9caffad7a7cf2063bc9c9a74195c" alt="Docker Repository Authentication" data-og-width="945" width="945" data-og-height="152" height="152" data-path="images/console-templates-11.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-11.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=64d8129734e54342c9f0ad8a468c241a 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-11.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=346890098f2918b036798ee6e72c7840 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-11.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=cc1ce3577f7e7ec29c24de6be5b619c4 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-11.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=687cc079e04e348b468c8cae13ab1de3 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-11.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=5a6d6173d6dd2f3f4b9e030394078335 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-11.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=da79a3dd042f2f457189e1df0aabd978 2500w" />
</Frame>

**Docker Registry Server Names**

You don't have to specify docker.io as the server name if your repository is Docker Hub. Docker automatically uses docker.io to pull the image if no other registry is specified.

You do have to specify your server name if your repository is something else. For example:

* GitHub Container Registry (GHCR) - Server Name: `ghcr.io`
* Google Container Registry (GCR) - Server Name: `gcr.io`

## Disk Space

By setting the disk space in the template, you can ensure that new instances created from the template will use this amount as a minimum.&#x20;

<img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-12.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f6f7548d2944bba92edbf92f2298f1bd" alt="" data-og-width="945" width="945" data-og-height="129" height="129" data-path="images/console-templates-12.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-12.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=9b34aca53de956809dd5a0d518d8c7c3 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-12.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=4652475e296b06f026ce32e83bcad1ce 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-12.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=9abe04c75ecaea4888db8c536a7a50d0 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-12.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=1cc8ce0653aff8aae31e6cfd566796a6 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-12.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=8066a88a611676bd9e9fe43a08371cbe 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-12.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=3e7924b2c6ee30d2ca612dcb2ed09f68 2500w" />

## Template Visibility

Any template marked as public will be available in the template search system, while private images will not.

Private templates can still be used by others if you have shared the template URL.

<img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-13.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=49f230e0326c8dc467e6f741cad9ee81" alt="" data-og-width="945" width="945" data-og-height="65" height="65" data-path="images/console-templates-13.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-13.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=fa00d78c75d0bbd7ea1a3ead9dd8efaa 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-13.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=940356d95de0eae158a6d0506237a8b8 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-13.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=70bd0db750ee864a41c18c66c8947faa 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-13.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=0db3b59b6ef6b176065a3ea34136a3dd 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-13.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=081d8018edfae000027fa86a16aa4db4 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-13.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=bf5bde58b6f4e81cacbb30b86b2086a6 2500w" />

<Danger>
  Never save a template as public if it contains sensitive information or secrets. Use the account level environment variables as an alternative.
</Danger>

## CLI Command

Templates can be translated directly into CLI launch commands. This read-only area shows what you would need to type or copy to the CLI if you wanted to programatically launch an instance this way.

<Frame caption="Launch a template via the CLI">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-14.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ef36a018bb9f508d2d836c6a7cea71ca" alt="Launch a template via the CLI" data-og-width="945" width="945" data-og-height="183" height="183" data-path="images/console-templates-14.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-14.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=652af28974ad4b6ecd574e879a9d3022 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-14.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ff9256f8febdf503423e494aeb464291 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-14.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ca8783c389899765a89aa2528cf5bde8 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-14.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=6bf1ccd1747886b4b46719915db0c1d7 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-14.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=d33bd5a11900d30c08804f3c6a7642ee 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-14.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=651187a027e28f9ce019584ae5e7012a 2500w" />
</Frame>

To learn more about starting instance from the CLI, check out our [quickstart guide](/cli/get-started).

## Save the Template

Finally, you can save the template. If you are creating a new template or editing one which is not associated with your account - Such as one of our recommended templates - The buttons you see will be labelled 'Create'. For your own templates, you will see them labelled 'Save'

<Frame caption="Buttons for saving">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=204e5427f10491896bdfd3da4001ef7e" alt="Buttons for saving" data-og-width="800" width="800" data-og-height="139" height="139" data-path="images/console-templates-15.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=882f55ab8e980cee4c909756332105d2 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=3c762e2f60ae6b0e493a7fb390f8f684 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ffa93edd1d40351184f2741d546fe37c 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e7455ee727b36380074c4f246719f09b 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=4a4996d972ab492832c1443938572b2e 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-15.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ff72dd2126f7020597b1e9c21c0c14aa 2500w" />
</Frame>

The 'Create' button will create a copy of the template in the 'My Templates' section of the [templates page](https://cloud.vast.ai/templates/) for you to use later. The 'Create & Use' button will save the template, load it and then open up the [offers page](https://cloud.vast.ai/create/).
