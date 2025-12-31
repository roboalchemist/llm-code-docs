# Source: https://relay.dev/docs/guides/codemods/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Codemods]
-   [Codemods]

[Version: v20.1.0]

On this page

<div>

# Codemods

</div>

The Relay compiler has the ability to make changes across the source files of your projects with the use of codemods. You can see the list of codemods available by running the Relay compiler\'s `codemod` command:

``` 
> relay codemod --help
Apply codemod (verification with auto-applied fixes)

Usage: relay codemod [OPTIONS] [CONFIG] <COMMAND>

Commands:
  mark-dangerous-conditional-fragment-spreads  Marks unaliased conditional fragment spreads as @dangerously_unaliased_fixme
  help                                         Print this message or the help of the given subcommand(s)

Arguments:
  [CONFIG]  Compile using this config file. If not provided, searches for a config in package.json under the `relay` key or `relay.config.json` files among other up from the current working directory

Options:
  -p, --project <project>  Compile only this project. You can pass this argument multiple times. to compile multiple projects. If excluded, all projects will be compiled
  -h, --help               Print help
```

## Available codemods[​](#available-codemods "Direct link to Available codemods") 

The compiler currently has these available codemods:

### mark-dangerous-conditional-fragment-spreads[​](#mark-dangerous-conditional-fragment-spreads "Direct link to mark-dangerous-conditional-fragment-spreads") 

This codemod finds fragment spreads that are *dangerously unaliased*; that is, the fragment might not be fetched due to a directive such as `@skip` or its inclusion on a mismatched type within a union. If such a conditional fragment is not aliased with [`@alias`](/docs/guides/alias-directive/), there is no way for the resulting generated Flow or TypeScript types to reflect its nullability. This codemod will add the `@dangerously_unaliased_fixme` directive to such fragment spreads, indicating to developers that there is a problem to be fixed. After applying this codemod, the `enforce_fragment_alias_where_ambiguous` feature flag can be enabled, which will ensure any future ambiguous fragment spreads must be aliased.

Since this codemod can potentially modify many files, there is an optional `--rollout` parameter which, if used alongside the `enforce_fragment_alias_where_ambiguous` feature flag in rollout mode, allows progressive codemod and enforcement of this validation.

### remove-unnecessary-required-directives[​](#remove-unnecessary-required-directives "Direct link to remove-unnecessary-required-directives") 

Removes [\@required](/docs/api-reference/graphql-and-directives/#required) directives from non-null fields within [\@throwOnFieldError](/docs/api-reference/graphql-and-directives/#throwonfielderror) fragments and operations, or linked fields with [`@catch`](/docs/guides/catch-directive/), where the compiler is certain that the directive does not change the generated types for the data being fetched.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/codemods.md)