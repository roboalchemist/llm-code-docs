# Script Parser

Source: https://knip.dev/features/script-parser

Knip parses shell commands and scripts to find additional dependencies, entry
files and configuration files in various places:

- Inpackage.json
- InCLI arguments
- Inscripts
- Insource code

Shell scripts can be read and statically analyzed, but they’re not executed.

## package.json

Themain,bin,exportsandscriptsfields may contain entry files. Let’s
take a look at this example:

```typescript
{"name":"my-package","main":"index.js","exports":{"./lib":{"import":"./dist/index.mjs","require":"./dist/index.cjs"}},"bin":{"program":"bin/cli.js"},"scripts":{"build":"rollup src/entry.ts","start":"node --loader tsx server.ts"}}
```

From this example, Knip automatically adds the following files as entry files:

- index.js
- ./dist/index.mjs
- ./dist/index.cjs
- bin/cli.js
- src/entry.ts
- server.ts

### Excluded files

Knip would not add theexportsif thedistfolder is matching a pattern in a
relevant.gitignorefile orignoreoption.

Knip does not add scripts without a standard extension. For instance, thebin/toolfile might be a valid executable for Node.js, but wouldn’t be added
or parsed by Knip.

### CLI Arguments

When parsing thescriptsofpackage.jsonand other files, Knip detects
various types of inputs. Some examples:

- The first positional argument is usually an entry file
- Configuration files are often in the-cor--configargument
- The--require,--loaderor--importarguments are often dependencies

```typescript
{"name":"my-lib","scripts":{"start":"node --import tsx/esm run.ts","bundle":"tsup -c tsup.lib.config.ts","type-check":"tsc -p tsconfig.app.json"}}
```

The"start"script will havetsxmarked as a referenced dependency, and addsrun.tsas an entry file.

Additionally, the following files are detected as configuration files:

- tsup.lib.config.ts- to be handled by the tsup plugin
- tsconfig.app.json- to be handled by the TypeScript plugin

Such executables and their arguments are all defined in plugins separately for
fine-grained results.

## Scripts

Plugins may also use the script parser to extract entry files and dependencies
from commands. A few examples:

- GitHub Actions: workflow files may containruncommands (e.g..github/workflows/ci.yml)
- Husky & Lefthook: Git hooks such as.git/hooks/pre-pushcontain scripts;
alsolefthook.ymlhasruncommands
- Lint Staged: configuration values are all commands
- Nx: task executors andnx:run-commandsexecutors inproject.jsoncontains
scripts
- Release It:hookscontain commands

Plugins can also return configuration files. Some examples:

- The Angular plugin detectsoptions.tsConfigas a TypeScript config file
- The GitHub Actions plugin parsesruncommands which may contain
configuration file paths

## Source Code

When Knip is walking the abstract syntax trees (ASTs) of JavaScript and
TypeScript source code files, it looks for imports and exports. But there’s a
few more (rather obscure) things that Knip detects in the process. Below are
examples of additional scripts Knip parses to find entry files and dependencies.

### bun

If thebundependency is imported in source code, Knip considers the contents
of$template tags to be scripts:

```typescript
import{ $ }from'bun';await$`bun boxen I ❤ unicorns`;await$`boxen I ❤ unicorns`;
```

Parsing the script results in theboxenbinary (theboxen-clidependency) as
referenced (twice).

### execa

If theexecadependency is imported in source code, Knip considers the
contents of$template tags to be scripts:

```typescript
await$({ stdio:'inherit'})`c8 node hydrate.js`;
```

Parsing the script results inhydrate.jsadded as an entry file and thec8binary/dependency as referenced.

### zx

If thezxdependency is imported in source code, Knip considers the contents
of$template tags to be scripts:

```typescript
await$`node scripts/parse.js`;
```

This will addscripts/parse.jsas an entry file.

ISC License© 2024Lars Kappert

