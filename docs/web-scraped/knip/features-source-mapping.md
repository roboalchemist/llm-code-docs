# Source Mapping

Source: https://knip.dev/features/source-mapping

Knip is mostly interested in source code. Analyzing build artifacts hurts
performance and often leads to false positives, as they potentially contain
bundled code and unresolvable imports.

That’s why Knip tries to map such build artifacts back to their original source
files and analyze those instead. This is done based ontsconfig.jsonsettings.

## Example 1: package.json

Let’s look at an example case withpackage.jsonandtsconfig.jsonfiles, and
see how “dist” files are mapped to “src” files.

```typescript
{"name":"my-workspace","main":"index.js","exports":{".":"./src/entry.js","./feat":"./lib/feat.js","./public":"./dist/app.js","./public/*":"./dist/*.js","./public/*.js":"./dist/*.js","./dist/internal/*":null,},}
```

With this TypeScript configuration:

```typescript
{"compilerOptions":{"baseUrl":"src","outDir":"dist"}}
```

- ./src/entry.jsis not in anoutDirfolder, so it’s added as an entry file
- ./lib/feat.jsis not in anoutDirfolder, so it’s added as an entry file
- ./dist/app.jsis in adistfolder and mapped to./src/app.{js,ts}(¹)
- ./dist/*.jsis in adistfolder and mapped to./src/**/*.{js,ts}(¹)
- ./dist/internal/*is translated to./dist/internal/**and files in this
directory and deeper are ignored when globbing entry files

(¹) full extensions list is actually:js,mjs,cjs,jsx,ts,tsx,mts,cts

In--debugmode, look for “Source mapping” to see this in action.

Using./dist/*.jsmeans that all files matching./src/**/*.{js,ts}are added
as entry files. By default, unused exports of entry files are not reported. UseincludeEntryExportsto include them.

## Example 2: monorepo

Let’s say we have this module in a monorepo that importshelperfrom another
workspace in the same monorepo:

```typescript
import{ helper }from'@org/shared';
```

The target workspace@org/sharedhas thispackage.json:

```typescript
{"name":"@org/shared","main":"dist/index.js"}
```

The module resolver will resolve@org/sharedtodist/index.js. That file is
usually compiled and git-ignored, while Knip wants the source file instead.

You may need to compile build artifacts tooutDirfirst before Knip can
successfully apply source mapping for internal references in a monorepo.

If the target workspace has atsconfig.jsonfile with anoutDiroption, Knip
will try to map the “dist” file to the “src” file. Then ifsrc/index.tsexists, Knip will use that file instead ofdist/index.js.

Currently this only works based ontsconfig.json, in the future more source
mappings may be added.

ISC License© 2024Lars Kappert

