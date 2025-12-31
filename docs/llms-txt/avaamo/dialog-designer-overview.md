# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/dialog-designer-overview.md

# Flow designer - Overview

The **Flow designer** is an intuitive conversational modeling tool that enables you to build multi-turn conversational flows quickly with user intents and responses. The **Designer** provides a comprehensive set of content templates such as surveys, forms, carousels, and rich media cards to create beautiful and engaging conversational interfaces.

## Components of a Flow designer

The following diagram illustrates the main components of the **Flow designer**:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MaSoWZYn7Vd-1IIFevO%2F-MaSobo8nMwVfZm-LXdi%2F5.7-flow-designer.png?alt=media\&token=d774fb64-cd48-4909-9aa9-a526a0be0c88)

## Scenario

Consider that you are building an **Order Pizza Dialog skill** in a Pizza agent that is responsible for taking the user through a conversation for capturing the required data to order a pizza.&#x20;

1. Create an entity type - Pizza types with "veg" and "non-veg" entity values. See [Add entity type](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/add-new-entity-type), for more information.
2. Start by adding invocation intent such as "I want to order veg pizza" to invoke the skill. See [Add invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent), for more information.
3. Change default greeting message of the Dialog skill to "We have a wide variety of freshly baked pizzas. Would you like to order veg or non-veg pizza?". See [Change default greeting message](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/change-default-greeting-message), for more information.
4. The next step is where you build the flow by adding nodes in the Flow designer.

## Invocation intent key

This is the intent key provided at the time of creating the invocation intent. See [Add invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent), for more information.&#x20;

You can also use the intent key to transfer the conversational flow to a different intent based on your business requirement. See [Advanced settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings) and [Flow control](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control), for more information.

## Node

This is a primary component of the Flow designer. A node consists of user intent and a corresponding skill message. **Example**: Consider the following flow in the Order pizza skill.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MaSoWZYn7Vd-1IIFevO%2F-MaSobo8nMwVfZm-LXdi%2F5.7-flow-designer.png?alt=media\&token=d774fb64-cd48-4909-9aa9-a526a0be0c88)

* After the skill is invoked, the first message that is displayed is "We have a wide variety of pizza. Would you like to order veg or non-veg pizza?"
* When the user specifies the intent as "Veg" or "Non-Veg" pizza, then the corresponding message from the agent is to ask for toppings the user wishes to add to the pizza. The skill message here can be - "Great. Let's add some toppings. You can say something like onion, tomato, cheese, pepperoni, or a combination of these."&#x20;
* The intent "Veg" or "Non-Veg" pizza together with the skill message is referred to as a **node**.

### Creating a node

You can create a node in one of the following ways:

* **Using the plus (+) icon**: This creates a node below the current node.
* **Using the fork icon**: This creates a node as a forked branch to the current node. Use this when you are expecting different user intents for the same skill response.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MaSomHrNv7UUz3aXO2H%2F-MaSqlsuv5NapHI-Gdcf%2F5.7-flow-designer-add-node.png?alt=media\&token=e35fff1c-1a44-4c5b-a74d-f7467cd870ee)

**Example**: Considering the scenario of Order pizza skill, after the agent displays a message "We have a wide variety of freshly baked pizzas. Would you like to order veg or non-veg pizza?.", the user response can be "veg" or "non-veg". To implement this, you can create a node below the current node using the plus(+) icon to capture the user intent and corresponding response.

### User intent

User intent is where you capture the intention of what the user wishes to do. In the Flow designer,  user intent is indicated using a red call-out bubble above "Add agent Response".&#x20;

You can use one of the following options to specify the user intent - Training Phrase, Entity from Invocation Intent, System Intent, or Custom Code. See [Add user intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent), for more information.&#x20;

**Example**: Considering the scenario of Order pizza skill, you can create a node with a user intent using the existing entity "Pizza types"&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MaSomHrNv7UUz3aXO2H%2F-MaSrSrRucgx8gyWo5sC%2F5.7-flow-designer-add-user-intent.png?alt=media\&token=8e5e30b9-e640-4cb3-af3f-5c100c1a2a38)

Each user intent is associated with a unique intent key that is specified at the time of creating the intent. See [Add user intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent), for more information. Each user intent within a skill is uniquely identified using the following notation "I *<\<intent\_key>>*" **Example**: "I pizza\_types".&#x20;

{% hint style="info" %}
**Note**: The intent key for a forked branch node is the same for each child intent in the branch node.
{% endhint %}

You can also use the intent key to transfer the conversational flow to a different intent based on your business requirement. See [Advanced settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings) and [Flow control](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control), for more information.

### Skill response

A skill message in the Flow designer is where you configure a response for the corresponding user intent. In the **Flow designer**, skill response is indicated using a red call-out bubble above "Add agent Response".&#x20;

You can add rich responses to user queries in a Dialog skill. This can be as simple as a text message, card, quick reply, or complex JavaScript. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information.

**Example**: Considering the scenario of Order pizza skill, after the user chooses a Pizza type - "veg" or "non-veg", you can proceed further in the conversational flow by asking the user to choose some toppings for your pizza:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MaSrV7c51IGPAGPoOab%2F-MaSs0z-IKWnQwjpt5Lp%2F5.7-flow-designer-add-agent-response.png?alt=media\&token=68ff6b97-7390-4d11-8a27-424015302fd1)

## Next steps

Continue to build Pizza agent conversational flow by adding user intents and skill responses:

* Explore the various ways in which you can add user intents. See [Add user intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent), for more information.
* Explore the different types of skill responses such as card, carousel, quick reply, Listview. See [Build skill responses](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information. &#x20;
