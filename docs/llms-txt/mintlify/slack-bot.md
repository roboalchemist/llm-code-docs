# Source: https://mintlify.com/docs/ai/slack-bot.md

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
  If your Slack Workspace Owner requires admin approval to install apps, ask them to approve the Mintlify Slack app before you add it.
</Note>

1. Navigate to the [Integrations](https://dashboard.mintlify.com/products/assistant/settings/integrations) tab of the **Assistant Configurations** page in your dashboard.
2. In the Slack card, click **Connect**. This opens Slack.

<Frame>
  <img src="https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-light.png?fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=16fd173d82f1e5f8a2ad82e78aaa68b9" alt="The Connect button in the Slack card in light mode." className="block dark:hidden" data-og-width="842" width="842" data-og-height="230" height="230" data-path="images/assistant/slack-connect-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-light.png?w=280&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=23fe51216da7849b14aca5db3ae8f74d 280w, https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-light.png?w=560&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=9bcf9be6912ca8099655d2cfcf82927c 560w, https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-light.png?w=840&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=73668b838e11aeffc92b8c38893dcb53 840w, https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-light.png?w=1100&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=b1797f5cffc4ed66412e14a103dd74e2 1100w, https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-light.png?w=1650&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=2a695b92a3a14be4156ebe9d2a87793d 1650w, https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-light.png?w=2500&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=1cded7a3b2a3e523d4d15bb4529fe507 2500w" />

  <img src="https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-dark.png?fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=b3f0aca4b003fc9055f57b65226be210" alt="The Connect button in the Slack card in dark mode." className="hidden dark:block" data-og-width="842" width="842" data-og-height="230" height="230" data-path="images/assistant/slack-connect-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-dark.png?w=280&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=a98dd7e53513a10ed3c51bfb13665ef2 280w, https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-dark.png?w=560&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=918ae3c9a6125250929eca85904a5dcb 560w, https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-dark.png?w=840&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=3e3f16291e2d44d9e283daacaa06589c 840w, https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-dark.png?w=1100&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=c55c6477359451caa747339b13ac2625 1100w, https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-dark.png?w=1650&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=5331c78d26b38747442efb1743f3b90f 1650w, https://mintcdn.com/mintlify/pskY4AQ8UobQvbpU/images/assistant/slack-connect-dark.png?w=2500&fit=max&auto=format&n=pskY4AQ8UobQvbpU&q=85&s=0eaaae4bfc0224f25bda09161699978e 2500w" />
</Frame>

1. Follow the Slack prompts to add the app to your workspace.
2. Mention the bot to add it to a channel. The bot's default name is `@mintlify-assistant`.

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


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://mintlify.com/docs/llms.txt