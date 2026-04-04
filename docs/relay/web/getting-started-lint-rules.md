# Source: https://relay.dev/docs/getting-started/lint-rules/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Get Started]
-   [Relay ESLint Plugin]

[Version: v20.1.0]

On this page

<div>

# Relay ESLint Plugin

</div>

One of the unique features enabled by Relay is the ability to statically detect unused GraphQL fields. This can [categorically prevent](https://relay.dev/blog/2023/10/24/how-relay-enables-optimal-data-fetching/) the \"append only query\" problem that is a common disfunction in many GraphQL clients.

![Relay ESLint Plugin](/assets/images/no-unused-fields-a269dbf72527dd3e11b2e99ea6b14047.png)

This validation, and other helpful checks, are enabled by Relay\'s ESLint plugin [`eslint-plugin-relay`](https://www.npmjs.com/package/eslint-plugin-relay). **The Relay ESLint plugin is a key part of the Relay developer experience**.

## Installation[​](#installation "Direct link to Installation") 

Assuming you have [ESLint](https://eslint.org/) already installed, you can add the Relay ESLint plugin to your project by running:

``` 
npm install --save-dev eslint-plugin-relay
```

Then update your ESLint configuration to include the plugin:

``` 
import relay from 'eslint-plugin-relay';

export default [
  // ... other ESlint Config
  ,
    rules: relay.configs['ts-recommended'].rules,
  },
];
```

## Rule Descriptions[​](#rule-descriptions "Direct link to Rule Descriptions") 

The following validation rules are included in the Relay ESLint plugin:

### `relay/unused-fields`[​](#relayunused-fields "Direct link to relayunused-fields") 

Ensures that every GraphQL field referenced is used within the module that includes it. This helps enable Relay\'s [optimal data fetching](https://relay.dev/blog/2023/10/24/how-relay-enables-optimal-data-fetching/).

### `relay/no-future-added-value`[​](#relayno-future-added-value "Direct link to relayno-future-added-value") 

Ensures code does not try to explicitly handle the `"%future added value"` enum variant which Relay inserts as a placeholder to ensure you handle the possibility that new enum variants may be added by the server after your application has been deployed.

### `relay/graphql-syntax`[​](#relaygraphql-syntax "Direct link to relaygraphql-syntax") 

Ensures each `graphql` tagged template literal contains syntactically valid GraphQL. This is also validated by the Relay Compiler, but the ESLint plugin can often provide faster feedback.

### `relay/graphql-naming`[​](#relaygraphql-naming "Direct link to relaygraphql-naming") 

Ensures GraphQL fragments and queries follow Relay\'s naming conventions. This is also validated by the Relay Compiler, but the ESLint plugin can often provide faster feedback.

### `relay/function-required-argument`[​](#relayfunction-required-argument "Direct link to relayfunction-required-argument") 

Ensures that `readInlineData` is always passed an explicit argument even though that argument is allowed to be `undefined` at runtime.

### `relay/hook-required-argument`[​](#relayhook-required-argument "Direct link to relayhook-required-argument") 

Ensures that Relay hooks are always passed an explicit argument even though that argument is allowed to be `undefined` at runtime.

### `relay/must-colocate-fragment-spreads`[​](#relaymust-colocate-fragment-spreads "Direct link to relaymust-colocate-fragment-spreads") 

Ensures that when a fragment spread is added within a module, that module directly imports the module which defines that fragment. This prevents the anti-pattern when one component fetches a fragment that is not used by a direct child component. **Note**: This rule leans heavily on Meta\'s globally unique module names. It likely won\'t work well in other environments.

## Suppressing rules within graphql tags[​](#suppressing-rules-within-graphql-tags "Direct link to Suppressing rules within graphql tags") 

The following rules support suppression within graphql tags:

-   `relay/unused-fields`
-   `relay/must-colocate-fragment-spreads`

Supported rules can be suppressed by adding `# eslint-disable-next-line relay/name-of-rule` to the preceding line:

``` 
graphql`
  fragment foo on Page 
`;
```

Note that only the `eslint-disable-next-line` form of suppression works. `eslint-disable-line` doesn\'t currently work until graphql-js provides support for [parsing Comment nodes](https://github.com/graphql/graphql-js/issues/2241) in their AST.

## Contributing[​](#contributing "Direct link to Contributing") 

If you wish to contribute to the Relay ESLint plugin, you can find the code on GitHub at [relay/eslint-plugin-relay](https://github.com/relayjs/eslint-plugin-relay/).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/getting-started/lint-rules.md)