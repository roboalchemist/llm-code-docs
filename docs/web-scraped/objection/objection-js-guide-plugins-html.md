# Source: https://vincit.github.io/objection.js/guide/plugins.html

Title: Plugins | Objection.js

URL Source: https://vincit.github.io/objection.js/guide/plugins.html

Markdown Content:
A curated list of plugins and modules for objection. Only plugins that follow [the best practices](https://vincit.github.io/objection.js/guide/plugins.html#plugin-development-best-practices) are accepted on this list. Other modules like plugins for other frameworks and things that cannot be implemented following the best practices are an exception to this rule. If you are a developer of or otherwise know of a good plugin/module for objection, please create a pull request or an issue to get it added to this list.

[#](https://vincit.github.io/objection.js/guide/plugins.html#_3rd-party-plugins) 3rd party plugins
--------------------------------------------------------------------------------------------------

*   [objection-authorize(opens new window)](https://github.com/JaneJeon/objection-authorize) - integrate access control into Objection queries
*   [objection-dynamic-finder(opens new window)](https://github.com/snlamm/objection-dynamic-finder) - dynamic finders for your models
*   [objection-guid(opens new window)](https://github.com/seegno/objection-guid) - automatic guid for your models
*   [objection-password(opens new window)](https://github.com/scoutforpets/objection-password) - automatic password hashing for your models
*   [objection-soft-delete(opens new window)](https://github.com/griffinpp/objection-soft-delete) - Soft delete functionality with minimal configuration
*   [objection-unique(opens new window)](https://github.com/seegno/objection-unique) - Unique validation for your models
*   [objection-visibility(opens new window)](https://github.com/oscaroox/objection-visibility) - whitelist/blacklist your model properties

[#](https://vincit.github.io/objection.js/guide/plugins.html#other-3rd-party-modules) Other 3rd party modules
-------------------------------------------------------------------------------------------------------------

*   [objection-filter(opens new window)](https://github.com/tandg-digital/objection-filter) - API filtering on data and related models
*   [objection-graphql(opens new window)](https://github.com/vincit/objection-graphql) - Automatically generates rich graphql schema for objection models
*   [objectionjs-graphql(opens new window)](https://www.npmjs.com/package/objectionjs-graphql) - Automatically generates GraphQl schema for objection models compatible with Objection 3.x (Graph fetch support)

[#](https://vincit.github.io/objection.js/guide/plugins.html#plugin-development-best-practices) Plugin development best practices
---------------------------------------------------------------------------------------------------------------------------------

When possible, objection.js plugins should be implemented as [class mixins(opens new window)](http://justinfagnani.com/2015/12/21/real-mixins-with-javascript-classes/). A mixin is simply a function that takes a class as an argument and returns a subclass. Plugins should not modify [objection.Model](https://vincit.github.io/objection.js/api/model/), [objection.QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/) or any other global variables directly. See the [example plugin(opens new window)](https://github.com/Vincit/objection.js/tree/main/examples/plugin) for more info. There is also [another example(opens new window)](https://github.com/Vincit/objection.js/tree/main/examples/plugin-with-options) that should be followed if your plugin takes options or configuration parameters.

Mixin is just a function that takes a class and returns an extended subclass.

Mixins can be then applied like this:

This **doesn't** work since mixins never modify the input:

Multiple mixins:

There are a couple of helpers in objection main module for applying multiple mixins.

Mixins can also be used as decorators:
