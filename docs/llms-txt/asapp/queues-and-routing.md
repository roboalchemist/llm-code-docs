# Source: https://docs.asapp.com/agent-desk/digital-agent-desk/queues-and-routing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Queues and Routing

> Learn how to manage conversation queues and agent routing in the Digital Agent Desk.

Digital Agent Desk routes customer conversations to the most appropriate agents through a structured workflow:

1. A customer initiates a conversation
2. The system labels the conversation with an intent
3. Queue Routing evaluates the intent and additional criteria to select the appropriate queue
4. The queue assigns the conversation to an available agent from its associated agent group

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/routing.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=4c2ada7caa8d05394f588708a5d76569" alt="Issue Routing" data-og-width="1515" width="1515" data-og-height="1119" height="1119" data-path="images/messaging-platform/digital-agent-desk/routing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/routing.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=b99cda2a172bfff044136c23b60b243b 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/routing.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=21e60a7867578f09a39adb1adc79101a 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/routing.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=7b555c3a1d57acb245c017e6a7ace2c8 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/routing.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=3ee4b378177cfdd23ed8fa1992805aac 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/routing.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=e81ebcdc8788656c14b85079989d6729 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/routing.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=85ce6aeea80586ee6b68a89ba1778adc 2500w" />
</Frame>

Work with your ASAPP account team to configure intents, queues, and routing logic that align with your business needs.

## Managing Intents and Queues

An **Intent** classifies each customer conversation (issue) and serves as the primary method of categorization. ASAPP analyzes conversation data and business requirements to determine the available intents.

During runtime, Machine Learning (ML) models automatically assign the most appropriate Intent to each new issue.

**Queue Routing** uses these Intents along with other defined criteria to direct conversations to specific queues (referred to as [Attributes Based Routing](/agent-desk/digital-agent-desk/queues-and-routing/attributes-based-routing)). Each **queue** represents a group of agents qualified to handle particular types of issues.

<Note>
  ASAPP manages the configuration and maintenance of Intents and Queue Routing. Work with your ASAPP account team to optimize these settings for your business needs.
</Note>

## Optimizing Agent Concurrency

Concurrency controls how many simultaneous conversations each agent manages. Setting appropriate concurrency levels helps balance customer experience with agent workload.

Each agent has an individual concurrency level setting that determines their maximum number of concurrent conversations.

Digital Agent Desk provides several tools to help manage agent workloads:

* [High Effort Issues](#high-effort-issues) - Automatically identifies complex conversations that require more agent attention
* [Flexible Concurrency](#flexible-concurrency) - Dynamically adjusts capacity during natural conversation lulls

### High Effort Issues

By default, each conversation occupies one concurrency slot. However, certain conversations may require more time and attention from agents due to their complexity or scope.

Digital Agent Desk can automatically identify high-effort issues and assign them multiple concurrency slots based on the intent and other attributes.

For example, a technical troubleshooting conversation might count as two slots, while a simple account update remains one slot. This intelligent slot allocation helps:

* Give agents adequate time for complex customer needs
* Maintain balanced workloads across your team
* Improve customer satisfaction on challenging issues

Work with your ASAPP account team to configure complexity rules that align with your specific business scenarios and agent capabilities.

#### Monitoring High Effort Issues

The Real Time Dashboard displays agents handling high-effort issues with a "high effort" icon. Select any agent's name to view their current conversation assignments.

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/high-effort-dashboard.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=30d50b322ee9bb9e55fe1c0dfe3aa0cd" alt="High effort dashboard" data-og-width="902" width="902" data-og-height="842" height="842" data-path="images/messaging-platform/digital-agent-desk/high-effort-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/high-effort-dashboard.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=8eb6b93b1c373af148bedae54ace5970 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/high-effort-dashboard.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=6ecf69b2d0e5a8100af8522626ff6078 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/high-effort-dashboard.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=7a55e27e55ad840d3137ae639670f1a4 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/high-effort-dashboard.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=adb9df40649bf2a8c55c97ffe74faf48 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/high-effort-dashboard.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=b5490d9b2a1dbe7e8c23cb4fb0b799a8 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/high-effort-dashboard.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=94d2cb29b0afa06a52bff7bf8eb194e1 2500w" />
</Frame>

### Flexible Concurrency

Flexible Concurrency maximizes agent productivity by temporarily increasing their conversation capacity during natural downtimes, such as:

* When conversations enter auto-pilot timeout (a period of customer inactivity)
* While agents complete disposition tasks

<Frame>
  <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-concurrency.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=007b4f2875cad3285cab4fe004cda98d" alt="Flex concurrency" data-og-width="1985" width="1985" data-og-height="694" height="694" data-path="images/messaging-platform/digital-agent-desk/flex-concurrency.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-concurrency.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=5bd2dbb3e8e682d73b901bf2d042c97d 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-concurrency.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=8a96d87cc0d8a2927aee9d4f0def27a7 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-concurrency.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=2e969089714a3103090e90bf70e6ef8e 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-concurrency.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=9f5bbb87109e990f98cff068da3237d2 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-concurrency.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=eb7eaa06bc6faa62b2bd9ce7568b1761 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-concurrency.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=227d0f65c3900ed796401d075a2893ba 2500w" />
</Frame>

Configure Flexible Concurrency settings per queue to match different conversation types and agent capabilities.

#### Protecting Agents with Flex Protect

During auto-pilot timeout, the system assumes a conversation is temporarily inactive due to customer inactivity. However, customers may return and resume their conversation at any point during this timeout period. Without protection, this creates a challenging situation where an agent who received a new flexible assignment suddenly needs to handle both the returning customer and their new conversation simultaneously.

Flex Protect prevents this type of overload by:

* Assigning protected status to the agent
* Providing a configurable rest period where the system blocks new flexible assignments for that agent

<Note>
  We recommend enabling Flex Protect as agents may avoid using auto-pilot timeout if they fear being overloaded, leading to longer handle times.
</Note>

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/flex-protect.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=d7993f86484b4740656583004e64907b" alt="Flex protect" data-og-width="1985" width="1985" data-og-height="684" height="684" data-path="images/messaging-platform/digital-agent-desk/flex-protect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/flex-protect.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=18d09ae843d90b729a237840e99b9b11 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/flex-protect.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=e35a2c2a3dd1a9ee9c453232d5546ff2 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/flex-protect.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=ca4251c993bdc7f5ea0cdfb7104d1d69 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/flex-protect.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=36a6c4df6e1bb314bffb7bbd50e95e9c 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/flex-protect.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=a883d220d2c63cb352a2eb2d7af7a6e1 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/digital-agent-desk/flex-protect.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=f3495c006e503841970d7ed540b3a6fc 2500w" />
</Frame>

#### Monitoring Flexible Assignments

The Real Time Dashboard displays agents handling flexible assignments with a "flex" icon. Select any agent's name to view their current conversation assignments.

<Frame>
  <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-dashboard.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=88eaa85b440ba3e305b2fa1ee92757d1" alt="Flex dashboard" data-og-width="1554" width="1554" data-og-height="926" height="926" data-path="images/messaging-platform/digital-agent-desk/flex-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-dashboard.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=8d2b76b438902b407f51fe52d9af5999 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-dashboard.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=694c3030938e95cb98db9c016c7d28d5 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-dashboard.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=cfa849b36c84f572cd8c196b42146e0d 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-dashboard.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=2693d24642cf456ebe8e7426efdf8d7f 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-dashboard.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=f5be71922c3953460dcd210dcd2034e6 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/flex-dashboard.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=8129c7a7bc8e6afd7d4ca47e0ae95a4b 2500w" />
</Frame>
