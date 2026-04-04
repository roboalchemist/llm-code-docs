# Source: https://docs.pyinvoke.org/

Title: Welcome to Invoke’s documentation! — Invoke documentation

URL Source: https://docs.pyinvoke.org/

Published Time: Sat, 11 Oct 2025 00:42:26 GMT

Markdown Content:
This site covers Invoke’s conceptual & API documentation. For basic info on what Invoke is, including its public changelog & how the project is maintained, please see [the main project website](https://pyinvoke.org/).

Getting started[¶](https://docs.pyinvoke.org/#getting-started "Permalink to this headline")
-------------------------------------------------------------------------------------------

Many core ideas & API calls are explained in the tutorial/getting-started document:

*   [Getting started](https://docs.pyinvoke.org/en/stable/getting-started.html)
    *   [Defining and running task functions](https://docs.pyinvoke.org/en/stable/getting-started.html#defining-and-running-task-functions)
    *   [Task parameters](https://docs.pyinvoke.org/en/stable/getting-started.html#task-parameters)
    *   [Listing tasks](https://docs.pyinvoke.org/en/stable/getting-started.html#listing-tasks)
    *   [Running shell commands](https://docs.pyinvoke.org/en/stable/getting-started.html#running-shell-commands)
    *   [Declaring pre-tasks](https://docs.pyinvoke.org/en/stable/getting-started.html#declaring-pre-tasks)
    *   [Creating namespaces](https://docs.pyinvoke.org/en/stable/getting-started.html#creating-namespaces)

The `invoke` CLI tool[¶](https://docs.pyinvoke.org/#the-invoke-cli-tool "Permalink to this headline")
-----------------------------------------------------------------------------------------------------

Details on the CLI interface to Invoke, available core flags, and tab completion options.

*   [`inv[oke]` core usage](https://docs.pyinvoke.org/en/stable/invoke.html)
    *   [Core options and flags](https://docs.pyinvoke.org/en/stable/invoke.html#core-options-and-flags)
    *   [Shell tab completion](https://docs.pyinvoke.org/en/stable/invoke.html#shell-tab-completion)
        *   [Generating a completion script](https://docs.pyinvoke.org/en/stable/invoke.html#generating-a-completion-script)
        *   [Sourcing the script](https://docs.pyinvoke.org/en/stable/invoke.html#sourcing-the-script)
        *   [Utilizing tab completion itself](https://docs.pyinvoke.org/en/stable/invoke.html#utilizing-tab-completion-itself)

Concepts[¶](https://docs.pyinvoke.org/#concepts "Permalink to this headline")
-----------------------------------------------------------------------------

Dig deeper into specific topics:

*   [Configuration](https://docs.pyinvoke.org/en/stable/concepts/configuration.html)
    *   [Introduction](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#introduction)
    *   [The configuration hierarchy](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#the-configuration-hierarchy)
    *   [Default configuration values](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#default-configuration-values)
    *   [Configuration files](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#configuration-files)
    *   [Environment variables](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#environment-variables)
    *   [`Collection`-based configuration](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#collection-based-configuration)
    *   [Example of real-world config use](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#example-of-real-world-config-use)

*   [Invoking tasks](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html)
    *   [Basic command line layout](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html#basic-command-line-layout)
    *   [Task command-line arguments](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html#task-command-line-arguments)
    *   [How tasks run](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html#how-tasks-run)

*   [Using Invoke as a library](https://docs.pyinvoke.org/en/stable/concepts/library.html)
    *   [Reusing Invoke’s CLI module as a distinct binary](https://docs.pyinvoke.org/en/stable/concepts/library.html#reusing-invoke-s-cli-module-as-a-distinct-binary)
    *   [Customizing the configuration system’s defaults](https://docs.pyinvoke.org/en/stable/concepts/library.html#customizing-the-configuration-system-s-defaults)

*   [Loading collections](https://docs.pyinvoke.org/en/stable/concepts/loading.html)
    *   [Task module discovery](https://docs.pyinvoke.org/en/stable/concepts/loading.html#task-module-discovery)
    *   [Configuring the loading process](https://docs.pyinvoke.org/en/stable/concepts/loading.html#configuring-the-loading-process)

*   [Constructing namespaces](https://docs.pyinvoke.org/en/stable/concepts/namespaces.html)
    *   [Starting out](https://docs.pyinvoke.org/en/stable/concepts/namespaces.html#starting-out)
    *   [Naming your tasks](https://docs.pyinvoke.org/en/stable/concepts/namespaces.html#naming-your-tasks)
    *   [Nesting collections](https://docs.pyinvoke.org/en/stable/concepts/namespaces.html#nesting-collections)
    *   [Importing modules as collections](https://docs.pyinvoke.org/en/stable/concepts/namespaces.html#importing-modules-as-collections)
    *   [Default tasks](https://docs.pyinvoke.org/en/stable/concepts/namespaces.html#default-tasks)
    *   [Mix and match](https://docs.pyinvoke.org/en/stable/concepts/namespaces.html#mix-and-match)
    *   [More shortcuts](https://docs.pyinvoke.org/en/stable/concepts/namespaces.html#more-shortcuts)

*   [Testing Invoke-using codebases](https://docs.pyinvoke.org/en/stable/concepts/testing.html)
    *   [Subclass & modify Invoke ‘internals’](https://docs.pyinvoke.org/en/stable/concepts/testing.html#subclass-modify-invoke-internals)
    *   [Use `MockContext`](https://docs.pyinvoke.org/en/stable/concepts/testing.html#use-mockcontext)
    *   [Expect `Results`](https://docs.pyinvoke.org/en/stable/concepts/testing.html#expect-results)
    *   [Avoid mocking dependency code paths altogether](https://docs.pyinvoke.org/en/stable/concepts/testing.html#avoid-mocking-dependency-code-paths-altogether)

*   [Automatically responding to program output](https://docs.pyinvoke.org/en/stable/concepts/watchers.html)
    *   [Background](https://docs.pyinvoke.org/en/stable/concepts/watchers.html#background)
    *   [Basic use](https://docs.pyinvoke.org/en/stable/concepts/watchers.html#basic-use)

API[¶](https://docs.pyinvoke.org/#api "Permalink to this headline")
-------------------------------------------------------------------

Know what you’re looking for & just need API details? View our auto-generated API documentation:

*   [`__init__`](https://docs.pyinvoke.org/en/stable/api/__init__.html)
*   [`collection`](https://docs.pyinvoke.org/en/stable/api/collection.html)
*   [`config`](https://docs.pyinvoke.org/en/stable/api/config.html)
*   [`context`](https://docs.pyinvoke.org/en/stable/api/context.html)
*   [`exceptions`](https://docs.pyinvoke.org/en/stable/api/exceptions.html)
*   [`executor`](https://docs.pyinvoke.org/en/stable/api/executor.html)
*   [`loader`](https://docs.pyinvoke.org/en/stable/api/loader.html)
*   [`parser`](https://docs.pyinvoke.org/en/stable/api/parser.html)
*   [`program`](https://docs.pyinvoke.org/en/stable/api/program.html)
*   [`runners`](https://docs.pyinvoke.org/en/stable/api/runners.html)
*   [`tasks`](https://docs.pyinvoke.org/en/stable/api/tasks.html)
*   [`terminals`](https://docs.pyinvoke.org/en/stable/api/terminals.html)
*   [`util`](https://docs.pyinvoke.org/en/stable/api/util.html)
*   [`watchers`](https://docs.pyinvoke.org/en/stable/api/watchers.html)
