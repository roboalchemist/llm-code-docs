# Source: https://rocket.rs/guide/v0.3/

Title: Programming Guide - Rocket Web Framework

URL Source: https://rocket.rs/guide/v0.3/

Markdown Content:
Programming Guide - Rocket Web Framework
===============

![Image 1: cloud](https://rocket.rs/images/cloud-0.png)![Image 2: cloud](https://rocket.rs/images/cloud-1.png)![Image 3: cloud](https://rocket.rs/images/cloud-2.png)![Image 4: cloud](https://rocket.rs/images/cloud-0.png)![Image 5: cloud](https://rocket.rs/images/cloud-0.png)![Image 6: cloud](https://rocket.rs/images/cloud-0.png)

[Rocket Homepage](https://rocket.rs/)- [x] [overview](https://rocket.rs/overview/)[guide](https://rocket.rs/guide/v0.5/)[faq](https://rocket.rs/guide/v0.5/faq/#faq)[news](https://rocket.rs/news/)[docs](https://api.rocket.rs/v0.5/rocket/)[![Image 7: GitHub octocat](https://rocket.rs/images/github-mark-white.svg)](https://github.com/rwf2/Rocket/tree/v0.5.1)

[Guide](https://rocket.rs/guide/v0.3/)
======================================

v0.3

[v0.5](https://rocket.rs/guide/v0.5/)[v0.4](https://rocket.rs/guide/v0.4/)[master](https://rocket.rs/guide/master/)

#### The ins and outs of Rocket, in detail

![Image 8: warning icon](https://rocket.rs/images/warning-icon.svg) This documentation is out of date. [Go to current release.](https://rocket.rs/guide/v0.5/)![Image 9: warning icon](https://rocket.rs/images/warning-icon.svg)

* [Introduction](https://rocket.rs/guide/v0.3/introduction/#introduction)
  * [Audience](https://rocket.rs/guide/v0.3/introduction/#audience)
  * [Foreword](https://rocket.rs/guide/v0.3/introduction/#foreword)

* [Quickstart](https://rocket.rs/guide/v0.3/quickstart/#quickstart)
  * [Running Examples](https://rocket.rs/guide/v0.3/quickstart/#running-examples)

* [Getting Started](https://rocket.rs/guide/v0.3/getting-started/#getting-started)
  * [Installing Rust](https://rocket.rs/guide/v0.3/getting-started/#installing-rust)
    * [Minimum Nightly](https://rocket.rs/guide/v0.3/getting-started/#minimum-nightly)

  * [Hello, world!](https://rocket.rs/guide/v0.3/getting-started/#hello-world)

* [Overview](https://rocket.rs/guide/v0.3/overview/#overview)
  * [Lifecycle](https://rocket.rs/guide/v0.3/overview/#lifecycle)
  * [Routing](https://rocket.rs/guide/v0.3/overview/#routing)
  * [Mounting](https://rocket.rs/guide/v0.3/overview/#mounting)
    * [Namespacing](https://rocket.rs/guide/v0.3/overview/#namespacing)

  * [Launching](https://rocket.rs/guide/v0.3/overview/#launching)

* [Requests](https://rocket.rs/guide/v0.3/requests/#requests)
  * [Methods](https://rocket.rs/guide/v0.3/requests/#methods)
    * [HEAD Requests](https://rocket.rs/guide/v0.3/requests/#head-requests)
    * [Reinterpreting](https://rocket.rs/guide/v0.3/requests/#reinterpreting)

  * [Dynamic Segments](https://rocket.rs/guide/v0.3/requests/#dynamic-segments)
    * [Raw Strings](https://rocket.rs/guide/v0.3/requests/#raw-strings)

  * [Forwarding](https://rocket.rs/guide/v0.3/requests/#forwarding)
    * [Default Ranking](https://rocket.rs/guide/v0.3/requests/#default-ranking)

  * [Multiple Segments](https://rocket.rs/guide/v0.3/requests/#multiple-segments)
  * [Format](https://rocket.rs/guide/v0.3/requests/#format)
  * [Request Guards](https://rocket.rs/guide/v0.3/requests/#request-guards)
    * [Custom Guards](https://rocket.rs/guide/v0.3/requests/#custom-guards)
    * [Forwarding Guards](https://rocket.rs/guide/v0.3/requests/#forwarding-guards)

  * [Cookies](https://rocket.rs/guide/v0.3/requests/#cookies)
    * [Private Cookies](https://rocket.rs/guide/v0.3/requests/#private-cookies)
    * [Secret Key](https://rocket.rs/guide/v0.3/requests/#secret-key)
    * [One-At-A-Time](https://rocket.rs/guide/v0.3/requests/#one-at-a-time)

  * [Body Data](https://rocket.rs/guide/v0.3/requests/#body-data)
    * [Forms](https://rocket.rs/guide/v0.3/requests/#forms)
    * [JSON](https://rocket.rs/guide/v0.3/requests/#json)
    * [Streaming](https://rocket.rs/guide/v0.3/requests/#streaming)

  * [Query Strings](https://rocket.rs/guide/v0.3/requests/#query-strings)
  * [Error Catchers](https://rocket.rs/guide/v0.3/requests/#error-catchers)

* [Responses](https://rocket.rs/guide/v0.3/responses/#responses)
  * [Responder](https://rocket.rs/guide/v0.3/responses/#responder)
    * [Wrapping](https://rocket.rs/guide/v0.3/responses/#wrapping)
    * [Errors](https://rocket.rs/guide/v0.3/responses/#errors)

  * [Implementations](https://rocket.rs/guide/v0.3/responses/#implementations)
    * [Strings](https://rocket.rs/guide/v0.3/responses/#strings)
    * [Option](https://rocket.rs/guide/v0.3/responses/#option)
    * [Result](https://rocket.rs/guide/v0.3/responses/#result)

  * [Rocket Responders](https://rocket.rs/guide/v0.3/responses/#rocket-responders)
    * [Streaming](https://rocket.rs/guide/v0.3/responses/#streaming)
    * [JSON](https://rocket.rs/guide/v0.3/responses/#json)
    * [Templates](https://rocket.rs/guide/v0.3/responses/#templates)

* [State](https://rocket.rs/guide/v0.3/state/#state)
  * [Managed State](https://rocket.rs/guide/v0.3/state/#managed-state)
    * [Adding State](https://rocket.rs/guide/v0.3/state/#adding-state)
    * [Retrieving State](https://rocket.rs/guide/v0.3/state/#retrieving-state)
    * [Within Guards](https://rocket.rs/guide/v0.3/state/#within-guards)
    * [Unmanaged State](https://rocket.rs/guide/v0.3/state/#unmanaged-state)

  * [Databases](https://rocket.rs/guide/v0.3/state/#databases)
    * [Dependencies](https://rocket.rs/guide/v0.3/state/#dependencies)
    * [Managed Pool](https://rocket.rs/guide/v0.3/state/#managed-pool)
    * [Connection Guard](https://rocket.rs/guide/v0.3/state/#connection-guard)
    * [Usage](https://rocket.rs/guide/v0.3/state/#usage)

* [Fairings](https://rocket.rs/guide/v0.3/fairings/#fairings)
  * [Overview](https://rocket.rs/guide/v0.3/fairings/#overview)
    * [Attaching](https://rocket.rs/guide/v0.3/fairings/#attaching)
    * [Callbacks](https://rocket.rs/guide/v0.3/fairings/#callbacks)

  * [Implementing](https://rocket.rs/guide/v0.3/fairings/#implementing)
    * [Requirements](https://rocket.rs/guide/v0.3/fairings/#requirements)
    * [Example](https://rocket.rs/guide/v0.3/fairings/#example)

  * [Ad-Hoc Fairings](https://rocket.rs/guide/v0.3/fairings/#ad-hoc-fairings)

* [Testing](https://rocket.rs/guide/v0.3/testing/#testing)
  * [Local Dispatching](https://rocket.rs/guide/v0.3/testing/#local-dispatching)
  * [Validating Responses](https://rocket.rs/guide/v0.3/testing/#validating-responses)
  * [Testing "Hello, world!"](https://rocket.rs/guide/v0.3/testing/#testing-hello-world)
    * [Setting Up](https://rocket.rs/guide/v0.3/testing/#setting-up)
    * [Testing](https://rocket.rs/guide/v0.3/testing/#testing-1)

  * [Codegen Debug](https://rocket.rs/guide/v0.3/testing/#codegen-debug)

* [Configuration](https://rocket.rs/guide/v0.3/configuration/#configuration)
  * [Environment](https://rocket.rs/guide/v0.3/configuration/#environment)
  * [Rocket.toml](https://rocket.rs/guide/v0.3/configuration/#rocket-toml)
  * [Data Limits](https://rocket.rs/guide/v0.3/configuration/#data-limits)
  * [Extras](https://rocket.rs/guide/v0.3/configuration/#extras)
  * [Environment Variables](https://rocket.rs/guide/v0.3/configuration/#environment-variables)
  * [Configuring TLS](https://rocket.rs/guide/v0.3/configuration/#configuring-tls)

* [Pastebin](https://rocket.rs/guide/v0.3/pastebin/#pastebin)
  * [Finished Product](https://rocket.rs/guide/v0.3/pastebin/#finished-product)
  * [Getting Started](https://rocket.rs/guide/v0.3/pastebin/#getting-started)
  * [Index](https://rocket.rs/guide/v0.3/pastebin/#index)
  * [Uploading](https://rocket.rs/guide/v0.3/pastebin/#uploading)
    * [Unique IDs](https://rocket.rs/guide/v0.3/pastebin/#unique-ids)
    * [Processing](https://rocket.rs/guide/v0.3/pastebin/#processing)
    * [Upload Route](https://rocket.rs/guide/v0.3/pastebin/#upload-route)

  * [Retrieving Pastes](https://rocket.rs/guide/v0.3/pastebin/#retrieving-pastes)
  * [Conclusion](https://rocket.rs/guide/v0.3/pastebin/#conclusion)

* [Conclusion](https://rocket.rs/guide/v0.3/conclusion/#conclusion)
  * [Getting Help](https://rocket.rs/guide/v0.3/conclusion/#getting-help)
  * [What's next?](https://rocket.rs/guide/v0.3/conclusion/#what-s-next)

[](https://rocket.rs/guide/v0.3/#the-rocket-programming-guide "anchor")The Rocket Programming Guide
===================================================================================================

Welcome to Rocket!

This is the official guide. It is designed to serve as a starting point to writing web applications with Rocket and Rust. The guide is also designed to be a reference for experienced Rocket developers. This guide is conversational in tone. For concise and purely technical documentation, see the [API documentation](https://api.rocket.rs/v0.3).

The guide is split into several sections, each with a focus on a different aspect of Rocket. The sections are:

* **[Introduction](https://rocket.rs/guide/v0.3/introduction/):** introduces Rocket and its philosophy.
* **[Quickstart](https://rocket.rs/guide/v0.3/quickstart/):** presents the minimal steps necessary to run your first Rocket application.
* **[Getting Started](https://rocket.rs/guide/v0.3/getting-started/):** a gentle introduction to getting your first Rocket application running.
* **[Overview](https://rocket.rs/guide/v0.3/overview/):** describes the core concepts of Rocket.
* **[Requests](https://rocket.rs/guide/v0.3/requests/):** discusses handling requests: control-flow, parsing, and validating.
* **[Responses](https://rocket.rs/guide/v0.3/responses/):** discusses generating responses.
* **[State](https://rocket.rs/guide/v0.3/state/):** how to manage state in a Rocket application.
* **[Fairings](https://rocket.rs/guide/v0.3/fairings/):** provides an overview of Rocket's structured middleware.
* **[Testing](https://rocket.rs/guide/v0.3/testing/):** how to unit and integration test a Rocket application.
* **[Configuration](https://rocket.rs/guide/v0.3/configuration/):** how to configure a Rocket application.
* **[Pastebin](https://rocket.rs/guide/v0.3/pastebin/):** a tutorial on how to create a pastebin with Rocket.
* **[Conclusion](https://rocket.rs/guide/v0.3/conclusion/):** concludes the guide and discusses next steps for learning.

[](https://rocket.rs/guide/v0.3/#getting-help "anchor")Getting Help
-------------------------------------------------------------------

The official community support channels are the `#rocket` IRC channel on the [Mozilla IRC Server](https://wiki.mozilla.org/IRC) at `irc.mozilla.org` and the bridged [Rocket room on Matrix](https://riot.im/app/#/room/#mozilla_#rocket:matrix.org). If you're not familiar with IRC, we recommend chatting through [Matrix via Riot](https://riot.im/app/#/room/#mozilla_#rocket:matrix.org) or via the [Kiwi web IRC client](https://kiwiirc.com/client/irc.mozilla.org/#rocket). You can learn more about IRC via Mozilla's [Getting Started with IRC](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Getting_Started_with_IRC) guide.

* * *

[Introduction ►](https://rocket.rs/guide/v0.3/introduction/)

* * *

[© 2016-2025 Sergio Benitez](https://sergio.bz/)

![Image 10: Small Rocket Logo](https://rocket.rs/images/logo-small.svg)

[BACK TO TOP Δ](https://rocket.rs/guide/v0.3/#)

![Image 11: cloud](https://rocket.rs/images/cloud-0.png)![Image 12: cloud](https://rocket.rs/images/cloud-1.png)![Image 13: cloud](https://rocket.rs/images/cloud-2.png)
