# Source: https://docs.ghost.org/themes/helpers/utility/partials.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# partials

> Usage: `{{> "partial-name"}}`

***

`{{> "partials"}}` is a helper for reusing chunks of template code in handlebars files. This can be useful for any repeating elements, such as a post card design, or for splitting out components like a header for easier to manage template files.

All partials are stored in the `partials/` directory of the theme. Partials will inherit context and make that context available within the partial file.

### Example

```handlebars  theme={"dark"}
{{#foreach posts}}

  {{> "post-card"}}

{{/foreach}}
```

```html  theme={"dark"}
<!-- partials/post-card.hbs -->
<article class="post-card.hbs">
  <h2 class="post-card-title">
    <a href="{{url}}">{{title}}</a>
  </h2>
  <p>{{excerpt words="30"}}</p>
</article>
```

### Partial properties

Partials can take properties as well which provide the option to set contextual values per use case.

#### Properties example

```handlebars  theme={"dark"}
{{> "call-to-action" heading="Sign up now"}}
```

```html  theme={"dark"}
<!-- partials/call-to-action.hbs -->
<aside>
  {{#if heading}}
    <h2>{{heading}}</h2>
  {{/if}}
  <form>
    <!-- ... -->
  </form>
</aside>
```


Built with [Mintlify](https://mintlify.com).