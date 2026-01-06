# Configuration

Source: https://knip.dev/reference/configuration

This page lists all configuration file options.

## File Types

### JSON Schema

A$schemafield is a URL that you put at the top of your JSON file. This
allows you to get red squiggly lines inside of your IDE when you make a typo or
provide an otherwise invalid configuration option.

In JSON, use the provided JSON schema:

```typescript
{"$schema":"https://unpkg.com/knip@5/schema.json"}
```

### JSONC

In JSONC, use the provided JSONC schema:

```typescript
{"$schema":"https://unpkg.com/knip@5/schema-jsonc.json"}
```

Use JSONC if you want to use comments and/or trailing commas.

### TypeScript

Seedynamic configurationabout dynamic and typed configuration files.

## Project

### entry

Array of glob patterns to find entry files. Prefix with!for negation.
Example:

```typescript
{"entry":["src/index.ts","scripts/*.ts","!scripts/except-this-one.ts"]}
```

Also seeconfigurationandentry files.

### project

Array of glob patterns to find project files. Example:

```typescript
{"project":["src/**/*.ts","scripts/**/*.ts"]}
```

Also seeconfigurationandentry files.

### paths

Tools like TypeScript, webpack and Babel support import aliases in various ways.
Knip automatically includescompilerOptions.pathsfrom the TypeScript
configuration, but does not automatically use other types of import aliases.
They can be configured manually:

```typescript
{"paths":{"@lib":["./lib/index.ts"],"@lib/*":["./lib/*"]}}
```

Each workspace can have its ownpathsconfigured. Knippathsfollow the
TypeScript semantics:

- Path values are an array of relative paths.
- Paths without an*are exact matches.

## Workspaces

Individual workspace configurations may contain all other options listed on this
page, except for the following root-only options:

- exclude/include
- ignoreExportsUsedInFile
- ignoreWorkspaces
- workspaces

Workspaces can’t be nested in a Knip configuration, but they can be nested in a
monorepo folder structure.

Also seeMonorepos and workspaces.

## Plugins

There are a few options to modify the behavior of a plugin:

- Override a plugin’sconfigorentrylocation
- Force-enable a plugin by setting its value totrue
- Disable a plugin by setting its value tofalse

```typescript
{"mocha":{"config":"config/mocha.config.js","entry":["**/*.spec.js"]},"playwright":true,"webpack":false}
```

It should be rarely necessary to override theentrypatterns, since plugins
also read custom entry file patterns from the tooling configuration (seePlugins → entry files).

Plugin configuration can be set on root and on a per-workspace level. If enabled
on root level, it can be disabled on workspace level by setting it tofalsethere, and vice versa.

Also seePlugins.

## Rules & Filters

### rules

SeeRules & Filters.

### include

SeeRules & Filters.

### exclude

SeeRules & Filters.

### tags

Exports can be tagged with known or arbitrary JSDoc/TSDoc tags:

```typescript
/*** Description of my exported value**@typenumber*@internalImportant matters*@lintignore*/exportconstmyExport=1;
```

And then include (+) or exclude (-) these tagged exports from the report
like so:

```typescript
{"tags":["-lintignore"]}
```

This way, you can either focus on or ignore specific tagged exports with tags
you define yourself. This also works for individual class or enum members.

The default directive is+(include) and the@prefix is ignored, so the
notation below is valid and will report only exports tagged@lintignoreor@internal:

```typescript
{"tags":["@lintignore","@internal"]}
```

Also seeJSDoc & TSDoc Tags.

### treatConfigHintsAsErrors

Exit with non-zero code (1) if there are any configuration hints.

```typescript
{"treatConfigHintsAsErrors":true}
```

## Ignore Issues

### ignore

Please readconfiguring project filesbefore using theignoreoption.

Avoidignorepatterns. There is almost always a better solution:

- Follow up on configuration hints (if there are any).
- Fine-tuneentryandprojectpatterns.
- Useproduction mode.
- Otherignore*options.

NOTE: An exception to the rule: totemporarilyreport only issues in files
that match the negatedignorepattern:

```typescript
{"ignore":["!src/dir/**"]}
```

### ignoreFiles

Array of glob patterns of files to exclude from the “Unused files” section only.

Unlikeignore, which suppresses all issue types for matching files,ignoreFilesonly affects thefilesissue type. Use this when a file should
remain analyzed for other issues (exports, dependencies, unresolved) but should
not be considered for unused file detection.

```typescript
{"ignoreFiles":["src/generated/**","fixtures/**"]}
```

Suffix an item with!to enable it only in production mode.

### ignoreBinaries

Exclude binaries that are used but not provided by any dependency from the
report. Value is an array of binary names or regular expressions. Example:

```typescript
{"ignoreBinaries":["zip","docker-compose","pm2-.+"]}
```

Actual regular expressions can be used in dynamic configurations:

```typescript
exportdefault{ignoreBinaries:[/^pm2-.+/],};
```

Suffix an item with!to enable it only in production mode.

### ignoreDependencies

Array of package names to exclude from the report. Regular expressions allowed.
Example:

```typescript
{"ignoreDependencies":["hidden-package","@org/.+"]}
```

Actual regular expressions can be used in dynamic configurations:

```typescript
exportdefault{ignoreDependencies:[/@org\/.*/,/^lib-.+/],};
```

Suffix an item with!to enable it only in production mode.

Also seeUnused dependencies.

### ignoreMembers

Array of class and enum members to exclude from the report. Regular expressions
allowed. Example:

```typescript
{"ignoreMembers":["render","on.+"]}
```

Actual regular expressions can be used in dynamic configurations.

### ignoreUnresolved

Array of specifiers to exclude from the report. Regular expressions allowed.
Example:

```typescript
{"ignoreUnresolved":["ignore-unresolved-import","#virtual/.+"]}
```

Actual regular expressions can be used in dynamic configurations:

```typescript
exportdefault{ignoreUnresolved:[/^#/.+/],};
```

### ignoreWorkspaces

Array of workspaces to ignore, globs allowed. Example:

```typescript
{"ignoreWorkspaces":["packages/go-server","packages/flat/*","packages/deep/**"]}
```

Suffix an item with!to enable it only in production mode.

Prefix an item with!to override an earlier wildcard.

### ignoreIssues

Ignore specific issue types for specific file patterns. Keys are glob patterns
and values are arrays of issue types to ignore for matching files. This allows
ignoring specific issues (like unused exports) in generated files while still
reporting other issues in those same files.

```typescript
{"ignoreIssues":{"src/generated/**":["exports","types"],"**/*.generated.ts":["exports","classMembers"]}}
```

## Exports

### ignoreExportsUsedInFile

In files with multiple exports, some of them might be used only internally. If
these exports should not be reported, there is aignoreExportsUsedInFileoption available. With this option enabled, when something is also no longer
used internally, it will be reported as unused.

```typescript
{"ignoreExportsUsedInFile":true}
```

In a more fine-grained manner, to ignore only specific issue types:

```typescript
{"ignoreExportsUsedInFile":{"interface":true,"type":true}}
```

### includeEntryExports

By default, Knip does not report unused exports in entry files. When a
repository (or workspace) is self-contained or private, you may want to include
entry files when reporting unused exports:

```typescript
{"includeEntryExports":true}
```

If enabled, Knip will report unused exports in entry source files. But not in
entry and configuration files as configured by plugins, such asnext.config.jsorsrc/routes/+page.svelte.

This will also enable reporting unused members of exported classes and enums.

Set this option at root level to enable this globally, or within workspace
configurations individually.

## Compilers

Knip supports custom compilers to transform files before analysis.

Since compilers are functions, they can only be used in dynamic configuration
files (.jsor.ts), not in JSON configuration files.

### compilers

Override built-in compilers or add custom compilers for additional file types.

Also seeCompilers.

ISC License© 2024Lars Kappert

