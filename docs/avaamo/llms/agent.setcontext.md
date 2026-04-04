# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/agent.setcontext.md

# Agent.setContext

Sets the live agent context of the specified key to the indicated value before transferring to the live agent. To set multiple context values, you can specify a comma-separated list of key-value pairs in the `Agent.setContext` method.&#x20;

### **Syntax**

{% code overflow="wrap" %}

```javascript
Agent.setContext({"<<key1>>":"<<value1>>","<<key2>>":"<<value2>>","<<key3>>":"<<value3>>",...})

... - Indicates one or more parameter
```

{% endcode %}

### **Parameters**

* **key** - This can be any of the attributes in the user object or can be any custom user-defined properties. See [Attributes](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/context/user#attributes), for more information.
* **value** - This is a string value the specified key is set to.

{% hint style="success" %}
**Key Points**:&#x20;

* To get the value of the attributes set in the user object, you can use `context.user.<<key>>`. If you have set any other custom user properties, then you can use `context.user.custom_properties.<<key>>` to get the value of the set property.
* Alternatively, you also write any Javascript code to say make an API call, fetch the details, and then update the agent context. You can also update the agent context based on the user properties.&#x20;
  {% endhint %}

### **Example**

If you wish to transfer all the requests from "India" to say Team India rather than the default team, then you can set the agent context and use the same key in the routing rules. See [Example: Routing rule based on location](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/rule-based-routing#example-routing-rule-based-on-user-location), for a sample demonstration.&#x20;

This callback gets triggered before transferring to the live agent and hence can be used in setting the routing rules, to route the requests to different teams in the live agent system based on the location of the user. See [Rule-based routing](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/rule-based-routing), for more information.

`Agent.setContext({"location":"India"});`

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FIYN7jYzxFjCoGXB1c8KX%2FScreenshot%2003-07-2023%20at%2012.30%20(1).png?alt=media&#x26;token=1d4c87e1-8883-459f-8a04-ebdd1e3bfa11" alt=""><figcaption></figcaption></figure>
