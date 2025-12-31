# Source: https://relay.dev/docs/getting-started/babel-plugin/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Get Started]
-   [Relay Babel Plugin]

[Version: v20.1.0]

<div>

# Babel Plugin

</div>

Relay requires a [Babel plugin](https://www.npmjs.com/package/babel-plugin-relay) to convert GraphQL to compiler-generated runtime artifacts. Depending upon what framework/bundler you are using, there may be a framwork-specific plugin you can use:

-   Vite: [vite-plugin-relay](https://github.com/oscartbeaumont/vite-plugin-relay)
-   Next.js: [Relay config option](https://nextjs.org/docs/architecture/nextjs-compiler#relay)
-   SWC: [\@swc/plugin-relay](https://www.npmjs.com/package/@swc/plugin-relay)

If not, you can install the Babel plugin manually:

``` 
yarn add --dev babel-plugin-relay graphql
```

Add `"relay"` to the list of plugins in your `.babelrc` file:

``` 

```

Please note that the `"relay"` plugin should run before other plugins or presets to ensure the `graphql` template literals are correctly transformed. See Babel\'s [documentation on this topic](https://babeljs.io/docs/plugins/#pluginpreset-ordering).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/getting-started/babel-plugin.md)