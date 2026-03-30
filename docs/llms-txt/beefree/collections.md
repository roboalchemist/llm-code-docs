# Source: https://docs.beefree.io/beefree-sdk/apis/template-catalog-api/collections.md

# Collections

## Fetch a List of Collections

`/v1/catalog/collections`

**HTTP Method:** `GET`

**Description:** You can pull up a full list of all Collections in the catalog. Collections are groups of templates with similar attributes or purposes. This overview can help you understand the types of template groupings available.

The response will be paginated, with 200 items per page default for easy navigation. However, you can change this default by adjusting the ‘pagesize’ request parameter to suit your viewing preferences.

### Request Parameters

The following table displays request parameters.

| Parameter  | Value | Description                  |
| ---------- | ----- | ---------------------------- |
| `pagesize` | int   | Set the item number per page |

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FursFVV7Fg1YPzEaNM8QM%2Fcatalog-collections.yaml?alt=media&token=c87348ea-c4c7-459d-b5dd-ecc9f8420baa>" path="/v1/catalog/collections" method="get" %}
[catalog-collections.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FursFVV7Fg1YPzEaNM8QM%2Fcatalog-collections.yaml?alt=media\&token=c87348ea-c4c7-459d-b5dd-ecc9f8420baa)
{% endopenapi %}

## Fetch a single Collection

`/v1/catalog/collections/:slug`

**HTTP Method:** `GET`

**Description:** Access a specific Collection using its unique slug found in the URL. This lets you view detailed information about this particular group of templates, including its associated templates and any related details.

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FH4YoE5HtHwsZ9TJwAjuO%2Fcatalog-collections-slug.yaml?alt=media&token=b623b6b9-247c-4ef5-9a2a-f33ea622b8cd>" path="/v1/catalog/collections/:slug" method="get" %}
[catalog-collections-slug.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FH4YoE5HtHwsZ9TJwAjuO%2Fcatalog-collections-slug.yaml?alt=media\&token=b623b6b9-247c-4ef5-9a2a-f33ea622b8cd)
{% endopenapi %}
