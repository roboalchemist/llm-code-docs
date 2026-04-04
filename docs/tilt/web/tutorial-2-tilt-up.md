# Tilt Documentation
# Source: https://docs.tilt.dev/tutorial/2-tilt-up.html
# Path: tutorial/2-tilt-up.html

  * [ Getting Started ](/index.html) [ Getting Started ](/docs_nav_gettingstarted.html)
  * [ Guides ](/tiltfile_authoring.html) [ Guides ](/docs_nav_guides.html)
  * [ Tiltfile & CLI ](/api.html) [ Tiltfile & CLI ](/docs_nav_reference.html)
  * [ Tilt API ](https://api.tilt.dev) [ Tilt API ](https://api.tilt.dev)

Learn About Tilt

    

  * [ Getting Started ](/)
  * [ Is Tilt right for me? ](/product_faq.html)

First Look at Tilt

    

  * [ Overview ](/tutorial/index.html)
  * [ 1\. Preparation (optional) ](/tutorial/1-prerequisites.html)
  * [ 2\. Launching & Managing Resources ](/tutorial/2-tilt-up.html)
  * [ 3\. Tilt UI ](/tutorial/3-tilt-ui.html)
  * [ 4\. Code. Update. Repeat. ](/tutorial/4-code-update-repeat.html)
  * [ 5\. Smart Rebuilds with Live Update ](/tutorial/5-live-update.html)

Quick Links

    

  * [ Install ](/install.html)
  * [ Upgrade ](/upgrade.html)
  * [ Tiltfile Snippets ](/snippets.html)
  * [ Editor Support new ](/editor.html)

How Does Tilt Work?

    

  * [ The Control Loop ](/controlloop.html)
  * [ Choosing a Local Dev Cluster ](/choosing_clusters.html)
  * [ Local vs Remote Services ](/local_vs_remote.html)

FAQs

    

  * [ Frequently Asked Questions ](/faq.html)
  * [ Why is Tilt broken? ](/debug_faq.html)
  * [ What does Tilt send? ](/telemetry_faq.html)

#  Launching & Managing Resources

## Tilt Tutorial

## Tilt Avatars

We made [Tilt Avatars](https://github.com/tilt-dev/tilt-avatars) so you can
try Tilt without first setting it up for your own project.

Tilt Avatars consists of a Python web API backend to generate avatars, and a
JavaScript SPA (single page app) frontend. **It doesnât matter if youâre
not a Python or JavaScript guru** â you wonât need to deeply understand
the project code to learn about the `Tiltfile` and other Tilt concepts.

![Randomized Tilt avatar generation](/assets/docimg/tutorial/tilt-avatars.gif)

> **We know that no two projects are alike!**
>
> This project uses `Dockerfile`s with Docker as the build engine and
> `kubectl`-friendly YAML files. But thatâs only a small subset of Tilt
> functionality.
>
> Even if youâre using other technologies (e.g. Helm, CRDs, `podman`), we
> recommend starting here to learn the Tilt fundamentals.
>
> Once youâre comfortable with how Tilt works, weâve got comprehensive
> guides on `Tiltfile` authoring that cover these topics and much more!

## Run `tilt up` for the First Time

Tilt brings consistency to your development not only due to ensuring a
reproducible dev-environment-as-code, but launching any Tilt project is the
same with the `tilt up` command, so you always have a familiar starting point.
`tilt up` starts the Tilt control loop, which weâll explore in more detail
in a moment.

For this tutorial, however, weâre going to use a special `tilt demo`
command, which will perform a few steps:

  1. Create a temporary, local Kubernetes development cluster in Docker
  2. Clone the [Tilt Avatars](https://github.com/tilt-dev/tilt-avatars) sample project
  3. Launch a `tilt up` session for the sample project using the temporary Kubernetes cluster
  4. Clean everything up on exit ð§¹

Run the following command in your terminal to get started:

    
    
    tilt demo
    

You should see output similar to the following in your terminal: ![Running
tilt up in a Terminal window shows "Tilt started on http://localhost:3366/"
message](/assets/docimg/tutorial/tilt-up-cli.gif)

First, open the sample project directory in your preferred editor so that you
can make changes in the following steps.

Once youâve got the sample project open, return focus to the terminal window
and press `(Spacebar)`, and the Tilt UI will be opened in your default
browser.

In the next section, weâll explain the Tilt UI. But first, letâs dissect
whatâs happening in the background.

> **Already Have a Local Kubernetes Cluster? (Advanced)**
>
> You can clone the sample project and run `tilt up` directly:
>  
>  
>     git clone https://github.com/tilt-dev/tilt-avatars.git
>     cd tilt-avatars/
>     tilt up
>  
>
> Once finished, run `tilt down` from the `tilt-avatars` directory to clean
> up.

## `Tiltfile`

When you run `tilt up`, Tilt looks for a special file named `Tiltfile` in the
current directory, which defines your dev-environment-as-code.

A `Tiltfile` is written in
[Starlark](https://docs.bazel.build/versions/main/skylark/language.html), a
simplified dialect of Python.

> ð Not a Python expert? No worries. Our guides have lots of examples, so
> you can copy & paste your way to success!

Because your `Tiltfile` is a program, you can configure it with familiar
constructs like loops, functions, and arrays. This makes the `Tiltfile` more
extensible than a configuration file format like JSON or YAML, which requires
hard-coding all possible options upfront.

When Tilt executes the `Tiltfile`:

  1. Built-in functions like [`k8s_yaml`](/api.html#api.k8s_yaml) and [`docker_build`](/api.html#api.docker_build) register information with the Tilt engine
  2. Tilt uses the resulting configuration to assemble resources to build and deploy
  3. Tilt watches **relevant** source code files so it can trigger an update of the associated resource(s)

Within Tilt, the `Tiltfile` is itself a resource, so **you can even modify
your`Tiltfile` and see the changes without restarting Tilt**!

![Sample Tiltfile code](/assets/docimg/tutorial/tiltfile.png)

Later on, weâll explore how Tilt makes it possible to optimize this process
even more. You can skip container re-builds and Pod re-deployments entirely
via [Smart Rebuilds with Live Update](./5-live-update.html).

(If youâre curious, go ahead and open the [`tilt-avatars`
Tiltfile](https://github.com/tilt-dev/tilt-avatars/blob/main/Tiltfile) and
read through it. We wonât tell anyone you peeked.)

For now, thatâs all you need to know!

## On Resources

A âresourceâ is a bundle of work managed by Tilt. For example: a Docker
image to build + a Kubernetes YAML to apply.

> ð¶âð«ï¸ **Resources donât have to be containers!**
>
> Tilt can also [manage locally-executed commands](/local_resource.html) to
> provide a unified experience no matter how your code runs.

Resource bundling is **automatic** in most cases: Tilt finds the relationship
between bits of work (e.g. `docker build` \+ `kubectl apply`). When thatâs
not sufficient, `Tiltfile` functions like
[`k8s_resource`](/api.html#api.k8s_resource) let you configure resources on
top of what Tilt does automatically.

Because Tilt assembles multiple bits of work into a single resource, itâs
much easier to determine status and find errors across update (build/deploy)
and runtime.

### Update Status

Whenever you run `tilt up` or change a source file, Tilt determines which
resources need to be changed to bring them up-to-date.

To execute these updates, Tilt might:

  * Compile code locally on your machine (e.g. `make`)
  * Build a container image (e.g. `docker build`)
  * Deploy a modified K8s object or Helm chart (e.g. `kubectl apply -f` or `helm install`)

![Resource pane showing an update error](/assets/docimg/tutorial/tilt-ui-
update-status.png)

Tilt knows which files correspond to a given resource and update action. It
wonât re-build a container just because you changed a Pod label, or re-
compile your backend when youâve only edited some JSX.

> ð¥ï¸ When you `tilt up`, if your services are already running and
> havenât changed, Tilt wonât unnecessarily re-deploy them!

### Runtime Status

Unfortunately, just because it builds does not mean it works.

In Tilt, the runtime status lets you know whatâs happening with your code
_after_ itâs been deployed.

![Resource pane showing a runtime error](/assets/docimg/tutorial/tilt-ui-
runtime-status.png)

More importantly, Tilt lets you know _why_. Thereâs a lot of ways things can
go wrong, and Tilt will save you from playing â20 Questions with
`kubectl`.â

## The Control Loop

Tilt is based around the idea of a [control loop](/controlloop.html). This
gives you real-time, circular feedback: something watches, something reacts,
and equilibrium is maintained.

This is intentionally more âhands-freeâ than other dev tools. Traditional
build systems like `make` are oriented around tasks that are invoked on-demand
by the user. Even many service-oriented development tools like `docker-compose
up` donât _react_ to changes once started. Newer tools, such as Webpack,
often include hot module reload, but have limitations. (For example, changes
to `webpack.config.js` require a manual restart.)

![Diagram of Tilt's control loop architecture](/assets/img/controlloop/06.jpg)

Some examples of what Tilt handles for you:

  * Source code file changes â sync to running container
  * Dependency changes (e.g. `package.json`) â sync to running container and then run code in the container (e.g. `npm install`)
  * Build spec changes (e.g. `Dockerfile`) â re-build container image + re-deploy
  * Deployment spec changes (e.g. `app.yaml`) â reconcile deployment state (e.g. `kubectl apply -f ...`)
  * `Tiltfile` changes â re-evaluate and create new resources, modify existing, and delete obsolete as needed

**So, once youâve run`tilt up`, you can focus on your code and let Tilt
continuously react to your changes without worrying if theyâre the
ârightâ type of changes.**

This has other benefits: for example, when you run `tilt up`, Tilt wonât re-
deploy any services that are already running and up-to-date!

If youâd like a more in-depth look at Tiltâs control loop, check out
[Tiltâs Control Loop Demystified](/controlloop.html).

[ â 1\. Preparation (optional) ](/tutorial/1-prerequisites.html) [ 3\. Tilt
UI â ](/tutorial/3-tilt-ui.html)

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/2-tilt-up.md)







### Was this doc helpful?

Yes No

