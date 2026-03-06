# Source: https://docs.vast.ai/documentation/templates/examples/grobid.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Templates for GROBID

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Create a Vast.ai Template for GROBID",
  "description": "A complete walkthrough of creating a Vast.ai template using an existing Docker image, demonstrated with GROBID as an example application.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Find a Suitable Docker Image",
      "text": "Search for the official GROBID image on DockerHub. There are multiple GROBID images available, but use the official one from grobid/grobid for this guide."
    },
    {
      "@type": "HowToStep",
      "name": "Select the Version Tag",
      "text": "Choose a version tag from the Tags tab. We recommend selecting the latest stable version. At the time of writing, the current stable version is 0.8.0."
    },
    {
      "@type": "HowToStep",
      "name": "Set Image and Tag in Template",
      "text": "In the Docker Repository And Environment section of the Vast.ai template editor, enter your image path and tag (e.g., grobid/grobid:0.8.0)."
    },
    {
      "@type": "HowToStep",
      "name": "Map Ports",
      "text": "According to the GROBID containerization guide, port 8070 needs to be exposed. Add -p 8070:8070 in the Ports section to map the container's port 8070 to the host machine's port 8070."
    },
    {
      "@type": "HowToStep",
      "name": "Select Launch Mode",
      "text": "Select the SSH launch mode for this template to enable command-line access to the instance."
    },
    {
      "@type": "HowToStep",
      "name": "Configure On-start Script",
      "text": "Find the CMD or ENTRYPOINT command in the image's DockerHub page under the Tags tab. Add this command to the On-start Script section. Also append environment variables to /etc/environment file to make them available to all users and processes."
    },
    {
      "@type": "HowToStep",
      "name": "Name and Save Template",
      "text": "Specify the template name and description, then click 'Create & Use' to save the template and navigate to the GPU offers search page."
    },
    {
      "@type": "HowToStep",
      "name": "Rent Instance and Access GROBID",
      "text": "Select an instance offer and rent it. Once the instance is ready (blue 'CONNECT' button appears), click the IP range button to see the IP and port information. Copy the machine IP and port to load the GROBID web app in your browser."
    }
  ]
})
}}
/>

## Introduction

This guide demonstrates creating a template using an existing Docker image. See our [Creating Templates](/documentation/templates/creating-templates) guide for more details on template configuration. We will be using the image from [GROBID on dockerhub](https://hub.docker.com/r/grobid/grobid).

## Find The Image and Tag You Want to Use

### Step 1 - Find a Suitable Image

There are multiple GROBID images in dockerhub, but for this guide we will be using the official GROBID image.

<Frame caption="Grobid Overview">
  ![Grobid Overview](https://vast.ai/uploads/grobid_overview.png)
</Frame>

### Step 2 - Selecting the Version Tag

If you don't already have a version you intend to use, we recommend selecting the latest stable version.&#x20;

<Frame caption="Stable Tag">
  ![Stable Tag](https://vast.ai/uploads/stable_tag.png)
</Frame>

At the time of writing, the current stable version is 0.8.0, so that is the version we'll be using here.

## Configuring The Template

### Step 1 - Setting Your Chosen Image and Tag in Your Vast.ai Template

In the Docker Repository And Environment section, you will enter your image path and tag.

<Frame caption="Imageandtag">
  ![Imageandtag](https://vast.ai/uploads/templates/ImageAndTag.png)
</Frame>

### Step 2 - Map Ports and Specify Your Image and Tag Combination

The overview page for this image at dockerhub has a link to their guide to [using GROBID with containers](https://grobid.readthedocs.io/en/latest/Grobid-docker/#crf-and-deep-learning-image), which you can read to get their recommendations for containerizing GROBID.&#x20;

As we follow their guide to containerizing GROBID, we'll need to make sure the container's port 8070 is set to the host machine's port 8070. We will do that in the Vast.ai template. We use -p 8070:8070 as one of the docker run options.

<Frame caption="Run Cmd">
  ![Run Cmd](https://vast.ai/uploads/run_cmd.png)
</Frame>

**Note:** Vast only allows -e and -p docker run options to set environment variables and expose ports.

<Frame caption="Grobidport">
  ![Grobidport](https://vast.ai/uploads/templates/GrobidPort.png)
</Frame>

### Step 3 - Select the Launch Mode

Here we will select the SSH launch mode.

<Frame caption="Sshdirect">
  ![Sshdirect](https://vast.ai/uploads/templates/SSHDirect.png)
</Frame>

### Step 4 - Look for CMD or ENTRYPOINT command

<Frame caption="Found Tag">
  ![Found Tag](https://vast.ai/uploads/found_tag.png)
</Frame>

To find this for the template we are creating, we searched the [image's page in Dockerhub](https://hub.docker.com/r/grobid/grobid) and found the **CMD&#x20;**&#x63;ommand in the **Tags** tab under the link "0.8.0" highlighted in blue.

<Frame caption="Found Cmd">
  ![Found Cmd](https://vast.ai/uploads/found_cmd.png)
</Frame>

### Step 5 - Fill Out On-start Script section using the CMD command we just found

Next, we add the contents of the **CMD&#x20;**&#x63;ommand to the end of the bash commands section of the **On-start Script** fields.

Also, appended environment variables to /etc/environment file in our on-start section.

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=8c2a472c7f7376a29c6d74c4de94b596" alt="" data-og-width="930" width="930" data-og-height="159" height="159" data-path="images/console-creating-templates-for-grobid.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=cff8871bf43d6037d8b199b8366856e0 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=762242ea430ae696ad25bb306a20bdc9 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=52b54159811795e225bdce83ebfc743b 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=2dc4735f92ec08de5b5122629f62708f 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=476a28e41f5991eb05f8f0e6247f19a4 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=fd94da7e9b2cffe77f8305049336a678 2500w" />

This makes environment variables available to all users and processes and ensures they are persistent even if our instance/docker container is rebooted. We suggest doing the same for your templates.

### Step 6 - Name and Save The Template

<Frame caption="Grobidexample">
  ![Grobidexample](https://vast.ai/uploads/templates/GrobidExample.png)
</Frame>

When you are finished setting up your template, If you haven't already done so, specify the template name and description.

Finally, click **Create & Use** to save the template and navigate to the GPU offers search page. You'll notice that your template is selected and ready to be used.

## Rent an Instance Using Your Template and Open GROBID Web App

Once you have selected an instance offer, You'll click on the **INSTANCES&#x20;**&#x6C;ink in the left menu and see your rented GPU instance that has your template applied.&#x20;

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-2.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=4feb5053b253885ec8fe5dd7d54fb45e" alt="" data-og-width="910" width="910" data-og-height="151" height="151" data-path="images/console-creating-templates-for-grobid-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-2.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=d6a30c67d4dde7cc9ec565328326eb9b 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-2.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=e43967c9192155b3de9cae49f0c4c0d4 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-2.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=ac99d03ba0bef9130828304bb32e7b52 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-2.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=94315a14cea4bb91455e57360032cf9f 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-2.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=efc81f6ecf46433edbcd42e8ae5a7038 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-2.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=85676741fcd321a599c13994b7f4f738 2500w" />

When the instance is done loading and the **>\_CONNECT** state on the blue button appears, you should be able to see the ip range button at the top of the instance card.

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-3.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=a359678ad0010345f644c553508d3f4f" alt="" data-og-width="800" width="800" data-og-height="120" height="120" data-path="images/console-creating-templates-for-grobid-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-3.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=0f4f5a023fb8659737bf46b75bca7922 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-3.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=6eb95f5fae681267f67947cb4b9da74a 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-3.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=ef5ea1d7387b1151e2921ab9c3f1ee44 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-3.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7ca3f0619a9edde2b828e5b6f2feb952 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-3.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=46945c997766649d2df89ee3749002f3 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-3.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=9cdce10373032e842de495ac36d6790e 2500w" />

If you click the IP range button you will see a new modal has the IP and port information for your instance. You'll see the port 8070 that we set listed in Open Ports.

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobi-4.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=645a9347c850c1862a99840c968d568a" alt="" data-og-width="800" width="800" data-og-height="1077" height="1077" data-path="images/console-creating-templates-for-grobi-4.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobi-4.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=488e196c046de27f903555a4d6ad4a6e 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobi-4.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=c390d783fa0005846d4173c03a47a24c 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobi-4.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=6bc8a3a03ff38cf7fbbffcfc2f64184d 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobi-4.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=ea4fe4bece127d0986b853b1e2b2fbc1 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobi-4.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=6de2ac44d9741fd0d3fdea0397e11023 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobi-4.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=0e217fa7822ffb4393497255cc03b3f2 2500w" />

You can copy the machine IP and port and load the address (in this example: 195.0.159.206:55734) in a new browser tab or window. This address will load the GROBID web app.

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-5.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=39196202780eece3d7c8f0d05bac6021" alt="" data-og-width="1114" width="1114" data-og-height="369" height="369" data-path="images/console-creating-templates-for-grobid-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-5.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=eba776a128f33c8c7a18e571c8834f79 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-5.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=b4749dddb805f12de4c2ead496fb2f32 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-5.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=456544e32817c6dc94f21185bc9a845e 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-5.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=24fc1eff388fca3b6a5bd8996abdefd2 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-5.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=783db8b7d9eefd941f095aef4361ae99 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-creating-templates-for-grobid-5.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=b4874a1ca4bc8bb090323d6ea37a493a 2500w" />

## Additional Resources

[GROBID Documentation](https://grobid.readthedocs.io/en/latest/)
