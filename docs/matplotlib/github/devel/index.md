# Contribute {#developers-guide-index}

::: ifconfig
releaselevel != \'dev\'

::: important
::: title
Important
:::

If you plan to contribute to Matplotlib, please read the [development
version](https://matplotlib.org/devdocs/devel/index.html) of this
document as it will have the most up to date installation instructions,
workflow process, and contributing guidelines.
:::
:::

`heart;1em;sd-text-info`{.interpreted-text role="octicon"} Thank you for
your interest in helping to improve Matplotlib!
`heart;1em;sd-text-info`{.interpreted-text role="octicon"}

This project is a community effort, and everyone is welcome to
contribute. Everyone within the community is expected to abide by our
`code of conduct <code_of_conduct>`{.interpreted-text role="ref"}.

There are various ways to contribute, such as optimizing and refactoring
code, detailing unclear documentation and writing new examples, helping
the community, reporting and fixing bugs, requesting and implementing
new features\...

## GitHub issue tracker[]{#submitting-a-bug-report} {#request-a-new-feature}

The [issue tracker](https://github.com/matplotlib/matplotlib/issues)
serves as the centralized location for making feature requests,
reporting bugs, identifying major projects to work on, and discussing
priorities.

We have preloaded the issue creation page with markdown forms requesting
the information we need to triage issues and we welcome you to add any
additional information or context that may be necessary for resolving
the issue:

::: grid
1 1 2 2

::: {.grid-item-card class-header="sd-fs-5"}
### `bug;1em;sd-text-info`{.interpreted-text role="octicon"} **Submit a bug report**

Thank you for your help in keeping bug reports targeted and descriptive.

::: {.button-link expand="" color="primary"}
<https://github.com/matplotlib/matplotlib/issues/new/choose>

Report a bug
:::
:::

::: {.grid-item-card class-header="sd-fs-5"}
### `light-bulb;1em;sd-text-info`{.interpreted-text role="octicon"} **Request a new feature**

Thank you for your help in keeping feature requests well defined and
tightly scoped.

::: {.button-link expand="" color="primary"}
<https://github.com/matplotlib/matplotlib/issues/new/choose>

Request a feature
:::
:::
:::

Since Matplotlib is an open source project with limited resources, we
encourage users to also
`participate <contribute_code>`{.interpreted-text role="ref"} in fixing
bugs and implementing new features.

## Contributing guide

We welcome you to get more involved with the Matplotlib project! If you
are new to contributing, we recommend that you first read our
`contributing guide<contributing>`{.interpreted-text role="ref"}:

::: {.toctree hidden=""}
contribute
:::

::: {.grid class-row="sd-fs-5 sd-align-minor-center"}
1 1 2 2

::: grid-item
::: {.grid gutter="1"}
1

::: {.grid-item-card link="contribute_code" link-type="ref" class-card="sd-shadow-none" class-body="sd-text-{primary}"}
`code;1em;sd-text-info`{.interpreted-text role="octicon"} Contribute
code
:::

::: {.grid-item-card link="contribute_documentation" link-type="ref" class-card="sd-shadow-none" class-body="sd-text-{primary}"}
`note;1em;sd-text-info`{.interpreted-text role="octicon"} Write
documentation
:::

::: {.grid-item-card link="contribute_triage" link-type="ref" class-card="sd-shadow-none" class-body="sd-text-{primary}"}
`issue-opened;1em;sd-text-info`{.interpreted-text role="octicon"} Triage
issues
:::

::: {.grid-item-card link="other_ways_to_contribute" link-type="ref" class-card="sd-shadow-none" class-body="sd-text-{primary}"}
`globe;1em;sd-text-info`{.interpreted-text role="octicon"} Build
community
:::
:::
:::

::: grid-item
::: {.grid gutter="1"}
1

::: grid-item
`info;1em;sd-text-info`{.interpreted-text role="octicon"}
`Is this my first contribution? <new_contributors>`{.interpreted-text
role="ref"}
:::

::: grid-item
`question;1em;sd-text-info`{.interpreted-text role="octicon"}
`Where do I ask questions? <get_connected>`{.interpreted-text
role="ref"}
:::

::: grid-item
`git-pull-request;1em;sd-text-info`{.interpreted-text role="octicon"}
`How do I choose an issue? <managing_issues_prs>`{.interpreted-text
role="ref"}
:::

::: grid-item
`codespaces;1em;sd-text-info`{.interpreted-text role="octicon"}
`How do I start a pull request? <how-to-pull-request>`{.interpreted-text
role="ref"}
:::
:::
:::
:::

## Development workflow {#development_environment}

If you are contributing code or documentation, please follow our guide
for setting up and managing a development environment and workflow:

::: grid
1 1 2 2

::: {.grid-item-card shadow="none"}
**Install** \^\^\^ .. rst-class:: section-toc .. toctree:: :maxdepth: 4

> development_setup
:::

::: {.grid-item-card shadow="none"}
**Workflow** \^\^\^\^

::: {.toctree maxdepth="2"}
development_workflow
:::

::: {.toctree maxdepth="1"}
troubleshooting.rst
:::
:::
:::

## Policies and guidelines {#contribution_guideline}

::: admonition
AI Usage

AI may be used responsibly as a supportive tool, but we expect authentic
contributions. For guidance, see our
`AI policy <generative_ai>`{.interpreted-text role="ref"}.
:::

These policies and guidelines help us maintain consistency in the
various types of maintenance work. If you are writing code or
documentation, following these policies helps maintainers more easily
review your work. If you are helping triage, community manage, or
release manage, these guidelines describe how our current process works.

::: {.grid class-row="sf-fs-1" gutter="2"}
1 1 2 2

::: {.grid-item-card shadow="none"}
**Code** \^\^\^

::: {.toctree maxdepth="1"}
coding_guide api_changes testing
:::
:::

::: {.grid-item-card shadow="none"}
**Documentation** \^\^\^

::: {.toctree maxdepth="1"}
document style_guide tag_guidelines
:::
:::

::: {.grid-item-card shadow="none"}
**Triage And Review** \^\^\^

::: {.toctree maxdepth="1"}
triage pr_guide
:::
:::

::: {.grid-item-card shadow="none"}
**Maintenance** \^\^\^

::: {.toctree maxdepth="1"}
release_guide communication_guide min_dep_policy MEP/index
:::
:::
:::
