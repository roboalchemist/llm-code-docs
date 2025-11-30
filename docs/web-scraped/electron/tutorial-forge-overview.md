# Source: https://www.electronjs.org/docs/latest/tutorial/forge-overview

On this page

# Distributing Apps With Electron Forge

Electron Forge is a tool for packaging and publishing Electron applications. It unifies Electron\'s build tooling ecosystem into a single extensible interface so that anyone can jump right into making Electron apps.

Alternative tooling

If you do not want to use Electron Forge for your project, there are other third-party tools you can use to distribute your app.

These tools are maintained by members of the Electron community, and do not come with official support from the Electron project.

**Electron Builder**

A \"complete solution to package and build a ready-for-distribution Electron app\" that focuses on an integrated experience. [`electron-builder`](https://github.com/electron-userland/electron-builder) adds a single dependency and manages all further requirements internally.

`electron-builder` replaces features and modules used by the Electron maintainers (such as the auto-updater) with custom ones.

**Hydraulic Conveyor**

A [desktop app deployment tool](https://hydraulic.dev) that supports cross-building/signing of all packages from any OS without the need for multi-platform CI, can do synchronous web-style updates on each start of the app, requires no code changes, can use plain HTTP servers for updates and which focuses on ease of use. Conveyor replaces the Electron auto-updaters with Sparkle on macOS, MSIX on Windows, and Linux package repositories.

Conveyor is a commercial tool that is free for open source projects. There\'s an example of [how to package GitHub Desktop](https://hydraulic.dev/blog/8-packaging-electron-apps.html) which can be used for learning.

## Getting started[â€‹](#getting-started "Direct link to Getting started") 

The [Electron Forge docs](https://www.electronforge.io/) contain detailed information on taking your application from source code to your end users\' machines. This includes:

- Packaging your application [(package)](https://www.electronforge.io/cli#package)
- Generating executables and installers for each OS [(make)](https://www.electronforge.io/cli#make), and,
- Publishing these files to online platforms to download [(publish)](https://www.electronforge.io/cli#publish).

For beginners, we recommend following through Electron\'s [tutorial](/docs/latest/tutorial/tutorial-prerequisites) to develop, build, package and publish your first Electron app. If you have already developed an app on your machine and want to start on packaging and distribution, start from [step 5](/docs/latest/tutorial/tutorial-packaging) of the tutorial.

## Getting help[â€‹](#getting-help "Direct link to Getting help") 

- If you need help with developing your app, our [community Discord server](https://discord.gg/APGC3k5yaH) is a great place to get advice from other Electron app developers.
- If you suspect you\'re running into a bug with Forge, please check the [GitHub issue tracker](https://github.com/electron/forge/issues) to see if any existing issues match your problem. If not, feel free to fill out our bug report template and submit a new issue.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/forge-overview.md)