# Tilt Documentation
# Source: https://docs.tilt.dev/index.html
# Path: index.html

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

#  Getting Started With Tilt

Kubernetes for Prod, Tilt for Dev

Modern apps are made of too many services. Theyâre everywhere and in
constant communication.

[Tilt](https://tilt.dev/) powers microservice development and makes sure they
behave! Run `tilt up` to work in a complete dev environment configured for
your team.

Tilt automates all the steps from a code change to a new process: watching
files, building container images, and bringing your environment up-to-date.
Think `docker build && kubectl apply` or `docker-compose up`.

# Get Tilt

Installing the `tilt` binary is a one-step command.

### macOS/Linux

    
    
    curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
    

### Windows

    
    
    iex ((new-object net.webclient).DownloadString('https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.ps1'))
    

## Finding the right manual

**Completely new to Tilt?**  
Watch our two minute explanation video and browse through [FAQs about
Tilt](/faq.html).  
Then head over to our [tutorial](/tutorial/index.html) to run Tilt yourself
for the very first time!

**Setting up Tilt for existing services?**  
We have best practice guides for:

  * [Plain Old Static HTML](/example_static_html.html)
  * [Go](/example_go.html)
  * [NodeJS](/example_nodejs.html)
  * [Python](/example_python.html)
  * [Java](/example_java.html)
  * [C#](/example_csharp.html)
  * [Bazel](/example_bazel.html)

**Optimizing your Tiltfile?**  
Search for the function you need in our [API reference](api.html).

## Watch: Tilt in Two Minutes

## Community

**Questions:** Join [the Kubernetes slack](http://slack.k8s.io) and find us in
the [#tilt](https://kubernetes.slack.com/messages/CESBL84MV/) channel. Or
[file an issue](https://github.com/tilt-dev/tilt/issues). For code snippets of
Tiltfile functionality shared by the Tilt community, check out [Tilt
Extensions](https://github.com/tilt-dev/tilt-extensions).

**Contribute:** Check out our [guidelines](https://github.com/tilt-
dev/tilt/blob/master/CONTRIBUTING.md) to contribute to Tiltâs source code.
To extend the capabilities of Tilt via new Tiltfile functionality, read more
about [Extensions](extensions.html).

**Follow along:** [@tilt_dev](https://twitter.com/tilt_dev) on Twitter. For
updates and announcements, follow [the blog](https://blog.tilt.dev) or
subscribe to [the newsletter](https://tilt.dev/subscribe).

**Help us make Tilt even better:** Tilt sends anonymized usage data, so we can
improve Tilt on every platform. Details in [âWhat does Tilt
send?â](http://docs.tilt.dev/telemetry_faq.html). If you find a security
issue in Tilt, see our [security policy](https://github.com/tilt-
dev/tilt/blob/master/SECURITY.md).

We expect everyone in our community (users, contributors, followers, and
employees alike) to abide by our [**Code of Conduct**](code_of_conduct.html).

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/index.md)







### Was this doc helpful?

Yes No

