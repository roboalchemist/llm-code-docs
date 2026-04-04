# Production Mode

Source: https://knip.dev/features/production-mode

The default mode for Knip is comprehensive and targets all project code,
including configuration files, test files, Storybook stories, and so on. Test
files usually import production files. This prevents production files or their
exports from being reported as unused, while sometimes both of them can be
deleted. Knip features a “production mode” to focus only on the code that you
ship.

## Configuration

To tell Knip what is production code, add an exclamation mark behind eachpattern!that represents production code:

```typescript
{"entry":["src/index.ts!","build/script.js"],"project":["src/**/*.ts!","build/*.js"]}
```

Depending on file structure and enabled plugins, you might not need to modify
your configuration at all.

Run Knip with the--productionflag:

```typescript
knip--production
```

Here’s what’s included in production mode:

- Onlyentryandprojectpatterns suffixed with!
- Only productionentryfile patterns exported by plugins (such as Next.js and
Remix)
- Only thestartandpostinstallscripts
- Ignore exports with the@internaltag

The production run does not replace the default run. Depending on your needs you
can run either of them or both separately. Usually both modes can share the same
configuration.

To see the difference between default and production mode in great detail, use
the--debugflag and inspect what entry and project files are used, and the
plugins that are enabled. For instance, in production mode this shows that files
such as tests and Storybook files (stories) are excluded from the analysis.

In case files like mocks and test helpers are reported as unused files, use
negated patterns to exclude those files in production mode:

```typescript
{"entry":["src/index.ts!"],"project":["src/**/*.ts!","!src/test-helpers/**!"]}
```

Also seeconfiguring project filesto alignentryandprojectwith
production mode.

## Strict Mode

In production mode, onlydependencies(notdevDependencies) are considered
when finding unused or unlisted dependencies.

Additionally, the--strictflag can be added to:

- Verify isolation: workspaces should use strictly their owndependencies
- IncludepeerDependencieswhen finding unused or unlisted dependencies
- Report type-only imports listed independencies

```typescript
knip--production--strict
```

Using--strictimplies--production, so the latter can be omitted.

## Types

Add--exclude typesif you don’t want to include types in the report:

```typescript
knip--production--excludetypes
```

ISC License© 2024Lars Kappert

