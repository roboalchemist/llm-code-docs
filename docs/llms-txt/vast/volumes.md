# Source: https://docs.vast.ai/documentation/instances/storage/volumes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Volumes

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Create and Manage Volumes on Vast.ai",
  "description": "A comprehensive guide to creating and managing local volumes on Vast.ai including creating volumes via GUI or CLI, viewing pricing, deleting volumes, creating instances with existing volumes, and cloning volumes to different machines.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Create Volume via GUI",
      "text": "On the Search page, select a template and click 'Add volume' dropdown. Click the + button next to 'Local volume' to adjust volume size using the slider. Offers will display available volume size. Click Rent to launch the instance with the volume, which will be automatically mounted at /data directory."
    },
    {
      "@type": "HowToStep",
      "name": "Create Volume via Template Configuration",
      "text": "Open Template Editor and scroll to 'Disk Space (Container + Volume)' section. Check 'Add recommended volume settings', enter volume size and installation path. Click 'Save&Use' or 'Create&Use Template'. Adjust volume size in Search page and select a GPU to rent."
    },
    {
      "@type": "HowToStep",
      "name": "Create Volume via CLI",
      "text": "Search for volume offers with 'vastai search volumes'. Create a volume with 'vastai create volume <offer_id> -s <volume_size> -n <name>'. View volumes with 'vastai show volumes'. Mount to instance using '-v <volume_name>:<mount_point>' in the env argument when creating instance."
    },
    {
      "@type": "HowToStep",
      "name": "Delete Volume",
      "text": "Ensure the volume is not attached to any instance - delete the instance first if needed. Go to the Storage page, find the volume, click the three-dot menu, and select 'Delete volume'. Confirm deletion (this is permanent and cannot be undone)."
    },
    {
      "@type": "HowToStep",
      "name": "Use Existing Volume for New Instance",
      "text": "Go to the Storage page and select your volume. In the Volume Info section, click 'Rent instance using this volume'. You'll be redirected to the Search Page filtered for the same machine where the volume is located. Select an offer and the volume will be automatically attached to the new instance."
    }
  ]
})
}}
/>

The [**Storage**](https://cloud.vast.ai/storage/) page allows you to easily access and manage your **volumes -** storage that can be attached to your instances for data storage.

We currently provide **local volumes only**, meaning:

* A volume is physically tied to the machine it was created on.
* It can only be attached to instances running on the same physical machine.
* It cannot be moved or attached to instances on other machines.

<Note>
  Volume size cannot be changed after creation, so be sure to choose the size carefully based on your expected storage needs.&#x20;
</Note>

## Creating a Volume in GUI

This guide will walk you through the process of creating a volume using a template in the GUI. You can create the volume during instance creation by using a template with volume settings enabled, or you can create a volume by using dropdown menu on the Search page.&#x20;

### **How to create a volume via Add volume dropdown menu on the Search page?**

1. Select a template then click on **Add volume** dropdown. You will see an option labeled **Local volume** with a + (plus) button next to it.

   <img src="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes.webp?fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=d818347fcfa8ee7b670e80b32ac995fe" alt="" data-og-width="1280" width="1280" data-og-height="674" height="674" data-path="images/volumes.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes.webp?w=280&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=37bc7ec3b9a85e095d87028788076e8f 280w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes.webp?w=560&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=abb08fc0d1c2ad931cd93ed6b91cbbb0 560w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes.webp?w=840&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=9b6b0b523935cbd5461579e293c70f4b 840w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes.webp?w=1100&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=cf45e7b8f47987661e544c641b2deea0 1100w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes.webp?w=1650&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=1b8617e0d1a2626979c5061a6007fd27 1650w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes.webp?w=2500&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=cda1b8eaa8cfad3463ee56b9b1ff4107 2500w" />
2. Click + button. This will allow you to adjust the volume size using the slider. Once enabled, offes will display the available volume size.&#x20;

   <Frame caption="Create local volume">
       <img src="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-2.webp?fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=9bb72e7030922749446069dc9b84eab6" alt="Create local volume" data-og-width="1280" width="1280" data-og-height="712" height="712" data-path="images/volumes-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-2.webp?w=280&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=2634841a7f0b293cd855022106815cb0 280w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-2.webp?w=560&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=96cbae1718d37cb1c5d0fccf1aeb2fa1 560w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-2.webp?w=840&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=a5a6f8c05a4f1ea243ff95bd681a4111 840w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-2.webp?w=1100&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=e0cd4c44b94e30c0c6c006be139932e0 1100w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-2.webp?w=1650&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=7d7b05e56f17a3bb5066893cbfe5150b 1650w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-2.webp?w=2500&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=b7f469fe30e4566bb14508c2474c34b1 2500w" />
   </Frame>
3. Click **Rent&#x20;**&#x62;utton to launch your instance along with the volume. Once the instance is running, your volume will be automatically mounted and available inside the container at the /data directory.

   <Frame caption="Volume on instance">
       <img src="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-3.webp?fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=7b38d96b6f8e241b5415e530556ccad2" alt="Volume on instance" data-og-width="1018" width="1018" data-og-height="645" height="645" data-path="images/volumes-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-3.webp?w=280&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=6257a5e5b8a76b2d49cab81b0bb85516 280w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-3.webp?w=560&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=170f374bb64059724d0579eec28c315b 560w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-3.webp?w=840&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=161746e6605734ba2930d66b89e472c6 840w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-3.webp?w=1100&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=f058d8fa3acb2307d778c5245c64a60a 1100w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-3.webp?w=1650&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=e54c8e9ef1bf53b788d37e668246d4c7 1650w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-3.webp?w=2500&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=c8293aaa3a82f2817a8f41e57c05ed52 2500w" />
   </Frame>
4. You can find your volume information on **Storage&#x20;**&#x70;age.

   <Frame caption="Volume info">
       <img src="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-4.webp?fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=701c608adba8e5806f535276ed7a31d6" alt="Volume info" data-og-width="1280" width="1280" data-og-height="525" height="525" data-path="images/volumes-4.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-4.webp?w=280&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=c5c62a1739792c9d2e6e0b06d1e564bc 280w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-4.webp?w=560&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=b9ea7c821d212507a4e633d16501e42d 560w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-4.webp?w=840&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=5393c15275f319eb2db77f60addd1980 840w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-4.webp?w=1100&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=f3b7088e88382caee6d1519379732efb 1100w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-4.webp?w=1650&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=fa104f9c3d29cbead41bc583c1e1c5b5 1650w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-4.webp?w=2500&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=d8f958134d4d86f34ee516d8f290c1e5 2500w" />
   </Frame>

### **How to create a volume using a template?**

1. Choose  a Template. You can either choose an existing template from the [**Recommended**](https://cloud.vast.ai/templates/) list or create your own [custom template](/documentation/templates/creating-templates).
2. Open Template Editor (Click on pencil icon on a template card). Scroll down until you see the **Disk Space (Container + Volume)&#x20;**&#x73;ection.&#x20;

   <img src="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-5.webp?fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=a05044602cb747bb9cc9713e13c523e1" alt="Volume settings" data-og-width="800" width="800" data-og-height="657" height="657" data-path="images/volumes-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-5.webp?w=280&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=6004df77e76256e3aebdc8e9bd993db3 280w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-5.webp?w=560&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=116432e3c735acb6e9c703b4198ba988 560w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-5.webp?w=840&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=2fc16b3f7b305ab449a1eabeb9a99cd0 840w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-5.webp?w=1100&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=aaf3fdd5360eb9357eae7a47eb813396 1100w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-5.webp?w=1650&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=262d589b4e42a7e06f293034c19e5aa9 1650w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-5.webp?w=2500&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=0f2379c0ac6634b5d4b975528b3a8189 2500w" />
3. In this section, check the box **Add recommended volume settings**. Once selected, a new configuration area will appear where you can enter the **volume size&#x20;**&#x61;nd specify the **installation path.&#x20;**&#x41; default path is provided, but you can modify it if needed.&#x20;

   <Frame caption="Volume settings">
       <img src="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-6.webp?fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=d107bd4b36b023ddf52444b5bdcb5edd" alt="Volume settings" data-og-width="1049" width="1049" data-og-height="354" height="354" data-path="images/volumes-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-6.webp?w=280&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=d9b20538fd243a6eeb8f92cfbe4749f9 280w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-6.webp?w=560&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=764c4ab1f520483f366abe9548369567 560w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-6.webp?w=840&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=a357d4fa0d2ae8f59d20b5dacef25aa8 840w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-6.webp?w=1100&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=26f053aa120943b90ae5f2b9d2ed644a 1100w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-6.webp?w=1650&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=421d5c6eb13eb050bdc6ccb1d8ed34df 1650w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-6.webp?w=2500&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=9bbd902a1a58cfcb51cfb4a820dcad7a 2500w" />
   </Frame>
4. After filling in the volume details, click **Save\&Use&#x20;**&#x6F;r **Create\&Use Template&#x20;**&#x74;o apply your changes and navigate to the Search page. Offers that support volumes will now display a volume badge showing the available volume size. You can adjust the volume size using the slider in the Search page after your template is configured.

   <img src="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-7.webp?fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=c70715c2f8c2ad95a6b154ddcaaa286a" alt="Volume settings" data-og-width="1280" width="1280" data-og-height="676" height="676" data-path="images/volumes-7.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-7.webp?w=280&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=1d55b1da6336fbd36e0a9d031aec4f74 280w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-7.webp?w=560&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=e873689b57753427b0b8033e69660fd4 560w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-7.webp?w=840&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=36b54b78ab2be7fb9d2ac93727dbe8e8 840w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-7.webp?w=1100&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=60c8fc9a74cf76cece6d81e4b301e125 1100w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-7.webp?w=1650&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=1ddcffdec1e9637d5024dc76fc18949e 1650w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-7.webp?w=2500&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=a4064978ff8418bec6384f0d24628c34 2500w" />
5. Select a GPU and click **Rent&#x20;**&#x62;utton.

### **How to view volume pricing?**

To view pricing details, simply hover over the Rent button for any offer.&#x20;

<img src="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-8.webp?fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=f0d07bb5a6cd540184f7e2498eb287ac" alt="" data-og-width="800" width="800" data-og-height="375" height="375" data-path="images/volumes-8.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-8.webp?w=280&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=5b776105e9adc182a574127a956ce9be 280w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-8.webp?w=560&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=20cd05562e5cedaee43bb9d4a272c35c 560w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-8.webp?w=840&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=7f75fc09a7cf7dae04f372055e0c11bc 840w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-8.webp?w=1100&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=b4a5392d1394c7db761e5c9d620b9ceb 1100w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-8.webp?w=1650&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=1a2b80b5b936d23e79830b466c8626b2 1650w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-8.webp?w=2500&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=763a1353b89acfe4dd1c16a60989a2f2 2500w" />

### Deleting volume

To delete a volume, the instance it is attached to must be **deleted first**. Deleting a volume that is currently **mounted to a running or stopped instance is not allowed**.

Delete a Volume:

1. Make sure the volume is **not attached** to any instance.
   &#x20;If it is, **delete the instance** first from the Instances page.
2. Once the volume is detached, go to the **Storage** page.
3. Find the volume you want to delete, click on the **three-dot menu** (⋮) next to it, and select **"Delete volume"**.

   <Frame caption="Delete volume">
       <img src="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-9.webp?fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=cb0d822b0931c74b3f25b9ddddd960e4" alt="Delete volume" data-og-width="1280" width="1280" data-og-height="540" height="540" data-path="images/volumes-9.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-9.webp?w=280&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=924a7e65a42e58d918ae9f9129d2126b 280w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-9.webp?w=560&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=a788903a7c7ad4d46228fd927039886c 560w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-9.webp?w=840&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=170ae795c18cd934aff97dd8485b0585 840w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-9.webp?w=1100&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=9e222f9f6cd77a2d9933be2ea571811d 1100w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-9.webp?w=1650&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=4b41df08a96e9e2b51eaad176a3c7238 1650w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-9.webp?w=2500&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=170124f25598d02e93442f185753809c 2500w" />
   </Frame>
4. Confirm the deletion. This action is **permanent** and cannot be undone.

<Warning>
  Important: Deleting a volume will permanently remove all data stored in it. Make sure to back up any important data before proceeding.
</Warning>

### How to create an instance with existing volume?

If you already have a volume and want to launch a new instance using it, follow these steps:

1. Go to the **Storage** page and select the volume you want to use.

2. In the **Volume Info** section, you will see a button labeled **Rent instance using this volume**.

   <img src="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-10.webp?fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=8c4db1caeb318e91efe1850d0fdcacfc" alt="Rent instance using this volume" data-og-width="1280" width="1280" data-og-height="884" height="884" data-path="images/volumes-10.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-10.webp?w=280&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=ab654c1695400e43e38b41977f4ce40b 280w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-10.webp?w=560&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=ab9eb0a79d57f5da8a097bc265579e35 560w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-10.webp?w=840&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=f4c9d1deeb06f35fe2107d5a2680235f 840w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-10.webp?w=1100&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=5482e5891a57e783b772ae83145f2f99 1100w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-10.webp?w=1650&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=082666cb048688d73ed1379d6e4e7620 1650w, https://mintcdn.com/vastai-80aa3a82/1a9mKbP8zn3lYY0d/images/volumes-10.webp?w=2500&fit=max&auto=format&n=1a9mKbP8zn3lYY0d&q=85&s=6ca65ed70090abc4332bcf61bc6fff35 2500w" />

3. Click this button. You will be redirected to the **Search Page**, where available offers are automatically filtered to match the **same machine** where the volume is located.

4. Select your preferred offer and proceed to launch the instance.
   &#x20;The selected volume will be automatically attached to the instance upon creation.

## Creating a Volume in CLI

To create a volume, you can use the vast CLI. See our [CLI documentation](https://cloud.vast.ai/cli/) for set-up and usage of the CLI. You can search for volume offers using the command:

```text Text theme={null}
vastai search volumes
```

There is a modified list of search params available, for more information, you can add the -- help option to the search.&#x20;

This will bring up a list of available volume offers. You will be able to see the maximum capacity for the volume (in Gigabytes). Just like creating an instance, you can copy the offer ID and create a volume with the command:

```text Text theme={null}
  vastai create volume <offer_id> -s <volume_size> -n <name>
```

This will send a command to the host machine to allocate the given space to your volume. You can optionally specify a name with -n, it can be alphanumeric with underscores, with a max length of 64. If all goes well, you should be able to see your volume as created when you run the command&#x20;

```text Text theme={null}
vastai show volumes
```

### How can I  create an instance with a volume?

Now that your volume is created, you can use it by creating an instance on the machine with the volume, and passing the volume in the env argument. The format is -v \<volume\_name>:\<mount\_point>, for example:&#x20;

```text Text theme={null}
vastai create instance 874 --image pytorch/pytorch --env '-v V.881:/mnt' --disk 30 --ssh --direct
```

That command mounts your volume at the directory /mnt. The directory does not need to exist in order to be mounted.

### Can I use my volume on a different machine?

You can't directly use the same volume on a different machine, but you can clone the volume to a machine that has an available volume contract.The clone command will create a new volume contract on the new machine, provision the volume, and copy all existing data from the existing volume to the new volume. To clone a volume, you can use the command:

```text Text theme={null}
vastai clone volume <existing_volume_id> <dest_contract_id>
```

where \<dest\_contract\_id> is a volume offer of at least the size of your existing volume.&#x20;

The volumes are independent and do not sync data after the clone is completed. Any changes that occur (on either) volume AFTER the volume is successfully cloned will not be reflected on the other volume.

### How can I delete my volume?

When you're done using it, you can delete your volume using the command&#x20;

```text Text theme={null}
vastai delete volume <volume_id>
```

<Warning>
  This will only work if all instances using the volume have been destroyed.&#x20;
</Warning>

### How can I see what instances are using my volume?

The command

```text Text theme={null}
vastai show volumes
```

will display a list of volumes you own, as well as what instances exist that are using that volume.

## A machine with my volume went offline! Am I still being charged?

Just like with normal instances, you are never charged when a machine is offline. This is usually a temporary issue, and when the machine comes back online, volume charges will resume as normal. If you wish to delete the volume in the meantime, you can do so, and you will not be charged when the machine comes back online. If the machine is offline for an extended period of time, please reach out to vast support.&#x20;

## Can I use my volume with a VM instance?

At this time, volumes are only supported for docker instances, and cannot be used with VM instances.
