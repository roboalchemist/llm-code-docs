# Source: https://nitro.build/raw/deploy/providers/iis.md

# IIS

> Deploy Nitro apps to IIS.

## Using [IISnode](https://github.com/Azure/iisnode)

**Preset:** `iis_node`

<steps level="4">

#### Install the latest LTS version of [Node.js](https://nodejs.org/en/) on your Windows Server

#### Install [IISnode](https://github.com/azure/iisnode/releases)

#### Install [IIS `URLRewrite` Module](https://www.iis.net/downloads/microsoft/url-rewrite)

#### In IIS, add `.mjs` as a new mime type and set its content type to `application/javascript`

#### Deploy the contents of your `.output` folder to your website in IIS

</steps>

## Using IIS handler

**Preset:** `iis_handler` / `iis`

You can use IIS http handler directly.

<steps level="4">

#### Install the latest LTS version of [Node.js](https://nodejs.org/en/) on your Windows Server

#### Install [IIS `HttpPlatformHandler` Module](https://www.iis.net/downloads/microsoft/httpplatformhandler)

#### Copy your `.output` directory into the Windows Server, and create a website on IIS pointing to that exact directory

</steps>

## IIS config options

<code-group>

```ts [nitro.config.ts]
export default defineNitroConfig({
  // IIS options default
  iis: {
    // merges in a pre-existing web.config file to the nitro default file
    mergeConfig: true,
    // overrides the default nitro web.config file all together
    overrideConfig: false,
  },
});
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    // IIS options default
    iis: {
      // merges in a pre-existing web.config file to the nitro default file
      mergeConfig: true,
      // overrides the default nitro web.config file all together
      overrideConfig: false,
    },
  },
});
```

</code-group>
