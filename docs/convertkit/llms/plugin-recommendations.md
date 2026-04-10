# Source: https://developers.kit.com/plugins/media-source/plugin-recommendations.md

# Source: https://developers.kit.com/plugins/content-blocks/plugin-recommendations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Content blocks plugin recommendations

> Best practices, tips and tricks to get the most out of content block plugins

* For email client compatibility, we suggest that you use inline `style` attributes such as `<div style="color: red;"></div>` instead of CSS classes.
  * To test email client compatibility, we recommend using [https://www.caniemail.com](https://www.caniemail.com) and [https://www.litmus.com/](https://www.litmus.com/)
  * The only exception to this is if you need to include media queries to make your elements responsive on mobile, for example:

```html  theme={null}
    <style>
    @media only screen and (max-width:600px) {
        .a-unique-class { ... }
    }
    </style>

    <div class="a-unique-class">
    ...
    </div>
```

* Include `target=_blank` to all links

* Use the full path URL for all links to ensure they can be opened

* In most cases, you shouldn’t apply a background color to your plugin (unless the user is able to customize it). This is because the user might be using a custom background color on their email. By <em>not</em> applying a background color, your element’s background will automatically be the same as their email.


Built with [Mintlify](https://mintlify.com).