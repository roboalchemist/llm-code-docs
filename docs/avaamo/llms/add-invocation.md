# Source: https://docs.avaamo.com/user-guide/skills/dialog-skill/add-invocation.md

# Add invocation

Invocation defines when a dialog skill is triggered by user input. In dialog skills, invocation is instruction-based, enabling flexible, intelligent matching rather than rigid training sentences.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FSpP2F52kPnpetIbeiUYO%2FScreenshot%202026-01-15%20at%2010.52.10%E2%80%AFAM.png?alt=media&#x26;token=bdc0f013-015c-432a-98ca-8e8a96438f42" alt=""><figcaption></figcaption></figure>

Invocation intent can be defined using entities as follows.

### **Entities**

Invocation intent using entity name and description. This approach is suitable for simple and flexible intent matching.

You can define invocation intent by specifying an entity with a **name** and a **description**.

* The entity name specifies the information required to invoke it.
* The description is passed to the LLM, which infers the entity value from the user’s input.
* The extracted entity helps determine whether to invoke the dialogue flow or a node.

**Example**

* **Entity name:** `pizza_type`
* **Description:** Indicates the pizza type, such as vegetarian or non-vegetarian.

**How to add an Entity**

1. Click `Add entity`, enter the name and description. Click `Save`.

### Entity Extraction Script

For advanced invocation scenarios, you can use an `Entity Extraction Script`. This method is recommended when invocation depends on complex conditions or strict validation rules.

* The script is written in **JavaScript (JS)**.
* It enables precise control over how entities are extracted.
* You can implement custom logic such as keyword matching, rule-based checks, or NLP-based extraction.

{% hint style="info" %}
**Note:** If both the entity name and description and an entity extraction script are configured, the extraction script takes precedence and overrides the name-and-description–based entity extraction.
{% endhint %}
