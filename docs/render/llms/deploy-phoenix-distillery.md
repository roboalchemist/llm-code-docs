# Source: https://render.com/docs/deploy-phoenix-distillery.md

# Deploy a Phoenix App with Distillery

This is a guide to deploying [Phoenix](https://phoenixframework.org) projects on Render using [Distillery](https://hexdocs.pm/distillery/home.html).

We'll start off with a bare Phoenix project with [Ecto](https://hexdocs.pm/ecto), modify it to use Distillery, and deploy it on Render. The full source code for this tutorial is available at https://github.com/render-examples/phoenix-distillery.

## Create a Phoenix App with Distillery

1. Create a new Phoenix app in the terminal:

   ```shell
   mix phx.new phoenix_distillery # also fetch and install dependencies
   cd phoenix_distillery
   ```

2. Update `mix.exs` to add Distillery to deps:

   ```elixir
   defp deps do
     [ ...,
       {:distillery, "~> 2.0"}
     ]
   ```

   Then run `mix deps.get` in your terminal to update dependencies.

## Configure Distillery

1. Let's configure Distillery for production. Update the `Endpoint` config in `config/prod.exs` so it looks like this:

   ```elixir
   config :phoenix_distillery, PhoenixDistilleryWeb.Endpoint,
     cache_static_manifest: "priv/static/cache_manifest.json",
     server: true, # critical for Phoenix to run
     root: ".",
     version: Application.spec(:phoenix_distillery, :vsn)
   ```

   Read more about [Distillery configuration](https://hexdocs.pm/distillery/guides/phoenix_walkthrough.html#distillery-configuration).

   We're not going to check secrets into source control. Instead, we're going to manage them in production with Render environment variables. So let's delete the line at the end referring to `prod.secret.exs`.

   ```elixir
   import_config "prod.secret.exs" # delete me
   ```

   And delete the file `config/prod.secret.exs`.

2. You're now ready to initialize your Distillery release.

   ```shell
   mix distillery.init
   ```

   This will create `rel/config.exs`, `rel/vm.args`, and the empty directory `rel/plugins`.

   `rel/vm.args` is used for [runtime configuration](https://hexdocs.pm/distillery/config/runtime.html#option-2-vmargs) by default, but we're going to use the [Mix Config Provider](https://hexdocs.pm/distillery/config/runtime.html#mix-config-provider) instead so you can delete this file.

### Creating a Mix Config Provider

1. Create a Mix configuration file at `rel/config/config.exs`:

   ```shell
   mkdir -p rel/config
   ```

   Contents of `rel/config/config.exs` :

   ```elixir
   use Mix.Config

   port = String.to_integer(System.get_env("PORT") || "4000")
   default_secret_key_base = :crypto.strong_rand_bytes(43) |> Base.encode64

   config :phoenix_distillery, PhoenixDistilleryWeb.Endpoint,
     http: [port: port],
     url: [host: "localhost", port: port],
     secret_key_base: System.get_env("SECRET_KEY_BASE") || default_secret_key_base
   ```

   This sets up the Mix configuration provider to get values from runtime environment variables.

2. Update `rel/config.exs` to use your new provider. Change the `environment :prod` section in the file to this:

   ```elixir{5-10}
   environment :prod do
     set include_erts: true
     set include_src: false
     set cookie: :"GZUAPxTBG1]F%gaBG6.|Fxqpi^]dVX>:AFn^YxR/RY%KE1ys/l6$cd3}8r4h$B4E"
     set config_providers: [
       {Distillery.Releases.Config.Providers.Elixir, ["${RELEASE_ROOT_DIR}/etc/config.exs"]}
     ]
     set overlays: [
       {:copy, "rel/config/config.exs", "etc/config.exs"}
     ]
   end
   ```

### Configuring Ecto

Let's configure Ecto to get the `DATABASE_URL` from the environment. Change `lib/phoenix_distillery/repo.ex` so it looks like this:

    ```elixir{4-9}
    defmodule PhoenixDistillery.Repo do
      use Ecto.Repo,
        otp_app: :phoenix_distillery,
        adapter: Ecto.Adapters.Postgres,
        pool_size: 10

      def init(_type, config) do
        {:ok, Keyword.put(config, :url, System.get_env("DATABASE_URL"))}
      end
    end
    ```

    This way Ecto gets database connection information from *runtime* environment variables.

## Build a Release with Distillery

You're now ready to build and run your first release!

```shell
npm run deploy --prefix assets && MIX_ENV=prod mix do phx.digest, distillery.release --env=prod
```

The output should look like this:

```bash
==> Assembling release..
==> Building release phoenix_distillery:0.1.0 using environment prod
==> Including ERTS 10.4.4 from /usr/local/Cellar/erlang/22.0.7/lib/erlang/erts-10.4.4
==> Packaging release..
Release successfully built!
To start the release you have built, you can use one of the following tasks:

# start a shell, like 'iex -S mix'
> _build/prod/rel/phoenix_distillery/bin/phoenix_distillery console

# start in the foreground, like 'mix run --no-halt'
> _build/prod/rel/phoenix_distillery/bin/phoenix_distillery foreground

# start in the background, must be stopped with the 'stop' command
> _build/prod/rel/phoenix_distillery/bin/phoenix_distillery start

If you started a release elsewhere, and wish to connect to it:

# connects a local shell to the running node
> _build/prod/rel/phoenix_distillery/bin/phoenix_distillery remote_console

# connects directly to the running node's console
> _build/prod/rel/phoenix_distillery/bin/phoenix_distillery attach

For a complete listing of commands and their use:

> _build/prod/rel/phoenix_distillery/bin/phoenix_distillery help
```

You can now test your release (assuming PostgreSQL is up on your local machine):

```shell{outputLines:3-4}
export DATABASE_URL=postgresql://username:password@127.0.0.1:5432/phoenix_distillery
_build/prod/rel/phoenix_distillery/bin/phoenix_distillery foreground

12:00:00.123 [info] Running PhoenixDistilleryWeb.Endpoint with cowboy 2.6.1 at http://localhost:4000
```

You can now deploy your app in production! 🎉

## Deploying to Render

1. Create a build script called `build.sh` at the root of your repo:

   ```bash
   #!/usr/bin/env bash
   # exit on error
   set -o errexit

   export MIX_ENV=prod

   # get app name and version from mix.exs
   export APP_NAME="$(grep 'app:' mix.exs | sed -e 's/\[//g' -e 's/ //g' -e 's/app://' -e 's/[:,]//g')"
   export APP_VSN="$(grep 'version:' mix.exs | cut -d '"' -f2)"

   # remove existing builds
   rm -rf "_build"

   # Compile app and assets
   mix deps.get --only prod
   mix compile
   cd assets && npm install && npm run deploy && cd ..

   # create release
   # we don't need to create a tarball because the app will be
   # served directly from the build directory
   mix do phx.digest, distillery.release --env=prod --no-tar

   echo "Linking release $APP_NAME:$APP_VSN to _render/"

   ln -sf "_build/$MIX_ENV/rel/$APP_NAME" _render
   ```

   Make the script executable before checking it into Git:

   ```shell
   chmod a+x build.sh
   ```

2. [Create](https://dashboard.render.com/new/database) a new PostgreSQL database on Render.

3. Create a new *Web Service* on Render, and give Render permission to access your new repo.

4. Use the following values during creation:

   |                   |                                               |
   | ----------------- | --------------------------------------------- |
   | *Language*      | `Elixir`                                      |
   | *Build Command* | `./build.sh`                                  |
   | *Start Command* | `./_render/bin/phoenix_distillery foreground` |

   Also add these environment variables to the web service:

| Key | Value |
| --- | --- |
| `SECRET_KEY_BASE` | A sufficiently strong secret. You can generate a secret locally by running `mix phx.gen.secret` |
| `DATABASE_URL` | The internal database URL of the database you created above. |

Going forward, every push to your repo will automatically build your app and deploy it in production. If the build fails, Render will automatically stop the deploy process and the existing version of your app will keep running until the next successful deploy.

Read about [customizing Elixir and Erlang versions](elixir-erlang-versions) for your app.