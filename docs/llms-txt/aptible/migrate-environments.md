# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/migrate-environments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to migrate environments

> Learn how to migrate environments

## Migrating to a stack in the same region

It is possible to migrate environments from one [Stack](/core-concepts/architecture/stacks) to another so long as both stacks are in the same [Region](/core-concepts/architecture/stacks#supported-regions). The most common use case for this is migrating resources from a shared stack to a dedicated stack.

If you would like to migrate environments between stacks in the same region, please contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) with details on the environment name and the stacks to and from which you want the environment migrated.

## Migrating to a stack in a different region

It is not possible to migrate environments from a stack in a different region, for example from a us-west-1  stack to a stack in us-west-2 . To achieve this, you must redeploy your resources to a new environment.
