# Source: https://rocket.rs/guide/master/

Title: Programming Guide - Rocket Web Framework

URL Source: https://rocket.rs/guide/master/

Markdown Content:
Programming Guide - Rocket Web Framework
===============

![Image 1: cloud](https://rocket.rs/images/cloud-0.png)![Image 2: cloud](https://rocket.rs/images/cloud-1.png)![Image 3: cloud](https://rocket.rs/images/cloud-2.png)![Image 4: cloud](https://rocket.rs/images/cloud-0.png)![Image 5: cloud](https://rocket.rs/images/cloud-0.png)![Image 6: cloud](https://rocket.rs/images/cloud-0.png)

[Rocket Homepage](https://rocket.rs/)- [x] [overview](https://rocket.rs/overview/)[guide](https://rocket.rs/guide/v0.5/)[faq](https://rocket.rs/guide/v0.5/faq/#faq)[news](https://rocket.rs/news/)[docs](https://api.rocket.rs/v0.5/rocket/)[![Image 7: GitHub octocat](https://rocket.rs/images/github-mark-white.svg)](https://github.com/rwf2/Rocket/tree/v0.5.1)

[Guide](https://rocket.rs/guide/master/)
========================================

master

[v0.5](https://rocket.rs/guide/v0.5/)[v0.4](https://rocket.rs/guide/v0.4/)[v0.3](https://rocket.rs/guide/v0.3/)

#### The ins and outs of Rocket, in detail

![Image 8: warning icon](https://rocket.rs/images/warning-icon.svg) This version is in development. [Go to current release.](https://rocket.rs/guide/v0.5/)![Image 9: warning icon](https://rocket.rs/images/warning-icon.svg)

* [Introduction](https://rocket.rs/guide/master/introduction/#introduction)
  * [Audience](https://rocket.rs/guide/master/introduction/#audience)
  * [Foreword](https://rocket.rs/guide/master/introduction/#foreword)

* [Upgrading](https://rocket.rs/guide/master/upgrading/#upgrading)
  * [Getting Help](https://rocket.rs/guide/master/upgrading/#getting-help)

* [Quickstart](https://rocket.rs/guide/master/quickstart/#quickstart)
  * [Running Examples](https://rocket.rs/guide/master/quickstart/#running-examples)

* [Getting Started](https://rocket.rs/guide/master/getting-started/#getting-started)
  * [Installing Rust](https://rocket.rs/guide/master/getting-started/#installing-rust)
  * [Hello, world!](https://rocket.rs/guide/master/getting-started/#hello-world)

* [Overview](https://rocket.rs/guide/master/overview/#overview)
  * [Lifecycle](https://rocket.rs/guide/master/overview/#lifecycle)
  * [Routing](https://rocket.rs/guide/master/overview/#routing)
  * [Mounting](https://rocket.rs/guide/master/overview/#mounting)
  * [Launching](https://rocket.rs/guide/master/overview/#launching)
  * [Futures and Async](https://rocket.rs/guide/master/overview/#futures-and-async)
    * [Async Routes](https://rocket.rs/guide/master/overview/#async-routes)
    * [Multitasking](https://rocket.rs/guide/master/overview/#multitasking)

* [Requests](https://rocket.rs/guide/master/requests/#requests)
  * [Methods](https://rocket.rs/guide/master/requests/#methods)
    * [HEAD Requests](https://rocket.rs/guide/master/requests/#head-requests)
    * [Reinterpreting](https://rocket.rs/guide/master/requests/#reinterpreting)

  * [Dynamic Paths](https://rocket.rs/guide/master/requests/#dynamic-paths)
    * [Multiple Segments](https://rocket.rs/guide/master/requests/#multiple-segments)
    * [Ignored Segments](https://rocket.rs/guide/master/requests/#ignored-segments)

  * [Forwarding](https://rocket.rs/guide/master/requests/#forwarding)
    * [Default Ranking](https://rocket.rs/guide/master/requests/#default-ranking)

  * [Request Guards](https://rocket.rs/guide/master/requests/#request-guards)
    * [Custom Guards](https://rocket.rs/guide/master/requests/#custom-guards)
    * [Guard Transparency](https://rocket.rs/guide/master/requests/#guard-transparency)
    * [Forwarding Guards](https://rocket.rs/guide/master/requests/#forwarding-guards)
    * [Fallible Guards](https://rocket.rs/guide/master/requests/#fallible-guards)

  * [Cookies](https://rocket.rs/guide/master/requests/#cookies)
    * [Private Cookies](https://rocket.rs/guide/master/requests/#private-cookies)
    * [Secret Key](https://rocket.rs/guide/master/requests/#secret-key)

  * [Format](https://rocket.rs/guide/master/requests/#format)
  * [Body Data](https://rocket.rs/guide/master/requests/#body-data)
    * [JSON](https://rocket.rs/guide/master/requests/#json)
    * [Temporary Files](https://rocket.rs/guide/master/requests/#temporary-files)
    * [Streaming](https://rocket.rs/guide/master/requests/#streaming)

  * [Forms](https://rocket.rs/guide/master/requests/#forms)
    * [Multipart](https://rocket.rs/guide/master/requests/#multipart)
    * [Parsing Strategy](https://rocket.rs/guide/master/requests/#parsing-strategy)
    * [Defaults](https://rocket.rs/guide/master/requests/#defaults)
    * [Field Renaming](https://rocket.rs/guide/master/requests/#field-renaming)
    * [Ad-Hoc Validation](https://rocket.rs/guide/master/requests/#ad-hoc-validation)
    * [Wrapping Validators](https://rocket.rs/guide/master/requests/#wrapping-validators)
    * [Collections](https://rocket.rs/guide/master/requests/#collections)
    * [Nesting](https://rocket.rs/guide/master/requests/#nesting)
    * [Vectors](https://rocket.rs/guide/master/requests/#vectors)
    * [Nesting in Vectors](https://rocket.rs/guide/master/requests/#nesting-in-vectors)
    * [Nested Vectors](https://rocket.rs/guide/master/requests/#nested-vectors)
    * [Maps](https://rocket.rs/guide/master/requests/#maps)
    * [Arbitrary Collections](https://rocket.rs/guide/master/requests/#arbitrary-collections)
    * [Context](https://rocket.rs/guide/master/requests/#context)

  * [Query Strings](https://rocket.rs/guide/master/requests/#query-strings)
    * [Static Parameters](https://rocket.rs/guide/master/requests/#static-parameters)
    * [Dynamic Parameters](https://rocket.rs/guide/master/requests/#dynamic-parameters)
    * [Trailing Parameter](https://rocket.rs/guide/master/requests/#trailing-parameter)

  * [Error Catchers](https://rocket.rs/guide/master/requests/#error-catchers)
    * [Scoping](https://rocket.rs/guide/master/requests/#scoping)
    * [Default Catchers](https://rocket.rs/guide/master/requests/#default-catchers)
    * [Built-In Catcher](https://rocket.rs/guide/master/requests/#built-in-catcher)

* [Responses](https://rocket.rs/guide/master/responses/#responses)
  * [Responder](https://rocket.rs/guide/master/responses/#responder)
    * [Wrapping](https://rocket.rs/guide/master/responses/#wrapping)
    * [Errors](https://rocket.rs/guide/master/responses/#errors)
    * [Status](https://rocket.rs/guide/master/responses/#status)

  * [Custom Responders](https://rocket.rs/guide/master/responses/#custom-responders)
  * [Implementations](https://rocket.rs/guide/master/responses/#implementations)
    * [Strings](https://rocket.rs/guide/master/responses/#strings)
    * [Option](https://rocket.rs/guide/master/responses/#option)
    * [Result](https://rocket.rs/guide/master/responses/#result)

  * [Rocket Responders](https://rocket.rs/guide/master/responses/#rocket-responders)
    * [Async Streams](https://rocket.rs/guide/master/responses/#async-streams)
    * [WebSockets](https://rocket.rs/guide/master/responses/#websockets)
    * [JSON](https://rocket.rs/guide/master/responses/#json)

  * [Templates](https://rocket.rs/guide/master/responses/#templates)
    * [Live Reloading](https://rocket.rs/guide/master/responses/#live-reloading)

  * [Typed URIs](https://rocket.rs/guide/master/responses/#typed-uris)
    * [Ignorables](https://rocket.rs/guide/master/responses/#ignorables)
    * [Deriving](https://rocket.rs/guide/master/responses/#deriving-uridisplay)
    * [Typed URI Parts](https://rocket.rs/guide/master/responses/#typed-uri-parts)
    * [Conversions](https://rocket.rs/guide/master/responses/#conversions)

* [State](https://rocket.rs/guide/master/state/#state)
  * [Managed State](https://rocket.rs/guide/master/state/#managed-state)
    * [Adding State](https://rocket.rs/guide/master/state/#adding-state)
    * [Retrieving State](https://rocket.rs/guide/master/state/#retrieving-state)
    * [Within Guards](https://rocket.rs/guide/master/state/#within-guards)

  * [Request-Local State](https://rocket.rs/guide/master/state/#request-local-state)
  * [Databases](https://rocket.rs/guide/master/state/#databases)
    * [Driver Features](https://rocket.rs/guide/master/state/#driver-features)
    * [Synchronous ORMs](https://rocket.rs/guide/master/state/#synchronous-orms)
    * [Examples](https://rocket.rs/guide/master/state/#examples)

* [Fairings](https://rocket.rs/guide/master/fairings/#fairings)
  * [Overview](https://rocket.rs/guide/master/fairings/#overview)
    * [Attaching](https://rocket.rs/guide/master/fairings/#attaching)
    * [Callbacks](https://rocket.rs/guide/master/fairings/#callbacks)

  * [Implementing](https://rocket.rs/guide/master/fairings/#implementing)
    * [Requirements](https://rocket.rs/guide/master/fairings/#requirements)
    * [Example](https://rocket.rs/guide/master/fairings/#example)

  * [Ad-Hoc Fairings](https://rocket.rs/guide/master/fairings/#ad-hoc-fairings)

* [Testing](https://rocket.rs/guide/master/testing/#testing)
  * [Local Dispatching](https://rocket.rs/guide/master/testing/#local-dispatching)
  * [Validating Responses](https://rocket.rs/guide/master/testing/#validating-responses)
  * [Testing "Hello, world!"](https://rocket.rs/guide/master/testing/#testing-hello-world)
    * [Setting Up](https://rocket.rs/guide/master/testing/#setting-up)
    * [Testing](https://rocket.rs/guide/master/testing/#testing-1)

  * [Asynchronous Testing](https://rocket.rs/guide/master/testing/#asynchronous-testing)
  * [Codegen Debug](https://rocket.rs/guide/master/testing/#codegen-debug)

* [Configuration](https://rocket.rs/guide/master/configuration/#configuration)
  * [Overview](https://rocket.rs/guide/master/configuration/#overview)
    * [Profiles](https://rocket.rs/guide/master/configuration/#profiles)

  * [Default Provider](https://rocket.rs/guide/master/configuration/#default-provider)
    * [Rocket.toml](https://rocket.rs/guide/master/configuration/#rocket-toml)
    * [Environment Variables](https://rocket.rs/guide/master/configuration/#environment-variables)

  * [Configuration Parameters](https://rocket.rs/guide/master/configuration/#configuration-parameters)
    * [Secret Key](https://rocket.rs/guide/master/configuration/#secret-key)
    * [Limits](https://rocket.rs/guide/master/configuration/#limits)
    * [TLS](https://rocket.rs/guide/master/configuration/#tls)
    * [Mutual TLS](https://rocket.rs/guide/master/configuration/#mutual-tls)
    * [Proxied TLS](https://rocket.rs/guide/master/configuration/#proxied-tls)
    * [Crypto Providers](https://rocket.rs/guide/master/configuration/#crypto-providers)
    * [Workers](https://rocket.rs/guide/master/configuration/#workers)

  * [Extracting Values](https://rocket.rs/guide/master/configuration/#extracting-values)
  * [Custom Providers](https://rocket.rs/guide/master/configuration/#custom-providers)

* [Deploying](https://rocket.rs/guide/master/deploying/#deploying)
  * [Overview](https://rocket.rs/guide/master/deploying/#overview)
  * [Common Scenarios](https://rocket.rs/guide/master/deploying/#common-scenarios)
    * [Self-Managed](https://rocket.rs/guide/master/deploying/#self-managed)
    * [Containerization](https://rocket.rs/guide/master/deploying/#containerization)
    * [Fully-Managed](https://rocket.rs/guide/master/deploying/#fully-managed)

* [Pastebin Tutorial](https://rocket.rs/guide/master/pastebin/#pastebin-tutorial)
  * [Finished Product](https://rocket.rs/guide/master/pastebin/#finished-product)
  * [Getting Started](https://rocket.rs/guide/master/pastebin/#getting-started)
  * [Index](https://rocket.rs/guide/master/pastebin/#index)
  * [Design](https://rocket.rs/guide/master/pastebin/#design)
  * [Retrieving Pastes](https://rocket.rs/guide/master/pastebin/#retrieving-pastes)
    * [A Problem](https://rocket.rs/guide/master/pastebin/#a-problem)
    * [The Solution](https://rocket.rs/guide/master/pastebin/#the-solution)

  * [Uploading](https://rocket.rs/guide/master/pastebin/#uploading)
    * [Streaming Data](https://rocket.rs/guide/master/pastebin/#streaming-data)
    * [Solution](https://rocket.rs/guide/master/pastebin/#solution)

  * [Conclusion](https://rocket.rs/guide/master/pastebin/#conclusion)

* [Conclusion](https://rocket.rs/guide/master/conclusion/#conclusion)
  * [Getting Help](https://rocket.rs/guide/master/conclusion/#getting-help)
  * [What's next?](https://rocket.rs/guide/master/conclusion/#what-s-next)

* [FAQ](https://rocket.rs/guide/master/faq/#faq)
  * [About Rocket](https://rocket.rs/guide/master/faq/#about-rocket)
  * [How To](https://rocket.rs/guide/master/faq/#how-to)
  * [Debugging](https://rocket.rs/guide/master/faq/#debugging)

[](https://rocket.rs/guide/master/#the-rocket-programming-guide "anchor")The Rocket Programming Guide
=====================================================================================================

Welcome to Rocket!

This is the official guide for Rocket v0.6. It is designed to serve as a starting point to writing web applications with Rocket and Rust. The guide is also designed to be a reference for experienced Rocket developers. This guide is conversational in tone. For purely technical documentation with examples, see the [API documentation](https://api.rocket.rs/master/rocket).

The guide is split into several sections, each with a focus on a different aspect of Rocket. The sections are:

* [Introduction](https://rocket.rs/guide/master/introduction/) - introduces Rocket and its philosophy
* [Upgrading](https://rocket.rs/guide/master/upgrading/) - a migration guide from Rocket v0.5 to v0.6
* [Quickstart](https://rocket.rs/guide/master/quickstart/) - the minimal steps to running your first Rocket application
* [Getting Started](https://rocket.rs/guide/master/getting-started/) - a gentle introduction to running your first Rocket application
* [Overview](https://rocket.rs/guide/master/overview/) - an overview of Rocket's core concepts
* [Requests](https://rocket.rs/guide/master/requests/) - handling request and body data: control-flow, parsing, validation
* [Responses](https://rocket.rs/guide/master/responses/) - generating responses and using typed URIs
* [State](https://rocket.rs/guide/master/state/) - managing application state and connecting to databases
* [Fairings](https://rocket.rs/guide/master/fairings/) - Rocket's structured middleware
* [Testing](https://rocket.rs/guide/master/testing/) - unit and integration testing with the built-in testing library
* [Configuration](https://rocket.rs/guide/master/configuration/) - overview and customization of Rocket application configuration
* [Deploying](https://rocket.rs/guide/master/deploying/) - how to deploy a Rocket application to production
* [Pastebin Tutorial](https://rocket.rs/guide/master/pastebin/) - step-by-step guide to creating a pastebin with Rocket
* [Conclusion](https://rocket.rs/guide/master/conclusion/) - next steps, and learning more about Rocket
* [FAQ](https://rocket.rs/guide/master/faq/) - answers to frequently asked questions about Rocket and its usage

[](https://rocket.rs/guide/master/#getting-help "anchor")Getting Help
---------------------------------------------------------------------

The official community support channels are via Matrix chat on [`#rocket:mozilla.org`](https://matrix.to/#/#rocket:mozilla.org) and via [GitHub Discussions](https://github.com/rwf2/Rocket/discussions). To join us on Matrix, we recommend the browser-based [Element](https://chat.mozilla.org/#/room/#rocket:mozilla.org) client. The [FAQ](https://rocket.rs/guide/master/faq/) also provides answers to commonly asked questions.

* * *

[Introduction ►](https://rocket.rs/guide/master/introduction/)

* * *

[© 2016-2025 Sergio Benitez](https://sergio.bz/)

![Image 10: Small Rocket Logo](https://rocket.rs/images/logo-small.svg)

[BACK TO TOP Δ](https://rocket.rs/guide/master/#)

![Image 11: cloud](https://rocket.rs/images/cloud-0.png)![Image 12: cloud](https://rocket.rs/images/cloud-1.png)![Image 13: cloud](https://rocket.rs/images/cloud-2.png)
