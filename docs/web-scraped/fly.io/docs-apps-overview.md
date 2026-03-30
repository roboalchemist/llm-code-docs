# Source: https://fly.io/docs/apps/overview

Title: Fly Apps overview

URL Source: https://fly.io/docs/apps/overview

Published Time: Thu, 26 Feb 2026 22:12:59 GMT

Markdown Content:
Fly Apps overview · Fly Docs
===============

[Skip to content](https://fly.io/docs/apps/overview#main-content-start)

[](https://fly.io/)[](https://fly.io/docs/)

[**Need a Logo?** View Our Brand Assets](https://fly.io/docs/about/brand/)

Open main menu[](https://fly.io/)[](https://fly.io/docs/)

[Pricing](https://fly.io/pricing/)[Support](https://fly.io/docs/about/support/)

[Sign In](https://fly.io/app/sign-in/)[Sign Up](https://fly.io/app/sign-up/)

[Docs Index](https://fly.io/docs/)[Apps on Fly.io](https://fly.io/docs/apps/)
*   [Fly Apps overview](https://fly.io/docs/apps/overview/)
*   [Get app info](https://fly.io/docs/apps/info/)
*   [Restart an app](https://fly.io/docs/apps/restart/)
*   [Delete an app](https://fly.io/docs/apps/delete/)
*   [Move an app between orgs](https://fly.io/docs/apps/move-app-org/)

[Fly Launch](https://fly.io/docs/launch/)Toggle Fly Launch section
*   [Launch a new app](https://fly.io/docs/launch/create/)
*   [Deploy an app](https://fly.io/docs/launch/deploy/)
*   [Scale Machine CPU and RAM](https://fly.io/docs/launch/scale-machine/)
*   [Scale the number of Machines](https://fly.io/docs/launch/scale-count/)
*   [Autostop/autostart Machines](https://fly.io/docs/launch/autostop-autostart/)
*   [Autoscale based on metrics](https://fly.io/docs/launch/autoscale-by-metric/)
*   [Add volume storage](https://fly.io/docs/launch/volume-storage/)
*   [Use process groups](https://fly.io/docs/launch/processes/)
*   [Deploy with GitHub Actions](https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/)
*   [Deploy monorepo apps](https://fly.io/docs/launch/monorepo/)
*   [Troubleshoot when a host is down](https://fly.io/docs/apps/trouble-host-unavailable/)
*   [App config reference (fly.toml)](https://fly.io/docs/reference/configuration/)

Secrets Toggle Secrets section
*   [Set runtime secrets](https://fly.io/docs/apps/secrets/)
*   [Set build secrets](https://fly.io/docs/apps/build-secrets/)

Production Apps Toggle Production Apps section
*   [Going to production](https://fly.io/docs/apps/going-to-production/)
*   [App availability and resiliency](https://fly.io/docs/apps/app-availability/)
*   [Fine-tune and benchmark apps](https://fly.io/docs/apps/fine-tune-apps/)
*   [App handover guide](https://fly.io/docs/apps/app-handover-guide/)
*   [Concurrency settings](https://fly.io/docs/apps/concurrency/)

--- title: "Fly Apps overview" layout: docs toc: false nav: apps redirect_from: /docs/reference/apps/ --- A Fly App is an abstraction for a group of Fly Machines running your code on Fly.io. You can create and manage your app as a whole using [Fly Launch](/docs/launch/), but you can also have a Fly App with individual Machines running tasks or user code. For a quick primer on Fly Launch, Fly Machines, and Fly Apps, see [Fly.io essentials](/docs/getting-started/essentials/). ## A Fly App can be almost anything From an admin point of view, a Fly App is just a group of Machines (with optional attached volumes) that belongs to one organization. From a developer point of view, a Fly App might be: * a fullstack application (or just part of one) * a database * a few Machines running tasks, or a bunch of Machines, all with different configs, doing things you want them to do * anything you can think of doing with fast-launching Machines, including [GPU Machines](/docs/gpus/) for AI/ML workloads All the apps in your organization can communicate over a [private network](/docs/networking/private-networking/), so it’s also possible to have multiple apps working together as one system. ## Components of a Fly App Fly Apps include: * app configuration * provisioned resources * Anycast IP addresses * certificates * custom domains * secrets * Fly Volumes (optional) Fly Apps run on flyd. Learn more about how flyd works and how it came to be in the blog post: [Carving the Scheduler Out of Our Orchestrator](https://fly.io/blog/carving-the-scheduler-out-of-our-orchestrator/). ## Ways to create an app There might be an infinite number of potential apps you can run on Fly.io, but there are only a few ways to create one. ### Create and deploy with Fly Launch Fly Launch is perfect for most apps and databases. Use Fly Launch to create your app and then manage the whole lifecycle, from starting to scaling to changing and redeploying. [Get started](/docs/getting-started/) with Fly Launch or learn more about using [Fly Launch](/docs/launch/) to create, configure, deploy, and scale your app. ### Create an app manually Most of the time, all you need is [Fly Launch](/docs/launch/) to create and manage your app. But you can skip all the handy launch scanners and resource provisioning Fly Launch offers and use the `fly apps create` command or the Machines API to create an app and then piece it together. You can get a [`fly.toml` config file](/docs/reference/configuration/) from an example app or hand-craft one yourself. Or if you don't need app-wide config, you can use the Fly App to hold the Machines you plan to spin up individually based on a particular image. Using the `fly apps create` command is useful when deploying our [autoscaler app](/docs/launch/autoscale-by-metric/), or example apps created by others, that already have `fly.toml` and Dockerfiles ready to go. Creating apps with the Machines API might be the right choice if you want to create apps for your own users with pre-defined or custom `fly.toml` files. For more information, see the [`fly apps create` docs](/docs/flyctl/apps-create/) and the [create App resource docs](/docs/machines/api/apps-resource/#create-a-fly-app). <div class="note icon"> **Tip:** When you [create a Machine with `fly machine run`](/docs/machines/flyctl/fly-machine-run/) without specifying an app to put it in, you automatically get a new app at the same time. This scenario might be useful when you're spinning up individual Machines on-demand for multiple users or tasks. </div>

[Docs](https://fly.io/docs/)[Apps on Fly.io](https://fly.io/docs/apps)Fly Apps overview
Fly Apps overview
=================

A Fly App is an abstraction for a group of Fly Machines running your code on Fly.io. You can create and manage your app as a whole using [Fly Launch](https://fly.io/docs/launch/), but you can also have a Fly App with individual Machines running tasks or user code.

For a quick primer on Fly Launch, Fly Machines, and Fly Apps, see [Fly.io essentials](https://fly.io/docs/getting-started/essentials/).

[](https://fly.io/docs/apps/overview#a-fly-app-can-be-almost-anything)A Fly App can be almost anything
------------------------------------------------------------------------------------------------------

From an admin point of view, a Fly App is just a group of Machines (with optional attached volumes) that belongs to one organization.

From a developer point of view, a Fly App might be:

*   a fullstack application (or just part of one) 
*   a database 
*   a few Machines running tasks, or a bunch of Machines, all with different configs, doing things you want them to do 
*   anything you can think of doing with fast-launching Machines, including [GPU Machines](https://fly.io/docs/gpus/) for AI/ML workloads 

All the apps in your organization can communicate over a [private network](https://fly.io/docs/networking/private-networking/), so it’s also possible to have multiple apps working together as one system.

[](https://fly.io/docs/apps/overview#components-of-a-fly-app)Components of a Fly App
------------------------------------------------------------------------------------

Fly Apps include:

*   app configuration 
*   provisioned resources 
*   Anycast IP addresses 
*   certificates 
*   custom domains 
*   secrets 
*   Fly Volumes (optional) 

Fly Apps run on flyd. Learn more about how flyd works and how it came to be in the blog post: [Carving the Scheduler Out of Our Orchestrator](https://fly.io/blog/carving-the-scheduler-out-of-our-orchestrator/).

[](https://fly.io/docs/apps/overview#ways-to-create-an-app)Ways to create an app
--------------------------------------------------------------------------------

There might be an infinite number of potential apps you can run on Fly.io, but there are only a few ways to create one.

### [](https://fly.io/docs/apps/overview#create-and-deploy-with-fly-launch)Create and deploy with Fly Launch

Fly Launch is perfect for most apps and databases. Use Fly Launch to create your app and then manage the whole lifecycle, from starting to scaling to changing and redeploying. [Get started](https://fly.io/docs/getting-started/) with Fly Launch or learn more about using [Fly Launch](https://fly.io/docs/launch/) to create, configure, deploy, and scale your app.

### [](https://fly.io/docs/apps/overview#create-an-app-manually)Create an app manually

Most of the time, all you need is [Fly Launch](https://fly.io/docs/launch/) to create and manage your app. But you can skip all the handy launch scanners and resource provisioning Fly Launch offers and use the `fly apps create` command or the Machines API to create an app and then piece it together.

You can get a [`fly.toml` config file](https://fly.io/docs/reference/configuration/) from an example app or hand-craft one yourself. Or if you don’t need app-wide config, you can use the Fly App to hold the Machines you plan to spin up individually based on a particular image.

Using the `fly apps create` command is useful when deploying our [autoscaler app](https://fly.io/docs/launch/autoscale-by-metric/), or example apps created by others, that already have `fly.toml` and Dockerfiles ready to go.

Creating apps with the Machines API might be the right choice if you want to create apps for your own users with pre-defined or custom `fly.toml` files.

For more information, see the [`fly apps create` docs](https://fly.io/docs/flyctl/apps-create/) and the [create App resource docs](https://fly.io/docs/machines/api/apps-resource/#create-a-fly-app).

**Tip:** When you [create a Machine with `fly machine run`](https://fly.io/docs/machines/flyctl/fly-machine-run/) without specifying an app to put it in, you automatically get a new app at the same time. This scenario might be useful when you’re spinning up individual Machines on-demand for multiple users or tasks.

Copy page as markdown or[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fapps%2Foverview.html.markerb)

[Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Fly+Apps+overview%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fapps%2Foverview%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fapps%2Foverview.html.markerb%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Fly+Apps+overview%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/apps/overview.html.markerb)
