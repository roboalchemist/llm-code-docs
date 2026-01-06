# Tilt Documentation
# Source: https://docs.tilt.dev/telemetry_faq.html
# Path: telemetry_faq.html

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

#  What does Tilt send?

Tilt sends anonymized data about how you use it.

The first time you visit the web UI, Tilt nudges you to explicitly opt in or
out of analytics.

You can opt-in from the command-line with:

    
    
    tilt analytics opt in
    

You can change your mind at any time by running:

    
    
    tilt analytics opt out
    

and restarting Tilt.

* * *

### Why does Tilt want analytics?

Weâre a small company trying to make Tilt awesomer.

We can do this better if we understand which features people are using and
which bugs people are running into.

* * *

### Where does the analytics data go?

Tilt sends telemetry data to our in-house analytics ingestion server at
`events.windmill.build`.

This data may be stored in managed database services (like Google Cloud) or
managed analytics services (like Datadog) to help us analyze it.

We will not resell or give away this data to advertisers.

* * *

### What kinds of data does Tilt record if I opt-in?

Weâre interested in how people, in aggregate, use Tilt â which Tiltfile
built-ins people use, what parts of the Web UI people interact with, etc.

We donât want to collect data about you or your project.

When possible, strings that may contain information about your project (repo
names, service names, directory names) are hashed to protect your privacy.

The hashing system isnât foolproof. Itâs possible that some of the data we
collect could include snippets of data about your project (e.g. that you have
a service named `deathray-backend` or an error message that includes the
string it failed to parse). You should probably not opt-in if youâre working
on a classified project.

* * *

### Can you give some examples?

Hereâs an example of the data Tilt sends when you run `tilt up` with
analytics enabled:

    
    
    {
      "watch": "true",
      "version": "0.10.18-dev",
      "user": "a62525469776f5b299733bdc95718d47",
      "os": "linux",
      "name": "tilt.cmd.up",
      "mode": "auto",
      "machine": "8c581ff2fc00c6a47ecbd50abe47fb40",
      "git.origin": "3QLdKIWhsYTCsPI0vtsx6Q=="
    }
    

Hereâs an example of the data Tilt sends when a Tiltfile loads:

    
    
    {
      "version": "0.10.18-dev",
      "user": "a62525469776f5b299733bdc95718d47",
      "tiltfile.invoked.docker_build.arg.ref": "3",
      "tiltfile.invoked.docker_build.arg.live_update": "3",
      "tiltfile.invoked.docker_build.arg.ignore": "3",
      "tiltfile.invoked.docker_build.arg.dockerfile": "3",
      "tiltfile.invoked.docker_build.arg.context": "3",
      "tiltfile.invoked.docker_build": "3",
      "tiltfile.invoked.default_registry.arg.name": "1",
      "tiltfile.invoked.default_registry": "1",
      "os": "linux",
      "name": "tilt.tiltfile.loaded",
      "machine": "8c581ff2fc00c6a47ecbd50abe47fb40",
      "git.origin": "3QLdKIWhsYTCsPI0vtsx6Q=="
    }
    

Weâve talked about adding a command that displays everything Tilt is sending
in a part of the web UI, for transparency. If youâre interested in this, let
us know.

* * *

### What other ways can I control analytics?

You can disable analytics in the current environment by running:

    
    
    export TILT_DISABLE_ANALYTICS="true"
    

Tilt also respects the DO_NOT_TRACK environment variable used for [other
TUI/console apps](https://consoledonottrack.com/):

    
    
    export DO_NOT_TRACK="1"
    

You can also enable analytics in the Tiltfile by adding:

    
    
    analytics_settings(enable=True)
    

The Tiltfile setting overrides user preferences. Itâs intended for devtools
teams opting-in all users on the team.

The environment setting overrides both the Tiltfile and user preferences.

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/telemetry_faq.md)







### Was this doc helpful?

Yes No

