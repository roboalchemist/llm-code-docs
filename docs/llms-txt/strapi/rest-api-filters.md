# REST API: Filters

The [REST API](/cms/api/rest) offers the ability to filter results found with its ["Get entries"](/cms/api/rest#get-all) method.<br/>
Using optional Strapi features can provide some more filters:

- If the [Internationalization (i18n) plugin](/cms/features/internationalization) is enabled on a content-type, it's possible to filter by locale.
- If the [Draft & Publish](/cms/features/draft-and-publish) is enabled, it's possible to filter based on a `published` (default) or `draft` status.

:::tip

<details>
<summary>JavaScript query (built with the qs library):</summary>

</ApiCall>

## Example: Find multiple restaurants with ids 3, 6,8

You can use the `$in` filter operator with an array of values to find multiple exact values.

<br />

<details>
<summary>JavaScript query (built with the qs library):</summary>

</ApiCall>

## Complex filtering

Complex filtering is combining multiple filters using advanced methods such as combining `$and` & `$or`. This allows for more flexibility to request exactly the data needed.

<br />

<details>
<summary>JavaScript query (built with the qs library):</summary>

</ApiCall>

## Deep filtering

Deep filtering is filtering on a relation's fields.

:::note
- Relations, media fields, components, and dynamic zones are not populated by default. Use the `populate` parameter to populate these content structures (see [`populate` documentation](/cms/api/rest/populate-select#population))
- You can filter what you populate, you can also filter nested relations, but you can't use filters for polymorphic content structures (such as media fields and dynamic zones).
:::

:::caution
Querying your API with deep filters may cause performance issues.  If one of your deep filtering queries is too slow, we recommend building a custom route with an optimized version of the query.
:::

<details>
<summary>JavaScript query (built with the qs library):</summary>

</ApiCall>