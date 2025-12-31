# Source: https://mintlify.com/docs/ai/discord.md

# Discord bot

> Add a bot to your Discord server that answers questions based on your documentation.

<Info>
  Discord integrations are available on [Pro and Custom plans](https://mintlify.com/pricing?ref=discord) with access to the assistant.
</Info>

The Discord bot supports your community with real-time answers from your documentation. The bot uses the Mintlify assistant to search your docs and provide accurate, cited responses, so it is always up-to-date.

The Discord bot only works in public channels. It replies to `@` mentions or to all messages in a specific channel.

Each message sent by the Discord bot counts toward your assistant message usage.

## Add the Discord bot to your server

<Note>
  You must have the "Manage Server" permission in Discord to add the bot.
</Note>

1. Navigate to the [Integrations](https://dashboard.mintlify.com/products/assistant/settings/integrations) tab of the **Assistant Configurations** page in your dashboard.
2. In the Discord card, click **Connect**. This opens Discord.
   <Frame>
     <img src="https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-light.png?fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=f0a40c8910f8b0fafa0b45d99350c019" alt="The connect button in light mode." className="block dark:hidden" data-og-width="854" width="854" data-og-height="234" height="234" data-path="images/assistant/discord-connect-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-light.png?w=280&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=e9baa0baeef52c87db15c1f8df0c8c9d 280w, https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-light.png?w=560&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=5072b9877e4072590f00b3dc12261c5d 560w, https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-light.png?w=840&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=ce85c584f64ca9f790576e846c7c51a4 840w, https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-light.png?w=1100&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=c999c92fbbf30024c64d90d2f52e952d 1100w, https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-light.png?w=1650&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=152d5b4e7376852a0a4432aac61a8330 1650w, https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-light.png?w=2500&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=7540a16039560e7157708061b6f767c2 2500w" />

     <img src="https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-dark.png?fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=281845b61bbd547f20deea944542ae4c" alt="The connect button in dark mode." className="hidden dark:block" data-og-width="854" width="854" data-og-height="234" height="234" data-path="images/assistant/discord-connect-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-dark.png?w=280&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=ef6261bc5de49b2ff7286332643a9c86 280w, https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-dark.png?w=560&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=6a0a172e909b23d9f8b8dac128bb498f 560w, https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-dark.png?w=840&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=0650463a971a5601457e3c360de2f3b4 840w, https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-dark.png?w=1100&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=d1180df5c2027ada9d68bf1816ab5f3c 1100w, https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-dark.png?w=1650&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=428bcec30891b043ba38404fe9bd172b 1650w, https://mintcdn.com/mintlify/SyQazJmuH84Z27gS/images/assistant/discord-connect-dark.png?w=2500&fit=max&auto=format&n=SyQazJmuH84Z27gS&q=85&s=4bd1ce5e6a6cd0d1a1569790d8756b67 2500w" />
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


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://mintlify.com/docs/llms.txt