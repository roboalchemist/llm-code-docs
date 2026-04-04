# Tilt Documentation
# Source: https://docs.tilt.dev/tutorial/index.html
# Path: tutorial/index.html

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

#  First Look at Tilt

This tutorial is designed to introduce the key concepts of Tilt.

If youâre new to containerized development, donât panic: this tutorial
focuses on Tilt. We wonât dive into the internals of `Dockerfile` or
Kubernetes YAML.

Throughout the tutorial, weâll refer to the [`tilt-
avatars`](https://github.com/tilt-dev/tilt-avatars) project. The full source
is available on [GitHub](https://github.com/tilt-dev/tilt-avatars) to refer to
or checkout locally to follow along interactively.

> ð¡ In the first section, weâll make sure youâve got the necessary
> prerequisites installed!

## Table of Contents

  1. **Preparation (Optional)**

If you want to follow along interactively, youâll need Tilt, Docker, and the
sample project source code. We know it can be daunting, so weâve tried to
streamline the experience and will get you going from scratch in under 10
minutes!

  2. **Launching & Managing Resources**

Say hello to your new best friend: `tilt up`. This section introduces the Tilt
control loop and will forever change the way you think about development
tools.

  3. **Tilt UI**

Welcome to the command center. The Tilt UI aggregates logs across all your
services, provides at at-a-glance view of your dev environmentâs state, and
so much more. Did we mention it also looks â¨fantasticâ¨ while doing so?

  4. **Code. Update. Repeat.**

See Tilt in action and learn how Tilt optimizes your dev experience by
building the right thing at the right time.

  5. **Smart Rebuilds with Live Update**

Syncing file changes is just the start. Tiltâs Live Update provides the
flexibility to support all languages and frameworks even if they donât offer
native hot reload support. The only downside is you wonât have time for
[office sword fights](https://xkcd.com/303/) anymore.

## Whatâs Next?

Ready to use Tilt in your _own_ project? Fantastic! The [Write a Tiltfile
Guide](/tiltfile_authoring.html) will apply what youâll learn in this
tutorial to write a `Tiltfile` from scratch and supercharge your dev
environment.

[ 1\. Preparation (optional) â ](/tutorial/1-prerequisites.html)

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/index.md)







### Was this doc helpful?

Yes No

