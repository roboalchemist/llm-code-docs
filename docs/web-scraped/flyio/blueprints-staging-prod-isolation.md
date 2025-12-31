# Source: https://fly.io/docs/blueprints/staging-prod-isolation/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Staging and production isolation 

<figure class="flex justify-center">
<img src="/static/images/staging-prod-iso.png" class="w-full max-w-lg mx-auto" alt="Illustration by Annie Ruygt of a gateway and buildings" />
</figure>

## [](#overview)[Overview] 

You want to isolate your production environment from your test or staging environments by limiting production access to the smallest possible group. You can get dependable isolation by using multiple organizations. Organization access is invitation-only and orgs are isolated from one another at a low level by our private networking architecture: every organization has its own [private network](/docs/networking/private-networking/) by default.

All Fly.io accounts start with a "personal" organization. You can create as many organizations as you need, not just for different environments, but also for different projects or clients.

Before you create a new organization, here's what you need to know:

-   You can consolidate billing for multiple organizations under a a single parent organization, or you can create regular organizations with separate payment methods and billing. Learn more about [unified billing](/docs/about/billing/#unified-billing).
-   You invite or remove members in each organization separately.
-   An organization can have multiple apps and those apps can communicate with each other securely over the org's private network.

Adjust the pattern to fit your needs. For example:

-   personal organization: the org you started with, and the one you keep for personal projects
-   staging organization: `<project>-staging` used for development and testing
-   production organization: `<project>-production` used for your production app

## [](#work-with-multiple-organizations)[Work with multiple organizations] 

It's best if you use one Fly.io account to manage all your organizations, so you can access them without logging in and out. App names are unique across the Fly.io platform, so your staging and production apps will have different names and their own `fly.toml` files for configuration.

### [](#manage-organizations-in-your-dashboard)[Manage organizations in your dashboard] 

To create a new org from the [dashboard]((https://fly.io/dashboard/)), select **Create new organization** from the **Organization** dropdown.

To view or send invites to members, use the **Organization** dropdown to choose an org, then go to **Team**.

### [](#manage-organizations-with-flyctl)[Manage organizations with flyctl] 

To create new organizations and invite or remove members, use [`fly orgs` flyctl commands](/docs/flyctl/orgs/).

When you have more than one org, flyctl prompts you to choose an organization when required. You can run commands on a specific app in any org using the `--app` option if you aren't in the app's project source directory in your terminal.

## [](#other-kinds-of-isolation-and-access-control)[Other kinds of isolation and access control] 

-   When you only need app isolation within an org, you can use [custom private networks](/docs/networking/custom-private-networks/) to isolate apps from one another by creating an app with `fly apps create` and the `--network` option.
-   When you want user or 3rd-party access control, you can use [deploy](https://community.fly.io/t/deploy-tokens/11895) and [org-scoped tokens](https://community.fly.io/t/org-scoped-tokens/13194) to limit access to apps or orgs.

## [](#related-reading)[Relatedâ€¯reading] 

-   [Going to production checklist](/docs/apps/going-to-production/) A broad checklist for productionâ€'readiness that includes isolating environments and access control.\
-   [Staging environments with GitHub actions](/docs/django/advanced-guides/staging-environments-with-github-actions/) A practical guide focused on using GitHub Actions to deploy dedicated staging environments. Complements the isolation pattern nicely.

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fblueprints%2Fstaging-prod-isolation.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Staging+and+production+isolation%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fblueprints%2Fstaging-prod-isolation%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fblueprints%2Fstaging-prod-isolation.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Staging+and+production+isolation%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/blueprints/staging-prod-isolation.html.md)