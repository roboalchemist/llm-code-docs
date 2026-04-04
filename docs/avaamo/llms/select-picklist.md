# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/select-picklist.md

# Select (PickList)

You can use a picklist in the card input to provide a list of options for the user to choose from. This also acts as a search box that allows you to filter and select values.&#x20;

## Syntax

The following is the syntax to add a picklist response in the card input:

{% hint style="info" %}
**Notes**:&#x20;

* There is a 191-character limit for all the user-defined text fields.
* You can add any number of options to the picklist. However, only the first 50 options in a picklist are visible in the UI. As you start entering the text in the **Select** textbox of the picklist, the values are filtered and displayed in the list.&#x20;
* If you are using custom feedback, then for each option in the picklist you must specify the UUID. Currently, in the Custom feedback JS code, it is recommended to use user-friendly identifiers for UUIDs instead of a random-generated number in the "Options" object as it helps you to identify the message in the [User feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) page. See[ Example 3: Custom feedback](#custom-feedback), for a sample code. Also see [Custom feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/custom-feedback), for more information.
  {% endhint %}

```yaml
"card": {
 "inputs": [{
 "type": "picklist",
 "title": "<<picklist_title>>",
 *"default_value": "<<uuid_value>>",
 *"should_validate": true/false,
 "uuid": "<<secure_random_uuid>>",
 "options": [{
 *"uuid": "<<unique_id>>",
 "option": "<<value>>"
 },...]
 }]
}
* - Indicates optional parameter
… - Indicates one or more parameter
```

<table><thead><tr><th width="178.21173373304563">Attribute</th><th width="464.12813091394855">Description</th><th>Type</th></tr></thead><tbody><tr><td>title</td><td>Indicates the title of the picklist.</td><td>String</td></tr><tr><td>default_value</td><td><p>Indicates the default value selected in the picklist when rendered to the user. You must specify the uuid value from the options in the default value. Note that this is an optional attribute.</p><p></p><p>If you specify a default value and wish to see all the values in the picklist, then you must remove the default value in the search box.</p></td><td>String</td></tr><tr><td>should_validate</td><td>Indicates if the user can skip entering values for the field or not. By default, the value is set to true.</td><td>Boolean</td></tr><tr><td>uuid</td><td><p>Indicates a secure random UUID that can be used later to get the option selected by the user. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information.</p><p></p><p>Option selected by the user is available in the context.last_message.</p><p>Syntax: context.last_message.&#x3C;&#x3C;uuid>></p></td><td>String</td></tr><tr><td>options</td><td><p>Indicates an array of options in the picklist. If you wish to specify the default value, then specify the following in each array element:</p><ul><li><p><strong>uuid</strong>: Indicates a secure random UUID that can be used to specify the default_value. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information.</p></li><li><strong>option</strong>: Value of the option</li></ul></td><td>An Array of JSON key-value pairs </td></tr></tbody></table>

## Examples

### Picklist without default value

```yaml
return [{
  "card": {
    "inputs": [
      {
        "type": "picklist",
        "title": "Select one topping",
        "uuid": "d1135584-6a33-4962-bad1-0607ccc44955",
        "options": [
          "Cheese",
          "Corn",
          "Tomato",
          "Onion",
          "Chicken"
        ]
      }
    ]
  }
}]
```

In the agent, the following response is displayed:&#x20;

&#x20;![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FeeXbmNNUrMI2Yarmu9Ps%2FJS-Card-Picklist.png?alt=media\&token=f5882d1d-a239-4928-a50e-0574d750e69c)

You can use `context.last_message.<<uuid>>` to get the option selected by the user.&#x20;

### Picklist with default value&#x20;

```yaml
return [{
  "card": {
    "inputs": [
      {
        "type": "picklist",
        "title": "Pick",
        "default_value": "3d0a2797-a887-4055-a49f-225041ae536b",
        "uuid": "d1135584-6a33-4962-bad1-0607ccc44955",
        "options": [
          {
            "uuid": "70bf3d14-08b9-437f-97f1-be9cf493c3ba",
            "option": "Cheese"
          },
          {
            "uuid": "285dc7a2-cf61-413b-975c-236774df77aa",
            "option": "Corn"
          },
          {
            "uuid": "3d0a2797-a887-4055-a49f-225041ae536b",
            "option": "Tomato"
          },
          {
            "uuid": "67a162bb-689f-4148-8fe3-63a86f6cf668",
            "option": "Onion"
          },
          {
            "uuid": "514f394c-7997-45dd-bbca-9b6d3faa9a2a",
            "option": "Chicken"
          }
        ]
      }
    ]
  }
}
]
```

In the agent, the following response is displayed:&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F1o0ntk4YZnWVhY77Pzzo%2Fimage.png?alt=media\&token=2c4e862a-f6be-4330-93c1-e23e37a36b1d)

Clear the default value in the search box, to display all the values in the picklist. You can use `context.last_message.<<uuid>>` to get the option selected by the user.

### Custom feedback

The following is a sample code to illustrate how to use Picklist in Custom feedback. Note that here, it is recommended to use user-friendly identifiers for UUIDs instead of a random-generated number in the "Options" object as it helps you to identify the message in the [User feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) page.

```javascript
return {
  "notification_message": "Thank you for your valuable feedback. We hope to see you next time.",  
   "card": {
      "inputs": [
        {
          "type": "picklist",
          "title": "Pick",
          "default_value": "3d0a2797-a887-4055-a49f-225041ae536b",
          "uuid": "d1135584-6a33-4962-bad1-0607ccc44955",
          "options": [
            {
              "uuid": "Cheese",
              "option": "Cheese"
            },
            {
              "uuid": "Corn",
              "option": "Corn"
            },
            {
              "uuid": "Tomato",
              "option": "Tomato"
            },
            {
              "uuid": "Onion",
              "option": "Onion"
            },
            {
              "uuid": "Chicken",
              "option": "Chicken"
            }
          ]
        }
      ]
    }
  }
```

You can use `context.last_message.<<uuid>>` to get the option selected by the user.

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response)
{% endcontent-ref %}
