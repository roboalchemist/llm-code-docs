# Source: https://docs.envzero.com/guides/integrations/plugins/opa-plugin.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Opa Plugin

> Enforce policies in env zero deployments using the Open Policy Agent (OPA) plugin

## Overview

This plugin executes the Open Policy Agent engine (aka the `opa` CLI) and lets you easily integrate policy enforcements within your env zero deployments.

The plugin will install the `opa` binary and execute its `opa eval` command

For more information, check out the [OPA Plugin git repository](https://github.com/env0/env0-opa-plugin).

## Inputs

To use the OPA plugin, you need to pass the following inputs:

1. `path` (**Required**) - the path to your bundle directory (the root folder is your project's root folder)
2. `query` (**Required**) - a query to eval with opa eval
3. `flags` - a string containing additional flags as one string

Built with [Mintlify](https://mintlify.com).
