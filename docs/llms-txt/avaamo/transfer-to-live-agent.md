# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/transfer-to-live-agent.md

# Transfer to live agent

You can transfer to a live agent using [Agent.transfer](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/agent.transfer) method in JS.

Consider that in the MacPizza agent, for user intent, the response leads to an unhandled query. You can provide an option to transfer to a live agent. The following is a sample JS to transfer to a live agent:

```javascript
Agent.transfer();
return "I am sorry, I am still learning. Transferring to an Agent for more assistance.";
```

The following response is displayed in the agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FkpbWLS8hJS1rGxTcizAb%2Fimage.png?alt=media\&token=b366fae9-cb2b-4393-a067-ec64907be04b)

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to)
{% endcontent-ref %}
