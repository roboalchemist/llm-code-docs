# Integrated Monorepos

Source: https://knip.dev/features/integrated-monorepos

Some repositories have a singlepackage.json, but consist of multiple projects
with configuration files across the repository. A good example is theNx
integrated monorepo style.

An integrated monorepo is a single workspace.

## Entry Files

The default entrypoints files might not be enough. Here’s an idea that might fit
this type of monorepo:

```typescript
{"entry":["{apps,libs}/**/src/index.{ts,tsx}"],"project":["{apps,libs}/**/src/**/*.{ts,tsx}"]}
```

## Plugins

Let’s assume some of these projects are applications (“apps”) which have their
own ESLint configuration files and Cypress configuration and test files. This
may result in those files getting reported as unused, and consequently also the
dependencies they import and refer to.

In that case, we could configure the ESLint and Cypress plugins like this:

```typescript
{"eslint":{"config":["{apps,libs}/**/.eslintrc.json"]},"cypress":{"entry":["apps/**/cypress.config.ts","apps/**/cypress/e2e/*.spec.ts"]}}
```

Adapt the file patterns to your project, and the relevantconfigandentryfiles and dependencies should no longer be reported as unused.

## Internal Workspace Dependencies

A note about repositories with multiplepackage.jsonfiles andinternalworkspace packages: it is recommended to list all dependencies in each consumingpackage.json, allowing Knip to do fine-grained reporting of both unused and
unlisted dependencies.

An alternative is toignoreDependencies: ["@internal/*"].

ISC License© 2024Lars Kappert

