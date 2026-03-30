# Source: https://docs.vast.ai/documentation/reference/keys.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Keys

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Manage Keys on Vast.ai",
  "description": "A guide to managing SSH keys, API keys, and session keys for secure access to your Vast.ai account.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Add SSH Keys",
      "text": "Click on the +New button in the SSH Keys section. Copy and paste your SSH public key into the input to attach it to your account. You can use this SSH key to log into instances remotely. Once saved, it will appear in the SSH Keys section and will be automatically added to your future instances."
    },
    {
      "@type": "HowToStep",
      "name": "Create API Keys",
      "text": "Click on the +New button in the API Keys section. Select specific permissions and assign a name to the key (by default, all your account permissions are selected). You will need an API key to access the Command Line Interface and the REST API."
    },
    {
      "@type": "HowToStep",
      "name": "Manage Session Keys",
      "text": "Review your session keys regularly for security. Session keys are temporary keys that allow access to your Vast.ai account and are automatically created when you log in. They expire in one week. You can view a list of all active session keys and see which devices are currently logged into your account. If you notice any session keys that you don't recognize, you can delete those keys to immediately remove access."
    }
  ]
})
}}
/>

The Keys page helps you manage secure access to your Vast.ai account. Here, you'll find different types of keys used for authentication and connection.

## SSH Keys

You can add, edit, or remove your ssh keys in the SSH Keys section of the Keys page of your console.

<Frame caption="SSH Keys empty section">
    <img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-2.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=ee9da8cd0a06f76df7a0daefc8ec9316" alt="SSH Keys empty section" data-og-width="974" width="974" data-og-height="258" height="258" data-path="images/console-keys-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-2.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=bf684848f9f73ed0a7db5f2d3958ebb7 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-2.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=9c7f368a5cb42bbe9e48d30fb638c99c 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-2.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=855edc61eb35aa52e35e475328252b80 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-2.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=1bfee14fdb9cf891849f1b122d11b992 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-2.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=3d64607730ee2ea8016ef1ecde75eae7 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-2.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=b73a4ff63165c462b2778ccf30e52cd9 2500w" />
</Frame>

Add a new ssh key by clicking on the **+New** button. Copy and paste your key into the input in order for it to be attached to your account. You can use this ssh key to log into instances remotely. More [here](/documentation/instances/sshscp).

<Frame caption="Add SSH Key">
    <img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-3.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=af420ad5d113f1eec7569af0558df027" alt="Add SSH Key" data-og-width="800" width="800" data-og-height="390" height="390" data-path="images/console-keys-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-3.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=bc6601d2cddc37b0c325fd3ecd87a609 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-3.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=6c006ac1b29fc8194f6b9a1ada822703 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-3.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7c5a7ce0e687f2aa9b39583556df9a6a 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-3.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=f261952f70dff57a4ef80c95ee463c8a 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-3.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=8ae224cee9b3b375362363d01fabd512 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-3.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=c6b7564ff533bce4d111790c3f19fa84 2500w" />
</Frame>

Once the SSH key is saved, it will appear in the SSH Keys section and will be automatically added to your future instances.

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-4.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=3f60694c8a33950942497e4bf917f6de" alt="SSH Keys" data-og-width="942" width="942" data-og-height="311" height="311" data-path="images/console-keys-4.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-4.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=c4ba96932f91742e34b8ee08cce6d295 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-4.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=441bcf5fa3c7f8b6208e8a4f1ab1935c 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-4.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=b9fb209d91c8e1dae83e089df823e4dc 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-4.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=3f305ba035f12d21bbed35a34678cc29 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-4.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7dc94a68c41cd24c9d28de3657c8bb99 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-4.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=d687d291fc531bab1c7675b114c948a4 2500w" />

You can edit an existing ssh key by clicking on the **Edit** button and changing the text.

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-5.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=05a156d4a4b4dedc8110bc362a4bf9ed" alt="Edit SSH Key" data-og-width="800" width="800" data-og-height="359" height="359" data-path="images/console-keys-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-5.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=d8ecacf1d0992b9825f4e1d933b37109 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-5.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=688fb0f9ee44aad3efdddf788ad0ac68 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-5.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=30abdc3c419e9ad975e0e6cb4d2fa9fc 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-5.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=cc1574534a66e342b8fa5075984e668e 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-5.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=e31f789b6a3a425eb0e37b6dcc1d6871 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-5.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=dbcbfafd2781ccfa68e5a0a29dbed096 2500w" />

Delete an existing ssh key by selecting the **Delete** button.

These ssh keys will be used primarily when accessing an instance. You must switch out your ssh keys on this page if you wish to connect easily via multiple machines.

## API Keys

You can view, copy, edit, and update your API keys in the Keys section of the console. You will need an API key to access the Command Line Interface and the REST API.

To create an API key click on the **+New** button. It will trigger API key creation pop-up.

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-6.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7a99db976bdef97e9738ec401c0e5353" alt="API Keys" data-og-width="931" width="931" data-og-height="657" height="657" data-path="images/console-keys-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-6.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=393f76c6ad4c4ccc9661024eb391f6c4 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-6.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7f71547881a2befd02077c133fa056e2 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-6.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=3d3121eb8535f9943c1a6284ff3d43e7 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-6.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=38718dbbd99b8abdab0fb6d715098cda 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-6.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=eee000408c9e9b0b3defd60f7ea85d82 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-6.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=c25fc40ead5434703927770a268ad5e2 2500w" />

Here, you can select specific permissions and assign a name to the key (by default, all you account permissions are selected).

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-7.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=b5989d9aae21e3f0f0639b274e8659a7" alt="API Keys" data-og-width="903" width="903" data-og-height="121" height="121" data-path="images/console-keys-7.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-7.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=ef35ded18c9932007d89343f065bf20f 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-7.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=64d1706671a318b922057069939dfc71 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-7.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=34a6cb1a5bfd405a4a4a6b6517ce000b 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-7.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=277f8c41b2ba6c69f342e3b7ac171c10 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-7.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=0812e60ce14a452e928400aca9557038 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys-7.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=6bcb7f9eda116b2865eda596632c76fc 2500w" />

You can reset an API key by clicking the **Reset** button. A new key will be automatically generated. To remove a key, simply click the **Delete** button.

## Session Keys

A **session key** is a temporary key that allows access to your Vast.ai account. These keys are automatically created when you log in and will expire in one week.

However, for security reasons, it's important to review your session keys regularly. You can view a list of all active session keys and see which devices are currently logged into your account. If you notice any session keys that you don't recognize, or if a device is no longer in use, you can delete those keys to immediately remove access. This helps keep your account secure and ensures only your devices remain connected.

<img src="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys.webp?fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=bec511227a3c5e664b40fe6e897fda97" alt="Session Keys" data-og-width="1088" width="1088" data-og-height="543" height="543" data-path="images/console-keys.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys.webp?w=280&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=af2398621528faba860dc32e2f34cfed 280w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys.webp?w=560&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=e6b2dc98158e1e3eab8bb895383a6ab8 560w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys.webp?w=840&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=f1f3ec795d4ab749e9a3724046d2d368 840w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys.webp?w=1100&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=9b07500e6c75c3658e9c15b98aceb7b1 1100w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys.webp?w=1650&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=48f9e1741d65010495f2fdaca831b656 1650w, https://mintcdn.com/vastai-80aa3a82/xCLov_y0JNSp_qUD/images/console-keys.webp?w=2500&fit=max&auto=format&n=xCLov_y0JNSp_qUD&q=85&s=7e53c7f2d6c67e9fe9e578115c7daaf0 2500w" />
