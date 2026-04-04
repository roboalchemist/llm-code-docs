# Performance

Source: https://knip.dev/guides/performance

This page describes a few topics around Knip’s performance, and how you might
improve it.

Knip does not want to tell you how to structure files or how to write your code,
but it might still be good to understand inefficient patterns for Knip.

Use the--debugand--performanceflags to find potential bottlenecks.

## Cache

Use--cacheto speed up consecutive runs.

## Ignoring files

Files matching theignorepatterns are not excluded from the analysis. They’re
just not printed in the report. Use negatedentryandprojectpatterns to
exclude files from the analysis.

Readconfiguring project filesfor details and examples. Improving
configuration may have a significant impact on performance.

## Workspace sharing

Knip shares files from separate workspaces if the configuration intsconfig.jsonallows this. This aims to reduce memory consumption and run
duration. Relevant compiler options includebaseUrl,pathsandmoduleResolution.

With the--debugflag you can see how many programs Knip uses. Look for
messages like this:

```typescript
...[*] Installed 2 programsfor29workspaces...[*] Analyzing used resolved files [P1/1] (123)...[*] Analyzing used resolved files [P1/2] (8)...[*] Analyzing used resolved files [P2/1] (41)...
```

The first number inP1/1is the number of the programs, the second number
indicates additional entry files were found so it does another round of analysis
on those files.

Use—isolate-workspacesto disable this behavior. This is usually not
necessary, but more of an escape hatch in cases with memory usage issues or
incompatiblecompilerOptionsacross workspaces. Workspaces are analyzed
sequentially to spread out memory usage more evenly, which may prevent crashes
on large monorepos.

## Language Service

Knip does not install the TypeScript Language Service (LS) by default. This is
expensive, as TypeScript needs to set up symbols and caching for the rather slowfindReferencesfunction.

There are two cases that enforce Knip to install the LS.

### 1. Class members

ThefindReferencesfunction is used to find unused members of imported classes
(i.e. when the issue typeclassMembersis included).

### 2. Include external type definitions

When--include-libsis enabled, Knip enables loading type definitions of
external dependencies. This will also install the LS to access itsfindReferencesfunction. It acts as an extra line of defense: only exports
that weren’t referenced to during default procedure go through this.

## Metrics

Usethe--performanceflagto see how many times potentially expensive
functions (e.g.findReferences) are invoked and how much time is spent in
those functions. Example usage:

```typescript
knip--includeclassMembers--performance
```

## A last resort

In case Knip is unbearably slow (or even crashes), you could resort tolint
individual workspaces.

ISC License© 2024Lars Kappert

