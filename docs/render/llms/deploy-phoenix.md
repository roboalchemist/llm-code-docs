# Source: https://render.com/docs/deploy-phoenix.md

# Deploy a Phoenix App on Render

This guide walks through deploying a [Phoenix](https://phoenixframework.org) application on Render.

The finished code for this example is available on [GitHub](https://github.com/render-examples/phoenix_hello).

## Getting started

Create a new Phoenix app in the terminal. We don't need a database for this example, so pass the `--no-ecto` flag to `mix`:

```shell
mix archive.install hex phx_new
mix phx.new phoenix_hello --no-ecto # also fetch and install dependencies
cd phoenix_hello
```

## Create a build script

We need to run a series of commands to build our app on every push to our Git repo, which we can accomplish with a build script. Create a script named `build.sh` at the root of your repo:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

# Initial setup
mix deps.get --only prod
MIX_ENV=prod mix compile

# Compile assets
# Make sure tailwind and esbuild are installed
MIX_ENV=prod mix assets.build
# Build minified assets
MIX_ENV=prod mix assets.deploy

# Create server script, Build the release, and overwrite the existing release directory
MIX_ENV=prod mix phx.gen.release
MIX_ENV=prod mix release --overwrite
```

Make sure the script is executable before you commit it:

```shell
chmod a+x build.sh
```

## Update your app for Render

Update `config/runtime.exs` to change the highlighted line below:

```elixir
host = System.get_env("PHX_HOST") || "example.com" # highlight-line
port = String.to_integer(System.get_env("PORT") || "4000")
```

to this:

```elixir
host = System.get_env("RENDER_EXTERNAL_HOSTNAME") || "localhost" # highlight-line
port = String.to_integer(System.get_env("PORT") || "4000")
```

Render populates `RENDER_EXTERNAL_HOSTNAME` for `config/runtime.exs`.

> If you add a [custom domain](custom-domains) to your Render app, don't forget to change the host to your new domain.

## Build and test your release locally

Compile your release locally by running `./build.sh`. The end of the output should look like this:

```shell{outputLines:2-23}
./build.sh

* assembling phoenix_hello-0.1.0 on MIX_ENV=prod
* using config/runtime.exs to configure the release at runtime
* skipping elixir.bat for windows (bin/elixir.bat not found in the Elixir installation)
* skipping iex.bat for windows (bin/iex.bat not found in the Elixir installation)

Release created at _build/prod/rel/phoenix_hello

    # To start your system
    _build/prod/rel/phoenix_hello/bin/phoenix_hello start

Once the release is running:

    # To connect to it remotely
    _build/prod/rel/phoenix_hello/bin/phoenix_hello remote

    # To stop it gracefully (you may also send SIGINT/SIGTERM)
    _build/prod/rel/phoenix_hello/bin/phoenix_hello stop

To list all commands:

    _build/prod/rel/phoenix_hello/bin/phoenix_hello
```

Test your release by running the following command and navigating to http://localhost:4000.

```bash
SECRET_KEY_BASE=`mix phx.gen.secret` _build/prod/rel/phoenix_hello/bin/server
```

> You might need to run `mix deps.get` locally to enable `phx.gen.secret`, because it's a dev dependency instead of a prod dependency. You should add/commit your `mix.lock` file before running this.

> You might notice the start command is different from the output of `build.sh`. The `phx.gen.release` command in the build script creates a wrapper for launching your application that include setting the PHX_SERVER variable, so a webserver will start. You can also use the start command from the `build.sh` output, but you will need to set `PHX_SERVER` to `true` in the environment variables if you do.

If everything looks good, push your changes to your repo. Next, let's deploy your app to Render!

## Deploy to Render

1. In the [Render Dashboard](https://dashboard.render.com), create a new *web service* and connect your Phoenix app's repo.

2. Set the following values during service creation:

   | Setting           | Value                                      |
   | ----------------- | ------------------------------------------ |
   | *Language*      | `Elixir`                                   |
   | *Build Command* | `./build.sh`                               |
   | *Start Command* | `_build/prod/rel/phoenix_hello/bin/server` |

3. Add the following environment variable to your web service:

| Key | Value |
| --- | --- |
| `SECRET_KEY_BASE` | A sufficiently strong secret. You can generate one from your local project directory with the following command: ```shell{outputLines:2-2}
   mix phx.gen.secret
   ``` |

That's it! Your Phoenix web service will be live at its `onrender.com` subdomain as soon as the deploy finishes.

Read about [setting Elixir and Erlang/OTP versions](elixir-erlang-versions) for your app.