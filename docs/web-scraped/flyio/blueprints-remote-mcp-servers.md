# Source: https://fly.io/docs/blueprints/remote-mcp-servers/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Deploying Remote MCP Servers 

![Illustration by Annie Ruygt of bird working at their computer while drinking coffee](/static/images/remote-mpc.png)

## [](#overview)[Overview] 

The Model Context Protocol (MCP) is a fun new way to give LLMs new powers. Originally developed by Anthropic, the protocol has since been adopted by OpenAI (with Google Gemini support in the works at the time of writing).

The protocol defines a standardized way of connecting tools and providing additional context to LLMs, not dissimilar to the way USB provides a standardized way to connect computers to peripherals and devices. Fly Machines are tightly isolated VMs that are perfect for running MCP servers.

This guide will help you understand, at a very high level, how to build, deploy, and connect remote MCP servers on Fly.io. Keep in mind that this is an nascent, still-emerging protocol â€" details are subject to change. For specific implementation details, the [Model Context Protocol](https://modelcontextprotocol.io/) site is the authoritative source of truth (complete with [a handy .txt version for LLM prompting](https://modelcontextprotocol.io/llms-full.txt)).

We've also started to integrate some MCP tooling into the `flyctl` that should give you a more concrete sense of how you might deploy MCP servers on Fly.io (read more in [this community forum post](https://community.fly.io/t/running-mcps-on-and-with-fly-io/24588)). Note that our MCP implementation is experimental and may still have sharp edges!

## [](#remote-mcp-servers)[Remote MCP Servers] 

MCP to date has been largely local-only, but the protocol also [specs out transports](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports) for remote MCP servers. Remote MCP servers solve a bunch of problems:

-   Easier to update a centralized server instead of dispersed, local packages
-   You can give MCP clients persistent connections that don't evaporate when someone closes their laptop
-   Securely sandbox MCP server activity in case the robots go rogue

## [](#single-tenant-or-multi-tenant)[Single Tenant or Multi-tenant] 

There are broadly two patterns you might want to follow when deploying a remote MCP server to Fly.io:

1.  Multi-tenant MCP server (one app, many users)
2.  Single-tenant MCP servers (one app per user)

We're partial to the single-tenant pattern â€" it ensures proper isolation, and also helps with minimize your Fly.io bill: unused Machines can stop and start as needed, so you won't waste resources on idle users (more about why we think one app per customer is the right pattern [here](https://fly.io/docs/machines/guides-examples/one-app-per-user-why/)). `fly-replay` makes it easy to route requests to the correct app / Fly Machine (see more detail about this pattern in [Per-user Dev Environments with Fly Machines](https://fly.io/docs/blueprints/per-user-dev-environments/)).

## [](#multi-tenant-mcp-servers)[Multi-tenant MCP Servers] 

![Diagram showing multi-tenant MCP server architecture on Fly.io](/static/images/docs-mcp-multi-tenant.webp)

You'll need two main components:

1.  **MCP-Remote Shim (optional)**: Tiny client-side proxy that connects local MCP clients to your remote servers (only needed if the MCP client doesn't support auth and / or streamable HTTP requests to a remote MCP server). Handles authentication via a secret shared between the shim and the router app (authentication could be a simple API token, username + password, or a full OAuth dance). Securely stores and refreshes tokens as needed. To see an example, try the experimental `fly mcp proxy` command in the `flyctl`. This sets up a local proxy that forwards MCP client requests to a remote URL (more details in [the docs](https://fly.io/docs/flyctl/mcp) and [the community forum](https://community.fly.io/t/running-mcps-on-and-with-fly-io/24588)).
2.  **MCP Server App**: This runs the actual MCP goodness and authenticates requests from the MCP client. Should have a single streamable HTTP endpoint path for MCP client connections, as well as any specific business logic or other integrations. To try our implementation, include the experimental `fly mcp wrap` command in the Dockerfile for your MCP server app. This instantiates a lightweight HTTP server to receive requests forwarded from the local MCP client via `fly mcp proxy` (more details in [the docs](https://fly.io/docs/flyctl/mcp) and [the community forum](https://community.fly.io/t/running-mcps-on-and-with-fly-io/24588)).

## [](#single-tenant-mcp-servers)[Single-tenant MCP Servers] 

![Diagram showing single-tenant MCP server architecture on Fly.io](/static/images/docs-mcp-single-tenant.webp)

There are three main components:

1.  **Router App**: Receives requests from the MCP client and handles auth, then routes requests to per-user apps + Fly Machines with `fly-replay`. See [Connecting to User Machines](/docs/blueprints/connecting-to-user-machines/) for details on implementing the routing pattern. Optionally handles user management and permissions. You can use the experimental `fly mcp wrap` command in the Dockerfile of your router app to instantiate a lightweight HTTP server to receive requests forwarded from a local MCP client (more details in [the docs](https://fly.io/docs/flyctl/mcp) and [the community forum](https://community.fly.io/t/running-mcps-on-and-with-fly-io/24588)). Note that `fly mcp wrap` does not handle request routing â€" you'll have to implement that separately.
2.  **MCP Server Apps**: Per-user (or per-team) apps that run the actual MCP goodness. Should have a single streamable HTTP endpoint path for MCP client connections, as well as any specific business logic or other integrations.
3.  **MCP-Remote Shim (optional)**: Tiny client-side proxy that connects local MCP clients to your remote servers (only needed if the MCP client doesn't support auth and / or streamable HTTP requests to a remote MCP server). Handles authentication via a secret shared between the shim and the router app (authentication could be a simple API token, username + password, or a full OAuth dance). Securely stores and refreshes tokens as needed. To see an example, try the experimental `fly mcp proxy` command in the `flyctl`, which sets up a local proxy that forwards MCP client requests to a remote URL (more details in [the docs](https://fly.io/docs/flyctl/mcp) and [the community forum](https://community.fly.io/t/running-mcps-on-and-with-fly-io/24588)).

## [](#how-users-experience-it)[How Users Experience It] 

From your users' perspective, the experience should be delightfully simple:

1.  They add a new MCP server to their MCP client with a simple one-liner
2.  If needed, the user is walked through an authentication flow (ie a browser window pops open to kick off the OAuth dance or provide an API key)
3.  After logging in, the MCP client can now access all the tools you've exposed
4.  The connection persists across restarts without re-authentication

## [](#taking-it-further)[Taking It Further] 

If you'd like your MCP servers to connect to third party OAuth APIs without having to directly handle API tokens, consider using [ssokenizer](https://github.com/superfly/ssokenizer) (or [tokenizer](https://github.com/superfly/tokenizer) for generic, non-OAuth flows).

## [](#related-reading)[Related reading] 

-   [Model Context Protocol (MCP) Documentation](/docs/mcp/) Learn more in our reference for MCP: what it is, how it works, and how to deploy servers.\
-   [Connecting to User Machines](/docs/blueprints/connecting-to-user-machines/) Find out about patterns for routing from a central router app to perâ€'user apps/machines via `flyâ€‘replay`, which is useful when you build singleâ€'tenant MCP setups.\
-   [Launchingâ€¯MCP Servers with flyctl](/docs/flyctl/mcp-server/) Read about the experimental `fly mcp server` command: how to start a local or remote MCP server using `flyctl`, including flags and usage.\

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fblueprints%2Fremote-mcp-servers.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Deploying+Remote+MCP+Servers%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fblueprints%2Fremote-mcp-servers%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fblueprints%2Fremote-mcp-servers.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Deploying+Remote+MCP+Servers%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/blueprints/remote-mcp-servers.html.md)