# Source: https://vincit.github.io/objection.js/guide/documents.html

Title: Documents | Objection.js

URL Source: https://vincit.github.io/objection.js/guide/documents.html

Markdown Content:
Documents | Objection.js
===============

[Objection.js](https://vincit.github.io/objection.js/)

[Guide](https://vincit.github.io/objection.js/guide/)

API Reference API Reference
*   [Main Module](https://vincit.github.io/objection.js/api/objection/)
*   [Query Builder](https://vincit.github.io/objection.js/api/query-builder/)
*   [Model](https://vincit.github.io/objection.js/api/model/)
*   [Types](https://vincit.github.io/objection.js/api/types/)

[Recipe Book](https://vincit.github.io/objection.js/recipes/)

Release Notes Release Notes
*   [Changelog](https://vincit.github.io/objection.js/release-notes/changelog.html)
*   [Migration to 3.0](https://vincit.github.io/objection.js/release-notes/migration.html)
*   [v2.x documentation (opens new window)](https://github.com/Vincit/objection.js/tree/v2/doc)
*   [v1.x documentation (opens new window)](https://github.com/Vincit/objection.js/tree/v1/doc)

[⭐ Star (opens new window)](https://github.com/vincit/objection.js)

[GitHub (opens new window)](https://github.com/vincit/objection.js)

[Guide](https://vincit.github.io/objection.js/guide/)

API Reference API Reference
*   [Main Module](https://vincit.github.io/objection.js/api/objection/)
*   [Query Builder](https://vincit.github.io/objection.js/api/query-builder/)
*   [Model](https://vincit.github.io/objection.js/api/model/)
*   [Types](https://vincit.github.io/objection.js/api/types/)

[Recipe Book](https://vincit.github.io/objection.js/recipes/)

Release Notes Release Notes
*   [Changelog](https://vincit.github.io/objection.js/release-notes/changelog.html)
*   [Migration to 3.0](https://vincit.github.io/objection.js/release-notes/migration.html)
*   [v2.x documentation (opens new window)](https://github.com/Vincit/objection.js/tree/v2/doc)
*   [v1.x documentation (opens new window)](https://github.com/Vincit/objection.js/tree/v1/doc)

[⭐ Star (opens new window)](https://github.com/vincit/objection.js)

[GitHub (opens new window)](https://github.com/vincit/objection.js)
*   Guide

    *   [Installation](https://vincit.github.io/objection.js/guide/installation.html)
    *   [Getting started](https://vincit.github.io/objection.js/guide/getting-started.html)
    *   [Models](https://vincit.github.io/objection.js/guide/models.html)
    *   [Relations](https://vincit.github.io/objection.js/guide/relations.html)
    *   [Query examples](https://vincit.github.io/objection.js/guide/query-examples.html)
    *   [Transactions](https://vincit.github.io/objection.js/guide/transactions.html)
    *   [Hooks](https://vincit.github.io/objection.js/guide/hooks.html)
    *   [Validation](https://vincit.github.io/objection.js/guide/validation.html)
    *   [Documents](https://vincit.github.io/objection.js/guide/documents.html)
    *   [Plugins](https://vincit.github.io/objection.js/guide/plugins.html)
    *   [Contribution guide](https://vincit.github.io/objection.js/guide/contributing.html)

[#](https://vincit.github.io/objection.js/guide/documents.html#documents) Documents
===================================================================================

Objection.js makes it easy to store non-flat documents as table rows. All properties of a model that are marked as objects or arrays in the model's [jsonSchema](https://vincit.github.io/objection.js/api/model/static-properties.html#static-jsonschema) are automatically converted to JSON strings in the database and back to objects when read from the database. The database columns for the object properties can be normal text columns. Postgresql has the `json` and `jsonb` data types that can be used instead for better performance and possibility to [query the documents(opens new window)](http://www.postgresql.org/docs/9.4/static/functions-json.html). If you don't want to use [jsonSchema](https://vincit.github.io/objection.js/api/model/static-properties.html#static-jsonschema) you can mark properties as objects using the [jsonAttributes](https://vincit.github.io/objection.js/api/model/static-properties.html#static-jsonattributes) Model property.

The `address` property of the Person model is defined as an object in the [Person.jsonSchema](https://vincit.github.io/objection.js/api/model/static-properties.html#static-jsonschema):

```
const jennifer = await Person.query().insert({
  firstName: 'Jennifer',
  lastName: 'Lawrence',
  age: 24,
  address: {
    street: 'Somestreet 10',
    zipCode: '123456',
    city: 'Tampere'
  }
});

const jenniferFromDb = await Person.query().findById(jennifer.id);

console.log(jennifer.address.city); // --> Tampere
console.log(jenniferFromDb.address.city); // --> Tampere
```

← [Validation](https://vincit.github.io/objection.js/guide/validation.html)[Plugins](https://vincit.github.io/objection.js/guide/plugins.html) →
