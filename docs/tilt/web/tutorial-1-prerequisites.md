# Tilt Documentation
# Source: https://docs.tilt.dev/tutorial/1-prerequisites.html
# Path: tutorial/1-prerequisites.html

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

#  Preparation (Optional)

## Tilt Tutorial

For this tutorial, weâll focus on Tilt fundamentals by walking through a
sample project.

Our sample project uses Docker for building container images and Kubernetes
for running them. However, itâs possible to use Tilt without Docker or
Kubernetes! Tilt is incredibly flexible and supports a variety of ways to
build and run your services during local development.

We wonât actually dive into a Dockerfile or Kubernetes YAML, since thatâs
out of scope for this introduction.

To follow along interactively, youâll need to have Docker and Tilt installed
on your machine.

Prefer not to download additional tools? You can still follow along on the web
- go ahead and skip to the [next section](./2-tilt-up.html)!

> ðââï¸ **Not using Kubernetes or Docker?**
>
> Weâve got plenty of guides for using Tilt with Helm, podman, local
> processes, and more to help you get started after learning the Tilt
> fundamentals from this tutorial.

## Install Tilt

On macOS/Linux, weâve got an install script that will use
[Homebrew](https://brew.sh) if available (and a direct download otherwise):

    
    
    curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
    

On Windows, weâve got an install script that will use
[Scoop](https://scoop.sh/) if available (and a direct download otherwise):

    
    
    iex ((new-object net.webclient).DownloadString('https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.ps1'))
    

If youâd rather install manually or via another method, refer to the guide
on [Alternative Installations](/install.html#alternative-installations).

## Install Docker

Docker provides comprehensive [install
instructions](https://docs.docker.com/get-docker/) for all supported OSes and
Linux distributions:

  * [Docker Desktop for Mac](https://docs.docker.com/desktop/mac/install/)
  * [Docker Desktop for Windows](https://docs.docker.com/desktop/windows/install/) (including WSL)
  * Docker for Linux 
    * [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    * [Direct from binary](https://docs.docker.com/engine/install/binaries/)
    * [All other distributions](https://docs.docker.com/engine/install/#server)
    * Convenience script (auto-detects distribution): 
          
          curl -fsSL https://get.docker.com | sh
          

> ð¡ On Linux, following the [Manage Docker as a non-root
> user](https://docs.docker.com/engine/install/linux-postinstall/#manage-
> docker-as-a-non-root-user) post-install guide is suggested so that you
> donât have to run Tilt with `sudo`. (Please take careful note of the
> security considerations outlined in the guide.)

A quick way to test out your Docker install is to run the `hello-world`
container:

    
    
    docker run --rm hello-world
    

You should see some output from Docker as it downloads the `hello-world` image
followed by a greeting message with some information about Docker. If you are
having trouble, Docker provides troubleshooting guides for
[macOS](https://docs.docker.com/desktop/mac/troubleshoot/) and
[Windows](https://docs.docker.com/desktop/windows/troubleshoot/).

[ â Overview ](/tutorial/index.html) [ 2\. Launching & Managing Resources
â ](/tutorial/2-tilt-up.html)

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/1-prerequisites.md)







### Was this doc helpful?

Yes No

