# Source: https://docs.vast.ai/documentation/templates/managing-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Templates

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Manage Vast.ai Templates",
  "description": "A guide to updating, sharing, and troubleshooting Vast.ai templates including referral links and template versioning.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Update a Template",
      "text": "Navigate to the templates page and select 'My Templates'. Make your changes by clicking the pencil icon on the template you want to update."
    },
    {
      "@type": "HowToStep",
      "name": "Share a Template",
      "text": "Click the three dots icon in the bottom right of the template card. Choose 'Copy referral link' (always points to the most recent template version with this name) or 'Copy template link' (points to this specific template version at this point in time). Both links include your referral code so you can earn if new users sign up."
    },
    {
      "@type": "HowToStep",
      "name": "Troubleshoot Common Issues",
      "text": "If your image is built for a different CPU architecture, find a machine with the required architecture. If your image requires a higher CUDA version, look for a machine with higher Max CUDA version. If your image runs jupyter, try running it on a port different than 8080. For SSH launch mode issues, add your public key to ~/.authorized_keys, install openssh, start it when the container starts, and forward the ssh server's port."
    }
  ]
})
}}
/>

## Updating a Template

If you want to make changes to a template you previously saved, simply navigate back to the templates page and select 'My Templates'.  Here you'll be able to make your changes by clicking the pencil icon.

<Frame caption="My templates showing the NVIDIA CUDA - Demo template">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-16.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=a10dba2b81b04511da306adab3943250" alt="My templates showing the NVIDIA CUDA - Demo template" data-og-width="800" width="800" data-og-height="659" height="659" data-path="images/console-templates-16.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-16.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=222383226ae20e83d098a1df2d1ada01 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-16.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=0361a4ee0436222b62187bd061171605 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-16.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=4d95e9b2ffd691f9ab7e9b86af2bb860 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-16.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e4107173a768513602929f1685049943 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-16.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=82a6b71266be86d417804846e8b7e583 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-16.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=9dd219092a382e9a9816e0ae2602c6cc 2500w" />
</Frame>

## Sharing a Template

It's really easy to share your template with other users.  We have two special links you can use and both include your referral code so you can earn if new users sign up - Find more about that [here](/documentation/reference/referral-program).

To share, click the three dots icon in the bottom right of the template card.

<Frame caption="Menu shows sharing options">
    <img src="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-17.webp?fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f02daabbababb169c43dd8cd9512d0ba" alt="Menu shows sharing options" data-og-width="800" width="800" data-og-height="341" height="341" data-path="images/console-templates-17.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-17.webp?w=280&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=f06b8d4b2943fdb72f1574ec90409709 280w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-17.webp?w=560&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=ccd4a53a9f4bc4dfd7c8da469cd92ff4 560w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-17.webp?w=840&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=00cc544a7828c59653c8f71d2c56c273 840w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-17.webp?w=1100&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=e81cf9a3b618c1ffdccfe27cd9a84891 1100w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-17.webp?w=1650&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=62beb1b7ab3c97f6d42f702394832d2d 1650w, https://mintcdn.com/vastai-80aa3a82/v_EM_-NdbnPjb9tX/images/console-templates-17.webp?w=2500&fit=max&auto=format&n=v_EM_-NdbnPjb9tX&q=85&s=6842a0ecb290e1cf11c3ad6003eef60f 2500w" />
</Frame>

### Copy referral link

This will copy a link that contains your referral ID, creator ID and the template name.  It will always point to the most recent template you created with this name - Really useful if you want people clicking the link to always get the most recent version.

### Copy template link&#x20;

This will copy a link containing your referral ID and the template hash ID.  It points to this specific template at this point in time. &#x20;

Templates all have a unique hash after every save.  This is useful as it allows you to find a previous version if you have tracked the hash ID, but for sharing you probably want the referral link above.

<Note>
  Remember to add a comprehensive Readme to your template if you're going to share it.  This will help users to get started easily.
</Note>

## Troubleshooting

* If your image is built for a different CPU architecture than your Vast machine, then it won't work. You can try to find a machine with the required CPU architecture using our GUI or [CLI](/cli/get-started).
* If your image requires a higher CUDA version, then look for a machine with a higher Max CUDA version. The Max CUDA version can be found on the instance card.&#x20;
* If your image is built to run jupyter, then try running it on a port different than 8080.
* If you are having issues using ssh launch mode, add your public key to \~/.authorized\_keys, install openssh, start openssh when the container starts, and forward the ssh server's port.
