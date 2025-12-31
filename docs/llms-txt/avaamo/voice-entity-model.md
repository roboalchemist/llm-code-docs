# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent/voice-entity-model.md

# Voice entity model

With the virtual world expanding, it is crucial to deliver virtual voice agents that are more sensitive, intuitive, and accurate. This helps is providing a more engaging experience with the user.

The first step towards enhancing accuracy is to understand the user query correctly. Hence, in any Conversational AI Platform, it is critical to extract and understand the entities accurately, since often that is the starting point of the conversation and it completes the user query. See [Entities](https://docs.avaamo.com/user-guide/overview-and-concepts/entity-types), for more information.

**Example**: In the user query, "Can you book an appointment for John today?", the following entities must be extracted accurately to proceed further with booking appointment:

| Entity | value |
| ------ | ----- |
| Name   | John  |
| date   | today |

Another example can be extracting the name and date of birth to authenticate a user for refilling a prescription.

If the information in the user query is understood correctly, then the entire conversation flow proceeds smoothly with the agent. This can lead to a good and pleasant user experience. With the **Voice entity model**, a virtual agent’s ability to extract precise entities during a conversation has considerably enhanced increasing conversational ease and experience.

### What is the Voice entity model?

Voice entity models are pre-built models to precisely detect relevant entities from the user's speech. It is a model built by using millions of actual user utterances combined with domain-specific data.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FG8L2LOWxpktcpva66Udb%2Fimage.png?alt=media\&token=078e11f7-be6c-4659-b43f-788647fb6f2e)

### Why use Voice entity models?

&#x20;Voice entity models help us to:

* Enhance the accuracy of interpreting user query and hence provides a good user experience
* Accelerates agent development, since the same voice entity models can be used in multiple intent interpretations without having to code.&#x20;

### When and where to use voice entity models?

Voice entity models are available when:

* You have deployed your agent in the C-IVR channel. See [C-IVR](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.
* You are building a conversational flow using Dialog skills. See [Dialog skills](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer), for more information.

### List of Voice entity models

The following are the most commonly used voice entity models:

<table><thead><tr><th width="169">Entity Model</th><th>Description</th><th>Spoken example</th><th>Written example</th></tr></thead><tbody><tr><td>Name</td><td>People Name including first and last name.</td><td>Matthew Brown</td><td>Matthew Brown</td></tr><tr><td>Email</td><td>Email Id</td><td>matthew at the rate avaamo dot com</td><td>matthew@avaamo.com</td></tr><tr><td>Spell Word</td><td>Spell Word</td><td>M a t h e w</td><td>Mathew</td></tr><tr><td>Date</td><td>Expected Date</td><td>twenty two of may two thousand and fourteen</td><td>22 of may 2014</td></tr><tr><td>Date of Birth</td><td>Expected date less than current date</td><td>twenty two of may two thousand and fourteen</td><td>22 of may 2014</td></tr><tr><td>Time</td><td>A specific time of day.</td><td>seven o'clock</td><td>7:00</td></tr><tr><td>Amount</td><td>A numerical value including whole numbers, fractions, and decimals.</td><td>twenty two</td><td>22</td></tr><tr><td>Age</td><td>A numerical value including whole numbers, fractions, and decimals.</td><td>twenty two years and six months</td><td>22 years and 6 months</td></tr><tr><td>Numbers</td><td>A numerical value including whole numbers, fractions, and decimals.</td><td>twenty two</td><td>22</td></tr><tr><td>Alphanumeric Sequence</td><td>A sequence of letters [a-z] and/or digits.</td><td>"a b c one two three"</td><td>ABC123</td></tr><tr><td>Alphabetical Sequence</td><td>A sequence of letters [a-z].</td><td>h q q g w r m y o</td><td>HQQGWRMYO</td></tr><tr><td>Digital Sequence</td><td>A digit sequence of any length.</td><td>one double oh two three</td><td>10023</td></tr><tr><td>Phone Number</td><td>A phone number, as used in the target locale.</td><td>plus one two one two five five five three seven one nine</td><td>+1-212-555-3719</td></tr><tr><td>Money</td><td>An amount of money with a currency unit name.</td><td>twelve dollars and eighty four cents</td><td>$12.84</td></tr><tr><td>Postal Code</td><td>A postal code, as used in the target locale.</td><td>k one a zero b one</td><td>K1A0B1</td></tr></tbody></table>

### How to use Voice entity models?

Voice entity models are available where you capture user intent in a Conversational-IVR flow using Dialog skills.&#x20;

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can build and manage dialogs (conversational flow) immediately after creating a Dialog skill. See [Create new Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill), for more information.

* If you wish to edit skills in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent.&#x20;

    See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
  * In the **Agent** page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;

* The quality of the intents and their training determines the quality of the agent's accuracy in understanding the user queries. See [Design skill](https://docs.avaamo.com/user-guide/how-to/design-skill#intent-and-training-phrases), for more information on intent training guidelines.
  {% endhint %}

* In the **Dialog skill** page, click **Edit** to unlock the skill&#x20;

* Click the **Implementation** option in the left navigation pane. A dialog flow tree is displayed.&#x20;

* Add user intents by creating a new node in one of the following ways:
  * Click the **plus (+)** icon to add a new user intent and skill response in the node below the current node.
  * Click the **fork** icon to add a new user intent and skill response as a forked branch to the current node.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ma7bIuRq5MKOQJmzUGc%2F-Ma80SBNObJgy5nLYK_I%2F5.7-dialog-add-user-intent.png?alt=media\&token=f7fcc81f-4e3e-4252-a631-32b3b94aaba9)

* Click the red call-out bubble above "Add agent Response" to add an Intent and specify the following details:
* In the intent where you expect the user utterances to be of any of the voice entity models, select the required voice entity model from the **Voice entity model** list. See [Best practices](#best-practices), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FdkSKhQ5usfw0fDGeJrRC%2Fimage.png?alt=media\&token=f868ca85-6c2c-4e23-89a4-163f1c60e455)

* Click **Save**.&#x20;

### Best practices

* It is recommended to design the conversational flow to use only a single voice entity model per intent. This helps in improving the accuracy of user utterance recognition.
* It is recommended to use the Voice entity model instead of [Voice hints](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/voice-hints) as applicable. Voice entity models are more robust and help significantly increase the accuracy of user utterances.
