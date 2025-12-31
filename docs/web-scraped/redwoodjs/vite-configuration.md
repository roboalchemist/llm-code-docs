# Source: https://docs.redwoodjs.com/docs/vite-configuration

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Vite Configuration]

[Version: 8.8]

On this page

<div>

# Vite Configuration

</div>

Redwood uses Vite. One of Redwood\'s tenets is convention over configuration.

Vite is an awesome build tool, but we don\'t want it to be something that you have to be familiar with to be productive. So it\'s worth repeating that you don\'t have to do any of this, because we configure everything you will need out of the box with a Redwood Vite plugin.

Regardless, there\'ll probably come a time when you have to configure Vite. All the Vite configuration for your web side sits in `web/vite.config.ts`, and can be configured the same as any other Vite project. Let\'s take a peek!

``` 
import dns from 'dns'
import  from 'vite'
import redwood from '@redwoodjs/vite'

dns.setDefaultResultOrder('verbatim')

const viteConfig = 
export default defineConfig(viteConfig)
```

Checkout Vite\'s docs on [configuration](https://vitejs.dev/config/)

### Sass and Tailwind CSS[​](#sass-and-tailwind-css "Direct link to Sass and Tailwind CSS") 

Redwood is already configured to use Sass, if the packages are there:

``` 
yarn workspace web add -D sass sass-loader
```

And if you want to use Tailwind CSS, just run the setup command:

``` 
yarn rw setup ui tailwindcss
```

## Vite Dev Server[​](#vite-dev-server "Direct link to Vite Dev Server") 

Redwood uses Vite\'s preview server for local development. When you run `yarn rw dev`, keys in your `redwood.toml`\'s `[web]` table---like `port` and `apiUrl`---are used as vite preview server options (in this case, [preview.port](https://vitejs.dev/config/preview-options.html#preview-port) and [preview.proxy](https://vitejs.dev/config/preview-options.html#preview-proxy) respectively).

> You can peek at all the out-of-the-box configuration for your Vite preview server in the [RedwoodJS Vite plugin](https://github.com/redwoodjs/redwood/blob/main/packages/vite/src/index.ts)

### Using `--forward`[​](#using---forward "Direct link to using---forward") 

While you can configure Vite using `web/vite.config.js`, it\'s often simpler to use `yarn rw dev`\'s `--forward` option.

For example, if you want to force optimise your Vite dependencies again, you can run:

``` 
yarn rw dev --fwd="--force"
```

You can also use `--forward` to override keys in your `redwood.toml`. For example, the following starts your app on port `1234` and disables automatic browser opening:

``` 
yarn rw dev --forward="--port 1234 --no-open"
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/vite-configuration.md)