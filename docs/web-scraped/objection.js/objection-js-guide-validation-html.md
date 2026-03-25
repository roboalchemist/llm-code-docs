# Source: https://vincit.github.io/objection.js/guide/validation.html

Title: Validation | Objection.js

URL Source: https://vincit.github.io/objection.js/guide/validation.html

Published Time: Wed, 25 Sep 2024 11:34:05 GMT

Markdown Content:
Validation | Objection.js
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
        *   [Examples](https://vincit.github.io/objection.js/guide/validation.html#examples)

    *   [Documents](https://vincit.github.io/objection.js/guide/documents.html)
    *   [Plugins](https://vincit.github.io/objection.js/guide/plugins.html)
    *   [Contribution guide](https://vincit.github.io/objection.js/guide/contributing.html)

[#](https://vincit.github.io/objection.js/guide/validation.html#validation) Validation
======================================================================================

[JSON schema(opens new window)](http://json-schema.org/) validation can be enabled by setting the [jsonSchema](https://vincit.github.io/objection.js/api/model/static-properties.html#static-jsonschema) property of a model class. The validation is ran each time a [Model](https://vincit.github.io/objection.js/api/model/) instance is created.

You rarely need to call [$validate](https://vincit.github.io/objection.js/api/model/instance-methods.html#validate) method explicitly, but you can do it when needed. If validation fails a [ValidationError](https://vincit.github.io/objection.js/api/types/#class-validationerror) will be thrown. Since we use Promises, this usually means that a promise will be rejected with an instance of [ValidationError](https://vincit.github.io/objection.js/api/types/#class-validationerror).

See [the recipe book](https://vincit.github.io/objection.js/recipes/custom-validation.html) for instructions if you want to use some other validation library.

[#](https://vincit.github.io/objection.js/guide/validation.html#examples) Examples
----------------------------------------------------------------------------------

All these will trigger the validation:

```
Person.fromJson({ firstName: 'jennifer', lastName: 'Lawrence' });
await Person.query().insert({ firstName: 'jennifer', lastName: 'Lawrence' });
await Person.query()
  .update({ firstName: 'jennifer', lastName: 'Lawrence' })
  .where('id', 10);

// Patch operation ignores the `required` property of the schema
// and only validates the given properties. This allows a subset
// of model's properties to be updated.
await Person.query()
  .patch({ age: 24 })
  .where('age', '<', 24);

await Person.query().insertGraph({
  firstName: 'Jennifer',
  pets: [
    {
      name: 'Fluffy'
    }
  ]
});

await Person.query().upsertGraph({
  id: 1,
  pets: [
    {
      name: 'Fluffy II'
    }
  ]
});
```

Validation errors provide detailed error message:

```
try {
  await Person.query().insert({ firstName: 'jennifer' });
} catch (err) {
  console.log(err instanceof objection.ValidationError); // --> true
  console.log(err.data); // --> {lastName: [{message: 'required property missing', ...}]}
}
```

Error parameters returned by [ValidationError](https://vincit.github.io/objection.js/api/types/#class-validationerror) could be used to provide custom error messages:

```
try {
  await Person.query().insert({ firstName: 'jennifer' });
} catch (err) {
  let lastNameErrors = err.data.lastName;

  for (let i = 0; i < lastNameErrors.length; ++i) {
    let lastNameError = lastNameErrors[i];

    if (lastNameError.keyword === 'required') {
      console.log('This field is required!');
    } else if (lastNameError.keyword === 'minLength') {
      console.log('Must be longer than ' + lastNameError.params.limit);
    } else {
      console.log(lastNameError.message); // Fallback to default error message
    }
  }
}
```

← [Hooks](https://vincit.github.io/objection.js/guide/hooks.html)[Documents](https://vincit.github.io/objection.js/guide/documents.html) →
