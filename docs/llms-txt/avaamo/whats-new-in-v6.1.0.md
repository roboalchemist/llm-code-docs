# Source: https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.1.x/whats-new-in-v6.1.0.md

# What's new in v6.1.0?

In this release, a new agent called the **Universal Agent** has been introduced. In simple terms, a **Universal agent** is a "group of agents" that handles tasks of multiple agents in a single conversational flow. It can integrate and connect with independent virtual agents to route, filter, and provide real-time responses.&#x20;

The primary feature of a Universal agent is the ability to have "one" agent across multiple departments in an Enterprise organization. Typically, large enterprises can have multiple departments, each with its own individual agents catering to different aspects of the organization. Since all agents are a part of the same organization, by integrating these into a Universal agent, you are providing a seamless and pleasant experience to the users.&#x20;

The following illustration depicts an "Acme Enterprise" Universal agent linked with independent virtual agents such as - Acme HR, Acme IT, and Acme Finance. Each department can continue to build these agents independently. The user can just use one agent - the  "Acme Enterprise" agent for all the queries across different departments:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FaHxSVAnYGwAkTh3LQ6Gs%2Facme-enterprise-UA-RN.png?alt=media\&token=8bb65d1a-5bd6-4ba6-a957-e00f356275f7)

## How does it work - Quick Overview?

Each agent linked to the universal agents is referred to as a **Member agent**. When a user query is posted to a Universal agent, it routes the user’s intent to the appropriate **Member agent** for simple Q\&A or multi-turn conversations, renders member responses inline, and also manages the conversation context.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FX20U3UTsFJr3BDwpGJMO%2FScreenshot%202022-04-22%20at%205.21.29%20PM.png?alt=media\&token=c5a3cae4-5d88-4711-8710-c234948718ba)

{% hint style="success" %}
With release 6.1.0, a Universal agent can connect with any Avaamo agent.
{% endhint %}

## Why Universal agents?

The Universal agent is a very powerful feature that combines the capabilities of individual agents into one unified agent.&#x20;

To provide an overview of some key benefits, it is categorized based on the user persona - [End users](#end-users), [Developers](#developers), and [Business users](#business-users) in the enterprise organization.&#x20;

### End users

The following lists some of the key benefits of Universal agents for end-users:

* **Unified interface:** Provides a unified interface to the users, completely hiding the details of the connected members. All intents/ use cases are available via a single agent. It centralizes the agent interaction across multiple departments, domains, or sectors.
* **Seamless user experience**: Avoids putting users through the hassles of using multiple agents built for various tasks. For example: When different departments in an organization such as procurement, finance, and HR have independent virtual assistants to answer queries and complete mundane tasks, it is tedious for users who want assistance in matters relevant to more than one department - as they have to go through the hassles of using multiple agents to built for various tasks.

### Developers

The following lists some of the key benefits of Universal agents for developers:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2D1yt4wOg098PeP68RkS%2FScreenshot%202022-05-11%20at%2011.13.45%20AM.png?alt=media\&token=523ccbe6-7208-46c2-b5f0-1e2f77cc5f42)

* **Quick and easy configuration**: Provides quick and easy methods to create and manage the connected member agents.&#x20;
* **Separation and Modularization:** Each member agent is an independent virtual agent that can be managed separately by each department or sector. Universal Agent leverages the training imparted to the individual members for intent detection. No duplication of training is required. This helps in easy maintenance and also helps to troubleshoot and debug easily.&#x20;
* **Regression testing**: Allow you to perform regression testing across member agents. You can test end-to-end flow in a single Universal agent, instead of performing multiple regression testing in each member agent.

See [Add member agents](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/add-member-agents), [Manage member agents](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/manage-member-agents), and [Regression testing](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing-universal-agents), for more information.

### Business users

**Unified analytics**: Provides a unified analytics dashboard for monitoring the usage across the member agents.  See [Analytics - Universal agents](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics-universal-agent), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fmyd9lGbigfwptRQFeOKw%2F6.1-analytics-new.png?alt=media\&token=80b3d47a-1934-4946-b699-ff939fde5e6d)

## Key highlights&#x20;

The following are some of the key highlights of Universal agents:

* **Intent detection and routing**: Universal agents detect the intent and route the conversation to the appropriate member that can fulfill the user’s request in the best possible way.
* **Context management**: Universal agents maintain the context of the dialog once the conversation starts with a particular member agent. It detects the end of conversation and fallback from the member agents.
* **Disambiguation:** When the user's intent is not clear, the Universal agent disambiguates between its member agents and displays options for the user to choose from.
* **Intent switching:** Universal agents allow switching of intents mid-way through a dialog from one member agent to another.
* **Conversation resumption:** Universal agents maintain the conversation context at all times across member agents.
* **Context sharing:** Universal agents detect and preserve contextual information of conversation across members.

## More information

See [Universal agent](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent), for more information.
