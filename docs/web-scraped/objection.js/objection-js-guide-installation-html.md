# Source: https://vincit.github.io/objection.js/guide/installation.html

Title: Installation | Objection.js

URL Source: https://vincit.github.io/objection.js/guide/installation.html

Published Time: Wed, 25 Sep 2024 11:34:05 GMT

Markdown Content:
Installation | Objection.js
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

[#](https://vincit.github.io/objection.js/guide/installation.html#installation) Installation
============================================================================================

Objection.js can be installed using `npm` or `yarn`. Objection uses [knex(opens new window)](https://knexjs.org/) as its database access layer, so you also need to install it.

```
npm install objection knex
yarn add objection knex
```

You also need to install one of the following depending on the database you want to use:

```
npm install pg
npm install sqlite3
npm install mysql
npm install mysql2
```

You can use the `next` tag to install an alpha/beta/RC version:

```
npm install objection@next
```

[Getting started](https://vincit.github.io/objection.js/guide/getting-started.html) →
