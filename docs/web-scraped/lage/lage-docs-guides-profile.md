# Source: https://microsoft.github.io/lage/docs/guides/profile

Title: Profiling | Lage

URL Source: https://microsoft.github.io/lage/docs/guides/profile

Markdown Content:
Profiling | Lage
===============

[Skip to main content](https://microsoft.github.io/lage/docs/guides/profile#__docusaurus_skipToContent_fallback)

[![Image 1: Lage Logo](https://microsoft.github.io/lage/img/lage.png)](https://microsoft.github.io/lage/)[Guide](https://microsoft.github.io/lage/docs/introduction)

[GitHub](https://github.com/microsoft/lage)

Search...

*   [Introduction](https://microsoft.github.io/lage/docs/introduction)
*   [Quick Start](https://microsoft.github.io/lage/docs/quick-start)
*   [Guides](https://microsoft.github.io/lage/docs/guides/) 
    *   [Installation](https://microsoft.github.io/lage/docs/guides/installation)
    *   [Pipelines](https://microsoft.github.io/lage/docs/guides/pipeline)
    *   [Scoping by packages](https://microsoft.github.io/lage/docs/guides/scopes)
    *   [Local caching](https://microsoft.github.io/lage/docs/guides/cache)
    *   [Remote cache](https://microsoft.github.io/lage/docs/guides/remote-cache)
    *   [Profiling](https://microsoft.github.io/lage/docs/guides/profile)
    *   [Priorities](https://microsoft.github.io/lage/docs/guides/priority)
    *   [Distributed Builds](https://microsoft.github.io/lage/docs/guides/buildxl)

*   [Reference](https://microsoft.github.io/lage/docs/guides/profile#) 
*   [Cookbook](https://microsoft.github.io/lage/docs/guides/profile#) 
*   [Contributing](https://microsoft.github.io/lage/docs/contributing)

*   [](https://microsoft.github.io/lage/)
*   [Guides](https://microsoft.github.io/lage/docs/guides/)
*   Profiling

On this page

Profiling
=========

A particularly complex monorepo can present opportunities for optimization. For example, when there are really large packages, it might be more efficient to break those up so the build can be split across different CPU cores. `lage` greatly enhances the ability for developers to see where the bottlenecks are.

To collect a profile of the `lage` run, simply add the `--profile` argument.

`lage build test --profile`

Using the profile[​](https://microsoft.github.io/lage/docs/guides/profile#using-the-profile "Direct link to Using the profile")
-------------------------------------------------------------------------------------------------------------------------------

When the run is finished, a profile JSON file is produced. This file is to be imported into a Chromium-based browser's devtools Performance tab.

Sample of `lage` profile session[​](https://microsoft.github.io/lage/docs/guides/profile#sample-of-lage-profile-session "Direct link to sample-of-lage-profile-session")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For example, you can see the following `lage` run of the [Fluent UI](https://developer.microsoft.com/en-us/fluentui/#/components) repo. You can see that there is a dip in the concurrency when building the `office-ui-fabric-react` package. This makes sense, because many internal packages depends on that one large package.

[Edit this page](https://github.com/microsoft/lage/edit/master/docs/docs/guides/profile.md)

[Previous Remote cache](https://microsoft.github.io/lage/docs/guides/remote-cache)[Next Priorities](https://microsoft.github.io/lage/docs/guides/priority)

*   [Using the profile](https://microsoft.github.io/lage/docs/guides/profile#using-the-profile)
*   [Sample of `lage` profile session](https://microsoft.github.io/lage/docs/guides/profile#sample-of-lage-profile-session)
