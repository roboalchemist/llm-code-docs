# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/train-your-agent.md

# Train your agent

For an agent to respond to user queries, each intent must be trained with specific sentences that are used as representative phrases for user queries. This set of sentences is referred to as the Training data set.&#x20;

One of the main challenges of training your agent is predicting the possible set of queries users might ask your agent. Training your agent, hence, is an iterative and continuous process, and training with the right amount of intents and phrases is essential for a good user experience. It is a process of teaching your Avaamo agent how to respond to the user's intentions.&#x20;

The following diagram broadly illustrates the recommended guidelines to get started with your agent development:

![](https://lh3.googleusercontent.com/yhMgi0V40IhMrkd-V9w3wKsmEvqLDLWUXhQudiZVXYQb0OBhBKaG5iMtQlbiJSOi3CU1ziq0y7ubYpplwqTbNklkOBFzUWCXEamCnrPo3xT7jRwYIEhohe317iMwIexFbO86pjSI)

{% hint style="success" %}
**Note**: Throughout your agent development process, it is recommended that you refer to suggested best practices and guidelines. This can help you to increase agent accuracy and provide a good user experience.
{% endhint %}

### **Bootstrap**

* Get a list of possible user queries for your agent.&#x20;
* Group the user queries with common intents.&#x20;
* Identify the skills from the intent. An agent is a container of skills, each specialized to understand and handle a specific task in the user conversation flow. **Example**: In the **Pizza agent**, you can create an "Order Pizza" skill responsible for handling all pizza orders, similarly you can create a "FAQ" skill to handle all the Mac Pizza FAQs.  See [Skills](https://docs.avaamo.com/user-guide/overview-and-concepts/skills), for more information.&#x20;
* Classify the intents into one of the following buckets - Training phrases, Entity, System entity, or Custom code. See [Intents](https://docs.avaamo.com/user-guide/overview-and-concepts/intents), for more information.&#x20;
* Train your agent with these initial sets of queries to bootstrap your agent. See [Build agents](https://docs.avaamo.com/user-guide/how-to/build-agents), for more information.

### Share and test

* With the initial set of queries trained in your agent, self-test your agent to see if the intents and entities are getting identified and extracted properly. See [Test your agent](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents), for more information.
* It is strongly recommended to create a thorough regression test file and continuously improve at each stage of agent development.&#x20;
* Share your prototype agent with test users. This helps to further train your agent with real user queries rather than speculations.&#x20;
* Avaamo Platform allows you to promote your agent to different stages of the agent life cycle and parallelly continue the development phase. See [Agent life cycle](https://docs.avaamo.com/user-guide/how-to/plan-your-development-process-agent-life-cycle), for more information on how you can use the Avaamo Platform effectively in a structured release management process.

### **Review and monitor**

* Review all the user conversations, especially those that are unhandled or went as disambiguous by your agent. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/debug-agents#using-conversation-history) and [Query insights](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/query-insights), for more information on these tools. They can help you sift through the conversation quickly.&#x20;
* Monitor your agent using **Analytics**. See [Monitor agents](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze), for more information.

### Improvise

* Use [Agent diagnostics](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/agent-diagnostics-deprecated) and [Unhandled query analyzer](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/query-analyzer-deprecated) tools in the Avaamo Platform to further analyze the quality of the agent's training data. Contact Avaamo Support, to enable these tools for your account.&#x20;
* Train your agent using the details from the tool to further improve the prediction accuracy. Continue with Step 2.
