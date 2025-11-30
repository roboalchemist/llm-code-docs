# Source: https://www.electronjs.org/docs/latest/tutorial/application-distribution

On this page

# Application Packaging

To distribute your app with Electron, you need to package and rebrand it. To do this, you can either use specialized tooling or manual approaches.

## With tooling[â€‹](#with-tooling "Direct link to With tooling") 

There are a couple tools out there that exist to package and distribute your Electron app. We recommend using [Electron Forge](/docs/latest/tutorial/forge-overview). You can check out its [documentation](https://www.electronforge.io) directly, or refer to the [Packaging and Distribution](/docs/latest/tutorial/tutorial-packaging) part of the Electron tutorial.

## Manual packaging[â€‹](#manual-packaging "Direct link to Manual packaging") 

If you prefer the manual approach, there are 2 ways to distribute your application:

- With prebuilt binaries
- With an app source code archive

### With prebuilt binaries[â€‹](#with-prebuilt-binaries "Direct link to With prebuilt binaries") 

To distribute your app manually, you need to download Electron\'s [prebuilt binaries](https://github.com/electron/electron/releases). Next, the folder containing your app should be named `app` and placed in Electron\'s resources directory as shown in the following examples.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The location of Electron\'s prebuilt binaries is indicated with `electron/` in the examples below.

macOS

``` 
electron/Electron.app/Contents/Resources/app/
âââ package.json
âââ main.js
âââ index.html
```

Windows and Linux

``` 
electron/resources/app
âââ package.json
âââ main.js
âââ index.html
```

Then execute `Electron.app` on macOS, `electron` on Linux, or `electron.exe` on Windows, and Electron will start as your app. The `electron` directory will then be your distribution to deliver to users.

### With an app source code archive (asar)[â€‹](#with-an-app-source-code-archive-asar "Direct link to With an app source code archive (asar)") 

Instead of shipping your app by copying all of its source files, you can package your app into an [asar](https://github.com/electron/asar) archive to improve the performance of reading files on platforms like Windows, if you are not already using a bundler such as Parcel or Webpack.

To use an `asar` archive to replace the `app` folder, you need to rename the archive to `app.asar`, and put it under Electron\'s resources directory like below, and Electron will then try to read the archive and start from it.

macOS

``` 
electron/Electron.app/Contents/Resources/
âââ app.asar
```

Windows

``` 
electron/resources/
âââ app.asar
```

You can find more details on how to use `asar` in the [`electron/asar` repository](https://github.com/electron/asar).

### Rebranding with downloaded binaries[â€‹](#rebranding-with-downloaded-binaries "Direct link to Rebranding with downloaded binaries") 

After bundling your app into Electron, you will want to rebrand Electron before distributing it to users.

- **Windows:** You can rename `electron.exe` to any name you like, and edit its icon and other information with tools like [rcedit](https://github.com/electron/rcedit).

- **Linux:** You can rename the `electron` executable to any name you like.

- **macOS:** You can rename `Electron.app` to any name you want, and you also have to rename the `CFBundleDisplayName`, `CFBundleIdentifier` and `CFBundleName` fields in the following files:

  - `Electron.app/Contents/Info.plist`
  - `Electron.app/Contents/Frameworks/Electron Helper.app/Contents/Info.plist`

  You can also rename the helper app to avoid showing `Electron Helper` in the Activity Monitor, but make sure you have renamed the helper app\'s executable file\'s name.

  The structure of a renamed app would be like:

``` 
MyApp.app/Contents
âââ Info.plist
âââ MacOS/
â   âââ MyApp
âââ Frameworks/
    âââ MyApp Helper.app
        âââ Info.plist
        âââ MacOS/
            âââ MyApp Helper
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

it is also possible to rebrand Electron by changing the product name and building it from source. To do this you need to set the build argument corresponding to the product name (`electron_product_name = "YourProductName"`) in the `args.gn` file and rebuild.

Keep in mind this is not recommended as setting up the environment to compile from source is not trivial and takes significant time.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/application-distribution.md)