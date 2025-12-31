# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/overview-get-started.md

# Overview - Get started

{% hint style="info" %}
**Note**: You can create Universal agents only if it is enabled in your account. Contact Avaamo Support for further assistance.&#x20;
{% endhint %}

In simple terms, a **Universal agent** is a "group of agents" that handles tasks of multiple agents in a single conversational flow. It can integrate and connect with independent virtual agents to route, filter, and provide real-time responses.&#x20;

The primary feature of a Universal agent is the ability to have "one" agent across multiple departments in an Enterprise organization. Typically, large enterprises can have multiple departments, each with its own individual agents catering to different aspects of the organization. Since all agents are a part of the same organization, by integrating these into a Universal agent, you are providing a seamless and pleasant experience to the users.&#x20;

The following illustration depicts an "Acme Enterprise" Universal agent linked with independent virtual agents such as - Acme HR, Acme IT, and Acme Finance. Each department can continue to build these agents independently. The user can just use one agent - the  "Acme Enterprise" agent for all the queries across different departments:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FaHxSVAnYGwAkTh3LQ6Gs%2Facme-enterprise-UA-RN.png?alt=media\&token=8bb65d1a-5bd6-4ba6-a957-e00f356275f7)

### How does it work - Quick Overview?

Each agent linked to the Universal agents is referred to as a **Member agent**. When a user query is posted to a Universal agent, it routes the user’s intent to the appropriate **Member agent** for simple Q\&A or multi-turn conversations, renders member responses inline, and also manages the conversation context.&#x20;

The main purpose of a Universal agent is to centralize agent interaction across multiple departments, domains, or sectors. Users can use one agent to find responses to queries that span multiple sectors.

On the home page, the Universal agent can be identified and differentiated from other agents as the icon for the Universal agent has a soft shadow extending from it.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FScCVpEWW0SahmWlLMw77%2FScreenshot%202022-05-11%20at%2011.21.45%20AM.png?alt=media\&token=632dc9ac-fb22-455e-bd35-7bb0844bdf54)

### Create a Universal agent

{% hint style="info" %}
**Note**: Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
{% endhint %}

* In the Avaamo Platform UI, click the **Agents** option in the top menu, navigate to the **Development** tab, and select **Universal Agent** under **Create**.
* Specify the **Agent name**, **Agent description,** and **Agent avatar** for the Universal agent. Refer [Create a new agent ](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills)for more information on these fields.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fqe8No0BXtupqWv4GYEw1%2FScreenshot%202022-04-08%20at%203.38.00%20PM.png?alt=media\&token=c5108f76-23f3-4485-b4b0-f0c066947c4b)

### Open or view a Universal agent

Any newly created Universal agent is displayed on the **Agents** page. You can open or view a Universal agent by either clicking on the agent name, or clicking on the 3 dots under **Actions** for the Universal agent and selecting **View**.

### Delete a Universal agent

{% hint style="info" %}
**Notes**:&#x20;

* It is recommended to use this option with caution because when you force unlock an agent all the unsaved changes made by the other user is lost.
* In order to use this option, you must at least have edit permission on the agent.
  {% endhint %}

1. On the **Agents** page, click the 3 dots under **Actions** for the universal agent that you want to delete.
2. Select **Delete**. The agent is deleted and a confirmation box notifying you of the successful deletion of the agent is displayed.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fry3bi9C1Xq69R4oENixX%2FScreenshot%202022-05-10%20at%206.33.33%20PM.png?alt=media\&token=fed8b0fc-fada-4ea1-b4ef-78c96a0ae321)

### Make a copy of a Universal Agent

You can make a copy of your Universal agent using the **Make a copy** option. When you copy an agent, an exact clone of the Universal agent is created. This is similar to the **Make a copy** option available for independent agents. See [Make a copy](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/make-a-copy), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7Ch8poKEOQZVhWcD6bO0%2Fagent-copy.png?alt=media\&token=ba10d630-fcb6-415c-aa00-36d60eaa23e1)

You can always rename a Universal agent's copy by opening the agent and clicking the pencil icon (edit icon) next to the Universal agent's name.

### Skill in a Universal agent

A newly created universal agent has the **Greetings,** **Unhandled** and **Smalltalk** skills in it by default. You can configure this skill as required. See [Built-in skills](https://docs.avaamo.com/user-guide/how-to/add-skills-to-agent#built-in-skills), for more information.

{% hint style="info" %}
**Note:** Currently, the Frustration built-in skill is not available in the Universal agent. Frustration built-in skill requires configuring live agent option which is currently available only in the individual member agents.&#x20;
{% endhint %}

Besides the **Greetings, Unhandled** and **Smalltalk** skills, you cannot create any other skill as the purpose of the universal agent is to combine and centralize the tasks of multiple agents. Hence, instead of the option to add skills, you have the option to add member agents. See [Add member agents](https://docs.avaamo.com/user-guide/how-to/build-agents/create-universal-agent/add-member-agents) for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZBDOA1vRfBcOauWbClR2%2FScreenshot%202022-04-08%20at%203.56.03%20PM.png?alt=media\&token=a6d4d7a1-9214-4b6d-b5b5-e41c08c99fb4)

### Configure Universal agents

The following options are available for configuration in Universal agents:

* **Channels**: Currently, you can deploy a Universal agent only on a Web, Android, or iOS channel. See [Configure web channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/configure-web-channel) for more information.
* **Permissions:** The procedure to manage access and permission remains the same as applicable for any regular agent. See [Add permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information.
* **Persistent menu:** The procedure to add a persistent menu remains the same as applicable for any regular agent. See [Persistent menu](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-persistent-menu), for more information.&#x20;
* **Settings:** See [Define settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings) to understand how to manage general settings for your Universal agent.&#x20;
  * Note that `Max question repeat count` and `options in Advanced settings` are available only in the Member agents. These options are very specific on how individual agents prefer to handle the flow and hence are relevant only to the Member agents. This also provides better flexibility as it allows the member agents to handle these settings independently.
  * The **Dispatcher handler** option is available only for Universal agents. In this handler, you can provide a script that is called before probing the member agents. For example, you can use this handler for setting up conditions before probing the member agents. See [Dispatch handler](https://docs.avaamo.com/user-guide/how-to/configure-agents/define-settings#dispatch-handler), for more information.

### Connecting to a live agent

When the user requests to talk to a live agent, links to the live agent for each member agent are displayed. The user can select which member's live agent the user wants to talk to.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2ba4JQUPvjMCi8CvUGqv%2Facme-enterprise-talk-to-agent.png?alt=media\&token=74ed10c7-fa7f-4fcd-b97e-8d21a17406ec)

{% hint style="info" %}
**Notes**:

* The skill command `#end agent` is not applicable to Universal agents, since the live agent interactions are handled by individual member agents. See [Skill commands](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/skill-commands), for more information.
* A Live agent interaction in the Universal agents is an explicit action. It requires users to choose which live agent in the available member agents they wish to connect with. Hence, the live agent transfer rules such as "Silent switch" and "Switch to live agent for unhandled queries" are not applicable in the live agent interactions of a Universal agent. See [Live agent transfer rules](https://docs.avaamo.com/user-guide/how-to/configure-agents/switch-to-live-agent/pre-built-live-agent#live-agent-transfer-rules), for more information.
  {% endhint %}

### Debug Universal agents

All the options available to debug agents such as JS errors, Debug log, Storage, and Conversation history are available in the Universal agents too. See [Debug agents](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents), for more information.

{% hint style="info" %}
**Notes:**

* When a query is posted to a Universal agent, then the conversation is recorded in the Conversation history of the Universal agent and in the corresponding member agent from where the response is received.&#x20;
* JS errors, Debug logs, and Storage pages display details relevant only to the Universal agent.
  {% endhint %}

### Test Universal agents

You can test Universal agents using the Simulator and using Regression testing. Regression testing in Universal agents allows you to test queries with its member agents.

* See [Agent simulator](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/simulator), for more information.
* See [Regression testing in Universal agents](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing-universal-agents), for more information on the format that you can use to test Universal agents.

### Monitor Universal agent

The **Monitor -> Analytics** page in the Universal agent provides a unified analytics dashboard for monitoring the usage across the member agents along with the total queries, unhandled queries, and disambiguations. See [Analytics in Universal agents](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics-universal-agent), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FYt9KgSWyVVyovLIjarB4%2Fua-analytics.png?alt=media\&token=ff4aeba7-90a9-49ba-b054-f983f58cd94f)

### Key points&#x20;

* Currently, Universal agents do not participate in Agent life cycle stages.
* Currently, Universal agents can be deployed on the Web, iOS, and Android channels.
* Only supports conversation in the English language.
* Currently, [information masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking) is not supported in Universal agents. This implies that if you have a Universal agent with masking enabled for member agents, then even though the responses are masked in the member agents, the same responses remain unmasked in the Universal agent.
* You can also use `context.memberAgents` to get a list of all enabled member agents. The returned object is an array and you can use this information in any JS block of the Universal agent to get the member key and member name:&#x20;

```json
"memberAgents": [
    {
      "key": "home_loan",
      "name": "Home Loan"
    },
    {
      "key": "education",
      "name": "Educational Loan Virtual Agent"
    },
    {
      "key": "personal",
      "name": "Personal Home Loan Agent"
    },
    {
      "key": "vehicle",
      "name": "Vehicle Loan"
    }
  ]
```
