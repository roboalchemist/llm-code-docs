# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/intent-execution-sequence.md

# Intent execution sequence

When a user posts a query to an agent, the agent understands and classifies the input and then selects an appropriate skill to engage with the user. This article explains the **priority of intent execution** at the agent level and at the dialog skill level. Further, in the dialog skill, it illustrates post-processing and skill response flow.

## **At agent level**

Avaamo Platform evaluates all the intents and the intent with the best possible match is considered. There are three skills considered during intent execution - Dialog, Q\&A, and Smalltalk. Further, a Dialog skill can be invoked using Custom Code or Training Phrases. You can also create Pre-Unhandled Dialog skills. See [Add invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent), for more information.

The following is the priority of the intent execution at the agent level:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Ff80uzdefrC4rpMwHtmyw%2Fimage.png?alt=media\&token=40e5e8d6-8c02-4404-9869-aae9d118c3bf)

### **Key points**

* At any point during the intent execution, when the user query does not match with intent, then the agent responds with a selection of closest intent options, which is referred to as disambiguation.
* If there are multiple Q\&A with the exact same query, then the response from the first matching skill is displayed.
* If you add Smalltalk questions in Q\&A skill, then intent matching is affected. Hence, it is recommended not to use Smalltalk questions in the Q\&A skill. See [Skills](https://docs.avaamo.com/user-guide/overview-and-concepts/skills), to learn more about different types of skills and their purpose.

### Order of execution of custom code intents at **the** agent level

At the agent level, for the skills with custom code as intent type at invocation intent, the order of execution is the same as the order of the creation of respective skills. \
Example:&#x20;

* Skill A with custom code invocation intent - Created on 12th Dec 2021
* Skill B with custom code invocation intent - Created on 13th Dec 2021

In the above scenario, Skill A's custom code executes first and then followed by Skill B. However, you have the flexibility to define the weightage in the JS code as per your business requirement. You can assign weightage with any number between 0 and 1, for example, 0.2, 0.5. The custom code with the highest weightage is considered.&#x20;

**Example**: Consider that you can have two Dialog skills with pre-unhandled intent. One that invokes another skill in your agent to get the response and another with your business website search. Based on the response received from each one of these, you can infer, assign weightage, and return weightage. The custom code with the highest weightage is considered.

### **Switching between single-turn and multi-turn conversations**

Dynamic Q\&A, Smalltalk, and a Dialog skill with a single node, and Answers are referred to as **single-turn conversations**. These are one-off questions and answers.

‌Dialog skill with multiple nodes and flows that requires back and forth agent user conversation to accomplish a particular task are referred to as **multi-turn conversations**.&#x20;

‌In an agent-user interaction, it is quite common for a user to ask one-off questions or queries in between a Dialog multi-turn conversation. In such cases, the response if available for the one-off questions or queries is displayed. Post the response, when a user query is again posted, the conversation resumes from the node where it switched in the Dialog multi-turn conversation. This continues until a leaf node is reached in the Dialog skill.

‌**Example 1**:&#x20;

Dialog skill 1:&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F6c8IInAAhb8jJz8llX3R%2Fimage.png?alt=media\&token=8b3aa96d-39c4-4b51-bde5-075156b3a453)

‌

Dialog skill 2:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MUgg2wU3Zmr65VQtHxA%2F-MUghou25VEU3ViPxi0S%2Fintent-execution-example2.3.png?alt=media\&token=376a35e5-63ef-4425-9d0d-7fa941912443)

Consider the following agent-user interaction,&#x20;

1. User query -> "I want to find a doctor"
2. Dialog skill 1 is invoked and the control is now at node 1.1
3. User query -> "I want to refill my prescription"
4. Dialog skill 2 is invoked and the control is now at node 2.1
5. User query -> "Check for primary care physician in Boston area"
6. Conversation resumes at node 1.3 in Dialog skill 1

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbkAfUD7MMURcK77WAj3i%2Fimage.png?alt=media\&token=d53a9ed2-5094-433f-b8cf-6db0ab12ecca)

**Example 2**:&#x20;

Dialog skill 1:&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FEniyh2DFFIzwCzBBJqDr%2Fimage.png?alt=media\&token=2a7d923a-9285-4bbe-a494-d7ffbda7b3fc)

Dynamic Q\&A skill:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MUgg2wU3Zmr65VQtHxA%2F-MUgiFZJox1DxOTsAeag%2Fintent-execution-example2.2.png?alt=media\&token=c0f26ee1-91c3-4a1c-8fc4-80b0d362d7d9)

Consider the following agent-user interaction,&#x20;

1. User query -> "I want to find a doctor"
2. Dialog skill 1 is invoked and the control is now at node 1.1
3. User query -> "What are the symptoms of flu?"
4. Dynamic Q\&A is invoked and the response from Q\&A is displayed.
5. User query -> "Check for primary care physician in Boston area"
6. Conversation resumes at node 1.3 in Dialog skill 1

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fu4RWDGQxwkmfbiCwoAnt%2Fimage.png?alt=media\&token=7f043991-0e0d-4bcc-81e5-2c7e43b99cfb)

## **At Dialog skill level**

In a Dialog skill, you can add the following types of intent for a node in the flow - Training Phrase, Entity from Invocation Intent, System Intent, or Custom Code. See [Add user intent](applewebdata://74CCEB77-913D-409C-9C05-3B021CA2A30A/@avaamo/s/v5/~/drafts/-LzKmdbdxTA2YT4BO1xi/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent), for more information.&#x20;

If a Dialog skill is invoked at the agent level, then the Avaamo Platform executes the intent in the following priority within the Dialog skill:

{% hint style="info" %}
**Note:** This order of intent execution is applicable for nodes at the same level.&#x20;
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lzjtn0NTOO34emRGBX5%2F-LzkCvt8by1dopC7YDhT%2Fconcept-dialog-execution.png?alt=media\&token=c8c68778-7e3e-4560-ab87-14d3ce25ea7d)

{% hint style="success" %}
**Key Point**: At any point during the intent execution, when the user query does not match with intent, then the agent responds with a selection of closest intent options, which is referred to as disambiguation.
{% endhint %}

## Post-Processing and skill response execution

In a dialog skill, during intent matching, you can add a post-processing script that is executed after the intent is invoked, and before displaying the skill response. In the post-processing script, you can also include certain flow control statements such as "goto\_node" that allows you to navigate to different nodes in the dialog flow. See [Build skill responses using script and code](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill), for more information.

The following illustration depicts the post-processing and skill response execution flow:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lzjtn0NTOO34emRGBX5%2F-Lzk8pUUWhdAeEhff4MA%2Fconcept-intent-execution.png?alt=media\&token=2040195b-79db-48a1-9907-39047393a408)

{% hint style="info" %}
**Note**: Post-processing is where the intent execution still continues after matching the invocation intent; hence, when post-processing is enabled at the invocation intent, the entity skipping is no longer relevant and not evaluated.&#x20;
{% endhint %}
