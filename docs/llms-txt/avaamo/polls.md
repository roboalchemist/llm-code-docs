# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/polls.md

# Polls

You can add an input card with an option to poll to capture the opinion or vote of the users interacting with the skill.&#x20;

## Syntax

The following is the syntax to add a poll response:

{% hint style="info" %}
**Notes**:&#x20;

* There is a 191-character limit for all the user-defined text fields.
* If you are using custom feedback, then for each option in the Polls you must specify the UUID. Currently, in the Custom feedback JS code, it is recommended to use user-friendly identifiers for UUIDs instead of a random-generated number in the "Options" object as it helps you to identify the message in the [User feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) page. See [Example 3: Custom feedback](#custom-feedback), for a sample code. Also see [Custom feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/custom-feedback), for more information.
  {% endhint %}

```yaml

"card": {
 "inputs": [{
 "type": "poll",
 "title": "<<poll_title>>",
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

<table data-header-hidden><thead><tr><th width="192">Attribute</th><th width="383.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td><strong>Attribute</strong></td><td><strong>Description</strong></td><td><strong>Type</strong></td></tr><tr><td>title</td><td>Indicates the title of the poll.</td><td>String</td></tr><tr><td>default_value</td><td><p>Indicates the default value selected in the poll when rendered to the user. You must specify the uuid value from the options in the default value. </p><p></p><p>Note that this is an optional attribute.</p></td><td>String</td></tr><tr><td>should_validate</td><td>Indicates if the user can skip entering values for the field or not. By default, the value is set to <strong>true</strong>.</td><td>Boolean</td></tr><tr><td>uuid</td><td><p>Indicates a secure random UUID that can be used later to get the text entered by the user. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information. </p><p></p><p>File uploaded name is available in the <a href="https://docs.google.com/document/d/1kLeCPObAeXeon6viGnywY3_9HQxSmfs-YS-xB561Ekg/edit#heading=h.sprg97pwog6">context.last_message</a>.</p><p>Syntax: context.last_message.&#x3C;&#x3C;uuid>></p></td><td>String</td></tr><tr><td>options</td><td><p>Indicates an array of options in the poll. If you wish to specify the default value, then specify the following in each array element:</p><ul><li><p><strong>uuid</strong>: Indicates a secure random UUID that can be used to specify the default_value. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information.</p></li><li><strong>option</strong>: Value of the option</li></ul></td><td>An array of JSON key-value pairs</td></tr></tbody></table>

## **Examples**

### Polls without default value

The following is a sample code to illustrate how to use Polls in cards without providing any default value:

```yaml
return [{
  "card": {
    "inputs": [
      {
        "type": "poll",
        "title": "How was our service?",
        "uuid": "52837223-a60d-4e8e-9a90-c92e40f70fe9",
        "options": [
          "Good",
          "Very Good",
          "OK",
          "Need to improve"
        ]
      }
    ]
  }
}]
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7MEZDPejndykkQxptNdv%2Fimage.png?alt=media\&token=536750b7-84b3-4905-bb2f-2dcf76c267ba)

You can use `context.last_message.<<uuid>>` to get the option selected by the user.

### Polls with default values

The following is a sample code to illustrate how to use Polls in cards with a default value:

```yaml
return [{
  "card": {
    "inputs": [
      {
        "type": "poll",
        "title": "How was our service?",
        "default_value": "0090a567-8351-4ef4-b5db-e10b0ce83114",
        "uuid": "52837223-a60d-4e8e-9a90-c92e40f70fe9",
        "options": [
          {
            "uuid": "bd52ff4b-f5ea-4403-8134-b32abea16464",
            "option": "Very Good"
          },
          {
            "uuid": "0090a567-8351-4ef4-b5db-e10b0ce83114",
            "option": "Good"
          },
          {
            "uuid": "7d09b083-12ca-4696-8093-38f7db21efdd",
            "option": "OK"
          },
          {
            "uuid": "cd81194d-dea0-466d-92e4-151d435490ed",
            "option": "Need to improve"
          }
        ]
      }
    ]
  }
}]
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FdaE0xcP8fD4fcUomWKmW%2Fimage.png?alt=media\&token=bac56ce7-49c5-4d6b-bb03-65e24fc8acc9)

You can use `context.last_message.<<uuid>>` to get the option selected by the user.

### Custom feedback

The following is a sample code to illustrate how to use Polls in Custom feedback. Note that here, it is recommended to use user-friendly identifiers for UUIDs instead of a random-generated number in the "Options" object as it helps you to identify the message in the [User feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) page.

```javascript
return {
  "notification_message": "Thank you for your valuable feedback. We hope to see you next time.",  
  "card": {
    "inputs": [
      {
        "type": "poll",
        "title": "How was our service?",
        "default_value": "0090a567-8351-4ef4-b5db-e10b0ce83114",
        "uuid": "52837223-a60d-4e8e-9a90-c92e40f70fe9",
        "options": [
          {
            "uuid": "Very Good",
            "option": "Very Good"
          },
          {
            "uuid": "Good",
            "option": "Good"
          },
          {
            "uuid": "OK",
            "option": "OK"
          },
          {
            "uuid": "Need to improve",
            "option": "Need to improve"
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
