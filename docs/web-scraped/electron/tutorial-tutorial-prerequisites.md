# Source: https://www.electronjs.org/docs/latest/tutorial/tutorial-prerequisites

On this page

# Prerequisites

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]Follow along the tutorial

This is **part 1** of the Electron tutorial.

1.  **[Prerequisites](/docs/latest/tutorial/tutorial-prerequisites)**
2.  [Building your First App](/docs/latest/tutorial/tutorial-first-app)
3.  [Using Preload Scripts](/docs/latest/tutorial/tutorial-preload)
4.  [Adding Features](/docs/latest/tutorial/tutorial-adding-features)
5.  [Packaging Your Application](/docs/latest/tutorial/tutorial-packaging)
6.  [Publishing and Updating](/docs/latest/tutorial/tutorial-publishing-updating)

Electron is a framework for building desktop applications using JavaScript, HTML, and CSS. By embedding [Chromium](https://www.chromium.org/) and [Node.js](https://nodejs.org/) into a single binary file, Electron allows you to create cross-platform apps that work on Windows, macOS, and Linux with a single JavaScript codebase.

This tutorial will guide you through the process of developing a desktop application with Electron and distributing it to end users.

## Goals[â€‹](#goals "Direct link to Goals") 

This tutorial starts by guiding you through the process of piecing together a minimal Electron application from scratch, then teaches you how to package and distribute it to users using Electron Forge.

If you prefer to get a project started with a single-command boilerplate, we recommend you start with Electron Forge\'s [`create-electron-app`](https://www.electronforge.io/) command.

## Assumptions[â€‹](#assumptions "Direct link to Assumptions") 

Electron is a native wrapper layer for web apps and is run in a Node.js environment. Therefore, this tutorial assumes you are generally familiar with Node and front-end web development basics. If you need to do some background reading before continuing, we recommend the following resources:

- [Getting started with the Web (MDN Web Docs)](https://developer.mozilla.org/en-US/docs/Learn/)
- [Introduction to Node.js](https://nodejs.dev/en/learn/)

## Required tools[â€‹](#required-tools "Direct link to Required tools") 

### Code editor[â€‹](#code-editor "Direct link to Code editor") 

You will need a text editor to write your code. We recommend using [Visual Studio Code](https://code.visualstudio.com/), although you can choose whichever one you prefer.

### Command line[â€‹](#command-line "Direct link to Command line") 

Throughout the tutorial, we will ask you to use various command-line interfaces (CLIs). You can type these commands into your system\'s default terminal:

- Windows: Command Prompt or PowerShell
- macOS: Terminal
- Linux: varies depending on distribution (e.g. GNOME Terminal, Konsole)

Most code editors also come with an integrated terminal, which you can also use.

### Git and GitHub[â€‹](#git-and-github "Direct link to Git and GitHub") 

Git is a commonly-used version control system for source code, and GitHub is a collaborative development platform built on top of it. Although neither is strictly necessary to building an Electron application, we will use GitHub releases to set up automatic updates later on in the tutorial. Therefore, we\'ll require you to:

- [Create a GitHub account](https://github.com/join)
- [Install Git](https://github.com/git-guides/install-git)

If you\'re unfamiliar with how Git works, we recommend reading GitHub\'s [Git guides](https://github.com/git-guides/). You can also use the [GitHub Desktop](https://desktop.github.com/) app if you prefer using a visual interface over the command line.

We recommend that you create a local Git repository and publish it to GitHub before starting the tutorial, and commit your code after every step.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]Installing Git via GitHub Desktop

GitHub Desktop will install the latest version of Git on your system if you don\'t already have it installed.

### Node.js and npm[â€‹](#nodejs-and-npm "Direct link to Node.js and npm") 

To begin developing an Electron app, you need to install the [Node.js](https://nodejs.org/en/download/) runtime and its bundled npm package manager onto your system. We recommend that you use the latest long-term support (LTS) version.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

Please install Node.js using pre-built installers for your platform. You may encounter incompatibility issues with different development tools otherwise. If you are using macOS, we recommend using a package manager like [Homebrew](https://brew.sh/) or [nvm](https://github.com/nvm-sh/nvm) to avoid any directory permission issues.

To check that Node.js was installed correctly, you can use the `-v` flag when running the `node` and `npm` commands. These should print out the installed versions.

``` 
$ node -v
v16.14.2
$ npm -v
8.7.0
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]caution

Although you need Node.js installed locally to scaffold an Electron project, Electron **does not use your system\'s Node.js installation to run its code**. Instead, it comes bundled with its own Node.js runtime. This means that your end users do not need to install Node.js themselves as a prerequisite to running your app.

To check which version of Node.js is running in your app, you can access the global [`process.versions`](https://nodejs.org/api/process.html#processversions) variable in the main process or preload script. You can also reference [https://releases.electronjs.org/releases.json](https://releases.electronjs.org/releases.json).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/tutorial-1-prerequisites.md)