# Source: https://developers.make.com/custom-apps-documentation/best-practices/naming-conventions/modules/modules-names.md

# Modules names

Module names are unique identifiers for each module in your app.

They are internal names and differ from the [module labels](https://developers.make.com/custom-apps-documentation/best-practices/naming-conventions/modules/module-labels) that a user sees when using the app.

Module names:

* must be between 3 and 48 characters long
* must match pattern `/^[a-zA-Z][0-9a-zA-Z]+[0-9a-zA-Z]$/`

{% hint style="info" %}
A module name should not match any reserved word in JavaScript. See the list of reserved words in JavaScript [here](https://www.w3schools.com/js/js_reserved.asp).
{% endhint %}
