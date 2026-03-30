# CLI

> Generates a type-safe client based on your Repo's schema.

## Generate

```
basehub generate
```

This command will get your BaseHub Token from your environment using [dotenv-mono](https://www.npmjs.com/package/dotenv-mono), use that to query the BaseHub API, and generate a type-safe SDK out of its schema.

### Arguments

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Name

Description

Default

Required

`--watch`

Watch mode will listen to schema changes and re-generate the SDK automatically.

`false`

No

`--output`

Specifcy a different location for the generated output.

`.basehub`

No

`--env-prefix`

Specify a different prefix for [relevant environment variables](#relevant-environment-variables).

`BASEHUB_`

No

`--draft`

Draft mode will query draft (non-committed) content from the GraphQL API.

`false`

No

`--ref`

BaseHub ref to use (branch name or commit ID)

`main`

No

### Aliases

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Command

Description

`basehub`

Same as running `basehub generate [...args]`

`basehub dev`

Same as running `basehub generate --watch --draft [...args]`

### Relevant Environment Variables

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Name

Description

Required

`TOKEN`

A Repo’s read or write token.

Yes

`REF`

Draft mode will query draft (non-committed) content from the GraphQL API.

No

## Dev

```
basehub dev
```

The `dev` command is very useful for local development. It basically runs `basehub generate --watch --draft [...args]` (notice how watch and draft mode are both being forced).