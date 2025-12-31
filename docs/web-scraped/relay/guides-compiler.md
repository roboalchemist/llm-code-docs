# Source: https://relay.dev/docs/guides/compiler/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Get Started]
-   [Relay Compiler]

[Version: v20.1.0]

On this page

<div>

# Relay Compiler

</div>

Relay depends upon ahead-of-time compilation of GraphQL queries and fragments to generate artifacts that are used at runtime.

The Relay compiler is a command line tool that reads GraphQL fragments, queries, and mutations in your JavaScript code and generates TypeScript/Flow types and additional JavaScript code that gets included in your code via [Relay\'s Babel Plugin](/docs/getting-started/babel-plugin/).

This guide explains configuring and using the Relay Compiler.

## Configuration[​](#configuration "Direct link to Configuration") 

The Relay compiler will look for a Relay config in the following locations. It\'s up to you to decide which location works best for your project.

-   `relay.config.json` in your project root
-   `relay.config.(js/mjs/ts)` in your project root
-   A `"relay"` key in your `package.json`

The Relay compiler config tells Relay things like where it can find your GraphQL schema and what language your code is written in. A minimal Relay compiler config looks like this:

relay.config.json

``` 

```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

Install the [Relay VSCode extension](/docs/editor-support/) to get autocomplete, hover tips, and type checking for the options in your relay config.

The compiler config is very powerful, and includes many specialized configuration options. For a full enumeration of the available options see the [Compiler Configuration](/docs/getting-started/compiler-config/) page.

## Running the compiler[​](#running-the-compiler "Direct link to Running the compiler") 

It is generally recommended that you add a `scripts` entry to your `package.json` to make it easy to run the Relay compiler for your project.

package.json

``` 

}
```

With this added you can run the Relay compiler like so:

``` 
npm run relay
```

### Watch mode[​](#watch-mode "Direct link to Watch mode") 

If you have [watchman](https://facebook.github.io/watchman) installed you can pass `--watch` to the Relay compiler to have it continue running and automatically update generated files as you edit your product code:

``` 
npm run relay --watch
```

### Codemods[​](#codemods "Direct link to Codemods") 

The Relay compiler supports some built in codemods. Learn more in the [Codemods Guide](/docs/guides/codemods/).

### Help[​](#help "Direct link to Help") 

To learn about the other capabilities of the Relay compiler see it\'s extensive `--help` output:

``` 
npm run relay --help
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/getting-started/compiler.md)