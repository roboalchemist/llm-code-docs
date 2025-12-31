# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/add-new-entity-type.md

# Add entity type

**Avaamo Platform** provides several in-built system entities in your agents that can match the common data types such as Location, Date, DateTime, Person, Email, URL. In addition, you can also create new **entities (custom and system)** within the agent and add to your agent skills. Custom entities created for an agent are available only for that agent. System entities are available across all the agents. **Example:** For a pizza agent, you can consider adding the following entity types and values:

* Pizza size: small, medium, large
* Pizza type: veg, non-veg
* Pizza toppings: cheese, corn, tomato, chicken, pepperoni

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can add entity types to an agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the Avaamo Platform UI, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M1-Cw3gjMOqqT-f5uSA%2F-M1-GKnIeEM1X_AjVLJt%2FEntityType.gif?alt=media\&token=b3af4f86-f337-4cfc-b665-87d42fb59f99)

### **Add new entity type**

* In the **Agent -> Entity types** page, click **Add new**.
* In the **Create new entity type** pop-up, specify the following details, and click **create**:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-NqZZF5UwTnocz-Uz2%2F-M-NxZFbcPk7F8FduIF2%2Fagent-entity-type-create.png?alt=media\&token=b92baf0a-e4b5-4861-b177-c64e4479dcc7)

<table><thead><tr><th width="177.241948153967">Parameters</th><th width="577.4285714285713">Description</th></tr></thead><tbody><tr><td>Name</td><td>Indicates the name of the entity type. This identifies the entity type when you are searching and adding entity types for skill in an agent.</td></tr><tr><td>Key</td><td>Indicates the internal primary key used in the Avaamo Platform for uniquely identifying the entity type. It is recommended that the key is of at least 3 characters. As you type, the key is automatically converted to Snake Case. See <a href="https://en.wikipedia.org/wiki/Snake_case">Snake Case</a>, for more information.</td></tr><tr><td>Description</td><td>Indicates the description of the agent. Use this to specify the purpose of the entity type.</td></tr><tr><td>Skip Lemmatization</td><td><p>Indicates if the extracted entity from the user query must be matched to <strong>lemma</strong> (Canonical form, dictionary form, or citation form of a group of words) or not. <strong>Example</strong>: run, runs, ran and running are forms of the same <a href="https://en.wikipedia.org/wiki/Lexeme">lexeme</a>, with run as the lemma.</p><p></p><p><strong>Example</strong>: You have created an entity type for pizza toppings with "cheese" as one of its values. </p><p>Consider user queries - "I want to order cheese pizza" and "I want to order pizza with lots of cheeses". </p><ul><li>With Skip Lemmatization checked - Only "I want to order veg cheese pizza" is extracted and matched correctly.</li><li>With Skip Lemmatization unchecked - Both the queries are matched and extracted correctly. Here, cheese and cheeses are forms of the same lexeme, with cheese as the lemma. </li></ul><p>See <a href="https://en.wikipedia.org/wiki/Lemmatisation">Lemmatization</a>, for more information. </p><p><strong>Note</strong>: This is not applicable to entities with regular expression.</p></td></tr><tr><td>Parent entity type </td><td><p>Indicates the parent entity type linked to this entity type. A child entity type can be linked to only one parent entity type. However, the parent entity type itself can be a child of some other entity type, and currently, there is no limitation on the number of such links supported in the Avaamo Platform.<br></p><p><strong>Example</strong>: State entity type can be parent entity type to city entity type. For the pizza agent, pizza type can be a parent entity type to pizza toppings. </p><p></p><p>With the parent, child linking of the entity types, you can leverage Avaamo Platform capability to understand and respond to user queries by skipping entities. See <a href="../../../overview-and-concepts/advanced-concepts/entity-skipping">Entity skipping</a>, for more information. Also see <a href="../example-pizza-agent#entity-skipping-entity-type-linked-to-parent-entity-type">Entity skipping - Entity type linked to parent entity type</a>, for a detailed example.</p><p></p><p><strong>Note</strong>: Parent entity type is not applicable for entities with regular expression.</p></td></tr><tr><td>Regular expression</td><td><p>Indicates a regular expression that is used to match the value of the extracted entity from the training data. You cannot link a parent entity type to a regular expression entity. See <a href="../manage-entity-types#regex-entity-key-points">Regex entity (Key-points)</a>, for more information.<br></p><p><strong>Example</strong>: You can create an entity type to match a regular expression such as pizza order number sequence in the user sentence. Later, when you create a node in the dialog, you can select this entity for processing user intent for the order number. See <a href="../../build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent">Add user intent</a>, for more information. </p></td></tr></tbody></table>

A new empty entity type is created. In the **Entities** page, you can add entity values and alternate values. See [Add entity values](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-entity-types#add), for more information.

### **Next steps**

You can also edit the entity type or delete an entity type, as required. See [Manage entity type](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/manage-entity-type), for more information.

Also see [Example -  Pizza agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/example-pizza-agent), for more examples on usages of entity types.
