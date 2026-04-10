# Source: https://docs.deepconverse.com/product-docs/conversational-flow-builder/how-to-use-rules-in-conversations.md

# How to use Rules in Conversations

When conversations are complex and responses to questions depend on attributes in external information we can make use of rules to navigate the user to the right conversation response.

Rules allow you to define segmented conversation responses based on a defined criteria.&#x20;

### Adding Rules

1. Rules can be authored by dragging the ***Rule*** node on to the flow builder.&#x20;
2. On the right panel you can add a rule by entering a name for your rule.
3. Once you add the rule click on the name of the rule you added to define the criteria for it.\ <br>

   <figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FsGhB8dqskgaeZY7BSoz5%2Fimage.png?alt=media&#x26;token=ef92999e-3ede-4d97-a713-0a408f493f32" alt=""><figcaption></figcaption></figure>

### Authoring Rule Criteria

Each rule criteria is composed of one or more conditions and for each of the conditions you can do the following:

* Check all of the conditions (**AND** operation) - In this mode all conditions need to hold true for the rule to be true
* Check any of the conditions (**OR** operation) - In this mode any of the condition needs to be true for the rule to be true

The rule condition is composed of three parts:

1. Parameter Field Name
2. Operator
3. Field Value

#### Adding Conditions

| **Operator** | **Supported Types**   |
| ------------ | --------------------- |
| Not Equals   | Number, Text, Boolean |
| Equals       | Number, Text, Boolean |
| Greater Than | Number                |
| Less Than    | Number                |
| Contains     | Text                  |
| Is Not Empty | Text, List            |
| Is Empty     | Text, List            |

{% embed url="<https://player.vimeo.com/video/631335378>" %}

<br>
