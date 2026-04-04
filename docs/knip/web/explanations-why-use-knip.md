# Why use Knip?

Source: https://knip.dev/explanations/why-use-knip

The value of removing clutter is clear, but finding it manually is tedious. This
is where Knip comes in: comprehensive and accurate results at any scale.

Knip finds and fixes unused dependencies, exports and files.

Deep analysis fromfine-grained entry pointsbased on the actual frameworks
and tooling in(mono)reposfor accurate and actionable results. Advanced
features for maximum coverage:

- Custom module resolution
- Configuration file parsers
- Advanced shell script parser
- Built-in and custom compilers
- Auto-fix most issues

## Less is more

There are plenty of reasons to delete unused files, dependencies and “dead
code”:

- Easier maintenance: things are easier to manage when there’s less of it.
- Improved performance: startup time, build time and/or bundle size can be
negatively impacted when unused code, files and/or dependencies are included.
Relying on tree-shaking when bundling code helps, but it’s not a silver
bullet.
- Easier onboarding: there should be no doubts about whether files, dependencies
and exports are actually in use or not. Especially for people new to the
project and/or taking over responsibilities this is harder to grasp.
- Prevent regressions: tools like TypeScript, ESLint and Prettier do all sorts
of checks and linting to report violations and prevent regressions. Knip does
the same for dependencies, exports and files that are obsolete.
- Keeping dead code around has a negative value on readability, as it can be
misleading and distracting. Even if it serves no purpose it will need to be
maintained (source:Safe dead code removal → YAGNI).
- Also seeWhy are unused dependencies a problem?andWhy are unused
exports a problem?.

## Automation

Code and dependency management is usually not the most exciting task for most of
us. Knip’s mission is to automate finding clutter. This is such a tedious job if
you were to do it manually, and where would you even start? Knip applies many
techniques and heuristics to report what you need and save a lot of time.

Knip not only finds clutter, it can alsoremove clutter!

Use Knip next to a linter like ESLint or Biome: after removing unused variables
inside files, Knip might find even more unused code. Rinse and repeat!

## Comprehensive

You can use alternative tools that do the same. However, the advantage of a
strategy that addresses all of dependencies, exports and files is in their
synergy:

- Utilizing plugins to find their dependencies includes the capacity to find
additional entry and configuration files. This results in more resolved and
used files. Better coverage gives better insights into unused files and
exports.
- Analyzing more files reveals more unused exports and dependency usage,
refining the list of both unused and unlisted dependencies.
- This approach is amplified in a monorepo setting. In fact, files and internal
dependencies can recursively reference each other (across workspaces).

## Greenfield or Legacy

Installing Knip in greenfield projects ensures the project stays neat and tidy
from the start. Add it to your CI workflow and prevent any regressions from
entering the codebase.

Use Knip in a CI environment to prevent future regressions.

In large and/or legacy projects, Knip may report false positives and require
some configuration. It aims to be a great assistant when cleaning up parts of
the project or doing large refactors. Even a list of results with a few false
positives is many times better and faster than if you were to do it manually.

## Unobtrusive

Knip does not introduce new syntax for you to learn. This may sound obvious, but
consider comments like the following:

```typescript
// eslint-disable-next-line// prettier-ignore// @ts-expect-error
```

Maybe you wonder why Knip does not have similar comments like// knip-ignoreso you can get rid of false positives? A variety of reasons:

- A false positive may be a bug in Knip, and should be reported, not dismissed.
- Instead of proprietary comments, usestandardized annotationsthat also
serve as documentation.
- In the event you want to remove Knip, just uninstallknipwithout having to
remove useless comments scattered throughout the codebase.

Tip: use@lintignorein JSDoc comments, so other linters can use the same.

ISC License© 2024Lars Kappert

