# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/multi-line-text.md

# Multi-line text

You can add a multi-line input card in the skill response.&#x20;

### Syntax

The following is the syntax to add a multi-line text in the card input:

{% hint style="info" %}
**Notes**:&#x20;

* There is a 191-character limit for all the user-defined text fields except `data_capture` field. You can specify upto 60000 characters in the `data_capture` field.
* **hint** attribute is not supported in the Microsoft Teams channel due to the limitations on the channel's side. See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.
  {% endhint %}

```yaml
"card": {
 "inputs": [{
 "type": "data_capture",
 "title": "<<text_title>>",
 *"should_validate": true/false,
 *"hint": "<<hint_text>>",
 *"default_value": "<<default_text>>",
 "uuid": "<<secure_random_uuid>>"
 },...]
}
* - Indicates optional parameter
… - Indicates one or more parameter
```

<table><thead><tr><th width="180.33333333333331">Attribute</th><th width="463">Description</th><th>Type</th></tr></thead><tbody><tr><td>title</td><td>Indicates the title of the text field.</td><td>String</td></tr><tr><td>should_validate</td><td>Indicates if the user can skip entering values for the field or not before submitting. By default, the value is set to true.</td><td>Boolean</td></tr><tr><td>hint</td><td>Indicates a sample hint for the user to enter the value in the field. This is displayed in the input field before the user enters a value.</td><td>String</td></tr><tr><td>default_value</td><td>Indicates the default value displayed in the text field when rendered to the user.</td><td>String</td></tr><tr><td>uuid</td><td><p>Indicates a secure random UUID that can be used later to get the text entered by the user. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information.</p><p></p><p>Option selected by the user is available in the context.last_message.</p><p>Syntax: context.last_message.&#x3C;&#x3C;uuid>></p></td><td>String</td></tr></tbody></table>

### Example

The following is a sample JS to provide a multi-line text field in card input with hint text:

```yaml
return[{
  "card": {
    "inputs": [
      {
        "type": "data_capture",
        "title": "How was our service?",
        "uuid": "a4615857-c2f7-4586-b4b0-f771683fcb1a"
        "hint": "xxx@yyy.com"
      }
    ]
  }
}]
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FlqBw3X6RN4S8HOL7uyf1%2Fimage.png?alt=media\&token=7622b7a7-33e3-4528-8ec0-32ca800c0a2a)

You can use `context.last_message.<<uuid>>` to get the text entered by the user.

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response)
{% endcontent-ref %}
