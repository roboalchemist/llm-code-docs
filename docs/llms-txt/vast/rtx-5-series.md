# Source: https://docs.vast.ai/rtx-5-series.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# RTX 5 Series

> Optimize your GPU experience with our comprehensive guide on RTX 5 Series GPUs (5090/5080/5070) and CUDA 12.8 compatibility. Learn how to rent an RTX 5090 on Vast.ai, select the right templates, and customize your storage while ensuring optimal performance.

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Rent RTX 5 Series GPUs on Vast.ai",
  "description": "A guide to renting and configuring RTX 5 Series GPUs (5090/5080/5070/5060) on Vast.ai with proper CUDA 12.8 compatibility and template selection.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Create or Log in to Vast.ai Account",
      "text": "Go to cloud.vast.ai and either create a new account or log in to your existing account."
    },
    {
      "@type": "HowToStep",
      "name": "Select Compatible Template with Automatic Tag",
      "text": "Select a Recommended template with '[Automatic]' set as the Version Tag (this is the default option). To verify, click the pencil icon on the template card to open the template editor and view the image tag. Templates with [Automatic] tag will pull the most recent supported docker image with CUDA 12.8 and PyTorch 2.7+ for Blackwell GPU compatibility."
    },
    {
      "@type": "HowToStep",
      "name": "Select the 5 Series GPU from Search Filters",
      "text": "In the GPU drop down menu, select the specific 5 series card you want to rent (5090/5080/5070/5060) or select the whole RTX 5 series category. Only templates compatible with Blackwell GPUs will show these GPUs in the offer listing."
    },
    {
      "@type": "HowToStep",
      "name": "Review and Customize Instance",
      "text": "Set your storage and further refine your search filters (e.g., secure cloud, location, system RAM, CPU, etc.). Do NOT change the Docker image as you need to maintain CUDA 12.8 compatibility. If you switch to an incompatible Docker image, you may lose 5 series compatibility."
    },
    {
      "@type": "HowToStep",
      "name": "Select and Rent",
      "text": "Click 'Rent' next to your preferred server. You can now launch Jupyter notebooks, SSH into the instance, or start your own training jobs using the pre-installed CUDA 12.8 / PyTorch environment."
    }
  ]
})
}}
/>

## Renting RTX 5 Series GPUs (5090/5080/5070/5060)

Many of our recommended templates now support Blackwell series Nvidia GPU's including the RTX 5 series.

Blackwell GPUs do not have the same backwards compatibility as seen in some previous generation Nvidia GPU's so it is important that the template and Docker image has been configured to use CUDA 12.8 and PyTorch 2.7 or greater.

Any template that is known to be compatible with this GPU type will automatically show these GPUs in the offer listing.  Those without support will exclude the unsupported cards when searching for an instance.

Templates configured with the `[Automatic]` tag will pull the most recent & supported docker image.  This enables wider support across the range of GPUs you can find at Vast.ai

## Steps to Rent an RTX 5000 Series GPU on Vast.ai

1. **Create / Log in to your Vast.ai account**
   Go to [cloud.vast.ai](https://cloud.vast.ai) and either create a new account or log in.

2. **Select a Recommended template with "\[Automatic]" set as the Version Tag (this is the default option).**
   To check this, click the 'pencil' icon on the template card to open the template editor, you can view the image tag.

   <img src="https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series.webp?fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=cda9408340cbd1c2efc8fca4adaf3a79" alt="" data-og-width="961" width="961" data-og-height="130" height="130" data-path="images/rtx-5-series.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series.webp?w=280&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=0373b04288659f89c21784bf798358bc 280w, https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series.webp?w=560&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=40334f5e1a2f6601309bf0569ce0bf45 560w, https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series.webp?w=840&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=b0d5a2f32526834bec271e510b7fc0ff 840w, https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series.webp?w=1100&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=7be02362eea4c7f6fef048fcc13169cc 1100w, https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series.webp?w=1650&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=7f5dc706c3f36c8dd497f8bb331f5b88 1650w, https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series.webp?w=2500&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=eb0993a314ffef4d1695c569db61425b 2500w" />

3. **Select the 5 series GPU from search filters**
   In the GPU drop down menu select the specific 5 series card you want to rent or select the whole category.

   <img src="https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series-2.webp?fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=9c9a4241a9756afd99a9606b59aed118" alt="" data-og-width="800" width="800" data-og-height="552" height="552" data-path="images/rtx-5-series-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series-2.webp?w=280&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=7c11ee8475015ffe46cd9cc4ce53c05f 280w, https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series-2.webp?w=560&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=5d5fd2ad6b0aec6899f88f674762ac03 560w, https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series-2.webp?w=840&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=2accb02127b7e747ca8568350b1f6704 840w, https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series-2.webp?w=1100&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=50fb3122f6581767ab44bc98e53a8632 1100w, https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series-2.webp?w=1650&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=64d8ceb9c18bc58ef7b9b4bee0ef2ce7 1650w, https://mintcdn.com/vastai-80aa3a82/cNHQLqV42N4xE1uT/images/rtx-5-series-2.webp?w=2500&fit=max&auto=format&n=cNHQLqV42N4xE1uT&q=85&s=55ea8365034ac5cb31ec0a2d4da51a21 2500w" />

4. **Review and customize**
   Set your storage and further refine your search filters (e.g., secure cloud, location, system RAM, CPU, etc.). ⚠️ Do **not** change the Docker image because you need to maintain CUDA 12.8 and the dev version of PyTorch. If you switch to an incompatible Docker image, you may lose 5 series compatibility.

5. **Select and rent**
   Click “Rent” next to your preferred server. You can now launch Jupyter notebooks, SSH into the instance, or start your own training jobs using the pre-installed CUDA 12.8 / PyTorch dev environment.

## Tips and Troubleshooting

* **Check CUDA version**: If you manually change the Docker image, ensure it’s compiled for CUDA 12.8 or else you may lose compatibility with these GPUs.
* **Stay up to date**: New PyTorch releases (especially nightlies / dev builds) often update their CUDA support. If you need a stable release, confirm that the Docker image tags match a stable version with CUDA 12.8.
* **Use custom Docker**: If you have your own Docker image, you must ensure it is built with CUDA 12.8 (and ideally tested on a GPU supporting that version).
