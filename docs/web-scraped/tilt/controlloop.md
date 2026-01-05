# Tilt Documentation
# Source: https://docs.tilt.dev/controlloop.html
# Path: controlloop.html

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

#  Tilt's Control Loop

When someone first encounters Tilt, usually their mental modelâs something
like this:

![Magic](/assets/img/controlloop/02.jpg)

That is, write the Tiltfile, magic happens, and itâs all live.

For most people, this level of understanding is plenty. Tilt responds to your
changes, and the right code is always running in your cluster.

But sometimes you need to know a little more about whatâs going on:

  * Maybe for debugging.
  * Maybe for creating custom functionality.
  * Or maybe youâre just curious.

In this article, weâre going to clarify this flow, and show youâat a high
levelâwhat actually happens to go from Tiltfile to services running in
Kubernetes.

Consider watching this content in video format if you prefer:

## What is a resource?

On the cluster part of the diagram above, thatâs your application running in
Kubernetes. As far as Tilt is concerned, these objectsâand they can be pods,
jobs, deployments, ingresses, anythingâas well as any other bit of work Tilt
might have to doâ¦ theyâre organized into resources.

![Resources](/assets/img/controlloop/03.jpg)

Thatâs what those things on the Tilt sidebar really represent.

So a resource is any bundle of work managed by Tilt.

  * It can be a container image to build plus some Kubernetes YAML to deployâmaybe this is one of the microservices youâre working on.
  * It can be just Kubernetes YAML to deployâlike a database instance.
  * Or it can be a command to run on localhostâlike a script that generates some artifact, which you then sync into a running container.

Now how does Tilt know what your resources are, and how to execute them? That
happens in the Tiltfile.

## The Tiltfile

A Tiltfile, as you might know, is a configuration file written in Starlark, a
dialect of Python. Itâs real code and you can use conditionals, loops,
functions, and so on.

![Tiltfile](/assets/img/controlloop/01.jpg)

Now, this is important: The Tiltfile itself does _not_ execute anything in
your cluster. Instead, it stitches together all the information about your
resources, and relays them to the Tilt engine.

![Resources](/assets/img/controlloop/04.jpg)

For example, in the Tiltfile above weâre using the `k8s_yaml` function to
tell Tilt about Kubernetes objects that need deploying, and the `docker_build`
function to tell Tilt how to build images.

Letâs take the `k8s_yaml` call. It doesnât apply YAML to your cluster
directlyâinstead, it registers that YAML internally.

At the end of Tiltfile execution, Tilt will package that YAML into a resource
and send that resource to the Tilt engine, where it can then be applied.

In addition, Tilt has some heuristics to group related bits of work into the
same resource. If you tell Tilt to build a âmyserviceâ image, and give it
YAML to deploy an image called âmyserviceâ, Tilt puts two and two together
and groups those instructions into a single resource.

Lastly, Tilt watches the Tiltfile, and any files that feed into it. If Tilt
detects any changes that might affect the output of the Tiltfile, it evaluates
the Tiltfile again.

![Tiltfile Watch](/assets/img/controlloop/05.jpg)

## Applying resources

Now that we know what resources are, and how to define those resources in the
Tiltfile, letâs talk about _how_ Tilt executes those resources, and _when_
it does so.

![Resources](/assets/img/controlloop/07.jpg)

To execute a resource, the âhowâ depends on what the resource is. As we
discussed earlier, a resource can be:

  * an image and some YAML
  * just the YAML
  * a local command

So:

  * If itâs a local resource, run the command locally.
  * If image build instructions are present, build the image.
  * If Kubernetes YAML is present, deploy it to the cluster.
  * (And when configured, Tilt can modify a running container in place for faster updates.)

Now, a very important part of Tilt is that it updates your cluster in real
time. It is always running the most current code, and the most current
configuration. How does Tilt do that?

![Resource Watch](/assets/img/controlloop/06.jpg)

By watching for certain key events. Generally those are:

  * A change to the resourceâs definition in the Tiltfile.
  * A user manually triggering the execution of that resource.
  * Or change to a file that the resource cares about.

You might be wondering, how does Tilt know what files a resource cares about?

Explicitly, you can specify in the Tiltfile that a resource depends on certain
files and folders.

And implicitly, Tilt assumes that if youâre building an image and the
context is the âmyserviceâ directory, any file changes in that directory
will affect that resource.

## Summary

To wrap this up, letâs have a quick recap of Tiltâs control flow:

  * First, execute the Tiltfile in its entirety, and create resource definitions. Some of these are configured manually, and some Tilt uses heuristics to assemble.
  * Whenever the Tiltfile changes, re-execute it and update the internal resource definitions.
  * Next, the engine executes the resources, and if any resources contain Kubernetes objects, these end up deployed to your cluster.
  * Lastly, resources get updated whenever thereâs a triggering event. These can be a definition changing, a relevant file changing, or the user manually triggering the resource.

This knowledge should make it easier for you to debug your applications, and
to create custom functionality.

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/controlloop.md)







### Was this doc helpful?

Yes No

