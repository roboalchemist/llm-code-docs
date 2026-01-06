# Issue Reproduction

Source: https://knip.dev/guides/issue-reproduction

If you encounter an issue or false positives when using Knip, you canopen an
issue on GitHub. This will help you in your project, and will also improve
Knip for everyone else!

Think of Knip as a kitchen sink, it handles a large amount of projects and
configurations, and your project is different from all others. Many factors may
influence the issue at hand, such as:

- Code syntax, import and export structure in source files
- Dependencies, scripts and entry files inpackage.json
- TypeScript configuration intsconfig.json
- Enabled plugins and related configuration files
- Dependent or depending workspaces in a monorepo
- Knip configuration inknip.json

Create the minimum of source code and configuration with a few files to
reproduce and demonstrate the issue. Having this as a basis has many benefits:

- Minimize barriers and unrelated contextual overhead
- Optimize shared understanding of the situation
- Serves as a “contract” to fix the actual issue
- Files serve as a fixture to the project

Providing this with an issue description will help us help you and improve the
chances the issue can be looked into efficiently and in a timely manner.

## Before opening an issue

Before opening an issue, please make sure you:

- are using the latest version
- have read the relevant documentation
- have searchedexisting issues
- have checked the list ofknown issues

Please file only a single issue at a time, so each of them can be labeled and
tracked separately.

There is no need to open an issue if you’re going to submit a pull request to
close it right away anyway. In that case it’s preferred to keep things central
in either an issue or pull request.

## Templates

A convenient way to create a minimal reproduction is by starting with one of
these templates in CodeSandbox or StackBlitz:

Shoutout toCodeSandboxandStackBlitzfor generously providing these
free dev containers!

## Alternatives

Other solutions to share a minimal and reproducible case may work well too,
including:

- A public repository on e.g. GitHub or GitLab.
- A newfixtures folder in the Knip repository.

The goal is to have an easy and common understanding and reproduction. A link to
your existing project repository will likely not be considered “minimal”. Issues
containing just a screenshot, or snippets of output or source code don’t provide
the full picture and aren’t complete nor actionable.

If you’re unable to create a reproduction using one of the methods described
then please clearly explain this in the issue orcontact me.

## Pull Request

The optimal way is to add fixtures and failing tests to the Knip repository, and
open a pull request to discuss the issue! Also seeinstructions for
development.

ISC License© 2024Lars Kappert

