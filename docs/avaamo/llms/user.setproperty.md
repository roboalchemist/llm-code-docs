# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperty.md

# User.setProperty

Sets the user property of the specified key to the indicated value. The value can be a single value or an array of values.

If you wish to set multiple user properties with different key-value pairs, then use `User.setProperties`. See [User.setProperties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperties), for more information.

**Syntax**:

<pre class="language-javascript"><code class="lang-javascript">User.setProperty("&#x3C;&#x3C;key>>","&#x3C;&#x3C;value>>")  

<strong>User.setProperty("&#x3C;&#x3C;key>>",["&#x3C;&#x3C;value1>>","&#x3C;&#x3C;value2>>",...])
</strong>
… - Indicates one or more parameter
</code></pre>

### **Parameters**

* **key** - This can be any of the attributes in the user object or can be any custom user-defined properties. See [Attributes](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/context/user#attributes), for more information.
* **value** - This is a string value the specified key is set to. You can also set an array of values to the specified key.

{% hint style="success" %}
**Key point**: To get the value of the attributes set in the user object, you can use `context.user.<<key>>`. If you have set any other custom user properties, then you can use `context.user.custom_properties.<<key>>` to get the value of the set property.
{% endhint %}

### **Examples**

<table><thead><tr><th width="354">Examples</th><th>How to get the value?</th></tr></thead><tbody><tr><td>User.setProperty("last_name","Williams")</td><td>context.user.last_name </td></tr><tr><td>User.setProperty("customerType","guest")</td><td>context.user.custom_properties.customerType </td></tr><tr><td>User.setProperty("country",["India","Australia"])</td><td>context.user.custom_properties.country</td></tr></tbody></table>

See [Set user property](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/set-user-property), for a sample scenario.
