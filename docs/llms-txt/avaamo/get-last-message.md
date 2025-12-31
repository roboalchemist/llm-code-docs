# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/get-last-message.md

# Get last message

You can get the last message of the agent using [context.last\_message](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context). You can use this to:

* Re-iterate or reconfirm the user’s intention
* Extract user’s intent from the last message and perform certain validations

{% hint style="info" %}
**Notes**:

* In the text, quick reply, card, or carousel, you can use **${context.last\_message}** to extract the last message sent by the user.
* In a JS node, you can use **context.last\_message** to extract the last message.
* You can use **context.last\_message.<\<uuid>>** to access card responses in the last message of the user. See [Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card), for more information.
* If you have added a form element to a card response, then the system generates an element uuid that can be used in **context.last\_message.<\<uuid>>**. See [Add Form Elements](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-form-elements), for more information.
  {% endhint %}

Consider that you have used [context.last\_message](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context) to log the last message of the agent in the console log while ordering a pizza for debugging purposes:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LxZooBkSO4YKEY4YBEV%2F-LxZqdHfTofgCJKz5caJ%2Fjs-context-last-message.png?alt=media&#x26;token=da2da4bc-3aee-4d33-9860-da56a53f8f0a" alt=""></div>

```
console.log(context.last_message);
```

In the agent, the following details are displayed in the console:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LxZooBkSO4YKEY4YBEV%2F-LxZqzVqRkazTJMXEBVh%2Fjs-context-last-message-result.png?alt=media&#x26;token=0daa978f-c9a0-4c79-80f8-19a60ab8e35f" alt=""></div>

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to)
{% endcontent-ref %}
