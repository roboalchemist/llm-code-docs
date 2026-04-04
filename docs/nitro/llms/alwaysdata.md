# Source: https://nitro.build/raw/deploy/providers/alwaysdata.md

# Alwaysdata

> Deploy Nitro apps to alwaysdata.

**Preset:** `alwaysdata`

<read-more to="https://alwaysdata.com">

</read-more>

## Set up application

### Pre-requisites

<steps level="4">

#### [Register a new profile](https://www.alwaysdata.com/en/register/) on alwaysdata platform if you don't have one

#### Get a free 100Mb plan to host your app

</steps>

<note>

Keep in mind your *account name* will be used to provide you a default URL in the form of `account_name.alwaysdata.net`, so choose it wisely. You can also link your existing domains to your account later or register as many accounts under your profile as you need.

</note>

### Local deployment

<steps level="4">

#### Build your project locally with `npm run build -- preset alwaysdata`

#### [Upload your app](https://help.alwaysdata.com/en/remote-access/) to your account in its own directory (e.g. `$HOME/www/my-app`). You can use any protocol you prefer (SSH/FTP/WebDAV…) to do so

#### On your admin panel, [create a new site](https://admin.alwaysdata.com/site/add/) for your app with the following features:- *Addresses*: `[account_name].alwaysdata.net`

- *Type*: Node.js
- *Command*: `node ./output/server/index.mjs`
- *Working directory*: `www/my-app` (adapt it to your deployment path)
- *Environment*:```ini
NITRO_PRESET=alwaysdata

```
- *Node.js version*: `Default version` is fine; pick no less than `20.0.0` (you can also [set your Node.js version globally](https://help.alwaysdata.com/en/languages/nodejs/configuration/#supported-versions))
- *Hot restart*: `SIGHUP`

<read-more to="https://help.alwaysdata.com/en/languages/nodejs" title="Get more information about alwaysdata Node.js sites type"></read-more>

#### Your app is now live at `http(s)://[account_name].alwaysdata.net`.

</steps>
