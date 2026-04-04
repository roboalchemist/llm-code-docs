# Tilt Documentation
# Source: https://docs.tilt.dev/tutorial/3-tilt-ui.html
# Path: tutorial/3-tilt-ui.html

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

#  Tilt UI

## Tilt Tutorial

## Launching the Web UI

In your terminal window running `tilt demo`, press `(Spacebar)`. Tilt will
open your default browser to the Tilt UI. (Or navigate there directly in your
preferred browser using the URL from the terminal.)

## Resource Overview

The Resource Overview is the first thing you see when you open the Tilt UI.
You can always return to it by clicking the Tilt logo in the upper left
corner.

![Tilt UI resource overview](/assets/docimg/tutorial/tilt-ui-table.png)

This view shows all your resources (services) at a glance, grouped by their
[resource labels](/tiltfile_concepts.html#resource-groups).

The Resource Overview is essential to get a quick view of your projectâs
entire state and offers critical info at a glance:

  * **Update and Resource Status**

If you look at the `api` resource row, youâll see both the update and
runtime status. Since this is a âKubernetes Deployâ type resource, the
update included building the image and `kubectl apply`ing it the cluster. The
runtime status reflects the Podâs current state in the cluster. e.g. Is it
running and passing readiness checks?

  * **Pod ID**

Copy a Pod ID to your clipboard in one click, so you can interact with it as
needed via `kubectl` or other tools.

  * **Widgets**

[Custom buttons](/buttons.html) let you run any one-off tasks (unit tests,
lint, etc.) youâve configured for a resource.

  * **Endpoints**

Remembering port numbers when youâve got a bunch of services can be a
challenge. Endpoints gives you quick access to all your Tilt managed port
forwards. You can also define custom endpoints for relevant external
references such as a wiki page so that theyâre never more than a click away.

  * **Trigger Mode**

By default, resources in Tilt are updated whenever a relevant file changes.
Itâs possible to change the default behavior on a per-resource basis (or
globally) in the Tiltfile with [manual update
control](/manual_update_control.html). The trigger mode toggles for each
resource in the UI make it easy to quickly pause and resume automatic updates
to it.

Even if a resource is in manual mode, itâs always possible to trigger an
update on-demand!

From here, click the endpoint link on the âwebâ resource to open the
frontend for the Tilt Avatars app.

![Using "Endpoints" from Tilt UI Resource Overview to open the Tilt Avatars
frontend](/assets/docimg/tutorial/tilt-ui-web-endpoint.gif)

Finished making an awesome avatar? ð»

Click on the âapiâ resource to navigate to the Resource Details view for
the respective resource.

## Resource Details

The central focus of the Resource Detail view is logs, but all the information
from the Resource Overview such as [custom buttons](/buttons.html), endpoints,
and pod IDs are available here as well.

Try clicking the âTrigger Updateâ (â») button next to the âwebâ
resource to run a manual update, which will re-build and re-deploy the Pod:
![Triggering an update for the "web" resource in the Tilt UI Resource Detail
view](/assets/docimg/tutorial/tilt-ui-trigger-update.gif)

> ð The âAll Resourcesâ link in the navbar will show logs for all
> services at once instead of a single service

### Log Filtering

Tilt provides several mechanisms to focus your logs:

  * **Source**

By default, Tilt shows both build/update and runtime logs interleaved. Itâs
possible to restrict this to a single source. For example, if youâre trying
to fix an error during your resource start, it might be helpful to temporarily
hide the build logs to reduce noise as you make changes.

  * **Level**

In addition to unifying your logs, Tilt collects errors and warnings from
different tools such as Docker build errors, Kubernetes events, and more. You
can quickly filter the view to just these important events including the
surrounding context by clicking `... (more)`.

  * **Keyword/Regex Filter**

If youâve ever tried to catch an error whiz by while tailing logs, you might
have found yourself copying the output to a text editor to search through it.
Tilt lets you non-destructively filter by keywords or regex match.

![Filtering logs via source, level, and keyword in the Tilt UI Resource Detail
view](/assets/docimg/tutorial/tilt-ui-logs.gif)

## What Else?

You can extend the Tilt UI with [custom buttons](/buttons.html) to run common
tasks such as unit tests or lint with one-click. Buttons support parameterized
inputs and the log output goes directly to the relevant resource, so you
donât have to jump back and forth between a terminal and the Tilt UI.

Otherwise, the Tilt UI is designed to be unobtrusive and run in the
background, notifying you only when something needs your attention.

Multi-service development might be complex, but we aim for simplicity in the
Tilt UI!

[ â 2\. Launching & Managing Resources ](/tutorial/2-tilt-up.html) [ 4\.
Code. Update. Repeat. â ](/tutorial/4-code-update-repeat.html)

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/3-tilt-ui.md)







### Was this doc helpful?

Yes No

