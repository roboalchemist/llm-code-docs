# Source: https://docs.beefree.io/beefree-sdk/apis/template-catalog-api/categories.md

# Categories

## Fetch a list of all Categories

`/v1/catalog/categories`

**HTTP Method:** `GET`

**Description:** Retrieve a list of all the Templates within the catalog, applying filters based on request parameters.

You can extract a list of all the Categories present within the catalog. This comprehensive list includes all categories under which templates are classified.

The response that you receive is paginated for ease of reading and navigation. It displays 200 items per page by default, providing a comprehensive view of the catalog content.

However, if you wish to adjust the number of items shown on each page, you can use the ‘pagesize’ request parameter.

### Request Parameters

The following table displays request parameters.

| Parameter  | Value | Description                  |
| ---------- | ----- | ---------------------------- |
| `pagesize` | int   | Set the item number per page |

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FwuscIMhPNNc41kXk6BsQ%2Fcatalog-categories.yaml?alt=media&token=fee09489-9bc5-4dac-8638-ec96038f24c9>" path="/v1/catalog/categories" method="get" %}
[catalog-categories.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FwuscIMhPNNc41kXk6BsQ%2Fcatalog-categories.yaml?alt=media\&token=fee09489-9bc5-4dac-8638-ec96038f24c9)
{% endopenapi %}

## Fetch a single Category

`/v1/catalog/categories/:slug`

**HTTP Method:** `GET`

**Description:** Retrieve a list of all the Templates within the catalog, applying filters based on request parameters.

Retrieve detailed information about a specific Category using its unique identifier, or slug, which can be found in the URL. This method allows you to access in-depth data related to that particular category, such as its associated templates and related metadata.

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FvezcfRVpIewgKcmmRx2c%2Fcatalog-categories-slug.yaml?alt=media&token=c482263d-3e4f-4d94-bd7b-3fc30d5fd36d>" path="/v1/catalog/categories/:slug" method="get" %}
[catalog-categories-slug.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FvezcfRVpIewgKcmmRx2c%2Fcatalog-categories-slug.yaml?alt=media\&token=c482263d-3e4f-4d94-bd7b-3fc30d5fd36d)
{% endopenapi %}
