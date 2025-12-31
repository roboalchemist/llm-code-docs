# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/quick-reply.md

# Quick Reply response (Javascript)

You can use a quick reply to add an acknowledgment to the user’s questions or responses.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* There is a 191-character limit for all the user-defined text fields.
* **Date Picker** link for Quick Reply is not supported in the Microsoft Teams channel due to the limitations on the channel's side. See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.
* If the agent response contains sensitive PII data such as name, account number, password, then it is recommended to mask the agent responses to protect user privacy. See [Agent response masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking#masking-agent-responses), for more information.
  {% endhint %}

## Syntax

The following is the syntax to add a quick reply response:

```yaml
quick_reply: {
    "content": "<<quick_reply_message_content>>",
    "links": [
      {
      "title": "<<link_title_1>>", 
      "type": "<<link_type_1>>", 
      "value": "<<link_value_1>>",
      *"format": "<<date_picker_format>>"
      *"minDate": "<<date_picker_start_date>>",
      *"maxDate": "<<date_picker_end_date>>"
     *"hidden_content": "<<hidden_content>>"
       },...
     ]
}
* - Indicates optional parameter
… - Indicates one or more parameter
```

<table><thead><tr><th width="150">Attribute</th><th width="429.1780104712042">Description</th><th>Type</th></tr></thead><tbody><tr><td>content</td><td>Indicates the message content of the quick reply response.</td><td>String</td></tr><tr><td>links</td><td><p>Indicates an array of links in the quick reply response. Each array contains:</p><ul><li><strong>title</strong>: Title of the link</li><li><p><strong>type</strong>: Type of link. Supported values are</p><ul><li>post_message </li><li>deeplink (used for providing links). Note that this value is deprecated from v6.4.0 onwards. See <a href="../../../../../../../release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice">Deprecation notice</a>, for more information. </li><li>date </li></ul></li><li><strong>value</strong>: Value of the link. Note that <code>value parameter with URLs</code> is deprecated from v6.4.0 onwards. See <a href="../../../../../../../release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice">Deprecation notice</a>, for more information.  </li><li><strong>hidden_conten</strong>t: Hidden content not visible to the user. Typically, used for navigation flow such as Goto node or start over. This is an optional attribute.</li><li><strong>format</strong>: Specify the format of the date picker link.</li><li><strong>minDate:</strong> Set the minimum date in the date picker link. minDate value must be specified in the same format used for the date picker.</li><li><strong>maxDate</strong>: Set the maximum date in the date picker link. maxDate value must be specified in the same format used for the date picker.</li></ul></td><td>An Array of JSON key-value pairs</td></tr></tbody></table>

## Examples

### Post message

The following is a sample JS to post a message in Quick reply:

{% code overflow="wrap" %}

```javascript
return [{
    quick_reply: {
        "content": "Would you like help with any of the following?",
        "links": [{
                "title": "Placing an order",
                "type": "post_message",
                "value": "Just mention type of pizza with your toppings and you are good to go."
            },
            {
                "title": "Kids Menu",
                "type": "post_message",
                "value": "All our menu items are customizable for kids."
            },
            {
                "title": "Others",
                "type": "post_message",
                "value": "We will connect with a customer service representative."
            }
        ]
    }
}]
```

{% endcode %}

In the agent, the following response is displayed with the provided quick reply links:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJcqpbdnt4gBV2U8nBP3P%2Fimage.png?alt=media\&token=3aacab4c-88a6-484e-bcef-c3b597894bef)

### Date picker

Use the following format to provide a date picker in a quick reply response. Here, `date_format` is any date format that you wish to display in the agent.&#x20;

```javascript
return {
    quick_reply: {
        "content": "Pick a delivery date",
        "links": [{
            "title": "Delivery date",
            "type": "date",
            "format": "DD/MM/YYYY"
        }]
    }
}
```

In the agent, the following response is displayed with a date picker link button:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FQv1PAdnsj0oS9xksYkve%2Fquick-reply-deeplink-delivery-date.png?alt=media\&token=744bc38c-7963-44ee-bde6-29eb2375419a)

{% hint style="danger" %}
**Deprecated**:  You can also use`avaamo:#app/datepicker/messages/new?format=<<date_format>>`, for providing a date picker in the Quick reply response.&#x20;

{% code overflow="wrap" %}

```javascript
return [{
    quick_reply: {
        "content": "Pick a delivery date",
        "links": [{
            "title": "Delivery date",
            "type": "deeplink",
            "value": "avaamo:#app/datepicker/messages/new?format=DD/MM/YYYY"
        }]
    }
}]
```

{% endcode %}

However, using `deeplink in the type parameter` and `specifying the URL in the value parameter` is deprecated from the v6.4.0 release onwards. See [Deprecation notice](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice), for more information.&#x20;
{% endhint %}

### Date picker with Min and Max dates

Use the following format to provide a date picker in a quick reply response. Here, `date_format` is any date format that you wish to display in the agent.&#x20;

```javascript
return {
    quick_reply: {
        "content": "Pick a delivery date",
        "links": [{
                "title": "Delivery dates",
                "type": "date",
                "format": "YYYY-DD-MM",
                "minDate": "2022-25-04",
                "maxDate": "2022-30-04"
            },
            {
                "title": "Registration",
                "type": "post_message",
                "value": "I want to order register at MacPizza."
            },
            {
                "title": "Order pizza",
                "type": "post_message",
                "value": "I want to order a pizza."
            }
        ]
    }
}
```

{% hint style="danger" %}
**Deprecated**:  You can also use`avaamo:#app/datepicker/messages/new?format=<<date_format>>&minDate=<<date in epoch format>>&maxDate=<<date in epoch format>>`, for providing a date picker in the Quick reply response.&#x20;

<pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript"><strong>return [{
</strong>    quick_reply: {
        "content": "Ok sure. Pick a delivery date",
        "links": [{
            "title": "Delivery date",
            "type": "deeplink",
            "value": "avaamo:#app/datepicker/messages/new?format=DD-MM-YYYY&#x26;minDate=1650877346000&#x26;maxDate=165130934600"
        }]
    }
}]
</code></pre>

However, using `deeplink in the type parameter` and `specifying the URL in the value parameter` is deprecated from the v6.4.0 release onwards. See [Deprecation notice](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice), for more information.&#x20;
{% endhint %}

### Goto node

Use `#goto_node_<<skill_key>>.<<intent_key>>`in the `hidden_content` parameter of the quick reply JS to navigate to a specific node in the flow.

{% code overflow="wrap" %}

```javascript
return [{
    quick_reply: {
        "content": "Would you like help with any of the following?",
        "links": [
          {
             "title": "Just starters for now",
             "type": "post_message",
             "value": "Get starters",
             "hidden_content": "#goto_node_macpizza_order.starters"
               
          },
            {
                "title": "Registration",
                "type": "post_message",
                "value": "I want to order register at MacPizza."
            },
            {
                "title": "Order pizza",
                "type": "post_message",
                "value": "I want to order a pizza."
            }
        ]
    }
}]


```

{% endcode %}

In the agent, the following response is displayed. When you click the Get Starters link button, it navigates to the corresponding goto node as specified in the quick reply JS:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F54Igokcmqda3oZqtmzIH%2Fquick-reply-deeplink-goto_1.png?alt=media\&token=38e12cd9-fb6d-4c0d-bcfb-9c81c8244b5c)

Click the `Just starters for now` button to navigate to the starter node directly:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXWx9kN9txO436XeLZlAO%2Fquick-reply-deeplink-goto_2.png?alt=media\&token=b57dc79e-4fef-4e8a-84ce-6d24ca594b1d)

{% hint style="danger" %}
**Deprecated**:  You can also `use avaamo:#messages/hidden/%23goto_node_<skill_key>>.<<intent_key>>/new/<<message>>,`for navigation to a different node in the conversation flow. &#x20;

{% code overflow="wrap" %}

```javascript
return [{
    quick_reply: {
        "content": "Would you like help with any of the following?",
        "links": [{
            "title": "Just starters for now",
            "type": "deeplink",
            "value": "avaamo:#messages/hidden/%23goto_node_order.starters/ new/Getstarters "
        }]
    }
}]
```

{% endcode %}

However, using `deeplink in the type parameter` and `specifying the URL in the value parameter` is deprecated from the v6.4.0 release onwards. See [Deprecation notice](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice), for more information. &#x20;
{% endhint %}

### Start over

Use `start over`in the `hidden_content` parameter of the quick reply JS to reset the current conversation and displays the greeting message. Note that this does not create a new conversation UUID.&#x20;

**Example**: The following is a sample JS to use a "Start over" in a quick reply:

{% code overflow="wrap" %}

```javascript
return [{
    quick_reply: {
        "content": "Confirm your order?",
        "links": [{
                "title": "Wrong order",
                "type": "post_message",
                "value": "Wrong order start again",
                "hidden_content": "start over"
            },
            {
                "title": "Place order",
                "type": "post_message",
                "value": "Confirm order."
            }

        ]
    }
}]


```

{% endcode %}

In the agent, the following response is displayed with a start-over link button:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fc0It6zYuZbC5DG6X7fDD%2Fquick-reply-deeplink-startover-2.png?alt=media\&token=c576d1f7-047d-4b7e-9928-fdd3ddd8494d)

Click the `Wrong order` button to start the conversation from the beginning:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FEPqjposf8nm9gNX65a9Y%2Fquick-reply-deeplink-startover-1.png?alt=media\&token=b61034a8-7006-40fd-a0c2-760db3553dc4)

{% hint style="danger" %}
**Deprecated**: You can also `use avaamo:#messages/hidden/start%20over/new/<<message>>`to start over the conversation from the greeting message.

{% code overflow="wrap" %}

```javascript
return [{
    quick_reply: {
        "content": "Confirm your order?",
        "links": [{
            "title": "Wrong order ",
            "type": "deeplink ",
            "value": "avaamo: #messages/hidden/start%20over/new/Wrong order"
        }]
    }
}]
```

{% endcode %}

However, using `deeplink in the type parameter` and `specifying the URL in the value parameter` is deprecated from the v6.4.0 release onwards. See [Deprecation notice](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0#deprecation-notice), for more information. &#x20;
{% endhint %}
