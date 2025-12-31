# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/card-links.md

# Card links

You can add customized card links in the skill response.&#x20;

## Syntax

The following is the syntax to add customized card links:

{% hint style="info" %}
**Notes**:&#x20;

* There is a 191-character limit for all the user-defined text fields.
* Currently, in the custom feedback, the post\_message type is not supported. See [Custom feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/custom-feedback), for more information.
  {% endhint %}

```json
"card": {
 "links": [{
 "type": "<<link_type>>",
 "title": "<<link_title>>",
 *"url": "<<link_url>>",
 *"value": "<<link_value>>",
 *"srcdoc": "<<source_doc>>",
 *"webview_height_ratio": "<<view_type>>",
 *"hidden_content": "<<hidden_content>>",
 *"format": "<<date_picker_format>>"
 *"minDate": "<<date_picker_start_date>>",
 *"maxDate": "<<date_picker_end_date>>"
 },...]
}
 * - Indicates optional parameter
… - Indicates one or more parameter
```

<table><thead><tr><th width="222">Attribute</th><th width="426.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>type</td><td><p>Indicate the type of link. Supported values:</p><ul><li>web_page</li><li>post_message</li><li>deeplink. Note that this value is deprecated from v6.4.0 onwards. See <a href="../../../../../../../../release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice">Deprecation notice</a>, for more information. </li><li>web_view_srcdoc</li><li>web_view_url</li><li>date</li></ul></td><td>String</td></tr><tr><td>title</td><td>Indicates the title of the link.</td><td>String</td></tr><tr><td>url</td><td>Indicates the URL of the link. </td><td>String</td></tr><tr><td>value</td><td>Indicates the value of the link.</td><td>String</td></tr><tr><td>srcdoc</td><td><p>Indicate the HTML document to display in a</p><p>web view; all styles must be inline. <br></p><ul><li>Webview (HTML) supports upto 65000 characters. If you have a requirement to use a larger HTML, then it is recommended to use <a href="#web-view-url">Webview (URL)</a> option. </li><li>Specify HTML in the proper standard format. Include all the required elements such as HTML, HEAD, TITLE, and BODY. The "title" tag is displayed in the popup title. If you wish to omit the "title" tag, then it is still recommended to include an empty "title" tag, so that it adheres to proper HTML standards.</li></ul></td><td>String</td></tr><tr><td>webview_height_ratio</td><td><p>Indicates the view type of web view document</p><p>such as Compact, Tall, Full.</p></td><td>String</td></tr><tr><td>hidden_content</td><td><p>Indicates hidden content not visible to the user. Typically, used for navigation flow such as the Goto node, and to start over the conversation from the beginning. See <a href="#hidden_content">hidden_content</a>, for more information.</p><p></p><p>Note that when you have <code>hidden_content</code> in the Card links, the text displayed is as mentioned in the <code>value</code> and the <code>context.last_message</code> or the processed message in query insight contains <code>hidden_content.</code> See <a href="../../../reference-library/context">Context</a> and <a href="../../../../../../../build-agents/debug-agents#using-insights">Message insights</a>, for more information.</p><p></p><p>This is an optional attribute.  </p></td><td>String</td></tr><tr><td>format</td><td>Indicates the format of the date picker. This is an optional attribute.  </td><td>String</td></tr><tr><td>minDate</td><td>Indicates the minimum date in the date picker link.  minDate value must be specified in the same format used for the date picker. This is an optional attribute.  </td><td>String</td></tr><tr><td>maxDate</td><td>Indicates the maximum date in the date picker link.  maxDate value must be specified in the same format used for the date picker. This is an optional attribute.  </td><td>String</td></tr></tbody></table>

## Examples

### Post message link

The following is a sample JS for the Post Message link:

```javascript
return [{
  "card": {
    "title": "NetBanking",
    "links": [
      {
        "type": "post_message",
        "title": "confirm",
        "value": "confirm"
      }
    ]
  }
}]
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FQM3IMSoMLx7FgUTgNe6A%2Fimage.png?alt=media\&token=efa03e3b-77f9-40b1-81b0-7552bb17a7a6)

### Web page link

The following is a sample JS for Web Page link:

```javascript
return [{
  "card": {
    "links": [
      {
        "type": "web_page",
        "title": `<div style="text-align:center;"><b> Mac Pizza Website </b></div>`,
        "value": "https://www.macpizza.com/"
      }
    ],
    "inputs": [
      {
        "type": "single_line_text",
        "title": "First Name",
        "uuid": "firstName",
        "default_value": "John"
      },
      {
        "type": "single_line_text",
        "title": "Last Name",
        "uuid": "lastName",
        "default_value": "Creek"
      }
    ]
  }
}]
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FkW4SKoEQlrlxYwiZ1U8I%2Fimage.png?alt=media\&token=0406d184-3012-44b4-bbe0-c5efa16755a2)

### Date picker link

Use the following format to provide a date picker in a quick reply response. Here, `date_format` is any date format that you wish to display in the agent.&#x20;

```javascript
return [{
    "card": {
        "links": [{
            "title": "Promotional offer! Pick a free pizza delivery date.",
            "type": "date",
            "format": "DD/MM/YYYY"
        }]
    }
}]
```

In the agent, the following response is displayed with a date picker link button:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbRv3x7k4pNtghUUzJbJK%2FScreenshot%202023-01-30%20at%203.12.06%20PM.png?alt=media\&token=b8b53435-07c6-4cda-b232-a2c5785d170f)

Click the link to display the date picker:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FpakZE0x6MWE85lhPcCCT%2FScreenshot%202023-01-30%20at%203.13.54%20PM.png?alt=media\&token=6424945b-f90c-4f9a-aaae-685e7b0847c2)

{% hint style="danger" %}
**Deprecated**:  You can also use`avaamo:#app/datepicker/messages/new?format=<<date_format>>`, for providing a date picker in the Card response.&#x20;

{% code overflow="wrap" %}

```javascript
return [{
    "card": {
        "links": [{
            "title": "Promotional offer! Pick a free pizza delivery date.",
            "type": "deeplink",
            "value": "avaamo:#app/datepicker/messages/new?format=DD/MM/YYYY"
        }]
    }
}]
```

{% endcode %}

However, using `deeplink in the type parameter` and `specifying the URL in the value parameter` is deprecated from the v6.4.0 release onwards. See [Deprecation notice](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice), for more information. &#x20;
{% endhint %}

### Date picker link with minimum and maximum dates

Use the following format to provide a date picker in a quick reply response. Here, `date_format` is any date format that you wish to display in the agent.&#x20;

```javascript
return [{
    "card": {
        "links": [{
            "title": "Promotional offer! Pick a free pizza delivery date.",
            "type": "date",
            "format": "YYYY-DD-MM",
            "minDate": "2022-25-04",
            "maxDate": "2022-30-04"
        }]
    }
}]
```

In the agent, the following response is displayed with a date picker link button:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbRv3x7k4pNtghUUzJbJK%2FScreenshot%202023-01-30%20at%203.12.06%20PM.png?alt=media\&token=b8b53435-07c6-4cda-b232-a2c5785d170f)

Click the link to display the date picker

{% hint style="danger" %}
**Deprecated**:  You can also use`avaamo:#app/datepicker/messages/new?format=<<date_format>>`, for providing a date picker in the Card response.&#x20;

{% code overflow="wrap" %}

```javascript
return [{
    "card": {
        "links": [{
            "title": "Promotional offer! Pick a free pizza delivery date.",
            "type": "deeplink",
            "value": "avaamo:#app/datepicker/messages/new?format=DD/MM/YYYY&minDate=1650877346000&maxDate=165130934600"
        }]
    }
}]
```

{% endcode %}

However, using `deeplink in the type parameter` and `specifying the URL in the value parameter` is deprecated from the v6.4.0 release onwards. See [Deprecation notice](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice), for more information.&#x20;
{% endhint %}

### Goto\_node

Use `#goto_node_<<skill_key>>.<<intent_key>>`in the `hidden_content` parameter of the card JS to navigate to a specific node in the flow.

```javascript
return [{
    "card": {
        "links": [{
            "title": "Order just starters for now",
            "type": "post_message",
            "value": "Get starters",
            "hidden_content": "#goto_node_macpizza_order.starters"
        }]
    }
}]
```

In the agent, the following response is displayed. When you click the title link, it navigates to the corresponding goto node as specified in the quick reply JS:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FGRtiqnBwBbKg7JsgigRU%2FScreenshot%202023-01-30%20at%203.39.52%20PM.png?alt=media\&token=43836763-bef3-4fb8-a2ff-1cca226a687b)

{% hint style="danger" %}
**Deprecated**:  You can also use `avaamo:#messages/hidden/%23goto_node_<skill_key>>.<<intent_key>>/new/<<message>>,`for navigation to a different node in the conversation flow. &#x20;

{% code overflow="wrap" %}

```javascript
return [{
    "card": {
        "links": [{
            "title": "Just order starters for now",
            "type": "deeplink",
            "value": "avaamo:#messages/hidden/%23goto_node_macpizza_order.starters/new/Get starters"
        }]
    }
}]
```

{% endcode %}

However, using `deeplink in the type parameter` and `specifying the URL in the value parameter` is deprecated from the v6.4.0 release onwards. See [Deprecation notice](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice), for more information.&#x20;
{% endhint %}

### Start\_over

Use `start over`in the `hidden_content` parameter of the quick reply JS to reset the current conversation and displays the greeting message. Note that this does not create a new conversation UUID.&#x20;

```javascript
return [{
    "card": {
        "links": [{
            "title": "Order from the start",
            "type": "post_message",
            "value": "Start over",
            "hidden_content": "start over"
        }]
    }
}]
```

Click the `Order from the start` title link to start the conversation from the beginning:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FzIdUJ0slMICx9lzYJUDf%2FScreenshot%202023-01-30%20at%203.46.03%20PM.png?alt=media\&token=dafe6971-4888-473b-84cf-0d804e563d21)

{% hint style="danger" %}
**Deprecated**: You can also `use avaamo:#messages/hidden/start%20over/new/<<message>>,`to start over the conversation from the greeting message.

{% code overflow="wrap" %}

```javascript
return [{
    "card": {
        "links": [{
            "title": "Order from the start",
            "type": "post_message",
            "value": "Start over",
            "hidden_content": "start over"
        }]
    }
}]

```

{% endcode %}

However, using `deeplink in the type parameter` and `specifying the URL in the value parameter` is deprecated from the v6.4.0 release onwards. See [Deprecation notice](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice), for more information.&#x20;
{% endhint %}

### Web view

The following is a sample JS for Web view:

{% code overflow="wrap" %}

```yaml
return [{
  "card": {
    "links": [
      {
        "title": "Disclaimer",
        "type": "web_view_srcdoc",
        "srcdoc": '<html><head><title> </title></head><body><h1 style="margin-left:25px; color:red;"><b>Disclaimer</b><br><br></h1><p style="margin-left:25px; margin-right:25px;"><i>This is a <b>tentative assessment</b> based on limited information and generalized practice, so please treat it as <b>directional guidance</b> only.</i></p></body></html>',
        "webview_height_ratio": "compact"
      }
    ],
    "inputs": [
      {
        "type": "data_capture",
        "title": "How was our service?",
        "uuid": "comments",
        "default_value": "Excellent service with prompt delivery!!!"
      }
    ]
  }
}]
```

{% endcode %}

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJI7qcQdnlqWxdZZaQbNB%2Fimage.png?alt=media\&token=897e1b23-5bc6-4061-9cd0-8a9c8533f2e4)

### Web view URL

The following is a sample JS for Web view URL:

{% hint style="info" %}
**Notes**:&#x20;

* The URL must be accessible without any privacy and security restrictions from the agent.
* The link you are using must be allowed to be opened in an iframe.
* Ensure that you have whitelisted all the URLs that are rendered inside the Team's web view or Task Module in the Teams App. See [Microsoft teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information.
  {% endhint %}

```yaml
return [{
  "card": {
    "links": [
      {
        "type": "web_view_url",
        "title": "Mac Pizza website",
        "value": "https://www.macpizza.com/"
      }
    ],
    "inputs": [
      {
        "type": "data_capture",
        "title": "How was our service?",
        "uuid": "comments",
        "default_value": "Excellent service with prompt delivery!!!"
      }
    ]
  }
}]
```

### Mail link

The following is a sample JS for mail URL:

```yaml
return {
  "card": {
    "title": "Write to us",
    "description": "Let us know what you think",
    "links": [
       {
        "url": "mailto:macpizza@gmail.com",
        "type": "web_page",
        "title": "email"
      }
    ]
  }
}
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJhPkOFciH3xFRLsm0mzU%2Fimage.png?alt=media\&token=e66e398a-b565-415a-8047-7960e2c0d820)

You can click "email" to send an email to the specified email address.

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response)
{% endcontent-ref %}
