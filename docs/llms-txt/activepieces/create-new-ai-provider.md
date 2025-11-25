# Source: https://www.activepieces.com/docs/developers/misc/create-new-ai-provider.md

# Create New AI Provider

ActivePieces currently supports the following AI providers:

* OpenAI
* Anthropic

To create a new AI provider, you need to follow these steps:

## Implement the AI Interface

Create a new factory that returns an instance of the `AI` interface in the `packages/pieces/community/common/src/lib/ai/providers/your-ai-provider.ts` file.

```typescript  theme={null}
export const yourAiProvider = ({
  serverUrl,
  engineToken,
}: { serverUrl: string, engineToken: string }): AI<YourAiProviderSDK> => {
  const impl = new YourAiProviderSDK(serverUrl, engineToken);
  return {
    provider: "YOUR_AI_PROVIDER" as const,
    chat: {
      text: async (params) => {
        try {
          const response = await impl.chat.text(params);
          return response;
        } catch (e: any) {
          if (e?.error?.error) {
            throw e.error.error;
          }
          throw e;
        }
      }
    },
  };
};
```

## Register the AI Provider

Add the new AI provider to the `AiProviders` enum in `packages/pieces/community/common/src/lib/ai/providers/index.ts` file.

```diff  theme={null}
export const AiProviders = [
+  {
+    logoUrl: 'https://cdn.activepieces.com/pieces/openai.png',
+    defaultBaseUrl: 'https://api.your-ai-provider.com',
+    label: 'Your AI Provider' as const,
+    value: 'your-ai-provider' as const,
+    models: [
+      { label: 'model-1', value: 'model-1' },
+      { label: 'model-2', value: 'model-2' },
+      { label: 'model-3', value: 'model-3' },
+    ],
+    factory: yourAiProvider,
+  },
...
]
```

## Define Authentication Header

Now we need to tell ActivePieces how to authenticate to your AI provider. You can do this by adding an `auth` property to the `AiProvider` object.

The `auth` property is an object that defines the authentication mechanism for your AI provider. It consists of two properties: `name` and `mapper`. The `name` property specifies the name of the header that will be used to authenticate with your AI provider, and the `mapper` property defines a function that maps the value of the header to the format that your AI provider expects.

Here's an example of how to define the authentication header for a bearer token:

```diff  theme={null}
export const AiProviders = [
  {
    logoUrl: 'https://cdn.activepieces.com/pieces/openai.png',
    defaultBaseUrl: 'https://api.your-ai-provider.com',
    label: 'Your AI Provider' as const,
    value: 'your-ai-provider' as const,
    models: [
      { label: 'model-1', value: 'model-1' },
      { label: 'model-2', value: 'model-2' },
      { label: 'model-3', value: 'model-3' },
    ],
+    auth: authHeader({ bearer: true }), // or authHeader({ name: 'x-api-key', bearer: false })
    factory: yourAiProvider,
  },
...
]
```

## Test the AI Provider

To test the AI provider, you can use a **universal AI** piece in a flow. Follow these steps:

* Add the required headers from the admin console for the newly created AI provider. These headers will be used to authenticate the requests to the AI provider.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=80d92caf90c116589c7ecbc7f80a9514" alt="Configure AI Provider" data-og-width="1420" width="1420" data-og-height="800" height="800" data-path="resources/screenshots/configure-ai-provider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1d94288df818cc7c1d241d5681dcbcab 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=14038529f8d565a38edd58ac89c802d9 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=894ea0d5839737c4bfd66bdaffda5e80 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0176a920881ca1d8de1c71e1e9ba758f 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=20df3793ad011b2c71ab6c1b0f01a39b 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=18d3a1c09352aad3355efe6cee91745c 2500w" />

* Create a flow that uses our **universal AI** pieces. And select **"Your AI Provider"** as the AI provider in the **Ask AI** action settings.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=a8a84f27f69dd930bee70e90dd3cf04c" alt="Configure AI Provider" data-og-width="396" width="396" data-og-height="346" height="346" data-path="resources/screenshots/use-ai-provider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0d5aa117ae018abf79c21b20c272e1ba 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ba68de87edb99ea946286144dc0156c5 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=45b38c46cfb36795aa94617cdef23f82 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e261625b74c3ffff781bfa91f61257e5 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=754f91e9bfc7839e70ced50c821d960c 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=70c00d59a33ae118191072cdfbdd902d 2500w" />
