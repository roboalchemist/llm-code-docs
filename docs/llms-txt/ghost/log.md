# Source: https://docs.ghost.org/themes/helpers/utility/log.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# log

> Usage: `{{log value}}`

***

When running Ghost in development mode, you can use the `{{log}}` helper to output debug messages to the server console. In particular you can get handlebars to output the details of objects or the current context

For example, to output the full ‘context’ that handlebars currently has access to:

`{{log this}}`

Or, to log each post in the loop:

```handlebars  theme={"dark"}
{{#foreach posts}}
   {{log post}}
{{/foreach}}
```

If you’re developing a theme and running an install [using Ghost-CLI](/install/local/), you must use `NODE_ENV=development ghost run` to make debug output visible in the console.


Built with [Mintlify](https://mintlify.com).