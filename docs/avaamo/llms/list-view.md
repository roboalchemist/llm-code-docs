# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/list-view.md

# ListView response (Javascript)

You can add a customized list view using JavaScript in an agent's response.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* There is a 191 character limit for all the user-defined text fields.
* If the agent response contains sensitive PII data such as name, account number, password, then it is recommended to mask the agent responses to protect user privacy. See [Agent response masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking#masking-agent-responses), for more information.
  {% endhint %}

### Syntax

Broadly, the following is the syntax to add a customized list view:

```yaml
"list_view": {
   *"top_element_style": "<<style_type>>",
   "items": [{
   "title": "<<item_title>>",
   *"subtitle": "<<item_subtitle>>",
   *"image_path": "<<image_url>>",
   "links": [{
    <<customized links>>
    },...]
   },...]
}
* - Indicates optional parameter
… - Indicates one or more parameter
```

<table><thead><tr><th width="197.82599529326916">Attribute</th><th width="358.71637120354313">Description</th><th>Type</th></tr></thead><tbody><tr><td>top_element_style</td><td><p>Indicates the style type for the list view. Supported values - Large, Compact. </p><p></p><p>Default value is Large.</p></td><td>String</td></tr><tr><td>items</td><td><p>Indicates the array of items in the list view. You can add upto 50 items to the list. Each item contains the following details:</p><ul><li>title: Title of the item</li><li>subtitle: Sub-title of the item</li><li>image_path: Image used for the item. You can add an image similar to the way you add an image to a card. See <a href="card/card-images">Card Images</a>, for more information.</li><li>links: An array of customized card links such as Post Message, Web Page, Deep Link, and Web View.</li></ul></td><td>Array</td></tr><tr><td>links</td><td><p>Indicates an array of customized list view links such as Post Message, Web Page, Deep Link, and Web View. </p><p></p><p>All the link types supported for card links are available in the list view also. See <a href="card/card-links">Card Links</a>, for more information.</p></td><td>An array of JSON key-value pairs.</td></tr></tbody></table>

### Example

The following is a sample JS for list view:

```yaml
return [{
    "list_view": {
        "top_element_style": "compact",
        "items": [{
                "title": "Coke",
                "subtitle": "All Chilled",
                "links": [{
                    "type": "post_message",
                    "title": "Get a pack of 5",
                    "value": "coke"
                }]
            },
            {
                "title": "Coffee",
                "subtitle": "Cold",
                "links": [{
                    "type": "post_message",
                    "title": "Buy one get one",
                    "value": "coffee"
                }]
            }
        ]
    }
}];
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FtO4oZANmzVJScykBmuQT%2Fimage.png?alt=media\&token=70fffb3e-2b43-49c9-93a8-d1f4cff985a3)
