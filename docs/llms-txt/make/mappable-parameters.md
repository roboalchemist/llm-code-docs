# Source: https://developers.make.com/custom-apps-documentation/component-blocks/mappable-parameters.md

# Source: https://developers.make.com/custom-apps-documentation/best-practices/input-parameters/mappable-parameters.md

# Mappable parameters

## Types of fields

You can use mappable parameters in many types of fields:

<details>

<summary>Standard fields</summary>

* Visible by default
* Frequently used
* Typically easy to understand
* Visible on the third-party’s Web UI by default
* Consider copying the UX from the third-party’s Web UI, for clarity
* `Limit` should be the last variable

</details>

<details>

<summary>Advanced fields</summary>

* Hidden by the Advanced settings toggle
* Not needed by the majority of users
* Generally more difficult to understand
* Might require technical knowledge. A hint or link to documentation is necessary
* Includes custom fields, if supported by the app
* Hidden on the third-party’s Web UI
* Placed at the bottom of all fields. This ensures that when users toggle to the advanced settings, they can easily view them without being mixed in with regular fields
* Consider copying the UX from the third-party’s Web UI, for clarity
* `Limit` should be the last variable

</details>

<details>

<summary>Required fields</summary>

* Require minimal effort to make the module work
* Validate if the user has filled in all necessary fields required by the API call
* Guard against getting an API error from the third party due to missing fields
* Ideally contain a default value
* If an advanced field, must contain a default value

</details>

<details>

<summary>Conditionally-required fields</summary>

* Required based on a condition. For example:
  * Either field A or field B is required
  * The field is only required to create but not update in an upsert module
* A clear hint is mandatory to explain the condition
* Should follow required fields and be located before optional fields
  * This could be an exception if the fields have to be arranged in logical blocks

</details>

<details>

<summary>Optional fields</summary>

* Not necessary for the API to work, but good to have
* Enrich the UX by providing flexibility to the user to send all fields the API supports

</details>

<details>

<summary>Static, dynamic, and semi-dynamic fields</summary>

When mapping parameters, there are different types of fields to choose from.

**Static fields**

With static fields, all parameters are manually specified in the module, so every users sees the same options. Though not ideal, some APIs require the use of static fields.

**Dynamic fields**

With dynamic fields, all parameters are loaded dynamically from the API, using [dynamic fields RPCs](https://developers.make.com/custom-apps-documentation/app-components/rpcs/dynamic-fields-rpc). The options shown to a user are based on the user's account specifications. For example, a user who is a manager may have access to more files and folders in an account than another employee. Every user will have a different experience interacting with the module based on their account login. Whenever possible, using dynamic fields is the ideal approach.

Sometimes field types in third-party applications do not match types supported in Make. In this case, when defining mappable parameters using an RPC, you also need to [implement a custom IML function](https://developers.make.com/custom-apps-documentation/app-components/iml-functions/dynamic-mappable-parameters) to convert the type.

**Semi-dynamic fields**

It's also possible to use a combination of static and dynamic fields to customize the user experience, based on user settings and availability in the API.

</details>

<details>

<summary>Custom fields</summary>

Custom fields are user-defined fields in the third-party application. You can use custom fields with RPCs as well, for further customization.

However, if an API supports implementation of custom fields where the **field name** and **field value** may be specified by the user (the user is creating new custom fields), both of the fields should **not** be mandatory. There may be reasons for a value to be empty, and requiring both could cause an error. Instead, require only **field value**. Additionally, if the API doesn't allow empty values, the validation of an empty value should be set so the pair will not be sent.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-301d8f4138581a317b18a45f08993f81b06d9c09%2Fmappable_customfields.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

</details>

## Date parameters

Use the date and time type parameters instead of asking users to format the date and time themselves. These values should be formatted in the backend to support Make's format.

{% tabs %}
{% tab title="Correct" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-2e1c68b408fb91124db05f234c0630e231b7da02%2Fcorrect_timestamp.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Exception: If the endpoint accepts date only or time only, use the `text` parameter with a clear hint and example.
{% endhint %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-4c2442b32d61335c7ff975587b713e3222e0e11c%2Fcorrect_timestamp2.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Incorrect: wrong parameter type" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-d4ebcf4cc0650e49b79d70ac0c0beedbe6c4b54f%2Fincorrect_timestamp.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Incorrect: not user-friendly" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-5e2ba57b98dd8e6884d96b569affa1a03298b064%2Fnotuserfriendly_timestamp.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Even though this will be sent correctly, it is not user-friendly.
{% endhint %}
{% endtab %}
{% endtabs %}

### Processing of date parameters

When a field is a type "date", it should be possible to use our keyword "now" as a value. The field should accept ISO-8601 date format and if the service requires only the date (no time) or a different format like timestamp, this formatting should happen inside the module.

{% hint style="info" %}
Users of the app should never be prompted to format the date inputs the way API requires. Apps that require this will not be approved by Make.
{% endhint %}

{% tabs %}
{% tab title="Good practice" %}
**Communication**:

```javascript
{
    "url": "/api/users",
    "method": "POST",
    "body": {
        "name": "{{parameters.name}}",
        "birthday": "{{formatDate(parameters.birthday, 'YYYY-MM-DD')}}",
        "due_date": "{{formatDate(parameters.due_date, 'X')}}"
    },
    "response": {
        "output": "{{body}}"
    }
}
```

{% hint style="info" %}
Parameter `birthday` is required to have format YYYY-MM-DD and parameter `due_date` is required to be a time stamp by the service, so the formatting happens inside the Communication part of the module.
{% endhint %}

**Parameters**:

```javascript
[
    {
        "name": "name",
        "type": "text",
        "label": "Name"
    },
    {
        "name": "birthday",
        "type": "date",
        "label": "Birthday"
    },
    {
        "name": "due_date",
        "type": "date",
        "label": "Due Date"
    }
]
```

{% hint style="info" %}
The parameters `birthday` and `due_date` are correctly date typed and don't need to be formatted by the user who can use the `now` keyword.
{% endhint %}
{% endtab %}

{% tab title="Bad practice" %}
**Communication**:

```javascript
{
    "url": "/api/users",
    "method": "POST",
    "body": {
        "name": "{{parameters.name}}",
        "birthday": "{{parameters.birthday}}",
        "due_date": "{{parameters.due_date}}"
    },
    "response": {
        "output": "{{body}}"
    }
}
```

{% hint style="info" %}
Parameter `birthday` is required to have format YYYY-MM-DD and parameter `due_date` is required to be a time stamp but nothing is done with the value.
{% endhint %}

**Parameters**:

```javascript
[
    {
        "name": "name",
        "type": "text",
        "label": "Name"
    },
    {
        "name": "birthday",
        "type": "date",
        "label": "Birthday",
        "help": "Format YYYY-MM-DD"
    },
    {
        "name": "due_date",
        "type": "integer",
        "label": "Due Date",
        "help": "Enter a timestamp"
    }
]
```

{% hint style="info" %}
The parameter `due_date` is an incorrect type and `birthday` is required to be formatted by the user.
{% endhint %}
{% endtab %}
{% endtabs %}

## Support of array aggregators

If the API doesn't support arrays or arrays of collection, you need to implement an IML function that enables the use of array aggregators.

{% tabs %}
{% tab title="Incorrect" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-7b9ae65950c76f6436c4cdfeada459b3084cae0c%2Fmappable_arrayincorrect.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Correct" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-4613874560e5a2785eb42008ccc988a470e5d240%2Fmappable_arraycorrect.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```javascript
[
	{
		"name": "array",
		"type": "array",
		"label": "PDF documents",
		"required": true,
		"spec": {
			"type": "collection",
			"label": "Document",
			"spec": [
				{
					"name": "name",
					"type": "filename",
					"label": "Name",
					"semantic": "file:name",
					"required": true
				},
				{
					"name": "data",
					"type": "buffer",
					"label": "Data",
					"semantic": "file:data",
					"required": true
				}
			]
		},
		"labels": {
			"add": "Add document"
		}
	}
]
```

{% endtab %}
{% endtabs %}

## Remote procedure calls (RPCs)

For every parameter where options are listed dynamically (values pulled from the API), you should implement an RPC, especially when you need to provide an ID (or raw value) instead of a label.

For example, if you have a lot of customers and you don’t remember their IDs, the RPC will display a list of names / emails and fill in the ID for you. Also, RPCs help the user to understand the behavior and outputs of the module before building the logic of their scenario.

If there are many RPCs nested to each other, you need to implement an additional select which allows users to choose whether they will map the deepest parameter from previous modules or whether they will follow every RPC to select every parameter in order to get into the deepest parameter.

{% tabs %}
{% tab title="Select for the method" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-1227710bd0f4324ee5a44859e36e59fa2a7f28aa%2Frpc_selectformethod.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Nested ID field" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c3a20d56b25c4eb05f0e2adc0c4cdb9fe6a38e54%2Frpc_nestedID.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

### Edit mode

The edit mode (`"mode": "edit"`) is used in modules where the RPCs should be switched off by default. Those modules are - UPDATE, GET, DELETE etc.

There are two main reasons why this is used:

1. To reduce module load time: If you click on the module to open it, all options for all RPCs need to be loaded before it opens. By using `mode:edit`, the module opens right away and RPC options are loaded when you open the select field.\
   \
   Imagine a module to create a donut:
   * RPC for the type of dough
   * RPC for the icing color or flavor
   * RPC for the type of sprinkles
   * RPC for filling options\
     \
     With this setup, the module will take a long time to load, especially if the API server is busy.
2. If we expect the user will want to map the value, not select from the list. For example, in a Watch for new orders > Mark order as received module, map the Order ID from the previous module.

Edit mode is also recommended in modules that will always be working with the lowest entity, for example, an attachment for an e-mail in a module.

## Mappable: false

You may want to hide the mapping toggle to help the user enter correct information in a field.

For example, in a `select` field type a user should select from a list of options. Having a map toggle is unnecessary and may confuse the user.

To hide the mappable toggle, use the `"mappable": false` parameter.

{% tabs %}
{% tab title="Issue" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-04fb2be02b58cb5141919dc7daaf1100bb441815%2Fmappable_issue.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
After switching on the mapping toggle, the text fields disappear.
{% endhint %}
{% endtab %}

{% tab title="Solution" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c331ef4f6002f740debd060ad2c4f9610d99333b%2Fmappable_false_solution.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
`"mappable": false` hides the mapping toggle:
{% endhint %}
{% endtab %}
{% endtabs %}

## Messages (banners)

In some circumstances, you may want to give users additional information in a module.\
\
There are three distinct message types available, each with a specific icon and guidelines for appropriate use. The recommended length of the message is 50 to 300 characters.

### Information (blue)

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-437bccd9830dd0d61fdbca7fe7e17a19de437d29%2Fcustomapps_newinfobanner_blueexample.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
{
    "type": "banner",
    "title": "This is an info",
    "text": "Here is a description of info.",
    "theme": "info"
}
```

{% endtab %}
{% endtabs %}

### Warning (yellow)

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-dc7e51385fce2c9e764a3a67ad400d8030db2bb9%2Fcustomapps_newinfobanner_yellowexample.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
{
	"type": "banner",
	"title": "This is a warning",
	"text": "Here is a description of warning.",
	"theme": "warning"
}
```

{% endtab %}
{% endtabs %}

### Danger (red)

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-fe865fbdb68643adea945147df1a22c59ede286c%2Fbanner_warning.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
{
	"type": "banner",
	"title": "Headline, if needed...",
	"text": "Minimum recommended length of message text. (50 characters)",
	"theme": "danger"
}
```

{% endtab %}
{% endtabs %}

## ID finder

The ID finder allows users to identify items within a module by entering search criteria. The ID finder can either be the only search method for a field or it can be included in a list of multiple search methods.

The ID finder window can either include a single search criterion (keyword or exact match) or multiple search criteria. There are specific guidelines to follow when implementing the ID finder, both within the module and the ID finder itself.

<details>

<summary>Module guidelines for the ID finder</summary>

When implementing the ID finder within a module, it is important to consider whether it is the only available search method to identify the item, or if there are multiple search methods. Regardless of the number of search methods, the ID finder button should always be labeled **ID finder**.

If you are implementing the ID finder for a field that is not searching for an ID, for example the **Dropbox > Watch files** module with the **File Path** field, the button should read **Finder** instead of **ID finder**.

**Single search method**

If a module contains only the ID finder as a search method, the name of the field should be the **\[Item] ID** that is being searched for.

* **\[Item] ID** field names include:
  * **Campaign ID** - campaign to be updated
  * **Employee ID** - employee record to delete
  * Etc.

**Multiple search methods**

If a module contains multiple search methods, they should be listed in an **\[Item]** **search method** dropdown. Replace **\[Item]** with the name of item that is being searched for.

* **\[Item] search method** field names include:
  * **Spreadsheet search method** - spreadsheet to add a row to
  * **Channel search method** - channel to send a message to
  * **Record search method** - record to update
  * Etc.
* **\[Item] search method** dropdown options include:
  * Search by keyword (ID finder with keyword search)
  * Search by \[item] (ID finder with exact match search)
  * Select by file path
  * Select from list
  * Enter manually
  * Etc.

</details>

<details>

<summary>ID finder guidelines</summary>

The ID finder can include either one single search criterion (keyword or exact match) or multiple search criteria. It is important to note that the number of results the ID finder will return is limited both on the Make platform side and the app side. Because of this, we do not advise users to leave the search field empty to return all results, as this information can be misleading.

The standard blue info box message should be used for all ID finders, except for in cases of Single search criterion: exact match.

{% hint style="info" %}
Only a limited number of results can be shown. If you don’t see the item you’re looking for, try more specific search criteria.
{% endhint %}

**Single search criteria**

**Keyword search**

* The name of the search field should always be **\[Search item] Keywords**.
  * **\[Search Item] keywords** examples include:
    * **Channel name keywords**
    * **Address keywords**
* Include the blue info box that instructs users to use more specific search criteria. In this case, that is a more specific keyword.

**Exact match required**

* The name of the search field should be identical to the name of the item that the user must match.
  * For example, if a user must enter an item’s name, the field should be **Name**.
* Do not include the blue info box that tells users to use more specific search criteria, as there are no other criteria or way to make an exact match more specific.
* In the search field hint, add the following: Must be the exact **\[Search item]**.
  * For example:
    * Field: **Channel name**.
    * Hint: Must be the exact **Channel name**.

**Multiple search criteria**

**Keyword search**

* The name of the search field should always be **\[Search Item] keywords**
  * **\[Search Item] keywords** examples include:
    * **Spreadsheet keywords**
    * **Employee Title keywords**
* Include the blue info box that instructs users to use more specific search criteria. In this case, that is either a more specific keyword or utilizing the other criteria in the ID finder to refine their search.

</details>

<details>

<summary>ID finder results</summary>

If the API allows, the ID finder’s results should be listed in alphabetical order.

</details>

<details>

<summary>ID finder template</summary>

```javascript
{
    "name": "recordId",
    "type": "text",
    "label": "Record ID",
    "rpc": {
        "label": "ID finder",
        "url": "rpc://...",
        "parameters": [
            {
                "type": "banner",
                "text": "If you don't see the result you're looking for, try more specific search criteria.",
                "theme": "info"
            },
            {
                "name": "query",
                "type": "text",
                "label": "Query"
            }
        ]
    }
}
```

</details>

## Support for custom query and filter options

Certain APIs provide support for custom queries or filters when searching records, such as invoices. In Make, our goal is to offer query and filter capabilities to both regular and advanced users.

Therefore we have implemented two methods of achieving this functionality, and ideally users should be able to choose between the two options.

### Predefined query

We have utilized the familiar filter setup format found in Scenario Builder. With this approach, users are not required to learn the query format. Instead, they can simply set up the query in a manner similar to configuring filters.

When the module is executed, a custom IML function constructs the query, adhering to the specified format.

### Custom query

Users have the option to manually compose their own queries. This feature is particularly valuable when the API supports new operators that are not yet available within the module.

To assist users in leveraging the query field effectively, the following helpful information should be provided:

* Query format: The guidelines for structuring the query.
* Example of a functional query: An illustrative sample query as reference.
* API documentation URL: Direct access to the API documentation with query specification.

### Search filters

{% tabs %}
{% tab title="Correct" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-0e8497de225d4012ddfdb7bc14326df6339a045c%2Fsearchfilter_correct1.png?alt=media" alt="" width="487"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Provide a list of fields and a list of operators.
{% endhint %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-35c8ce8f1e20d84becd08c3bc21e1507ec7ecfbd%2Fsearchfilter_correct2.png?alt=media" alt="" width="478"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Group operators by their data types
{% endhint %}
{% endtab %}

{% tab title="Incorrect" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-0f5d1b1a6b96bcf8759d4eacfd9b87aa55086031%2Fsearchfilter_incorrecta.png?alt=media" alt="" width="496"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Do not ask users to construct the query string.
{% endhint %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-bae87be1f4ded9eb5657976c8c54ce70e4ea99f3%2Fsearchfilter_incorrect2.png?alt=media" alt="" width="494"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Do not share operator among all data types.
{% endhint %}
{% endtab %}
{% endtabs %}

## Labels

Labels are available for:

* Array(s)
* Array item(s)
  * Default to `Item`
  * This should be consistent and related to the label of the array. For example, if the label of an array is `Recipients` , the label of an array item should be `Recipient`.
* Button(s) to add an array item
  * Default to `Add item`.
  * The button label should be consistent and related to the label of array items. For example, if the label of an array item is `Recipient` , the label of the button should be `Add recipient`.

<div align="center"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-e6823bdbebe560eec4dd95cbd92df3f9b2e2def8%2Flabel_array_collection.png?alt=media" alt="" width="491"><figcaption></figcaption></figure></div>

{% tabs %}
{% tab title="API expecting array of collection" %}

```javascript
//If the API is expecting an array of collection
// {
//     "recipients": [
//         {
//              "name": "abc"
//         }
//     ]
// }
[
	{
		"name": "recipients",
		"type": "array",
		// Label of the array
		"label": "Recipients",
		"spec": {
			"type": "collection",
			// Label of array item(s)
			"label": "Recipient",
			"spec": [
				{
					"name": "name",
					"type": "text",
					"label": "Name",
					"required": true
				}
			]
		},
		"labels": {
			// Label of the button to add an array item
			"add": "Add recipient"
		}
	}
]
```

{% endtab %}

{% tab title="API expecting primitive array" %}

```javascript
// If the API is expecting a primitive array
// {
//     "recipients": [
//         "name-abc"
//     ]
// }
[
	{
		"name": "recipients",
		"type": "array",
		// Label of the array
		"label": "Recipients",
		"spec": {
			"type": "text",
			// Label of array item(s)
			"label": "Recipient name"
		},
		"labels": {
			// Label of the button to add an array item
			"add": "Add recipient name"
		}
	}
]
```

{% endtab %}
{% endtabs %}

## Universal module

* If possible, provide a universal module.
* The prefix path of the URL should not contain the version of the API, to ensure that users can use any version of the API. Even if there is no other version, it is good practice in case there is one in the future.
* The hint under the URL should contain the correct prefix path of the URL, together with an example of a postfix path of the URL.
* The example should be “ready-to-use”. We recommend using methods for retrieving a record in the example (GET).

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-9e3d05724cc71e95d2f1c2a3913ac534f9322ccc%2Funiversalmodule_mappable.png?alt=media" alt="" width="314"><figcaption></figcaption></figure></div>
