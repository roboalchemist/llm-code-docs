# Rules & Filters

Source: https://knip.dev/features/rules-and-filters

Use rules or filters to customize Knip’s output. This has various use cases, a
few examples:

- Temporarily focus on a specific issue type.
- You don’t want to see unusedtype,interfaceandenumexports reported.
- Specific issue types should be printed, but not counted against the total
error count.

If you’re looking to handle one-off exceptions, also seeJSDoc tags.

## Filters

You can--includeor--excludeany of the reported issue types to slice &
dice the report to your needs. Alternatively, they can be added to the
configuration (e.g."exclude": ["dependencies"]).

Use--includeto report only specific issue types. The following example
commands do the same:

```typescript
knip--includefiles--includedependenciesknip--includefiles,dependencies
```

Or the other way around, use--excludeto ignore the types you’re not
interested in:

```typescript
knip--includefiles--excludeenumMembers,duplicates
```

Also see thelist of issue types.

### Shorthands

Knip has shortcuts to include only specific issue types.

- The--dependenciesflag includes:dependencies(anddevDependencies+optionalPeerDependencies)unlistedbinariesunresolvedcatalog
- The--exportsflag includes:exportstypesenumMembersduplicates
- The--filesflag is a shortcut for--include files

The--dependenciesflag includes:

- dependencies(anddevDependencies+optionalPeerDependencies)
- unlisted
- binaries
- unresolved
- catalog

The--exportsflag includes:

- exports
- types
- enumMembers
- duplicates

The--filesflag is a shortcut for--include files

## Rules

Userulesin the configuration to customize the issue types that count towards
the total error count, or to exclude them altogether.

```typescript
{"rules":{"files":"warn","classMembers":"off","duplicates":"off"}}
```

Also see theissue types overview.

NOTE: If thedependenciesissue type is included, thedevDependenciesandoptionalPeerDependenciestypes can still be set to"warn"separately.

The rules are modeled after the ESLintrulesconfiguration, and could be
extended in the future.

## Rules or filters?

Filters are meant to be used as command-line flags, rules allow for more
fine-grained configuration.

- Rules are more fine-grained since they also have “warn”.
- Rules could be extended in the future.
- Filters can be set in configuration and from CLI (rules only in
configuration).
- Filters have shorthands (rules don’t have this).

ISC License© 2024Lars Kappert

