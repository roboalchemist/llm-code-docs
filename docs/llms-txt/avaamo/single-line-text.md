# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/single-line-text.md

# Single line text

You can add a single-line input card in the skill response.&#x20;

## Syntax

The following is the syntax to add a single line of text in the card input:

{% hint style="info" %}
**Notes**:&#x20;

* There is a 191-character limit for all the user-defined text fields.
* **hint** attribute is not supported in the Microsoft Teams channel due to the limitations on the channel's side. See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS teams channel.
  {% endhint %}

```yaml
"card": {
 "inputs": [{
 "type": "single_line_text",
 "title": "<<text_title>>",
 *"sub_type": "<<single_text_subtype>>",
 *"should_validate": true/false,
 *"hint": "<<hint_text>>",
 *"format": "<<format>>",
 *"regex_format": "<<regex_format>>",
 *"default_value": "<<default_text>>",
 *"uuid": "<<secure_random_uuid>>"
 },...]
}

* - Indicates optional parameter
… - Indicates one or more parameter
```

<table><thead><tr><th width="184.33333333333331">Attribute</th><th width="467.14496873223425">Description</th><th>Type</th></tr></thead><tbody><tr><td>title</td><td>Indicates the title of the text field.</td><td>String</td></tr><tr><td>sub_type</td><td><p>Indicates the text subtype. Supported values:</p><ul><li><strong>password</strong>: Masks the characters entered by the user.</li><li><strong>number</strong>: Allows a user to enter only numbers. A number scroll is provided to increment and decrement numbers.</li><li><strong>email</strong>: Validates if the email is in the required format. You can use a hint to indicate the expected format.</li><li><strong>url</strong>: Validates if the URL is in the required format. You can use a hint to indicate the expected format.</li></ul></td><td>String</td></tr><tr><td>should_validate</td><td>Indicates if the user can skip entering values for the field or not before submitting. By default, the value is set to true.</td><td>Boolean</td></tr><tr><td>hint</td><td>Indicates a sample hint for the user to enter the value in the field. This is displayed in the input field before the user enters a value.</td><td>String</td></tr><tr><td>format</td><td><p>Indicates the format in which the data is collected. The data entered by the user is automatically converted into the specified format.</p><p>Typically, can be used for a number field to collect time or phone numbers. Example: xx:xx, xxxxxxxxxx</p></td><td>String</td></tr><tr><td>regex_format</td><td>Indicates regex validation to be performed on the field before submission.</td><td>String</td></tr><tr><td>default_value</td><td>Indicates the default value displayed in the text field when rendered to the user.</td><td>String</td></tr><tr><td>uuid</td><td><p>Indicates a secure random UUID that can be used later to get the text entered by the user. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information.</p><p></p><p>Text entered by the user is available in the</p><p><a href="https://docs.google.com/document/d/1kLeCPObAeXeon6viGnywY3_9HQxSmfs-YS-xB561Ekg/edit#heading=h.sprg97pwog6">context.last_message</a>.</p><p>Syntax: context.last_message.&#x3C;&#x3C;uuid>> or context.last_message["&#x3C;&#x3C;uuid>>"]</p></td><td>String</td></tr></tbody></table>

### Example 1

The following is a sample JS to provide a single text field in card input with different options:

```yaml
return[{
  "card": {
    "links": [
      {
        "type": "web_page",
        "title": "MacPizza Website",
        "url": "https://www.macpizza.com/"
      }
    ],
    "inputs": [
      {
        "type": "single_line_text",
        "title": "First Name",
        "uuid": "bad85eb9-0713-4da7-8d36-07a8e4b00eab",
        "regex_format": "^[a-zA-Z]+$"
      },
      {
        "type": "single_line_text",
        "title": "Last Name",
        "uuid": "f382d89b-8c91-405f-80ce-422ce51cb70f",
        "should_validate": false
      },
      {
        "type": "single_line_text",
        "title": "Password",
        "sub_type": "password",
        "uuid": "e8b6b922-44b9-4f34-8e70-f371ccfff3ad"
      },
      {
        "type": "single_line_text",
        "title": "Email",
        "sub_type": "email",
        "uuid": "22980238-a32c-45e9-bcdb-fbd8c51492b2",
        "hint": "xxx@yyy.com"
      },
      {
        "type": "single_line_text",
        "title": "Phone number",
        "sub_type": "number",
        "uuid": "19189953-301e-4e03-b51d-c42dc1088ed4",
        "format": "xxxxxxxxxx"
      },
      {
        "type": "single_line_text",
        "title": "Blog URL",
        "sub_type": "url",
        "uuid": "a294f28d-3fda-4bcf-996e-1d914f7aa86a"
      }
    ]
  }
}]
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FcffLbbk4gGvdahiHcx6h%2Fimage.png?alt=media\&token=12f7762d-8f03-40ce-bc06-b7ca16089c7c)

You can use `context.last_message.<<uuid>>` to get the text entered by the user.

{% hint style="success" %}
**Key Points:**

* You can submit even without entering details of the Last Name since "should\_validate" is set **false** for the field.
* Since the **email** field is set with **sub\_type** as **email**, on submission, the system validates if the email syntax is correct. However, it doesn’t validate if the email exists or not. The hint provides a sample example of the expected format for the email field.
* Since the **phone number** field is set with **sub\_type** as a **number** and with a format, the numbers entered by the user are automatically converted into the specified format.
* Since the **blog URL** field is set with **sub\_type** as **url**, on submission, the system validates if the URL syntax is correct. However, it doesn’t validate if the URL exists or not.
  {% endhint %}

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response)
{% endcontent-ref %}
