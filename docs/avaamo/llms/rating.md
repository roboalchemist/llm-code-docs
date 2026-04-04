# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/rating.md

# Rating

You can add an input card with a rating system in the skill response.&#x20;

### Syntax

The following is the format to add a rating response:

{% hint style="info" %}
**Note**: There is a 191 character limit for all the user-defined text fields.
{% endhint %}

```yaml
"card": {
 "inputs": [{
 "type": "rating",
 "title": "<<rating_title>>",
 "uuid": "<<secure_random_uuid>>"
 }]
}
```

<table data-header-hidden><thead><tr><th>Attribute</th><th width="320.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td><strong>Attribute</strong></td><td><strong>Description</strong></td><td><strong>Type</strong></td></tr><tr><td>title</td><td>Indicates the title of the rating card.</td><td>String</td></tr><tr><td>uuid</td><td><p>Indicates a secure random UUID that can be used later to get the text entered by the user. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information. </p><p></p><p>Option selected by the user is available in the context.last_message.</p><p>Syntax: context.last_message.&#x3C;&#x3C;uuid>></p></td><td>String</td></tr></tbody></table>

### Example

The following is a sample JS to specify rating in response:

```yaml
return {
  "card": {
    "inputs": [
      {
        "title": "Rate our service",
        "type": "rating",
        "uuid": "784cc8d5-b3d0-4cbc-89c4-4ef3c2fa43ea"
      }
    ]
  }
}
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F8OSIN4Kq93cssAYWXdDm%2Fimage.png?alt=media\&token=5ce2e397-5433-4ea8-bcd9-0a18d30eb783)

You can use `context.last_message.<<uuid>>` to get the option selected by the user.

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response)
{% endcontent-ref %}
