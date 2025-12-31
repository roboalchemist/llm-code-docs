# Source: https://mintlify.com/docs/ai/suggestions.md

# Agent suggestions

> Monitor Git repositories for changes and receive suggested documentation updates.

<Note>
  Agent suggestions are available on [Custom plans](https://mintlify.com/pricing?ref=autopilot). To enable suggestions for your organization, [contact our sales team](mailto:gtm@mintlify.com).
</Note>

You can allow the [agent](/ai/agent) to suggest documentation updates from two sources.

* **Pull request changes**: Monitor selected Git repositories for code changes that require documentation updates.
* **Assistant conversations**: Analyze questions that users ask the assistant on your documentation site to identify content gaps.

When the agent identifies potential documentation updates, it creates a suggestion in your dashboard with context to create a pull request.

Use suggestions to proactively keep your documentation up to date when new features ship or to address common user questions.

## Prerequisites

Before using suggestions, you must install the [Mintlify GitHub App](/deploy/github) in your organization. The app must have access to your documentation repository and at least one other repository where code changes require documentation updates.

## Configure suggestions

Configure which repositories the agent monitors and how you receive notifications in the agent settings. The settings page displays all the GitHub organizations and repositories the agent is monitoring.

To access the agent settings:

1. Click the **Ask agent** button in your dashboard to open the agent panel.
2. Click the **Settings** button.
   <Frame>
     <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=ecb555eecfddf7480baaaf7d2fd6bce9" alt="The settings button in light mode." className="block dark:hidden" data-og-width="668" width="668" data-og-height="112" height="112" data-path="images/agent/dashboard-settings-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=f6663dbc0d65a673d8d40a1a5021c4e6 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=8f16ed84866ed266b6c94ee063504e86 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=0f09f59a375b2d0fa1a52e7105b9983a 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=9bd984bb1301430689ca1f80a55949da 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=27abd64a63bcba9de2cb2ca4fea13c76 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-light.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=0fbcc0de8221607fd1ddddc91ff7299c 2500w" />

     <img src="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=a3250fa23cac19e8914b7185ac24c6d0" alt="The settings button in dark mode." className="hidden dark:block" data-og-width="670" width="670" data-og-height="112" height="112" data-path="images/agent/dashboard-settings-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=280&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=e24b9bd26f3ae15ba38467da9e9fd650 280w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=560&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=1dbb09e9fc6d17ab545c6ad46e7e5585 560w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=840&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=05978a332b79eb6ccf7d86ae3c579039 840w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=1100&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=38f053dd12cc6197779a368756b5eb34 1100w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=1650&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=c1d8e1cd78e6a494852b809cbeb1a695 1650w, https://mintcdn.com/mintlify/l1-TgESjTbrqcwOU/images/agent/dashboard-settings-dark.png?w=2500&fit=max&auto=format&n=l1-TgESjTbrqcwOU&q=85&s=508da1702ec011fa336b0fd7738c60c1 2500w" />
   </Frame>

### Monitor repositories

The agent monitors the default branch (typically `main`) for each repository that you enable. A GitHub check named **Mintlify Autopilot** runs on pull requests in monitored repositories to analyze them for potential documentation updates. When you merge a pull request that requires documentation updates, the agent creates a suggestion in your dashboard.

<Note>
  When you first enable monitoring for a repository, the agent creates suggestions for pull requests merged in the last seven days. This backfill only occurs if no suggestions already exist for that repository. You may see multiple suggestions appear immediately after enabling monitoring.
</Note>

If you disable monitoring, the agent immediately stops monitoring the repository. Any existing suggestions for that repository remain in your dashboard until you dismiss them.

### Conversation insights

Enable conversation insights to receive suggestions based on common questions users ask the assistant.

When enabled, the agent periodically analyzes assistant conversations and creates suggestions when it identifies patterns of questions that indicate missing or unclear documentation.

### Notifications

Agent suggestions always appear in your dashboard. You can configure notifications to receive email or Slack direct messages when the agent creates new suggestions.

<Tip>
  If you don't receive email notifications for suggestions, check your spam folder and add the email address `notifications@mintlify.com` to your safe sender list.
</Tip>

## Review suggestions

The agent creates suggestions in your dashboard. Each suggestion shows the pull request or assistant conversation topic that triggered the suggestion, creation date, and proposed documentation updates.

The **Ask agent** button in your dashboard displays the number of suggestions waiting for your review.

<Frame>
  <img src="https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-light.png?fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=ee43454f05cddd0e0a409d2fc62d32cc" alt="The Ask agent button showing four suggestions in light mode." className="block dark:hidden" data-og-width="350" width="350" data-og-height="162" height="162" data-path="images/suggestions/count-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-light.png?w=280&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=953e8fdf858e41af5935ddc9dca80432 280w, https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-light.png?w=560&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=e1ee702f175d92d4144a5ff4b3cb344d 560w, https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-light.png?w=840&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=a731fad0243cc81938b142c0dc3f709d 840w, https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-light.png?w=1100&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=2b4eba66ba14bc117f95598f1d690ac9 1100w, https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-light.png?w=1650&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=0fdf163d478e15ee988f27da22aa5892 1650w, https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-light.png?w=2500&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=3b3f41c4899bc747736772f5b985824d 2500w" />

  <img src="https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-dark.png?fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=7077f4d4827154e6d73df75a6fb863e0" alt="The Ask agent button showing four suggestions in dark mode." className="hidden dark:block" data-og-width="350" width="350" data-og-height="162" height="162" data-path="images/suggestions/count-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-dark.png?w=280&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=115f73ee40cb3c64cf78b744135ec960 280w, https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-dark.png?w=560&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=12604a13780b762f5909ef9cff3c1564 560w, https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-dark.png?w=840&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=e48fdca93662cf53d460e200e54dc840 840w, https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-dark.png?w=1100&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=c0c1555343fb0068f58eacd95617d58f 1100w, https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-dark.png?w=1650&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=acd67882aff7b0935c2f6aa273e97aad 1650w, https://mintcdn.com/mintlify/HWCrkYCTtCJkLU3u/images/suggestions/count-dark.png?w=2500&fit=max&auto=format&n=HWCrkYCTtCJkLU3u&q=85&s=7a3b88244941b23931b3f39773069da9 2500w" />
</Frame>

### Create pull requests

Add suggestions as context for the agent to create pull requests.

1. Click the **Ask agent** button in your dashboard to open the agent panel.
2. Click **Add to chat**.
3. Submit the prompt to the agent to open a pull request.

### Dismiss suggestions

If a suggestion doesn't require documentation updates or you've already addressed the changes, dismiss it to remove it from your dashboard.

1. Click the **Ask agent** button in your dashboard to open the agent panel.
2. Click the **Dismiss** button next to any suggestions that you want to dismiss.

The suggestion is immediately removed from your dashboard. You cannot retrieve dismissed suggestions.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://mintlify.com/docs/llms.txt