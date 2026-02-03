# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent.md

# Add invocation intent

An **invocation intent** is an intent or a training phrase that invokes the skill when added to an agent. You can also add a custom JS code to invoke your intent if required.

As you enter training phrases for the invocation intent, the platform automatically extracts the slots and includes all the entities in your skill. Note the points:

* The color of the phrases in the user utterances matches with the slots for easy identification.&#x20;
* In cases, where the slots are not extracted, you can right-click on the word or phrase to select and add slots manually. Note that you can manually extract only those slots for which the entities are already added in the Invocation intent.
* In cases where you need any complex or custom extraction, then you can use the regular expression entity type. See [Add entity types to agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent) and [examples](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/example-pizza-agent), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ma4D1bNLbh_rRZXnqvS%2F-Ma4E8THSD1qjMhffJnK%2F5.7-dialog-skill-invocation-intent.png?alt=media\&token=4973bb5e-7599-4b31-be33-9d07aebbdd93)

{% hint style="success" %}
**Key Point**: You can also create a post-processing script in the Dialog skill.
{% endhint %}

## **Adding invocation intent**

Consider that you wish to create an Order skill to place a pizza order in a Pizza agent.&#x20;

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can build and manage dialogs (conversational flow) immediately after creating a Dialog skill. See [Create new Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-dialog-skill), for more information.
* If you wish to edit skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * In the Agent page, navigate to the Skills option in the left navigation menu and click the required skill.&#x20;
    {% endhint %}

**To add an invocation intent**:

* In the **Dialog skill** page, click **Edit** to unlock the skill.
* Click **Invocation intent** in the left navigation menu.
* Specify the intent key, type, training phrases, and post-processing details in the invocation intent and click **Save**:

### 1. Intent key

Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the intent name. By default, a key is automatically generated for you. You can also update the key to any user-friendly identifier.&#x20;

**Supported characters**: Alphanumeric and underscore

It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See [Snake Case](https://en.wikipedia.org/wiki/Snake_case), for more information. You can use this in any [JS code customizations (Flow control)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control), [regression testing](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing), and [query insights](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/query-insights) for getting a closer look at the user conversations with the agent.

Note that the intent key must be unique within the skill.

### 2. Intent Type

Specify the type of intent:

* **Training phrases**: Use this if you wish to specify training phrases as invocation intent.
* **Custom code**: Use this if you wish to specify a JS as a custom intent instead of training phrases.&#x20;
* **Pre-unhandled**: Use this if you wish to specify a JS that is executed before executing the Unhandled node.&#x20;

### 3. Training Phrases

Specify variations of user utterances that invoke this skill. This is enabled if you select Intent type as Training phrases. As you enter training phrases for the invocation intent, the platform automatically extracts the slots and includes all the entities in your skill. Note the points:

* The color of the phrases in the user utterances matches with the slots for easy identification.&#x20;
* In cases, where the slots are not extracted, you can right-click on the word or phrase to select and add slots manually. Note that you can manually extract only those slots for which the entities are already added in the Invocation intent.
* Click the slots to rename, if required.

{% hint style="info" %}
**Notes**:&#x20;

* You can specify Training phrases upto 300 characters.
* If you have specified intent type as Training phrases and if you require additional entities in the flow, then it must always be a part of the training data in the invocation intent.&#x20;
  {% endhint %}

{% hint style="success" %}
**Key Points**:

* If you want training data that must match specific and generic queries, then it is recommended to provide generic training data. Example: If you wish to match "I want my fund value" and "I want fund value", then it is recommended to use "I want fund value" in the training data.
* You must retain only those entities that are required and delete the ones if not needed.
  {% endhint %}

### 4. Custom Intent Handler

Specify a custom JS for invoking this skill. This is enabled if you select the Intent type as Custom code. Note that goto\_node is not supported in the custom intent handler, you must return true or false in this handler. If the code returns true, then it takes through the flow specified in the skill.

{% hint style="info" %}
**Note**: If you have specified intent type as Custom code, then you can add required entities to the skill using the Add entity option. See [Entities](#7.-entities), for more information.
{% endhint %}

### 5. Pre-Unhandled Intent Handler

Specify a JS that is executed just before the Unhandled node. This is enabled if you select Intent type as Pre-unhandled. Note that goto\_node is not supported in the pre-unhandled intent handler, you must return true or false in this handler. If the code returns true, then it takes through the flow specified in the skill.

Few examples include:

* Invoke a specialized live agent&#x20;
* Invoke a custom search or your own a website search

If you have multiple Dialog skills with pre-unhandled intents, then you can define a weightage for each of the pre-unhandled intent codes as per your business model. You can assign weightage with any number between 0 and 1, for example, 0.2, or 0.5. The pre-unhandled intent code with the highest weightage is considered.&#x20;

**Example**: Consider that you can have two Dialog skills with pre-unhandled intent. One that invokes a custom search and another with your business website search. Based on the response received from each one of these, you can infer, assign weightage, and return weightage. The custom code with the highest weightage is considered.&#x20;

{% hint style="info" %}
**Note**: If you have specified intent type as **Pre-Unhandled**, then you can add required entities to the skill using the **Add entity** option. See [Entities](#7.-entities), for more information.
{% endhint %}

### 6. Add training set

This allows you to add training data in different languages. It is not required to train your skill in English only, you can train your skill in different languages.&#x20;

* Add language in **Configuration -> Languages** and save the skill.&#x20;
* Click **Add training set** in Invocation Intent.&#x20;
* Select the required language and add the training set in the selected language.

### 7. Entities

Based on the training phrases, the platform automatically extracts and includes all the required entities in your skill. Note the color of the phrases matches with entities for easy identification. You can review these entities and delete those not required for the skill. See [Add entity types to agent](applewebdata://9A520571-0A8D-4D20-9B69-57776C06AEDE/@avaamo/s/avaamo/~/drafts/-MEMRR4arlIeVAXDyv-N/how-to/build-agents/add-entity-types-to-agent) and [examples](applewebdata://9A520571-0A8D-4D20-9B69-57776C06AEDE/@avaamo/s/avaamo/~/drafts/-MEMRR4arlIeVAXDyv-N/how-to/build-agents/add-entity-types-to-agent/example-pizza-agent), for more information.

{% hint style="success" %}
**Key Points**:&#x20;

* User-defined entities take priority over system entities, in cases where both match the user intent.

* Slot name must be unique across all entity types in an agent. When a user query is posted, the intent execution considers the training data across all the skills in the agent, hence, the slot name must remain unique across all entity types in an agent. **Example**: Consider that you have a slot name "otp" with entity type as "Number". In this case, if you try to add the same slot name "otp"  for a different entity type "One-time password", then an error message is displayed that the slot name is already taken by another entity type.
  {% endhint %}

* If you have specified intent type as **Training phrases** and if you require additional entities in the flow, then it must always be a part of the training data in the invocation intent.&#x20;

* If you have specified intent type as **Custom code or Pre-unhandled**, then you can add required entities to the skill using the **Add entity** option:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MQB9PH7GEkl3jSFQZgM%2F-MQBk55GT_J05-2u1fu5%2Finvocation-intent-add-entity.png?alt=media\&token=690d5060-1198-4c5a-8b96-46e8069f466a)

### 8. Post Processing

Specify any JS that is executed after the intent is invoked and before displaying the skill response. Custom Javascript to dynamically reroute the flow and skip the current intent.

```
Example:
if(context.variables.hasId==true){
 return goto_output(2)
}
```

{% hint style="info" %}
**Note**: Post-processing is where the intent execution still continues after matching the invocation intent; hence, when post-processing is enabled at the invocation intent, the entity skipping is no longer relevant and not evaluated.&#x20;
{% endhint %}

See [Skill response execution](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/intent-execution-sequence#post-processing-and-skill-response-execution), for more information on the sequence of execution.

## **Example 1:** Weather agent

Consider a skill "Find Weather" to help users find the current weather of a location. As you enter the training phrases in the invocation intent, the location entity and corresponding slot is automatically extracted from the training phrases. Here, the location entity is a system entity:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mac0E7i2uWY0cxITsqV%2F-MacGx_LS-_eTdoi79q0%2F5.7-invocation-intent-example-1.png?alt=media\&token=ca584a76-a568-4c8b-978f-e6b7692006aa)

## **Example 2: Pizza agent**

Consider a skill "Order Pizza" to help users place a pizza order. Consider that you have also created two entity types:

* pizza types - veg, non-veg
* pizza toppings - cheese, tomato, onion, pepper

As you enter the training phrase with values from the entities, say "I want to order veg pepper pizza" in the invocation intent, the entities and corresponding slots are automatically extracted from the training phrase.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MacH77zzW8L_BBCUkEg%2F-MacHQWlMVfV19-HkBIQ%2F5.7-invocation-intent-example-2.png?alt=media\&token=117a212c-d13c-4a54-a6ff-f803eaca0cd6)

## **Example 3: Travel agent**

Consider a skill "Book Tickets" to help users book travel tickets. As you enter the training phrase in the invocation intent, the location entity and corresponding slot is automatically extracted from the training phrase. Here, the location entity is a system entity. Note that here, you can rename the slots to "from\_location" and "to\_location" which helps you identify the source and destination.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MacH77zzW8L_BBCUkEg%2F-MacIi_k4XNZC20AS4IV%2F5.7-invocation-intent-example-3.png?alt=media\&token=48190a1a-18e5-4c4c-8a90-8e722e3a90bf)
