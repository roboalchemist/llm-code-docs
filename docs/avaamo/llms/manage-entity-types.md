# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/manage-entity-types.md

# Manage entity values

In the **Entities** page, you can manage entity values and its alternate values for an entity type, using the following actions:

* [Add](#add)&#x20;
* [Edit](#edit)&#x20;
* [Delete](#delete)
* [Export](#export)
* [Import](#import)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M1U51blbd8exyPfWvED%2F-M1U7EoBtUo_xU2ic5sR%2FAddEntityValues.gif?alt=media\&token=250b279b-af71-409d-9081-6102cd330962)

{% hint style="success" %}
**Key points**:&#x20;

* You can also right-click and open the entity types in a new browser tab or window. This reduces the number of clicks and helps you to work with your skills parallelly as you view or modify the entity types.&#x20;
* There is no limit on the number of values in an entity type. However, you can manage only upto 10,000 entity values in the UI. If you have an entity with more than 10,000 values, then it is recommended to export entity values to a CSV file from the UI, perform operations (edit or add values) in the exported file and then import the entity values back to the agent.
  {% endhint %}

{% hint style="info" %}
**Notes**:&#x20;

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add values to entity types immediately after creating an entity type. See [Add new entity type](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/add-new-entity-type), for more information.
* If you wish to edit an entity type in an agent, then:
  * Navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
  * In the **Agent** page, navigate to the **Entity types** option in the left navigation menu. Search and open the required entity type. See [Search entity types](#search-entity-types), for more information.
    {% endhint %}

## Add&#x20;

* In the **Entities** page, enter the entity value and click **Add.**&#x20;
* For each entity value, enter an alternate value in the **Alternate value** text box and click **Add**. **Examples**: San Francisco: SF and New York: NYC | The Big Apple.&#x20;
* If you have selected a parent entity type, then specify the corresponding parent entity value.&#x20;
* If you are creating an entity type with a regular expression, then specify the required regular expression and check the **Regular expression** option.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5mtEeLQ8cDwsox4vgNKk%2FScreenshot%202023-03-16%20at%202.34.22%20PM.png?alt=media&#x26;token=86c27383-2d0f-4ae8-a453-e1bceb26f95d" alt=""><figcaption></figcaption></figure>

### Regex entity (Key-points)

Note the following key points on regex entities:

* Identify a pattern for your regular expression that has defined boundaries. If a regular expression pattern is very generic without any boundaries, then it can result in unintended entity extraction from the user query. Hence, this can result in incorrect matches. Few examples of regular expression entity without boundaries:
  * A regex pattern that matches any word with 5 letters.&#x20;
  * A regex pattern that matches any set of characters with hyphens.
* Verify if the regular expression is valid.&#x20;
* Check if the regular expression contains any special character in your regex.&#x20;
* Regex entity is extracted only from the first capture group as an entity value. Example:

```
Pattern: more\sthan\s(\d+)\s*(?:sq ft|square feet|sqft)
Input String: villas more than 3400 sq ft
Full Match: more than 3400 sq ft
Group 1: 3400

Extracted entity: 3400
```

* Multiple occurrences of the same is also extracted from the training sentences.&#x20;
* If there is more than one regex in the entity and if more than one regex pattern matches, then the first matched pattern is considered.&#x20;
* Regex entity values are case-insensitive.
* Only those regex patterns that work with JavaScript is supported.
* Use the non-capturing group (?:pattern) when you need to repeat a grouping but do not need to use the captured value that comes from a traditional (capturing) group. Example:&#x20;

```
Scenario: To match any number followed by Rs. 

Here since the purpose is to capture number, you can put 
"Rs" in a non-capturing group

Suggested Pattern: (\d+)\s*(?:Rs)
```

* Avoid catastrophic backtracking. See [Exponential backtracking](https://en.wikipedia.org/wiki/ReDoS#Exponential_backtracking), for more information.

## Edit&#x20;

In the **Entities** page, click the entity value you wish to edit. Update the entity value, remove or add alternate values as required.&#x20;

## Delete&#x20;

You can delete an entity value from an entity type using the delete icon next to the entity value row. Alternatively, you can delete all the entity values of an entity type in the agent, if they are no longer required.&#x20;

* In the **Entities** page, click **Clear all** option.
* An alert message is displayed. Click **Clear** in the alert message to clear all the entities.
* Click **Save.**

## Export and Import entity values

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M1U7s-d5AtGIb5Z-3Ci%2F-M1U975CkL81kIVeldfo%2FExportImportEnityValues.gif?alt=media\&token=0f0ba052-bddb-402c-839b-9188e62175c3)

### Export&#x20;

* In the **Entities** page, click the **Export** option.&#x20;
* A CSV file is downloaded with entity values and its alternate values. You can edit this CSV file and import the values back to the platform.

**Example 1**: Entity with values (No parent entity)

&#x20;                                                             **types**

| value   | alternative-1  | alternative-2 |
| ------- | -------------- | ------------- |
| non-veg | non-vegetarian |               |
| veg     | vegan          | vegetarian    |

**Example 2**: Entity with values linked to the parent entity, Here, pizza\_types is a parent entity type of pizza\_toppings.

&#x20;                                                           **toppings**

| types   | value     |
| ------- | --------- |
| non-veg | chicken   |
| veg     | onion     |
| non-veg | pepperoni |
| veg     | tomato    |

### Import&#x20;

* In the **Entities** page, click the **Import values** option.&#x20;
* In the **Import** pop-up, click **Browse** to browse a CSV file with entity values. In the CSV file, the first column contains the name of the entity value and the consecutive columns include alternate values. You can also click **Download Sample CSV**, for a sample file.
* Click **Submit** to load all the entities to the agent. Import automatically saves the entity values.

{% hint style="info" %}
**Notes**:&#x20;

* You cannot import a duplicate entity value. An error message is displayed, when you try to save the entity type.
* When you import entity values to an entity type in an agent, the entity type key must match. Additionally, when you import entity values with a parent entity type, then the entity type key and all the parent entity values must match.&#x20;
* You can import upto 100000 entity values. If you wish to import more than 100000 entity values, then contact Avaamo Support.
  {% endhint %}
