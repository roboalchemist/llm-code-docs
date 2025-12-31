# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/checklist.md

# Checklist

You can add an input card with a checklist for your end-users to select from.&#x20;

## Syntax

The following is the syntax to add a checklist response:

{% hint style="info" %}
**Notes**:&#x20;

* There is a 191-character limit for all the user-defined text fields.
* If you are using custom feedback, then for each option in the checklist you must specify the UUID. Currently, in the Custom feedback JS code, it is recommended to use user-friendly identifiers for UUIDs instead of a random-generated number in the "Options" object as it helps you to identify the message in the [User feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) page. See [Example 3: Custom feedback](#custom-feedback), for a sample code. Also see [Custom feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/custom-feedback), for more information.
  {% endhint %}

```yaml
"card": {
 "inputs": [{
 "type": "checklist",
 "title": "<<checklist_title>>",
 *"default_value": "<<uuid_value>>",
 *"should_validate": true/false,
 "uuid": "<<secure_random_uuid>>",
 "options": [{
 *"uuid": "<<secure_random_uuid>>",
 "option": "<<value>>"
 },...]
 }]
}
* - Indicates optional parameter
… - Indicates one or more parameter
```

<table><thead><tr><th width="177.33333333333331">Attribute</th><th width="392.7105561861522">Description</th><th>Type</th></tr></thead><tbody><tr><td>title</td><td>Indicates the title of the checklist.</td><td>String</td></tr><tr><td>default_value</td><td><p>Indicates the default value selected in the checklist</p><p>when rendered to the user. This is a comma-separated list and you can specify multiple values.</p><p>You must specify the uuid value from the options in the default value. Note that this is an optional attribute.</p></td><td>String</td></tr><tr><td>should_validate</td><td>Indicates if the user can skip entering values for the field or not. By default, the value is set to true.</td><td>Boolean</td></tr><tr><td>uuid</td><td><p>Indicates a secure random UUID that can be used later to get the text entered by the user. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information. </p><p></p><p>If multiple checklists are used in a card, each checklist must have a unique UUID.</p><p></p><p>The option selected by the user is available in the <a href="https://docs.google.com/document/d/1kLeCPObAeXeon6viGnywY3_9HQxSmfs-YS-xB561Ekg/edit#heading=h.sprg97pwog6">context.last_message</a>.</p><p>Syntax: context.last_message.&#x3C;&#x3C;uuid>></p></td><td>String</td></tr><tr><td>options</td><td><p>Indicates an array of options in the poll. If you wish to specify the default value, then specify the following in each array element:</p><ul><li><p><strong>uuid</strong>: Indicates a secure random UUID that can be used to specify the default_value. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information.</p></li><li><strong>option</strong>: Value of the option</li></ul></td><td><p>An array of </p><p>JSON key-value </p><p>pairs </p></td></tr></tbody></table>

## **Examples**

### Checklist without default value

The following is a sample code to illustrate how to use Checklist in cards without providing any default value:

```yaml
return [{
  "card": {
    "inputs": [
      {
        "type": "checklist",
        "title": "What do you like the most?",
        "uuid": "f8ce4692-7126-4110-a291-98e27df7c2d1",
        "options": [
          "Taste",
          "Variety",
          "Delivery",
          "Price"
        ]
      }
    ]
  }
}]
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FMs8amF1zO8NcnsyGoGnd%2Fimage.png?alt=media\&token=cc2483e1-52c5-4ac0-a5c7-ab7d168feaf0)

You can use `context.last_message.<<uuid>>` to get the option selected by the user.

### Checklist with default value

The following is a sample code to illustrate how to use Checklist in cards with a default value:

```yaml
return [{
  "card": {
    "inputs": [
      {
        "type": "checklist",
        "title": "What do you like the most?",
        "default_value": "e9ce7d73-f6ad-4301-b0e0-ad9b491e8dbb,afe96fb8-2312-4eee-9fba-c8e6a81fb217",
        "uuid": "f8ce4692-7126-4110-a291-98e27df7c2d1",
        "options": [
          {
            "uuid": "e9ce7d73-f6ad-4301-b0e0-ad9b491e8dbb",
            "option": "Taste"
          },
          {
            "uuid": "afe96fb8-2312-4eee-9fba-c8e6a81fb217",
            "option": "Variety"
          },
          {
            "uuid": "ff605b0d-963d-49d2-8dba-0b1fdce93f4c",
            "option": "Delivery"
          },
          {
            "uuid": "a6d531cd-725d-40ea-bf45-e0a903b2e76d",
            "option": "Price"
          }
        ]
      }
    ]
  }
}]
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FEC7UNABzK23M1pWlgveV%2Fimage.png?alt=media\&token=dae8d6e0-8fcc-4942-811e-00ef14ace8ea)

You can use `context.last_message.<<uuid>>` to get the option selected by the user.

### Custom feedback

The following is a sample code to illustrate how to use Checklist in Custom feedback. Note that here, it is recommended to use user-friendly identifiers for UUIDs instead of a random-generated number in the "Options" object as it helps you to identify the message in the [User feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) page.

```javascript
return {
  "notification_message": "Thank you for your valuable feedback. We hope to see you next time.",  
   "card": {
      "inputs": [
        {
          "type": "checklist",
          "title": "What do you like the most?",
          "default_value": "e9ce7d73-f6ad-4301-b0e0-ad9b491e8dbb,afe96fb8-2312-4eee-9fba-c8e6a81fb217",
          "uuid": "f8ce4692-7126-4110-a291-98e27df7c2d1",
          "options": [
            {
              "uuid": "Taste",
              "option": "Taste"
            },
            {
              "uuid": "Variety",
              "option": "Variety"
            },
            {
              "uuid": "Delivery",
              "option": "Delivery"
            },
            {
              "uuid": "Price",
              "option": "Price"
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
