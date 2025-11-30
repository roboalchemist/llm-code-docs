# Source: https://www.electronjs.org/docs/latest/tutorial/updates

On this page

# Updating Applications

There are several ways to provide automatic updates to your Electron application. The easiest and officially supported one is taking advantage of the built-in [Squirrel](https://github.com/Squirrel) framework and Electron\'s [autoUpdater](/docs/latest/api/auto-updater) module.

## Using cloud object storage (serverless)[â€‹](#using-cloud-object-storage-serverless "Direct link to Using cloud object storage (serverless)") 

For a simple serverless update flow, Electron\'s autoUpdater module can check if updates are available by pointing to a static storage URL containing latest release metadata.

When a new release is available, this metadata needs to be published to cloud storage alongside the release itself. The metadata format is different for macOS and Windows.

### Publishing release metadata[â€‹](#publishing-release-metadata "Direct link to Publishing release metadata") 

With Electron Forge, you can set up static file storage updates by publishing metadata artifacts from the ZIP Maker (macOS) with `macUpdateManifestBaseUrl` and the Squirrel.Windows Maker (Windows) with `remoteReleases`.

See Forge\'s [Auto updating from S3](https://www.electronforge.io/config/publishers/s3#auto-updating-from-s3) guide for an end-to-end example.

Manual publishing

On macOS, Squirrel.Mac can receive updates by reading a `releases.json` file with the following JSON format:

releases.json

``` 

    },
    
    }
  ]
}
```

On Windows, Squirrel.Windows can receive updates by reading from the RELEASES file generated during the build process. This file details the `.nupkg` delta package to update to.

RELEASES

``` 
B0892F3C7AC91D72A6271FF36905FEF8FE993520 electron-fiddle-0.36.3-full.nupkg 103298365
```

These files should live in the same directory as your release, under a folder structure that is aware of your app\'s platform and architecture.

For example:

``` 
my-app-updates/
ââ darwin/
â  ââ x64/
â  â  ââ my-app-1.0.0-darwin-x64.zip
â  â  ââ my-app-1.1.0-darwin-x64.zip
â  â  ââ RELEASES.json
â  ââ arm64/
â  â  ââ my-app-1.0.0-darwin-arm64.zip
â  â  ââ my-app-1.1.0-darwin-arm64.zip
â  â  ââ RELEASES.json
ââ win32/
â  ââ x64/
â  â  ââ my-app-1.0.0-win32-x64.exe
â  â  ââ my-app-1.0.0-win32-x64.nupkg
â  â  ââ my-app-1.1.0-win32-x64.exe
â  â  ââ my-app-1.1.0-win32-x64.nupkg
â  â  ââ RELEASES
```

### Reading release metadata[â€‹](#reading-release-metadata "Direct link to Reading release metadata") 

The easiest way to consume metadata is by installing [update-electron-app](https://github.com/electron/update-electron-app), a drop-in Node.js module that sets up autoUpdater and prompts the user with a native dialog.

For static storage updates, point the `updateSource.baseUrl` parameter to the directory containing your release metadata files.

main.js

``` 
const  = require('update-electron-app')

updateElectronApp(/$`
  }
})
```

## Using update.electronjs.org[â€‹](#using-updateelectronjsorg "Direct link to Using update.electronjs.org") 

The Electron team maintains [update.electronjs.org](https://github.com/electron/update.electronjs.org), a free and open-source webservice that Electron apps can use to self-update. The service is designed for Electron apps that meet the following criteria:

- App runs on macOS or Windows
- App has a public GitHub repository
- Builds are published to [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release)
- Builds are [code-signed](/docs/latest/tutorial/code-signing) **(macOS only)**

The easiest way to use this service is by installing [update-electron-app](https://github.com/electron/update-electron-app), a Node.js module preconfigured for use with update.electronjs.org.

Install the module using your Node.js package manager of choice:

- npm
- Yarn

``` 
npm install update-electron-app
```

``` 
yarn add update-electron-app
```

Then, invoke the updater from your app\'s main process file:

main.js

``` 
require('update-electron-app')()
```

By default, this module will check for updates at app startup, then every ten minutes. When an update is found, it will automatically be downloaded in the background. When the download completes, a dialog is displayed allowing the user to restart the app.

If you need to customize your configuration, you can [pass options to update-electron-app](https://github.com/electron/update-electron-app) or [use the update service directly](https://github.com/electron/update.electronjs.org).

## Using other update services[â€‹](#using-other-update-services "Direct link to Using other update services") 

If you\'re developing a private Electron application, or if you\'re not publishing releases to GitHub Releases, it may be necessary to run your own update server.

### Step 1: Deploying an update server[â€‹](#step-1-deploying-an-update-server "Direct link to Step 1: Deploying an update server") 

Depending on your needs, you can choose from one of these:

- [Hazel](https://github.com/vercel/hazel) â€" Update server for private or open-source apps which can be deployed for free on [Vercel](https://vercel.com). It pulls from [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) and leverages the power of GitHub\'s CDN.
- [Nuts](https://github.com/GitbookIO/nuts) â€" Also uses [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release), but caches app updates on disk and supports private repositories.
- [electron-release-server](https://github.com/ArekSredzki/electron-release-server) â€" Provides a dashboard for handling releases and does not require releases to originate on GitHub.
- [Nucleus](https://github.com/atlassian/nucleus) â€" A complete update server for Electron apps maintained by Atlassian. Supports multiple applications and channels; uses a static file store to minify server cost.

Once you\'ve deployed your update server, you can instrument your app code to receive and apply the updates with Electron\'s [autoUpdater](/docs/latest/api/auto-updater) module.

### Step 2: Receiving updates in your app[â€‹](#step-2-receiving-updates-in-your-app "Direct link to Step 2: Receiving updates in your app") 

First, import the required modules in your main process code. The following code might vary for different server software, but it works like described when using [Hazel](https://github.com/vercel/hazel).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]Check your execution environment!

Please ensure that the code below will only be executed in your packaged app, and not in development. You can use the [app.isPackaged](/docs/latest/api/app#appispackaged-readonly) API to check the environment.

main.js

``` 
const  = require('electron')
```

Next, construct the URL of the update server feed and tell [autoUpdater](/docs/latest/api/auto-updater) about it:

main.js

``` 
const server = 'https://your-deployment-url.com'
const url = `$/update/$/$`

autoUpdater.setFeedURL()
```

As the final step, check for updates. The example below will check every minute:

main.js

``` 
setInterval(() => , 60000)
```

Once your application is [packaged](/docs/latest/tutorial/application-distribution), it will receive an update for each new [GitHub Release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) that you publish.

### Step 3: Notifying users when updates are available[â€‹](#step-3-notifying-users-when-updates-are-available "Direct link to Step 3: Notifying users when updates are available") 

Now that you\'ve configured the basic update mechanism for your application, you need to ensure that the user will get notified when there\'s an update. This can be achieved using the [autoUpdater API events](/docs/latest/api/auto-updater#events):

main.js

``` 
autoUpdater.on('update-downloaded', (event, releaseNotes, releaseName) => 

  dialog.showMessageBox(dialogOpts).then((returnValue) => )
})
```

Also make sure that errors are [being handled](/docs/latest/api/auto-updater#event-error). Here\'s an example for logging them to `stderr`:

main.js

``` 
autoUpdater.on('error', (message) => )
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]Handling updates manually

Because the requests made by autoUpdate aren\'t under your direct control, you may find situations that are difficult to handle (such as if the update server is behind authentication). The `url` field supports the `file://` protocol, which means that with some effort, you can sidestep the server-communication aspect of the process by loading your update from a local directory. [Here\'s an example of how this could work](https://github.com/electron/electron/issues/5020#issuecomment-477636990).

## Update server specification[â€‹](#update-server-specification "Direct link to Update server specification") 

For advanced deployment needs, you can also roll out your own Squirrel-compatible update server. For example, you may want to have percentage-based rollouts, distribute your app through separate release channels, or put your update server behind an authentication check.

Squirrel.Windows and Squirrel.Mac clients require different response formats, but you can use a single server for both platforms by sending requests to different endpoints depending on the value of `process.platform`.

main.js

``` 
const  = require('electron')

const server = 'https://your-deployment-url.com'
// e.g. for Windows and app version 1.2.3
// https://your-deployment-url.com/update/win32/1.2.3
const url = `$/update/$/$`

autoUpdater.setFeedURL()
```

### Windows[â€‹](#windows "Direct link to Windows") 

A Squirrel.Windows client expects the update server to return the `RELEASES` artifact of the latest available build at the `/RELEASES` subpath of your endpoint.

For example, if your feed URL is `https://your-deployment-url.com/update/win32/1.2.3`, then the `https://your-deployment-url.com/update/win32/1.2.3/RELEASES` endpoint should return the contents of the `RELEASES` artifact of the version you want to serve.

https://your-deployment-url.com/update/win32/1.2.3/RELEASES

``` 
B0892F3C7AC91D72A6271FF36905FEF8FE993520 https://your-static.storage/your-app-1.2.3-full.nupkg 103298365
```

Squirrel.Windows does the comparison check to see if the current app should update to the version returned in `RELEASES`, so you should return a response even when no update is available.

### macOS[â€‹](#macos "Direct link to macOS") 

When an update is available, the Squirrel.Mac client expects a JSON response at the feed URL\'s endpoint. This object has a mandatory `url` property that maps to a ZIP archive of the app update. All other properties in the object are optional.

https://your-deployment-url.com/update/darwin/0.31.0

``` 

```

If no update is available, the server should return a [`204 No Content`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204) HTTP response.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/updates.md)