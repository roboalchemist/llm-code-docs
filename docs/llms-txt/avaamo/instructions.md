# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent/instructions.md

# Instructions

**Instructions** define how user input should trigger a specific conversation path. Instead of relying on example utterances alone, instructions let developers and designers describe intent conditions in clear, human-readable statements that the system evaluates via natural language understanding.

Instructions replace or complement traditional training phrases by providing the system with intent guidelines that guide its decision on when to invoke a dialogue flow or node.

#### What are the instructions

Instructions are declarative **intent conditions** written in natural language that describe when a flow or specific node should be triggered.

Unlike rigid training phrase lists, instructions are evaluated dynamically by the conversational engine to determine the appropriate invocation, enabling flexible intent matching across diverse user expressions.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FhxoSb0wPGVdGnAC8LLyN%2FScreenshot%202026-01-15%20at%2012.01.13%E2%80%AFPM.png?alt=media&#x26;token=6b36c45c-4903-4c27-8346-b195722ea453" alt=""><figcaption></figcaption></figure>

### How to use instructions?

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can build and manage dialogs (conversational flow) immediately after creating a Dialog skill. See [Create new Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill), for more information.

* If you wish to edit skills in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent.&#x20;

    See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;

* The quality of the intents and their training determines the agent's accuracy in understanding user queries. See [Design skill](https://docs.avaamo.com/user-guide/how-to/design-skill#intent-and-training-phrases), for more information on intent training guidelines.
  {% endhint %}

* In the **Dialog skill** page, click **Edit** to unlock the skill&#x20;

* Click the **Implementation** option in the left navigation pane. A dialog flow tree is displayed.&#x20;

* Add user intents by creating a new node in one of the following ways:
  * Click the **plus (+)** icon to add a new user intent and skill response in the node below the current node.
  * Click the **fork** icon to add a new user intent and skill response as a forked branch to the current node.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ma7bIuRq5MKOQJmzUGc%2F-Ma80SBNObJgy5nLYK_I%2F5.7-dialog-add-user-intent.png?alt=media\&token=f7fcc81f-4e3e-4252-a631-32b3b94aaba9)

* Click the red call-out bubble above "Add agent Response" to add an Intent and specify the following details:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mb13EdXe79533aZbVXP%2F-Mb13ViuJ4MB7uMvfyq5%2F5.7-dialog-user-intent-custom-code.png?alt=media\&token=42546463-239a-46ff-82b4-48d28e4871c2)

<table><thead><tr><th width="156.90434698745716">Parameters</th><th width="342.1725340776212">Description</th><th align="center">Maximum length</th></tr></thead><tbody><tr><td>Intent name</td><td><p>Indicates the name of the intent. </p><p></p><p>Each intent name must be unique within the skill.</p></td><td align="center"><p>192 </p><p>characters</p></td></tr><tr><td>Intent key</td><td><p>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the intent name. </p><p></p><p>By default, a key is automatically generated for you. Click <strong>Edit</strong> to update the key to any user-friendly identifier. Note that the intent key must be unique within the skill.</p><p></p><p>Supported characters: Alphanumeric and underscore</p><p></p><p>It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information. You can use this in any <a href="../../../customize-your-skill/reference-library/flow-control">JS code customizations (Flow control)</a>, <a href="../../../../../build-agents/test-agents/regression-testing">regression testing</a>, and <a href="../../../../../build-agents/monitor-and-analyze/query-insights">query insights</a> for getting a closer look at the user conversations with the agent.</p><p></p></td><td align="center"></td></tr><tr><td>Intent type</td><td>Indicates the type of user intent. Select <strong>Instructions</strong>.</td><td align="center">N/A</td></tr><tr><td>Custom intent handler</td><td>In the instruction text field, enter a natural language description of when this intent should be triggered.</td><td align="center">N/A</td></tr></tbody></table>

* Click **Save**.&#x20;
