# Tilt Documentation
# Source: https://docs.tilt.dev/debug_faq.html
# Path: debug_faq.html

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

#  Why is Tilt broken?

Tilt is broken. What should you do?

There are a lot of ways to get help, depending on how willing you are to get
your hands dirty.

* * *

### Where can I ask questions?

Join [the Kubernetes slack](http://slack.k8s.io) and find us in the
[#tilt](https://kubernetes.slack.com/messages/CESBL84MV/) channel. The entire
Tilt team is there, and can answer any questions you have.

Or you can [file an issue](https://github.com/tilt-dev/tilt/issues).

* * *

### Why does Tilt crash on startup?

Run:

    
    
    tilt doctor
    

Tilt will print out status information:

  * Tilt version
  * Operating system
  * Docker host and version
  * Kubernetes version
  * Type of Kubernetes cluster (Docker for Mac, Microk8s, etc)
  * Container runtime

This can help you figure out what cluster Tilt thinks youâre using. Itâs
usually the first thing we ask for when people file issues with Tilt.

* * *

### What info should I send when I need help?

A snapshot is a link that you can send to someone that will allow them to
interactively explore your current Tilt state. This is useful for async
debugging and adding context to bug reports. They look like pretty much just
like Tilt, but frozen in time:

<https://cloud.tilt.dev/snapshot/AYSV59gLhM3GVMuuR28=>

A snapshot is a frozen âmoment-in-timeâ version of the Tilt UI. In a
snapshot you can drill in to specific services, see alerts and Kubernetes
events. Pretty much anything you can do in normal Tilt, you can do in a
snapshot!

This is also helpful to send along with bug reports.

For more information, see â[Share Errors and Cluster State with
Snapshots](snapshots.html)â.

* * *

### Why does my image build fail in Tilt when it succeeds with `docker build`?

Run:

    
    
    tilt docker -- build ARGS
    

This will run Docker the same way that Tilt runs Docker.

Tilt automatically enables optimizations that you may not be using by default.
For example, if you are using minikube and run:

    
    
    tilt docker -- build -t image-name .
    

Tilt may print:

    
    
    Running Docker command as:
    DOCKER_HOST=tcp://192.168.99.100:2376 DOCKER_CERT_PATH=/home/nick/.minikube/certs DOCKER_TLS_VERIFY=1 docker build -t image-name .
    

because itâs running against Minikubeâs Docker instance, not your Docker
instance.

* * *

### Why is Tilt using so much CPU or memory?

Please file an issue if Tilt is being a resource hog! Weâve made it a lot
better in the last few months but there may still be builds that cause
problems.

As of v0.10.26, Tilt exposes the standard Go pprof hooks over
[HTTP](https://golang.org/pkg/net/http/pprof/).

To look at a 30-second CPU profile:

    
    
    go tool pprof http://localhost:10350/debug/pprof/profile?seconds=30
    

To look at the heap profile:

    
    
    go tool pprof http://localhost:10350/debug/pprof/heap
    

This opens a special REPL that lets you explore the data. Type `web` in the
REPL to see a CPU graph.

For more information on pprof, see [the Go pprof
guide](https://github.com/google/pprof/blob/master/doc/README.md).

* * *

### What does Tilt think is happening right now?

The internal Tilt engine is implemented as a control loop, just like
Kubernetes.

Tilt watches lots of different inputs (your Tiltfile, your local source files,
and your Kubernetes cluster) for changes. The control loop records these
changes in a central state store. Then, Tilt kicks off updates to your cluster
based on the state store.

That means all the state Tilt knows about lives in a single place. And you can
inspect it!

While Tilt is running in one terminal, open another terminal and run:

    
    
    tilt dump engine
    

Tilt will print a JSON representation of everything it knows about your build
state and your cluster state.

The Tilt UI has a similar control loop. Run:

    
    
    tilt dump webview
    

to see the complete state of the Tilt web UI.

* * *

### How can I keep track of Tilt usage on my team?

Tilt has an experimental Tiltfile function: `experimental_telemetry_cmd`.

This command takes a string which is a command to run. Tilt will exec this
command every minute and pass it on STDIN a series of [OpenTelemetry
spans](https://github.com/open-telemetry/opentelemetry-
specification/blob/master/specification/overview.md#distributed-tracing) in
the form of newline-separated JSON objects. These spans representing all of
the userâs activity in the last minute, and you can manipulate and ingest
them as you will.

For example, you could write a script to send Tiltâs telemetry output to
Honeycomb, and invoke it via `experimental_telemetry_cmd` like so:

    
    
    experimental_telemetry_cmd("/path/to/honeycomb_ingest.py")
    

The argument to this function is just a shell command, so thereâs a lot of
flexibility. If for example you wanted to send Tiltâs telemetry output to a
script run via a Docker image, you could call:

    
    
    experimental_telemetry_cmd("docker run --env USER -i my-telemetry-image")
    

The JSON that gets passed looks like this:

    
    
    {"SpanContext":{"TraceID":"00000000000000000000000000000000","SpanID":"0000000000000000","TraceFlags":1},"ParentSpanID":"0000000000000000","SpanKind":1,"Name":"tilt.dev/usage/update","StartTime":"2019-12-11T12:18:30.702255-05:00","EndTime":"2019-12-11T12:18:31.920728054-05:00","Attributes":null,"MessageEvents":null,"Links":null,"Status":0,"HasRemoteParent":false,"DroppedAttributeCount":0,"DroppedMessageEventCount":0,"DroppedLinkCount":0,"ChildSpanCount":0}
    {"SpanContext":{"TraceID":"00000000000000000000000000000000","SpanID":"0000000000000000","TraceFlags":1},"ParentSpanID":"0000000000000000","SpanKind":1,"Name":"tilt.dev/usage/update","StartTime":"2019-12-11T12:18:31.922581-05:00","EndTime":"2019-12-11T12:18:32.257773437-05:00","Attributes":null,"MessageEvents":null,"Links":null,"Status":0,"HasRemoteParent":false,"DroppedAttributeCount":0,"DroppedMessageEventCount":0,"DroppedLinkCount":0,"ChildSpanCount":0}
    

Here are some example scripts that report these spans as:

  * [A datadog time series](https://github.com/jazzdan/datadog_example/blob/master/example.rb)
  * [A statsd reporter](https://github.com/jazzdan/statsd_example/blob/master/main.rb)

This is an experimental feature designed for larger companies.

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/debug_faq.md)







### Was this doc helpful?

Yes No

