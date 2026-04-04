# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/show-ambiguous-intents.md

# Show ambiguous intents

You can use a set of closely matched intents to show the most "common questions" that are related to a user’s query in a particular context. This feature helps you to anticipate other questions that users might have as a follow-up that you can show in a section such as "Here’s related content" or as "Other Common Questions".&#x20;

You can show the best answer and additionally show three “common questions” from the curated set of responses that are related to the user query. This feature can help in:&#x20;

* Reducing false positives and providing more options from a similar set of responses already available in the agent.&#x20;
* Providing a pleasant user experience where the agent attempts to provide the best possible answers from all possible available options in the agent.
* Providing guided navigation that allows users to explore more options.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Ft09Q6Bhsv4Hqqc5YQZej%2Fimage.png?alt=media\&token=42fabbf3-ec46-497c-a20a-383f1e2aa965)

{% hint style="success" %}
**Key Point**: You can achieve this functionality only when you have a set of responses applicable to the same context of a user query.
{% endhint %}

This example shows how to loop through the ambiguous intents in the pre-unhandled node.

**To show common questions:**

* You must have a Dialog skill with a pre-unhandled node in the invocation intent. See [Add invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent), for more information.
* In the JS of the pre-unhandled node, get a list of ambiguous intents from context.insights - context.insights.ambiguous\_intents

```javascript
if (!!context.insights.ambiguous_intents) {
    var common_questions = renderCommonQuestions(
       context.insights.ambiguous_intents
    );
}
```

* Loop through the top three disambiguous intents and add it to card links to display to the user. The following is a sample code:

<pre class="language-javascript"><code class="lang-javascript"><strong>var renderCommonQuestions = (ambiguous_intents, display_num = 3) => {
</strong>    // Purpose: render list response for other common questions
    // Input: list of ambiguous intents
    // Output: list
    var common_links = [];
    for (var intent of ambiguous_intents) {
        common_links.push({
            type: "post_message",
            title: intent.document,
            value: intent.document
        })
        if (common_links.length === display_num) {
            break;
        }
    }
    var common_questions = {
        card: {
            description: "&#x3C;b>Other Common Questions&#x3C;/b>",
            links: common_links
        }
    };
    return common_questions;
}  
</code></pre>
