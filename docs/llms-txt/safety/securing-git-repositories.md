# Source: https://docs.safetycli.com/safety-docs/installation/securing-git-repositories.md

# Securing Git Repositories

## Securing your git source control management system

The best place to start with scanning your Python codebases for dependency vulnerabilities is in a central place for your team, like your build pipeline or your central source control management system. This allows quick setup and will allow you to know what dependencies are in your systems, and secure them before they get to your production systems, without having to set up each developer's environment.

## A quick intro to transitive dependencies

It's important to scan all the Python dependencies present in your systems, and not just the ones listed in your requirements files (these are called transitive, recursive, and run-time dependencies).

## Scanning *all* of your dependencies in your SCM systems

Luckily, scanning your Python environments is really easy to do using our Safety command-line tool. Its default configuration is to scan the local environment where it is running. See our guides below to integrate Safety CLI into your SCM system:
