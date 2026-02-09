# Source: https://bun.com/docs/guides/runtime/import-toml.md

> ## Documentation Index
> Fetch the complete documentation index at: https://bun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Import a TOML file

Bun natively supports importing `.toml` files.

```toml data.toml icon="file-code" theme={"theme":{"light":"github-light","dark":"dracula"}}
name = "bun"
version = "1.0.0"

[author]
name = "John Dough"
email = "john@dough.com"
```

***

Import the file like any other source file.

```ts data.ts icon="https://mintcdn.com/bun-1dd33a4e/Hq64iapoQXHbYMEN/icons/typescript.svg?fit=max&auto=format&n=Hq64iapoQXHbYMEN&q=85&s=c6cceedec8f82d2cc803d7c6ec82b240" theme={"theme":{"light":"github-light","dark":"dracula"}}
import data from "./data.toml";

data.name; // => "bun"
data.version; // => "1.0.0"
data.author.name; // => "John Dough"
```

***

See [Docs > Runtime > TypeScript](/runtime/typescript) for more information on using TypeScript with Bun.
