# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/FormulaProvider.md

# [FormulaProvider](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider)

Base class for formula providers which are classes which may be attached to an [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-inputField) and configured with a [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-record) from which it will pull the values of fields references by `$fieldName` in any evaluated formula typed into the [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-inputField).

A [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-inputField) may be configured with an [dataField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField#config-dataField). The referenced [DataField](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField) may itself be configured with a [formulaProviders](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-formulaProviders) object which maps formula provider prefixes to configuration objects. When the [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-inputField) is mutated, if it starts with `=<prefix>(` then a [FormulaProvider](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider) registered under that prefix will be instantiated and used to evaluate the input value upon change (which fires on blur).

They may also be configured with a [store](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-store) which is used when the `$data` token is used in a formula to represent the JSON string of the whole dataset.

By default, a formula will be evaluated by passing it to the configured [url](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-url) as the [paramName](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-paramName) parameter in a POST request. The response will be expected to be a JSON object from which the value of the [responseField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-responseField) will be used as the result of the formula.

An implementation may provide a [generateContent](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-generateContent) callback which accepts the input field's formula value with referenced record field names substituted in. The `generateContent` callback must return a value based on that string.

An implementation may monitor the input field, and upon change, may use the field's value, and its [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-record) to calculate a new value in its [handleFormulaChange](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-handleFormulaChange) method.

The value passed to [handleFormulaChange](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-handleFormulaChange) has the following substitutions made:

* `$fieldName` tokens replaced by the value of the named field from the configured [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-record)
* `$this` token replaced by a JSON representation of the string values of the [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-record)
* `$data` token replaced by a JSON representation of all records in the configured [store](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-store)

An implementation _may_ implement a [handleFormulaInput](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-handleFormulaInput) method to be notified upon any mutation of its [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-inputField).

Data Fields and Formula Providers
---------------------------------

When updating a DataField that contains a formula, a special sibling [DataField](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField) is created to store the formula.

```
export default class Product extends Model {
    static fields = [
        'name',
        {
             name             : 'seoDescription',
             formulaProviders : {
                 AI   : {
                     url  : './myAIServerEndpoint.php',
                 }
             }
         }
    ];
});

const myModel = new Product({
    name : 'FitPro Adjustable Dumbbells'
});

// Setting a formula value of the field which has a formulaProvider will automatically trigger a call to the `url`
// from the formulaProvider to get the result, which is then stored in the `seoDescription` data field. The formula
// is then stored in the sibling field prepended with a '#'.
myProduct.set('seoDescription', '=AI(Generate 10 word SEO description for $name)');
```

When you persist a Model with a formula field, the formula field is stored as a sibling field to the formula field. The serialized JSON of a record having a `seoDescription` formula field would look like this:

```
 {
    "brand"           : "FitPro",
    "seoDescription"  : "Compact, versatile adjustable dumbbells for efficient home strength training workouts.",
    "#seoDescription" : "=AI(Generate 10 word SEO description for $name)",
  }
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[record](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-record)
The Record from which this formula provider fetches field definitions and values

[store](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-store)
The store from which this formula provider fetches field definitions. Defaults to the [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-record)'s first store.

[inputField](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-inputField)
The input field which provides the formula.

This field becomes this object's `owner`, so that it can be used as the `thisObj` for callbacks.

If this `FormulaProvider` was created from a known `type`, for example the input field was configured with

```
    formulaConfig : {
        type   : 'aiformula',
        url    : 'https://aimodule.com/',
        apiKey : 'XXXXXXX'
    }
```

then the field value is taken to _always_ represent a formula, and the entire string is used when passing the formula to [handleFormulaChange](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-handleFormulaChange).

If this `FormulaProvider` was inferred from the [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-inputField)'s value starting with a formula prefix (eg `=AI(`), then the string _between the parentheses_ is used and [handleFormulaChange](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-handleFormulaChange) is only called if the value matches eg `=AI(.*)`.

* `$fieldName` tokens replaced by the value of the named field from the configured [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-record)
* `$this` token replaced by a JSON representation of the string values of the [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-record)
* `$data` token replaced by a JSON representation of all records in the configured [store](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-store)

[handleFormulaInput](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-handleFormulaInput)
A function or the name of a function in the ownership hierarchy to execute when the [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-inputField) is mutated by any means such as typing or pasting.

[handleFormulaChange](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-handleFormulaChange)
A function or the name of a function in the ownership hierarchy to execute when the input field fires its `change` event which is usually on blur.

[url](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-url)
The URL to which the formula will be sent for evaluation in a JSON packet in a property named by [paramName](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-paramName).

The response is expected to be a JSON object from which the value of the [responseField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-responseField) will be used as the result of the formula.

```
{
  "content" : "Hello World!"
}
```

[method](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-method)
The HTTP method to use when sending the formula to the server.

[fetchOptions](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-fetchOptions)
An object containing the Fetch options to pass to the server request. Use this to control if credentials are sent and other options, read more at [MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

[paramName](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-paramName)
The name of the property in the JSON object sent to the server which contains the formula.

It may be a dot-separated path to inject a nested value.

[responseField](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-responseField)
The name of the property in the JSON object received from the server which contains the result of the formula.

It may be a dot-separated path to a nested value.

Expected response format with the default value for this property ("content"):

```
{
  "content" : "Hello World!"
}
```

[headers](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-headers)
The headers to send with the request.

[generateContent](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#config-generateContent)
A function or the name of a function in the ownership hierarchy which, when passed a fully constructed formula, yields the result.

Inject an implementation if the result is calculated programmatically or from a local source instead of being generated by a remote server via the [url](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-url).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFormulaProvider](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-isFormulaProvider)
Identifies an object as an instance of [FormulaProvider](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider) class, or subclass thereof.

[isFormulaProvider](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-isFormulaProvider-static)
Identifies an object as an instance of [FormulaProvider](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider) class, or subclass thereof.

[record](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-record)
The Record from which this formula provider fetches field definitions and values

[inputField](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-inputField)
The input field which provides the formula.

This field becomes this object's `owner`, so that it can be used as the `thisObj` for callbacks.

If this `FormulaProvider` was created from a known `type`, for example the input field was configured with

```
    formulaConfig : {
        type   : 'aiformula',
        url    : 'https://aimodule.com/',
        apiKey : 'XXXXXXX'
    }
```

then the field value is taken to _always_ represent a formula, and the entire string is used when passing the formula to [handleFormulaChange](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-handleFormulaChange).

If this `FormulaProvider` was inferred from the [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-inputField)'s value starting with a formula prefix (eg `=AI(`), then the string _between the parentheses_ is used and [handleFormulaChange](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-handleFormulaChange) is only called if the value matches eg `=AI(.*)`.

* `$fieldName` tokens replaced by the value of the named field from the configured [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-record)
* `$this` token replaced by a JSON representation of the string values of the [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-record)
* `$data` token replaced by a JSON representation of all records in the configured [store](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-store)

[handleFormulaInput](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-handleFormulaInput)
A function or the name of a function in the ownership hierarchy to execute when the [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-inputField) is mutated by any means such as typing or pasting.

[handleFormulaChange](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-handleFormulaChange)
A function or the name of a function in the ownership hierarchy to execute when the input field fires its `change` event which is usually on blur.

[url](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-url)
The URL to which the formula will be sent for evaluation in a JSON packet in a property named by [paramName](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-paramName).

The response is expected to be a JSON object from which the value of the [responseField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-responseField) will be used as the result of the formula.

```
{
  "content" : "Hello World!"
}
```

[method](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-method)
The HTTP method to use when sending the formula to the server.

[paramName](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-paramName)
The name of the property in the JSON object sent to the server which contains the formula.

It may be a dot-separated path to inject a nested value.

[responseField](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-responseField)
The name of the property in the JSON object received from the server which contains the result of the formula.

It may be a dot-separated path to a nested value.

Expected response format with the default value for this property ("content"):

```
{
  "content" : "Hello World!"
}
```

[headers](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-headers)
The headers to send with the request.

[generateContent](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#property-generateContent)
A function or the name of a function in the ownership hierarchy which, when passed a fully constructed formula, yields the result.

Inject an implementation if the result is calculated programmatically or from a local source instead of being generated by a remote server via the [url](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-url).

## Functions

Functions are methods available for calling on the class

[onFieldChange](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#function-onFieldChange)
Called when the [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-inputField) fires its change event.

If this `FormulaProvider` was created from an explicit `type`, or the value matches a formula format, then a formula value is created from the [inputField](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-inputField)'\` value with the following substitutions made:

* `$fieldName` tokens replaced by the value of the named field from the configured [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-record)
* `$this` token replaced by a JSON representation of the string values of the [record](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#property-record)
* `$data` token replaced by a JSON representation of all records in the configured [store](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-store)

The resulting string is passed to the [handleFormulaChange](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-handleFormulaChange) callback.

This may be called to trigger the change processing at any time. For instance if the record is mutated, the app may wish to cause the change processing to execute.

[calculate](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#function-calculate)
Processes the passed prompt using the configured [generateContent](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-generateContent) or the configured [url](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider#config-url) and returns the string result.

Note that this is an `async` function and the return value will need to be `await`ed.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[formulaNetworkError](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#event-formulaNetworkError)
Fires when the network request to the server fails.

This event bubbles, so can be caught on the FormulaProvider instance, its owning inputField or any parent widget.

When this error occurs, the formula result will be an empty string.

[formulaChange](https://bryntum.com/docs/gantt/api/Core/util/FormulaProvider#event-formulaChange)
Fires when the formula source has been processed and is about to be used.

Referenced cell values have been substituted in.

A handler may change the `formula` property of the event object to modify the formula before it is used.
