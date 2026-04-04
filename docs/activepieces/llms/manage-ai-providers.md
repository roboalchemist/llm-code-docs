# Source: https://www.activepieces.com/docs/admin-console/manage-ai-providers.md

# Manage AI Providers

Set your AI providers so your users enjoy a seamless building experience with our universal AI pieces like [Text AI](https://www.activepieces.com/pieces/text-ai).

## Manage AI Providers

You can manage the AI providers that you want to use in your flows. To do this, go to the **AI** page in the **Admin Console**.

You can define the provider's base URL and the API key.

These settings will be used for all the projects for every request to the AI provider.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=80d92caf90c116589c7ecbc7f80a9514" alt="Manage AI Providers" data-og-width="1420" width="1420" data-og-height="800" height="800" data-path="resources/screenshots/configure-ai-provider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1d94288df818cc7c1d241d5681dcbcab 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=14038529f8d565a38edd58ac89c802d9 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=894ea0d5839737c4bfd66bdaffda5e80 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0176a920881ca1d8de1c71e1e9ba758f 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=20df3793ad011b2c71ab6c1b0f01a39b 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=18d3a1c09352aad3355efe6cee91745c 2500w" />

## Configure AI Credits Limits Per Project

You can configure the token limits per project. To do this, go to the project general settings and change the **AI Credits** field to the desired value.

<Note>
  This limit is per project and is an accumulation of all the reported usage by the AI piece in the project.
  Since only the AI piece goes through the Activepieces API,
  using any other piece like the standalone OpenAI, Anthropic or Perplexity pieces will not count towards or respect this limit.
</Note>

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=3a37db4f477f8fcf4c6a7749afedbdd0" alt="Manage AI Providers" data-og-width="1420" width="1420" data-og-height="800" height="800" data-path="resources/screenshots/ai-credits-limit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=1e4619f6a62a954d9e3edc1d83a3f351 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=9339b91b24aee4f662222ed815982bd4 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=91726634f998e19818cdcea4c83b8882 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f8299e5908cde2cf4f10c04d750b64ea 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=8f255a7d9bd82ebe13e3b200932a3810 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=c5b35d163e6e0487bf289a850a42df1b 2500w" />

### AI Credits Explained

AI credits are the number tasks that can be run by any of our universal AI pieces.

So if you have a flow run that contains 5 universal AI pieces steps, the AI credits consumed will be 5.
