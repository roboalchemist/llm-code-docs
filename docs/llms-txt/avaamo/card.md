# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card.md

# Card response (Javascript)

You can add customized input cards and links as skill responses in a JS node. The following is the syntax to add a customized card input:

```yaml
"card": {
 "notification_message": "<<custom_feedback_message>>", 
 "title": "<<card_title>>",
 "description": "<<card_description>>",
 "showcase_image_path": "<<image_URL>>",
 "links": [{
 <<customized card links>>
 },...]
 "inputs": [{
 <<customized card input>>
 },...]
}
… - Indicates one or more parameter
```

{% hint style="success" %}
**Key points**:&#x20;

* All the image types and sizes supported in the card input UI are also applicable when specifying images in the card input JS.
* There is a 191-character limit for all the user-defined text fields except the description field. You can specify upto 60000 characters in the `description` field.
* You can add upto 25 form elements to a card.
* Note the following points regarding Custom feedback. See [Custom feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/custom-feedback), for more information.
  * Not all Card elements are supported in Custom feedback. See individual elements for more information.&#x20;
  * Currently, any media content including images is not supported in Custom feedback.
* If the agent response contains sensitive PII data such as name, account number, and password, then it is recommended to mask the agent responses to protect user privacy. See [Agent response masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking#masking-agent-responses), for more information.
  {% endhint %}

<table><thead><tr><th width="233">Attribute</th><th width="399.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>notification_message</td><td><p>Indicates the message displayed by the agent after providing custom user feedback. Note that this attribute is applicable only when you are using the custom feedback option. </p><p></p><p>See <a href="../../../../../../build-agents/configure-agents/custom-feedback#example-positive-feedback">Custom feedback</a>, for an example. For example, in this message, you can say "Thank you for your valuable feedback. We appreciate your time and response."</p></td><td>String</td></tr><tr><td>title</td><td>Indicates the title of the card.</td><td>String</td></tr><tr><td>description</td><td><p>Indicates the description of the card. </p><p></p><p>Note that the purpose of this field must be used to describe the element using simple text only. It is recommended to avoid using scripting in the description.</p></td><td>String</td></tr><tr><td>showcase_image_path</td><td>Indicates the image used for the card. See <a href="card/card-images">Card Images</a>, for more information.</td><td>Integer</td></tr><tr><td>inputs</td><td><p>Indicates an array of customized card inputs:</p><ul><li><a href="card/single-line-text">Single Line Text</a></li><li><a href="card/multi-line-text">Multi-Line Text</a></li><li><a href="card/date-and-time">Date and Time</a></li><li><a href="card/select-picklist">Select (Picklist)</a></li><li><a href="card/file-upload">File Upload</a></li><li><a href="card/polls">Polls</a></li><li><a href="card/checklist">Checklist</a></li><li><a href="card/rating">Rating</a></li></ul></td><td>An array of JSON key-value pairs.</td></tr><tr><td>links</td><td><p>Indicates an array of customized card links such as Post Message, Web Page, Deep Link, Navigation link (hidden_content), and Web View. </p><p></p><p>See <a href="card/card-links">Card Links</a>, for more information.</p></td><td>An array of JSON key-value pairs</td></tr></tbody></table>
