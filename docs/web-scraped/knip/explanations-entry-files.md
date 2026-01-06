# Entry Files

Source: https://knip.dev/explanations/entry-files

Entry files are the starting point for Knip to determine what files are used in
the codebase. More entry files lead to increased coverage of the codebase. This
also leads to more dependencies to be discovered. This page explains how Knip
and its plugins try to find entry files so you don’t need to configure them
yourself.

## Default entry file patterns

For brevity, thedefault configurationon the previous page mentions onlyindex.jsandindex.ts, but the default set of file names and extensions is
actually a bit larger:

- index,mainandcli
- js,mjs,cjs,jsx,ts,mts,ctsandtsx

This means files likemain.cjsandsrc/cli.tsare automatically added as
entry files. Here’s the default configuration in full:

```typescript
{"entry":["{index,cli,main}.{js,cjs,mjs,jsx,ts,cts,mts,tsx}","src/{index,cli,main}.{js,cjs,mjs,jsx,ts,cts,mts,tsx}"],"project":["**/*.{js,cjs,mjs,jsx,ts,cts,mts,tsx}!"]}
```

Next to the default locations, Knip looks forentryfiles in other places. In
a monorepo, this is done for each workspace separately.

The values you set override the default values, they are not merged.

Also seeFAQ: Where does Knip look for entry files?

## Plugins

Plugins often add entry files. For instance, if the Remix, Storybook and Vitest
plugins are enabled in your project, they’ll add additional entry files. Seethe next page about pluginsfor more details about this.

## Scripts in package.json

Thepackage.jsonis scanned for entry files. Themain,bin, andexportsfields may contain entry files. Thescriptsare also parsed to find entry
files and dependencies. SeeScript Parserfor more details.

## Ignored files

Knip respects.gitignorefiles. By default, ignored files are not added as
entry files. This behavior can be disabled by using the--no-gitignoreflag on the CLI.

## Configuring project files

Seeconfiguring project filesfor guidance on tuningentryandprojectand when to useignore.

ISC License© 2024Lars Kappert

