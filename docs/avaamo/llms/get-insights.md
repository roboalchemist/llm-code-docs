# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/get-insights.md

# Get skill conversation insights

You can get the skill conversation insights using [context.insights](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/insights). Typically, insights can be used for troubleshooting purposes to analyze the skill flow and to create a better user experience.

Consider that in the MacPizza agent, for user intent, the response leads to an unhandled query. You can use **context.insights** to further analyze the skill flow. The following is a sample JS to get the insight details from the context object and display on the console:

```javascript
console.log(context.insights);
```

In the agent, the following details are displayed in the console:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F0QPugQFM720jnQCfm8F6%2Fimage.png?alt=media\&token=c9aed84e-49ed-4b66-975a-3e04c95b1737)

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to)
{% endcontent-ref %}
