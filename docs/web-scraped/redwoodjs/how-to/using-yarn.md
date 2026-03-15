# Source: https://docs.redwoodjs.com/docs/how-to/using-yarn

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Using Yarn]

[Version: 8.8]

On this page

<div>

# Using Yarn

</div>

## What is Yarn?[​](#what-is-yarn "Direct link to What is Yarn?") 

[Yarn](https://yarnpkg.com/) is a package manager for JavaScript. It is used to manage and install dependencies for JavaScript projects, particularly for Node.js applications. Yarn offers features like parallel package installations and offline caching and uses a `yarn.lock` file to control and reproduce consistent installations of dependencies across different environments.

## Installing yarn[​](#installing-yarn "Direct link to Installing yarn") 

> \"The preferred way to manage Yarn is through [Corepack](https://nodejs.org/dist/latest/docs/api/corepack.html), a new binary shipped with all Node.js releases starting from 16.10.\"\
> -[from the Yarn documentation](https://yarnpkg.com/getting-started/install)

Corepack is included with all Node.js \>=16.10 installs, but you must opt-in. To enable it, run the following command:

``` 
corepack enable
```

## Using the correct version of yarn[​](#using-the-correct-version-of-yarn "Direct link to Using the correct version of yarn") 

To see the version of yarn that you have installed, run the following command:

``` 
yarn --version
```

**Redwood requires Yarn (\>=1.22.21)**

You can upgrade yarn by running the following command:

``` 
corepack prepare yarn@stable --activate
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

If this command fails, you may need to [uninstall the current version of Yarn first](#uninstalling-yarn).

``` 
corepack disable
npm uninstall -g yarn --force
corepack enable
```

## Installing packages and dependencies with yarn[​](#installing-packages-and-dependencies-with-yarn "Direct link to Installing packages and dependencies with yarn") 

You\'ll need to run `yarn install` in the root of your project directory to install all the necessary packages and dependencies for your project.

Redwood separates the backend (`api`) and frontend (`web`) concerns into their own paths in the codebase. ([Yarn refers to these as \"workspaces\"](https://yarnpkg.com/features/workspaces). In Redwood, we refer to them as \"sides.\") When you add packages going forward you\'ll need to specify which workspace they should go in.

For example to install a package on the `web` or **frontend** side, you would run the following command:

``` 
yarn workspace web add package-name
```

and to install a package on the `api` or **backend** side, you would run the following command:

``` 
yarn workspace api add package-name
```

## Uninstalling yarn[​](#uninstalling-yarn "Direct link to Uninstalling yarn") 

To uninstall yarn, run the following command:

``` 
corepack disable
npm uninstall -g yarn --force
```

## Additional Information[​](#additional-information "Direct link to Additional Information") 

For additional information, you can refer directly to the [yarn documentation](https://yarnpkg.com/).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/using-yarn.md)