# Source: https://rocket.rs/guide/

Title: Programming Guide - Rocket Web Framework

URL Source: https://rocket.rs/guide/

Markdown Content:
Programming Guide - Rocket Web Framework
===============

![Image 1: cloud](https://rocket.rs/images/cloud-0.png)![Image 2: cloud](https://rocket.rs/images/cloud-1.png)![Image 3: cloud](https://rocket.rs/images/cloud-2.png)![Image 4: cloud](https://rocket.rs/images/cloud-0.png)![Image 5: cloud](https://rocket.rs/images/cloud-0.png)![Image 6: cloud](https://rocket.rs/images/cloud-0.png)

[Rocket Homepage](https://rocket.rs/)- [x] [overview](https://rocket.rs/overview/)[guide](https://rocket.rs/guide/v0.5/)[faq](https://rocket.rs/guide/v0.5/faq/#faq)[news](https://rocket.rs/news/)[docs](https://api.rocket.rs/v0.5/rocket/)[![Image 7: GitHub octocat](https://rocket.rs/images/github-mark-white.svg)](https://github.com/rwf2/Rocket/tree/v0.5.1)

[Guide](https://rocket.rs/guide/v0.5/)
======================================

v0.5

[v0.4](https://rocket.rs/guide/v0.4/)[v0.3](https://rocket.rs/guide/v0.3/)[master](https://rocket.rs/guide/master/)

#### The ins and outs of Rocket, in detail

* [Introduction](https://rocket.rs/guide/v0.5/introduction/#introduction)
  * [Audience](https://rocket.rs/guide/v0.5/introduction/#audience)
  * [Foreword](https://rocket.rs/guide/v0.5/introduction/#foreword)

* [Upgrading](https://rocket.rs/guide/v0.5/upgrading/#upgrading)
  * [Crate Organization](https://rocket.rs/guide/v0.5/upgrading/#crate-organization)
    * [Off-by-Default Secrets](https://rocket.rs/guide/v0.5/upgrading/#off-by-default-secrets)
    * [Contrib Deprecation](https://rocket.rs/guide/v0.5/upgrading/#contrib-deprecation)

  * [Stable and Async Support](https://rocket.rs/guide/v0.5/upgrading/#stable-and-async-support)
    * [Stable Release Channel](https://rocket.rs/guide/v0.5/upgrading/#stable-release-channel)
    * [Feature Attribute](https://rocket.rs/guide/v0.5/upgrading/#feature-attribute)
    * [Updates to Launch](https://rocket.rs/guide/v0.5/upgrading/#updates-to-launch)
    * [Blocking I/O](https://rocket.rs/guide/v0.5/upgrading/#blocking-i-o)
    * [Blocking Compute](https://rocket.rs/guide/v0.5/upgrading/#blocking-compute)
    * [Async Traits](https://rocket.rs/guide/v0.5/upgrading/#async-traits)

  * [Configuration](https://rocket.rs/guide/v0.5/upgrading/#configuration)
    * [Profiles](https://rocket.rs/guide/v0.5/upgrading/#profiles)
    * [Typed Extraction](https://rocket.rs/guide/v0.5/upgrading/#typed-extraction)

  * [Routing](https://rocket.rs/guide/v0.5/upgrading/#routing)
    * [Default Ranks](https://rocket.rs/guide/v0.5/upgrading/#default-ranks)
    * [Kleene Multi-Segments](https://rocket.rs/guide/v0.5/upgrading/#kleene-multi-segments)
    * [Fewer Raw Strings](https://rocket.rs/guide/v0.5/upgrading/#fewer-raw-strings)
    * [Queries as Forms](https://rocket.rs/guide/v0.5/upgrading/#queries-as-forms)

  * [Forms](https://rocket.rs/guide/v0.5/upgrading/#forms)
    * [Multipart](https://rocket.rs/guide/v0.5/upgrading/#multipart)
    * [Field Validation](https://rocket.rs/guide/v0.5/upgrading/#field-validation)

  * [Notable New Features](https://rocket.rs/guide/v0.5/upgrading/#notable-new-features)
    * [Sentinels](https://rocket.rs/guide/v0.5/upgrading/#sentinels)
    * [More Typed URIs](https://rocket.rs/guide/v0.5/upgrading/#more-typed-uris)
    * [Real-Time Streams](https://rocket.rs/guide/v0.5/upgrading/#real-time-streams)
    * [WebSockets](https://rocket.rs/guide/v0.5/upgrading/#websockets)

  * [Getting Help](https://rocket.rs/guide/v0.5/upgrading/#getting-help)

* [Quickstart](https://rocket.rs/guide/v0.5/quickstart/#quickstart)
  * [Running Examples](https://rocket.rs/guide/v0.5/quickstart/#running-examples)

* [Getting Started](https://rocket.rs/guide/v0.5/getting-started/#getting-started)
  * [Installing Rust](https://rocket.rs/guide/v0.5/getting-started/#installing-rust)
  * [Hello, world!](https://rocket.rs/guide/v0.5/getting-started/#hello-world)

* [Overview](https://rocket.rs/guide/v0.5/overview/#overview)
  * [Lifecycle](https://rocket.rs/guide/v0.5/overview/#lifecycle)
  * [Routing](https://rocket.rs/guide/v0.5/overview/#routing)
  * [Mounting](https://rocket.rs/guide/v0.5/overview/#mounting)
  * [Launching](https://rocket.rs/guide/v0.5/overview/#launching)
  * [Futures and Async](https://rocket.rs/guide/v0.5/overview/#futures-and-async)
    * [Async Routes](https://rocket.rs/guide/v0.5/overview/#async-routes)
    * [Multitasking](https://rocket.rs/guide/v0.5/overview/#multitasking)

* [Requests](https://rocket.rs/guide/v0.5/requests/#requests)
  * [Methods](https://rocket.rs/guide/v0.5/requests/#methods)
    * [HEAD Requests](https://rocket.rs/guide/v0.5/requests/#head-requests)
    * [Reinterpreting](https://rocket.rs/guide/v0.5/requests/#reinterpreting)

  * [Dynamic Paths](https://rocket.rs/guide/v0.5/requests/#dynamic-paths)
    * [Multiple Segments](https://rocket.rs/guide/v0.5/requests/#multiple-segments)
    * [Ignored Segments](https://rocket.rs/guide/v0.5/requests/#ignored-segments)

  * [Forwarding](https://rocket.rs/guide/v0.5/requests/#forwarding)
    * [Default Ranking](https://rocket.rs/guide/v0.5/requests/#default-ranking)

  * [Request Guards](https://rocket.rs/guide/v0.5/requests/#request-guards)
    * [Custom Guards](https://rocket.rs/guide/v0.5/requests/#custom-guards)
    * [Guard Transparency](https://rocket.rs/guide/v0.5/requests/#guard-transparency)
    * [Forwarding Guards](https://rocket.rs/guide/v0.5/requests/#forwarding-guards)
    * [Fallible Guards](https://rocket.rs/guide/v0.5/requests/#fallible-guards)

  * [Cookies](https://rocket.rs/guide/v0.5/requests/#cookies)
    * [Private Cookies](https://rocket.rs/guide/v0.5/requests/#private-cookies)
    * [Secret Key](https://rocket.rs/guide/v0.5/requests/#secret-key)

  * [Format](https://rocket.rs/guide/v0.5/requests/#format)
  * [Body Data](https://rocket.rs/guide/v0.5/requests/#body-data)
    * [JSON](https://rocket.rs/guide/v0.5/requests/#json)
    * [Temporary Files](https://rocket.rs/guide/v0.5/requests/#temporary-files)
    * [Streaming](https://rocket.rs/guide/v0.5/requests/#streaming)

  * [Forms](https://rocket.rs/guide/v0.5/requests/#forms)
    * [Multipart](https://rocket.rs/guide/v0.5/requests/#multipart)
    * [Parsing Strategy](https://rocket.rs/guide/v0.5/requests/#parsing-strategy)
    * [Defaults](https://rocket.rs/guide/v0.5/requests/#defaults)
    * [Field Renaming](https://rocket.rs/guide/v0.5/requests/#field-renaming)
    * [Ad-Hoc Validation](https://rocket.rs/guide/v0.5/requests/#ad-hoc-validation)
    * [Wrapping Validators](https://rocket.rs/guide/v0.5/requests/#wrapping-validators)
    * [Collections](https://rocket.rs/guide/v0.5/requests/#collections)
    * [Nesting](https://rocket.rs/guide/v0.5/requests/#nesting)
    * [Vectors](https://rocket.rs/guide/v0.5/requests/#vectors)
    * [Nesting in Vectors](https://rocket.rs/guide/v0.5/requests/#nesting-in-vectors)
    * [Nested Vectors](https://rocket.rs/guide/v0.5/requests/#nested-vectors)
    * [Maps](https://rocket.rs/guide/v0.5/requests/#maps)
    * [Arbitrary Collections](https://rocket.rs/guide/v0.5/requests/#arbitrary-collections)
    * [Context](https://rocket.rs/guide/v0.5/requests/#context)

  * [Query Strings](https://rocket.rs/guide/v0.5/requests/#query-strings)
    * [Static Parameters](https://rocket.rs/guide/v0.5/requests/#static-parameters)
    * [Dynamic Parameters](https://rocket.rs/guide/v0.5/requests/#dynamic-parameters)
    * [Trailing Parameter](https://rocket.rs/guide/v0.5/requests/#trailing-parameter)

  * [Error Catchers](https://rocket.rs/guide/v0.5/requests/#error-catchers)
    * [Scoping](https://rocket.rs/guide/v0.5/requests/#scoping)
    * [Default Catchers](https://rocket.rs/guide/v0.5/requests/#default-catchers)
    * [Built-In Catcher](https://rocket.rs/guide/v0.5/requests/#built-in-catcher)

* [Responses](https://rocket.rs/guide/v0.5/responses/#responses)
  * [Responder](https://rocket.rs/guide/v0.5/responses/#responder)
    * [Wrapping](https://rocket.rs/guide/v0.5/responses/#wrapping)
    * [Errors](https://rocket.rs/guide/v0.5/responses/#errors)
    * [Status](https://rocket.rs/guide/v0.5/responses/#status)

  * [Custom Responders](https://rocket.rs/guide/v0.5/responses/#custom-responders)
  * [Implementations](https://rocket.rs/guide/v0.5/responses/#implementations)
    * [Strings](https://rocket.rs/guide/v0.5/responses/#strings)
    * [Option](https://rocket.rs/guide/v0.5/responses/#option)
    * [Result](https://rocket.rs/guide/v0.5/responses/#result)

  * [Rocket Responders](https://rocket.rs/guide/v0.5/responses/#rocket-responders)
    * [Async Streams](https://rocket.rs/guide/v0.5/responses/#async-streams)
    * [WebSockets](https://rocket.rs/guide/v0.5/responses/#websockets)
    * [JSON](https://rocket.rs/guide/v0.5/responses/#json)

  * [Templates](https://rocket.rs/guide/v0.5/responses/#templates)
    * [Live Reloading](https://rocket.rs/guide/v0.5/responses/#live-reloading)

  * [Typed URIs](https://rocket.rs/guide/v0.5/responses/#typed-uris)
    * [Ignorables](https://rocket.rs/guide/v0.5/responses/#ignorables)
    * [Deriving](https://rocket.rs/guide/v0.5/responses/#deriving-uridisplay)
    * [Typed URI Parts](https://rocket.rs/guide/v0.5/responses/#typed-uri-parts)
    * [Conversions](https://rocket.rs/guide/v0.5/responses/#conversions)

* [State](https://rocket.rs/guide/v0.5/state/#state)
  * [Managed State](https://rocket.rs/guide/v0.5/state/#managed-state)
    * [Adding State](https://rocket.rs/guide/v0.5/state/#adding-state)
    * [Retrieving State](https://rocket.rs/guide/v0.5/state/#retrieving-state)
    * [Within Guards](https://rocket.rs/guide/v0.5/state/#within-guards)

  * [Request-Local State](https://rocket.rs/guide/v0.5/state/#request-local-state)
  * [Databases](https://rocket.rs/guide/v0.5/state/#databases)
    * [Driver Features](https://rocket.rs/guide/v0.5/state/#driver-features)
    * [Synchronous ORMs](https://rocket.rs/guide/v0.5/state/#synchronous-orms)
    * [Examples](https://rocket.rs/guide/v0.5/state/#examples)

* [Fairings](https://rocket.rs/guide/v0.5/fairings/#fairings)
  * [Overview](https://rocket.rs/guide/v0.5/fairings/#overview)
    * [Attaching](https://rocket.rs/guide/v0.5/fairings/#attaching)
    * [Callbacks](https://rocket.rs/guide/v0.5/fairings/#callbacks)

  * [Implementing](https://rocket.rs/guide/v0.5/fairings/#implementing)
    * [Requirements](https://rocket.rs/guide/v0.5/fairings/#requirements)
    * [Example](https://rocket.rs/guide/v0.5/fairings/#example)

  * [Ad-Hoc Fairings](https://rocket.rs/guide/v0.5/fairings/#ad-hoc-fairings)

* [Testing](https://rocket.rs/guide/v0.5/testing/#testing)
  * [Local Dispatching](https://rocket.rs/guide/v0.5/testing/#local-dispatching)
  * [Validating Responses](https://rocket.rs/guide/v0.5/testing/#validating-responses)
  * [Testing "Hello, world!"](https://rocket.rs/guide/v0.5/testing/#testing-hello-world)
    * [Setting Up](https://rocket.rs/guide/v0.5/testing/#setting-up)
    * [Testing](https://rocket.rs/guide/v0.5/testing/#testing-1)

  * [Asynchronous Testing](https://rocket.rs/guide/v0.5/testing/#asynchronous-testing)
  * [Codegen Debug](https://rocket.rs/guide/v0.5/testing/#codegen-debug)

* [Configuration](https://rocket.rs/guide/v0.5/configuration/#configuration)
  * [Overview](https://rocket.rs/guide/v0.5/configuration/#overview)
    * [Profiles](https://rocket.rs/guide/v0.5/configuration/#profiles)

  * [Default Provider](https://rocket.rs/guide/v0.5/configuration/#default-provider)
    * [Rocket.toml](https://rocket.rs/guide/v0.5/configuration/#rocket-toml)
    * [Environment Variables](https://rocket.rs/guide/v0.5/configuration/#environment-variables)

  * [Configuration Parameters](https://rocket.rs/guide/v0.5/configuration/#configuration-parameters)
    * [Secret Key](https://rocket.rs/guide/v0.5/configuration/#secret-key)
    * [Limits](https://rocket.rs/guide/v0.5/configuration/#limits)
    * [TLS](https://rocket.rs/guide/v0.5/configuration/#tls)
    * [Mutual TLS](https://rocket.rs/guide/v0.5/configuration/#mutual-tls)
    * [Workers](https://rocket.rs/guide/v0.5/configuration/#workers)

  * [Extracting Values](https://rocket.rs/guide/v0.5/configuration/#extracting-values)
  * [Custom Providers](https://rocket.rs/guide/v0.5/configuration/#custom-providers)

* [Deploying](https://rocket.rs/guide/v0.5/deploying/#deploying)
  * [Overview](https://rocket.rs/guide/v0.5/deploying/#overview)
  * [Common Scenarios](https://rocket.rs/guide/v0.5/deploying/#common-scenarios)
    * [Self-Managed](https://rocket.rs/guide/v0.5/deploying/#self-managed)
    * [Containerization](https://rocket.rs/guide/v0.5/deploying/#containerization)
    * [Fully-Managed](https://rocket.rs/guide/v0.5/deploying/#fully-managed)

* [Pastebin Tutorial](https://rocket.rs/guide/v0.5/pastebin/#pastebin-tutorial)
  * [Finished Product](https://rocket.rs/guide/v0.5/pastebin/#finished-product)
  * [Getting Started](https://rocket.rs/guide/v0.5/pastebin/#getting-started)
  * [Index](https://rocket.rs/guide/v0.5/pastebin/#index)
  * [Design](https://rocket.rs/guide/v0.5/pastebin/#design)
  * [Retrieving Pastes](https://rocket.rs/guide/v0.5/pastebin/#retrieving-pastes)
    * [A Problem](https://rocket.rs/guide/v0.5/pastebin/#a-problem)
    * [The Solution](https://rocket.rs/guide/v0.5/pastebin/#the-solution)

  * [Uploading](https://rocket.rs/guide/v0.5/pastebin/#uploading)
    * [Streaming Data](https://rocket.rs/guide/v0.5/pastebin/#streaming-data)
    * [Solution](https://rocket.rs/guide/v0.5/pastebin/#solution)

  * [Conclusion](https://rocket.rs/guide/v0.5/pastebin/#conclusion)

* [Conclusion](https://rocket.rs/guide/v0.5/conclusion/#conclusion)
  * [Getting Help](https://rocket.rs/guide/v0.5/conclusion/#getting-help)
  * [What's next?](https://rocket.rs/guide/v0.5/conclusion/#what-s-next)

* [FAQ](https://rocket.rs/guide/v0.5/faq/#faq)
  * [About Rocket](https://rocket.rs/guide/v0.5/faq/#about-rocket)
  * [How To](https://rocket.rs/guide/v0.5/faq/#how-to)
  * [Debugging](https://rocket.rs/guide/v0.5/faq/#debugging)

[](https://rocket.rs/guide/#the-rocket-programming-guide "anchor")The Rocket Programming Guide
==============================================================================================

Welcome to Rocket!

This is the official guide for Rocket v0.5. It is designed to serve as a starting point to writing web applications with Rocket and Rust. The guide is also designed to be a reference for experienced Rocket developers. This guide is conversational in tone. For purely technical documentation with examples, see the [API documentation](https://api.rocket.rs/v0.5/rocket).

The guide is split into several sections, each with a focus on a different aspect of Rocket. The sections are:

* [Introduction](https://rocket.rs/guide/v0.5/introduction/) - introduces Rocket and its philosophy
* [Upgrading](https://rocket.rs/guide/v0.5/upgrading/) - a migration guide from Rocket v0.4 to v0.5
* [Quickstart](https://rocket.rs/guide/v0.5/quickstart/) - the minimal steps to running your first Rocket application
* [Getting Started](https://rocket.rs/guide/v0.5/getting-started/) - a gentle introduction to running your first Rocket application
* [Overview](https://rocket.rs/guide/v0.5/overview/) - an overview of Rocket's core concepts
* [Requests](https://rocket.rs/guide/v0.5/requests/) - handling request and body data: control-flow, parsing, validation
* [Responses](https://rocket.rs/guide/v0.5/responses/) - generating responses and using typed URIs
* [State](https://rocket.rs/guide/v0.5/state/) - managing application state and connecting to databases
* [Fairings](https://rocket.rs/guide/v0.5/fairings/) - Rocket's structured middleware
* [Testing](https://rocket.rs/guide/v0.5/testing/) - unit and integration testing with the built-in testing library
* [Configuration](https://rocket.rs/guide/v0.5/configuration/) - overview and customization of Rocket application configuration
* [Deploying](https://rocket.rs/guide/v0.5/deploying/) - how to deploy a Rocket application to production
* [Pastebin Tutorial](https://rocket.rs/guide/v0.5/pastebin/) - step-by-step guide to creating a pastebin with Rocket
* [Conclusion](https://rocket.rs/guide/v0.5/conclusion/) - next steps, and learning more about Rocket
* [FAQ](https://rocket.rs/guide/v0.5/faq/) - answers to frequently asked questions about Rocket and its usage

[](https://rocket.rs/guide/#getting-help "anchor")Getting Help
--------------------------------------------------------------

The official community support channels are via Matrix chat on [`#rocket:mozilla.org`](https://matrix.to/#/#rocket:mozilla.org) and via [GitHub Discussions](https://github.com/rwf2/Rocket/discussions). To join us on Matrix, we recommend the browser-based [Element](https://chat.mozilla.org/#/room/#rocket:mozilla.org) client. The [FAQ](https://rocket.rs/guide/faq/) also provides answers to commonly asked questions.

* * *

[Introduction ►](https://rocket.rs/guide/v0.5/introduction/)

* * *

[© 2016-2025 Sergio Benitez](https://sergio.bz/)

![Image 8: Small Rocket Logo](https://rocket.rs/images/logo-small.svg)

[BACK TO TOP Δ](https://rocket.rs/guide/#)

![Image 9: cloud](https://rocket.rs/images/cloud-0.png)![Image 10: cloud](https://rocket.rs/images/cloud-1.png)![Image 11: cloud](https://rocket.rs/images/cloud-2.png)
