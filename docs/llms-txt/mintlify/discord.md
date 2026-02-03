# Source: https://www.mintlify.com/docs/ai/discord.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Discord bot

> Add a bot to your Discord server that answers questions based on your documentation.

<Info>
  Discord integrations are available on [Pro and Enterprise plans](https://mintlify.com/pricing?ref=discord) with access to the assistant.
</Info>

The Discord bot supports your community with real-time answers from your documentation. The bot uses the Mintlify assistant to search your docs and provide accurate, cited responses, so it is always up-to-date.

The Discord bot only works in public channels. It replies to `@` mentions or to all messages in a specific channel.

Each message sent by the Discord bot counts toward your assistant message usage.

## Add the Discord bot to your server

<Note>
  You must have the "Manage Server" permission in Discord to add the bot.
</Note>

1. Navigate to the [Assistant](https://dashboard.mintlify.com/products/assistant) page in your dashboard.
2. In the Discord card, click **Configure**. This opens Discord.
   <Frame>
     <img src="https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=647b6ec148afcbb3177e536cba7f858e" alt="The connected apps section of the assistant page." className="block dark:hidden" data-og-width="1854" width="1854" data-og-height="470" height="470" data-path="images/assistant/connected-apps-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=280&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=e9337774ec02cdd6283428e915d417a9 280w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=560&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=002e3b6a86986574ce4611a069b896c7 560w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=840&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=d054f667a3cb4b1c650728528c367db0 840w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=1100&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=6f4cac6d895a64601545887c516f844f 1100w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=1650&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=0b00626aa3bc80ec27b30ea90617c440 1650w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=2500&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=cb9077db04fd6afce9f657268f4c54bb 2500w" />

     <img src="https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=cc2ef191b665b1042d1130d28b9346f2" alt="The connected apps section of the assistant page." className="hidden dark:block" data-og-width="1854" width="1854" data-og-height="470" height="470" data-path="images/assistant/connected-apps-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=280&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=0e068244afd690277d45d1d7fc3af0f5 280w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=560&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=67289ab57f5dfe6a2f1e497dc3568181 560w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=840&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=d95c2630a73c17a6626fd831704fdbeb 840w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=1100&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=8bddf2a70a68e65ce9650b7196aac94c 1100w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=1650&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=7faabc681aefdb7d0a3f72cdf11fc9cc 1650w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=2500&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=87a21214500ff312ea6d92eb68205cfb 2500w" />
   </Frame>
3. In Discord, select the server you want to add the bot to.
4. Authorize the bot to access your server.
5. Mention the bot to add it to a channel. The bot's default name is `@Mintlify Bot`.

## Create an `#ask-ai` channel

To help your community quickly get answers to their questions, the bot can reply to every message in a channel that you choose. By default, the bot replies to every message in channels named `#ask-ai`. Create an `#ask-ai` channel and let your community know that the bot will reply to messages in that channel.

If you want the bot to reply to messages in a different channel, select a channel in the Discord bot [configuration menu](https://dashboard.mintlify.com/products/assistant/settings/integrations).

<Frame>
  <img src="https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-light.png?fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=daeb71b6661d36ec7f64b4edc64222e2" alt="The Discord configuration panel in light mode." className="block dark:hidden" data-og-width="922" width="922" data-og-height="1132" height="1132" data-path="images/assistant/discord-configure-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-light.png?w=280&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=444db0c31c72bc13ff9452800ad457b3 280w, https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-light.png?w=560&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=fcd7ef3629aabc5790210369cc91b711 560w, https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-light.png?w=840&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=5014c756356529ad882c94b2741bc542 840w, https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-light.png?w=1100&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=576523a3120035713dc7dfae037e896f 1100w, https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-light.png?w=1650&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=ffdf96e4f2f8d6ffbe46e98690ffa15b 1650w, https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-light.png?w=2500&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=bf8c4f8c5fe40fbd70623bb8ddb5c6ab 2500w" />

  <img src="https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-dark.png?fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=39c6abfb3380410858bd4e6ec84f3d16" alt="The Discord configuration panel in dark mode." className="hidden dark:block" data-og-width="922" width="922" data-og-height="1132" height="1132" data-path="images/assistant/discord-configure-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-dark.png?w=280&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=b295bb8957fd27d4344b499c388512f3 280w, https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-dark.png?w=560&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=0cac75b5c95c7dfef3bf44241fe0c832 560w, https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-dark.png?w=840&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=cbb4899f61397ad956de3e553da58504 840w, https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-dark.png?w=1100&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=1de7de847f5fb9d1a67037e0fe16145a 1100w, https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-dark.png?w=1650&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=c8a1f823b82a0985844fb78c66a2177c 1650w, https://mintcdn.com/mintlify/nZ_rhnFbeRPc80xO/images/assistant/discord-configure-dark.png?w=2500&fit=max&auto=format&n=nZ_rhnFbeRPc80xO&q=85&s=d9b1554ef4783bed03fc66ebbad5f919 2500w" />
</Frame>

See [Starting Your First Discord Server](https://discord.com/blog/starting-your-first-discord-server) on the Discord blog for more information on creating a channel.

## Manage the Discord bot

After you add the Discord bot to your server, you can manage or remove the bot from the [Integrations](https://dashboard.mintlify.com/products/assistant/settings/integrations) tab in your dashboard.

In the Discord bot configuration menu, customize the bot by changing its avatar or name, and choose which channel it automatically replies to all messages in.
