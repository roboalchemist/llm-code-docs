# Source: https://docs.apify.com/platform/actors/development/actor-definition.md

# Actor definition

**Learn how to turn your arbitrary code into an Actor simply by adding an Actor definition directory.**

***

A single isolated Actor consists of source code and various settings. You can think of an Actor as a cloud app or service that runs on the Apify platform. The run of an Actor is not limited to the lifetime of a single HTTP transaction. It can run for as long as necessary, even forever.

Basically, Actors are programs packaged as [Docker images](https://hub.docker.com/), which accept a well-defined JSON input, perform an action, and optionally produce an output.

Actors have the following elements:

* The main **[actor.json](https://docs.apify.com/platform/actors/development/actor-definition/actor-json.md)** file contains **metadata** such as the Actor name, description, author, version, and links pointing to the other definition files below.
* **[Dockerfile](https://docs.apify.com/platform/actors/development/actor-definition/dockerfile.md)** which specifies where is the Actor's source code, how to build it, and run it.
* **Documentation** in the form of a **README.md** file.
* **[Input](https://docs.apify.com/platform/actors/development/actor-definition/input-schema.md)** and **[dataset schemas](https://docs.apify.com/platform/actors/development/actor-definition/dataset-schema.md)** that describe what input the Actor requires and what results it produces.
* Access to an out-of-box **[storage](https://docs.apify.com/platform/storage.md)** system for Actor data, results, and files.

The documentation and the input/dataset schemas make it possible for people to easily understand what the Actor does, enter the required inputs both in the user interface or API, and integrate the Actor's results with their other workflows. Actors can easily call and interact with each other, enabling building more complex systems on top of simple ones.

The Apify platform provides an open [API](https://docs.apify.com/api/v2.md), cron-style [scheduler](https://docs.apify.com/platform/schedules.md), [webhooks](https://docs.apify.com/platform/integrations/webhooks.md), and [integrations](https://docs.apify.com/platform/integrations.md) to services such as Zapier or Make, which make it easy for users to integrate Actors with their existing workflows. Anyone is welcome to [publish Actors](https://docs.apify.com/platform/actors/publishing.md) in [Apify Store](https://apify.com/store), and you can even [monetize your Actors](https://docs.apify.com/platform/actors/publishing/monetize.md).

Actors can be developed and run locally and then easily deployed to the Apify platform using the [Apify CLI](https://docs.apify.com/cli) or a [GitHub integration](https://docs.apify.com/platform/integrations/github.md). For more details, see the [Deployment](https://docs.apify.com/platform/actors/development/deployment.md) section.

> **To get a better idea of what Apify Actors are, visit [Apify Store](https://apify.com/store), and try out some of them!**
