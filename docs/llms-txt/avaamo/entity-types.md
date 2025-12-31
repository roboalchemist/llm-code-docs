# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/entity-types.md

# Entities

In simple terms, if an intent refers to a verb or the action in the user query, then an entity refers to a noun (the object on which the action is performed) in the user query. **Example**: In the user query \
"I want to book tickets from San Francisco to New York", San Francisco and New York represent entities of type Location.

### Entity types

An entity type is a named collection of similar objects such as states in a country, all pediatricians, a list of product names, or data types (Date, Email, Location). Each entity type contains one or more values. **Example**: An entity type named "US City" contains values - Los Altos, San Francisco, Los Angeles.

The following entity types are available in the Avaamo Platform:

* **System entities**: In-built entities in your agents that can match the common data types such as Location, Date, DateTime, Person, Organization.
* **Custom entities**: User-defined entities that represent the structured data related to your business. Few examples of customized entities in a Pizza agent - pizza size (small, medium, large), toppings (cheese, corn, tomato).&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* When you define a custom entity, the custom entity values must be replaceable in all the training data, which implies that in all the intents the custom entity values must have the same meaning.
* If you are using a date-time system entity in your training data and in a scenario where the only day and month is specified in the user query but not the year, the system picks the closest date to the current date. Example:&#x20;
  * Date in user query -> Feb 12
  * Current date -> Aug 6, 2020
  * Since Feb 12 2020 is closer than Feb 12, 2021, the year considered in the user query is 2020 instead of 2021.
    {% endhint %}

### **Entity alternate values**

Some of the entity values may have one or more direct alternate values or other phrases/words considered equivalent in meaning.&#x20;

**Examples**:&#x20;

* City entity type:

<table><thead><tr><th width="175.43298969072168">Entity value</th><th>Alternate value</th></tr></thead><tbody><tr><td>San Francisco</td><td>SF</td></tr><tr><td>New York</td><td>NYC, The Big Apple</td></tr></tbody></table>

* Pizza sizes entity type and alternate values

| Entity value | Alternate value |
| ------------ | --------------- |
| small        | 12 inch         |
| medium       | 14 inch         |
| large        | 16 inch         |

See [Add new entity type](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/add-new-entity-type), for more information on managing entity types and their values in the Avaamo Platform.

### Entity disambiguation

When a user value does not match a specific entity value at a node entity step in the conversation flow, the agent responds with a selection of closest entity values, referred to as entity disambiguation.&#x20;

Consider that you have an entity type "Colorado Cities" with four values - Colorado Springs, Glenwood Springs, Hot Sulphur Springs, and Idaho Springs.&#x20;

In the conversation flow, if a node entity "Colorado Cities" is expected and the user just enters "Springs" when asked for a Colorado city, then the system shows a disambiguation message to confirm for "Colorado Springs" or “Glenwood Springs” and any other entity value with Springs in "Colorado Cities" entity type.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fn56ij4xbdaaIl7I7dSl2%2Fimage.png?alt=media\&token=54fa73af-f3fb-4601-b92f-9e4d5f4f5cf0)

{% hint style="info" %}
**Notes**:&#x20;

* This disambiguation works even when there is a single option.
* The top 5 closest disambiguations is displayed to the user.
* Disambiguation options are from the selected entity node values.
  {% endhint %}

### Name entity recognition

In certain scenarios, the entity values are also used as common words. Example: "I am looking for Doctor Treat" and "Chocolate is his favorite treat". Both of these mean different in different context. For such scenarios, you can create a custom name entity type for the Platform to appropriately recognize and extract the "Name" entity as required based on the context of the user query.

{% hint style="info" %}
**Notes**:&#x20;

* This feature is applicable to only custom entity types.
* Contact support to enable this feature for your agent.
  {% endhint %}

**Example**:&#x20;

User: "*I am looking for Doctor Bill*", extracts Bill as a name

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F4nYosM6JoiS2Cch8F4dG%2Fimage.png?alt=media\&token=a0088843-222a-4a3b-a2a4-ce05082bcfad)

Here, the name is a custom entity type and this query extracts *Bill* as a name.&#x20;

User: "*I am unable to find my bill*", does not extract bill as a name.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fo6YWh4w3dJ4a61AEf9Om%2Fimage.png?alt=media\&token=3e1ed76c-7f2d-4c3e-8d32-a693ccc077cf)

Here, the word "bill" is not extracted as a "Name" entity.

### Number entity extraction

When the user enters a number name instead of a number, the number name entity is automatically recognized and converted to a number if it is expected at a number entity step.&#x20;

**Example**: If a user enters "two and half million", then it is automatically converted to 2500000 if it is expected at a number entity step or if a user enters a query as illustrated below then the number name is automatically converted to a number entity.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FgGzI2p52yK1rKeb4RKRG%2Fimage.png?alt=media\&token=01a854c2-75eb-47bf-a84e-791e14e94823)
