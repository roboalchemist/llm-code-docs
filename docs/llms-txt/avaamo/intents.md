# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/intents.md

# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/intents.md

# Intents and Training Data

An **intent** is an action in the user query that indicates what the user wishes to do.&#x20;

As you build your agent and skills, you must train the agent to understand the user queries. Intents and training data are the basic building blocks of training your agent.

The quality of the intents and their training determines the quality of the agent's accuracy in understanding the user queries. Creating the right number of intents with the right number of training data samples for each intent is essential for a good user experience.&#x20;

### Intent

In simple terms, the intent is a user's intention to act on something. For example, consider the following sentences about weather details:

```
Show me yesterday's weather.
How cold will it be tonight in Boston?
```

Here, all sentences are related to the same intent "Find Weather" expressed in different ways. Now, consider another example with the following user queries about insurance claims:

```
I met with an accident. Can you help me create a new claim?
I want to report a claim.
Would you help me with a new claim?
```

All sentences are related to the same intent "Report claim" expressed in different ways.

{% hint style="success" %}
**Key Points**:&#x20;

* A single skill can understand and respond to one or multiple user intents. **Example**: A "Reset password" Dialog skill that responds to only one intent of steps required to reset password or a Q\&A skill that can comprise of multiple questions and responses.
* As a best practice, it is recommended to name your intents with a combination of a verb and a noun that helps to identify the action and the object on which the action is performed. **Example**: Order Pizza, Find weather, Report claim.&#x20;
  {% endhint %}

### Training data

For an agent to respond to user queries, each intent must be trained with specific sentences that are used as representative phrases for user queries. This set of sentences is referred to as the **Training data set**.&#x20;

{% hint style="success" %}
**Key Points**:&#x20;

* Training data are not user queries. User queries are queries posted by the user to the agent. Training data is a set of sentences that are used to train the intent for responding to user queries.
* Training data are also referred to as Training phrases or Training utterances.
  {% endhint %}

**Example**: The following table lists a few examples of intent with training phrases:

<table><thead><tr><th>Intent</th><th width="553">Training Phrases </th></tr></thead><tbody><tr><td>Order Pizza</td><td>I want to order veg cheese pizza with French Fries.</td></tr><tr><td>Find weather</td><td>I want to check Boston's weather tomorrow.</td></tr><tr><td>Report a new claim</td><td>I want to report a claim for policy number 08765434546.</td></tr></tbody></table>

{% hint style="success" %}
**Key Points**:&#x20;

* An intent represents a specific named action identified by its training data.&#x20;
* See [Intent and training phrases](https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill#intent-and-training-phrases), to learn about the recommended best practices.
  {% endhint %}

### Types of Intent

The following lists different types of intents that can be specified in the Avaamo Platform:

<table><thead><tr><th width="214">Intent Type</th><th width="548.3526570048309">Description</th></tr></thead><tbody><tr><td>Training Phrases</td><td><p>These are the inline user intents (utterances or phrases) in the conversation flow. </p><p></p><p><strong>Example</strong>: I want to order pizza, I want to order a large cheese pizza.</p></td></tr><tr><td>Entity</td><td><p>These are intents with <a href="entity-types">entities</a>. </p><p></p><p><strong>Example</strong>: Consider that in the Order Pizza skill, the first message asks the user for the type of pizza (veg or non-veg). In return, you can specify an intent with these entities to process the user response and proceed further in the conversation flow.  </p></td></tr><tr><td><p></p><p>System Intent</p></td><td><p>These are the system intents with pre-defined training phrases already available in the platform. </p><p></p><p><strong>Example</strong>: Consider that you wish to respond to the user's frustration by transferring to a live agent or via collecting feedback. You can create a user intent with frustration system intent and add a skill response to transfer to a live agent.</p></td></tr><tr><td><p></p><p>Custom Code</p></td><td><p>These are intents with custom JavaScript code. </p><p></p><p><strong>Example</strong>: You can create a custom intent with a regular expression to match the pizza order number entered by the user. Alternatively, you can also create an entity with a regular expression. </p></td></tr><tr><td>Pre-unhandled</td><td>You can define the pre-unhandled intents for the agent to give users a few more options and help with the query instead of just responding with an unhandled intent.  </td></tr><tr><td>Unhandled </td><td><p>By default, for all the user queries that do not get matched to any predefined intents in the agent, the agent has a node within the flow to respond to the user's query with statements like -</p><p><em>"I am sorry I do not understand."</em><br><em>"I am sorry. I don't have an answer for that."</em></p><p>These classify as unhandled queries as ideally, the user's query goes unanswered.</p></td></tr></tbody></table>

See [Add user intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent), for more information.

{% hint style="info" %}
**Note**: The quality of the intents and their training determines the quality of the agent's accuracy in understanding the user queries. See [Design skill](https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill), for more information on intent training guidelines.
{% endhint %}

### Disambiguation

When a user intent does not match a specific intent, the agent responds with a selection of closest intent options, referred to as a disambiguation intent. If the user selects and responds with one of the options, the query is successful else it is categorized as a failed disambiguation query.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FWjnnY60JczYznqOFrfI0%2Fimage.png?alt=media\&token=73832eaa-8b61-4400-9d94-1f40bdf950c9)

Here, we have queried "order". The agent has responded with the intents that support "order". This is categorized as disambiguation. If you select one of the above options, the query is a successful disambiguation query and if you select "none of these" then it is a failed disambiguation query.

{% hint style="info" %}
**Notes**:&#x20;

* The top 5 closest disambiguations is displayed to the user.
* Smalltalk does not participate in disambiguation.
  {% endhint %}

### Wild card

You can add a wild card for the agent to avoid responding with unhandled intent. These wild card intents are saved with no training data. **Example**: In scenarios, where you are validating certain user input, you can handle invalid inputs in a wild card. In the wild card, you can, for example, navigate to specific nodes in the flow. If you are not using a wild card, then the invalid inputs go to an unhandled node. The wild card allows developers to have better flow control for handling such cases.
