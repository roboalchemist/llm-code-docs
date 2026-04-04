# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/set-user-property.md

# Set user property

You can use **User.setProperty** to set the user property of the specified key to the indicated value. See [setProperty](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperty), for more information.

{% hint style="info" %}
**Note**: To set multiple user properties, you can use `User.setProperties` method. See [User.setProperties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperties), for more information.
{% endhint %}

### Example 1: Set user property to a single value

Consider that when a user starts interacting with the MacPizza agent, you wish to check if the user is registered and if the user is not registered, then you wish to set the `customerType` property of a user to `guest`.

The following is a sample JS to set the user property:

```javascript
User.setProperty("customerType","guest");
```

The following is a sample JS to get the user property that is displayed in the console:

```javascript
console.log("Customer type is " + context.user.custom_properties.customerType);
```

You can also view the set user properties in the user conversation history. See [Conversation history](https://docs.avaamo.com/user-guide/build-agents/debug-agents#using-conversation-history), for more information:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LzM4xB0NnvEope3XqkK%2F-LzM6N9pvR3Uyc0CUaqV%2Fjs-user-property.png?alt=media\&token=8034a574-fea8-4bac-9982-aefe50803992)

### Example 2: Set user property to an array of values

Consider that an employee works out of two locations - `India` and `Australia` and you wish to set the `country` user property to both of these values.

The following is a sample JS to set the user property to an array of values:

```javascript
User.setProperty("country",["India","Australia"]);
```

The following is a sample JS to get the user property that is displayed in the console:

```javascript
console.log("Customer type is " + context.user.custom_properties.country);
```

You can also view the set user properties in the user conversation history. See [Conversation history](https://docs.avaamo.com/user-guide/build-agents/debug-agents#using-conversation-history), for more information:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F8rcKIsPth8JT9UgGJfmI%2Fimage.png?alt=media&#x26;token=33cba45e-73a5-4644-bab3-da3102a873a4" alt=""><figcaption></figcaption></figure>
