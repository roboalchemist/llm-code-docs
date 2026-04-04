# Source: https://developers.make.com/custom-apps-documentation/app-components/modules/universal-module/graphql.md

# GraphQL

## **Naming Convention**

All GraphQL universal modules should have the following module label and description:

* **Module label**: Execute a GraphQL query
* **Module description**: Performs an arbitrary authorized API call.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c61f2978cd90eaa8aef5598d7968bf5ec538c6d7%2Fgraphql_createmodule.png?alt=media" alt="" width="367"><figcaption></figcaption></figure></div>

{% tabs %}
{% tab title="Appearance" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-219f83051a315146c04bd41960749adde5830d4d%2Fgraphql_module.png?alt=media" alt="" width="539"></div>
{% endtab %}

{% tab title="Communication" %}

```json
{
    "url": "https://www.example.com/graphql",
    "method": "{{parameters.method}}",
    "qs": {
		"query": "{{parameters.queryQs}}"
	},
    "headers": {
		"Content-Type": "application/json"
	},
	"body": {
		"query": "{{parameters.queryBody}}",
		"operationName": "{{parameters.operationName}}",
		"variables": "{{if(isArray(parameters.variables), toCollection(parameters.variables, 'key', 'value'), parameters.variables)}}"
	},
	"type": "json",
    "response": {
        "output": {
            "headers": "{{headers}}",
            "body": "{{body}}",
			"statusCode": "{{statusCode}}"
        }
    }
}
```

{% endtab %}

{% tab title="Static parameters" %}
![](https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-24db6b771ccbdb1b438811fa47e149be70ed4961%2FexampleGraphqlStaticParams.png?alt=media)
{% endtab %}

{% tab title="Mappable parameters" %}

```json
[
    {
        "name": "method",
        "type": "select",
        "label": "Method",
        "required": true,
        "default": "POST",
        "options": [
            {
                "label": "GET (introspection query)",
                "value": "GET",
				"nested": [
					{
						"name": "queryQs",
						"label": "Query",
						"type": "text",
						"required": true
					}
				]
            },
            {
                "label": "POST (queries and mutations)",
                "value": "POST",
				"nested": [
					{
						"name": "queryBody",
						"label": "Query",
						"type": "text",
						"required": true
					},
					{
						"name": "operationName",
						"label": "Operation name",
						"type": "text",
						"advanced": true
					},
					{
						"name": "variablesDataSource",
						"label": "Variables data source",
						"type": "select",
						"required": true,
						"advanced": true,
						"default": "array",
						"options": [
							{
								"value": "array",
								"label": "Form",
								"nested": [
									{
										"name": "variables",
										"label": "Variables",
										"type": "array",
										"mappable": {
											"help": "Key-Value pairs as an Array of Collections e.g. `[{key:id,value:123},{key:name,value:'John'},…]`"
										},
										"spec": [
											{
												"name": "key",
												"label": "Key",
												"type": "text"
											},
											{
												"name": "value",
												"label": "Value",
												"type": "text"
											}
										]
									}
								]
							},
							{
								"value": "object",
								"label": "Collection",
								"nested": [
									{
										"name": "variables",
										"label": "Variables",
										"help": "A single Collection e.g. `{id:123,name:'John', …}`",
										"type": "any"
									}
								]
							}
						]
					}
				]
            }
        ]
    }
]
```

{% endtab %}

{% tab title="Interface" %}

```json
[
	{
		"name": "body",
		"type": "any",
		"label": "Body"
	},
	{
		"name": "headers",
		"type": "collection",
		"label": "Headers"
	},
	{
		"name": "statusCode",
		"type": "number",
		"label": "Status code"
	}
]
```

{% endtab %}

{% tab title="Samples" %}

```json
{}
```

{% endtab %}
{% endtabs %}
