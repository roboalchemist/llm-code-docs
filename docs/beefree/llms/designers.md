# Source: https://docs.beefree.io/beefree-sdk/apis/template-catalog-api/designers.md

# Designers

## Fetch a list of all Designers

`/v1/catalog/designers`

**HTTP Method:** `GET`

**Description:** Access a complete list of all Designers in the catalog.

The response is paginated, with a standard display of 200 items per page. You can manipulate the ‘pagesize’ request parameter to control the number of items shown per page.

### Request Parameters

The following table displays request parameters.

| Parameter  | Value | Description                  |
| ---------- | ----- | ---------------------------- |
| `pagesize` | int   | Set the item number per page |

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FE6bkQWJsGXvKQXiDs9qY%2Fcatalog-designers.yaml?alt=media&token=d1e1a7cc-1335-43ce-965c-fd83b803ca51>" path="/v1/catalog/designers" method="get" %}
[catalog-designers.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FE6bkQWJsGXvKQXiDs9qY%2Fcatalog-designers.yaml?alt=media\&token=d1e1a7cc-1335-43ce-965c-fd83b803ca51)
{% endopenapi %}

## Fetch a single Designer

`/v1/catalog/designers/:slug`

**HTTP Method:** `GET`

**Description:** Retrieve detailed information for a specific Designer, identified by the unique slug present in the URL. This enables the procurement of comprehensive data pertaining to the particular designer, including their portfolio of templates and any associated metadata within the catalog.

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FIURC3jqWItPfPRr4YUDG%2Fcatalog-designers-slug.yaml?alt=media&token=7417a68a-7221-4b21-a77b-79917d5d0e95>" path="/v1/designers/:slug" method="get" %}
[catalog-designers-slug.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FIURC3jqWItPfPRr4YUDG%2Fcatalog-designers-slug.yaml?alt=media\&token=7417a68a-7221-4b21-a77b-79917d5d0e95)
{% endopenapi %}
