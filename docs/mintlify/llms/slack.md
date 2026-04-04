# Source: https://www.mintlify.com/docs/agent/slack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add the agent to Slack

> Use the agent in Slack to make documentation updates from conversations and capture team knowledge.

<Note>
  If your Slack Workspace Owner requires admin approval to install apps, ask them to approve the Mintlify app before you connect it.
</Note>

## Connect your Slack workspace

1. Open the agent panel in your dashboard.
2. Click the **Settings** button.
   <Frame>
     <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=ecb555eecfddf7480baaaf7d2fd6bce9" alt="The settings button in light mode." className="block dark:hidden" data-og-width="668" width="668" data-og-height="112" height="112" data-path="images/agent/dashboard-settings-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=f6663dbc0d65a673d8d40a1a5021c4e6 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=8f16ed84866ed266b6c94ee063504e86 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=0f09f59a375b2d0fa1a52e7105b9983a 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=9bd984bb1301430689ca1f80a55949da 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=27abd64a63bcba9de2cb2ca4fea13c76 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=0fbcc0de8221607fd1ddddc91ff7299c 2500w" />

     <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=a3250fa23cac19e8914b7185ac24c6d0" alt="The settings button in dark mode." className="hidden dark:block" data-og-width="670" width="670" data-og-height="112" height="112" data-path="images/agent/dashboard-settings-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=e24b9bd26f3ae15ba38467da9e9fd650 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=1dbb09e9fc6d17ab545c6ad46e7e5585 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=05978a332b79eb6ccf7d86ae3c579039 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=38f053dd12cc6197779a368756b5eb34 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=c1d8e1cd78e6a494852b809cbeb1a695 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=508da1702ec011fa336b0fd7738c60c1 2500w" />
   </Frame>
3. In the Slack integration section, click **Connect**.
4. Follow the Slack prompts to add the `mintlify` app to your workspace.
5. Follow the Slack prompts to link your Mintlify account to your Slack workspace.
6. Test that the agent is working and responds when you:
   * Send a direct message to it.
   * Mention it with `@mintlify` in a channel.

## Use the agent in Slack

Once connected, you can:

* Send direct messages to the agent to use it privately to update your documentation.
* Mention `@mintlify` in a channel to use it publicly and collaboratively.
* Continue conversations in threads to iterate on changes.
* Share pull request links with the agent to update related documentation.

## Update documentation

Use the agent to update your documentation with a new request or in an existing thread.

* **New request**: Send a direct message to the agent or mention `@mintlify` in a channel with instructions on what to update.
* **Existing thread**: Reply in the thread and mention `@mintlify` with instructions on what to update.

The agent reads the context of the request or thread and creates a pull request in your connected repository with the updates.

## Best practices

* **Be specific**: Tell the agent exactly what you want documented and where it should go.
* **Add context**: If a thread doesn't contain all the necessary information, include additional details in your message to the agent.
* **Review carefully**: You should always review pull requests that the agent creates before merging them.
