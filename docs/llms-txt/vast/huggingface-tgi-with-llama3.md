# Source: https://docs.vast.ai/huggingface-tgi-with-llama3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Huggingface TGI with LLama3

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Setup Huggingface TGI with Llama3 on Vast.ai",
  "description": "A step-by-step guide to setting up and exposing an API for Llama3 Text Generation using Huggingface TGI on Vast.ai's GPU instances.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Choose the Huggingface Llama3 TGI API Template",
      "text": "Login to your Vast account on the console and select the HuggingFace Llama3 TGI API template. This template uses the meta-llama/Meta-Llama-3-8B-Instruct model and TGI 2.0.4 from Huggingface. The template comes with filters for minimum requirements including 100GB disk space and at least 16GB GPU RAM."
    },
    {
      "@type": "HowToStep",
      "name": "Modify the Template",
      "text": "Add your Huggingface access token in the Docker run options. You will need to apply to have access to Llama3 on Huggingface to access this gated repository. Add your token with the rest of the docker run options, then press 'Select & Save' to get ready to launch your instance."
    },
    {
      "@type": "HowToStep",
      "name": "Rent a GPU",
      "text": "Choose to rent a GPU from either the search page or the CLI/API. For someone just getting started, an Nvidia RTX 4090 or A5000 is recommended. Click RENT to launch your instance."
    },
    {
      "@type": "HowToStep",
      "name": "Monitor Your Instance",
      "text": "Once you rent a GPU, your instance will begin spinning up on the Instances page. The API will be ready when your instance status shows as running. Go to the IP & Port Config by pressing the blue button on top of the instance card to see the networking configuration."
    },
    {
      "@type": "HowToStep",
      "name": "Access the API",
      "text": "After opening the IP & Port Config, find the forwarded port from 5001 where your API resides. To hit TGI, use the '/generate' endpoint on that port. You now have a running instance with an API using TGI loaded with Llama3 8B!"
    }
  ]
})
}}
/>

This is a guide on how to setup and expose an API for Llama3 Text Generation.

>

## 1) Choose The Huggingface LLama3 TGI API Template From the Recommended Section

Login to your Vast account on the [console](https://cloud.vast.ai)

Select the [HuggingFace Llama3 TGI API](https://cloud.vast.ai/?template_id=906891f677fb36f21662a92e6092b5fc) template by clicking the link provider

For this template we will be using the meta-llama/Meta-Llama-3-8B-Instruct model, and the TGI 2.0.4 from Huggingface

Templates encapsulate all the information required to run an application with the autoscaler, including machine parameters, docker image, and environment variables.

For this template, the only requirement is that you have your own Huggingface access token. You will also need to apply to have access to Llama3 on huggingface in order to access this gated repository.

The template comes with some filters that are minimum requirements for TGI to run effectively. This includes but is not limited to a disk space requirement of 100GB, and a gpu ram requirement of at least 16GB.

After selecting the template your screen should look like this:

<Frame caption="Select">
    <img src="https://mintcdn.com/vastai-80aa3a82/MV3o3hbz7ZsjLzLy/images/Select.png?fit=max&auto=format&n=MV3o3hbz7ZsjLzLy&q=85&s=02e8297d55467706c3411dcb8a9fa6bf" alt="Select" data-og-width="1082" width="1082" data-og-height="465" height="465" data-path="images/Select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/MV3o3hbz7ZsjLzLy/images/Select.png?w=280&fit=max&auto=format&n=MV3o3hbz7ZsjLzLy&q=85&s=8fff2658ba8f39ea17b1244a3e74e88f 280w, https://mintcdn.com/vastai-80aa3a82/MV3o3hbz7ZsjLzLy/images/Select.png?w=560&fit=max&auto=format&n=MV3o3hbz7ZsjLzLy&q=85&s=8fb7d9f1ddde6e1be705793093308c26 560w, https://mintcdn.com/vastai-80aa3a82/MV3o3hbz7ZsjLzLy/images/Select.png?w=840&fit=max&auto=format&n=MV3o3hbz7ZsjLzLy&q=85&s=60bc97e88501c1fd1a8ee3de9a455517 840w, https://mintcdn.com/vastai-80aa3a82/MV3o3hbz7ZsjLzLy/images/Select.png?w=1100&fit=max&auto=format&n=MV3o3hbz7ZsjLzLy&q=85&s=3baf5713662c147ee48d9e7cf85d16fe 1100w, https://mintcdn.com/vastai-80aa3a82/MV3o3hbz7ZsjLzLy/images/Select.png?w=1650&fit=max&auto=format&n=MV3o3hbz7ZsjLzLy&q=85&s=7a6e17fad2f5bab89d29bd4fb4cd9248 1650w, https://mintcdn.com/vastai-80aa3a82/MV3o3hbz7ZsjLzLy/images/Select.png?w=2500&fit=max&auto=format&n=MV3o3hbz7ZsjLzLy&q=85&s=4928a1b1b5bc5569ac5575d94cbd7085 2500w" />
</Frame>

## 2) Modifying the Template

>

Once you have selected the template, you will need to then add in your huggingface token and click the 'Select & Save' button.

You can add your huggingface token with the rest of the docker run options.

<Frame caption="Edithf">
  ![Edithf](https://vast.ai/uploads/HuggingFace/EditHf.png)
</Frame>

This is the only modification you will need to make on this template.

You can then press 'Select & Save' to get ready to launch your instance.

## 3) Rent a GPU

Once you have selected the template, you can then choose to rent a GPU of your choice from either the search page or the CLI/API.

For someone just getting started I recommend either an Nvidia RTX 4090, or an A5000.

<Frame caption="Rent">
  ![Rent](https://vast.ai/uploads/HuggingFace/Rent.png)
</Frame>

## 4) Monitor Your Instance

Once you rent a GPU your instance will being spinning up on the Instances page.

You know the API will be ready when your instance looks like this:

<Frame caption="Llama3Tgiinstances">
  ![Llama3Tgiinstances](https://vast.ai/uploads/llama3tgiinstances.png)
</Frame>

Once your instance is ready you will need to find where your API is exposed. Go to the IP & Config by pressing the blue button on the top of the instance card. You can see the networking configuration here.

<Frame caption="Llama3Ip">
  ![Llama3Ip](https://vast.ai/uploads/llama3ip.png)
</Frame>

After opening the IP & Port Config you should see a forwarded port from 5001, this is where your API resides. To hit TGI you can use the '/generate' endpoint on that port.

Here is an example:

<Frame caption="Llama3Tgipostman">
  ![Llama3Tgipostman](https://vast.ai/uploads/llama3tgipostman.png)
</Frame>

## 5) Congratulations!

You now have a running instance with an API that is using TGI loaded up with Llama3 8B!

# Serverless/Autoscaler Guide

As you use TGI you may want to scale up to higher loads. We currently offer a serverless version of the Huggingface
TGI via a template built to run with the Autoscaler. See [Getting Started with Autoscaler](/documentation/serverless/getting-started-with-serverless)
