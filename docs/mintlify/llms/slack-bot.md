# Source: https://www.mintlify.com/docs/ai/slack-bot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack bot

> Add a bot to your Slack workspace that answers questions based on your documentation.

<Info>
  The Slack app is available for [Pro and Custom plans](https://mintlify.com/pricing?ref=slack-app) with access to the assistant.
</Info>

The Slack app adds a bot to your workspace that supports your community with real-time answers. The bot uses the Mintlify assistant to search your docs and provide accurate, cited responses, so it is always up-to-date.

The bot can only see messages in channels you specifically add it to. It does not have global read access to your workspace.

The bot responds to `@` mentions or to all messages in a specific channel that you configure.

Each message sent by the bot counts toward your assistant message usage.

## Set up the Slack app

<Note>
  You can only install the Slack app once per workspace. If you have multiple Mintlify deployments, you can only connect one deployment at a time to a workspace. You must disconnect the app from one deployment before connecting it to another.
</Note>

If your Slack Workspace Owner requires admin approval to install apps, ask them to approve the Mintlify Slack app before you add it.

1. Navigate to the [Assistant](https://dashboard.mintlify.com/products/assistant) page in your dashboard.
2. In the Slack card, click **Configure**. This opens Slack.
   <Frame>
     <img src="https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=647b6ec148afcbb3177e536cba7f858e" alt="The connected apps section of the assistant page." className="block dark:hidden" data-og-width="1854" width="1854" data-og-height="470" height="470" data-path="images/assistant/connected-apps-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=280&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=e9337774ec02cdd6283428e915d417a9 280w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=560&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=002e3b6a86986574ce4611a069b896c7 560w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=840&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=d054f667a3cb4b1c650728528c367db0 840w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=1100&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=6f4cac6d895a64601545887c516f844f 1100w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=1650&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=0b00626aa3bc80ec27b30ea90617c440 1650w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-light.png?w=2500&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=cb9077db04fd6afce9f657268f4c54bb 2500w" />

     <img src="https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=cc2ef191b665b1042d1130d28b9346f2" alt="The connected apps section of the assistant page." className="hidden dark:block" data-og-width="1854" width="1854" data-og-height="470" height="470" data-path="images/assistant/connected-apps-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=280&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=0e068244afd690277d45d1d7fc3af0f5 280w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=560&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=67289ab57f5dfe6a2f1e497dc3568181 560w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=840&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=d95c2630a73c17a6626fd831704fdbeb 840w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=1100&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=8bddf2a70a68e65ce9650b7196aac94c 1100w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=1650&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=7faabc681aefdb7d0a3f72cdf11fc9cc 1650w, https://mintcdn.com/mintlify/iWC1DRgIiF7skzGL/images/assistant/connected-apps-dark.png?w=2500&fit=max&auto=format&n=iWC1DRgIiF7skzGL&q=85&s=87a21214500ff312ea6d92eb68205cfb 2500w" />
   </Frame>
3. Follow the Slack prompts to add the app to your workspace.
4. Mention the bot to add it to a channel. The bot's default name is `@mintlify-assistant`.

## Create an `#ask-ai` channel

To help your users quickly get answers to their questions, the bot can reply to every message in a channel that you choose. By default, the bot replies to every message in channels named `#ask-ai`. Create an `#ask-ai` channel and let your users know that the bot replies to messages in that channel. See [Create a channel](https://slack.com/help/articles/201402297-Create-a-channel) in the Slack Help Center for more information.

If you want the bot to reply to messages in a different channel, select a channel in the Slack bot [configuration menu](https://dashboard.mintlify.com/products/assistant/settings/integrations).

<Frame>
  <img src="https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-light.png?fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=52112c0ed2e0d0767ef9ce9529e31b5b" alt="The Slack configuration panel in light mode." className="block dark:hidden" data-og-width="912" width="912" data-og-height="952" height="952" data-path="images/assistant/slack-configure-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-light.png?w=280&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=35b7d9e871acd00465d5cb0de29833b1 280w, https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-light.png?w=560&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=66060eb7772ce5558b3a242498b404f2 560w, https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-light.png?w=840&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=0d2d5f73a8033abc443bd783764666e0 840w, https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-light.png?w=1100&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=4a54bdde6221dabd55a22f3bc476a527 1100w, https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-light.png?w=1650&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=5068147fa991faa05dfc059bb0f4ce44 1650w, https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-light.png?w=2500&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=f694543a254ef4b0eb3e4ee4d17a4099 2500w" />

  <img src="https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-dark.png?fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=ac31230309042ad15238b57518038bf9" alt="The Slack configuration panel in dark mode." className="hidden dark:block" data-og-width="914" width="914" data-og-height="954" height="954" data-path="images/assistant/slack-configure-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-dark.png?w=280&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=758bd60e7a6eda22a63e0129a114dafb 280w, https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-dark.png?w=560&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=735fe2b01a48007310d1a980f0bb8f5f 560w, https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-dark.png?w=840&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=85269f5e0c304d032aa049c2f9bb10fc 840w, https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-dark.png?w=1100&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=f1db1d6595375e0c978ad7f4aa00e2f5 1100w, https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-dark.png?w=1650&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=41b01ef125a4f9d14c4b6854b5007810 1650w, https://mintcdn.com/mintlify/Cua8vliIsZB_FwDG/images/assistant/slack-configure-dark.png?w=2500&fit=max&auto=format&n=Cua8vliIsZB_FwDG&q=85&s=d22865176e4d349d9e90a09c4550a3ca 2500w" />
</Frame>

## Manage the Slack app

After you add the app to your workspace, you can manage or remove the app from the [Integrations](https://dashboard.mintlify.com/products/assistant/settings/integrations) tab.

In the Slack bot configuration menu, customize the bot by changing its avatar or name, and choose which channel it automatically replies to all messages in.
