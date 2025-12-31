# Source: https://docs.helicone.ai/integrations/tools/xcode.md

# Xcode Integration (AI Gateway)

> Configure Xcode's Intelligence model provider to route through Helicone's AI Gateway for observability.

This guide shows how to add Helicone as a model provider in Xcode so your chats route through the Helicone AI Gateway and show up in your Helicone dashboard.

## Prerequisites

* A Helicone account and API key
* Org/provider keys configured in Helicone (so models can be listed)

## Steps

1. Open Xcode Settings

   * Xcode → Settings…

   <img src="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-settings.png?fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=aae1cd36d1e089a605787b9532a2f783" alt="Xcode Settings - Intelligence section" data-og-width="310" width="310" data-og-height="330" height="330" data-path="images/integrations/xcode/xcode-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-settings.png?w=280&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=4d437d155a86fd68aae0b41091b05f9d 280w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-settings.png?w=560&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=d2f17c80b3758505b21849a9597952e0 560w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-settings.png?w=840&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=746b50aea418290f8fe37542132a4b44 840w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-settings.png?w=1100&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=2be0b5143ed7791b9f61b026d699188d 1100w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-settings.png?w=1650&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=4dd47f1c785c70e22c8c6182d8c8c94e 1650w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-settings.png?w=2500&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=0dc2baa8a891008cec6928b34734046e 2500w" />

2. Add Helicone as a model provider

   * Select the Intelligence tab
   * Click "Add a model provider…"

   <img src="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-add-model.png?fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=e679d5cc098ecc0dcb3a148fdd02d75e" alt="Add model provider dialog in Xcode" data-og-width="726" width="726" data-og-height="466" height="466" data-path="images/integrations/xcode/xcode-add-model.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-add-model.png?w=280&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=9371f7154759d643e6527825270518fc 280w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-add-model.png?w=560&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=ce0997be508c5bd63ec25239f74dcb74 560w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-add-model.png?w=840&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=15091c32c3be04afdc8e32092c7cc00b 840w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-add-model.png?w=1100&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=aa8969ec7cac551cc9281521c3678958 1100w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-add-model.png?w=1650&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=ff63b6e4b8fff4e682108dabf8f8ba53 1650w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-add-model.png?w=2500&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=232bb6bf34ec230eccd20459797f425a 2500w" />

   * Fill the form with:
     * URL: `https://ai-gateway.helicone.ai`
     * API Key: `Bearer <helicone-api-key>`
     * API Key Header: `Authorization`
     * Description: `Helicone` (you can name this however you like)

   <img src="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-configure-helicone.png?fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=26b7f05c2acca39533cd87334828566e" alt="Add model provider dialog in Xcode" data-og-width="498" width="498" data-og-height="406" height="406" data-path="images/integrations/xcode/xcode-configure-helicone.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-configure-helicone.png?w=280&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=1cf23c5dcf4fdc10ce9f6dee98836c64 280w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-configure-helicone.png?w=560&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=f0451212360cda601485b590ba78b6c6 560w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-configure-helicone.png?w=840&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=21ca9f2aee6ddbb30d3f3a79bd784295 840w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-configure-helicone.png?w=1100&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=7fd7c572cf6463cf305b8dce6bcaf097 1100w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-configure-helicone.png?w=1650&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=35934a56b65cee26a2f9657f47598b57 1650w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-configure-helicone.png?w=2500&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=13c5871f100d39210320c123cc9a2fa6 2500w" />

3. Confirm models are available

   * After saving, Xcode should list available models from Helicone
   * There are many models; use Favorites to pin the ones you use most

   <img src="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-models-list.png?fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=d506848e7f041d0f1519b08e30028450" alt="Models list in Xcode with favorites" data-og-width="696" width="696" data-og-height="447" height="447" data-path="images/integrations/xcode/xcode-models-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-models-list.png?w=280&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=5847d509f13c29c1fb4fbcde5396c88c 280w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-models-list.png?w=560&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=ecb04f725fbfb82bc4ea4b5b6bd8061c 560w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-models-list.png?w=840&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=a2bf56d9a34dbbdf41ddff8e3b8f7148 840w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-models-list.png?w=1100&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=d524f901185dc0729cbd8cf448652cc6 1100w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-models-list.png?w=1650&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=6f75d57bfdf1d6cd3b54d7be856cac79 1650w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-models-list.png?w=2500&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=d1cb8b17bde3582107c0e9aeea242174 2500w" />

4. Start chatting and view logs in Helicone

   * Use the chat in Xcode with your selected model
   * Open the Helicone dashboard to see your requests, tokens, and costs

   <img src="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat.png?fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=01ec946b832a499d0810c12bac3d71c7" alt="Chatting in Xcode and viewing requests in Helicone" data-og-width="929" width="929" data-og-height="739" height="739" data-path="images/integrations/xcode/xcode-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat.png?w=280&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=5c76bc31496cb7cb6f696df09290c56a 280w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat.png?w=560&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=a88670177a3a15d4c2778c92802ca6ce 560w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat.png?w=840&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=453a959283187dc43ba8ad36aeef99cb 840w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat.png?w=1100&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=1371b3fca8a8bd5b794af40ecba37bfe 1100w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat.png?w=1650&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=12cf2fe91400bd27aa3f9f79cd9b7bc0 1650w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat.png?w=2500&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=4060920ff20b34cb5bd5c9a08971071c 2500w" />

5. Switch chat model

   * In the chat widget, press the dropdown to select a new model.

   <img src="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat-model-select.png?fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=83453e27763e0b5a17f7424a201007d2" alt="Chatting in Xcode and viewing requests in Helicone" data-og-width="453" width="453" data-og-height="446" height="446" data-path="images/integrations/xcode/xcode-chat-model-select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat-model-select.png?w=280&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=9640298d21fd75d9990e6e86e696b4f1 280w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat-model-select.png?w=560&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=6d7f129beac478b153c60d44baa411ca 560w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat-model-select.png?w=840&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=09ebfdb4e79a61de94010c6b3b4efae3 840w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat-model-select.png?w=1100&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=03775fec60d5fcabdc39424cfd09b8d3 1100w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat-model-select.png?w=1650&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=2edea38c60d806dfe84dfe0b388d228a 1650w, https://mintcdn.com/helicone/f5fOPlFeMMiXGcWR/images/integrations/xcode/xcode-chat-model-select.png?w=2500&fit=max&auto=format&n=f5fOPlFeMMiXGcWR&q=85&s=fdb197dd45d6924f3faf7cfc7cebdec8 2500w" />

## Notes

* URL points to the Helicone AI Gateway. Your Helicone API key is sent via the `Authorization` header.
* If you don’t see models, verify your org/provider keys are set in Helicone and that your key has access.
