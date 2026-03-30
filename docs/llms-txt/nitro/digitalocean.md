# Source: https://nitro.build/raw/deploy/providers/digitalocean.md

# DigitalOcean

> Deploy Nitro apps to DigitalOcean.

**Preset:** `digital_ocean`

<read-more title="Digital Ocean App Platform" to="https://docs.digitalocean.com/products/app-platform/">

</read-more>

## Set up application

<steps level="4">

#### Create a new Digital Ocean app following the [guide](https://docs.digitalocean.com/products/app-platform/how-to/create-apps/)

#### Next, you'll need to configure environment variables. In your app settings, ensure the following app-level environment variables are set:```bash

NITRO_PRESET=digital_ocean

```

<br />[More information](https://docs.digitalocean.com/products/app-platform/how-to/use-environment-variables/).

#### You will need to ensure you set an `engines.node` field in your app's `package.json` to ensure Digital Ocean uses a supported version of Node.js:```json
{
   "engines": {
      "node": "16.x"
   }
}
```

<br />[See more information](https://docs.digitalocean.com/products/app-platform/languages-frameworks/nodejs/#node-version).

#### You'll also need to add a run command so Digital Ocean knows what command to run after a build. You can do so by adding a start script to your `package.json`:```json

{
   "scripts": {
      "start": "node .output/server/index.mjs"
   }
}

```



#### Finally, you'll need to add this start script to your Digital Ocean app's run command. Go to `Components > Settings > Commands`, click "Edit", then add `npm run start`

</steps>

Your app should be live at a Digital Ocean generated URL and you can now follow [the rest of the Digital Ocean deployment guide](https://docs.digitalocean.com/products/app-platform/how-to/manage-deployments/).
