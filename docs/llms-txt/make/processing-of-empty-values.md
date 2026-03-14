# Source: https://developers.make.com/custom-apps-documentation/other/processing-of-empty-values.md

# Processing of 'empty' Values

{% hint style="info" %}
The new approach for processing empty values, as described in this document, is applicable only for apps with **Apps platform version 2** (apps created after 11/02/2019). Apps with **Apps platform version 1** behave according to the old rules due to backward compatibility.
{% endhint %}

In this approach, almost every input parameter of a module is ignored if there is no value. If the user wants to rewrite (erase) the value of a field in service, the user has to use the `erase` keyword. Here is an example of how to erase the values for the **Query string** and **Body** fields.

<div align="center"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-b13f0f2289e65f31b351be483e1413ab5abfcfd2%2Femptyvalues_erase.png?alt=media" alt="" width="375"></div>

The processing of "empty" values is completely managed by Make. So you don't have to implement this in your app. Keep in mind that when an empty value comes to a module, a value still has to be sent to the service.

For example, when a user updates a task and in the module configuration there is a multiple-select with labels that they leave untouched, it is unclear what action should be performed. Does this mean that they want to leave the task labels unchanged or want to remove all the labels?

The new behavior for parameter processing solves this problem.

By default, if the user doesn't select any label, Make ignores the field. If the user wants to remove all assigned labels from the task, they have to use the `erase` keyword.

## How Make evaluates empty values <a href="#how-integromat-evaluates-empty-values" id="how-integromat-evaluates-empty-values"></a>

<table><thead><tr><th valign="top">Type of empty value</th><th valign="top">Manifest 1.0</th><th valign="top">Manifest 2.0 implicit behavior</th><th valign="top">Manifest 2.0 field with erase pill (map mode)</th></tr></thead><tbody><tr><td valign="top"><strong>string</strong></td><td valign="top"><code>null</code></td><td valign="top"><code>undefined</code></td><td valign="top"><code>null</code></td></tr><tr><td valign="top"><strong>string</strong> (forced empty string using IML)</td><td valign="top"><code>""</code></td><td valign="top"><code>""</code></td><td valign="top">​</td></tr><tr><td valign="top"><strong>number</strong></td><td valign="top"><code>null</code></td><td valign="top"><code>undefined</code></td><td valign="top"><code>null</code></td></tr><tr><td valign="top"><strong>boolean</strong></td><td valign="top"><code>undefined</code></td><td valign="top"><code>undefined</code></td><td valign="top"><code>undefined</code></td></tr><tr><td valign="top"><strong>array</strong></td><td valign="top"><code>[]</code></td><td valign="top"><code>undefined</code></td><td valign="top"><code>[]</code></td></tr><tr><td valign="top"><strong>multiple select</strong></td><td valign="top"><code>[]</code></td><td valign="top"><code>undefined</code></td><td valign="top"><code>[]</code></td></tr><tr><td valign="top"><strong>select</strong> (nothing selected)</td><td valign="top"><code>null</code></td><td valign="top"><code>undefined</code></td><td valign="top">​</td></tr><tr><td valign="top"><strong>select</strong> (selected value is<code>""</code>)</td><td valign="top"><code>null</code></td><td valign="top"><code>undefined</code></td><td valign="top">​</td></tr><tr><td valign="top"><strong>select</strong> (selected value is <code>null</code>)</td><td valign="top">invalid value</td><td valign="top">invalid value</td><td valign="top">​</td></tr><tr><td valign="top"><strong>select</strong> (map mode)</td><td valign="top"><code>null</code></td><td valign="top"><code>undefined</code></td><td valign="top"><code>null</code></td></tr><tr><td valign="top"><strong>collection</strong></td><td valign="top">not changed (collection of empty values)</td><td valign="top">Recursively processed corresponding to the rules in this table</td><td valign="top">Recursively processed corresponding to the rules in this table</td></tr></tbody></table>

### Collection example

When using a collection parameter in a module, behavior differs depending on whether fields are left empty or the `erase` pill is applied:

If the user leaves all fields empty, the request contains an empty collection.

If the user applies the erase pill to one of the parameters inside collection, Make sends the collection with explicit null values for its fields.

{% tabs %}
{% tab title="Result: user leaves fields empty" %}

```json
"collection": {}
```

{% endtab %}

{% tab title="Result: user applies erase pill" %}

```json
"collection": {
"parameter": null
}
```

{% endtab %}
{% endtabs %}

This difference can cause issues in some apps. If the collection values are not modified inside module IML functions and the empty collection is passed directly into the request body or query string, the API may receive `{},` which can result in unexpected behavior.

## When the `erase` pill is shown <a href="#when-the-erase-pill-is-shown" id="when-the-erase-pill-is-shown"></a>

The `erase` keyword is shown for the **update** and **universal** modules.

The type of module is defined in the metadata of a module. A **universal** module is a module without a defined module action field.

<div align="center"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-20f5fa0941036531a261afba122f8a3c77b8f94c%2Fempty_values.png?alt=media" alt="" width="375"></div>
