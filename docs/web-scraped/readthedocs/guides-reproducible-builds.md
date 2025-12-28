# Source: https://docs.readthedocs.com/platform/latest/guides/reproducible-builds.html

# How to create reproducible builds[](#how-to-create-reproducible-builds "Link to this heading")

Your documentation depends on a number of dependencies to be built. If your docs don't have [[reproducible]](../glossary.html#term-reproducible) builds, an update in a dependency can break your builds when least expected, or make your docs look different from your local version. This guide will help you to keep your builds working over time, so that you can focus on content.

Contents

-   [Define OS and tool versions in the config file](#define-os-and-tool-versions-in-the-config-file)

-   [Use a requirements file for Python dependencies](#use-a-requirements-file-for-python-dependencies)

-   [Pin your transitive dependencies](#pin-your-transitive-dependencies)

Note

This page explains how to pin the versions that correctly build your project. The versions used in this page are just for illustrative purpose. They are not the latest nor the recommended versions. It is up to you to find those versions.

## [Define OS and tool versions in the config file](#id6)[](#define-os-and-tool-versions-in-the-config-file "Link to this heading")

We recommend defining the explicit version of the OS and tool versions used to build your documentation using the [`.readthedocs.yaml`]. This file *provides you per version settings*, and *those settings live in your Git repository*.

This allows you to validate changes using [[pull requests]](../pull-requests.html), and ensures that all your versions can be rebuilt from a reproducible configuration.

[.readthedocs.yaml][](#id1 "Link to this code")

    version: 2

    # Explicitly set the OS and Python versions
    build:
      os: "ubuntu-24.04"
      tools:
        nodejs: "20"
        python: "3.12"