# Source: https://fly.io/docs/about/cost-management/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Cost Management on Fly.io 

## [](#predicting-your-fly-io-bill-and-avoiding-surprises)[Predicting your Fly.io bill and avoiding surprises] 

Weâ€™ve done our best to make billing on Fly.io something you can reason about. Machines donâ€™t appear out of nowhere. If something is running, itâ€™s because you launched it, or you configured something that did. In general, when we talk about **autoscaling**, we mean starting or stopping machines youâ€™ve already defined. We donâ€™t quietly spin up extras in the background that turn into mystery charges on your bill. The idea is that your bill should always be traceable to something you can see, name, and plausibly explain when someone asks. If itâ€™s not, weâ€™re happy to help you sort it out.

**Need more help understanding your bill?** Reach out to us at <billing@fly.io>.

## [](#a-few-examples)[A few examples] 

So when youâ€™re budgeting, you can look at what youâ€™ve provisioned and do some quick math. Letâ€™s say youâ€™ve deployed three â€œshared-1x 1GBâ€? machines in `sjc`. Thatâ€™s \$20.37/month, tops. If you let them stop when idle, you might only pay for a few hours of computeâ€"but the worst-case scenario is still capped at that monthly rate.

Here are a few more grounded examples:

-   A **staging app** running in the `sjc` region with one `shared-1x 256MB` machine that auto-stops when idle might cost less than **\$1/month**. If you leave it running full-time, itâ€™s still only **\$2.32/month**.
-   A **queue worker** (also in `sjc`) that uses metrics-based autoscaling on `shared-1x 512MB` machines might average 3â€"5 machines running during busy hours. If those stay up for 50% of the month, youâ€™re looking at **\$5.72â€"9.52/month**, worst-case around **\$19 month** if they all run 24/7.

We recommend budgeting for the â€œalways-onâ€? cost. You can get under that number with auto-stop or bursty usage, but donâ€™t depend on it to hit your budget.

If your estimate seems high, the most predictable way to save money isnâ€™t fiddling with auto-stop/start settings (since any random request might spin a machine up again), but by justâ€¦running fewer machines. Or smaller ones.

**Want to play with numbers?** Try the [Fly.io pricing calculator](https://fly.io/calculator) to get a rough sense of what your setup might cost. For the full breakdown, hereâ€™s our [pricing page](/docs/about/pricing/).

## [](#metrics-based-autoscaling-can-affect-costs)[Metrics-based autoscaling can affect costs] 

There is one important exception to the rule that Fly.io doesnâ€™t create machines on your behalf. If you use the **metrics-based autoscaler**, for example to scale a background worker based on queue depth, it *can* create or destroy machines automatically.

**When can the metrics-based autoscaler create machines?** When you deploy and configure the [**Fly Autoscaler**](/docs/launch/autoscale-by-metric/), and use `FAS_CREATED_MACHINE_COUNT` instead of `FAS_STARTED_MACHINE_COUNT`, you're giving it permission to create and destroy machines on your behalf. It still uses the machine sizes and regions you specify, and anything it spins up counts toward your bill. [Read more in the docs](/docs/launch/autoscale-by-metric/).

## [](#other-stuff-to-watch-for)[Other Stuff to Watch For] 

A few more things that can quietly run up your bill if you're not paying attention:

-   **Bandwidth costs can add up.** Outbound data transfer is billed at \$0.02/GB in North America and Europe, with higher rates in some other regions. Ingress is free. If you're serving media, syncing large datasets, or replicating across regions, bandwidth can quietly become a big line item. [Learn about data transfer pricing.](/docs/about/pricing/#data-transfer-pricing)
-   **Volumes donâ€™t stop billing when your machines do.** Persistent volumes are billed hourly, whether or not your machine is running. That 3GB volume you forgot about in `fra`? It's still costing you. [Read about storage pricing here](/docs/about/pricing/#volumes).
-   **Volume snapshots will start billing in January 2026.** If you're using automatic volume snapshots as part of your backup strategy, just be aware: starting next year, theyâ€™ll be a billable feature. [Weâ€™ve announced the change](https://community.fly.io/t/we-are-going-to-start-charging-for-volume-snapshots-from-january-2026/26202) and will share more details well ahead of time.
-   **Managed services live outside your apps.** Fly's [Managed Postgres](/docs/mpg/overview/) (MPG), [Upstash Redis](/docs/upstash/redis/), and [Tigris object storage](/docs/tigris/) donâ€™t get deleted when you delete your apps. Youâ€™ll find them in your Dashboard. If you're cleaning up, double-check there too. We've seen people get surprised by bills from leftover services and databases they thought were gone.
-   **Dedicated public IPv4 addresses arenâ€™t free.** Each http app gets billed \$2/month if you assign it a dedicated public IPv4. If youâ€™ve got a bunch of apps or deploy previews per branch, this can sneak up on you.
-   **Internal-only apps still count.** Just because a Fly app doesnâ€™t serve web traffic doesnâ€™t mean itâ€™s free. Background workers, queue processors, cron jobs: they all run machines, and those still cost money.

## [](#understanding-free-usage-and-overages)[Understanding Free Usage and Overages] 

-   **Free allowances donâ€™t cap your bill.** We may give you free credits and usage allowances, especially when youâ€™re starting out or have a legacy billing plan. But thereâ€™s no soft ceiling. If you go over, weâ€™ll bill you. We don't support billing alerts (yet), so budget accordingly.
-   **There is no "free account/free tier" on Fly.io.** We do have a Free Trial program, which you can read about [here](/docs/about/free-trial/).
-   **Check your dashboard often.** To spot ballooning costs and overages before they become an issue, check the "current month to date bill" item in your dashboard.

## [](#related-reading)[Related Reading] 

Want to go deeper on scaling strategies, autoscaling configuration, or controlling concurrency? These docs walk through the mechanics:

-   [Autoscale Fly Machines](/docs/blueprints/autoscale-machines/) A practical guide to getting basic autoscaling working with Fly Machines. Covers HTTP-based scaling triggers.
-   [Metrics-based Autoscaling](/docs/launch/autoscale-by-metric/) This is the one that *can* create machines automatically, based on queue depth or another metric you specify. Use it wisely.
-   [Setting Concurrency Limits](/docs/blueprints/setting-concurrency-limits/) Shows how to keep your app from getting overwhelmed by too many concurrent requests. Especially useful if youâ€™re scaling horizontally.

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fabout%2Fcost-management.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Cost+Management+on+Fly.io%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fabout%2Fcost-management%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fabout%2Fcost-management.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Cost+Management+on+Fly.io%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/about/cost-management.html.md)