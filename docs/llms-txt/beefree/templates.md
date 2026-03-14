# Source: https://docs.beefree.io/beefree-sdk/apis/template-catalog-api/templates.md

# Templates

## Get a list of all Templates

`/v1/catalog/templates`

**HTTP Method:** `GET`

**Description:** Retrieve a list of all the Templates within the catalog, applying filters based on request parameters.

You can execute a search by providing a series of terms within the ‘search’ request parameter. This search will operate on template title, description, category name, collection name, designer name, publication date (‘published\_at’), and tags.

The response will encompass a ‘facets’ field, outlining the count of existing Templates across each Category, Collections, Designers, and Tags fields and their sub-fields, considering any applied filters and searches.

The response is paginated, presenting 20 items per page by default. The ‘pagesize’ request parameter enables control over the page size.

### Request Parameters

The following table displays a list of request parameters.

| Parameter          | Example                 | Description                                              |
| ------------------ | ----------------------- | -------------------------------------------------------- |
| `search`           | activity, beach, summer | List of terms to search, separated by comma              |
| `category`         | small-business          | Filter by category slug                                  |
| `collection`       | e-commerce              | Filter by collection slug                                |
| `designer`         | bee-team                | Filter by designer slug                                  |
| `tag`              | activity, beach, summer | Filter by tag name                                       |
| `template_type`    | email                   | Filter by template\_type. Choiches are "email" or "page" |
| `pagesize`         | 20                      | Set the item number per page                             |
| `published_after`  | 2023-01-01              | Filter by published\_at after given date                 |
| `published_before` | 2023-01-01              | Filter by published\_at before given date                |

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FLgNOcJe7IiBGYcgwDTyn%2Fcatalog-templates.yaml?alt=media&token=2cb10feb-4c2d-4a96-b300-0991b3d16b62>" path="/v1/catalog/templates" method="get" %}
[catalog-templates.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FLgNOcJe7IiBGYcgwDTyn%2Fcatalog-templates.yaml?alt=media\&token=2cb10feb-4c2d-4a96-b300-0991b3d16b62)
{% endopenapi %}

## Fetch a single Template

`/v1/catalog/templates/:slug`

**HTTP Method:** `GET`

**Description:** Fetch a single template identified by its slug (in the URL).

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FpP0VKRl4kfr4tJcZ4AjZ%2Fcatalog-templates-slug.yaml?alt=media&token=69671b75-ceb1-45b0-bce2-40a0b1a747e3>" path="/v1/catalog/templates/:slug" method="get" %}
[catalog-templates-slug.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FpP0VKRl4kfr4tJcZ4AjZ%2Fcatalog-templates-slug.yaml?alt=media\&token=69671b75-ceb1-45b0-bce2-40a0b1a747e3)
{% endopenapi %}
