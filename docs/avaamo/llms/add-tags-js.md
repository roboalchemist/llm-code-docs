# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/add-tags-js.md

# Add tags (JS)

You can add tags dynamically to the skill response using `Tag.append('tag_name')`method. This is useful when you are dynamically constructing a response using JS and wish to add tags to the response.

{% hint style="info" %}
**Notes**:&#x20;

* You can only add tags that are configured in your agent. See [Add tags](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-tags), for more information on how to configure. If you add a tag that is not configured in your agent, then an error is thrown. You can view the error in Debug -> JS errors page. See[ Debug JS code](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/troubleshooting-tips), for more information.
* You can add only one tag`Tag.append('tag_name')`method. If you wish to add multiple tags, then you can call this method multiple times as required. You can associate 50 tags to a skill response.
  {% endhint %}

Consider that you are dynamically building a skill response using ListView. You can append tag before returning the response using Tag.append method:&#x20;

<pre class="language-javascript"><code class="lang-javascript"><strong>Tag.append('order');
</strong>
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
</code></pre>

{% hint style="info" %}
**Important:** `Tag.append` is deprecated; use `Tag.asyncAppend.`This method provides greater flexibility and simplifies implementation.
{% endhint %}

Use the example below:

```javascript
await(Tag.asyncAppend('order'));

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

You can view the top tags in the Analytics board. See [View analytics of top tags](https://docs.avaamo.com/user-guide/build-agents/monitor-and-analyze/analytics#top-tags), for more information on the "Top Tags" Analytics board.
