# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/slots.md

# Slots

When information is extracted from a user sentence, the first task is to identify the intent behind the user query. The next task is to extract parameters in the training data that complete the intent. These are referred to as **Slots**. Each slot maps to an [entity type](https://docs.avaamo.com/user-guide/entity-types#entity-types) for extraction and validation purposes.

{% hint style="success" %}
**Key Points**:&#x20;

* Based on the context, you can name each slot in the training data for easy identification.&#x20;
* The entity types that are to be added in the slots must be either available as system or custom entities in the agent.
* Slots are not always required to complete a user intent. Example: "*Who is your CEO?*" is complete on its own without requiring a slot.
* Typically, if slots are required to complete a user intent, then you must use a [Dialog skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer) to build a user conversation flow.
  {% endhint %}

**Example 1**:&#x20;

```yaml
Intent Name: Find Weather
Training Data: How is the weather?
Slot: none
```

In this example, there is no additional information on the place or city for which the weather details are required. Hence, no slots are extracted.

**Example 2**:&#x20;

```yaml
Intent Name: Find Weather
Training Data: How is the weather in [Los Altos]
Slot: city = Los Altos [Entity Type: Location]
```

In this example, the training data contains only one slot, the city for which the weather details is required.

**Example 3**:&#x20;

```yaml
Intent Name: Find flight
Training Data: Find flight from [Boston] to [New York]
Slots: 
* from_city = Boston [Entity Type: Location]
* to_city = New York [Entity Type: Location]
```

In this example, the training data contains two slots with the same entity type but with different purposes. Naming the slots appropriately, hence, helps in identifying the purpose of the slot.

In the Avaamo Platform, as you enter the training data for your skills, slots are automatically extracted and mapped to an entity type.&#x20;
