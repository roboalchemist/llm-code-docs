# REST API: Population & Field Selection

The [REST API](/cms/api/rest) by default does not populate any relations, media fields, components, or dynamic zones. Use the [`populate` parameter](#population) to populate specific fields and the [`select` parameter](#field-selection) to return only specific fields with the query results.

:::tip

</ApiCall>

## Population

The REST API by default does not populate any type of fields, so it will not populate relations, media fields, components, or dynamic zones unless you pass a `populate` parameter to populate various field types.

The `populate` parameter can be used alone or [in combination with multiple operators](#combining-population-with-other-operators) to have much more control over the population.

:::caution
The `find` permission must be enabled for the content-types that are being populated. If a role doesn't have access to a content-type it will not be populated (see [User Guide](/cms/features/users-permissions#editing-a-role) for additional information on how to enable `find` permissions for content-types).
:::

:::note
It's currently not possible to return just an array of ids with a request.
:::

:::strapi Populating guides

The [REST API guides](/cms/api/rest/guides/intro) section includes more detailed information about various possible use cases for the populate parameter:

- The [Understanding populate](/cms/api/rest/guides/understanding-populate) guide explains in details how populate works, with diagrams, comparisons, and real-world examples.
- The [How to populate creator fields](/cms/api/rest/guides/populate-creator-fields) guide provides step-by-step instructions on how to add `createdBy` and `updatedBy` fields to your queries responses.

:::

The following table sums up possible populate use cases and their associated parameter syntaxes, and links to sections of the Understanding populate guide which includes more detailed explanations:

| Use case  | Example parameter syntax | Detailed explanations to read |
|-----------| ---------------|-----------------------|
| Populate everything, 1 level deep, including media fields, relations, components, and dynamic zones | `populate=*`| [Populate all relations and fields, 1 level deep](/cms/api/rest/guides/understanding-populate#populate-all-relations-and-fields-1-level-deep) |
| Populate one relation,<br/>1 level deep | `populate=a-relation-name`| [Populate 1 level deep for specific relations](/cms/api/rest/guides/understanding-populate#populate-1-level-deep-for-specific-relations) |
| Populate several relations,<br/>1 level deep | `populate[0]=relation-name&populate[1]=another-relation-name&populate[2]=yet-another-relation-name`| [Populate 1 level deep for specific relations](/cms/api/rest/guides/understanding-populate#populate-1-level-deep-for-specific-relations) |
| Populate some relations, several levels deep | `populate[root-relation-name][populate][0]=nested-relation-name`| [Populate several levels deep for specific relations](/cms/api/rest/guides/understanding-populate#populate-several-levels-deep-for-specific-relations) |
| Populate a component | `populate[0]=component-name`| [Populate components](/cms/api/rest/guides/understanding-populate#populate-components) |
| Populate a component and one of its nested components | `populate[0]=component-name&populate[1]=component-name.nested-component-name`| [Populate components](/cms/api/rest/guides/understanding-populate#populate-components) |
| Populate a dynamic zone (only its first-level elements) | `populate[0]=dynamic-zone-name`| [Populate dynamic zones](/cms/api/rest/guides/understanding-populate#populate-dynamic-zones) |
| Populate a dynamic zone and its nested elements and relations, using a precisely defined, detailed population strategy | `populate[dynamic-zone-name][on][component-category.component-name][populate][relation-name][populate][0]=field-name`| [Populate dynamic zones](/cms/api/rest/guides/understanding-populate#populate-dynamic-zones) |

:::tip
The easiest way to build complex queries with multiple-level population is to use our [interactive query builder](/cms/api/rest/interactive-query-builder) tool.
:::

### Combining Population with other operators

By utilizing the `populate` operator it is possible to combine other operators such as [field selection](/cms/api/rest/populate-select#field-selection), [filters](/cms/api/rest/filters), and [sort](/cms/api/rest/sort-pagination) in the population queries.

:::caution
The population and pagination operators cannot be combined.
:::

#### Populate with field selection

`fields` and `populate` can be combined.

<details>
<summary>
</ApiCall>

#### Populate with filtering

`filters` and `populate` can be combined.

<details>
<summary>
</ApiCall>