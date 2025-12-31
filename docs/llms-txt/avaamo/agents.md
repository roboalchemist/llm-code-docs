# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/agents.md

# Agents

An **agent** is synonymous with a "human agent". Similar to a human agent that has or is trained with different skills for responding to user queries, an agent is a "container of skills", each specialized to understand and handle a specific task in the user conversation flow. In the Avaamo Platform, an agent can contain the following types of skills:

* [Smalltalk](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk): Used for informal or casual user conversations.
* [Dynamic Q\&A (Question & Answers)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a): Used for one-off questions and answers.
* [Dialog](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer): Used for complex multi-turn conversational flows.
* [Answers](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1): Used to provide answers from enterprise content.&#x20;

{% hint style="danger" %}
Answers skill is deprecated in Atlas 8. See [Atlas 8 - Deprecated and removed features](https://docs.avaamo.com/user-guide/deprecated-and-removed-features/atlas-8-deprecated-and-removed-features), for more information.
{% endhint %}

When a user posts a query to an agent, the agent understands and classifies the input (text and voice) and selects an appropriate skill to engage with the user.&#x20;

**Example**: A Pizza agent can contain Membership and Rewards policy Answers skill, Order Pizza Dialog skill, FAQ Q\&A skill, and Smalltalk skill for responding to user queries.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FK6V41Pe5LcXbwDLlWwqz%2Fimage.png?alt=media\&token=11692e84-44e1-469a-972a-84ccd1761a86)

Similarly, the following illustration depicts responses from a Dialog skill in a Pizza agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FkhOTUjQRDhtCty13p8ed%2Fimage.png?alt=media\&token=f2e3a546-2a7e-409c-b3e1-610464ff30de)

An **agent** is a primary interface for users to have a conversation across multiple channels such as Facebook, Microsoft Teams, Web, and Slack (to name a few).

{% hint style="success" %}
**Key Points**:

* Quickly get started with creating an agent and adding skills to the agent. See [Create agent](https://docs.avaamo.com/user-guide/quick-start-tutorials/create-an-agent), for more information.&#x20;
* Alternatively, you can also make a copy from one of the sample agents and start enhancing it.&#x20;
* Plan your development process. An agent goes through various iterations from its conception to production. See [Plan your development process (Agent life cycle)](https://docs.avaamo.com/user-guide/how-to/plan-your-development-process-agent-life-cycle), for more information.
* Get familiar with different UI elements of the agent dashboard. See the [Product overview](https://docs.avaamo.com/user-guide/quick-start-tutorials/product-overview), for more information.
* Understand the best practices, dos, and don'ts of designing an agent. See [Design agents](https://docs.avaamo.com/user-guide/how-to/build-agents/design-agents), for more information.
* As you build skills and add to the agent, you train the agent to respond to user queries. Further, with each user's conversations, the agent continuously learns and adapts iteratively to enhance the accuracy of the responses. See [Add skills to agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills-to-agent), for more information.
* Agents also provide several configuration options to add multiple languages, define environment variables, and other common settings. See [Configure agents](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents), for more information.
* Iteratively test your agent at each step using Simulator and Regression Testing. See [Test agents](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents), for more information.
* The agents can also be deployed across multiple channels enabling better customer engagement and satisfaction. See [Deploy agents](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy), for more information.
* Monitor the performance of your agent on different channels using analytics and insights. See [Monitor agents](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze), for more information.
  {% endhint %}

### Universal agent

In simple terms, a **Universal agent** is a "group of agents" that handles the tasks of multiple agents in a single conversational flow. It can integrate and connect with independent virtual agents to route, filter, and provide real-time responses.&#x20;

The primary feature of a Universal agent is the ability to have "one" agent across multiple departments in an Enterprise organization. Typically, large enterprises can have multiple departments, each with its agents catering to different aspects of the organization. Since all agents are a part of the same organization, by integrating these into a Universal agent, you are providing a seamless and pleasant experience to the users.&#x20;

The following illustration depicts an "Acme Enterprise" Universal agent linked with independent virtual agents such as - Acme HR, Acme IT, and Acme Finance. Each department can continue to build these agents independently. The user can just use one agent - the  "Acme Enterprise" agent for all the queries across different departments:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FnJuXjnugtu1YTPh6gDiX%2FScreenshot%202022-05-20%20at%206.01.13%20PM.png?alt=media\&token=b110d1be-d2f7-453f-a658-79fb38874cad)

See [Universal agents](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent), for more information.

### Advanced agents

In its fundamental nature, an `Advanced agent` achieves the "true" objective of a "Conversational Assistant" by involving the user in a dialogue closely resembling human interaction.&#x20;

The `Advanced Agent` uses our next-generation inference engine to provide a better user experience. It takes on a personalized approach, understanding nuances in the conversation, transforming interactions from a robotic demeanor to a more pleasurable and "conversational" experience for the user.

To the developers, this translates to **`a significant reduction in the amount of training data`** needed for the agent to comprehend user queries. You only have to train your agent with minimal meaningful user queries. The `Advanced agent` is capable of comprehending numerous nuances and variations in user queries.&#x20;

An `Advanced agent`, hence, stands out as distinctly superior, more intelligent, and more personalized compared to a `Standard agent`. The following illustrations depict a sample comparison of training data between a `Standard agent` and an `Advanced agent`:

|                                                                                                                       Standard agent                                                                                                                       |                                                                                                                       Advanced agent                                                                                                                       |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FeDSpekbePOODlJ3BW8dP%2Fimage.png?alt=media&#x26;token=be3fe3a2-0572-4e1a-95ac-bb77b54523af" alt="" data-size="original"> | <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fcbl7SfijnBlT1LkckXPN%2Fimage.png?alt=media&#x26;token=1b83f4e1-7486-437b-b53f-a5c6e39d9f61" alt="" data-size="original"> |

See [Advanced agents](https://docs.avaamo.com/user-guide/how-to/build-agents/create-advanced-agent), for more information.
