# Source: https://fly.io/docs/elixir/the-basics/troubleshooting/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Troubleshooting 

Some problems are harder to diagnose because they deal with [Elixir releases![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgY2xhc3M9ImlubGluZS1mbGV4IG1sLTIgc2VsZi1jZW50ZXIgcG9pbnRlci1ldmVudHMtbm9uZSIgdmlld2JveD0iMCAwIDE0IDE0Ij48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS4zIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMi42MjUgNC44MjVjMC0yLjMxOC0xLjg4Mi00LjItNC4yLTQuMmgtMy42YTQuMjAyIDQuMjAyIDAgMDAtNC4yIDQuMnYzLjZjMCAyLjMxOCAxLjg4MiA0LjIgNC4yIDQuMmgzLjZjMi4zMTggMCA0LjItMS44ODIgNC4yLTQuMnYtMy42ek00LjQ4MiA4LjYyNWw0LTQiPjwvcGF0aD48cGF0aCBkPSJNOC40ODIgNy4yOTdWNC42MjVINS44MSI+PC9wYXRoPjwvZz48L3N2Zz4=)](https://hexdocs.pm/mix/master/Mix.Tasks.Release.html) or Docker build problems. Typically, you don't run the application that way locally, so you only encounter those problems when it's time to deploy.

Here are a few tips to help diagnose and identify problems.

-   Run `mix release` locally on your project.
-   Build the Dockerfile locally to verify it builds correctly. `docker build .`
-   Check the `:prod` config in `config/runtime.exs`, which is not used locally. Carefully review it.
-   Run `fly logs` to check server logs.

For diagnosing database app issues, refer to the [Postgres Monitoring](/docs/postgres/managing/monitoring/) information.

Here's a quick hit list of commands to help:

-   Run `fly logs -a <pg-db-name>` to check database app's server logs.
-   Run `fly checks list -a <pg-db-name>` to check the database app's health.
-   Run `fly status -a <pg-db-name> --all` to see if any VMs failed.
-   Run `fly vm status <id> -a <pg-db-name>` to debug a specific VM.

## [](#diagnosis-tip)[Diagnosis Tip] 

------------------------------------------------------------------------

Most difficulties center around application config. Applications generated with an older version of Phoenix are configured differently than a newly generated app. If you have problems like connecting to your database, usually an IPv6 configuration update is needed.

The internal networks at Fly.io use a IPv6 addresses. Elixir/OTP needs some config to work smoothly.

One way to identify an issue is to generate a new Elixir application using a current version of Phoenix. Deploy that to Fly.io with a database. With that, you have a local working example to compare against. Don't worry, you can easily [`destroy`](/docs/flyctl/apps-destroy/) the test app when you're ready to.

Suggested files to pay attention to when looking for config differences.

-   `config/config.exs`
-   `config/prod.exs`
-   `config/runtime.exs`
-   `Dockerfile`
-   `mix.exs`

## [](#not-enough-connections)[Not Enough Connections] 

------------------------------------------------------------------------

A common failure mode is the application exhausting the number of free connections, your default `fly.toml` has the following settings:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
  [services.concurrency]
    hard_limit = 50
    soft_limit = 25
    type = "connections"
```

Setting the `hard_limit` and `soft_limit` closer to your needs will free up the number of live connections per node. A safe starting point could be 1000 for the hard*limit and 975 for the soft*limit. The "right" amount depends on how much data is actively stored in the LiveView processes. That value will vary for each application.

## [](#clustering)[Clustering] 

------------------------------------------------------------------------

Here are some troubleshooting tips when working with [Clustering](/docs/elixir/the-basics/clustering/).

When using [IEx to remote into a running application](/docs/elixir/the-basics/iex-into-running-app/) to diagnose connection issues, note if you see this warning when connecting:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
warning: the --remsh option will be ignored because IEx is running on limited shell
```

When that warning is present, the Elixir node we are connecting to is not the remote running node. A new node was launched when the remote shell request was ignored. Refer to the [docs here about the `--pty`](/docs/elixir/the-basics/iex-into-running-app/) option.

Another indication of this situation is when typing `Node.self()`, the name of the node is returned with a prefix similar to "rem-ea46-". Example:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
:"rem-ea46-hello_elixir@fdaa:0:1da8:a7b:115:5641:7e85:2"
```

A working remote shell will return a node name more like this:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
:"hello_elixir@fdaa:0:1da8:a7b:115:5641:7e85:2"
```

### [](#testing-node-connectivity)[Testing Node Connectivity] 

Using `libcluster` is an easy way to [auto-cluster](#clustering) an Elixir application. However, going through the process manually can help diagnose issues.

We can open two terminals locally on our machine. In terminal A, we get an [IEx terminal](/docs/elixir/the-basics/iex-into-running-app/) to one node. Then in terminal B, we get an IEx terminal to a different node.

In each terminal, we can ask the node for it's name:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
Node.self
```

Then, taking the response node in terminal A, we can explicitly try to connect through terminal B (on the other node).

That command might look like this:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
Node.connect(:"result-from-terminal-A@ipvs-address")
```

If the result is `true` then it either connected to the other node or we entered into the wrong terminal and it says it's connected to itself.

If we received a `true` response, we can check the list of connected nodes using this command:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
Node.list()
```

An empty list means is has no connections.

During the process, make note of any logged messages that might help explain why the two nodes can't connect.

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Felixir%2Fthe-basics%2Ftroubleshooting.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Troubleshooting%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Felixir%2Fthe-basics%2Ftroubleshooting%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Felixir%2Fthe-basics%2Ftroubleshooting.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Troubleshooting%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/elixir/the-basics/troubleshooting.html.md)