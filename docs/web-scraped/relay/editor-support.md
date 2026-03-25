# Source: https://relay.dev/docs/editor-support/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Get Started]
-   [Editor Support]

[Version: v20.1.0]

On this page

<div>

# Editor Support

</div>

*TL;DR: We have a [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=meta.relay)*

------------------------------------------------------------------------

The Relay compiler has a rich understanding of the GraphQL embedded in your code. We want to use that understanding to improve the developer experience of writing apps with Relay. So, starting in [v14.0.0](https://github.com/facebook/relay/releases/tag/v14.0.0), the new Rust Relay compiler can provide language features directly in your code editor. This means:

#### Relay compiler errors surface as red squiggles directly in your editor[​](#relay-compiler-errors-surface-as-red-squiggles-directly-in-your-editor "Direct link to Relay compiler errors surface as red squiggles directly in your editor") 

![](/img/docs/editor-support/diagnostics.png)

#### Autocomplete throughout your GraphQL tagged template literals[​](#autocomplete-throughout-your-graphql-tagged-template-literals "Direct link to Autocomplete throughout your GraphQL tagged template literals") 

![](/img/docs/editor-support/autocomplete.png)

#### Hover to see type information and documentation about Relay-specific features[​](#hover-to-see-type-information-and-documentation-about-relay-specific-features "Direct link to Hover to see type information and documentation about Relay-specific features") 

![](/img/docs/editor-support/hover.png)

#### `@deprecated` fields are rendered using ~~strikethrough~~[​](#deprecated-fields-are-rendered-using-strikethrough "Direct link to deprecated-fields-are-rendered-using-strikethrough") 

![](/img/docs/editor-support/deprecated.png)

#### Click-to-definition for fragments, fields and types[​](#click-to-definition-for-fragments-fields-and-types "Direct link to Click-to-definition for fragments, fields and types") 

![](/img/docs/editor-support/go-to-def.gif)

#### Quick fix suggestions for common errors[​](#quick-fix-suggestions-for-common-errors "Direct link to Quick fix suggestions for common errors") 

![](/img/docs/editor-support/code-actions.png)

## Language Server[​](#language-server "Direct link to Language Server") 

The editor support is implemented using the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) which means it can be used by a variety of editors, but in tandem with this release, [Terence Bezman](https://twitter.com/b_ez_man) from [Coinbase](https://www.coinbase.com/) has contributed an official VS Code extension.

[**Find it here!**](https://marketplace.visualstudio.com/items?itemName=meta.relay)

## Why Have a Relay-Specific Editor Extension?[​](#why-have-a-relay-specific-editor-extension "Direct link to Why Have a Relay-Specific Editor Extension?") 

The GraphQL foundation has an official language server and [VS Code extension](https://marketplace.visualstudio.com/items?itemName=GraphQL.vscode-graphql) which provides editor support for GraphQL generically. This can provide a good baseline experience, but for Relay users, getting this information directly from the Relay compiler offers a number of benefits:

-   Relay compiler errors can surface directly in the editor as "problems", often with suggested quick fixes
-   Hover information is aware Relay-specific features and directives and can link out to relevant documentation

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/editor-support.md)