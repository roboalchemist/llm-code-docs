# Document Service API

The Document Service API is built on top of the **Query Engine API**  and is used to perform CRUD ([create](#create), [retrieve](#findone), [update](#update), and [delete](#delete)) operations on **documents** 

:::strapi Entity Service API is deprecated in Strapi 5
The Document Service API replaces the Entity Service API used in Strapi v4 (

</ApiCall>

The `findOne()` method returns the matching document if found, otherwise returns `null`.

### `findFirst()`

Find the first document matching the parameters.

Syntax:  `findFirst(parameters: Params) => Document`

#### Parameters

| Parameter | Description | Default | Type |
|-----------|-------------|---------|------|
| [`locale`](/cms/api/document-service/locale#find-first) |  Locale of the documents to find. | Default locale | String or `undefined` |
| [`status`](/cms/api/document-service/status#find-first) | _If [Draft & Publish](/cms/features/draft-and-publish) is enabled for the content-type_:<br/>Publication status, can be: <ul><li>`'published'` to find only published documents</li><li>`'draft'` to find only draft documents</li></ul> | `'draft'` | `'published'` or `'draft'` |
| [`filters`](/cms/api/document-service/filters) | [Filters](/cms/api/document-service/filters) to use | `null` | Object |
| [`fields`](/cms/api/document-service/fields#findfirst)   | [Select fields](/cms/api/document-service/fields#findfirst) to return   | All fields<br/>(except those not populate by default)  | Object |
| [`populate`](/cms/api/document-service/populate) | [Populate](/cms/api/document-service/populate) results with additional fields. | `null` | Object |

#### Examples

<br />

##### Generic example

By default, `findFirst()` returns the draft version, in the default locale, of the first document for the passed unique identifier (collection type id or single type id):

</ApiCall>

##### Find the first document matching parameters

Pass some parameters to `findFirst()` to return the first document matching them.

If no `locale` or `status` parameters are passed, results return the draft version for the default locale:

</ApiCall>

### `findMany()`

Find documents matching the parameters.

Syntax: `findMany(parameters: Params) => Document[]`

#### Parameters

| Parameter | Description | Default | Type |
|-----------|-------------|---------|------|
| [`locale`](/cms/api/document-service/locale#find-many) |  Locale of the documents to find. | Default locale | String or `undefined` |
| [`status`](/cms/api/document-service/status#find-many) | _If [Draft & Publish](/cms/features/draft-and-publish) is enabled for the content-type_:<br/>Publication status, can be: <ul><li>`'published'` to find only published documents</li><li>`'draft'` to find only draft documents</li></ul> | `'draft'` | `'published'` or `'draft'` |
| [`filters`](/cms/api/document-service/filters) | [Filters](/cms/api/document-service/filters) to use | `null` | Object |
| [`fields`](/cms/api/document-service/fields#findmany)   | [Select fields](/cms/api/document-service/fields#findmany) to return   | All fields<br/>(except those not populate by default)  | Object |
| [`populate`](/cms/api/document-service/populate) | [Populate](/cms/api/document-service/populate) results with additional fields. | `null` | Object |
| [`pagination`](/cms/api/document-service/sort-pagination#pagination) | [Paginate](/cms/api/document-service/sort-pagination#pagination) results |
| [`sort`](/cms/api/document-service/sort-pagination#sort) | [Sort](/cms/api/document-service/sort-pagination#sort) results | | | 

#### Examples

<br />

##### Generic example

When no parameter is passed, `findMany()` returns the draft version in the default locale for each document:

</ApiCall>

##### Find documents matching parameters

Available filters are detailed in the [filters](/cms/api/document-service/filters) page of the Document Service API reference.

If no `locale` or `status` parameters are passed, results return the draft version for the default locale:

</ApiCall>

<!-- TODO: To be completed post v5 GA -->
<!-- #### Find ‘fr’ version of all documents with fallback on default (en)

```js
await documents('api:restaurant.restaurant').findMany({ locale: 'fr', fallbackLocales: ['en'] } );
``` -->

<!-- TODO: To be completed post v5 GA -->
<!-- #### Find sibling locales for one or many documents

```js
await documents('api:restaurant.restaurant').findMany({ locale: 'fr', populateLocales: ['en', 'it'] } );
// Option of response forma for this case 
{
  data: {
		title: { "Wonderful" }
  },
  localizations: [
    { enLocaleData },
    { itLocaleData }
  ]
}

await documents('api:restaurant.restaurant').findMany({ locale: ['en', 'it'] } );
// Option of response format for this case 
{
  data: {
		title: {
			"en": "Wonderful",
			"it": "Bellissimo"
		}
  },
}
```

</Request> -->

### `create()`

Creates a drafted document and returns it.

Pass fields for the content to create in a `data` object.

Syntax: `create(parameters: Params) => Document`

#### Parameters

| Parameter | Description | Default | Type |
|-----------|-------------|---------|------|
| [`locale`](/cms/api/document-service/locale#create) | Locale of the documents to create. | Default locale | String or `undefined` |
| [`fields`](/cms/api/document-service/fields#create)   | [Select fields](/cms/api/document-service/fields#create) to return   | All fields<br/>(except those not populated by default)  | Object |
| [`status`](/cms/api/document-service/status#create) | _If [Draft & Publish](/cms/features/draft-and-publish) is enabled for the content-type_:<br/>Can be set to `'published'` to automatically publish the draft version of a document while creating it  | -| `'published'` |
| [`populate`](/cms/api/document-service/populate) | [Populate](/cms/api/document-service/populate) results with additional fields. | `null` | Object |

#### Example

If no `locale` parameter is passed, `create()` creates the draft version of the document for the default locale:

</ApiCall>

:::tip
If the [Draft & Publish](/cms/features/draft-and-publish) feature is enabled on the content-type, you can automatically publish a document while creating it (see [`status` documentation](/cms/api/document-service/status#create)).
:::

### `update()`

Updates document versions and returns them.

Syntax: `update(parameters: Params) => Promise

</ApiCall>

<!-- ! not working -->
<!-- #### Update many document locales

```js
// Updates the default locale by default
await documents('api:restaurant.restaurant').update(documentId, {locale: ['es', 'en'], data: {name: "updatedName" }}
``` -->

### `delete()`

Deletes one document, or a specific locale of it.

Syntax: `delete(parameters: Params): Promise<{ documentId: ID, entries: Number }>`

#### Parameters

| Parameter | Description | Default | Type |
|-----------|-------------|---------|------|
| `documentId`| Document id | | `ID`|
| [`locale`](/cms/api/document-service/locale#delete) | Locale version of the document to delete. | `null`<br/>(deletes only the default locale) | String, `'*'`, or `null` |
| [`filters`](/cms/api/document-service/filters) | [Filters](/cms/api/document-service/filters) to use | `null` | Object |
| [`fields`](/cms/api/document-service/fields#delete)   | [Select fields](/cms/api/document-service/fields#delete) to return   | All fields<br/>(except those not populate by default)  | Object |
| [`populate`](/cms/api/document-service/populate) | [Populate](/cms/api/document-service/populate) results with additional fields. | `null` | Object |

#### Example

If no `locale` parameter is passed, `delete()` only deletes the default locale version of a document. This deletes both the draft and published versions:

<!-- ! not working -->
<!-- #### Delete a document with filters

To delete documents matching parameters, pass these parameters to `delete()`.

If no `locale` parameter is passed, it will delete only the default locale version:

 -->

### `publish()`

Publishes one or multiple locales of a document.

This method is only available if [Draft & Publish](/cms/features/draft-and-publish) is enabled on the content-type.

Syntax: `publish(parameters: Params): Promise<{ documentId: ID, entries: Number }>`

#### Parameters

| Parameter | Description | Default | Type |
|-----------|-------------|---------|------|
| `documentId`| Document id | | `ID`|
| [`locale`](/cms/api/document-service/locale#publish) | Locale of the documents to publish. | Only the default locale | String, `'*'`, or `null` |
| [`filters`](/cms/api/document-service/filters) | [Filters](/cms/api/document-service/filters) to use | `null` | Object |
| [`fields`](/cms/api/document-service/fields#publish)   | [Select fields](/cms/api/document-service/fields#publish) to return   | All fields<br/>(except those not populate by default)  | Object |
| [`populate`](/cms/api/document-service/populate) | [Populate](/cms/api/document-service/populate) results with additional fields. | `null` | Object |

#### Example

If no `locale` parameter is passed, `publish()` only publishes the default locale version of the document:

</ApiCall>

<!-- ! not working -->
<!-- #### Publish document locales with filters

```js
// Only publish locales with title is "Ready to publish"
await strapi.documents('api::restaurant.restaurant').publish(
  { filters: { title: 'Ready to publish' }}
);
``` -->

### `unpublish()`

Unpublishes one or all locale versions of a document, and returns how many locale versions were unpublished.

This method is only available if [Draft & Publish](/cms/features/draft-and-publish) is enabled on the content-type.

Syntax: `unpublish(parameters: Params): Promise<{ documentId: ID, entries: Number }>`

#### Parameters

| Parameter | Description | Default | Type |
|-----------|-------------|---------|------|
| `documentId`| Document id | | `ID`|
| [`locale`](/cms/api/document-service/locale#unpublish) | Locale of the documents to unpublish. | Only the default locale | String, `'*'`, or `null` |
| [`filters`](/cms/api/document-service/filters) | [Filters](/cms/api/document-service/filters) to use | `null` | Object |
| [`fields`](/cms/api/document-service/fields#unpublish)   | [Select fields](/cms/api/document-service/fields#unpublish) to return   | All fields<br/>(except those not populate by default)  | Object |
| [`populate`](/cms/api/document-service/populate) | [Populate](/cms/api/document-service/populate) results with additional fields. | `null` | Object |

#### Example

If no `locale` parameter is passed, `unpublish()` only unpublishes the default locale version of the document:

</ApiCall>

### `discardDraft()`

Discards draft data and overrides it with the published version.

This method is only available if [Draft & Publish](/cms/features/draft-and-publish) is enabled on the content-type.

Syntax: `discardDraft(parameters: Params): Promise<{ documentId: ID, entries: Number }>`

#### Parameters

| Parameter | Description | Default | Type |
|-----------|-------------|---------|------|
| `documentId`| Document id | | `ID`|
| [`locale`](/cms/api/document-service/locale#discard-draft) | Locale of the documents to discard. | Only the default locale. | String, `'*'`, or `null` |
| [`filters`](/cms/api/document-service/filters) | [Filters](/cms/api/document-service/filters) to use | `null` | Object |
| [`fields`](/cms/api/document-service/fields#discarddraft)   | [Select fields](/cms/api/document-service/fields#discarddraft) to return   | All fields<br/>(except those not populate by default)  | Object |
| [`populate`](/cms/api/document-service/populate) | [Populate](/cms/api/document-service/populate) results with additional fields. | `null` | Object |

#### Example

If no `locale` parameter is passed, `discardDraft()` discards draft data and overrides it with the published version only for the default locale:

</ApiCall>

### `count()`

Count the number of documents that match the provided parameters.

Syntax: `count(parameters: Params) => number`

#### Parameters

| Parameter | Description | Default | Type |
|-----------|-------------|---------|------|
| [`locale`](/cms/api/document-service/locale#count) | Locale of the documents to count | Default locale | String or `null` |
| [`status`](/cms/api/document-service/status#count) | _If [Draft & Publish](/cms/features/draft-and-publish) is enabled for the content-type_:<br/>Publication status, can be: <ul><li>`'published'` to find only published documents </li><li>`'draft'` to find draft documents (will return all documents)</li></ul> | `'draft'` | `'published'` or `'draft'` |
| [`filters`](/cms/api/document-service/filters) | [Filters](/cms/api/document-service/filters) to use | `null` | Object |

:::note
Since published documents necessarily also have a draft counterpart, a published document is still counted as having a draft version.

This means that counting with the `status: 'draft'` parameter still returns the total number of documents matching other parameters, even if some documents have already been published and are not displayed as "draft" or "modified" in the Content Manager anymore. There currently is no way to prevent already published documents from being counted.
:::

#### Examples

<br />

##### Generic example

If no parameter is passed, the `count()` method the total number of documents for the default locale:

</ApiCall>

##### Count published documents

To count only published documents, pass `status: 'published'` along with other parameters to the `count()` method.

If no `locale` parameter is passed, documents are counted for the default locale.

##### Count documents with filters

Any [filters](/cms/api/document-service/filters) can be passed to the `count()` method.

If no `locale` and no `status` parameter is passed, draft documents (which is the total of available documents for the locale since even published documents are counted as having a draft version) are counted only for the default locale:

```js
/**
 * Count number of draft documents (default if status is omitted) 
 * in English (default locale) 
 * whose name starts with 'Pizzeria'
 */
strapi.documents('api::restaurant.restaurant').count({ filters: { name: { $startsWith: "Pizzeria" }}})`
```