# Source: https://docs.hypermode.com/modus/run-locally.md

# Run Locally

> Test your Modus app and iterate quickly

Modus provides a local development environment that makes it easy to build and
test your app, with local access to models.

## Launching your app in development mode

To run your app, from the project root, run:

```sh
modus dev
```

The `modus dev` command compiles your app code, starts a local server, and
provides a URL to access your app's API. It also enables fast refresh, which
automatically recompiles and reloads any changed functions while preserving app
state during development.

Once your app is running, you can access the graphical interface for your API at
the URL located in your terminal.

```sh
View endpoint: http://localhost:8686/explorer
```

The API Explorer interface allows you to interact with your app's API and test
your functions.

<img className="block" src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/api-explorer.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=73a3bc7706024c3369fef94e6a2bc841" alt="API Graphical Interface." width="3022" height="1712" data-path="images/api-explorer.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/api-explorer.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=fd7e86a90a04bb31f2ef58f83d415b92 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/api-explorer.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8697a0f6eb57e84b6652a2b6d353cd40 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/api-explorer.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=89cc21976f39cbbe1bb15a9a647a93eb 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/api-explorer.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=39114adfb890acddea02d2ffeb87f023 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/api-explorer.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=39ca34b2979827b2fc55d256b4c3a40c 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/api-explorer.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4ce090f6b8ea104ed85bbb0c93713ce7 2500w" data-optimize="true" data-opv="2" />

## Environment secrets

When you run your app locally using `modus dev`, the runtime replaces the
placeholders of the manifest with values from environment variables defined in
your operating system or in `.env` files.

The environment variables keys must be upper case and follow the naming
convention:

`MODUS_<CONNECTION NAME>_<PLACEHOLDER>`

For example, with the following manifest:

```json modus.json
{
  "connections": {
    "openai": {
      "type": "http",
      "baseUrl": "https://api.openai.com/",
      "headers": {
        "Authorization": "Bearer {{API_KEY}}"
      }
    }
  }
}
```

The Modus runtime substitutes `{{API_KEY}}` with the value of the environment
variable `MODUS_OPENAI_API_KEY`

An easy way to define the environment variables when working locally is to use
the file `.env.dev.local` located in your app folder.

For the previous manifest, we can set the key in the .env.dev.local file as
follow:

```text .env.dev.local
MODUS_OPENAI_API_KEY="your openai key"
```

<Warning>
  You should exclude `.env` files from source control. Projects created with
  `modus new` exclude these files automatically when creating your project.
</Warning>

## Using Hypermode-hosted models

To use Hypermode-hosted models in your local environment, first install the Hyp
CLI:

```sh
npm install -g @hypermode/hyp-cli
```

Then log in to your Hypermode account:

```sh
hyp login
```

After logging in, your app automatically connects to Hypermode's
[Model Router](/model-router) when running locally.
