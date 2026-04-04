# Source: https://developers.make.com/custom-apps-documentation/app-components/iml-functions.md

# Custom IML functions

{% hint style="info" %}
Before getting started with custom IML functions, learn more about the the [Integromat Markup Language (IML)](https://developers.make.com/custom-apps-documentation/block-elements/iml).

Custom IML functions are not available by default. Contact us via our [helpdesk](https://www.make.com/en/ticket) if you need to create a custom IML function.
{% endhint %}

All built-in IML functions and your custom IML functions are available for you to use inside your own custom functions. You can access them in the `iml` namespace like this: `iml.parseDate()`.

A list of built-in IML functions is available [here](https://help.make.com/functions).

Only JavaScript built-in objects and Buffer are available for you to use. You can use all features of ES 6, like arrow functions, destructuring, etc…

## Limits

<table><thead><tr><th width="262.3333333333333" valign="top">Name</th><th valign="top">Total limit of ...</th><th valign="top">Value</th></tr></thead><tbody><tr><td valign="top">Max Execution Timeout</td><td valign="top">... seconds</td><td valign="top">10</td></tr><tr><td valign="top">Max Number</td><td valign="top">... characters</td><td valign="top">5000</td></tr></tbody></table>

## Examples

* [Dynamic mappable parameters](https://developers.make.com/custom-apps-documentation/app-components/iml-functions/dynamic-mappable-parameters)
* [Handling of full update approach in update modules](https://developers.make.com/custom-apps-documentation/app-components/iml-functions/handling-of-full-update-approach-in-update-modules)
* [Removal of empty collections and nulls](https://developers.make.com/custom-apps-documentation/app-components/iml-functions/removal-of-empty-collections-and-nulls)

## Test your custom IML functions

Learn more about debugging custom IML functions in the [Make DevTool](https://developers.make.com/custom-apps-documentation/debug-your-app/make-devtool).
