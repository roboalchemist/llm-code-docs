# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/entity-skipping.md

# Entity skipping

Avaamo Platform provides the ability to automatically detect the entities in a user query and skip asking questions to the users for which the answers are already available in the initial query. This is referred to as entity skipping.&#x20;

**Examples**:&#x20;

| Entity type  | Entity values                            |
| ------------ | ---------------------------------------- |
| Pizza types  | Veg, Non-Veg, Vegan                      |
| Specialists  | Cardiologist, Neurologist, Paediatrician |
| Account type | Savings, Current                         |

Further, you can also link an entity type to a parent entity type. **Example**: state entity type as a parent of the city entity type. The state entity type can in turn be a child of the country entity type. See [Add entity types to agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent), for more information.

{% hint style="info" %}
**Notes**:&#x20;

* If at the same level, multiple entity intents are matched for a user query, then entities are not skipped, as the platform is unsure which flow to further navigate. On the other hand, if you have such a use case, then consider accessing your requirements and revisiting your flow if required.
* Post-processing is where the intent execution still continues after matching a node; hence, when post-processing is enabled at a node, the entity skipping is no longer relevant and is not evaluated.
  {% endhint %}

Consider the following sample flow implementation in an "Order Pizza" dialog skill for ordering pizzas:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ma83jDUzdHL2zvK-bZ0%2F-Ma84gjkLGFjJIQCNARf%2F5.7-dialog-concept-entity-skipping.png?alt=media\&token=71275250-bd9d-4be3-9db3-572e895ea781)

### Entity type - Simple use case

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M1TqOK_OVuErYYU7tAh%2F-M1TunbF8fHIdBRPveFH%2FEntityTypeSimple.gif?alt=media\&token=14aab89d-3dca-4096-8d7e-a739fea3acb1)

* Create an entity type "Pizza type" for types of pizzas. See [Add new entity type](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/add-new-entity-type) and [Add entity values](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/manage-entity-types#add), for more information

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-NqZZF5UwTnocz-Uz2%2F-M-O5ikLnXSdA6rSqDlI%2Fhowto-agent-entity-type-example-1.png?alt=media\&token=334afbc2-3f07-45cf-866d-a5dadb4fbede)

* In your Dialog skill, the user intent "pizzatype" is mapped to the entity type "pizza\_type". See [Add user intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-NqZZF5UwTnocz-Uz2%2F-M-O1uwG27PgV8DKsuLN%2Fhowto-agent-entity-type-example-1-user-intent.png?alt=media\&token=926ff30c-c4a9-4c31-9e10-1895a45ac39e)

* Test the agent using the agent icon at the bottom-right corner:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FcbvFxYhMdkwR3Rt5TCHd%2Fimage.png?alt=media\&token=7dcd6be9-64a9-4c34-b807-bfd8c33cf393)

* Click the eye icon, you can view the entity extracted in the user query.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F8Ji60koLLgbVFIrzYkgj%2Fimage.png?alt=media\&token=23b37daf-5045-44f2-81bd-28b7f560325e)

Note that if you specify a value other than those mentioned in the entity values, then the query goes to an unhandled response.

### Entity skipping - Entity type linked to parent entity type

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M1TqOK_OVuErYYU7tAh%2F-M1Tu2VMYx3ZDezORfTd%2FEntityType%20-%20Entity%20Skipping.gif?alt=media\&token=c78b0475-1788-45dd-bccf-68fb963eae35)

* Create an entity type "Pizza toppings" and specify "Pizza type" as the parent entity type. See [Add new entity type](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/add-new-entity-type) and [Add entity values](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/manage-entity-types#add), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-NqZZF5UwTnocz-Uz2%2F-M-O6SsMQ9lRkxScB874%2Fhowto-entitytype-ex2.png?alt=media\&token=fcabfeeb-8168-438b-8a08-335412b3a9ff)

* In your Dialog skill, the user intent "pizzatoppings" is mapped to the entity type "pizza\_toppings". See [Add user intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-NqZZF5UwTnocz-Uz2%2F-M-O6piM-s8TU6ny2nAR%2Fhowto-entitytype-ex2-intent.png?alt=media\&token=1f579dff-b1e9-490a-bf01-1ff9e11de88b)

* Test the agent using the agent icon at the bottom-right corner. Note that as the entities are extracted from the user query, the platform understands that the details on the pizza type and pizza toppings are already provided by the user. Hence, those responses are skipped and the skill response after the pizza toppings is displayed to the user.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FrX0zPw9Vnhva2suONhdz%2Fimage.png?alt=media\&token=9528f128-6be2-468a-9c43-0b58d12917c5)

* Click the eye icon, you can view the entity extracted in the user query.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F0mdPrCXKHTHTFsmfHJAg%2Fimage.png?alt=media\&token=28cb5fa8-ac18-4cf2-9040-ee377803a443)&#x20;

Note that if you specify a value other than those mentioned in the entity values, then the query goes to an unhandled response.
