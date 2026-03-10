# REST API: `locale`

The [Internationalization (i18n) feature](/cms/features/internationalization) adds new abilities to the [REST API](/cms/api/rest).

:::prerequisites
To work with API content for a locale, please ensure the locale has been already [added to Strapi in the admin panel](/cms/features/internationalization#settings).
:::

The `locale` [API parameter](/cms/api/rest/parameters) can be used to work with documents only for a specified locale. `locale` takes a locale code as a value (see 

</Tabs>

### `GET` Get all documents in a specific locale {#rest-get-all}

</ApiCall>

### `GET` Get a document in a specific locale {#rest-get}

To get a specific document in a given locale, add the `locale` parameter to the query:

| Use case             | Syntax format and link for more information                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| In a collection type | [`GET /api/content-type-plural-name/document-id?locale=locale-code`](#get-one-collection-type) |
| In a single type     | [`GET /api/content-type-singular-name?locale=locale-code`](#get-one-single-type)               |

#### Collection types {#get-one-collection-type}

To get a specific document in a collection type in a given locale, add the `locale` parameter to the query, after the `documentId`:

</ApiCall>

#### Single types {#get-one-single-type}

To get a specific single type document in a given locale, add the `locale` parameter to the query, after the single type name:

</ApiCall>

### `POST` Create a new localized document for a collection type {#rest-create}

To create a localized document from scratch, send a POST request to the Content API. Depending on whether you want to create it for the default locale or for another locale, you might need to pass the `locale` parameter in the request's body

| Use case                      | Syntax format and link for more information                                               |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| Create for the default locale | [`POST /api/content-type-plural-name`](#rest-create-default-locale) |
| Create for a specific locale  | [`POST /api/content-type-plural-name`](#rest-create-specific-locale)<br/>+ pass locale in request body               |

#### For the default locale {#rest-create-default-locale}

If no locale has been passed in the request body, the document is created using the default locale for the application:

</ApiCall>

#### For a specific locale {#rest-create-specific-locale}

To create a localized entry for a locale different from the default one, add the `locale` attribute to the body of the POST request:

</ApiCall>

### `PUT` Create a new, or update an existing, locale version for an existing document {#rest-update}

With `PUT` requests sent to an existing document, you can:

- create another locale version of the document,
- or update an existing locale version of the document.

Send the `PUT` request to the appropriate URL, adding the `locale=your-locale-code` parameter to the query URL and passing attributes in a `data` object in the request's body:

| Use case             | Syntax format and link for more information                                               |
| -------------------- | --------------------------------------------------------------------------------------- |
| In a collection type | [`PUT /api/content-type-plural-name/document-id?locale=locale-code`](#rest-put-collection-type) |
| In a single type     | [`PUT /api/content-type-singular-name?locale=locale-code`](#rest-put-single-type)               |

:::caution
When creating a localization for existing localized entries, the body of the request can only accept localized fields.
:::

:::tip
The Content-Type should have the [`createLocalization` permission](/cms/features/rbac#collection-and-single-types) enabled, otherwise the request will return a `403: Forbidden` status.
:::

:::note
It is not possible to change the locale of an existing localized entry. When updating a localized entry, if you set a `locale` attribute in the request body it will be ignored.
:::

#### In a collection type {#rest-put-collection-type}

To create a new locale for an existing document in a collection type, add the `locale` parameter to the query, after the `documentId`, and pass data to the request's body:

</ApiCall>

#### In a single type {#rest-put-single-type}

To create a new locale for an existing single type document, add the `locale` parameter to the query, after the single type name, and pass data to the request's body:

</ApiCall>

<br/>

### `DELETE` Delete a locale version of a document {#rest-delete}

To delete a locale version of a document, send a `DELETE` request with the appropriate `locale` parameter.

`DELETE` requests only send a 204 HTTP status code on success and do not return any data in the response body.

#### In a collection type {#rest-delete-collection-type}

To delete only a specific locale version of a document in a collection type, add the `locale` parameter to the query after the `documentId`:

#### In a single type {#rest-delete-single-type}

To delete only a specific locale version of a single type document, add the `locale` parameter to the query after the single type name: