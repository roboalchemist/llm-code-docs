# Configuring Project Files

Source: https://knip.dev/guides/configuring-project-files

Theentryandprojectfile patterns are the first and most important
options. Getting those right is essential to help you delete more code and make
Knip faster:

- Start with defaults. Only add targetedentryoverrides when needed.
- Useprojectpatterns (with negations) to define the scope for Knip.
- Use production mode to exclude tests and other non-production files.
- Useignoreonly to suppress issues in specific files; it does not exclude
files from analysis.

Let’s dive in and expand on all of these.

## Entry files

Avoid adding too many files asentryfiles:

- Knip does not reportunused exportsin entry files by default.
- Properentryandprojectpatterns allow Knip to find unused files and
exports.

## Unused files

Files are reported as unused if they are in the set ofprojectfiles, but are
not resolved from theentryfiles:

```typescript
unused files = project files - (entry files + resolved files)
```

Seeentry filesto see where Knip looks for entry files. Fine-tuneentryand adjustprojectto fit your codebase.

Use negatedprojectpatterns to precisely include/exclude files for unused
files detection.

Useignore*to suppress specific issues in matching files; it does not exclude
files from analysis.

## Negated patterns

When there are too many files in the analysis, start here.

For instance, routes are entry files except those prefixed with an underscore:

```typescript
{"entry":["src/routes/*.ts","!src/routes/_*.ts"]}
```

Some files are not part of your source and are reported as unused (false
positives)? Use negatedprojectpatterns:

```typescript
{"entry":["src/index.ts"],"project":["src/**/*.ts","!src/exclude/**"]}
```

❌   Don’t useignorefor generated artifacts:

```typescript
{"entry":["src/index.ts","scripts/*.ts"],"ignore":["build/**","dist/**","src/generated.ts"]}
```

✅   Do define your project boundaries:

```typescript
{"entry":["src/index.ts","scripts/*.ts"],"project":["src/**","scripts/**"],"ignore":["src/generated.ts"]}
```

Why this is better:

- projectdefines what belongs to the codebase, so build outputs are excluded
from analysis and unused file detection
- ignoreis for the few files that should be analyzed but contain exceptions
- Improves performance by analyzing fewer files

## Ignore issues in specific files

Useignorewhen a specific analyzed file is not handled properly by Knip or
intentionally contains unused exports (e.g. generated files exporting
“everything”):

```typescript
{"entry":["src/index.ts"],"project":["src/**/*.ts"],"ignore":["src/generated.ts"]}
```

Also seeignoreExportsUsedInFilefor a more targeted approach.

## Production Mode

Default mode includes tests and other non-production files in the analysis. To
focus on production code, useproduction mode.

Don’t try to exclude tests viaignoreor negatedprojectpatterns. That’s
inefficient and ineffective due to entries added by plugins. Use production mode
instead.

❌   Don’t do this:

```typescript
{"ignore":["**/*.test.js"]}
```

Why not:ignorehides issues from the report; it does not exclude files from
analysis.

❌   Also don’t do this:

```typescript
{"entry":["index.ts","!**/*.test.js"]}
```

Why not: plugins add test files asentryfiles; you can’t and shouldn’t
override that globally.

❌   Or this:

```typescript
{"project":["**/*.ts","!**/*.spec.ts"]}
```

Why not:projectis for unused file detection; negating test files is
ineffective because they areentryfiles.

✅   Do this instead:

```typescript
knip--production
```

To fine-tune the resulting production file set, for instance to exclude test
helper files that still show as unused, use the exclamation mark suffix on
production patterns:

```typescript
{"entry":["src/index.ts!"],"project":["src/**/*.ts!","!src/test-helpers/**!"]}
```

Remember to keep adding the exclamation marksuffix!for production file
patterns.

Use the exclamation mark (!) on both ends (!) to exclude files in production
mode.

## Defaults & Plugins

To reiterate, the defaultentryandprojectfiles for each workspace:

```typescript
{"entry":["{index,cli,main}.{js,cjs,mjs,jsx,ts,cts,mts,tsx}","src/{index,cli,main}.{js,cjs,mjs,jsx,ts,cts,mts,tsx}"],"project":["**/*.{js,cjs,mjs,jsx,ts,cts,mts,tsx}!"]}
```

Next to this, there are other places whereKnip looks for entry files.

Additionally,plugins have plenty of entry files configuredthat are
automatically added as well.

ISC License© 2024Lars Kappert

