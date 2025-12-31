# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperties.md

# User.setProperties

Sets the user property of the specified key to the indicated value. To set multiple user properties, you can specify a comma-separated list of key-value pairs in the `User.setProperties` method.&#x20;

**Syntax:**

{% code overflow="wrap" %}

```javascript
User.setProperties({"<<key1>>":"<<value1>>","<<key2>>":"<<value2>>","<<key3>>":"<<value3>>",...})

User.setProperties({"<<key1>>":["<<value1>>","<<value2>>",...],"<<key2>>":["<<value1>>","<<value2>>",...],...})

... - Indicates one or more parameter
```

{% endcode %}

### **Parameters**

* **key** - This can be any of the attributes in the user object or can be any custom user-defined properties. See [Attributes](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/context/user#attributes), for more information.
* **value** - This is a string value the specified key is set to. You can also set an array of values to the specified key.

{% hint style="success" %}
**Key Point**: To get the value of the attributes set in the user object, you can use `context.user.<<key>>`. If you have set any other custom user properties, then you can use `context.user.custom_properties.<<key>>` to get the value of the set property.
{% endhint %}

### **Examples**

<table><thead><tr><th width="406">Examples</th><th>How to get the value?</th></tr></thead><tbody><tr><td><code>User.setProperties({"first_name":"david","last_name":"williams","id":"1123"})</code></td><td><code>Context.user.custom_properties</code> </td></tr><tr><td><code>User.setProperties({"student_name": ["david","sally","james" ],"guardian_name":["williams","gomez"]})</code></td><td><code>Context.user.custom_properties</code> </td></tr></tbody></table>
