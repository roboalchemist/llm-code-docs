# Source: https://www.electronjs.org/docs/latest/development/source-code-directory-structure

On this page

# Source Code Directory Structure

The source code of Electron is separated into a few parts, mostly following Chromium on the separation conventions.

You may need to become familiar with [Chromium\'s multi-process architecture](https://dev.chromium.org/developers/design-documents/multi-process-architecture) to understand the source code better.

## Structure of Source Code[â€‹](#structure-of-source-code "Direct link to Structure of Source Code") 

``` 
Electron
âââ build/ - Build configuration files needed to build with GN.
âââ buildflags/ - Determines the set of features that can be conditionally built.
âââ chromium_src/ - Source code copied from Chromium that isn't part of the content layer.
âââ default_app/ - A default app run when Electron is started without
|                  providing a consumer app.
âââ docs/ - Electron's documentation.
|   âââ api/ - Documentation for Electron's externally-facing modules and APIs.
|   âââ development/ - Documentation to aid in developing for and with Electron.
|   âââ fiddles/ - A set of code snippets one can run in Electron Fiddle.
|   âââ images/ - Images used in documentation.
|   âââ tutorial/ - Tutorial documents for various aspects of Electron.
âââ lib/ - JavaScript/TypeScript source code.
|   âââ browser/ - Main process initialization code.
|   |   âââ api/ - API implementation for main process modules.
|   |   âââ remote/ - Code related to the remote module as it is
|   |                 used in the main process.
|   âââ common/ - Relating to logic needed by both main and renderer processes.
|   |   âââ api/ - API implementation for modules that can be used in
|   |              both the main and renderer processes
|   âââ isolated_renderer/ - Handles creation of isolated renderer processes when
|   |                        contextIsolation is enabled.
|   âââ renderer/ - Renderer process initialization code.
|   |   âââ api/ - API implementation for renderer process modules.
|   |   âââ extension/ - Code related to use of Chrome Extensions
|   |   |                in Electron's renderer process.
|   |   âââ remote/ - Logic that handles use of the remote module in
|   |   |             the main process.
|   |   âââ web-view/ - Logic that handles the use of webviews in the
|   |                   renderer process.
|   âââ sandboxed_renderer/ - Logic that handles creation of sandboxed renderer
|   |   |                     processes.
|   |   âââ api/ - API implementation for sandboxed renderer processes.
|   âââ worker/ - Logic that handles proper functionality of Node.js
|                 environments in Web Workers.
âââ patches/ - Patches applied on top of Electron's core dependencies
|   |          in order to handle differences between our use cases and
|   |          default functionality.
|   âââ boringssl/ - Patches applied to Google's fork of OpenSSL, BoringSSL.
|   âââ chromium/ - Patches applied to Chromium.
|   âââ node/ - Patches applied on top of Node.js.
|   âââ v8/ - Patches applied on top of Google's V8 engine.
âââ shell/ - C++ source code.
|   âââ app/ - System entry code.
|   âââ browser/ - The frontend including the main window, UI, and all of the
|   |   |          main process things. This talks to the renderer to manage web
|   |   |          pages.
|   |   âââ ui/ - Implementation of UI stuff for different platforms.
|   |   |   âââ cocoa/ - Cocoa specific source code.
|   |   |   âââ win/ - Windows GUI specific source code.
|   |   |   âââ x/ - X11 specific source code.
|   |   âââ api/ - The implementation of the main process APIs.
|   |   âââ net/ - Network related code.
|   |   âââ mac/ - Mac specific Objective-C source code.
|   |   âââ resources/ - Icons, platform-dependent files, etc.
|   âââ renderer/ - Code that runs in renderer process.
|   |   âââ api/ - The implementation of renderer process APIs.
|   âââ common/ - Code that used by both the main and renderer processes,
|       |         including some utility functions and code to integrate node's
|       |         message loop into Chromium's message loop.
|       âââ api/ - The implementation of common APIs, and foundations of
|                  Electron's built-in modules.
âââ spec/ - Components of Electron's test suite run in the main process.
âââ BUILD.gn - Building rules of Electron.
```

## Structure of Other Directories[â€‹](#structure-of-other-directories "Direct link to Structure of Other Directories") 

- **.github** - GitHub-specific config files including issues templates, CI with GitHub Actions and CODEOWNERS.
- **dist** - Temporary directory created by `script/create-dist.py` script when creating a distribution.
- **node_modules** - Third party node modules used for building.
- **npm** - Logic for installation of Electron via npm.
- **out** - Temporary output directory of `ninja`.
- **script** - Scripts used for development purpose like building, packaging, testing, etc.

``` 
script/ - The set of all scripts Electron runs for a variety of purposes.
âââ codesign/ - Fakes codesigning for Electron apps; used for testing.
âââ lib/ - Miscellaneous python utility scripts.
âââ release/ - Scripts run during Electron's release process.
    âââ notes/ - Generates release notes for new Electron versions.
    âââ uploaders/ - Uploads various release-related files during release.
```

- **typings** - TypeScript typings for Electron\'s internal code.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/development/source-code-directory-structure.md)