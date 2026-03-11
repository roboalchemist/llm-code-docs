# Source: https://www.courier.com/docs/platform/content/template-designer/handlebars-designer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Handlebars Editor for Email Templates

> Courier’s Handlebars editor allows direct HTML/Handlebars editing for email templates, ideal for importing custom designs. Edits are channel-specific and non-reusable—consider template blocks for shared, cross-channel content.

> It's possible to edit the HTML of a Courier Email notification directly using the Handlebars template override.

## Where Handlebars Can Be Used

Handlebars templates can be used in several contexts within Courier:

* **Email Template Overrides**: Direct HTML/Handlebars editing for email notifications (described below)
* **[Template Blocks](/platform/content/content-blocks/template-blocks)**: Reusable Handlebars components within the Template Designer
* **[Brand Templates](/platform/content/brands/brands-overview)**: Custom header/footer templates for brand consistency
* **[Brand Snippets](/platform/content/brands/brand-snippets)**: Reusable Handlebars code snippets across templates

Courier extends Handlebars with [custom helpers](/platform/content/template-designer/handlebars-helpers) for logic operations, string formatting, math functions, date handling, and internationalization.

## Override the Template Designer With Handlebars

If you want to edit the HTML / Handlebars code of an Email Template directly, you can switch from the Template Designer to the Handlebars editor.

<Frame caption="Create Your Notification">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/handlebars-toggle.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=f0e390484bba4bc641b73bdc1647ef92" alt="Create Your Notification" width="1298" height="400" data-path="assets/platform/content/handlebars-toggle.png" />
</Frame>

This is a useful way to import existing HTML templates into Courier.

<Frame caption="HTML Template Editor">
  <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/handlebars-editor.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=740e188aba40b5a6f98c6e31c7d0a845" alt="Create Your Notification" width="2862" height="1546" data-path="assets/platform/content/handlebars-editor.png" />
</Frame>

<Warning>
  Content created using the Handlebars override is not reusable across channels.
</Warning>

<Warning>
  When you use the Handlebars override, your brand's header, footer, and CSS styles are **not** applied. The override replaces the entire email body. If you need brand styling, include it directly in your Handlebars HTML or use [template blocks](/platform/content/content-blocks/template-blocks) within the Template Designer instead.
</Warning>

If you need to use Handlebars for a portion of your email, use [template blocks](/platform/content/content-blocks/template-blocks) and combine them with other [block types](/platform/content/template-designer/template-designer-overview#reusable-drag-and-drop-content) to allow your non-handlebars code content to be re-used in other channels.

Edits made in the Handlebars editor will not apply to other Email notifications. To define the look and feel of all your emails at once, [customize your default brand template](/platform/content/brands/brands-overview#customizing-brands).

## Use Cases

### Conditionally Rendering Content

`#if` blocks can be used to control whether content is rendered.

```handlebars  theme={null}
<!-- equal -->
{{#if (condition (var "some_variable") "==" "show")}}
  <div align="center">Hello!</div>
{{/if}}

<!-- strict equal -->
{{#if (condition (var "some_variable") "===" "show")}}
  <div align="center">Hello!</div>
{{/if}}

<!-- not equal -->
{{#if (condition (var "some_variable") "!=" "hide")}}
  <div align="center">Hello!</div>
{{/if}}

<!-- greater than -->
{{#if (condition (var "some_array.length") ">" 0)}}
  <div align="center">Hello!</div>
{{/if}}

<!-- greater than or equal -->
{{#if (condition (var "some_array.length") ">=" 0)}}
  <div align="center">Hello!</div>
{{/if}}

<!-- less than -->
{{#if (condition (var "some_array.length") "<" 0)}}
  <div align="center">Hello!</div>
{{/if}}

<!-- less than or equal -->
{{#if (condition (var "some_array.length") "<=" 0)}}
  <div align="center">Hello!</div>
{{/if}}
```

### Pluralizing Text

The `formatMessage` helper can be used to pluralize text in rendered content. Pluralization respects the [ICU format](https://unicode-org.github.io/icu/userguide/format_parse/messages/) and entries follow [Unicode CLDR rules](https://cldr.unicode.org/index/cldr-spec/plural-rules).

**Example**

```handlebars  theme={null}
Your list contains
{{formatMessage
  "{itemCount, plural,
    =0 {no items}
    one {# item}
    other {# items}
}"
  itemCount=itemCount
}}.
```

### Setting Variables in the Payload

Using a Handlebars block, you can transform and set a variable, which can then be used in a template:

```handlebars  theme={null}
{{ set "number_rounded (round (var "data.number" )) }}
```

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Designer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Preview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://mintcdn.com/courier-4f1f25dc/X4imlV9f_sunHT-I/platform/content/template-designer/set-variable-designer.png?fit=max&auto=format&n=X4imlV9f_sunHT-I&q=85&s=d2c4f44ed2d65cdbf65d6e0529ad6f53" alt="kewl" width="1468" height="1222" data-path="platform/content/template-designer/set-variable-designer.png" /> | <img src="https://mintcdn.com/courier-4f1f25dc/X4imlV9f_sunHT-I/platform/content/template-designer/set-variable-preview.png?fit=max&auto=format&n=X4imlV9f_sunHT-I&q=85&s=3f61d406a9bf50101f511dbde4e94b25" alt="kewl" width="1850" height="1724" data-path="platform/content/template-designer/set-variable-preview.png" /> |

### Using the intl Block for Localization

You can wrap Handlebars functions with the intl block in order to access internationalization features including currency, number formatting and dates. See [Handlebars-intl](https://github.com/formatjs/handlebars-intl) for more information.

```handlebars  theme={null}
{{#intl formats=intl.formats locales="en-US"}}
  {{set
    "winPct_formatted"
    (formatMessage "{winPct, number, maximumFractionDigits=2}" winPct=(var "data.winPct"))
  }}
{{/intl}}
```
