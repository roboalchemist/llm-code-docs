# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/design-agents.md

# Design agents

An agent is synonymous to a "human agent". Similar to a human agent that has or is trained with different skills for responding to user queries, an agent is a "container of skills", each specialized to understand and handle a specific task in the user conversation flow. When a user posts a query to an agent, the agent understands and classifies the input (both text and voice) and then selects an appropriate skill to engage with the user.

Agents help you handle various use cases. The Avaamo platform equips you to build agents that suit all your business needs. Understanding the purpose of your agent and designing the agent in the right way with all the recommended best practices and guidelines is essential for a good user experience.

## 1. Define the purpose of the agent

Here are a few questions that can help you define the purpose of your agent:

* Why do you want to build an agent?
* Who is your target audience?
* How will your customers discover your agent?
* What kind of use cases would you want your agent to handle?
* What would you define as a successful agent interaction?
* Does your agent reflect your company's brand?
* Do you need to integrate the agent into existing systems?

## 2. Knowing your audience

* Understand that the needs and wants of your audience are important for the success of any agent.&#x20;
* You need to know your customers — the demographics they belong to, and the kind of questions they might have.&#x20;
* You can study previous interactions and equip your agent to respond to queries that they might frequently ask.&#x20;
* Knowing your customer base well enough will determine the success of your agent.

## 3. Design your agent right

With well-defined business requirements in place, you can get started on designing your agent.&#x20;

* The Avaamo platform allows you to quickly focus your efforts on developing a framework for the agent. Here, you start visualizing and incorporating the use cases and define a user journey.
* Ensure that you build the journey in such a way that it makes for the best user experience. Focus on developing just the framework, you can improve that later by adding Javascript or integration services codes. Use in-line intents, to begin with.
* The framework itself can be used to demonstrate the agent to the users or the proxy users to ensure that the agent design is as expected.
* Keep this question in mind always: "is the agent intuitive for someone who is using the agent for the first time?". If not, then redo, test, and review.

See [Build skills](https://docs.avaamo.com/user-guide/how-to/build-skills) and [Build agents](https://docs.avaamo.com/user-guide/how-to/build-agents), for more information.&#x20;

## 4. **Add a good greeting message**

Creating a good first impression of your agent with users matters and will help to engage the users positively.

* Your welcome message is designed to help your users understand that the users are talking to an agent, and it is one of the most important messages.&#x20;
* You can add the functionality of the agent to its welcome message.&#x20;
* By listing its functionality upfront, the agent keeps your users from being disappointed and gives them ideas and instructions on how to engage further.

In this greeting message example of a medical assistant, notice how the functionalities of the agent are listed upfront. This guides and eases user navigation and also provides a good first impression to the users:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FUHvceZ4EEgSxbNU5tPnb%2Fimage.png?alt=media\&token=799af1c6-eb2f-4d78-a363-51b8f2971240)

See [Greeting skill](https://docs.avaamo.com/user-guide/how-to/add-skills-to-agent#greeting-skill), for more information.

## 5. Entity types vs Dictionaries vs Training variations

* **Entity types**: An entity type is a named collection of similar objects such as states in a country, all pediatricians, a list of product names, or data types (Date, Email, Location). Each entity type contains one or more values. **Example**: An entity type named "US City" contains values - Los Altos, San Francisco, Los Angeles. See [Entities](https://docs.avaamo.com/user-guide/overview-and-concepts/entity-types), for more information.
* **Dictionaries**: A dictionary, in the agent, is a collection of words or phrases that hold a specific meaning to your business. **Example**: You are creating an HR agent regarding the employee bonus policies. Here, EB (Employee bonus), QEB (Quarterly Employee Bonus), and such terminologies can be added to the dictionary. See [Dictionaries](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-dictionaries), for more information.
* **Training variations**: For an agent to respond to user queries, each intent must be trained with specific sentences that are used as representative phrases for user queries. This set of sentences is referred to as the Training data set. See [Intent and Training Data](https://docs.avaamo.com/user-guide/overview-and-concepts/intents), for more information.

When you are deciding on whether you must create an entity type, dictionary, or training variations, consider answering these questions:&#x20;

| What are the values I have?                                                                                                             | Where should it go?                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Are the values a logical grouping of nouns e.g. scheme name, which holds the same meaning across all training variations for the agent? | Consider defining these as entity types and values. See [Add entity types to agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent), for more information.                                                                                                                                                                                                                                                     |
| Are these values not typical dictionary words but hold specific meaning to your business?                                               | <p>Consider defining these in the dictionary. </p><p>See <a href="configure-agents/add-dictionaries">Add dictionaries</a>, for more information.</p>                                                                                                                                                                                                                                                                                             |
| Are these just regular words for which you have given some alternate synonyms?                                                          | For example, eat -> grab, gobble, drink. Consider adding them as training data variations for the intent. See [Add invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent) and [Add user intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent), for more information. |

**Example**: The following table lists a few use cases and corresponding categorizations:

| Use case                                                     | How to define them? |
| ------------------------------------------------------------ | ------------------- |
| AEM: Adobe Experience Manager                                | Dictionaries        |
| KYC: Know your customer                                      | Dictionaries        |
| Policy: Plan, Strategy                                       | Training variations |
| Correction: change, updated                                  | Training variations |
| Ticket type: Incident, Request Item, Change Request, Problem | Entity type         |
| Account type: Savings, Current, Recurring, Fixed             | Entity type         |

{% hint style="info" %}
**Note**: Spell correction is performed on words in the user query by identifying and correcting the phrase that is closest to the training data. Hence, only those words that are a part of either part of training data, entities, or dictionary are spell-corrected.
{% endhint %}

## **6: Prepare for ambiguities and misunderstandings**

Program your agent to deal proactively with any ambiguities and misunderstandings. If your agent detects various entities and is unsure of a response, have your agent ask related questions, suggest a possible next step, and remedy misunderstandings. This way, if your agent's answer is not satisfactory, your users will have several other questions to choose from, and this will not result in an interrupted agent conversation flow.<br>

Anticipating follow-up questions can go a long way is building confidence with the user and navigating through the conversation flow. Leverage the Platform's capability to gather a set of closely matched intents related to a user’s query in a particular context. This helps you to anticipate follow-up questions users might have. Consider showing these in a section such as "Here’s related content" or as "Other Common Questions". This feature can help in:&#x20;

* Reducing false positives and providing more options from a similar set of responses already available in the agent.&#x20;
* Providing a pleasant user experience where the agent attempts to provide the best possible answers from all possible available options in the agent.
* Providing guided navigation allows the user to explore more options.

You can show the best answer and additionally show three "common questions" from the curated set of responses that are related to the user query.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F64EMgdUtvTe1wz0BUxMn%2Fimage.png?alt=media\&token=a6d9fa56-6958-4fac-a0bf-61e766a7f537)

See [how to show ambiguous intents](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/show-ambiguous-intents), for a sample scenario and example.

## **7: Take advantage of the auto-complete (Type-ahead) feature**

Leverage the auto-complete feature to reduce false positives and significantly improve accuracy. By presenting the user with a list of available options, the user likely selects one of those options for which accurate curated responses are already available in the agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FinsEXbgr2rCRHxn7Hpqe%2Fimage.png?alt=media\&token=5f41025b-b04c-437d-99bc-8e6269d7bdce)

See [Auto-complete in web channel](https://docs.avaamo.com/user-guide/how-to/configure-agents/deploy/web-channel#example-3-auto-complete), for more information.

## **8: Test rigorously**

One of the key factors for the success of any agent is thorough testing. Continuous testing is required for each skill to reach the maximum level of accuracy. These skills must be reviewed from time to time and improvements can be made to enhance the experience of the interaction between your users and the agent.

See [Test agents](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents), for more information.

## 9. Detect frustration and handle it

Unhappy customers are inevitable. The goal of the agent is not to wear them down or impress them with their smarts. The goal is to respond to the queries in a satisfactory manner. Design your agent to detect and understand dissatisfaction and frustration in the customer's tone. Handle the situation by integrating human intervention.

See [Frustration](https://docs.avaamo.com/user-guide/how-to/add-skills-to-agent#frustration) and [Unhandled skills](https://docs.avaamo.com/user-guide/how-to/add-skills-to-agent#unhandled-skill), for more information.

## 10. Continuously train the agent

Once the agent is deployed, closely monitor the initial interactions, and gather feedback to understand how your users are interacting with the agent. Gathering these use cases and adding them to your agent's conversation flow can improve user interaction over time.

Once you deploy the agent, ensure that you monitor the agent and its unhandled queries. You can categorize these unhandled queries into three categories:

1. Other variants of user requests for services that the agent already supports. These variants have to be added to the agent's training data.
2. New service requests that users are making of the agent, that you want to add to the agent's scope as part of a roadmap. These will be added over time when you have developed new intents and responses in your agent.
3. Service requests that you feel are totally out of scope for the agent. For example, a user may query the agent for the latest football score, while your agent may have nothing to do with sports. These may be discarded since you feel your agent should not be servicing these requests. Be helpful and while telling the user these questions you cannot help with, please suggest frequently asked questions so that users are reminded of the purpose and scope of your agent.

See [Monitor agents](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze), for more information.

While developing your agent, take into account the various channels that your agent would be deployed on. Understand the specific impacts of those channels on your agent development.

As an example, Facebook Messenger has many limitations on message sizes that you will want to incorporate into your agent for the best experience across channels.

## <img src="https://lh4.googleusercontent.com/CSqmMMpvN9MCCroadZb2rqkAUSUEydJdQ5PlRQcPjf1eSF2rFwOwfRRVJWdTyuxBCQqkK1zYi7D1YQwT3-MLCiP7lL9ZL7czfhZQ9RcOup4igOz4cm6MDrvov5QdpMilYiwx78Rm" alt="" data-size="line">**Don’ts**

* Do not overlap the purpose of the agent. Keeping your requirements clear always helps you to design your agent effectively. If you have two sets of requirements that serve different purposes, consider creating two different agents.&#x20;
* Do not overdesign or clutter your agent. Start with the basic set of requirements and test it. Iteratively build over the basic framework.
* Do not ignore JS Errors in your agent. Periodically plan to check for JS Errors and clean it up. See [JS Errors](https://docs.avaamo.com/user-guide/how-to/debug-agents#using-js-errors), for more information.
