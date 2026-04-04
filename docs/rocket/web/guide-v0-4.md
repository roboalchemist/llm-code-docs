# Source: https://rocket.rs/guide/v0.4/

Title: Programming Guide - Rocket Web Framework

URL Source: https://rocket.rs/guide/v0.4/

Markdown Content:
Programming Guide - Rocket Web Framework
===============

![Image 1: cloud](https://rocket.rs/images/cloud-0.png)![Image 2: cloud](https://rocket.rs/images/cloud-1.png)![Image 3: cloud](https://rocket.rs/images/cloud-2.png)![Image 4: cloud](https://rocket.rs/images/cloud-0.png)![Image 5: cloud](https://rocket.rs/images/cloud-0.png)![Image 6: cloud](https://rocket.rs/images/cloud-0.png)

[Rocket Homepage](https://rocket.rs/)- [x] [overview](https://rocket.rs/overview/)[guide](https://rocket.rs/guide/v0.5/)[faq](https://rocket.rs/guide/v0.5/faq/#faq)[news](https://rocket.rs/news/)[docs](https://api.rocket.rs/v0.5/rocket/)[![Image 7: GitHub octocat](https://rocket.rs/images/github-mark-white.svg)](https://github.com/rwf2/Rocket/tree/v0.5.1)

[Guide](https://rocket.rs/guide/v0.4/)
======================================

v0.4

[v0.5](https://rocket.rs/guide/v0.5/)[v0.3](https://rocket.rs/guide/v0.3/)[master](https://rocket.rs/guide/master/)

#### The ins and outs of Rocket, in detail

![Image 8: warning icon](https://rocket.rs/images/warning-icon.svg) This documentation is out of date. [Go to current release.](https://rocket.rs/guide/v0.5/)![Image 9: warning icon](https://rocket.rs/images/warning-icon.svg)

* [Introduction](https://rocket.rs/guide/v0.4/introduction/#introduction)
  * [Audience](https://rocket.rs/guide/v0.4/introduction/#audience)
  * [Foreword](https://rocket.rs/guide/v0.4/introduction/#foreword)

* [Quickstart](https://rocket.rs/guide/v0.4/quickstart/#quickstart)
  * [Running Examples](https://rocket.rs/guide/v0.4/quickstart/#running-examples)

* [Getting Started](https://rocket.rs/guide/v0.4/getting-started/#getting-started)
  * [Installing Rust](https://rocket.rs/guide/v0.4/getting-started/#installing-rust)
  * [Hello, world!](https://rocket.rs/guide/v0.4/getting-started/#hello-world)

* [Overview](https://rocket.rs/guide/v0.4/overview/#overview)
  * [Lifecycle](https://rocket.rs/guide/v0.4/overview/#lifecycle)
  * [Routing](https://rocket.rs/guide/v0.4/overview/#routing)
  * [Mounting](https://rocket.rs/guide/v0.4/overview/#mounting)
    * [Namespacing](https://rocket.rs/guide/v0.4/overview/#namespacing)

  * [Launching](https://rocket.rs/guide/v0.4/overview/#launching)

* [Requests](https://rocket.rs/guide/v0.4/requests/#requests)
  * [Methods](https://rocket.rs/guide/v0.4/requests/#methods)
    * [HEAD Requests](https://rocket.rs/guide/v0.4/requests/#head-requests)
    * [Reinterpreting](https://rocket.rs/guide/v0.4/requests/#reinterpreting)

  * [Dynamic Paths](https://rocket.rs/guide/v0.4/requests/#dynamic-paths)
    * [Multiple Segments](https://rocket.rs/guide/v0.4/requests/#multiple-segments)

  * [Forwarding](https://rocket.rs/guide/v0.4/requests/#forwarding)
    * [Default Ranking](https://rocket.rs/guide/v0.4/requests/#default-ranking)

  * [Query Strings](https://rocket.rs/guide/v0.4/requests/#query-strings)
    * [Optional Parameters](https://rocket.rs/guide/v0.4/requests/#optional-parameters)
    * [Multiple Segments](https://rocket.rs/guide/v0.4/requests/#multiple-segments-1)

  * [Request Guards](https://rocket.rs/guide/v0.4/requests/#request-guards)
    * [Custom Guards](https://rocket.rs/guide/v0.4/requests/#custom-guards)
    * [Guard Transparency](https://rocket.rs/guide/v0.4/requests/#guard-transparency)
    * [Forwarding Guards](https://rocket.rs/guide/v0.4/requests/#forwarding-guards)

  * [Cookies](https://rocket.rs/guide/v0.4/requests/#cookies)
    * [Private Cookies](https://rocket.rs/guide/v0.4/requests/#private-cookies)
    * [Secret Key](https://rocket.rs/guide/v0.4/requests/#secret-key)
    * [One-At-A-Time](https://rocket.rs/guide/v0.4/requests/#one-at-a-time)

  * [Format](https://rocket.rs/guide/v0.4/requests/#format)
  * [Body Data](https://rocket.rs/guide/v0.4/requests/#body-data)
    * [Forms](https://rocket.rs/guide/v0.4/requests/#forms)
    * [JSON](https://rocket.rs/guide/v0.4/requests/#json)
    * [Streaming](https://rocket.rs/guide/v0.4/requests/#streaming)

  * [Error Catchers](https://rocket.rs/guide/v0.4/requests/#error-catchers)

* [Responses](https://rocket.rs/guide/v0.4/responses/#responses)
  * [Responder](https://rocket.rs/guide/v0.4/responses/#responder)
    * [Wrapping](https://rocket.rs/guide/v0.4/responses/#wrapping)
    * [Errors](https://rocket.rs/guide/v0.4/responses/#errors)
    * [Status](https://rocket.rs/guide/v0.4/responses/#status)

  * [Custom Responders](https://rocket.rs/guide/v0.4/responses/#custom-responders)
  * [Implementations](https://rocket.rs/guide/v0.4/responses/#implementations)
    * [Strings](https://rocket.rs/guide/v0.4/responses/#strings)
    * [Option](https://rocket.rs/guide/v0.4/responses/#option)
    * [Result](https://rocket.rs/guide/v0.4/responses/#result)

  * [Rocket Responders](https://rocket.rs/guide/v0.4/responses/#rocket-responders)
    * [Streaming](https://rocket.rs/guide/v0.4/responses/#streaming)
    * [JSON](https://rocket.rs/guide/v0.4/responses/#json)

  * [Templates](https://rocket.rs/guide/v0.4/responses/#templates)
    * [Live Reloading](https://rocket.rs/guide/v0.4/responses/#live-reloading)

  * [Typed URIs](https://rocket.rs/guide/v0.4/responses/#typed-uris)
    * [Ignorables](https://rocket.rs/guide/v0.4/responses/#ignorables)
    * [Deriving](https://rocket.rs/guide/v0.4/responses/#deriving-uridisplay)
    * [Typed URI Parts](https://rocket.rs/guide/v0.4/responses/#typed-uri-parts)
    * [Conversions](https://rocket.rs/guide/v0.4/responses/#conversions)

* [State](https://rocket.rs/guide/v0.4/state/#state)
  * [Managed State](https://rocket.rs/guide/v0.4/state/#managed-state)
    * [Adding State](https://rocket.rs/guide/v0.4/state/#adding-state)
    * [Retrieving State](https://rocket.rs/guide/v0.4/state/#retrieving-state)
    * [Within Guards](https://rocket.rs/guide/v0.4/state/#within-guards)

  * [Request-Local State](https://rocket.rs/guide/v0.4/state/#request-local-state)
  * [Databases](https://rocket.rs/guide/v0.4/state/#databases)
    * [Usage](https://rocket.rs/guide/v0.4/state/#usage)

* [Fairings](https://rocket.rs/guide/v0.4/fairings/#fairings)
  * [Overview](https://rocket.rs/guide/v0.4/fairings/#overview)
    * [Attaching](https://rocket.rs/guide/v0.4/fairings/#attaching)
    * [Callbacks](https://rocket.rs/guide/v0.4/fairings/#callbacks)

  * [Implementing](https://rocket.rs/guide/v0.4/fairings/#implementing)
    * [Requirements](https://rocket.rs/guide/v0.4/fairings/#requirements)
    * [Example](https://rocket.rs/guide/v0.4/fairings/#example)

  * [Ad-Hoc Fairings](https://rocket.rs/guide/v0.4/fairings/#ad-hoc-fairings)

* [Testing](https://rocket.rs/guide/v0.4/testing/#testing)
  * [Local Dispatching](https://rocket.rs/guide/v0.4/testing/#local-dispatching)
  * [Validating Responses](https://rocket.rs/guide/v0.4/testing/#validating-responses)
  * [Testing "Hello, world!"](https://rocket.rs/guide/v0.4/testing/#testing-hello-world)
    * [Setting Up](https://rocket.rs/guide/v0.4/testing/#setting-up)
    * [Testing](https://rocket.rs/guide/v0.4/testing/#testing-1)

  * [Codegen Debug](https://rocket.rs/guide/v0.4/testing/#codegen-debug)

* [Configuration](https://rocket.rs/guide/v0.4/configuration/#configuration)
  * [Environment](https://rocket.rs/guide/v0.4/configuration/#environment)
  * [Rocket.toml](https://rocket.rs/guide/v0.4/configuration/#rocket-toml)
  * [Data Limits](https://rocket.rs/guide/v0.4/configuration/#data-limits)
  * [Extras](https://rocket.rs/guide/v0.4/configuration/#extras)
  * [Environment Variables](https://rocket.rs/guide/v0.4/configuration/#environment-variables)
  * [Programmatic](https://rocket.rs/guide/v0.4/configuration/#programmatic)
  * [Configuring TLS](https://rocket.rs/guide/v0.4/configuration/#configuring-tls)

* [Pastebin](https://rocket.rs/guide/v0.4/pastebin/#pastebin)
  * [Finished Product](https://rocket.rs/guide/v0.4/pastebin/#finished-product)
  * [Getting Started](https://rocket.rs/guide/v0.4/pastebin/#getting-started)
  * [Index](https://rocket.rs/guide/v0.4/pastebin/#index)
  * [Uploading](https://rocket.rs/guide/v0.4/pastebin/#uploading)
    * [Unique IDs](https://rocket.rs/guide/v0.4/pastebin/#unique-ids)
    * [Processing](https://rocket.rs/guide/v0.4/pastebin/#processing)
    * [Upload Route](https://rocket.rs/guide/v0.4/pastebin/#upload-route)

  * [Retrieving Pastes](https://rocket.rs/guide/v0.4/pastebin/#retrieving-pastes)
  * [Conclusion](https://rocket.rs/guide/v0.4/pastebin/#conclusion)

* [Conclusion](https://rocket.rs/guide/v0.4/conclusion/#conclusion)
  * [Getting Help](https://rocket.rs/guide/v0.4/conclusion/#getting-help)
  * [What's next?](https://rocket.rs/guide/v0.4/conclusion/#what-s-next)

[](https://rocket.rs/guide/v0.4/#the-rocket-programming-guide "anchor")The Rocket Programming Guide
===================================================================================================

Welcome to Rocket!

This is the official guide for Rocket v0.4. It is designed to serve as a starting point to writing web applications with Rocket and Rust. The guide is also designed to be a reference for experienced Rocket developers. This guide is conversational in tone. For purely technical documentation with examples, see the [API documentation](https://api.rocket.rs/v0.4).

The guide is split into several sections, each with a focus on a different aspect of Rocket. The sections are:

* **[Introduction](https://rocket.rs/guide/v0.4/introduction/):** introduces Rocket and its philosophy.
* **[Quickstart](https://rocket.rs/guide/v0.4/quickstart/):** presents the minimal steps necessary to run your first Rocket application.
* **[Getting Started](https://rocket.rs/guide/v0.4/getting-started/):** a gentle introduction to getting your first Rocket application running.
* **[Overview](https://rocket.rs/guide/v0.4/overview/):** describes the core concepts of Rocket.
* **[Requests](https://rocket.rs/guide/v0.4/requests/):** discusses handling requests: control-flow, parsing, and validating.
* **[Responses](https://rocket.rs/guide/v0.4/responses/):** discusses generating responses.
* **[State](https://rocket.rs/guide/v0.4/state/):** how to manage state in a Rocket application.
* **[Fairings](https://rocket.rs/guide/v0.4/fairings/):** provides an overview of Rocket's structured middleware.
* **[Testing](https://rocket.rs/guide/v0.4/testing/):** how to unit and integration test a Rocket application.
* **[Configuration](https://rocket.rs/guide/v0.4/configuration/):** how to configure a Rocket application.
* **[Pastebin](https://rocket.rs/guide/v0.4/pastebin/):** a tutorial on how to create a pastebin with Rocket.
* **[Conclusion](https://rocket.rs/guide/v0.4/conclusion/):** concludes the guide and discusses next steps for learning.

[](https://rocket.rs/guide/v0.4/#getting-help "anchor")Getting Help
-------------------------------------------------------------------

The official community support channels is [`#rocket:mozilla.org`](https://matrix.to/#/#rocket:mozilla.org) on Matrix.

* * *

[Introduction ►](https://rocket.rs/guide/v0.4/introduction/)

* * *

[© 2016-2025 Sergio Benitez](https://sergio.bz/)

![Image 10: Small Rocket Logo](https://rocket.rs/images/logo-small.svg)

[BACK TO TOP Δ](https://rocket.rs/guide/v0.4/#)

![Image 11: cloud](https://rocket.rs/images/cloud-0.png)![Image 12: cloud](https://rocket.rs/images/cloud-1.png)![Image 13: cloud](https://rocket.rs/images/cloud-2.png)
