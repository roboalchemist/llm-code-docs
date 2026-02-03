# Source: https://docs.augmentcode.com/using-augment/slack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Augment for Slack

> Chat with Augment directly in Slack to explore your codebase, get instant help, and collaborate with your team on technical problems.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Augment for Slack

Augment for Slack brings the power of Augment Chat to your team's Slack workspace. Mention <Command text="@Augment" /> in any channel or start a DM with Augment to have deep codebase-aware conversations with your team. Before you can use Augment for Slack, you will need to [install the Augment Slack App](/setup-augment/install-slack-app).

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6f5619de7d03d015c25ce2f514a56fd5" alt="Augment for Slack" className="rounded-xl" data-og-width="1544" width="1544" data-og-height="866" height="866" data-path="images/slack-chat-reply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=636f110e793cb75bf701d78e0147210e 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4d4433371e614333995402bd9c502be4 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f2e551a655626021bb180c0494e84e5b 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=af85a5400a3db50da8b71456e47b51e8 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=80a7ddc46d881dcc81a51e3aa6f2d92e 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/slack-chat-reply.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4e240bc18073e63e661404f2d3cc00fe 2500w" />

## Adding Augment to Channels

Mention <Command text="@Augment" /> to add it to any public or private channel.

*Note: To protect your code, Augment excludes repository context in channels with external members.*

## Starting Conversations in Channels

Mention <Command text="@Augment" /> anywhere in your message or thread to start a conversation. Augment will consider the entire thread's context when responding. Remove messages by adding a ❌ reaction.

## Direct Messages

While group discussions help share knowledge, you can also have private conversations with Augment. Access it by:

* Clicking the Augment logo in the top right of your Slack workspace
* Finding it under <Command text="Apps" /> in the Slack sidebar
* Pressing <Keyboard shortcut="Cmd/Ctrl T" /> and searching for <Command text="@Augment" />

If you don't see the Augment logo, add it to your [navigation bar](/setup-augment/install-slack-app#3-add-augment-to-the-slack-navigation-bar). *If you don't see this option, contact your workspace admin to [re-install the App](/setup-augment/install-slack-app#2-install-slack-app).*

You do not need to mention Augment in direct messages - it will respond to every message!

## Restricting where Augment can be used

Augment already avoids responding with codebase context in external channels, to protect your codebase from Slack users outside of your organization. Beyond this, you can also further restrict what channels Augment can be used in, with an allowlist. If configured, Augment will only respond in channels or DMs that are in the allowlist. To use this feature, contact us.

## Repository Context

Augment uses the default branch (typically `main`) of your linked repositories. Currently, other branches aren't accessible.

If you have multiple repositories installed, use <Command text="/augment repo-select" /> to choose which repository Augment should use for the current conversation. This selection applies to the specific channel or DM where you run the command, allowing you to work with different repositories in different conversations.

## Feedback

Help us improve by reacting with 👍 or 👎 to Augment's responses, or use the `Send feedback` message shortcut. We love hearing from you!
