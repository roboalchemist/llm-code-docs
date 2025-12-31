# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.1.0.md

# Release notes v8.1.0

The Avaamo Conversational AI Platform Atlas 8.1.0 release includes **10** **enhancements** and a few bug fixes.

For streamlined navigation, these enhancements are categorized according to the modules within the Avaamo Conversational AI Platform:

<table><thead><tr><th width="194">Module</th><th>Enhancements</th></tr></thead><tbody><tr><td>LLaMB</td><td><a href="#integrate-llamb-with-any-enterprise-application-seamlessly">Custom channel support - Integrate LLaMB with any enterprise application seamlessly</a></td></tr><tr><td>LLaMB</td><td><a href="#improved-source-citation-in-llamb-responses">Improved source citations in LLaMB responses</a></td></tr><tr><td>LLaMB</td><td><a href="#improved-personalization-using-document-attributes">Improved personalization using document attributes </a></td></tr><tr><td>Advanced agents</td><td><a href="#enhance-the-conversational-experience-by-enabling-disabling-co-reference">Enhance the conversational experience by enabling/disabling co-reference </a></td></tr><tr><td>User property</td><td><a href="#improved-personalization-assign-multiple-values-to-single-user-property">Improved personalization: Assign multiple values to single user property</a></td></tr><tr><td>C-IVR  channel configuration improvements</td><td><a href="#ui-toggle-to-enable-wait-time-tone">Ease of use - UI toggle to enable wait time tone</a></td></tr><tr><td>Entities</td><td><a href="#enhance-the-accuracy-by-enabling-disabling-entity-value-translation">Enhance the accuracy by enabling/disabling entity value translation </a></td></tr><tr><td>New REST APIs</td><td><ul><li><a href="#user-property-api-create-get-update-and-delete">User property API (Create, Get, Update, and Delete)</a></li><li><a href="#get-message-insights">Get message insights </a></li></ul></td></tr><tr><td>Updated REST API</td><td><ul><li><a href="#standardization-of-analytics-message-api">Standardization of Analytics Message API</a></li></ul></td></tr></tbody></table>

### Integrate LLaMB with any enterprise application seamlessly

In this release, the deployment channel support for LLaMB has been enhanced. You can now deploy LLaMB in the `Custom channel` . This expands the capability to seamlessly integrate LLaMB with any enterprise application, making it more accessible to users.

Custom channel support has been a fundamental feature for all agents within the Avaamo Platform since its inception. With this release, this capability has been expanded to include agents equipped with LLaMB skills.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FwNQXwT0tuuipxFpTrIeR%2Fimage.png?alt=media&#x26;token=c74e7f2b-2de6-4e9b-b841-2620542cbd7c" alt=""><figcaption></figcaption></figure>

The user interacting with the agent sends/receives messages to/from a custom channel. The custom channel integrates with the Avaamo platform via Avaamo API and Webhook calls to send and receive messages. See [Custom channel](https://docs.avaamo.com/user-guide/llamb/custom-channel), for more information,&#x20;

In the previous release, you could deploy LLaMB only on the Web, MS Teams, Android, and iOS channels, limiting its reachability.

### Improved source citation in LLaMB responses&#x20;

This release has improved the source citations within LLaMB responses to enhance readability and optimize space utilization. The citations are now concise and streamlined, allowing users to focus more on the responses while still providing easy access to the citation references when required.

| Enhanced source citation (v8.1.0)                                                                                                                                                                                                                          | Earlier source citation (v8.0.0)                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fobjd57tlvLAqF23ySp99%2Fimage.png?alt=media&#x26;token=32149f29-ff38-4dfd-ae91-75e522b2ee69" alt="" data-size="original"> | <p></p><p><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fia5JjgwkJ8uM6EO9dI8Y%2Fimage.png?alt=media&#x26;token=4dc7383f-1ce5-4dda-883b-755940975dc5" alt="" data-size="original"></p> |

In this release,

* Each source citation is sequentially numbered and displayed within square brackets, such as <mark style="color:blue;">\[1]</mark>
* Multiple source citations are consolidated into a single line after the response, with each citation separated by a space, such as <mark style="color:blue;">\[1] \[2] \[3]</mark>
* Users can hover on the numbers to display the actual document name and click the document name to display the actual source.

In previous versions, each source citation was displayed on a separate line labeled "View source". This approach resulted in excessive use of space, particularly when multiple citations were present, diverting attention from the response to the sources.

### Improved personalization using document attributes &#x20;

In this release, you can associate attributes to the uploaded URLs for rendering personalized responses to the users based on business requirements.&#x20;

Typically, in enterprise organizations, content is extensive and often tailored to specific user groups. LLaMB facilitates seamless content ingestion and allows you to associate attributes with the uploaded content. Document attributes are valuable for filtering responses and creating personalized responses based on user properties like region, roles, and products.&#x20;

For example: When a policy document is specific to a certain region, specifying the relevant attribute for that document enables the agent to provide the corresponding policy information to users trying to access information from a specific region.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXSIQfKuIYXowbBTQgGaR%2Fimage.png?alt=media&#x26;token=4f563ad2-7a48-426a-bf16-49d69b159d52" alt=""><figcaption></figcaption></figure>

See [Document attributes](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/document-attributes), for more information.

### Enhance the conversational experience by enabling/disabling co-reference&#x20;

In this release, the configuration option for Advanced agents has been enhanced with a new checkbox `Disable Co-reference query generation`in the `Agent Configuration -> Settings` page.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F9gaaaurUk87WrzcxaS2H%2Fimage.png?alt=media&#x26;token=1e8272f4-5eae-4205-b20d-b78ce05962e6" alt=""><figcaption></figcaption></figure>

An `Advanced agent` can remember and maintain context throughout a conversation. This enables the system to understand references, callbacks, and evolving topics within the dialogue. However, co-reference may not be required for all the use cases. In specific scenarios where co-reference resolution might introduce errors or unnecessary complexity, you can choose to disable co-reference.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* By default, the co-reference option for Advanced agents is enabled.
* `Disable Co-reference query generation` option is available only for Advanced agents. &#x20;
  {% endhint %}

See [Disable Co-reference query generation](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#disable-co-reference-query-generation), for more information.

### Improved personalization: Assign multiple values to single user property

This release significantly boosts the ability to deliver personalized experiences through Avaamo agents. Now, in this release, you can assign an array of values to a single user property.

While personalized responses using user properties have been available since the 5.x release, they were restricted to single-value strings like "employee\_status" or "customerType." By utilizing user properties, you could authorize users via JWT, and when coupled with response filters, generate personalized responses.

However, a single-user property often requires multiple values in a true enterprise setting. For instance, an employee can have a hybrid location spanning two countries. With this enhancement, you can now assign an array of values to a single user property, enabling enhanced authentication and personalized responses based on these values.

This improvement is a significant advancement in personalized response creation, facilitating scalability at the enterprise level without being constrained by the limitations of single, simplistic user properties.

#### How to use?

{% tabs %}
{% tab title="User.setProperty" %}
**Syntax**:

<pre class="language-javascript"><code class="lang-javascript"><strong>User.setProperty("&#x3C;&#x3C;key>>",["&#x3C;&#x3C;value1>>","&#x3C;&#x3C;value2>>",...])
</strong>
Example: User.setProperty("country",["India","Australia"])
</code></pre>

See [User.setProperty](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperty), for more information.
{% endtab %}

{% tab title="User.setProperties" %}
**Syntax**:

{% code overflow="wrap" %}

```javascript
User.setProperties({"<<key1>>":["<<value1>>","<<value2>>",...],"<<key2>>":["<<value1>>","<<value2>>",...],...})

Example: User.setProperties({"student_name": ["david","sally","james" ],"guardian_name":["williams","gomez"]})
```

{% endcode %}

See [User.setProperties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperties), for more information.
{% endtab %}

{% tab title="Authorize using JWT" %}
You can now pass multiple values in a user property based on the requirement and authorize the users using JWT. Earlier, only single-valued user property was supported.

The following is a sample user payload with some basic user details such as email, and all are single string values and an additional country property with an array of values:

```json
{
 "uuid": "<unique user id>",
 "email": "john.doe@avaamo.com",
 "phone": "+1234567890",
 "first_name": "John",
 "last_name": "Doe",
 "iat": 1516239022,
 "country": ["India","Australia"];
 "exp": 1519339022
}
```

See [Authorization using JWT](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/authentication-using-jwt), for more information.
{% endtab %}

{% tab title="User properties in custom channel " %}
With this release, you can pass multiple values in a property in the custom channel payload. Earlier, only single-valued user property was supported in the custom channel payload.

The following is a sample user payload with some basic user details such as email, and all are single string values and an additional country property with an array of values:

{% code overflow="wrap" %}

```json
POST /bot_connector_webhooks/4a94ec00-xxxx-xxxx-xxxx-e8cc04172812/message.json HTTP/1.1
Host: https://cx.avaamo.com/
Content-Type: application/json
Cache-Control: no-cache
{
  "channel_uuid": "f33b3814-xxx-xxxx-xxxx-a1d2b77585af",
  "locale": "hi-IN",
  "user": {
    "first_name": "Will",
    "last_name": "Smith",
    "uuid": "9ac15843-xxxx-xxxx-xxxx-930b89ce797e",
    "custom_properties":{
          "country": ["India","Australia"],
          "customerType": "guest"
      }
  },
  "message": {
    "text": "hello"
  }
}
```

{% endcode %}

See [Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel), for more information.
{% endtab %}
{% endtabs %}

### UI toggle to enable wait time tone

In this release, the C-IVR channel configuration page has been enhanced with a new toggle option `Enable wait time tone`. &#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FtJzEq3YZIVxtqfauWvVg%2Fimage.png?alt=media&#x26;token=8b08f9f2-d40c-463e-86d1-af74743b23b7" alt=""><figcaption></figcaption></figure>

The ability to enable a wait time or idle tone has been available since the Atlas 8 release, where it proves particularly useful when an agent needs additional time to respond, keeping the user engaged and informed that a response is forthcoming. See [Voice idle tone in Atlas 8 release notes](https://docs.avaamo.com/user-guide/release-notes-v8.0#voice-idle-tone), for more information.

Previously, in the Atlas 8 release, developers had to contact Avaamo Support to activate this feature. Now, they can enable it directly from the channel configuration page, and hence,

* It is convenient and easy to use. Sliding the toggle option will enable the idle tone. Note that by default, the toggle is disabled.
* Provides developers complete control over when to enable and disable as per the requirements.
* Faster development cycle, since developers need not reach Avaamo Support to enable or disable this feature.

See [C-IVR channel configuration](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/conversational-ivr-c-ivr-phone), for more information.

### Enhance the accuracy by enabling/disabling entity value translation

In this release, the configuration option for agents has been enhanced with a new checkbox `Do not translate entity values` in the `Agent Configuration -> Settings` page.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fkr6CYXOC8VvfDW6iMgb3%2Fimage.png?alt=media&#x26;token=ae695486-41f7-4f69-87d0-bda1f9cf5ced" alt=""><figcaption></figcaption></figure>

By default, the entity values in different languages are always translated to en-US before intent matching. However, in certain scenarios, translating the entity values may result in a completely different meaning in the corrected query and can result in unexpected intent matches. In such cases, you can enable the checkbox `Do not translate entity values`. When you enable this checkbox entity values are not translated to en-US and are used as-is for intent matching.

{% hint style="info" %}
**Note:** By default, `Do not translate entity values` is disabled, which implies that entity values are always translated to en-US before intent matching.
{% endhint %}

See [Do not translate entity values](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#do-not-translate-entity-values), for more information.

### User property API (Create, Get, Update, and Delete)&#x20;

In this release, a new REST API has been introduced to:&#x20;

* Create new user property in the agent
* Get all the user properties from the agent
* Update the user property value in the agent for a specified key
* Delete user property in the agent with the specified key

{% tabs %}
{% tab title="Create (POST)" %}

```javascript
// Signature - Create user property

POST 
https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties
```

{% code overflow="wrap" %}

```javascript
// Sample cURL request - Create a new user property "region" for the given agent

curl --location 'https://cx.avaamo.com/api/v1/agents/94xxx/user_properties' \
--header 'access-token: xxxxxxxxx61f48829a47ccdxxxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "user_property": {
    "name": "region",
    "key": "region"
  }
}'
```

{% endcode %}
{% endtab %}

{% tab title="Get (GET)" %}

```javascript
// Signature - Get user property

GET 
https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties/{{property_id}}
```

```javascript
// Sample cURL Request - Get all the user properties from the agent: 

curl --location 'https://cx.avaamo.com/api/v1/agents/54xxx/user_properties' \
--header 'access-token: xxxxxxxxe61f48829a47ccd9xxxxxxxx'
```

```json
// Sample response

{
    "current_page": 1,
    "per_page": 25,
    "total_entries": 1,
    "total_pages": 1,
    "time_token": 1717055987.929187,
    "entries": [
        {
            "id": 92xx,
            "name": "region",
            "key": "region"
        }
    ]
}
```

{% endtab %}

{% tab title="Update (PUT)" %}

```javascript
// Signature - Update user property

PUT 
https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties/{{property_id}}
```

{% code overflow="wrap" %}

```javascript
// Sample cURL request - Update the name of the user property 

curl --location --request PUT 'https://cx.avaamo.com/api/v1/agents/942xx/user_properties/92xx' \
--header 'access-token: xxxxxxxxx61f48829a47ccdxxxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "user_property": {
    "name": "location"
  }
}'
```

{% endcode %}
{% endtab %}

{% tab title="Delete (DELETE)" %}
{% code overflow="wrap" %}

```javascript
// Signature - Delete user property

DELETE 
https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties/{{property_id}}
```

{% endcode %}

{% code overflow="wrap" %}

```javascript
// Sample cURL request - Delete the user property using the property identifier

curl --location --request DELETE 'https://cx.avaamo.com/api/v1/agents/94xxx/user_properties/92xx' \
--header 'access-token: xxxxxxxxx61f48829a47ccdxxxxxxxxx' \
--data ''
```

{% endcode %}
{% endtab %}
{% endtabs %}

See [User property API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/user-property-api), for more information.

### Get message insights

In this release, a new REST API has been introduced to get insights using the message UUID. Example: In the custom channel response, message UUID is returned and you can use the message UUID to get the insights using this API.

```javascript
// Signature

GET 
https://cx.avaamo.com/api/v1/agents/{{agent_id}}/query_insights/{{message_id}}.json
```

{% code overflow="wrap" %}

```json
// Sample Request

Example: Get insights for a specific message.

https://cx.avaamo.com/api/v1/agents/56xxx/query_insights/0606e1df-9e9b-4b42.json

// Sample response

{
  "insight": {
    "intent_type": "INLINE::INTENT",
    "skill_name": "Macpizza Order",
    "skill_key": "macpizza_order",
    "intent_name": "Macpizza Order",
    "intent_key": "pizza_toppings",
    "node_key": "macpizza_order.pizza_toppings",
    "original_text": "I want to order veg cheese pizza",
    "document": "I want to order veg cheese pizza",
    "entities": [
      {
        "entity": "pizza_toppings",
        "entity_type": "pizza_toppings",
        "entity_value": "cheese",
        "domain_key": "bot_inline_domain_bee25dca-3b9f-46eb-a456",
        "value": "cheese",
        "current_value": "cheese",
        "index": 20,
        "parent_entity_key": "pizza_types",
        "custom_entity_type": true
      }
    ],
    "negation": false,
    "sentiment": "neutral",
    "tone": "",
    "detected_language": "English(en-US)",
    "second_best_result": null,
    "matching_document": "I want to order veg cheese pizza"
  }
}
```

{% endcode %}

See [Message insights](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/message-insights), for more information.

### Standardization of Analytics Message API

In this release, the `Analytics Message API` has been standardized with the following changes:

* A new response attribute `layer_id` has been added to the user object. `layer_id`serves as a unique identifier for each user.&#x20;
* **first\_name**: If the user information is collected, then `first_name` indicates the first name of the user corresponding to the message, or else it is displayed as "You". See [Collect user information](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/widget-configuration#collect-user-information), for more details.

The following is a sample response returned by the Analytics Message API:

```json
{
    "current_page": 1,
    "per_page": 1,
    "total_entries": 8,
    "total_pages": 8,
    "time_token": 1716811116.983583,
    "entries": [
        {
            "message_uuid": "e00a9d28-xxxx-4350-xxxx-389c395afec5",
            "score": 1.0,
            "content": "",
            "intent_type": "JS::INTENT",
            "channel_name": "web",
            "created_at": 1716811065.0,
            "user": {
                "first_name": "David",
                "layer_id": "06c7beb3-9bf8-xxxx-xxxx-745e5431053d"
            },
            "intent_name": "custom code"
        }
    ]
}
```

See [Message API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/messages), for more information.&#x20;
