# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.removeproperty.md

# User.removeProperty

Delete or remove the specified user property added for a user. See [User.setProperty](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperty) and [User.setProperties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperties), for more information on adding user properties in JS code.

**Syntax**:

```javascript
User.removeProperty("<<key>>")  
```

### **Parameters**

* **key** - This can be any of the attributes in the user object or can be any custom user-defined properties. See [Attributes](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/context/user#attributes), for more information.

{% hint style="success" %}
**Key Point**: To get the value of the attributes set in the user object, you can use `context.user.<<key>>`. If you have set any other custom user properties, then you can use `context.user.custom_properties.<<key>>` to get the value of the set property.
{% endhint %}

### **Examples**

<table><thead><tr><th width="406">Examples</th><th>How to verify?</th></tr></thead><tbody><tr><td><code>User.removeProperty("last_name")</code></td><td>Check the user profile in the Conversation History page. The property for the user is no longer available. See <a href="../../../../../build-agents/debug-agents/conversation-history#user-icon">User icon</a>, for more information.</td></tr><tr><td><code>User.removeProperty("customerType")</code></td><td>Check the user profile in the Conversation History page. The property for the user is no longer available. See <a href="../../../../../build-agents/debug-agents/conversation-history#user-icon">User icon</a>, for more information.</td></tr></tbody></table>
