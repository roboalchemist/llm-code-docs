# Document Service API: Populating fields

By default the [Document Service API](/cms/api/document-service) does not populate any relations, media fields, components, or dynamic zones. This page describes how to use the `populate` parameter to populate specific fields.

:::tip
You can also use the `select` parameter to return only specific fields with the query results (see the [`select` parameter](/cms/api/document-service/fields) documentation).
:::

:::caution
If the Users & Permissions plugin is installed, the `find` permission must be enabled for the content-types that are being populated. If a role doesn't have access to a content-type it will not be populated.
:::

<!-- TODO: add link to populate guides (even if REST API, the same logic still applies) -->

## Relations and media fields

Queries can accept a `populate` parameter to explicitly define which fields to populate, with the following syntax option examples.

### Populate 1 level for all relations

To populate one-level deep for all relations, use the `*` wildcard in combination with the `populate` parameter:

</ApiCall>

### Populate 1 level for specific relations

To populate specific relations one-level deep, pass the relation names in a `populate` array:

</ApiCall>

### Populate several levels deep for specific relations

To populate specific relations several levels deep, use the object format with `populate`:

</ApiCall>

## Components & Dynamic Zones

Components are populated the same way as relations:

</ApiCall>

Dynamic zones are highly dynamic content structures by essence. To populate a dynamic zone, you must define per-component populate queries using the `on` property.

</ApiCall>

## Populating with `create()`

To populate while creating documents:

</ApiCall>

## Populating with `update()`

To populate while updating documents:

</ApiCall>

## Populating with `publish()`

To populate while publishing documents (same behavior with `unpublish()` and `discardDraft()`):

</ApiCall>