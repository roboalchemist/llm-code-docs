# Source: https://docs.readthedocs.com/platform/latest/config-file/v2.html

# Configuration file reference[](#configuration-file-reference "Link to this heading")

Read the Docs supports configuring your documentation builds with a configuration file. This file is named [`.readthedocs.yaml`] and should be placed in the top level of your Git repository.

The [`.readthedocs.yaml`] file can contain a number of settings that are not accessible through the Read the Docs website.

Because the file is stored in Git, the configuration will apply to the exact version that is being built. **This allows you to store different configurations for different versions of your documentation.**

Below is an example YAML file which shows the most common configuration options:

Sphinx

MkDocs

[.readthedocs.yaml][](#id1 "Link to this code")

     1# Read the Docs configuration file for Sphinx projects
     2# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details
     3
     4# Required
     5version: 2
     6
     7# Set the OS, Python version and other tools you might need
     8build:
     9  os: ubuntu-24.04
    10  tools:
    11    python: "3.12"
    12    # You can also specify other tool versions:
    13    # nodejs: "20"
    14    # rust: "1.70"
    15    # golang: "1.20"
    16
    17# Build documentation in the "docs/" directory with Sphinx
    18sphinx:
    19  configuration: docs/conf.py
    20  # You can configure Sphinx to use a different builder, for instance use the dirhtml builder for simpler URLs
    21  # builder: "dirhtml"
    22  # Fail on all warnings to avoid broken references
    23  # fail_on_warning: true
    24
    25# Optionally build your docs in additional formats such as PDF and ePub
    26# formats:
    27#   - pdf
    28#   - epub
    29
    30# Optional but recommended, declare the Python requirements required
    31# to build your documentation
    32# See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
    33# python:
    34#   install:
    35#     - requirements: docs/requirements.txt

[.readthedocs.yaml][](#id2 "Link to this code")

     1# Read the Docs configuration file for MkDocs projects
     2# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details
     3
     4# Required
     5version: 2
     6
     7# Set the version of Python and other tools you might need
     8build:
     9  os: ubuntu-22.04
    10  tools:
    11    python: "3.12"
    12
    13mkdocs:
    14  configuration: mkdocs.yml
    15
    16# Optionally declare the Python requirements required to build your docs
    17python:
    18  install:
    19  - requirements: docs/requirements.txt

See also

[[Configuration file overview]](index.html)

:   Practical steps to add a configuration file to your documentation project.

## Supported settings[](#supported-settings "Link to this heading")

Read the Docs validates every configuration file. Any configuration option that isn't supported will make the build fail. This is to avoid typos and provide feedback on invalid configurations.

Warning

When using a v2 configuration file, the local settings from the web interface are ignored.

-   [version](#version)

-   [formats](#formats)

-   [python](#python)

    -   [python.install](#python-install)

        -   [Requirements file](#requirements-file)

        -   [Packages](#packages)

-   [conda](#conda)

    -   [conda.environment](#conda-environment)

-   [build](#build)

    -   [build.os](#build-os)

    -   [build.tools](#build-tools)

    -   [build.tools.python](#build-tools-python)

    -   [build.tools.nodejs](#build-tools-nodejs)

    -   [build.tools.ruby](#build-tools-ruby)

    -   [build.tools.rust](#build-tools-rust)

    -   [build.tools.golang](#build-tools-golang)

    -   [build.apt_packages](#build-apt-packages)

    -   [build.jobs](#build-jobs)

    -   [build.jobs.build](#build-jobs-build)

    -   [build.commands](#build-commands)

-   [sphinx](#sphinx)

    -   [sphinx.builder](#sphinx-builder)

    -   [sphinx.configuration](#sphinx-configuration)

    -   [sphinx.fail_on_warning](#sphinx-fail-on-warning)

-   [mkdocs](#mkdocs)

    -   [mkdocs.configuration](#mkdocs-configuration)

    -   [mkdocs.fail_on_warning](#mkdocs-fail-on-warning)

-   [submodules](#submodules)

    -   [submodules.include](#submodules-include)

    -   [submodules.exclude](#submodules-exclude)

    -   [submodules.recursive](#submodules-recursive)

-   [search](#search)

    -   [search.ranking](#search-ranking)

    -   [search.ignore](#search-ignore)

### [version](#id4)[](#version "Link to this heading")

Required[:]

:   [`true`]

Example:

    version: 2