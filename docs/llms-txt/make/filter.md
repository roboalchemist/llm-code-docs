# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/filter.md

# Filter

## Specification

### options

Available types:

<table><thead><tr><th width="109" valign="top">Type</th><th valign="top">Specification</th></tr></thead><tbody><tr><td valign="top"><strong>array</strong></td><td valign="top">Left-side operands specified like option objects.</td></tr><tr><td valign="top"><strong>string</strong></td><td valign="top">A URL of the RPC returning the list of left-side operands.</td></tr><tr><td valign="top"><strong>object</strong></td><td valign="top">Detailed configuration for receiving the left-side operands.</td></tr></tbody></table>

Available parameters:

<table><thead><tr><th width="126">Parameter</th><th width="82">Type</th><th>Specification</th></tr></thead><tbody><tr><td><strong>store</strong></td><td>array</td><td>An array of left-side operands specified like an Option object.</td></tr><tr><td><strong>store</strong></td><td>string</td><td>A URL of the RPC returning the list of left-side operands.</td></tr><tr><td><strong>logic</strong></td><td>string</td><td>Allowed values: <code>both, and, or</code>. Specifies if only <code>and</code>, <code>or</code> or <code>both</code> types of filters are available.</td></tr><tr><td><strong>operators</strong></td><td>array</td><td>Custom operators. The data structure is the same as the grouped select box.</td></tr></tbody></table>

{% hint style="info" %}
If the left-side operands field is not filled, it can be filled manually.
{% endhint %}

## Examples

### Basic usage of a filter

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-8dd9f4c0b520243d1b4bd1c19847af2c89f33ced%2Ffilter1a.png?alt=media" alt="" width="542"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "search",
		"label": "Search criteria",
		"type": "filter",
		"options": [
			{
				"label": "Email",
				"value": "email"
			},
			{
				"label": "Username",
				"value": "username"
			}
		]
	}
]
```

{% endtab %}

{% tab title="Output" %}

```json
[
    [
        {
          "a": "username",
          "b": "A",
          "o": "text:startwith"
        },
        {
          "a": "username",
          "b": "B",
          "o": "text:endwith"
        }
    ],
    [
        {
          "a": "username",
          "b": "C",
          "o": "text:endwith"
        }
    ]
]
```

{% endtab %}
{% endtabs %}

### Custom operators

Many services have their own search options and syntax. That's why you may need to define your own operators. You can specify them inside the `options` object. You can create multiple groups of operators.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-26dcdde1df0bda1c3b92a54e1d8cba0147c355c5%2Ffilter2a.png?alt=media" alt="" width="542"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "search",
		"type": "filter",
		"label": "Search criteria",
		"options": {
			"operators": [
				{
					"label": "Text",
					"options": [
						{
							"label": "Matches",
							"value": "matches"
						},
						{
							"label": "Doesn't match",
							"value": "doesntmatch"
						}
					]
				},
				{
					"label": "Numbers",
					"options": [
						{
							"label": "Three times larger",
							"value": "threetimeslarger"
						}
					]
				}
			]
		}
	}
]
```

{% endtab %}
{% endtabs %}

### Only `and`, only `or` logic

You may need to set up an only `and` or only `or` filter. You can do this by setting the `logic` option. In this example, you can see how to create the filter parameter with only `and` logic. For the `or` alternative, change the keyword.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c450c82655c096ba4a4aef44cea5893ae2cae735%2Ffilter3a.png?alt=media" alt="" width="542"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
	{
		"name": "search",
		"type": "filter",
		"label": "Search criteria",
		"options": {
			"logic": "and"
		}
	}
]
```

{% endtab %}
{% endtabs %}

### Custom options, custom operators, and custom logic

This example combines custom options, custom operators, and custom logic.

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-5ab915651fe7000d5e66a64a7c52239e8dfdb313%2Ffilter4a.png?alt=media" alt="" width="541"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Source" %}

```json
[
{
        "name": "search",
        "type": "filter",
        "label": "Search criteria",
        "options": {
            "logic": "and",
            "store": [
                {
                    "label": "Email",
                    "value": "email"
                },
                {
                    "label": "Username",
                    "value": "username"
                }
            ],
            "operators": [
                {
                    "label": "Text",
                    "options": [
                        {
                            "label": "Matches",
                            "value": "matches"
                        },
                        {
                            "label": "Doesn't match",
                            "value": "doesntmatch"
                        },
                        {
                            "label": "Contains",
                            "value": "contains"
                        }
                    ]
                }
            ]
        }
    }
    ]
```

{% endtab %}
{% endtabs %}
