# Source: https://docs.deepconverse.com/product-docs/conversational-flow-builder/conversation-blocks/salesforce-blocks/agent-availability-block.md

# Agent Availability Block

{% hint style="info" %}
The Salesforce connector is available is part of the **Enterprise** plan
{% endhint %}

You can make use of the **Salesforce - Agent Availability** block to check if the agents are available to do live chat in a specific group.

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FzHfMSwge9jUGOJQ1zfdK%2Fimage.png?alt=media&#x26;token=11964f5a-3c50-4d09-bcef-3ae58b1b5d23" alt=""><figcaption></figcaption></figure>

### Setup

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FSv0baQ3ljvRYxWw0JfK5%2Fimage.png?alt=media&#x26;token=c3bb9a10-e004-4b13-ac37-6a72744aeac9" alt=""><figcaption></figcaption></figure>

You will need to define the following parameters:

1. Live Agent Url
2. Salesforce Organization Id
3. Deployment Id
4. Button Id

Once you define the node, the node will check for availability of agents and then set the parameter

```
availability = available (if agents are available)
availability = no (if no agents are available)
```

You can then use the parameter in subsequent rules to route the conversation accordingly.
