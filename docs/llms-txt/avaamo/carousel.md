# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/carousel.md

# Carousel response (Javascript)

You can add a customized carousel in the skill responses. A carousel is an array of card inputs. See [Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card), for more information.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* You cannot add form elements such as picklist, rating, checklist in the carousel. See [Add Form Elements](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-form-elements), for more information.
* There is a 191 character limit for all the user-defined text fields.
* If the agent response contains sensitive PII data such as name, account number, password, then it is recommended to mask the agent responses to protect user privacy. See [Agent response masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking#masking-agent-responses), for more information.
  {% endhint %}

### Syntax

Broadly, the following is the syntax to add a customized card input:<br>

```yaml
"carousel": {
   "cards": [{
    <<customized cards>>
    },...]
}
… - Indicates one or more parameter
```

| Attribute                                                                                                                                  | Description                             | Type                             |
| ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- | -------------------------------- |
| [cards](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card) | Indicates an array of customized cards. | An array of JSON key-value pairs |

### Examples

Example: The following is a sample JS for carousel skill response:

```javascript
return [{
    "carousel": {
        "title": "Payment Method",
        "cards": [
        {
                "card": {
                    "title": "NetBanking",
                    "links": [{
                        "type": "post_message",
                        "title": "confirm",
                        "value": "confirm"
                    }]
                }
            },
            {
                "card": {
                    "title": "Cash on Delivery",
                    "links": [{
                        "type": "post_message",
                        "title": "confirm",
                        "value": "confirm"
                    }]
                }
            },
        ]
    }
}];

```

In the skill, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FBkQyLj953O5cl4mlPTGe%2Fimage.png?alt=media\&token=cb5b5b83-bad9-4e8d-9904-fa8484e211c7)
