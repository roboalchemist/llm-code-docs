# Source: https://biomejs.dev/internals/language-support/

# Language support 

Legend:

-   ✅: Supported
-   🚫: Not in progress
-   ⌛️: In progress
-   🟡: Experimental

  Language                                                   Parsing                                      Formatting                                      Linting                                         Plugin Support
  ---------------------------------------------------------- -------------------------------------------- ----------------------------------------------- ----------------------------------------------- -----------------------------------------------
  [JavaScript](#javascript-support)                          [✅]      [✅]         [✅]         [✅]
  [TypeScript](#typescript-support)                          [✅]      [✅]         [✅]         [✅]
  JSX                                                        [✅]      [✅]         [✅]         [✅]
  TSX                                                        [✅]      [✅]         [✅]         [✅]
  JSON                                                       [✅]      [✅]         [✅]         [🚫]
  JSONC                                                      [✅]      [✅]         [✅]         [🚫]
  HTML\*                                                     [✅]      [✅]         [✅]         [✅]
  [Vue](#html-super-languages-support)                       [🟡]   [🟡]      [🟡]      [🟡]
  [Svelte](#html-super-languages-support)                    [🟡]   [🟡]      [🟡]      [🟡]
  [Astro](#html-super-languages-support)                     [🟡]   [🟡]      [🟡]      [🟡]
  CSS                                                        [✅️]      [✅️]         [✅️]         [✅]
  [YAML](https://github.com/biomejs/biome/issues/2365)       [⌛️]    [🚫]   [🚫]   [🚫]
  GraphQL                                                    [✅️]      [✅️]         [✅️]         [🚫]
  [Markdown](https://github.com/biomejs/biome/issues/3718)   [⌛️]    [🚫]   [🚫]   [🚫]
  GritQL                                                     [✅️]      [✅️]         [🚫]   [🚫]

*\* currently requires [explicit opt-in](https://biomejs.dev/reference/configuration/#html)*

## JavaScript support

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "JavaScript support"]](#javascript-support)

Biome supports the ES2024 version of the language.

Biome supports only the official syntax. The team starts development of the new syntax when a proposal reaches [Stage 3](https://github.com/tc39/proposals#stage-3).

## TypeScript support

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "TypeScript support"]](#typescript-support)

Biome supports TypeScript version 5.6.

## JSONC support

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "JSONC support"]](#jsonc-support)

JSONC stands for "JSON with Comments." This format is widely used by various tools like [VS Code](https://code.visualstudio.com/docs/languages/json#_json-with-comments), [TypeScript](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html), [Babel](https://babeljs.io/docs/config-files), etc. because it lets users add comments to configuration files. However, since JSONC isn't a strictly defined standard, there's some variation in how different tools handle trailing commas in JSONC files. To accommodate this, Biome doesn't provide a dedicated language configuration for JSONC. Instead, we've enhanced our JSON parsing and formatting capabilities with options like `json.parser.allowComments`, `json.parser.allowTrailingCommas`, and `json.formatter.trailingCommas`. This approach allows Biome to effectively support different variants of JSON files.

For files with an extension name of `.jsonc` or those identified as `jsonc` according to the [language identifier](https://code.visualstudio.com/docs/languages/identifiers), Biome automatically applies the following default settings for parsing and formatting them:

-   `json.parser.allowComments`: `true`
-   `json.parser.allowTrailingCommas`: `true`
-   `json.formatter.trailingCommas`: `none`

Please note, some well-known files like `tsconfig.json` and `.babelrc` don't use the `.jsonc` extension but still allow comments and trailing commas. While others, such as `.eslintrc.json`, only allow comments. Biome is able to identify these files and adjusts the `json.parser.allowTrailingCommas` option accordingly to ensure they are correctly parsed.

[This section](/guides/configure-biome#well-known-files) gives the full list of well-known files that Biome can recognize.

## HTML super languages support

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "HTML super languages support"]](#html-super-languages-support)

Since version `v2.3.0`, Biome supports Vue, Svelte and Astro file out of the box. This means that Biome is able to format and lint the HTML, CSS and JavaScript parts of the files.

However, this **support must be considered experimental** and subject to changes and improvements. In `v2.3.0`, we landed the architecture that enables this feature, however some formatting and linting rules must be adjusted.

In particular, as for `v2.3.0`, Biome doesn't do any particular parsing for language specific syntax, for example the control-flow syntax of Svelte e.g. ` `. This means that formatting might not match the desired expectations, and lint rules might not detect some cases.

Lint rules that work across embedded languages aren't supported yet.

### Linting HTML-ish languages

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Linting HTML-ish languages"]](#linting-html-ish-languages)

Some lint rules don't work across boundaries just yet. For example, the following `.vue` file, the rule `noUnusedVariables` will flag a false positive for `greeting`:

<figure class="frame has-title not-content">
<pre data-language="vue"><code>1&lt;script setup lang=&quot;ts&quot;&gt;2    const greeting = &quot;hello world&quot;3&lt;/script&gt;4
5&lt;template&gt;6    &lt;h1&gt;}&lt;/h1&gt;7&lt;/template&gt;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">app.vue</span></figcaption>
</figure>

When **linting** `.svelte`, `.astro` or `.vue` files, it's advised to turn off a few additional rules to prevent false positive linting errors caused by our partial support. Use the option `overrides` for that:

<figure class="frame not-content">
<pre data-language="json"><code>1,11          &quot;correctness&quot;: 15        }16      }17    }18  ]19}</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

### Formatting with different settings

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Formatting with different settings"]](#formatting-with-different-settings)

With Biome, you can control the formatting of different languages. Now that Biome can process multiple languages in the same file, the chances of inconsistencies can grow based on your configuration.

For example, you could risk having a file mixed with tabs and spaces when formatting a HTML-ish file that contains JavaScript and CSS code, like in the following example (we assume full support is enabled):

<figure class="frame not-content">
<pre data-language="json"><code>16  },7  &quot;css&quot;: 12  }13}</code></pre>
<div class="copy">
<div>

</div>
</div>
</figure>

We created a [GitHub discussion](https://github.com/biomejs/biome/discussions/7754) to address the issue, join the discussion and let us know what you think.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTFDMTEuNzM0OCAxMSAxMS40ODA0IDExLjEwNTQgMTEuMjkyOSAxMS4yOTI5QzExLjEwNTQgMTEuNDgwNCAxMSAxMS43MzQ4IDExIDEyVjE2QzExIDE2LjI2NTIgMTEuMTA1NCAxNi41MTk2IDExLjI5MjkgMTYuNzA3MUMxMS40ODA0IDE2Ljg5NDYgMTEuNzM0OCAxNyAxMiAxN0MxMi4yNjUyIDE3IDEyLjUxOTYgMTYuODk0NiAxMi43MDcxIDE2LjcwNzFDMTIuODk0NiAxNi41MTk2IDEzIDE2LjI2NTIgMTMgMTZWMTJDMTMgMTEuNzM0OCAxMi44OTQ2IDExLjQ4MDQgMTIuNzA3MSAxMS4yOTI5QzEyLjUxOTYgMTEuMTA1NCAxMi4yNjUyIDExIDEyIDExWk0xMi4zOCA3LjA4QzEyLjEzNjUgNi45Nzk5OCAxMS44NjM1IDYuOTc5OTggMTEuNjIgNy4wOEMxMS40OTczIDcuMTI3NTkgMTEuMzg1MSA3LjE5ODk2IDExLjI5IDcuMjlDMTEuMjAxNyA3LjM4NzIgMTEuMTMwNiA3LjQ5ODgyIDExLjA4IDcuNjJDMTEuMDI0IDcuNzM4NjggMTAuOTk2NiA3Ljg2ODgyIDExIDhDMTAuOTk5MiA4LjEzMTYxIDExLjAyNDUgOC4yNjIwNyAxMS4wNzQyIDguMzgzOTFDMTEuMTI0IDguNTA1NzQgMTEuMTk3MyA4LjYxNjU2IDExLjI5IDguNzFDMTEuMzg3MiA4Ljc5ODMzIDExLjQ5ODggOC44NjkzNiAxMS42MiA4LjkyQzExLjc3MTUgOC45ODIyNCAxMS45MzYgOS4wMDYzMiAxMi4wOTkgOC45OTAxMUMxMi4yNjE5IDguOTczOTEgMTIuNDE4NCA4LjkxNzkyIDEyLjU1NDcgOC44MjcwN0MxMi42OTEgOC43MzYyMiAxMi44MDI5IDguNjEzMjggMTIuODgwNSA4LjQ2OTA3QzEyLjk1ODIgOC4zMjQ4NiAxMi45OTkyIDguMTYzNzggMTMgOEMxMi45OTYzIDcuNzM1MjMgMTIuODkyNyA3LjQ4MTYzIDEyLjcxIDcuMjlDMTIuNjE0OSA3LjE5ODk2IDEyLjUwMjggNy4xMjc1OSAxMi4zOCA3LjA4Wk0xMiAyQzEwLjAyMjIgMiA4LjA4ODc5IDIuNTg2NDkgNi40NDQzIDMuNjg1M0M0Ljc5OTgxIDQuNzg0MTIgMy41MTgwOSA2LjM0NTkgMi43NjEyMSA4LjE3MzE3QzIuMDA0MzMgMTAuMDAwNCAxLjgwNjMgMTIuMDExMSAyLjE5MjE1IDEzLjk1MDlDMi41NzggMTUuODkwNyAzLjUzMDQxIDE3LjY3MjUgNC45Mjg5NCAxOS4wNzExQzYuMzI3NDYgMjAuNDY5NiA4LjEwOTI5IDIxLjQyMiAxMC4wNDkxIDIxLjgwNzlDMTEuOTg4OSAyMi4xOTM3IDEzLjk5OTYgMjEuOTk1NyAxNS44MjY4IDIxLjIzODhDMTcuNjU0MSAyMC40ODE5IDE5LjIxNTkgMTkuMjAwMiAyMC4zMTQ3IDE3LjU1NTdDMjEuNDEzNSAxNS45MTEyIDIyIDEzLjk3NzggMjIgMTJDMjIgMTAuNjg2OCAyMS43NDEzIDkuMzg2NDIgMjEuMjM4OCA4LjE3MzE3QzIwLjczNjMgNi45NTk5MSAxOS45OTk3IDUuODU3NTIgMTkuMDcxMSA0LjkyODkzQzE4LjE0MjUgNC4wMDAzNSAxNy4wNDAxIDMuMjYzNzUgMTUuODI2OCAyLjc2MTJDMTQuNjEzNiAyLjI1ODY2IDEzLjMxMzIgMiAxMiAyWk0xMiAyMEMxMC40MTc4IDIwIDguODcxMDQgMTkuNTMwOCA3LjU1NTQ0IDE4LjY1MThDNi4yMzk4NSAxNy43NzI3IDUuMjE0NDcgMTYuNTIzMyA0LjYwODk3IDE1LjA2MTVDNC4wMDM0NyAxMy41OTk3IDMuODQ1MDQgMTEuOTkxMSA0LjE1MzcyIDEwLjQzOTNDNC40NjI0IDguODg3NDMgNS4yMjQzMyA3LjQ2MTk3IDYuMzQzMTUgNi4zNDMxNUM3LjQ2MTk3IDUuMjI0MzMgOC44ODc0MyA0LjQ2MjQgMTAuNDM5MyA0LjE1MzcyQzExLjk5MTEgMy44NDUwNCAxMy41OTk3IDQuMDAzNDYgMTUuMDYxNSA0LjYwODk2QzE2LjUyMzMgNS4yMTQ0NyAxNy43NzI3IDYuMjM5ODQgMTguNjUxOCA3LjU1NTQ0QzE5LjUzMDggOC44NzEwMyAyMCAxMC40MTc3IDIwIDEyQzIwIDE0LjEyMTcgMTkuMTU3MiAxNi4xNTY2IDE3LjY1NjkgMTcuNjU2OUMxNi4xNTY2IDE5LjE1NzEgMTQuMTIxNyAyMCAxMiAyMFoiPjwvcGF0aD48L3N2Zz4=)Note

This last section might become outdated, so it's advised to use the [playground](https://biomejs.dev/playground), and check if your feature has been implemented.

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLTIyY21rdDNwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuMmVtOyI+PHBhdGggZD0iTTIyIDcuMjRhMSAxIDAgMCAwLS4yOS0uNzFsLTQuMjQtNC4yNGExIDEgMCAwIDAtMS4xLS4yMiAxIDEgMCAwIDAtLjMyLjIybC0yLjgzIDIuODNMMi4yOSAxNi4wNWExIDEgMCAwIDAtLjI5LjcxVjIxYTEgMSAwIDAgMCAxIDFoNC4yNGExIDEgMCAwIDAgLjc2LS4yOWwxMC44Ny0xMC45M0wyMS43MSA4Yy4xLS4xLjE3LS4yLjIyLS4zM2ExIDEgMCAwIDAgMC0uMjR2LS4xNGwuMDctLjA1Wk02LjgzIDIwSDR2LTIuODNsOS45My05LjkzIDIuODMgMi44M0w2LjgzIDIwWk0xOC4xNyA4LjY2bC0yLjgzLTIuODMgMS40Mi0xLjQxIDIuODIgMi44Mi0xLjQxIDEuNDJaIj48L3BhdGg+PC9zdmc+)Edit page](https://github.com/biomejs/website/edit/main/src/content/docs/internals/language-support.mdx)

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNyAxMUg5LjQxbDMuMy0zLjI5YTEuMDA0IDEuMDA0IDAgMSAwLTEuNDItMS40MmwtNSA1YTEgMSAwIDAgMC0uMjEuMzMgMSAxIDAgMCAwIDAgLjc2IDEgMSAwIDAgMCAuMjEuMzNsNSA1YTEuMDAyIDEuMDAyIDAgMCAwIDEuNjM5LS4zMjUgMSAxIDAgMCAwLS4yMTktMS4wOTVMOS40MSAxM0gxN2ExIDEgMCAwIDAgMC0yWiI+PC9wYXRoPjwvc3ZnPg==) [ Previous\
[Philosophy] ]](/internals/philosophy) [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNy45MiAxMS42MmExLjAwMSAxLjAwMSAwIDAgMC0uMjEtLjMzbC01LTVhMS4wMDMgMS4wMDMgMCAxIDAtMS40MiAxLjQybDMuMyAzLjI5SDdhMSAxIDAgMCAwIDAgMmg3LjU5bC0zLjMgMy4yOWExLjAwMiAxLjAwMiAwIDAgMCAuMzI1IDEuNjM5IDEgMSAwIDAgMCAxLjA5NS0uMjE5bDUtNWExIDEgMCAwIDAgLjIxLS4zMyAxIDEgMCAwIDAgMC0uNzZaIj48L3BhdGg+PC9zdmc+) [ Next\
[Architecture] ]](/internals/architecture)

Sponsored by

![Depot](/_astro/depot-logo-horizontal-on-light@3x.CwT7__a0_Z1k23Gh.webp?dpl=69532f2b69cab10008a149f1) ![Depot](/_astro/depot-logo-horizontal-on-dark@3x.BWjsBfKV_Z29sH19.webp?dpl=69532f2b69cab10008a149f1)

Copyright (c) 2023-present Biome Developers and Contributors.