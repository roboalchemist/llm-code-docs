# Source: https://www.mintlify.com/docs/index.md

# Source: https://www.mintlify.com/docs/guides/index.md

# Source: https://www.mintlify.com/docs/editor/index.md

# Source: https://www.mintlify.com/docs/components/index.md

# Source: https://www.mintlify.com/docs/agent/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the agent?

> Automate documentation updates with the agent. Create updates from Slack messages, PRs, or API calls.

<Info>
  The agent is available on [Enterprise plans](https://mintlify.com/pricing?ref=agent) for anyone with access to your dashboard.
</Info>

The agent creates pull requests with proposed changes to your documentation based on your prompts. When you send a request to the agent, it references your documentation, connected repositories, and Slack messages to create content that follows technical writing best practices and adheres to the Mintlify schema.

## What you can do with the agent

Use the agent to:

* Write new content based on your prompts, links to pull requests, or Slack threads.
* Revise outdated code examples and API references.
* Search and update existing content.
* Answer questions about your docs and technical writing topics.
* Capture knowledge from Slack conversations and pull requests before it gets lost.

## Where you can use the agent

* **Dashboard**: From any page in your dashboard, use the keyboard shortcut <kbd>⌘</kbd>+<kbd>I</kbd> (macOS) or <kbd>Ctrl</kbd>+<kbd>I</kbd> (Windows/Linux) to open the agent panel. Or click **Ask agent** on the [Overview](https://dashboard.mintlify.com/) page.
  <Frame>
    <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=56ee8c375606ca4a50b9b889474fc769" alt="The agent panel open in the dashboard." className="block dark:hidden" data-og-width="2056" width="2056" data-og-height="840" height="840" data-path="images/agent/dashboard-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=62e3a171a1923a8afc5e958979c9fa67 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=9b670552f1cd97b14fabef128ae051ee 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=cdf9081b352d9dc74f66b10ea1761333 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=2648dfc256eef274a6b2988da72b64db 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=2c179d8a203d364d04ca1201ce2caa83 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-light.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=52eaedba495900766dc706d0bda7e1bf 2500w" />

    <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=ad82516ec69eb247ac0475fd3397c338" alt="The agent panel open in the dashboard." className="hidden dark:block" data-og-width="2056" width="2056" data-og-height="840" height="840" data-path="images/agent/dashboard-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=bd58d31fcf5d51daaa7eec5dd3f565ce 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=98225e13a7b5d9052e7d9cb08d14d08a 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=1e82d5cf5b33c24744db75d4acff5f0e 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=76f753872cb7dca5446e2a98c8c7f6e8 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=50053641543ddeeeb18818da997132ea 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-dark.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=b1de133975f47c6a4f99eead9069d99e 2500w" />
  </Frame>
* **Slack**: Add the agent to your Slack workspace and mention `@mintlify` to prompt it.
* **API**: Embed the agent in custom applications using the [agent endpoints](/api-reference/agent/create-agent-job)

## Next steps

<Card title="Quickstart" horizontal icon="rocket" href="/agent/quickstart">
  Start using the agent in your dashboard.
</Card>

<Card title="Connect Slack" horizontal icon="slack" href="/agent/slack">
  Add the agent to your Slack workspace.
</Card>

<Card title="Customize behavior" horizontal icon="wrench" href="/agent/customize">
  Configure the agent with an `AGENTS.md` file.
</Card>

<Card title="Write effective prompts" horizontal icon="pen" href="/agent/effective-prompts">
  Get better results with focused prompts.
</Card>
