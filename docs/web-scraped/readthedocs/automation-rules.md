# Source: https://docs.readthedocs.com/platform/latest/automation-rules.html

# Automation rules[](#automation-rules "Link to this heading")

Automation rules allow project maintainers to automate actions on new branches and tags in Git repositories. If you are familiar with [[GitOps]](glossary.html#term-GitOps), this might seem familiar. The goal of automation rules is to be able to control versioning through your Git repository and avoid duplicating these efforts on Read the Docs.

See also

[[How to manage versions automatically]](guides/automation-rules.html)

:   A practical guide to managing automated versioning of your documentation.

[[Versions]](versions.html)

:   General explanation of how versioning works on Read the Docs

## How automation rules work[](#how-automation-rules-work "Link to this heading")

When a new tag or branch is pushed to your repository, Read the Docs receives a webhook. We then create a new Read the Docs *version* that matches your new Git *tag or branch*.

All automation rules are evaluated for this version, in the order they are listed. If the version **matches** the version type and the pattern in the rule, the specified **action** is performed on that version.

Note

Versions can match multiple automation rules, and all matching actions will be performed on the version.