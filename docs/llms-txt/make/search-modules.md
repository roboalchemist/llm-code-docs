# Source: https://developers.make.com/custom-apps-documentation/best-practices/modules/search-modules.md

# Search modules

[Search modules](https://developers.make.com/custom-apps-documentation/app-components/modules/search) are modules that returns multiple results, as opposed to [action modules](https://developers.make.com/custom-apps-documentation/app-components/modules/action) that return only a single result.

If you want to retrieve all users who are registered on your service, you can't use an action module because it only returns one result. Instead, use a search module.

For example, if you call `/users`, you will get a list of users in `body.data`.

{% tabs %}
{% tab title="Code to correctly output each user" %}

```json
{
    "url": "/users",
    },
    "response": {
        "output": "{{item}}",
        "iterate": "{{body.data}}",
        "limit": "{{parameters.limit}}"
    }
}
```

{% endtab %}
{% endtabs %}

## Iteration and pagination

Since search modules return multiple results, they should contain pagination and iterative directives.

An action module should never contain pagination or the iterate directive. To return multiple objects, create a search module instead.

{% tabs %}
{% tab title="Incorrect" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-272f1805ebb135bb0f4707e2015c55d4bda18bf2%2Fincorrect_actionmodule_pagination.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Correct" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-bdc4ba3654bcf2df1849f633acbdc4637ddcb3ca%2Fsearchmodules_correctpagination.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

## Pagination parameters <a href="#pagination-parameters" id="pagination-parameters"></a>

The `pagination` section should only contain parameters that relate to pagination. These will be merged with the rest of the parameters defined in the `qs` section, so there is no need to define them all again.

{% tabs %}
{% tab title="Incorrect" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-636ce426b464955f4809d3ec5994f982e94507e4%2Fpagination_parameters_incorrect.png?alt=media" alt="" width="563"></div>

{% hint style="info" %}
The pagination directive contains `"since"`, `"until"` and `"limit"` parameters that are already defined in query string ("qs").
{% endhint %}
{% endtab %}

{% tab title="Correct" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-78c6635432524bb88f62a9bb75577921d72a4ca0%2Fpagination_parameters_correct.png?alt=media" alt="" width="563"></div>

{% hint style="info" %}
The pagination directive correctly contains only the `"offset"` parameter.
{% endhint %}
{% endtab %}
{% endtabs %}

## Page size in pagination

The page size should be as large as possible to reduce the number of requests, minimize delay, and avoid hitting the rate limit.

### Examples

#### ActiveCampaign

[ActiveCampaign API pagination documentation](https://developers.activecampaign.com/reference/pagination):

<table><thead><tr><th width="178.4444580078125">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>limit</code></td><td>The number of results to display in each page (default = 20; <strong>max = 100</strong>).</td></tr><tr><td><code>offset</code></td><td>The starting point for the result set of a page. This is a zero-based index. For example, if there are 39 total records and the <code>limit</code> is the default of 20, use <code>offset=20</code> to get the second page of results.</td></tr></tbody></table>

In this case, set `limit` to 100 in the request.

#### Productive

[Productive API pagination documentation](https://developer.productive.io/index.html#header-pagination):

<table><thead><tr><th width="198.444580078125">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>current_page</code></td><td>1 by default or the value you put in page[number]</td></tr><tr><td><code>total_pages</code></td><td><code>total_count/page_size</code> rounded up</td></tr><tr><td><code>total_count</code></td><td>Total number of resources you have</td></tr><tr><td><code>page_size</code></td><td>30 by default or the value you put in page[size]</td></tr><tr><td><code>max_page_size</code></td><td><strong>200</strong></td></tr></tbody></table>

In this case, set `page_size` to 200.

## Limiting output

Search modules should allow users to limit their output (how many bundles they return).

This can be achieved by setting the `limit` parameter in the response.

By default, this parameter is added to the trigger (polling) modules and should be required. In search modules, this parameter should NOT be required so if a user leaves it empty, the search modules return everything. Its default value should be set to 10.

{% tabs %}
{% tab title="Communication" %}

```json
{
    "url": "/clients",
    "method": "GET",
    "qs": {
        "per_page": 100
    },
    "response": {
        "limit": "{{parameters.limit}}",
        "output": "{{item}}",
        "iterate": "{{body.clients}}"
    },
    "pagination": {
        "qs": {
            "page": "{{pagination.page}}"
        },
        "condition": "{{body.next_page}}"
    }
}
```

{% endtab %}

{% tab title="Mappable parameters" %}

```json
{
        "name": "limit",
        "label": "Limit",
        "type": "uinteger",
        "help": "Number of clients to return",
        "default": 10
    }
]
```

{% hint style="info" %}
The `limit` parameter should not be set to `"required":true` (except for polling trigger modules).

\
The `limit` parameter should never be set to `"advanced":true`.
{% endhint %}
{% endtab %}
{% endtabs %}
