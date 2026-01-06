# Troubleshooting

Source: https://knip.dev/guides/troubleshooting

We can distinguish two types of issues:

- Lint issues reported by Knip
- Exceptions thrown by Knip

Also see thedebugandtraceoptions below that can help to
troubleshoot issues.

The JavaScript/TypeScript ecosystem has a vast amount of frameworks and tools.
Additionally, file locations, configuration semantics, command-line arguments
and so on vary wildly. Files and dependencies are referenced in many ways. Knip
tries harder than you think to cover it all.

Knip is intentionally strict to maximize its potential. It may initially report
many unused files. However, getting this right will result in great reports and
tidy codebases.

If it doesn’t work out at first, a small change can go a long way.

## Lint issues reported by Knip

Knip reports lint issues in your codebase. Seehandling issuesto deal with
the reported issues.

If you’re considering filing an issue, please readissue reproductionfirst.

Exit code 1 indicates a successful run, but lint issues were found.

## Exceptions thrown by Knip

Knip may throw an exception, resulting in an unsuccessful run.

Seeknown issuesas it may be listed there and a workaround may be
available. If it isn’t clear what’s throwing the exception, try another run with--debugto locate the cause of the issue with more details.

If you’re considering filing an issue, please readissue reproductionfirst.

Exit code 2 indicates an exception was thrown by Knip.

## Debug

To better understand why Knip reports what it does, run it in debug mode by
adding--debugto the command:

```typescript
knip--debug
```

This will give a lengthy output, including:

- Included workspaces
- Used configuration per workspace
- Enabled plugins per workspace
- Glob patterns and options followed by matching file paths
- Plugin config file paths and found dependencies per plugin
- Compiled non-standard source files

## Trace

Use--traceto see where exports or dependencies are used:

- Use--trace-file [path]to output this only for the given file.
- Use--trace-export [name]to output this only for the given export name.
- Use--trace-dependency [name]to find where a dependency is imported
- Use both to trace a specific named or default export of a certain file.

This works across re-exports, barrel files and workspaces. Here’s an example
screenshot:

It’s like a reversed module graph. Instead of traversing imports it goes in the
opposite direction and shows where exports are imported.

The--trace-dependencyaccepts strings for exact matches, but if it looks like
a regex that works too:

Use—workspace [dir]to filter accordingly.

#### Legend

## Opening an issue

If you want to open an issue, please seeissue reproduction.

## Understanding Knip

Looking to better understand how Knip works? Theentry filesandpluginsexplanations cover two core concepts. After this you might want to
check out features likeproduction modeandmonorepos & workspaces.

In a more general sense,Why use Knip?explains what Knip can do for you.

## Asking for help

If you can’t find your answer in any of the aforementioned resources, feel free
toopen an issue on GitHub.

ISC License© 2024Lars Kappert

