# Source: https://render.com/docs/deploy-elixir-cluster.md

# Deploy a Distributed Elixir Cluster

This is a guide to deploying a distributed Elixir cluster on Render using [libcluster](https://hexdocs.pm/libcluster), [Phoenix](https://phoenixframework.org) and [Mix releases](https://hexdocs.pm/mix/Mix.Tasks.Release.html). The cluster is set up to discover nodes automatically and keep the node list current as they join or leave the cluster.

We'll start off with a bare Phoenix project, modify it to use Mix releases and `libcluster` and deploy it on Render. The full source code for this example is available at https://github.com/render-examples/elixir_cluster.

## Create a Phoenix App

1. Create a new Phoenix app in the terminal. We don't need a database in this example, so we're passing the `--no-ecto` flag to `mix`.

   ```shell{outputLines:1,3}
   # install phx.new; feel free to change 1.4.9 to a different version
   mix archive.install hex phx_new 1.4.9
   # create a new Phoenix app
   mix phx.new elixir_cluster_demo --no-ecto # also fetch and install dependencies
   cd elixir_cluster_demo
   ```

2. Update `mix.exs` to add `libcluster` to deps.

   ```elixir
   defp deps do
     [ ...,
       {:libcluster, "~> 3.1"}
     ]
   ```

   Then run `mix deps.get` in your terminal to update dependencies.

## Configure Mix Releases

Create [runtime configuration](https://hexdocs.pm/phoenix/releases.html#runtime-configuration) needed for Mix releases.

1. Rename `config/prod.secret.exs` to `config/releases.exs`.
2. Change `use Mix.Config` in your new `config/releases.exs` file to `import Config`.
3. Uncomment the following line in `config/releases.exs`:

   ```elixir
   config :elixir_cluster_demo, ElixirClusterDemoWeb.Endpoint, server: true
   ```

4. Finally, update `config/prod.exs` to delete the line `import_config "prod.secret.exs"` at the bottom.

## Configure libcluster

Our setup will create nodes with names like `elixir-cluster-demo@10.200.30.4`, where the IP addresses are dynamic. Render assigns IPs to nodes when they first start, and every deploy results in a new node IP. This is where `libcluster` comes in: it enables [automatic cluster formation ](https://hexdocs.pm/libcluster/readme.html#features) through multiple configurable [cluster management strategies](https://hexdocs.pm/libcluster/readme.html#clustering).

Given dynamic node IPs, DNS is the best way to reliably form a cluster and keep it up to date. Consequently, we will use `libcluster`'s [DNS strategy](https://hexdocs.pm/libcluster/Cluster.Strategy.Kubernetes.DNS.html) for cluster formation.

Let's add `libcluster` to our production config. Add the lines below to `rel/prod.exs`.

```elixir
dns_name = System.get_env("RENDER_DISCOVERY_SERVICE")
app_name = System.get_env("RENDER_SERVICE_NAME")

config :libcluster, topologies: [
  render: [
    strategy: Cluster.Strategy.Kubernetes.DNS,
    config: [
      service: dns_name,
      application_name: app_name
    ]
  ]
]
```

Render automatically populates `RENDER_DISCOVERY_SERVICE` and `RENDER_SERVICE_NAME` based on the name of your service.

Finally, add `libcluster` to the application supervisor by adding the lines highlighted below to `application.ex`:

```elixir{3,6,7}
  def start(_type, _args) do
    # List all child processes to be supervised
    topologies = Application.get_env(:libcluster, :topologies) || []

    children = [
      # start libcluster
      {Cluster.Supervisor, [topologies, [name: ElixirClusterDemo.ClusterSupervisor]]},
      # Start the endpoint when the application starts
      ElixirClusterDemoWeb.Endpoint
      # Starts a worker by calling: ElixirClusterDemo.Worker.start_link(arg)
      # {ElixirClusterDemo.Worker, arg},
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: ElixirClusterDemo.Supervisor]
    Supervisor.start_link(children, opts)
  end
```

## Display Connected Nodes

Once everything is wired up, you can access the current node using `node()` and other nodes in the cluster using `Node.list()`.

Our sample app displays all connected nodes on the homepage. Edit the index view and template in your own app as shown in [this commit](https://github.com/render-examples/elixir_cluster/commit/a7bec265602ab3e038a8e7af5e8a6cd67eba3e8b).

## Update Your App for Render

Update `config/prod.exs` to change the highlighted line below.

```elixir{2}
config :elixir_cluster_demo, ElixirClusterDemoWeb.Endpoint,
  url: [host: "example.com", port: 80],
  cache_static_manifest: "priv/static/cache_manifest.json"
```

to this:

```elixir{2}
config :elixir_cluster_demo, ElixirClusterDemoWeb.Endpoint,
  url: [host: System.get_env("RENDER_EXTERNAL_HOSTNAME") || "localhost", port: 80],
  cache_static_manifest: "priv/static/cache_manifest.json",
```

Render populates `RENDER_EXTERNAL_HOSTNAME` for `config/prod.exs`.

> If you add a custom domain to your Render app, don't forget to change the host to your new domain.

## Create a Build Script

We need to run a series of commands to build our app on every push to our Git repo, and we can accomplish this with a build script. Create a script called `build.sh` at the root of your repo:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

# Initial setup
mix deps.get --only prod
MIX_ENV=prod mix compile

# Compile assets
npm install --prefix ./assets
npm run deploy --prefix ./assets
mix phx.digest

# Build the release and overwrite the existing release directory
MIX_ENV=prod mix release --overwrite
```

Make sure the script is executable before checking it into Git:

```shell
chmod a+x build.sh
```

## Build Your Release Locally

Compile your release locally by running `./build.sh`. The output should look like this:

```bash
Generated elixir_cluster_demo app
* assembling elixir_cluster_demo-0.1.0 on MIX_ENV=prod
* using config/releases.exs to configure the release at runtime
* skipping elixir.bat for windows (bin/elixir.bat not found in the Elixir installation)
* skipping iex.bat for windows (bin/iex.bat not found in the Elixir installation)

Release created at _build/prod/rel/elixir_cluster_demo!

    # To start your system
    _build/prod/rel/elixir_cluster_demo/bin/elixir_cluster_demo start

Once the release is running:

    # To connect to it remotely
    _build/prod/rel/elixir_cluster_demo/bin/elixir_cluster_demo remote

    # To stop it gracefully (you may also send SIGINT/SIGTERM)
    _build/prod/rel/elixir_cluster_demo/bin/elixir_cluster_demo stop

To list all commands:

    _build/prod/rel/elixir_cluster_demo/bin/elixir_cluster_demo
```

If everything looks good, push your changes to your repo. You can now deploy your app in production! 🎉

## Deploying to Render

1. Create a new *Web Service* on Render, and give Render permission to access your new repo.

2. Use the following values during creation:

   |                   |                                                                     |
   | ----------------- | ------------------------------------------------------------------- |
   | *Language*      | `Elixir`                                                            |
   | *Build Command* | `./build.sh`                                                        |
   | *Start Command* | `_build/prod/rel/elixir_cluster_demo/bin/elixir_cluster_demo start` |

   Also add the following environment variables to your web service:

   | Key               | Value                                                                                           |
   | ----------------- | ----------------------------------------------------------------------------------------------- |
   | `SECRET_KEY_BASE` | A sufficiently strong secret. You can generate a secret locally by running `mix phx.gen.secret` |

That's it! Your distributed Elixir web service will be live on your Render URL as soon as the build finishes.

You can add nodes to your cluster by increasing the number of instances for your service under *Settings*.

[image: Update Server Instance Count]

You should see the second node on the homepage as soon as the instance update is live.

[image: Screenshot of Elixir Cluster Nodes]

Congratulations! You've successfully set up distributed Elixir in production, and your cluster will automatically update as nodes are added or removed from it. 🎉

Read about [customizing Elixir and Erlang versions](elixir-erlang-versions) for your app.