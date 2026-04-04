# Source: https://ast-grep.github.io/catalog/html.md

---
url: /catalog/html.md
---
# HTML

This page curates a list of example ast-grep rules to check and to rewrite HTML code.

:::tip Use HTML parser for frameworks
You can leverage the [`languageGlobs`](/reference/sgconfig.html#languageglobs) option to parse framework files as plain HTML, such as `vue`, `svelte`, and `astro`.

**Caveat**: This approach may not parse framework-specific syntax, like Astro's [frontmatter script](https://docs.astro.build/en/basics/astro-components/#the-component-script) or [Svelte control flow](https://svelte.dev/docs/svelte/if). You will need to load [custom languages](/advanced/custom-language.html) for such cases.
:::

## Upgrade Ant Design Vue&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6Imh0bWwiLCJxdWVyeSI6IiIsInJld3JpdGUiOiIiLCJzdHJpY3RuZXNzIjoicmVsYXhlZCIsInNlbGVjdG9yIjoiIiwiY29uZmlnIjoidXRpbHM6XG4gIGluc2lkZS10YWc6XG4gICAgaW5zaWRlOlxuICAgICAga2luZDogZWxlbWVudCBcbiAgICAgIHN0b3BCeTogeyBraW5kOiBlbGVtZW50IH1cbiAgICAgIGhhczpcbiAgICAgICAgc3RvcEJ5OiB7IGtpbmQ6IHRhZ19uYW1lIH1cbiAgICAgICAga2luZDogdGFnX25hbWVcbiAgICAgICAgcGF0dGVybjogJFRBR19OQU1FXG5ydWxlOlxuICBraW5kOiBhdHRyaWJ1dGVfbmFtZVxuICByZWdleDogOnZpc2libGVcbiAgbWF0Y2hlczogaW5zaWRlLXRhZyAgXG5maXg6IDpvcGVuXG5jb25zdHJhaW50czpcbiAgVEFHX05BTUU6XG4gICAgcmVnZXg6IGEtbW9kYWx8YS10b29sdGlwIiwic291cmNlIjoiPHRlbXBsYXRlPlxuICA8YS1tb2RhbCA6dmlzaWJsZT1cInZpc2libGVcIj5jb250ZW50PC9hLW1vZGFsPlxuICA8YS10b29sdGlwIDp2aXNpYmxlPVwidmlzaWJsZVwiIC8+XG4gIDxhLXRhZyA6dmlzaWJsZT1cInZpc2libGVcIj50YWc8L2EtdGFnPlxuPC90ZW1wbGF0ZT4ifQ==)

### Description

ast-grep can be used to upgrade Vue template using the HTML parser.

This rule is an example to upgrade [one breaking change](https://next.antdv.com/docs/vue/migration-v4#component-api-adjustment) in [Ant Design Vue](https://next.antdv.com/components/overview) from v3 to v4, unifying the controlled visible API of the component popup.

It is designed to identify and replace the `visible` attribute with the `open` attribute for specific components like `a-modal` and `a-tooltip`. Note the rule should not replace other visible attributes that are not related to the component popup like `a-tag`.

The rule can be broken down into the following steps:

1. Find the target attribute name by `kind` and `regex`
2. Find the attribute's enclosing element using `inside`, and get its tag name
3. Ensure the tag name is related to popup components, using constraints

### YAML

```yaml
id: upgrade-ant-design-vue
language: HTML
utils:
  inside-tag:
    # find the enclosing element of the attribute
    inside:
      kind: element
      stopBy: { kind: element } # only the closest element
      # find the tag name and store it in metavar
      has:
        stopBy: { kind: tag_name }
        kind: tag_name
        pattern: $TAG_NAME
rule:
  # find the target attribute_name
  kind: attribute_name
  regex: :visible
  # find the element
  matches: inside-tag
# ensure it only matches modal/tooltip but not tag
constraints:
  TAG_NAME:
    regex: a-modal|a-tooltip
fix: :open
```

### Example

```html {2,3}
<template>
  <a-modal :visible="visible">content</a-modal>
  <a-tooltip :visible="visible" />
  <a-tag :visible="visible">tag</a-tag>
</template>
```

### Diff

```html
<template>
  <a-modal :visible="visible">content</a-modal> // [!code --]
  <a-modal :open="visible">content</a-modal> // [!code ++]
  <a-tooltip :visible="visible" /> // [!code --]
  <a-tooltip :open="visible" /> // [!code ++]
  <a-tag :visible="visible">tag</a-tag>
</template>
```

### Contributed by

Inspired by [Vue.js RFC](https://github.com/vuejs/rfcs/discussions/705#discussion-7255672)

## Extract i18n Keys&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6Imh0bWwiLCJxdWVyeSI6IiIsInJld3JpdGUiOiIiLCJzdHJpY3RuZXNzIjoicmVsYXhlZCIsInNlbGVjdG9yIjoiIiwiY29uZmlnIjoicnVsZTpcbiAga2luZDogdGV4dFxuICBwYXR0ZXJuOiAkVFxuICBub3Q6XG4gICAgcmVnZXg6ICdcXHtcXHsuKlxcfVxcfSdcbmZpeDogXCJ7eyAkKCckVCcpIH19XCIiLCJzb3VyY2UiOiI8dGVtcGxhdGU+XG4gIDxzcGFuPkhlbGxvPC9zcGFuPlxuICA8c3Bhbj57eyB0ZXh0IH19PC9zcGFuPlxuPC90ZW1wbGF0ZT4ifQ==)

### Description

It is tedious to manually find and replace all the text in the template with i18n keys. This rule helps to extract static text into i18n keys. Dynamic text, e.g. mustache syntax, will be skipped.

In practice, you may want to map the extracted text to a key in a dictionary file. While this rule only demonstrates the extraction part, further mapping process can be done via a script reading the output of ast-grep's [`--json`](/guide/tools/json.html) mode, or using [`@ast-grep/napi`](/guide/api-usage/js-api.html).

### YAML

```yaml
id: extract-i18n-key
language: html
rule:
  kind: text
  pattern: $T
  # skip dynamic text in mustache syntax
  not: { regex: '\{\{.*\}\}' }
fix: "{{ $('$T') }}"
```

### Example

```html {2}
<template>
  <span>Hello</span>
  <span>{{ text }}</span>
</template>
```

### Diff

```html
<template>
  <span>Hello</span> // [!code --]
  <span>{{ $('Hello') }}</span> // [!code ++]
  <span>{{ text }}</span>
</template>
```

### Contributed by

Inspired by [Vue.js RFC](https://github.com/vuejs/rfcs/discussions/705#discussion-7255672)
