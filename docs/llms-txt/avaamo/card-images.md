# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/card-images.md

# Card images

You can add a card image to a customized input card using **showcase\_image\_path**. Upload the image to your own repository such as GitHub and specify the same image URL in the card input.&#x20;

* Recommended image types: PNG, JPEG
* Recommended image size: 800px \* 420px (width to height)

{% hint style="info" %}
**Notes**:&#x20;

* There is a 191-character limit for all the user-defined text fields.
* For security reasons, by default, you can upload upto 10 files in a span of 60 seconds. The number of files and the frequency or interval within which they can be uploaded is a configurable parameter. Contact Avaamo Support, for further assistance.
  {% endhint %}

```javascript
return [{
  "card": {
    "showcase_image_path": "<<image_URL>>",
    "inputs": [
      {
        "type": "picklist",
        "title": "Pick",
        "uuid": "opt",
        "options": [
          "Cheese",
          "Corn",
          "Tomato",
          "Onion"
        ]
      }
    ]
  }
}]
```

**Example**: The following is an example to add a card image:

{% code overflow="wrap" %}

```javascript
return [{
  "card": {
    "showcase_image_path": "https://raw.githubusercontent.com/john-lang/images/master/pizza.jpg",
    "inputs": [
      {
        "type": "picklist",
        "title": "Pick",
        "uuid": "opt",
        "options": [
          "Cheese",
          "Corn",
          "Tomato",
          "Onion"
        ]
      }
    ]
  }
}]
```

{% endcode %}

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response)
{% endcontent-ref %}
